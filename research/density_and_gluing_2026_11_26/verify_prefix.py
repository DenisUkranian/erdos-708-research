"""Exact arithmetic checks of the layered certificate for arbitrary prime prefixes."""
from fractions import Fraction as F
from itertools import product
from math import isqrt
from random import Random


def is_prime(n):
    return n >= 2 and all(n % i for i in range(2, isqrt(n) + 1))


def valuation(b, p):
    j = 0
    while b % p == 0:
        j += 1
        b //= p
    return j


def verify(M, fibers, shifts):
    if not fibers:
        return 0
    ends = {p: p * k for p, k in fibers.items()}
    source = {v for p, t in ends.items() for v in range(p, t + 1, p)}
    n = len(source)
    coords = sorted({0, M, *ends.values()})
    layers = []
    for a, b in zip(coords, coords[1:]):
        mu = sum((F(1, p) for p in fibers if ends[p] >= b), F())
        layers.append((a, b, mu, min(F(1), mu)))
    C = max([0] + [b for _, b, mu, _ in layers if mu >= 1])
    L = sum((b - a) * lam for a, b, _, lam in layers)
    ideal = sum((b - a) * (2*lam - lam**2) for a, b, _, lam in layers)
    assert C <= L <= ideal <= 2*n
    assert sum(k for p, k in fibers.items() if ends[p] > C) <= L

    demands = {}
    for q in range(2, M + 1):
        if is_prime(q):
            d = q
            while d <= M:
                ct = sum(v % d == 0 for v in source)
                if ct:
                    demands[q, d] = ct
                d *= q

    for shift in shifts:
        I = range(shift + 1, shift + M + 1)
        banks, hard = {}, set()
        for p, k in fibers.items():
            hits = [b for b in I if b % p == 0]
            if p <= n:
                banks[p] = set(sorted(hits, key=lambda b: -valuation(b, p))[:M//p])
            else:
                hard.update(hits[:k])
        y = dict.fromkeys(I, F())
        for a, b, mu, lam in layers:
            bank = {v for p, bank in banks.items() if ends[p] >= b for v in bank}
            for v in I:
                y[v] += F(b-a, M) * (1 if v in bank else lam)
        for v in hard:
            y[v] = 1
        hard_overhead = sum(F(L, p) for p in fibers if p > n)
        assert sum(y.values()) <= ideal + hard_overhead
        total_error = F()
        for (q, d), ct in demands.items():
            got = sum(y[v] for v in I if v % d == 0)
            if q > n:
                assert got >= ct and d == q
                continue
            c = max(C, ends.get(q, 0))
            g = c + sum((F(t-c, p) for p, t in ends.items() if t > c), F())
            error = sum((min(1, F(c, p*d)) for p, k in fibers.items()
                         if ends[p] > c and k >= d), F())
            total_error += error
            assert got >= F(M//d, M) * g >= F(g, d)-1
            assert ct <= F(g, d) + error
        bound = sum(sum(1 for (q, d) in demands if q <= n and d <= k)
                    * min(1, F(2*n, p)) for p, k in fibers.items() if ends[p] > C)
        assert total_error <= bound
    return len(shifts)


def main():
    count = shapes = saturated = 0
    for M in range(2, 13):
        ps = [p for p in range(2, M + 1) if is_prime(p)]
        for ks in product(*(range(M//p+1) for p in ps)):
            f = {p:k for p, k in zip(ps, ks) if k}
            if f:
                count += verify(M, f, [0, 1, M+2, 12347])
                shapes += 1
                saturated += sum((F(1,p) for p in f), F()) >= 1
    rng = Random(708)
    for _ in range(250):
        M = rng.randint(13, 64)
        ps = [p for p in range(2, M + 1) if is_prime(p)]
        f = {p:rng.randint(1, M//p) for p in ps if rng.random() < .65}
        if f:
            count += verify(M, f, [rng.randrange(1, 10**8)])
            shapes += 1
            saturated += sum((F(1,p) for p in f), F()) >= 1
    print(f"{shapes} prefix families, {count} family/shift certificates, {saturated} families attaining the saturated regime; all exact assertions passed.")


if __name__ == "__main__":
    main()
