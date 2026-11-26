"""Exact six-label countermodel to deriving one-deletion matching from moments."""
from fractions import Fraction
from itertools import combinations

heavy = ("A", "B")
light = ("w", "x", "y", "z")
labels = heavy + light
cost = {p: 60 for p in heavy} | {p: 30 for p in light}
marginal = {p: Fraction(7, 32) for p in heavy} | {p: Fraction(1, 4) for p in light}
zero = frozenset()
source = {zero: Fraction(5, 16)}
for h in heavy:
    for l in light:
        source[frozenset((h, l))] = Fraction(7, 128)
for size, probability in [(2, Fraction(1, 32)), (3, Fraction(1, 64))]:
    for t in combinations(light, size):
        source[frozenset(t)] = probability

target = source.copy()
delta = Fraction(1, 64)
def add(t, mass):
    t = frozenset(t)
    target[t] = target.get(t, 0) + mass

for h in heavy:
    for l in light:
        add((h, l), -delta)
for t in combinations(light, 3):
    add(t, -delta)
add(zero, delta)
for t in combinations(light, 2):
    add(t, delta)
for l in light:
    add(heavy + (l,), delta)
add(light, delta)

assert sum(source.values()) == sum(target.values()) == 1
assert min(target.values()) >= 0
assert all(sum(cost[p] for p in s) <= 100 for s in source)
feasible_count = 0
for k in range(len(labels) + 1):
    for t in combinations(labels, k):
        if sum(cost[p] for p in t) > 100:
            continue
        t = frozenset(t)
        moment = 1
        for p in t:
            moment *= marginal[p]
        for law in (source, target):
            assert sum(v for s, v in law.items() if t <= s) == moment
        feasible_count += 1

family = set(source) - {zero}
neighbors = {t for t in target if any(len(s - t) <= 1 for s in family)}
gap = sum(source[s] for s in family) - sum(target[t] for t in neighbors)
assert gap == delta
rank_three_gap = Fraction(99, 100) * sum(source[s] for s in family) - sum(target[t] for t in neighbors)
assert rank_three_gap == Fraction(7, 800)
print(f"{feasible_count} product moments checked; Hall gap {gap}; lifted lower bound {rank_three_gap}")
