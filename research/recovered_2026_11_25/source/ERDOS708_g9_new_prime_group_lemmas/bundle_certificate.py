#!/usr/bin/env python3
"""Sound all-shift certificate for nine-source prime groups with unit p-valuations.

Assumes (as external inputs) the established upper bounds
  g(1)<=1, g(2)<=2, g(3)<=4, g(4)<=5, g(5)<=6,
  g(6)<=8, g(7)<=9, g(8)<=11.

Returns a *sufficient* certificate for tau(A,I)<=12 for every interval I
of length M=max(A); a missing certificate is NOT a counterexample.
"""
from functools import lru_cache
from itertools import permutations
from math import isqrt
from typing import Sequence

UPPER = {0:0, 1:1, 2:2, 3:4, 4:5, 5:6, 6:8, 7:9, 8:11}

def certify(A: Sequence[int], p: int):
    if len(A) != 9 or len(set(A)) != 9 or min(A) < 2:
        raise ValueError('A must contain nine distinct integers >=2')
    M = max(A)
    if p < 13 or any(a % (p*p) == 0 for a in A if a%p==0):
        raise ValueError('Requires prime p>=13, with valuation 1 in every p-source')
    # primality check by trial division for independent verifiability
    if any(p % k == 0 for k in range(2,isqrt(p)+1)):
        raise ValueError('p must be prime')
    G = sorted([a for a in A if a % p == 0])
    d = len(G)
    if not 1 <= d <= 8:
        return None
    f = UPPER[9-d]
    s = 12-f-d
    if s < 0:
        return None
    cofactors = [a//p for a in G]
    assert all(u%p!=0 for u in cofactors)
    # Use one complete p-multiple, then (d-1) p-multiples for the
    # p-exponent, then s bundled cofactor products in ordered slots.
    caps = [M//j for j in range(f+d+1, f+d+s+1)]
    for anchor_index in range(d):
        rem = tuple(u for i,u in enumerate(cofactors) if i!=anchor_index)
        # Assign each factor to one of s ordered bins. Unary factors are harmless.
        @lru_cache(maxsize=None)
        def backtrack(i, bins):
            if i == len(rem):
                return bins
            u = rem[i]
            for k in range(s):
                if bins[k] <= caps[k]//u:
                    nb = bins[:k]+(bins[k]*u,)+bins[k+1:]
                    got = backtrack(i+1, nb)
                    if got is not None: return got
            return None
        result = backtrack(0, (1,)*s)
        if result is not None:
            assert len(result)==s
            assert all(j*v<=M for j,v in zip(range(f+d+1,13),result))
            assert __import__('math').prod(result)==__import__('math').prod(rem)
            return {
                'M':M, 'p':p, 'group_size':d, 'other_sources_upper':f,
                'anchor':G[anchor_index], 'p_multiples_added_at_most':d-1,
                'bundle_products':list(result),
                'bundle_slots':list(range(f+d+1, f+d+s+1)),
                'total_budget':f+d+s
            }
    return None

if __name__=='__main__':
    import argparse,json
    pa=argparse.ArgumentParser(description=__doc__)
    pa.add_argument('--p',type=int,required=True)
    pa.add_argument('A',type=int,nargs=9)
    args=pa.parse_args()
    print(json.dumps(certify(args.A,args.p),indent=2))
