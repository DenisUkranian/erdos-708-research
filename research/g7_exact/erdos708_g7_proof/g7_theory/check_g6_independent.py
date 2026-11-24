#!/usr/bin/env python3
"""Independent exhaustive verification of the reduced six-source finite range.

Does not import the search/Pareto code. Enumerates actual source subsets.
Loads only explicit cumulative-GCD witness lists and checks each from scratch.
"""
from itertools import combinations
from math import gcd, prod
from pathlib import Path
import json
import time

ROOT=Path(__file__).resolve().parent.parent
PRIMES=(2,3,5)


def valuation_vector(a):
    out=[]
    for p in PRIMES:
        count=0
        while a%p==0:
            count+=1
            a//=p
        out.append(count)
    return tuple(out) if a==1 else None


def universal_prime_union(e,m):
    cost=0
    for demand,p in zip(e,PRIMES):
        if demand==0:
            continue
        for k in range(1,9-cost):
            supplied=0
            power=p
            while power<=m:
                supplied+=min(k,m//power)
                power*=p
            if supplied>=demand:
                cost+=k
                break
        else:
            return False
    return True


def ordinary_bins(e,m):
    factors=[p for p,z in reversed(list(zip(PRIMES,e))) for _ in range(z)]
    capacities=[m//j for j in range(1,9)]
    # Deterministic first-fit only. Any successful witness is checked explicitly.
    bins=[1]*8
    for p in factors:
        for j in range(8):
            if bins[j]*p<=capacities[j]:
                bins[j]*=p
                break
        else:
            return False
    assert all(h<=c for h,c in zip(bins,capacities))
    assert prod(bins)==prod(p**z for p,z in zip(PRIMES,e))
    return True


def main():
    started=time.monotonic()
    slots=json.loads((ROOT/'smooth_proof/frontier_slots6.json').read_text())
    certs={}
    for m,e,hs in slots:
        assert len(hs)<=8
        previous=1
        for j,h in enumerate(hs,1):
            assert 1<=h<=m
            assert gcd(previous,h)<=m//j
            previous*=h
        assert previous%prod(p**z for p,z in zip(PRIMES,e))==0
        certs.setdefault(m,[]).append(tuple(e))

    # Generating all integers directly is intentionally independent of smooth().
    smooth=[]
    for a in range(2,9360):
        e=valuation_vector(a)
        if e is not None:
            smooth.append((a,e))
    subsets=0
    distinct_demands=0
    covered_by_union=covered_by_bins=covered_by_slots=0
    checked_maxima=0
    for m,em in smooth:
        if m<=8 or sum(em)<3:
            continue
        candidates=[]
        for a,e in smooth:
            if a>=m:
                break
            if sum(e)<3:
                continue
            largest=max(p for p,z in zip(PRIMES,e) if z)
            if 7*a>m*largest:
                candidates.append((a,e))
        if len(candidates)<5:
            continue
        checked_maxima+=1
        seen=set()
        for chosen in combinations(candidates,5):
            subsets+=1
            e=tuple(em[j]+sum(row[1][j] for row in chosen) for j in range(3))
            if e in seen:
                continue
            seen.add(e)
            distinct_demands+=1
            if universal_prime_union(e,m):
                covered_by_union+=1
                continue
            if ordinary_bins(e,m):
                covered_by_bins+=1
                continue
            if any(all(v<=w for v,w in zip(e,d)) for d in certs.get(m,())):
                covered_by_slots+=1
                continue
            # More successful packing witnesses are allowed, but obtain them
            # independently via exact integer tightest-fit choice.
            caps=[m//j for j in range(1,9)]
            bins=[1]*8
            factors=[p for p,z in reversed(list(zip(PRIMES,e))) for _ in range(z)]
            for p in factors:
                opts=[j for j in range(8) if bins[j]*p<=caps[j]]
                if not opts:
                    break
                j=opts[0]
                for k in opts[1:]:
                    if caps[k]*bins[j]<caps[j]*bins[k]:
                        j=k
                bins[j]*=p
            else:
                assert prod(bins)==prod(p**z for p,z in zip(PRIMES,e))
                assert all(h<=c for h,c in zip(bins,caps))
                covered_by_bins+=1
                continue
            caps=[m//j for j in range(1,9)]
            bins=[1]*8
            for p in factors:
                opts=[j for j in range(8) if bins[j]*p<=caps[j]]
                if not opts:
                    break
                j=opts[0]
                for k in opts[1:]:
                    if caps[k]*bins[j]>caps[j]*bins[k]:
                        j=k
                bins[j]*=p
            else:
                assert prod(bins)==prod(p**z for p,z in zip(PRIMES,e))
                assert all(h<=c for h,c in zip(bins,caps))
                covered_by_bins+=1
                continue
            raise AssertionError(dict(M=m,A=[a for a,_ in chosen]+[m],demand=e))
    result=dict(status='PASS',cutoff_exclusive=9360,
                checked_maxima=checked_maxima,actual_source_subsets=subsets,
                distinct_demands=distinct_demands,
                prime_union_demands=covered_by_union,
                ordinary_bin_demands=covered_by_bins,
                cumulative_gcd_demands=covered_by_slots,
                cumulative_gcd_certificates=len(slots),
                seconds=round(time.monotonic()-started,3))
    path=ROOT/'g7_theory/g6_independent_result.json'
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
