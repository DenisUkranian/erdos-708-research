#!/usr/bin/env python3
"""Finite level-by-level checks for the screened cofactor construction.

The sampled sizes, band endpoints and palette probabilities are finite test parameters.
No sampled frequency is used as an asymptotic bound. Standard library only.
"""
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import cache
from itertools import combinations
from math import gcd, lcm, prod
from random import Random


@cache
def factors(a):
    result = {}
    d = 2
    while d * d <= a:
        while a % d == 0:
            result[d] = result.get(d, 0) + 1
            a //= d
        d += 1
    if a > 1:
        result[a] = 1
    return result


def levels(h):
    return [p**j for p, e in factors(h).items() for j in range(1, e + 1)]


def balanced(a):
    pair = [1, 1]
    for q in sorted((p**e for p, e in factors(a).items()), reverse=True):
        side = int(pair[1] < pair[0])
        pair[side] *= q
    assert prod(pair) == a and gcd(*pair) == 1
    return pair


@dataclass(frozen=True)
class Task:
    row: int
    label: int
    kind: str


def tasks_for(a, parts):
    assert prod(h for h, _ in parts) == a and gcd(*(h for h, _ in parts)) == 1
    return [Task(a, h, kind if len(factors(h)) >= 2 else "single")
            for h, kind in parts if h > 1]


