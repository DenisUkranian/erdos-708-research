"""Check local cofactor blockers, shared representatives and level repair on exact examples."""
from collections import defaultdict
from math import gcd, lcm
from random import Random


def atoms(a):
    out = {}
    p = 2
    while p * p <= a:
        if a % p == 0:
            q = 1
            while a % p == 0:
                a //= p
                q *= p
            out[p] = q
        p += 1
    if a > 1:
        out[a] = a
    return out


def verify(A, x):
    M = max(A)
    I = range(x + 1, x + M + 1)
    factors = {a: atoms(a) for a in A}
    anchor = min(A)
    b0 = (x // anchor + 1) * anchor
    chosen = {b0}
    groups = defaultdict(list)
    for a in A:
        if a != anchor and len(factors[a]) >= 3:
            d = a // max(factors[a].values())
            groups[d].append(a)
    credits = defaultdict(set)
    for d, rows in sorted(groups.items()):
        forbidden = {e // gcd(e, d) for e in groups if e > d and gcd(e, d) > 1}
        bank = [b for b in I if b % d == 0 and b != b0
                and all((b // d) % t != 0 for t in forbidden)]
        if len(bank) < len(rows):
            return False
        for a, b in zip(rows, bank):
            for p in atoms(d):
                assert b not in credits[p]
                credits[p].add(b)
            chosen.add(b)

    for p in set().union(*(f.keys() for f in factors.values())):
        levels = []
        q = p
        while q <= M:
            levels.append((q, sum(a % q == 0 for a in A)))
            q *= p

        def score(b):
            return sum(b % q == 0 for q, _ in levels)

        shortfall = max(0, *(need - sum(b % q == 0 for b in chosen) for q, need in levels))
        for b in sorted(set(I) - chosen, key=score, reverse=True)[:shortfall]:
            chosen.add(b)
        assert all(sum(b % q == 0 for b in chosen) >= need for q, need in levels)
    assert len(chosen) <= 2 * len(A) - 1
    return True


if __name__ == "__main__":
    rng = Random(708)
    total = checked = 0
    for M in (120, 360, 840):
        rich = [a for a in range(2, M) if len(atoms(a)) >= 3]
        for x in (0, 10**9 + 113, lcm(*range(1, M + 1)) - M // 2):
            for _ in range(7):
                A = sorted({M, *rng.sample(rich, min(len(rich), 16))})
                checked += verify(A, x)
                total += 1
    print(f"Exact local-bin and level-cover certificates: {checked} of {total} sample instances.")
