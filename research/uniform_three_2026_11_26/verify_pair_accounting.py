"""Finite replays of the matching, pair credit, and nested repair."""
from collections import Counter, defaultdict
from itertools import combinations, product
from math import gcd, lcm, prod
from random import Random


def factor(a):
    factors = {}
    p = 2
    while p * p <= a:
        if a % p == 0:
            exponent = 0
            while a % p == 0:
                a //= p
                exponent += 1
            factors[p] = exponent
        p += 1
    if a > 1:
        factors[a] = 1
    return factors


def point_checks():
    pairs = [(2, 3), (5, 7), (11, 13)]
    count = 0
    for states in product(range(4), repeat=len(pairs)):
        for on_anchor in (False, True):
            anchor = set()
            for pair, state in zip(pairs, states):
                if state & 1:
                    anchor.add(pair[0])
                if state & 2:
                    anchor.add(pair[1])
            if on_anchor and any(set(pair) <= anchor for pair in pairs):
                continue
            old = anchor if on_anchor else set()
            missed = sum(len(set(pair) & old) for pair in pairs)
            assert int(not on_anchor) + missed <= len(pairs)
            count += 1
    return count


def replay(start, sources, seed):
    rng = Random(seed)
    size = max(sources)
    factors = {a: factor(a) for a in sources}
    anchor_bank = {}
    labels = {}
    regular = 0
    for a in sources:
        ps = sorted(factors[a])
        if len(ps) < 4:
            continue
        r, p, q = ps[-3:]
        powers = [t ** factors[a][t] for t in (r, p, q)]
        d = a // prod(powers[1:])
        # epsilon=1/2 in this finite replay
        if size**2 < d**2 * r**5:
            pair = sorted(powers)[:2]
            assert all(factor(t) == {t: 1} for t in pair)
            v = prod(pair)
            assert all(v*v <= size*t for t in pair)
            labels[a] = v
            d //= powers[0]
        else:
            regular += 1
        anchor_bank[a] = d
    def bank(d):
        return range((start // d + 1)*d, start + size + 1, d)

    owner = {}
    def augment(a, seen):
        for b in bank(anchor_bank[a]):
            if b in seen:
                continue
            seen.add(b)
            if b not in owner or augment(owner[b], seen):
                owner[b] = a
                return True
        return False
    for a in sorted(anchor_bank, key=anchor_bank.get, reverse=True):
        assert augment(a, set())
    account = {b: set(factor(anchor_bank[a])) for b, a in owner.items()}
    selected = set(owner)
    assigned = defaultdict(list)
    credits = 0
    # Force use of old representatives when eligible; exercise all bank types.
    for a, v in labels.items():
        allowed = [b for b in bank(v) if not set(factor(v)) <= account.get(b, set())]
        assert allowed
        at_anchor = [b for b in allowed if b in selected]
        b = rng.choice(at_anchor or allowed)
        assigned[b].append((a, v))

    discarded = set()
    for b, group in assigned.items():
        for (a, v), (a2, w) in combinations(group, 2):
            if gcd(v, w) > 1:
                discarded.update((a, a2))
        live = [(a, v) for a, v in group if a not in discarded]
        if live:
            selected.add(b)
            credits += len(live)

    required = Counter()
    for fs in factors.values():
        for p, e in fs.items():
            for j in range(1, e+1):
                required[p**j] += 1
    # Simultaneous nested-level repair, evaluated against the actual integers.
    for p in sorted(set().union(*factors.values())):
        powers = [p**j for j in range(1, max(fs.get(p, 0) for fs in factors.values())+1)]
        for power in reversed(powers):
            missing = required[power] - sum(b % power == 0 for b in selected)
            if missing > 0:
                available = (b for b in bank(power) if b not in selected)
                selected.update(next(available) for _ in range(missing))
    assert all(sum(b % power == 0 for b in selected) >= count
               for power, count in required.items())
    assert len(selected) <= 3*len(sources) + len(discarded)
    return regular, len(labels), credits, len(selected)


if __name__ == '__main__':
    print('Local credit configurations checked:', point_checks())
    size = 65536
    sources = {size}
    for r, p, q in combinations((5, 7, 11, 13, 17, 19, 23, 29, 31), 3):
        for exponent in (1, 2):
            a = 2*r**exponent*p*q
            if a <= size:
                while 2*a <= size:
                    a *= 2
                sources.add(a)
    center = lcm(*sources)
    for seed, start in enumerate((0, 987654321, center-size//2, center+101)):
        print('ordinary, exceptional, surviving pairs, selected:',
              replay(start, sorted(sources), seed))
