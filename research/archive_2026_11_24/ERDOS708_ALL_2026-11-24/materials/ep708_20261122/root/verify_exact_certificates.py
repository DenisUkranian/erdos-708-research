#!/usr/bin/env python3
"""Independent exact checks for auxiliary claims; NOT a solution of Erdos 708.

Uses only the Python standard library. The Hall certificate concerns the
restricted rule that only the largest prime factor may be removed. It does
not refute arbitrary prime removal, H2, or the original product-cover problem.
"""
from fractions import Fraction
import json
from pathlib import Path


def factors(n):
    out = []
    p = 2
    while p * p <= n:
        while n % p == 0:
            out.append(p)
            n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


def main():
    M, x = 440, 4400
    S = [2 * k for k in range(4, 221)
         if len(factors(k)) >= 2 and k != 169]
    assert len(S) == 171
    assert all(len(factors(m)) >= 3 for m in S)
    N = set()
    for m in S:
        d = m // max(factors(m))
        N.update(b for b in range(x + 1, x + M + 1) if b % d == 0)
    expected = {b for b in range(x + 1, x + M + 1)
                if any(b % d == 0 for d in [4, 6, 10, 14, 22])}
    assert N == expected and len(N) == 170 < len(S)
    mu = sum((Fraction(1, p) for p in [2, 3, 7]), Fraction())
    sigma2 = sum((Fraction(1, p*p) for p in [2, 3, 7]), Fraction())
    left = mu / (1 + mu)
    right = (mu*mu + sigma2) / 2
    assert mu == Fraction(41, 42)
    assert left == Fraction(41, 83)
    assert right == Fraction(1177, 1764)
    assert left < right
    result = {
        'status': 'exact_auxiliary_certificates_verified',
        'original_problem_solved': False,
        'restricted_matching': {
            'M': M, 'x': x, 'interval': [x+1, x+M],
            'rule': 'm/largest_prime_factor(m) must divide its distinct target',
            'source_size': len(S), 'neighbor_size': len(N),
            'source': S, 'neighbors': sorted(N),
            'scope': 'Refutes largest-prime-only matching; not Erdos 708.'
        },
        'sparse_comparison': {
            'primes': [2, 3, 7], 'mu': str(mu), 'sigma2': str(sigma2),
            'claimed_greater_left': str(left), 'right': str(right),
            'actual_right_minus_left': str(right-left),
            'scope': 'Refutes a numerical comparison; not H2.'
        }
    }
    out = Path(__file__).with_name('exact_auxiliary_certificates.json')
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({
        'status': result['status'], 'hall_sources': len(S),
        'hall_neighbors': len(N), 'sparse_left': str(left),
        'sparse_right': str(right), 'original_problem_solved': False
    }))


if __name__ == '__main__':
    main()
