#!/usr/bin/env python3
"""Independent standard-library verification of the saved exact certificate."""
from pathlib import Path
import json
from math import isqrt

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / "omega2_hall_certificate.json").read_text())
M = data["M"]
H = data["half_width"]
assert M == 2*H + 1
K = data["tuple_offsets"]
assert K == sorted(set(K)) and all(-H <= k <= H for k in K)

# Deliberately use trial division rather than the builder's sieve.
primes = []
for candidate in range(2, M + 1):
    if all(candidate % p for p in primes if p <= isqrt(candidate)):
        primes.append(candidate)

conditions = data["crt_conditions"]
assert [row["p"] for row in conditions] == primes
C = int(data["center_hex"], 16)
period = int(data["period_hex"], 16)
assert C > H
computed_period = 1
for row in conditions:
    p, residue = row["p"], row["center_mod_p"]
    assert 0 <= residue < p and C % p == residue
    assert all((residue + k) % p != 0 for k in K)
    computed_period *= p
assert computed_period == period

# For all-composite sources, the complete any-prime-quotient neighborhood
# is exactly the targets divisible by a prime q <= M/2:
# every nontrivial quotient has such a prime divisor; conversely source
# 2q permits quotient q. This avoids constructing a huge dense graph.
neighbor = bytearray(M)
start = C - H
for p in primes:
    if 2*p > M:
        break
    first = (-start) % p
    for j in range(first, M, p):
        neighbor[j] = 1
assert all(not neighbor[k + H] for k in K)

sources = M - 1 - len(primes)
exact_neighbors = sum(neighbor)
assert sources == data["source_count"] == 10353
assert len(K) == data["certified_rough_offsets"] == 1411
assert exact_neighbors <= M - len(K) == 10352 < sources
result = {
    "status": "PASS",
    "M": M,
    "prime_count_M": len(primes),
    "sources": sources,
    "certified_rough_offsets": len(K),
    "verified_crt_conditions": len(conditions),
    "exact_neighbors": exact_neighbors,
    "Hall_deficiency": sources - exact_neighbors,
    "scope": "Omega>=2 only; no refutation of Omega>=3 or Erdos 708",
}
(ROOT / "omega2_hall_verification.json").write_text(json.dumps(result, indent=2) + "\n")
print(result)
