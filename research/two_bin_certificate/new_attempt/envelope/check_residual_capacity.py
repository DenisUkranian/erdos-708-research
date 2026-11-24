"""Sanity checks for the exact source-envelope LP formula.

This does not test or compute g(n).  Numerical LP optimization is checked
against exact source-envelope values proved in the accompanying note.
"""

from fractions import Fraction
from itertools import product
from math import prod

import numpy as np
from scipy.optimize import linprog


def factor(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = 1
    return out


def divisor_vectors(ps, es):
    for ds in product(*(range(e + 1) for e in es)):
        if any(ds):
            yield prod(p**d for p, d in zip(ps, ds)), ds


def kernel(a, weights, length=None):
    fs = factor(a)
    ps = [p for p in fs if weights.get(p, 0) > 0]
    es = [fs[p] for p in ps]
    if not ps:
        return 0.0
    length = prod(p**e for p, e in zip(ps, es)) if length is None else length
    maxima = [0.0] * len(ps)
    for d, ds in divisor_vectors(ps, es):
        load = sum(weights[p] * e for p, e in zip(ps, ds))
        price = max(0.0, min(min(weights[p] for p, e in zip(ps, ds) if e),
                             (load - 1.0) / sum(ds)))
        for i, p in enumerate(ps):
            if ds[i] and d * d <= length * p:
                maxima[i] = max(maxima[i], price)
    return sum(e * m for e, m in zip(es, maxima))


def envelope(a, weights):
    fs = factor(a)
    original = [p for p in fs if weights.get(p, 0) > 0]
    load = sum(fs[p] * weights[p] for p in original)
    best_capacity, best_prices = 0.0, {}
    for use in product((False, True), repeat=len(original)):
        ps = [p for p, yes in zip(original, use) if yes]
        if not ps:
            continue
        es = [fs[p] for p in ps]
        h = prod(p**e for p, e in zip(ps, es))
        k = len(ps)
        rows, bounds = [], []
        for i in range(k):
            row = [0.0] * (2 * k)
            row[i], row[k + i] = -1.0, 1.0
            rows.append(row)
            bounds.append(0.0)
        for d, ds in divisor_vectors(ps, es):
            total = sum(ds)
            for i, p in enumerate(ps):
                if not ds[i] or d * d > h * p:
                    continue
                row = list(map(float, ds)) + [0.0] * k
                row[i] -= total
                row[k + i] = total
                rows.append(row)
                bounds.append(1.0)
        result = linprog([0.0] * k + [-float(e) for e in es],
                         A_ub=np.array(rows), b_ub=np.array(bounds),
                         bounds=[(0.0, weights[p]) for p in ps] + [(0.0, None)] * k,
                         method="highs")
        assert result.success, result.message
        capacity = -result.fun
        if capacity > best_capacity + 1e-12:
            best_capacity = capacity
            best_prices = dict(zip(ps, result.x[:k]))
    value = load - best_capacity
    attained = kernel(a, best_prices) + load - sum(fs[p] * v for p, v in best_prices.items())
    assert abs(value - attained) < 2e-9, (a, weights, value, attained, best_prices)
    return value, best_prices


def main():
    cases = [
        (30, {2: 1, 3: 1, 5: 1}, Fraction(1)),
        (40, {2: 1, 5: 1}, Fraction(13, 6)),
        (32, {2: Fraction(2, 5)}, Fraction(1, 3)),
        (128, {2: Fraction(4, 5)}, Fraction(77, 20)),
        (210, {2: 1, 3: 1, 5: 1, 7: 1}, Fraction(2)),
        (900, {2: 1, 3: 1, 5: 1}, Fraction(4)),
    ]
    for a, rational_weights, expected in cases:
        weights = {p: float(v) for p, v in rational_weights.items()}
        actual, attaining = envelope(a, weights)
        assert abs(actual - float(expected)) < 2e-9, (a, actual, expected)
        print({"a": a, "expected": str(expected), "LP_value": actual,
               "attaining_reduction": attaining})

    # The nontrivial 40=2^3*5 upper-capacity certificate is exact.
    u, v = Fraction(1, 3), Fraction(1)
    yp, yq = u, Fraction(5, 6)
    assert 3 * yp + yq == Fraction(11, 6)
    assert 2 * yq == 1 + v - u
    assert Fraction(4) - (3 * yp + yq) == Fraction(13, 6)
    print("Numerical LP checks agree with the stated exact values; the 40-capacity identity is checked with Fractions. No interval transfer is established.")


if __name__ == "__main__":
    main()
