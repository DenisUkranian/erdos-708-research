#!/usr/bin/env python3
"""Sound universal 12-slot certificate from disjoint unit-valuation prime groups.

All `p > sqrt(M)` in the prime list are automatically disjoint and
of unit valuation in every source, since each source is <= M.
See NEW_LEMMA_EN.md for the exact proof and inherited small-case assumptions.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product
from math import isqrt, prod
from typing import Sequence

UPPER = {0:0, 1:1, 2:2, 3:4, 4:5, 5:6, 6:8, 7:9, 8:11}

def primes_of(n):
    factors=[]
    p=2
    while p*p<=n:
        if n%p==0:
            factors.append(p)
            while n%p==0:n//=p
        p=3 if p==2 else p+2
    if n>1:factors.append(n)
    return factors

def certify(A: Sequence[int], prime_set=None):
    if len(A)!=9 or len(set(A))!=9 or min(A)<2:
        raise ValueError('Nine distinct sources >=2 required')
    M=max(A)
    if prime_set is None:
        prime_set=sorted({p for a in A for p in primes_of(a) if p>=13 and p*p>M})
    else:
        prime_set=sorted(set(prime_set))
    if any(p<13 or p not in primes_of(p) for p in prime_set):
        raise ValueError('Primes >=13 required')
    groups=[]
    for p in prime_set:
        g=[a for a in A if a%p==0]
        if not g: continue
        if any(a%(p*p)==0 for a in g):
            raise ValueError('Chosen prime occurs to exponent >=2')
        groups.append((p,g))
    used=[a for p,g in groups for a in g]
    if len(used)!=len(set(used)):
        raise ValueError('A source belongs to two chosen prime groups')
    m=len(used)
    if not 1<=m<=9:return None
    f=UPPER[9-m]
    s=12-f-m
    if s<0:return None
    slot_numbers=list(range(f+m+1,f+m+s+1))
    caps=[M//j for j in slot_numbers]

    def pack(rem):
        rem=tuple(sorted(rem,reverse=True))
        @lru_cache(None)
        def dfs(i,bins):
            if i==len(rem):return bins
            u=rem[i]
            for k in range(s):
                if bins[k] <= caps[k]//u:
                    nb=bins[:k]+(bins[k]*u,)+bins[k+1:]
                    res=dfs(i+1,nb)
                    if res is not None:return res
            return None
        return dfs(0,(1,)*s)

    for chosen in product(*(g for p,g in groups)):
        rem=[]
        for (p,g),anchor in zip(groups,chosen):
            rem.extend(a//p for a in g if a!=anchor)
        bins=pack(rem)
        if bins is None: continue
        assert prod(rem)==prod(bins)
        assert all(j*h<=M for j,h in zip(slot_numbers,bins))
        return {
            'M':M,
            'groups':[{'p':p,'source_count':len(g),'anchor':a,'remaining_cofactors':[b//p for b in g if b!=a]}
                      for (p,g),a in zip(groups,chosen)],
            'other_sources_upper':f,
            'count_of_prime_group_sources':m,
            'bundle_products':list(bins),
            'bundle_slots':slot_numbers,
            'total_budget':f+m+s,
        }
    return None

if __name__=='__main__':
    import argparse,json
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('A',nargs=9,type=int)
    parser.add_argument('--primes',nargs='*',type=int)
    args=parser.parse_args()
    print(json.dumps(certify(args.A, args.primes or None), indent=2))
