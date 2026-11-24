#!/usr/bin/env python3
"""Exact finite verification; no interval enumeration or external packages."""

from hashlib import sha256
from itertools import combinations
from math import comb, isqrt, prod
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
certificate_path = ROOT / "bounded_occurrence_h1_certificate.json"
data = json.loads(certificate_path.read_text())
primes = data["primes"]
k = len(primes)
assert primes == sorted(set(primes))
assert k == data["number_of_primes"] == 20
assert all(p > 2 and all(p % d for d in range(2, isqrt(p) + 1)) for p in primes)

M = data["M"]
half_width = data["half_width"]
assert M == primes[-1] ** 4 == 1590446354641
assert M == 2 * half_width + 1
assert 2 * primes[0] ** 4 > M
assert primes[0] ** 5 > M
assert data["maximum_prefix_occurrences"] == 4

C = 0
period = 1
rows = data["crt_conditions"]
assert [row["prime"] for row in rows] == primes
for row in rows:
    p = row["prime"]
    modulus = row["modulus"]
    residue = row["center_residue"]
    assert modulus == p ** 5
    assert residue == (p ** 5 - p) // 2
    assert residue > half_width and modulus - residue > half_width
    C += period * (((residue - C) * pow(period, -1, modulus)) % modulus)
    period *= modulus
if C <= half_width:
    C += period
assert C == int(data["center_hex"], 16)
assert period == int(data["period_hex"], 16)
assert C > half_width
assert all(C % row["modulus"] == row["center_residue"] for row in rows)
assert all(C % p == 0 and C % (p * p) != 0 for p in primes)

x = C - half_width - 1
assert x >= 0


def interval_count(d):
    return (x + M) // d - x // d


def count_excess(d):
    value = interval_count(d) - M // d
    assert value in (0, 1)
    return value


# Every intersection involving >=4 distinct listed primes contains
# exactly C. Four-prime products have one prefix multiple; all products
# involving >=5 listed primes have none. The extremal products establish
# these assertions simultaneously for every subset.
assert all(interval_count(prod(t)) == 1 and M // prod(t) == 1
           for t in combinations(primes, 4))
assert all(interval_count(prod(t)) == 1 and M // prod(t) == 0
           for t in combinations(primes, 5))
assert C % prod(primes) == 0
high_degree_term = -sum((-1) ** j * comb(k, j) for j in range(5, k + 1))
assert high_degree_term == comb(k - 1, 4)

pair_excess = sum(count_excess(prod(t)) for t in combinations(primes, 2))
triple_excess = sum(count_excess(prod(t)) for t in combinations(primes, 3))
assert pair_excess == data["pair_count_excess"] == 89
assert triple_excess == data["triple_count_excess"] == 573
capped_deficit = high_degree_term - pair_excess + triple_excess
assert capped_deficit == data["capped_hinge_deficit"] == 4360

# No fifth power occurs anywhere in either interval, so this is the
# complete raw valuation-tail correction, including every target power.
assert all(interval_count(p ** 5) == M // (p ** 5) == 0 for p in primes)
power_tail_excess = sum(count_excess(p ** j) for p in primes for j in (2, 3, 4))
assert power_tail_excess == data["raw_power_tail_excess"] == 39
raw_deficit = capped_deficit - power_tail_excess
assert raw_deficit == data["raw_hinge_deficit"] == 4321
lower_bound = comb(k - 1, 4) - comb(k, 2) - 3 * k
assert lower_bound == data["proved_raw_hinge_deficit_lower_bound"] == 3626
assert raw_deficit >= lower_bound > 0

result = {
    "status": "PASS",
    "certificate_sha256": sha256(certificate_path.read_bytes()).hexdigest(),
    "M": M,
    "number_of_primes": k,
    "smallest_prime": primes[0],
    "largest_prime": primes[-1],
    "maximum_prefix_prime_occurrences": 4,
    "crt_conditions_checked": len(rows),
    "four_prime_intersections_checked": comb(k, 4),
    "five_prime_intersections_checked": comb(k, 5),
    "center_bit_length": C.bit_length(),
    "pair_count_excess": pair_excess,
    "triple_count_excess": triple_excess,
    "raw_power_tail_excess": power_tail_excess,
    "capped_H1_prefix_minus_interval": capped_deficit,
    "raw_H1_prefix_minus_interval": raw_deficit,
    "general_lower_bound": lower_bound,
    "scope": "Refutes a universal O(k^2) H1 tail-discrepancy bound even with at most four heavy occurrences per prefix source; not a counterexample to J_weak or Erdos 708.",
}
(ROOT / "bounded_occurrence_h1_verification.json").write_text(
    json.dumps(result, indent=2) + "\n"
)
print(json.dumps(result, indent=2))
