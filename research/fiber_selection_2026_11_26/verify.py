"""Exact finite checks for the progression selection and conditional-density arguments."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import gcd, prod

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import maximum_flow


def primes_to(m):
    flags = bytearray(b'\x01') * (m + 1)
    flags[:2] = b'\x00\x00'
    for p in range(2, int(m**0.5) + 1):
        if flags[p]:
            flags[p*p::p] = bytes(len(flags[p*p::p]))
    return [p for p in range(2, m+1) if flags[p]]


def omega_table(m):
    counts = [0]*(m+1)
    for p in primes_to(m):
        for b in range(p, m+1, p):
            counts[b] += 1
    return counts


def union_minimum(rows, m, omega):
    source, targets = 0, 1+len(rows)
    sink = targets+m
    large = m+sum(omega[a] for a in rows)+1
    edges = [(targets+b-1, sink, 1) for b in range(1, m+1)]
    for i,a in enumerate(rows, 1):
        edges.append((source, i, omega[a]))
        edges.extend((i, targets+b-1, large) for b in range(a,m+1,a))
    tails,heads,capacities = zip(*edges)
    graph = coo_matrix((np.array(capacities,dtype=np.int32),(tails,heads)),shape=(sink+1,sink+1)).tocsr()
    return int(maximum_flow(graph,source,sink).flow_value)


def exhaustive_unions():
    cases = 0
    for m in range(2,10):
        omega = omega_table(m)
        banks = [sum(1<<(b-1) for b in range(a,m+1,a)) for a in range(1,m+1)]
        ideals = {0}
        for bank in banks:
            ideals |= {v|bank for v in ideals}
        for mask in range(1<<(m-2)):
            rows = [i for i in range(2,m) if mask>>(i-2)&1]+[m]
            best = min(v.bit_count()+sum(omega[a] for a in rows if not v>>(a-1)&1) for v in ideals)
            assert union_minimum(rows,m,omega)==best
            cases += 1
    print('flow equals exhaustive optimum on',cases,'source sets')


def levels(rows,m):
    return {d:c for p in primes_to(m) for d in powers(p,m)
            if (c:=sum(a%d==0 for a in rows))}


def powers(p,m):
    d=p
    while d<=m:
        yield d
        d*=p


def repaired_cover(rows,m,x,initial):
    required=levels(rows,m)
    chosen=set(initial)
    for p in primes_to(m):
        pp=[d for d in powers(p,m) if d in required]
        missing=max([0]+[required[d]-sum(b%d==0 for b in chosen) for d in pp])
        if missing:
            options=sorted((b for b in range((x//p+1)*p,x+m+1,p) if b not in chosen),
                           key=lambda b: -sum(b%d==0 for d in pp))
            chosen.update(options[:missing])
    # Remove redundant points in a fixed order. Counts stay integral throughout.
    counts={d:sum(b%d==0 for b in chosen) for d in required}
    for b in sorted(chosen):
        hit=[d for d in required if b%d==0]
        if all(counts[d]>required[d] for d in hit):
            chosen.remove(b)
            for d in hit:
                counts[d]-=1
    assert all(x<b<=x+m for b in chosen)
    assert all(sum(b%d==0 for b in chosen)>=c for d,c in required.items())
    return sorted(b-x for b in chosen)


def finite_obstruction():
    m,q,x=3001,5,1000037
    omega=omega_table(m)
    rows=[a for a in range(6,m//3+1,q) if omega[a]>=3]+[m]
    assert gcd(*rows)==1 and all(a%q==1 for a in rows)
    obstruction=sum(min(m//a,q,omega[a]) for a in rows)
    optimum=union_minimum(rows,m,omega)
    start=[b for b in range(x+1,x+m//3+1) if b%q==1]
    witness=repaired_cover(rows,m,x,start)
    assert optimum>=obstruction>2*len(rows)>=len(witness)
    print('finite obstruction M, n, 2n, disjoint-multiple lower, exact union optimum, verified H upper:',
          m,len(rows),2*len(rows),obstruction,optimum,len(witness))
    print('selected offsets:',*witness)


def calibrated_profile():
    m=4095
    x=273491
    primes=[2,3,5]
    caps=[2,1,2]
    def profile(b):
        return tuple(sum(b%p**j==0 for j in range(1,e+1)) for p,e in zip(primes,caps))
    sizes=Counter(profile(b) for b in range(1,m+1))
    rows=[b for b in range(2,m+1) if (sum(profile(b))>=2 and b%7!=1) or b%143==0]
    occupied=Counter(profile(b) for b in rows)
    def f(b):
        cell=profile(b)
        return Fraction(occupied[cell],sizes[cell]) if sizes[cell] else Fraction()
    canonical=[Fraction()]+[f(b) for b in range(1,m+1)]
    target=[Fraction()]+[f(b) for b in range(x+1,x+m+1)]
    assert sum(canonical)==len(rows)
    W=prod(1+2*e for e in caps)
    discrepancy=Fraction()
    for p in primes_to(m):
        for d in powers(p,m):
            a=sum(canonical[d::d])
            b=sum(target[(-x-1)%d+1::d])
            assert abs(a-b)<=W
            discrepancy=max(discrepancy,abs(a-b))
            if p in primes and d<=p**caps[primes.index(p)]:
                assert a==sum(u%d==0 for u in rows)
    print('calibration M, n, max level discrepancy, finite-difference bound:',m,len(rows),discrepancy,W)


def pair_selection():
    primes=(5,7,11,13,17,19)
    m=30030
    labelsets=[tuple(p for p in primes if a%p==0) for a in range(m+1)]
    rows={a for a in range(2,m+1) if (len(labelsets[a])>=2 and a%4!=0) or a%997==0}
    n=len(rows)
    t=Fraction(n,m)
    assert max(rows)==m
    mu=sum(Fraction(1,p) for p in primes)
    hits=sum(len(labelsets[a]) for a in rows)
    u=Fraction(hits,n)
    assert u>1+mu
    pairs=[p*q for p,q in combinations(primes,2)]
    source={d:sum(a%d==0 for a in rows) for d in pairs}
    baseline={d:t*(m//d) for d in pairs}
    actual_pairs=sum(source.values())
    assert Fraction(actual_pairs,n)>=u*(u-1)/2
    assert sum(baseline.values())<=n*mu**2/2
    hot=[d for d in pairs if source[d]>Fraction(33,32)*baseline[d]]
    density_target=Fraction(65,64)*t
    theta=Fraction(1,256)
    # Expected gain conditional on a choice. Later generators occur independently.
    pending=Counter(b for d in hot for b in range(d,m+1,d))
    weights=[(1-theta)**j for j in range(len(hot)+1)]
    def objective(b):
        return int(b in rows)-density_target
    expected=sum(objective(b)*(1-weights[count]) for b,count in pending.items())
    chosen, union=[],set()
    for d in hot:
        bank=range(d,m+1,d)
        for b in bank:
            pending[b]-=1
        gain=sum(objective(b)*weights[pending[b]] for b in bank if b not in union)
        if gain>0:
            chosen.append(d)
            union.update(bank)
    nr=len(rows&union)
    assert nr-density_target*len(union)>=expected>0
    print('pair selection M, n, lifted pairs, chosen pairs, rows in union, canonical union:',
          m,n,len(hot),chosen,nr,len(union))
    print('source density, within-union density:',t,Fraction(nr,len(union)))


def constants_and_powers():
    # Linear in mu after factoring out its nonnegative factor; check the worst endpoint.
    for mass,ell,kappa in [(10,Fraction(30,100),Fraction(1,32)),
                            (11,Fraction(30,100),Fraction(1,32)),
                            (11,Fraction(471,1000),Fraction(1,256))]:
        gap=Fraction(1,2)-ell-kappa*(Fraction(mass,2)+ell)
        assert gap>0
        assert (1-kappa/8)-(1+kappa/2)/(1+kappa)>kappa/4
        print('mass, large-prime bound, pair uplift, surplus coefficient:',mass,ell,kappa,gap)
    m=1260
    labels={4:Fraction(4,5),8:Fraction(1,2),9:Fraction(3,4),5:Fraction(2,3)}
    for a in range(1,m+1):
        hits=[w for d,w in labels.items() if a%d==0]
        joint=sum(x*y for x,y in combinations(hits,2))
        assert 2*joint>=sum(hits)**2-sum(hits)
    for d,e in combinations(labels,2):
        assert sum(b%d==0 and b%e==0 for b in range(1,m+1))==m//(d*e//gcd(d,e))
    print('nested-level intersections and second-moment check passed')


if __name__=='__main__':
    exhaustive_unions()
    finite_obstruction()
    calibrated_profile()
    pair_selection()
    constants_and_powers()
