"""Integer certificates for the small windows and the seven-source window. Requires NumPy."""
from functools import lru_cache
from math import factorial, lcm, prod

import numpy as np


def val(b, p):
    e = 0
    while b % p == 0:
        e += 1
        b //= p
    return e


def subset_sums(rows):
    out = np.zeros((1 << len(rows), len(rows[0])), dtype=np.int16)
    for i, row in enumerate(rows):
        out[1 << i:2 << i] = out[:1 << i] + row
    return out


def small():
    totals = [0, 0]
    biggest_gap = 0
    for m in range(2, 9):
        primes = [p for p in (2, 3, 5, 7) if p <= m]
        levels = [(p, j) for p in primes for j in range(1, m.bit_length()) if p**j <= m]

        def signature(b):
            return np.array([val(b, p) for p in primes] +
                            [int(b % p**j == 0) for p, j in levels], dtype=np.int16)

        demand = subset_sums([signature(b) for b in range(2, m+1)])[1 << (m-2):]
        period = lcm(*range(1, m+1))
        shifts = factorial(m) if m <= 6 else period
        # For m<=6, product(A) divides m!, a safe period for actual valuations capped at demand.
        # For every m the lcm is a full period for the level constraints.
        masks = sorted(range(1 << m), key=int.bit_count)
        order = np.array(masks)
        sizes = np.array([mask.bit_count() for mask in masks])
        signatures = [signature(b) for b in range(1, shifts+m)]
        for x in range(shifts):
            supplied = subset_sums(signatures[x:x+m])[order]
            def minimum(cols):
                feasible = (supplied[:, None, cols] >= demand[None, :, cols]).all(axis=2)
                assert feasible.any(axis=0).all()
                return sizes[feasible.argmax(axis=0)]
            ordinary = minimum(slice(0, len(primes)))
            level = minimum(slice(len(primes), None))
            assert (ordinary <= level).all()
            biggest_gap = max(biggest_gap, int((level-ordinary).max()))
        counts = [shifts*len(demand), period*len(demand)]
        totals = [a+b for a, b in zip(totals, counts)]
        print(f'M={m} sources={len(demand)} shifts={shifts} H-period={period}')
    print('A/shift cases for tau, full-lcm cases for H, maximum H-tau:', *totals, biggest_gap)


def seven():
    a = [60090, 4370, 6555, 15295, 24035, 28405, 37145]
    x = 920168185
    primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 2003)
    for b in a:
        assert prod(p**val(b,p) for p in primes) == b
    offsets = (11790, 27315, 28396, 56939, 60090)
    assert len(set(offsets)) == 5 and all(0 < i <= max(a) for i in offsets)
    assert prod(x+i for i in offsets) % prod(a) == 0
    full = (865, 3050, 9605, 35825, 11790, 24900, 50075)
    assert len(set(full)) == 7 and all(0 < i <= max(a) for i in full)
    assert all((x+i) % b == 0 for i, b in zip(full, sorted(a)))
    assert all(b % 5 == 0 for b in a)  # H>=7
    demand = tuple(sum(val(b,p) for b in a) for p in primes)
    profiles = {tuple(min(d,val(b,p)) for p,d in zip(primes,demand))
                for b in range(x+1,x+max(a)+1)}
    maximal = []
    for s in sorted(profiles, key=sum, reverse=True):
        if not any(all(i <= j for i,j in zip(s,t)) for t in maximal):
            maximal.append(s)
    choices = [[s for s in maximal if s[i]] for i in range(len(demand))]
    @lru_cache(None)
    def possible(d, k):
        if not any(d):
            return True
        if k == 0 or any(d[i] > k*max(s[i] for s in choices[i]) for i in range(len(d))):
            return False
        i = min((i for i in range(len(d)) if d[i]), key=lambda i:len(choices[i]))
        return any(possible(tuple(max(0,u-v) for u,v in zip(d,s)), k-1) for s in choices[i])
    assert not possible(demand, 4)   # even with unlimited copies of maximal profiles
    print('seven rows: tau=5 H=7; maximal valuation profiles:',len(maximal),'offsets:',*offsets)


if __name__ == '__main__':
    seven()
    small()
