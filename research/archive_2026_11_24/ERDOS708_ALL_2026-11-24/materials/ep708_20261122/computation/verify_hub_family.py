#!/usr/bin/env python3
"""Concrete exact checks of the unbounded hub-budget gap family in README."""

from hashlib import sha256
import json
from math import gcd, lcm, prod
from pathlib import Path

from verify_hub_obstruction import factor


def check(D, K):
    assert K % 2 == 1 and gcd(D, K) == 1 and K >= 2 * D
    A = [D * k for k in range((K + 1) // 2, K + 1)] + [(D - 1) * K]
    A = sorted(A)
    n, M = len(A), max(A)
    assert len(A) == len(set(A)) and n == (K + 3) // 2
    assert gcd(*A) == 1 and all(2 * a > M for a in A)
    assert 2 * n < M < 16 * n * n
    L = lcm(*A)
    low, high = L - M // 2 + 1, L + M // 2
    assert high - low + 1 == M and low > 0
    for a in A:
        assert high // a - (low - 1) // a == 1 and L % a == 0

    B = list(range(((low + D - 1) // D) * D, high + 1, D))
    assert len(B) == K
    first_k = ((low + K - 1) // K) * K
    extra = next(b for b in range(first_k, high + 1, K) if b % D)
    B.append(extra)
    assert len(set(B)) == K + 1 == 2 * n - 2
    assert prod(B) % prod(A) == 0

    source_factors = [factor(a) for a in A]
    active = set().union(*(set(f) for f in source_factors))
    hub_bound = 1 + sum(map(len, source_factors)) - len(active)
    return {
        "D": D, "K": K, "n": n, "M": M,
        "extra_source": (D - 1) * K,
        "lcm_A": str(L),
        "interval_low": str(low), "interval_high": str(high),
        "forced_hub_bound": hub_bound,
        "two_n": 2 * n,
        "verified_cover_size": len(B),
        "source_sha256": sha256(json.dumps(A).encode()).hexdigest(),
        "cover_sha256": sha256(json.dumps(B).encode()).hexdigest(),
        "product_divisibility_verified": True,
    }


if __name__ == "__main__":
    cases = [check(30, 61), check(30, 301), check(210, 421)]
    Path(__file__).with_name("hub_family_certificates.json").write_text(
        json.dumps(cases, indent=2) + "\n")
    for case in cases:
        print({k: case[k] for k in ["D", "K", "n", "M", "forced_hub_bound",
                                    "two_n", "verified_cover_size"]})
