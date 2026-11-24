"""Verify cardinality and row demand of one explicit intermediate counterexample.

This does not compute g(n), solve a covering instance, or test the target
asymptotic. It only verifies the source-set parameters of the CRT bank
counterlemma.
"""
import json
from pathlib import Path
import numpy as np

N, p = 11763, 11777
M = N * p
sieve = np.ones(N + 1, dtype=np.bool_)
sieve[:2] = False
for q in range(2, int(N**0.5) + 1):
    if sieve[q]:
        sieve[q*q::q] = False
primes = np.flatnonzero(sieve).tolist()
omega = np.zeros(M + 1, dtype=np.uint8)
for q in primes:
    power = q
    while power <= M:
        omega[power::power] += 1
        power *= q
selected = omega >= 4
selected[p::p] |= omega[p::p] >= 2
selected[:2] = False
size = int(np.count_nonzero(selected))
Dp = int(np.count_nonzero(selected[p::p]))
D2 = 0
power = 2
while power <= M:
    D2 += int(np.count_nonzero(selected[power::power]))
    power *= 2
hot_2_row_lower = 2 * (M // 4)
power = 8
while power <= M:
    hot_2_row_lower += M // power
    power *= 2
out = {
    "purpose": "Counterlemma parameter verification, not a computation of g(n)",
    "N": N, "p": p, "M": M, "small_prime_count": len(primes),
    "n_top": size, "density": size / M,
    "M_is_selected": bool(selected[M]),
    "source_M_load": "14/5",
    "selected_min_load": "11/5",
    "unselected_max_load": "9/5",
    "D_p": Dp, "D_2": D2,
    "unavoidable_hot_2_row_lower": hot_2_row_lower,
    "hot_2_lower_minus_D2": hot_2_row_lower - D2,
    "2n_less_than_M": 2 * size < M,
    "M_less_than_16n_squared": M < 16 * size * size,
    "not_an_optimality_claim": True,
}
assert M == 138532851
assert Dp == 10353 and selected[M]
print(json.dumps(out, indent=2))
Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n")
