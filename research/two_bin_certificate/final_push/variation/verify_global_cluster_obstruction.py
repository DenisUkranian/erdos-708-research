"""Exact checks for the abstract obstruction; not a computation of g(n)."""

from fractions import Fraction as Q
from math import comb


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


N = 20
c = Q(21, 10)
n = comb(N, 5)
pair_source = 102
pair_target = 272
full_target = 646
z_pair = Q(5, 8)

source_positions = n + pair_source * comb(N, 2) + 17442
target_positions = pair_target * comb(N, 2) + full_target
assert source_positions == target_positions == 52326
assert choose(19, 4) == z_pair * pair_target * 19 + full_target == 3876
F = z_pair * pair_target * comb(N, 2) + full_target
J = Q(2, 5) * n - 9 * full_target
assert F == Q(17, 8) * n == 32946
assert J == F - c * n == Q(1938, 5) == Q(n, 40)

for k in range(1, N + 1):
    source_count = choose(N-k, 5-k)
    if k == 1:
        source_count += pair_source * (N-1)
    elif k == 2:
        source_count += pair_source
    target_count = full_target
    if k == 1:
        target_count += pair_target * (N-1)
    elif k == 2:
        target_count += pair_target
    assert target_count >= source_count
    if k <= 2:
        assert target_count == source_count
    defect = Q(2, 5) * choose(N-k, 5-k) - 9 * full_target
    assert defect <= 0

for r in range(6):
    assert max(r-2, 0) <= Q(choose(r, 2), 3)

# Half-integral target-cell vertices, reduced by permutation symmetry.
vertices = []
for i in range(N + 1):
    for j in range(N-i + 1):
        source = sum(
            choose(i, r) * choose(j, s) * choose(N-i-j, 5-r-s)
            * max(Q(r) + Q(s, 2) - c, Q(0))
            for r in range(6)
            for s in range(6-r)
        )
        target = pair_target * (choose(i, 2) + Q(i*j, 2))
        target += full_target * max(Q(i) + Q(j, 2) - 1, Q(0))
        value = source - target
        assert value <= J
        vertices.append((value, i, j))
assert [(i, j) for value, i, j in vertices if value == J] == [(0, N)]

# Every proper cold-core quotient has nonpositive global maximum.
for k in range(1, N):
    assert Q(4, 5) * choose(k, 4) - full_target * (k-1) <= 0

# The separate actual-integer acyclic-root-cover obstruction.
assert Q(20, 3) - 8 * Q(2, 3) ** 3 == Q(116, 27) > 4
heavy_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
M = 31
for p in heavy_primes:
    M *= p
assert M == 200560490130
assert (29 * 23 * 19) ** 2 < M

print('PASS: exact rows, common size, global-vertex certificate, all divisor')
print('cuts and count dominations, binary cuts, and cold quotient maxima.')
print(f'n={n}, F={F}, J={J}, J/n={J/n}, unique cube optimizer=all halves.')
print('PASS: independent-set certificate for the actual E-free root family.')