def extract(rows, threshold):
    initial = {a: balanced(a) for a in rows}
    candidates = set()
    for pair in initial.values():
        for h in pair:
            atoms = [p**e for p, e in factors(h).items()]
            if len(atoms) >= 2:
                divisors = {1}
                for q in atoms:
                    divisors |= {v*q for v in divisors}
                candidates.update(divisors - {1})
    remaining = set(rows)
    tasks = []
    heavy = []
    for d in sorted(candidates):
        group = sorted(a for a in remaining if a % d == 0 and gcd(d, a//d) == 1)
        if d*len(group) < threshold:
            continue
        heavy.append(d)
        for a in group:
            tasks.extend(tasks_for(a, [(d, "B"), (a//d, "C")]))
        remaining.difference_update(group)
    for a in sorted(remaining):
        tasks.extend(tasks_for(a, [(h, "B") for h in initial[a]]))
    return tasks, heavy


@dataclass(frozen=True)
class Bands:
    core: tuple
    low: tuple
    high_start: int
    width: int

    def bin(self, p):
        if p in self.core:
            return None
        if p < self.high_start:
            return ("low", next(i for i, band in enumerate(self.low) if p in band))
        return ("high", (p-self.high_start)//self.width)

    @cache
    def screened(self, record):
        result = set(self.core)
        for kind, i in record:
            if kind == "low":
                result.update(self.low[i])
            else:
                left = self.high_start + i*self.width
                result.update(p for p in range(left, left+self.width)
                              if factors(p) == {p: 1})
        return result

    @cache
    def split(self, h):
        occupied = defaultdict(list)
        for p in factors(h):
            band = self.bin(p)
            if band is not None:
                occupied[band].append(p)
        high = [key for key in occupied if key[0] == "high"]
        g = h
        if high and len(occupied[max(high)]) == 1:
            p, = occupied.pop(max(high))
            g //= p**factors(h)[p]
        return tuple(sorted(occupied)), g


def exact_list(t, role, record, bands, offset, size):
    forbidden = bands.screened(record) if role != "B" else set()
    return [b for b in range((offset//t+1)*t, offset+size+1, t)
            if (role == "R" or gcd(t, b//t) == 1)
            and all((b//t) % p for p in forbidden)]


def keys(tasks, bands):
    result = {("B", ())}
    for t in tasks:
        if t.kind == "C":
            record, _ = bands.split(t.label)
            result.update((("C", record), ("R", record)))
    return sorted(result)


def lists_and_colors(tasks, bands, offset, size, rng, forced):
    ids_by_label = defaultdict(list)
    reserves = {}
    types = keys(tasks, bands)
    for i,t in enumerate(tasks):
        if t.kind == "single":
            continue
        record, g = bands.split(t.label) if t.kind == "C" else ((), 1)
        ids_by_label[t.kind, record, t.label].append(i)
        if g > 1:
            reserves[record,g] = exact_list(g, "R", record, bands, offset, size)
    uncolored = {(role,rec,h):exact_list(h,role,rec,bands,offset,size)
                 for role,rec,h in ids_by_label}
    forced_colors = {}
    for i,b in forced.items():
        task = tasks[i]
        rec = bands.split(task.label)[0] if task.kind == "C" else ()
        assert b in uncolored[task.kind, rec, task.label]
        assert forced_colors.setdefault(b,(task.kind,rec)) == (task.kind,rec)
    # Finite uniform palette probabilities. Resample until the needed C lists
    # have capacity. The proof uses size-dependent nonuniform probabilities.
    for _ in range(200):
        colors = [rng.choice(types) for _ in range(size)]
        for b,key in forced_colors.items():
            colors[b-offset-1] = key
        def belongs(b, role, rec):
            return colors[b-offset-1] == (role,rec)
        placements = dict(forced)
        trim = set()
        for (role,rec,h), ids in ids_by_label.items():
            bank = [b for b in uncolored[role,rec,h] if belongs(b,role,rec)]
            prescribed = {forced[i] for i in ids if i in forced}
            assert len(prescribed) == sum(i in forced for i in ids)
            others = [i for i in ids if i not in forced]
            free = [b for b in bank if b not in prescribed]
            rng.shuffle(free)
            placements.update(zip(others,free))
            trim.update(others[len(free):])
        if any(tasks[i].kind == "C" for i in trim):
            continue
        restoration = {(rec,g):[b for b in bs if belongs(b,"R",rec)]
                       for (rec,g), bs in reserves.items()}
        # This finite stronger test prepares for all potential restoration
        # requests before the placements are examined.
        demand = Counter((bands.split(t.label)) for t in tasks if t.kind == "C")
        if any(len(bs) < demand[key] for key,bs in restoration.items()):
            continue
        return placements, trim, restoration
    raise AssertionError("finite parameters did not yield sufficient dedicated capacities")


def independent_matching(requests, banks):
    match = {}
    def augment(i, seen):
        for b in banks[requests[i]]:
            if b in seen:
                continue
            seen.add(b)
            if b not in match or augment(match[b], seen):
                match[b] = i
                return True
        return False
    assert all(augment(i,set()) for i in range(len(requests)))
    assert len(match) == len(requests)
    return match


def verify(rows, tasks, offset, size, bands, rng, forced=None):
    assert len(rows) == len(set(rows)) and max(rows) <= size
    placed, trim, banks = lists_and_colors(tasks,bands,offset,size,rng,forced or {})
    assert set(placed).isdisjoint(trim) and all(tasks[i].kind == "B" for i in trim)
    assert set(placed)|trim == {i for i,t in enumerate(tasks) if t.kind != "single"}
    count = Counter()
    original = Counter(q for a in rows for q in levels(a))
    assert original == Counter(q for t in tasks for q in levels(t.label))
    at = defaultdict(list)
    for i,b in placed.items():
        at[b].append(i)
    marked = set()
    for site in at.values():
        assert len({tasks[i].kind for i in site}) == 1
        assert len({tasks[i].label for i in site}) == len(site)
        if tasks[site[0]].kind == "B":
            for i,j in combinations(site,2):
                h,k = tasks[i].label,tasks[j].label
                if gcd(h,k)>1:
                    assert lcm(h,k)<=size
                    marked.update((i,j))
                    count["bad_main_pairs"] += 1
    selected, credited, requests = set(), Counter(), []
    for b,site in at.items():
        good = [tasks[i] for i in site if i not in marked]
        if not good:
            continue
        selected.add(b)
        local = []
        for j,t in enumerate(good):
            h = t.label
            if t.kind == "C":
                record,g = bands.split(h)
                assert (record,g) == bands.split(good[0].label)
                if j:
                    h //= g
                    if g > 1:
                        requests.append((record,g))
                        count["composite_reserves"] += int(len(factors(g)) > 1)
                        count["below_2n_multiples"] += int(size//g < 2*len(rows))
            local.extend(levels(h))
        assert len(local) == len(set(local)) and all(b % q == 0 for q in local)
        credited.update(local)
    # Bank disjointness is checked globally, including across different g
    # with the same retained record. Check every reserve candidate physically.
    occupied = set(at)
    for (rec,g), bank in banks.items():
        assert not occupied.intersection(bank)
        assert all(b % g == 0 and all((b//g)%p for p in bands.screened(rec)) for b in bank)
        occupied.update(bank)
    witness = independent_matching(requests,banks)
    assert all(b in banks[requests[i]] for b,i in witness.items())
    for key, amount in Counter(requests).items():
        reserve_points = banks[key][:amount]
        assert len(reserve_points) == amount and not selected.intersection(reserve_points)
        selected.update(reserve_points)
        for _ in reserve_points:
            credited.update(levels(key[1]))
    assert len(selected) <= len(placed)-len(marked)
    deferred = [t.label for i,t in enumerate(tasks) if t.kind == "single" or i in marked|trim]
    assert credited + Counter(q for h in deferred for q in levels(h)) == original

    before = len(selected)
    per_prime = defaultdict(list)
    for q in original:
        p, = factors(q)
        per_prime[p].append(q)
    for p, pp in per_prime.items():
        deficit = max(original[q] - sum(b%q==0 for b in selected) for q in pp)
        if deficit>0:
            available = [b for b in range((offset//p+1)*p, offset+size+1,p)
                         if b not in selected]
            pp.sort(reverse=True)
            available.sort(key=lambda b:next((q for q in pp if b%q==0),1), reverse=True)
            assert len(available)>=deficit
            selected.update(available[:deficit])
    assert len(selected)-before <= sum(len(factors(h)) for h in deferred)
    assert all(sum(b%q==0 for b in selected)>=d for q,d in original.items())
    assert len(selected) <= 2*len(rows)+sum(len(factors(tasks[i].label))-1 for i in trim|marked)
    count.update(cases=1, rows=len(rows), levels=len(original), positions=len(selected),
                 main_trim=len(trim), main_marked=len(marked))
    return count


def fixture(records, additional, size, offset, spec, rng):
    rows, tasks, fixed = [], [], {}
    for root,h,kind,b in records:
        rows.append(root*h)
        tasks.extend(tasks_for(root*h, [(root,"B"),(h,kind)]))
        fixed[len(tasks)-1] = b
    for a in additional:
        rows.append(a)
        tasks.extend(tasks_for(a, [(1,"B"),(a,"B")]))
    return verify(rows,tasks,offset,size,spec,rng,fixed)


def audit_uncolored_lists(spec, offsets):
    # Test the exactness implication on all mixed h up to 196, independently
    # of the color assignment and the source extraction.
    events = 0
    for offset in offsets:
        by_site = defaultdict(list)
        for h in range(2,197):
            if len(factors(h)) < 2:
                continue
            record,g = spec.split(h)
            assert spec.screened(record).issuperset(factors(g))
            for b in exact_list(h,"C",record,spec,offset,700):
                by_site[record,b].append((h,g))
        for occupants in by_site.values():
            for (h,g),(k,f) in combinations(occupants,2):
                assert g == f and gcd(h//g,k//f) == 1
                events += 1
        low = spec.split(2*7)[0]
        assert low == spec.split(2*7**2)[0]
        assert not set(exact_list(2*7,"C",low,spec,offset,700)).intersection(
            exact_list(2*7**2,"C",low,spec,offset,700))
    assert events > 0
    return events


def main():
    rng = Random(708)
    spec = Bands((2,),((3,5),),7,2)
    wide = Bands((2,),((3,5),),7,6)
    assert wide.split(2*13*17**2)[1] == 2*13*17**2  # two bases in largest high bin
    assert wide.split(2*13**2*23)[1] == 2*13**2       # one largest high base
    assert wide.split(2*3*5)[1] == 2*3*5              # low bins are always retained
    # Prescribe unrelated prime-power classes by CRT.
    crt, modulus = 0, 1
    for d,r in [(2**8,-13),(3**6,-13),(5**4,-63),(7**4,-644),(11**3,-644)]:
        crt += modulus*((r-crt)*pow(modulus,-1,d)%d)
        modulus *= d
    total = Counter()
    heavy = 0
    for size,n,threshold in [(12000,26,15),(18000,35,24),(24000,50,32)]:
        rows = [30*p for p in (7,11,13,17,19,23,29,31)] + Random(n).sample(range(2,180),n-8)
        tasks, groups = extract(rows,threshold)
        assert any(t.kind=="C" for t in tasks)
        for offset in (0,1,437,crt,lcm(*range(1,65))):
            for bands in (spec,wide):
                total.update(verify(rows,tasks,offset,size,bands,rng))
                heavy += len(groups)
    # Two labels carry g=22 with shared prime 11. This was a bad long pair
    # in the earlier cutoff-only construction; the retained bin now pays it.
    offset, size = 140800, 1200
    short = next(b for b in range(offset+1,offset+size+1)
                 if b%42==0 and gcd(b//6,6)==gcd(b//14,14)==1)
    records = [(5,6*17,"C",141474),(5,6*19,"C",141474),
               (3,2*11*13,"C",140998),(3,2*11*17,"C",140998),
               (13,6,"B",short),(19,14,"B",short)]
    force = fixture(records,[],size,offset,spec,rng)
    assert force["composite_reserves"]==2 and force["main_marked"]==2
    # 6 and 18 share exactly the same record. Their private banks must be
    # disjoint by 3-adic exponent. A third bank restores 10.
    rec = [(5,6*17,"C",1938),(5,6*19,"C",1938),(5,18*17,"C",5814),
           (5,18*19,"C",5814),(7,10*17,"C",3910),(7,10*23,"C",3910)]
    overlapping_records = fixture(rec,[],10000,0,spec,rng)
    assert spec.split(6*17)[0]==spec.split(18*17)[0]
    assert overlapping_records["composite_reserves"]==3
    # Both residuals in the high tail are distinct. The restored core is
    # large enough that fewer than 2n multiples even exist in the prefix.
    g = 6*11*13
    site = g*17*19
    rec = [(5,g*17,"C",site),(5,g*19,"C",site)]
    extras = [p for p in range(31,500) if factors(p)=={p:1}][:60]
    large = fixture(rec,extras,83000,site-80,spec,rng)
    assert large["below_2n_multiples"]==1
    # A physical tied-high-bin label retains both 13 and 17, even though
    # a numerical prime power at the smaller base might be larger.
    tied = fixture([(3,2*13*17,"C",2*13*17*19)],[],2500,8000,wide,rng)
    print("Uncolored pair overlaps checked:",audit_uncolored_lists(wide,[0,crt]))
    print("Generated cases:",dict(total),"heavy groups across cases:",heavy)
    print("Forced composites and bad main collision:",dict(force))
    print("Common record and unequal cores:",dict(overlapping_records))
    print("Core with fewer than 2n multiples:",dict(large))
    print("Tied largest high bin:",dict(tied))
    print("PASS: dedicated restoration and every original prime-power level verified.")


if __name__ == "__main__":
    main()
