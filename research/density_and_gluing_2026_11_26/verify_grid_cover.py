"""Check shared target positions and nested repairs in finite grids of prime pairs."""
from collections import Counter
from itertools import product
from math import isqrt, prod


def prime_powers(limit):
    sieve = bytearray([1]) * (limit + 1)
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p::p] = bytes((limit - p * p) // p + 1)
    levels = []
    for p in range(2, limit + 1):
        if sieve[p]:
            d = p
            while d <= limit:
                levels.append(d)
                d *= p
    return levels


def check(m, shift, cells):
    cell_rows = {d: set(range(d, m + 1, d)) for d in cells}
    rows = set.union(*cell_rows.values())
    row_multiplicity = Counter(a for bank in cell_rows.values() for a in bank)
    for d, members in cell_rows.items():
        private = sum(row_multiplicity[a] == 1 for a in members)
        assert 2 * private > m // d

    banks = {d: set(range((shift // d + 1) * d, shift + m + 1, d)) for d in cells}
    sites = set.union(*banks.values())
    initial = len(sites)
    duplicated = sum(map(len, banks.values())) - initial
    assert duplicated > 0
    levels = prime_powers(m)
    for d in levels:
        demand = sum(a % d == 0 for a in rows)
        available = range((shift // d + 1) * d, shift + m + 1, d)
        deficit = demand - sum(b in sites for b in available)
        if deficit > 0:
            new_sites = [b for b in available if b not in sites][:deficit]
            assert len(new_sites) == deficit
            sites.update(new_sites)

    for d in levels:
        demand = sum(a % d == 0 for a in rows)
        assert sum(b % d == 0 for b in sites) >= demand
    assert prod(sites) % prod(rows) == 0
    assert len(sites) <= 2 * len(rows)
    return duplicated, len(sites) - initial


if __name__ == "__main__":
    cells = [p * q for p, q in product((5, 7, 11), (13, 17, 19))]
    center = prod((5, 7, 11, 13, 17, 19)) ** 2
    cases = [check(m, shift, cells) for m in (1500, 2300, 3300)
             for shift in (0, 8301, center - m // 2)]
    repairs = sum(repaired for _, repaired in cases)
    assert repairs > 0
    print(f"{len(cases)} grids checked, {sum(duplicates for duplicates, _ in cases)} "
          f"duplicate positions and {repairs} fresh level repairs.")
