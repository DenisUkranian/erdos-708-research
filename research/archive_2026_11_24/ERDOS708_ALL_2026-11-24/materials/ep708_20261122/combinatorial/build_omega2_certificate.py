#!/usr/bin/env python3
"""Build an exact CRT certificate refuting the Omega>=2 matching shortcut."""
from pathlib import Path
import json
from math import isqrt

ROOT = Path(__file__).resolve().parent
M = 11763
H = (M - 1) // 2


def primes_upto(n):
    sieve = bytearray(b"\1") * (n + 1)
    sieve[:2] = b"\0\0"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b"\0" * (((n - p*p) // p) + 1)
    return [p for p in range(2, n + 1) if sieve[p]]


primes = primes_upto(M)
survivors = [-1, 1]
for p in primes:
    if isqrt(H) < p <= H:
        survivors.extend([-p, p])

# Preserve the symmetric initial prime sieve; thereafter remove a least
# occupied residue class. Prefer zero, then the smaller residue in a tie.
for p in primes:
    if p > len(survivors):
        break
    counts = [0] * p
    for k in survivors:
        counts[k % p] += 1
    removed = min(range(p), key=lambda r: (counts[r], r != 0, r))
    if counts[removed]:
        survivors = [k for k in survivors if k % p != removed]

survivors.sort()
assert len(survivors) == 1411

# Final residues are selected from the FINAL tuple and directly verified.
# C == -missing (mod p) makes every C+k, k in K, indivisible by p.
crt_conditions = []
center, modulus = 0, 1
for p in primes:
    used = {k % p for k in survivors}
    missing = next(r for r in range(p) if r not in used)
    residue = (-missing) % p
    crt_conditions.append({"p": p, "center_mod_p": residue})
    step = ((residue - center) * pow(modulus, -1, p)) % p
    center += modulus * step
    modulus *= p

if center <= H:
    center += modulus

data = {
    "description": "A CRT Hall obstruction for full prime-quotient matching with Omega(m)>=2; not a counterexample to Omega>=3 or Erdos 708.",
    "M": M,
    "half_width": H,
    "source_set": "All composite integers m with 1 <= m <= M",
    "target_interval": "[C-half_width, C+half_width]",
    "tuple_offsets": survivors,
    "crt_conditions": crt_conditions,
    "center_hex": hex(center),
    "period_hex": hex(modulus),
    "prime_count_M": len(primes),
    "source_count": M - 1 - len(primes),
    "certified_rough_offsets": len(survivors),
    "neighbor_count_upper_bound": M - len(survivors),
}
(ROOT / "omega2_hall_certificate.json").write_text(json.dumps(data, indent=2) + "\n")
print({"M": M, "source_count": data["source_count"], "rough_offsets": len(survivors), "neighbor_upper_bound": data["neighbor_count_upper_bound"], "crt_conditions": len(crt_conditions), "center_bits": center.bit_length()})
