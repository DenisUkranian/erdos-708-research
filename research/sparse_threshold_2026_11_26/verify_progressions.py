#!/usr/bin/env python3
"""Finite arithmetic checks for the exceptional-primary construction; standard library only."""
from collections import Counter
from math import gcd, lcm, prod

STEP = 5040
SIEVE = (2, 3, 5, 7, 11, 13)


def factors(a):
    f = {}
    p = 2
    while p*p <= a:
        while a % p == 0:
            a //= p
            f[p] = f.get(p, 0) + 1
        p += 1
    if a > 1:
        f[a] = 1
    return f


def levels(a):
    return [p**k for p,e in factors(a).items() for k in range(1,e+1)]


def progression_checks():
    # Record a common v, common q, one low band containing 11,13, and a
    # small screened segment through 7. All recorded h are distinct.
    v, q = 2*3*11, 53
    hs = [v*p*q for p in (17,19,23,29,31,37,41,43,47)]
    screening_product = prod(SIEVE)
    residues = {}
    for p in SIEVE:
        residues[p] = {(-i*STEP) % p for i in range(7)}
        assert len(residues[p]) == (1 if p<=7 else 7)
    # Exact number of forbidden simultaneous classes for squarefree moduli.
    # Here each indicated prime must divide at least one of the seven forms.
    for primes in [(),(2,3,7),(5,11),(11,13),(2,11,13)]:
        d = prod(primes)
        actual = sum(all(x%p in residues[p] for p in primes) for x in range(d))
        assert actual == prod(len(residues[p]) for p in primes)
    count = pair_count = 0
    for origin in (0, 83, prod(SIEVE)**3 + 108):
        represented, sites = {}, set()
        # One real mask window, large enough for each whole seven-point bank.
        last = origin + (6*STEP+950)*max(hs)
        for h in hs:
            lo = origin//h+1
            starts = []
            for x in range(lo,lo+950):
                direct = all(gcd(x+i*STEP,screening_product)==1 for i in range(7))
                modular = all(x%p not in residues[p] for p in SIEVE)
                assert direct == modular
                if direct:
                    starts.append(x)
            assert starts
            for x in starts:
                points = [h*(x+i*STEP) for i in range(7)]
                assert origin < points[0] <= points[-1] <= last
                assert all(b%h==0 and gcd(b//h,screening_product)==1 for b in points)
                count += 1
            pts = [h*(starts[0]+i*STEP) for i in range(7)]
            sites.update(pts)
            a,b = pts[0],pts[6]
            assert a+b == 2*pts[3] and a+2*b == 3*pts[4]
            assert b-a == 6*STEP*h
            represented[h] = (a,b)
        assert len({b-a for a,b in represented.values()}) == len(hs)
        for coord,scale in [(lambda a,b:a,1),(lambda a,b:b,1),
                            (lambda a,b:a+b,2),(lambda a,b:a+2*b,3)]:
            assert {coord(a,b) for a,b in represented.values()} <= {scale*s for s in sites}
        # Check local overlapping block bookkeeping for this physical sample.
        for K in {1<<(h.bit_length()-1) for h in hs}:
            B = 20*STEP*K
            chosen = {h:ab for h,ab in represented.items() if K<=h<2*K}
            witnesses = Counter()
            for a,b in chosen.values():
                assert b-a < B
                j = a//B
                assert j*B <= a <= b < (j+2)*B
                witnesses[j] += 1
            for j,m in witnesses.items():
                local = sum(j*B <= s < (j+2)*B for s in sites)
                assert m**4 <= local**7
            contrib = Counter()
            for s in sites:
                for j in (s//B-1,s//B):
                    assert j*B<=s<(j+2)*B
                    contrib[s] += 1
            assert max(contrib.values())==2
        pair_count += len(represented)
    return count, pair_count


def first_multiple(x,t):
    return (x+t-1)//t*t


def physical(duplicate, collide):
    # In this deliberately short primary window the hub is the only candidate.
    # The anchor must take smallest q: p of the second and third labels is
    # the q of the preceding one. All three screened parts equal 2^2*3.
    v = 12
    data = [(29,13,17),(29,17,19),(29,19,23)]
    if duplicate:
        data += [(31,13,17)]
    hs = [v*p*q for _,p,q in data]
    rows = [d*h for (d,_,_),h in zip(data,hs)]
    assert len(rows) == len(set(rows))
    assert all(gcd(d,h)==1 for (d,_,_),h in zip(data,hs))
    # The ambient M and two disjoint target windows are actual integers.
    M = max(rows)
    hub = v*13*17*19*23
    origin,end = hub-1, hub-1+M
    reserve = (hub+1, hub+1+15000-1)
    assert reserve[1] <= end
    roots = {d for d,_,_ in data}
    W = min(d*sum(r==d for r,_,_ in data) for d in roots)
    n = len(rows)
    possible = {t for h in hs for t in range(1,h+1) if h%t==0}
    for t in possible:
        actual = sum(h%t==0 for h in hs)
        rows_bound = sum(M//(d*t) for d in roots)
        assert actual <= rows_bound and rows_bound*W*t <= n*M
    # Register each q once at each primary site. Screen for exact small part.
    # The real protocol permits the residual p or q to divide b/h again.
    registrations, accepted, failed = set(), [], []
    for i,((_,p,q),h) in enumerate(zip(data,hs)):
        candidates = [hub] if hub%h==0 and gcd(hub//h,2*3*5*7*11)==1 else []
        assert candidates
        if (hub,v,q) in registrations:
            failed.append(i)
            assert all((b,v,q) in registrations for b in candidates)
        else:
            accepted.append(i)
            registrations.add((hub,v,q))
    for _,v0,q in registrations:
        assert sum(1 for _,vv,qq in registrations if (vv,qq)==(v0,q))*v0*q*W <= n*M
    assert len(failed) == int(duplicate)
    anchor = min(accepted, key=lambda i: data[i][2])
    qs = [data[i][2] for i in accepted]
    assert data[anchor][1] < min(qs) and data[max(accepted,key=lambda i:data[i][2])][1] in qs
    at_hub = levels(v)+[data[anchor][1]]+qs
    assert len(at_hub)==len(set(at_hub)) and all(hub%t==0 for t in at_hub)
    ds = [v*data[i][1] for i in accepted if i!=anchor]
    assert ds == [204,228]
    l,r = reserve
    assert lcm(*ds)<=r-l+1
    placed = [first_multiple(l,d) for d in ds]
    if collide:
        placed = [first_multiple(l,lcm(*ds))]*len(ds)
    elif len(set(placed))<len(ds):
        placed[-1] += ds[-1]
    assert all(l<=b<=r and b%d==0 for b,d in zip(placed,ds))
    marked = {i for i,b in enumerate(placed) if placed.count(b)>1}
    assert len(marked)==2*int(collide)
    selected, credited = {hub}, Counter(at_hub)
    for i,(d,b) in enumerate(zip(ds,placed)):
        if i not in marked:
            selected.add(b)
            credited.update(levels(d))
    pending = [d for d,_,_ in data]+[hs[i] for i in failed]+[ds[i] for i in marked]
    need = Counter(t for a in rows for t in levels(a))
    assert need == credited + Counter(t for h in pending for t in levels(h))
    before = len(selected)
    # Highest needed levels first; all points are actual, including repairs.
    for p in sorted({p for a in rows for p in factors(a)}):
        pp = sorted((t for t in need if t%p==0),reverse=True)
        for t in pp:
            missing = need[t] - sum(b%t==0 for b in selected)
            if missing>0:
                for b in range(first_multiple(origin+1,t),end+1,t):
                    if b not in selected:
                        selected.add(b)
                        missing -= 1
                        if not missing:
                            break
                assert not missing
    assert len(selected)-before <= sum(len(factors(h)) for h in pending)
    assert all(sum(b%t==0 for b in selected)>=d for t,d in need.items())
    return len(accepted),len(failed),len(marked),len(selected)


if __name__ == "__main__":
    runs, pairs = progression_checks()
    print(f"All seven terms screened in {runs} genuine progressions; {pairs} endpoint pairs verified.")
    for duplicate,collide in ((False,False),(True,False),(True,True)):
        print("accepted, failed, restoration collisions, physical cover size:",physical(duplicate,collide))
    print("PASS: all original prime-power demands met.")
