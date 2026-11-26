"""Fully enumerate small rank-three two-block examples, and exact dual banks."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import prod

from cuts import factors


def placements(rows,x):
    m = max(rows)
    ps = sorted(set().union(*(factors(a) for a in rows)))
    assert all(all(p % d for d in range(2,int(p**.5)+1)) for p in ps)  # squarefree examples
    profiles = defaultdict(list)
    for b in range(x+1,x+m+1):
        sig = sum(1<<i for i,p in enumerate(ps) if b%p==0)
        if sig:
            profiles[sig].append(b)
    demand = [sum(a%p==0 for a in rows) for p in ps]
    fullsites = [range((x//a+1)*a,x+m+1,a) for a in rows]
    def price(sites):
        hosts = set(sites)
        return len(hosts)+sum(sum(a%p==0 for a,b in zip(rows,sites) if b==h)-1
                              for h in hosts for p in ps if any(a%p==0 and b==h for a,b in zip(rows,sites)))
    fixed = min(price(t) for t in product(*fullsites))
    # Equal signatures are interchangeable. Use sorted combinations with bounded repetition.
    pool = [s for s in profiles for _ in profiles[s][:len(rows)]]
    def profile_sets(k, lower, prefix):
        if k==0:
            yield prefix
            return
        for i in range(lower,len(pool)-k+1):
            if i>lower and pool[i]==pool[i-1]:
                continue
            yield from profile_sets(k-1,i+1,prefix+(pool[i],))
    first = None
    for k in range(max(demand),len(rows)+2):
        for sigs in profile_sets(k,0,()):
            if any(sum(bool(s>>i&1) for s in sigs)<v for i,v in enumerate(demand)):
                continue
            if first is None:
                first=k
            taken = Counter()
            sites = []
            for s in sigs:
                sites.append(profiles[s][taken[s]])
                taken[s]+=1
            def assign(i,unused):
                if i==len(rows):
                    return []
                atoms=factors(rows[i])
                for choice in product(*(range(k) for _ in atoms)):
                    if len(set(choice))>2:
                        continue
                    slots={(index,p) for p,index in zip(atoms,choice)}
                    if slots<=unused:
                        suffix=assign(i+1,unused-slots)
                        if suffix is not None:
                            blocks=[(prod(p for p,j in zip(atoms,choice) if j==index),sites[index])
                                    for index in sorted(set(choice))]
                            return [blocks]+suffix
                return None
            allslots={(j,p) for j,b in enumerate(sites) for p in ps if b%p==0}
            solution=assign(0,allslots)
            if solution is not None:
                assert first==k  # lower bound on every certificate is H
                assert all(prod(d for d,b in plan)==a and all(b%d==0 for d,b in plan)
                           for plan,a in zip(solution,rows))
                print(f'rows={rows} x={x} H=joint={k} fixed-full={fixed} splits={solution}')
                return
    raise AssertionError('missing placement')


def banks():
    for m in (96,257,1024,4096):
        for active in ((5,11,29),(7,11,13),(11,13,17,19)):
            assert sum(Fraction(1,p) for p in active)<=Fraction(1,3)
            demands=Counter()
            for a in range(1,m+1):
                qpart=prod(p**sum(a % p**e==0 for e in range(1,m.bit_length()))
                           for p in active)
                if qpart>1:
                    p=max(p for p in active if qpart%p==0)
                    demands[qpart//p]+=1
            for x in (0,1234567,prod(active)**3-m//2):
                used=set()
                for h,need in demands.items():
                    points=[b for b in range((x//h+1)*h,x+m+1,h)
                            if all((b//h)%p for p in active if p*h<=m)]
                    assert len(points)>=need and not (used & set(points))
                    used.update(points)
        print(f'exact price banks M={m}, 3 supports and 3 shifts: passed')


def normal_order():
    u,h=5003,30720
    primes=[p for p in range(2,u+1) if all(p%d for d in range(2,int(p**.5)+1))]
    assert primes[-1]==u and factors(h)==[2048,3,5]
    nheavy=sum(p>2048 for p in primes)
    c=Fraction(u*4,15)-8
    assert c/2>=nheavy+1
    light=[p for p in primes if p>2]
    lower=min((Fraction(h*u,2*p)*Fraction(p-1,2*p)-4)/(2*len(light)) for p in light)
    assert lower>=2
    print(f'marking U={u} heavy demand={nheavy}, guaranteed capacity={c/2}; '
          f'light supports={len(light)}, min guaranteed capacity={lower}')


def union_fibers():
    m=3000
    for ds in [(6,10),(18,30,45),(34,51,85,119)]:
        def count(x):
            hits=[False]+[any((x+i)%d==0 for d in ds) for i in range(1,m+1)]
            totals=[0]*(m+1)
            for q in range(1,m+1):
                start=(-x-1)%q+1
                totals[q]=sum(hits[start::q])
            return totals
        source=count(0)
        for x in (0,1,559849,232792560-m//2):
            target=count(x)
            assert target[1]-source[1]<=2**(len(ds)-1)
            assert max(a-b for a,b in zip(source[1:],target[1:]))<=2**(len(ds)-1)-1
        print(f'union of progressions {ds} M={m} canonical size={source[1]} counts passed')


if __name__=='__main__':
    placements((30,42,70,105),157)
    placements((30,42,70,105),831)
    banks()
    union_fibers()
    normal_order()
