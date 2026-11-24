"""Exact arithmetic verification of the separate-root counterexample.

This does not test or refute J_weak.  It verifies only the displayed local
inequality's failure; all parameters are explicit in the research addendum.
"""
from fractions import Fraction
from math import gcd, prod
import json

weights = {2: Fraction(1, 10), 3: Fraction(1, 1000),
           5: Fraction(1, 1000), 7: Fraction(1, 1000),
           11: Fraction(1, 1000), 13: Fraction(1)}
M, first, last, B = 338, 2939, 3276, 26
Q = prod(p for p in weights if p < 13)

def vp(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v

def load(n):
    return sum((w * vp(n, p) for p, w in weights.items()), Fraction())

def psi(u, r):
    return max(u + r - 1, 0) - max(r - 1, 0)

assert last - first + 1 == M
assert load(B // 13) <= 1 < load(B)
u = load(B) - 1
source_terms = [(t, psi(u, vp(t, 13)))
                for t in range(1, M // B + 1) if gcd(t, Q) == 1]
quotients = [b // B for b in range(first, last + 1) if b % B == 0]
target_good = [t for t in quotients if gcd(t, Q) == 1]
lhs = sum((value for _, value in source_terms), Fraction())
rhs = u * len(target_good)
mean = sum((w / (p - 1) for p, w in weights.items()), Fraction())
assert quotients == list(range(114, 127))
assert source_terms == [(1, Fraction()), (13, Fraction(1, 10))]
assert lhs == Fraction(1, 10) and rhs == 0
assert load(338) == Fraction(21, 10)
assert mean == Fraction(3687, 20000)
print(json.dumps({
    "status": "PASS: local separate-root comparison is false",
    "M": M, "I": [first, last], "root": B,
    "source_terms": [[t, str(v)] for t, v in source_terms],
    "target_quotients": quotients,
    "target_coprime_quotients": target_good,
    "lhs": str(lhs), "rhs": str(rhs), "weighted_mean": str(mean),
    "scope": "Not a counterexample to J_weak or to the minimal class."
}, indent=2))
