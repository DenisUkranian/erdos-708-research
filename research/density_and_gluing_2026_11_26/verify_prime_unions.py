"""Exact integer checks for prime-union gluing and flat-plus-anchor certificates."""
from fractions import Fraction
from itertools import combinations
from math import lcm


def primes(m):
    return [p for p in range(2,m+1) if all(p%d for d in range(2,int(p**0.5)+1))]


def powers(p,m):
    d=p
    while d<=m:
        yield d
        d*=p


def weight_test(m):
    ps=primes(m)
    ds={p:list(powers(p,m)) for p in ps}
    mask=[0]+[sum(1<<i for i in range(m) if (i+1)%d==0) for d in range(1,m+1)]
    # Every source subset with maximum m; full level period for the target.
    all_a=list(range(1<<(m-1),1<<m,2))   # exclude source 1
    period=lcm(*range(1,m+1))
    tests=0
    for x in range(period):
        target={d:sum(1<<i for i in range(m) if (x+i+1)%d==0)
                for pp in ds.values() for d in pp}
        ranks={p:sorted((i for i in range(m) if (x+i+1)%p==0),
                        key=lambda i:-sum((x+i+1)%d==0 for d in ds[p])) for p in ps}
        for a in all_a:
            c={d:(a&mask[d]).bit_count() for d in target}
            for v,w in ((1,3),(1,2),(a.bit_count(),m)):
                size={p:max((max(0,w*c[d]-v*(m//d))+(w-v)-1)//(w-v) for d in ds[p]) for p in ps}
                F=0
                for p in ps:
                    assert size[p]<=len(ranks[p])
                    for i in ranks[p][:size[p]]:
                        F|=1<<i
                for d,T in target.items():
                    hits=(F&T).bit_count()
                    assert v*T.bit_count()+(w-v)*hits>=w*c[d]
                    if w*d>v*m:
                        assert hits>=c[d]
                tests+=1
    return tests


def union_test(m):
    ps=primes(m)
    dlist=[(p,d) for p in ps for d in powers(p,m)]
    candidates=[tuple(ps[i] for i in range(len(ps)) if code>>i&1)
                for code in range(1,1<<min(len(ps),8))]
    if len(ps)>8:
        candidates.extend([tuple(ps[-8:]),tuple(ps[::2]),tuple(ps)])
    for P in candidates:
        A=[a for a in range(1,m+1) if any(a%p==0 for p in P)]
        n=len(A)
        mu=sum(Fraction(1,p) for p in P)
        mass=sum(m//p for p in P)
        K=max(m//p for p in P)
        assert n>=mass*(1-mu/2)
        assert K<=n
        for q,d in dlist:
            hits=sum(a%d==0 for a in A)
            if q not in P:
                assert hits<=mu*(m//d) and hits<=Fraction(mass,d)
                assert not hits or d<=K
        if mu>=1:
            # Weighted, exact thinning to reciprocal mass one.
            u={}
            left=Fraction(1)
            for p in P:
                u[p]=min(Fraction(1),left*p)
                left-=u[p]/p
            assert not left
            first=sum(u[p]*(m//p) for p in P)
            second=sum(u[p]*u[q]*(m//(p*q)) for p,q in combinations(P,2))
            assert n>=first-second>=Fraction(m,2)-len(P)
        elif K<m and mass<m-K:
            lam=Fraction(mass,m-K)
            assert all(lam*(m//d)>=Fraction(mass,d) for d in range(1,K+1))
    return len(candidates)


if __name__=='__main__':
    # Through seven, this is exhaustive over both source families and all level shifts.
    counts=[weight_test(m) for m in range(2,8)]
    print('flat-plus-anchor exact family/shift/weight checks M=2..7:',counts,'total',sum(counts))
    tests=[union_test(m) for m in (12,25,48,127,500)]
    print('prime-union generator sets tested:',tests,'total',sum(tests))
