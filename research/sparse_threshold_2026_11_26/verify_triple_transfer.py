"""Finite exact checks of the triple and ordinary placement accounting."""
from collections import Counter
from decimal import Decimal as D
from itertools import combinations
from math import gcd, lcm, prod

SMALL = (2, 3, 5)
BAND = (7, 11, 13, 17)
SCREEN = SMALL + BAND


def part(x, primes):
    result = 1
    for prime in primes:
        while x % prime == 0:
            result *= prime
            x //= prime
    return result


def unitary(x, divisor):
    return x % divisor == 0 and gcd(x // divisor, divisor) == 1


def levels(x):
    result = Counter()
    p = 2
    while p * p <= x:
        power = 1
        while x % p == 0:
            x //= p
            power *= p
            result[power] += 1
        p += 1
    if x > 1:
        result[x] += 1
    return result


def check_window(shift):
    maximum = 65536
    window = range(shift + 1, shift + maximum + 1)
    triples = [(h, p, q, r) for h in (1, 2, 3, 6, 9, 12)
               for p, q, r in combinations(BAND, 3)]
    ordinary = (46, 203, 403, 26, 58, 62, 391, 69, 91, 55)
    source = [prod(row) for row in triples] + list(ordinary)
    assert len(source) == len(set(source)) and max(source) <= maximum
    occupied = set()
    credits = {}

    def credit(b, factor):
        assert b in window and b % factor == 0
        assert gcd(credits.get(b, 1), factor) == 1
        credits[b] = credits.get(b, 1) * factor

    for h, p, q, r in triples:
        for label in (h*r, p*q):
            lo = (window.start + label - 1) // label * label
            candidates = [b for b in range(lo, window.stop, label)
                          if b not in occupied and part(b, SCREEN) == label]
            # Favor shared placements with a later ordinary label.
            b = max(candidates, key=lambda x: sum(unitary(x, k) for k in ordinary))
            occupied.add(b)
            credit(b, label)

    projected = [part(k, SCREEN) for k in ordinary]
    for t in set(projected) - {1}:
        hits = sum(unitary(b, t) for b in occupied)
        assert hits + projected.count(t) <= sum(unitary(a, t) for a in source)

    split = 0
    for k, t in zip(ordinary, projected):
        share = [b for b in sorted(occupied) if unitary(b, k)
                 and gcd(credits[b], k//t) == 1]
        if k != t and share:
            credit(share[0], k//t)
            split += 1
            label = t
        else:
            label = k
        if label > 1:
            fresh = next(b for b in window if b not in credits and unitary(b, label))
            credit(fresh, label)
    demand = sum((levels(a) for a in source), Counter())
    assert all(sum(b % power == 0 for b in credits) >= amount
               for power, amount in demand.items())
    assert len(credits) <= 2 * len(triples) + len(ordinary)
    assert split >= 2
    return len(triples), split, len(credits)


def check_constants():
    mass = (D('.281') / D('.259')).ln()
    for lower, upper, claimed in [('.438', '.482', '.028'), ('.528', '.741', '.87')]:
        u, v = D(lower), D(upper)
        bound = 2 * (u/D('.191')-1).ln()/v - 2*mass/(u-D('.281'))
        assert bound > D(claimed)
        print('Bank lower coefficient:', bound)
    assert mass/D('.259') < D('.316')
    beta = D('.8201')
    gap = 1-beta
    assert 6*gap-beta > D('.259') and beta-3*gap < D('.281')
    assert 1-D('4.5')*gap < D('.191') and beta < D(14)/17


if __name__ == '__main__':
    check_constants()
    for shift in (0, 4101, 87777, lcm(*range(1, 48)) * 23):
        print('Triple rows, split ordinary labels, physical positions:', check_window(shift))
