"""Construct the residue-cloned cover in the bounded-cofactor theorem."""
from collections import Counter
from itertools import product
from math import isqrt, lcm
from random import Random


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def check(M, f, shift):
    source = {p*h for p,k in f.items() for h in range(1,k+1)}
    m = sum(f.values())
    D = lcm(*range(1,max(f.values())+1))
    if M//D < m:
        return 0, 0
    I = range(shift+1, shift+M+1)
    T = Counter()
    for p,k in f.items():
        v = -I.start % p + I.start
        T.update(range(v, v+p*k, p))
    F = set(T)
    collisions = m-len(F)
    for b,copies in T.items():
        for _ in range(copies-1):
            first = (b-I.start) % D + I.start
            F.add(next(x for x in range(first,I.stop,D) if x not in F))
    assert len(F) == m
    for q in range(2, max(source)+1):
        if prime(q):
            d = q
            while d <= max(source):
                assert sum(v%d==0 for v in F) >= sum(v%d==0 for v in source)
                d*=q
    return 1, collisions

rng = Random(708)
cases = repaired = 0
for M in range(10, 112):
    ps = [p for p in range(2, M+1) if prime(p)]
    for _ in range(15):
        K = rng.randint(1,4)
        f = {p:rng.randint(1,min(K,M//p)) for p in rng.sample(ps,rng.randint(1,min(len(ps),10)))}
        shift = rng.choice([lcm(*f)-M//2, rng.randrange(1000000), 0])
        shift = max(0,shift)
        t,c=check(M,f,shift)
        cases+=t
        repaired+=c
print(cases, "sharp covers passed with", repaired, "duplicate copies replaced")
