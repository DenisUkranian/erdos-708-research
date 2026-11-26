"""Exact harmonic cuts and rank-weighted Hall tests on arithmetic intervals (NumPy, SciPy)."""
from fractions import Fraction
from math import comb, lcm, prod
from itertools import combinations
from random import Random

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import maximum_flow


def harmonic(m):
    period = lcm(*range(1, m+1))
    normal = sum(period//d for d in range(1, m+1))
    masks = np.arange(1 << m)
    charge = normal*np.array([int(t).bit_count() for t in masks])
    patterns = [[sum(1 << i for i in range(m) if (r+i+1) % d == 0)
                 for r in range(d)] for d in range(1, m+1)]
    best = (-1,0,0)
    for start in range(0, period, 64):
        xs = np.arange(start,min(start+64,period))
        a = np.zeros((len(xs),len(masks)),dtype=np.int32)
        for d in range(1,m+1):
            indices = np.array(patterns[d-1])[xs % d]
            a[np.arange(len(xs)),indices] += m*(period//d)
        for bit in range(m):
            v = a.reshape(len(xs),-1,2,1 << bit)
            v[:,:,1,:] += v[:,:,0,:]
        a -= charge
        i,t = np.unravel_index(a.argmax(),a.shape)
        if a[i,t] > best[0]:
            best = (int(a[i,t]),int(xs[i]),int(t))
    value,x,mask = best
    T = [i+1 for i in range(m) if mask >> i & 1]
    # Independent direct evaluation of the recovered maximizing cut.
    trapped = [d for d in range(1,m+1)
               if all(i in T for i in range((-x-1)%d+1,m+1,d))]
    actual = sum(Fraction(1,d) for d in trapped)/Fraction(normal,period)-Fraction(len(T),m)
    assert actual == Fraction(value,m*normal)
    print(f'harmonic M={m} shifts={period} max={actual} x={x} offsets={T}',flush=True)


def factors(a):
    p = 2
    result = []
    while p*p <= a:
        if a % p:
            p += 1
            continue
        power = 1
        while a % p == 0:
            power *= p
            a //= p
        result.append(power)
        p += 1
    if a > 1:
        result.append(a)
    return result


def deficiency(rows, m, x, adaptive):
    n = len(rows)
    if not n:
        return 0
    choices = [[a//p for p in (powers if adaptive else [max(powers)])] for a,powers in rows]
    labels = sorted({h for options in choices for h in options})
    ids = {h:1+n+i for i,h in enumerate(labels)}
    base = 1+n+len(labels)
    sink = base+m
    edges = [(base+i,sink) for i in range(m)]
    for i,options in enumerate(choices,1):
        edges.append((0,i))
        edges.extend((i, ids[h]) for h in options)
    for h,node in ids.items():
        edges.extend((node, base+i) for i in range((-x-1)%h,m,h))
    tails,heads = zip(*edges)
    graph = coo_matrix((np.ones(len(edges),dtype=np.int32),(tails,heads)),
                       shape=(sink+1,sink+1)).tocsr()
    return n-int(maximum_flow(graph,0,sink).flow_value)


def halls():
    for m in (210,840,2310,10010):
        bank = [(a,factors(a)) for a in range(2,m+1)]
        period = lcm(*range(1,m+1))
        starts = [0,period-m//2,Random(m).randrange(period)]
        for label,x in zip(('zero','center','seeded'),starts):
            tests = []
            for j in range(3,max(len(p) for a,p in bank)+1):
                rows = [(a,p) for a,p in bank if len(p)>=j]
                tests.append((len(rows),deficiency(rows,m,x,False),deficiency(rows,m,x,True)))
            print(f'Hall M={m} shift={label} (rows,fixed,adaptive)={tests}',flush=True)


def preil_full_cut():
    m, x, n = 300000000, 2000000000000001416, 132347966
    ps = (2,3,5,7,11,13,17,19,23,29,31,37)
    density = 1-prod(Fraction(p-1,p) for p in ps)*(1+sum(Fraction(1,p-1) for p in ps))
    error = sum((j-1)*comb(len(ps),j) for j in range(2,len(ps)+1))
    uniform = (m*density-error).__ceil__()
    actual = 0
    for j in range(2,len(ps)+1):
        for part in combinations(ps,j):
            d=prod(part)
            actual += (-1)**j*(j-1)*((x+m)//d-x//d)
    assert actual >= uniform > m//2 > n
    print(f'Preil full cut: density={density} error<{error+1} uniform lower={uniform}, '
          f'exact count inside adaptive neighbors={actual}, surplus over n={actual-n}')


if __name__ == '__main__':
    for size in range(4,13):
        harmonic(size)
    halls()
    preil_full_cut()
