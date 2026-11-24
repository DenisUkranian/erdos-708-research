#!/usr/bin/env python3
"""Verify an autonomous exact CRT counterexample to bank-product divisibility.

The verifier uses only the standard library and the adjacent certificate.
It does not read any older working file or enumerate the lifted interval.
"""

import hashlib
import json
from math import isqrt, prod
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERTIFICATE = ROOT / "bank_product_certificate.json"
data = json.loads(CERTIFICATE.read_text())
N = data["base_maximum"]
H = data["half_width"]
p = data["lifting_prime"]
M = data["ambient_maximum"]
assert (N, H, p, M) == (11763, 5881, 11777, 138532851)
assert N == 2 * H + 1 and M == p * N

# Trial division is intentionally independent of the original builder.
primes = []
for candidate in range(2, p + 1):
    if all(candidate % q for q in primes if q <= isqrt(candidate)):
        primes.append(candidate)
base_primes = [q for q in primes if q <= N]
assert primes[-1] == p and primes[-2] <= N
assert len(base_primes) == data["expected_base_prime_count"] == 1409
assert prod(data["base_maximum_factorization"]) == N
assert all(q in base_primes for q in data["base_maximum_factorization"])

is_prime = set(base_primes)
sources = [s for s in range(4, N + 1) if s not in is_prime]
assert sources[-1] == N
assert len(sources) == data["expected_source_count"] == 10353
assert len(sources) == N - 1 - len(base_primes)

conditions = data["crt_conditions"]
assert [row["prime"] for row in conditions] == base_primes + [p]
assert conditions[-1]["center_residue"] == H + 1
C = 0
period = 1
for row in conditions:
    q = row["prime"]
    residue = row["center_residue"]
    assert 0 <= residue < q
    C += period * (((residue - C) * pow(period, -1, q)) % q)
    period *= q
assert 0 <= C < period
assert C == int(data["center_hex"], 16)
assert period == int(data["period_hex"], 16)
assert C > H + 1
assert all(C % row["prime"] == row["center_residue"] for row in conditions)

rough = data["certified_rough_offsets"]
assert rough == sorted(set(rough))
assert len(rough) == 1411 and all(-H <= offset <= H for offset in rough)
for row in conditions[:-1]:
    assert all((row["center_residue"] + offset) % row["prime"] for offset in rough)

# J has length N, and its residues modulo p are precisely 1,...,N.
j_start = C - H
j_end = C + H
assert j_end - j_start + 1 == N
assert j_start % p == 1 and j_end % p == N
assert N < p
assert all((j_start + j) % p for j in range(N))

# Check the elementary characterization of all prime-deletion quotients.
# Every quotient s/q has a prime divisor <= N/2; conversely each prime
# r <= N/2 is itself the quotient (2r)/2 of a composite source.
source_set = set(sources)
quotient_count = 0
for s in sources:
    prime_divisors = [q for q in base_primes if q <= s and s % q == 0]
    assert prime_divisors
    for q in prime_divisors:
        quotient = s // q
        assert quotient >= 2
        small_factor = next(r for r in base_primes if quotient % r == 0)
        assert 2 * small_factor <= N
        quotient_count += 1
assert all(2 * r in source_set for r in base_primes if 2 * r <= N)

# Therefore the full quotient neighborhood is exactly this length-N mask.
neighbor = bytearray(N)
for r in base_primes:
    if 2 * r > N:
        break
    first = (-j_start) % r
    neighbor[first:N:r] = b"\1" * len(range(first, N, r))
assert {j - H for j, flag in enumerate(neighbor) if not flag} == set(rough)
neighbor_count = sum(neighbor)
assert neighbor_count == data["expected_bank_union_p_valuation"] == 10352

# The lifted interval has exactly these p-multiples, all of valuation one.
x = p * (C - H - 1)
right = p * (C + H)
assert x > 0 and right - x == M
assert (x // p + 1, right // p) == (j_start, j_end)
assert all((p * (j_start + j)) % (p * p) for j in range(N))

source_p_valuation = len(sources)
union_p_valuation = neighbor_count
assert source_p_valuation - union_p_valuation == data["expected_valuation_deficit"] == 1

# Scope checks: the prime cap and quadratic ambient restriction alone do
# not exclude the example. The forced bank of cofactor 4 certainly does.
m = len(sources)
assert p < 2 * m - 1
assert M < 16 * m * m
assert M // 4 > 10 * m

result = {
    "status": "PASS",
    "certificate_sha256": hashlib.sha256(CERTIFICATE.read_bytes()).hexdigest(),
    "base_maximum": N,
    "base_maximum_factorization": data["base_maximum_factorization"],
    "base_prime_count": len(base_primes),
    "source_count": m,
    "lifting_prime": p,
    "ambient_maximum": M,
    "crt_conditions_checked": len(conditions),
    "rough_offsets_checked": len(rough),
    "rough_residue_avoidance_checks": len(base_primes) * len(rough),
    "prime_deletion_quotients_checked": quotient_count,
    "center_bit_length": C.bit_length(),
    "period_bit_length": period.bit_length(),
    "source_p_valuation": source_p_valuation,
    "bank_union_p_valuation": union_p_valuation,
    "valuation_deficit": source_p_valuation - union_p_valuation,
    "forced_cofactor_4_bank_size_lower_bound": M // 4,
    "scope": "Refutes universal bank-product divisibility only; does not satisfy deletion minimality and does not refute the weighted-surplus target or Erdos 708.",
}
(ROOT / "bank_product_verification.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
