#!/usr/bin/env python3
"""Exact arithmetic verification of smooth-source slot-packing cutoffs.

This verifies only the analytic tail. It does not enumerate the finite source
sets below the printed cutoff and does not on its own prove an exact g(n).
"""
from math import factorial, prod
import json


def ceil_strict_root_ratio(numerator, denominator, degree):
    """Smallest integer m with denominator*m**degree > numerator."""
    lo, hi = 0, 1
    while denominator * hi ** degree <= numerator:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if denominator * mid ** degree > numerator:
            hi = mid
        else:
            lo = mid
    return hi


def threshold(n, slots, primes):
    assert slots > n
    start = slots * max(primes)
    rows = []
    last_bad_any = start - 1
    for p in primes:
        divisor = factorial(n) if p == max(primes) else 1
        numerator = factorial(slots) * p ** (slots - 1)
        coarse = ceil_strict_root_ratio(numerator, divisor, slots - n)
        last_bad = None
        for m in range(start, max(start, coarse)):
            lower = p * prod(max(m // (j * p) + 1, p)
                             for j in range(1, slots + 1))
            if lower * divisor <= m ** n:
                last_bad = m
                last_bad_any = max(last_bad_any, m)
        # For all m >= coarse the strict real-valued lower bound works;
        # direct exact integer checks cover [start, coarse).
        rows.append(dict(prime=p, demand_divisor=divisor,
                         analytic_coarse_from=coarse,
                         last_failure_at_or_above_start=last_bad))
    return dict(n=n, slots=slots, allowed_primes=primes,
                checking_from=start, proved_packing_for_all_M_from=last_bad_any+1,
                rows=rows)


if __name__ == '__main__':
    results = [threshold(6, 8, [2, 3, 5]),
               threshold(7, 10, [2, 3, 5, 7]),
               threshold(8, 12, [2, 3, 5, 7]),
               threshold(9, 14, [2, 3, 5, 7, 11])]
    assert results[0]['proved_packing_for_all_M_from'] == 9360
    assert results[1]['proved_packing_for_all_M_from'] == 19170
    assert results[2]['proved_packing_for_all_M_from'] == 12320
    assert results[3]['proved_packing_for_all_M_from'] == 24206
    print(json.dumps(results, indent=2))
