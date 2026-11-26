"""Exact small-scale replay of terminal-pair absorption with occupied target sites."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import prod
from random import Random

M = 1938
SMOOTH_LIMIT = 6
SHIFT = 3**25 - M//2


def factor(value):
    factors = {}
    p = 2
    while p*p <= value:
        while value%p == 0:
            factors[p] = factors.get(p,0) + 1
            value //= p
        p += 1
    if value>1:
        factors[value] = 1
    return factors


def smooth_part(value):
    part = 1
    for p in (2,3,5):
        while value%p==0:
            value //= p
            part *= p
    return part


def split(row):
    h=smooth_part(row)
    if h>SMOOTH_LIMIT:
        return None
    quotient=factor(row//h)
    if len(quotient)!=2 or max(quotient.values())!=1:
        return None
    p,q=sorted(quotient)
    return h,p,q


def instance():
    peeled=set()
    for h in (1,2,3,4,5,6):
        for p in (7,11,13,17,19):
            eligible=[q for q in (11,13,17,19,23,29,31) if p<q and h*p*q<=M]
            for q in eligible[:2]:
                peeled.add(h*p*q)
    residual={3,9,27,81,243,729,7*11*13,7*11*19,7*13*17,8*13*17}
    rows=sorted(peeled|residual)
    assert max(rows)==M
    assert peeled=={a for a in rows if split(a) is not None}
    return rows,sorted(peeled),sorted(residual)


def maxima_by_core(parts, bank, occupied):
    groups=defaultdict(lambda:defaultdict(list))
    for a,(h,p,q) in parts.items():
        groups[h][p].append(a)
    expansion=None
    deficiency=0
    for h,labels in groups.items():
        deficit=0
        for count in range(1,len(labels)+1):
            for chosen in combinations(labels,count):
                # All rows of a type have identical banks. A minimizing expansion
                # ratio or maximizing deficit may take every row of each used type.
                nrows=sum(len(labels[p]) for p in chosen)
                targets=set().union(*(bank[h,p] for p in chosen))
                ratio=Fraction(len(targets),nrows)
                expansion=ratio if expansion is None else min(expansion,ratio)
                deficit=max(deficit,nrows-len(targets-occupied))
        deficiency+=deficit
    return expansion,deficiency


def anchors(parts,bank,occupied):
    owner={}
    eligible={a:sorted(bank[h,p]-occupied) for a,(h,p,q) in parts.items()}
    def augment(a,visited):
        for b in eligible[a]:
            if b in visited:
                continue
            visited.add(b)
            if b not in owner or augment(owner[b],visited):
                owner[b]=a
                return True
        return False
    for a in parts:
        augment(a,set())
    return {a:b for b,a in owner.items()}


def valuation(b,p):
    v=0
    while b%p==0:
        b//=p
        v+=1
    return v


def prime_repair(rows,initial,window,mode):
    demand=defaultdict(list)
    for a in rows:
        for p,e in factor(a).items():
            demand[p].append(e)
    selected=set(initial)
    for p,exponents in sorted(demand.items()):
        chosen=[valuation(b,p) for b in selected]
        options=sorted(((valuation(b,p),b) for b in window if b not in selected and b%p==0),
                       reverse=True)
        if mode=='product':
            missing=max(0,sum(exponents)-sum(chosen))
            for supply,b in options:
                if not missing:
                    break
                selected.add(b)
                missing=max(0,missing-supply)
            assert not missing
        else:
            missing=max(0,max(sum(e>=j for e in exponents)-sum(v>=j for v in chosen)
                              for j in range(1,max(exponents)+1)))
            assert missing<=len(options)
            selected.update(b for v,b in options[:missing])
    return selected


def levels_hold(rows,selected):
    all_levels={p**j for a in rows for p,e in factor(a).items() for j in range(1,e+1)}
    return all(sum(b%d==0 for b in selected)>=sum(a%d==0 for a in rows) for d in all_levels)


def main():
    rows,peeled,remainder=instance()
    parts={a:split(a) for a in peeled}
    window=range(SHIFT+1,SHIFT+M+1)
    banks={(h,p):{b for b in window if b%p==0 and smooth_part(b)==h} for h,p,q in parts.values()}
    blocked=banks[4,17]
    assert len(blocked)>0
    initial={3**25}
    for a in remainder:
        if len(factor(a))>1:
            candidates=[b for b in window if b%a==0]
            initial.add(min(candidates,key=lambda b:(b%3==0,b)))
    assert prod(initial)%prod(remainder)==0
    largest=max(p*q for a in remainder for p,q in combinations([p for p in factor(a) if p>SMOOTH_LIMIT],2))
    assert largest*SMOOTH_LIMIT<=M
    print('M, input size, peeled, residual, max surviving p*q, forbidden site count:',
          M,len(rows),len(peeled),len(remainder),largest,len(blocked))
    rng=Random(708)
    for mode in ('product','levels'):
        base=initial if mode=='product' else prime_repair(remainder,initial,window,mode)
        scenarios={'base':base,
                   'full-bank':base|blocked,
                   'full-bank-plus-noise':base|blocked|set(rng.sample(list(window),35))}
        for case,occupied in scenarios.items():
            if mode=='product':
                assert prod(occupied)%prod(remainder)==0
            else:
                assert levels_hold(remainder,occupied)
            assigned=anchors(parts,banks,occupied)
            missing=sorted(set(peeled)-assigned.keys())
            gamma,deficit=maxima_by_core(parts,banks,occupied)
            assert len(missing)==deficit
            assert deficit*gamma<=len(occupied)
            assert gamma>1
            if case.startswith('full-bank'):
                assert missing and set(parts[a][:2] for a in missing)>={(4,17)}
                if mode=='product' and case=='full-bank':
                    assert not levels_hold(remainder,occupied)
            sites=set(assigned.values())
            assert len(sites)==len(assigned) and not sites&occupied
            for a,b in assigned.items():
                h,p,q=parts[a]
                assert b%(h*p)==0 and smooth_part(b)==h
            selected=prime_repair(rows,occupied|sites,window,mode)
            extra=sum(sum(factor(a).values()) if mode=='product' else len(factor(a)) for a in missing)
            assert len(selected)<=len(occupied)+2*len(assigned)+extra
            assert prod(selected)%prod(rows)==0
            if mode=='levels':
                assert levels_hold(rows,selected)
            print(mode,case,'F=',len(occupied),'expansion=',gamma,'deficit=',deficit,
                  'unmatched=',missing,'verified cover=',len(selected))


if __name__=='__main__':
    main()
