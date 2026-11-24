"""Exact finite checks for two intermediate-certificate counterexamples.

These computations are not new g(n) values and do not test an Erdős 708
counterexample. They check two overstrong auxiliary assertions only.
Uses the Python standard library.
"""

from collections import defaultdict
from fractions import Fraction
from math import prod


def active_factorization(a, primes):
    factors = {}
    for p in primes:
        exponent = 0
        while a % p == 0:
            a //= p
            exponent += 1
        if exponent:
            factors[p] = exponent
    return factors


def normalized_root_example():
    length = 100
    primes = (2, 3, 5, 7, 11, 13)
    factors = {a: active_factorization(a, primes) for a in range(1, length + 1)}
    load = {a: sum(factors[a].values()) for a in factors}
    sources = [a for a in load if load[a] >= 3]
    payments = defaultdict(int)
    for a in sources:
        active_part = prod(p ** exponent for p, exponent in factors[a].items())
        root = active_part // max(factors[a])
        payments[root] += load[a] - 2
    coefficients = {d: Fraction(s, length // d) for d, s in payments.items()}
    flow = [Fraction(0) for _ in range(length + 1)]
    for d, beta in coefficients.items():
        for b in range(d, length + 1, d):
            flow[b] += beta
    congested = [
        (b, flow[b] - max(0, load[b] - 1))
        for b in load
        if flow[b] > max(0, load[b] - 1)
    ]
    excess = sum(value for _, value in congested)
    source_mass = sum(load[a] - 2 for a in sources)
    target_hinge = sum(max(0, value - 1) for value in load.values())
    bank_norm = sum(beta * Fraction(length, d) for d, beta in coefficients.items())
    assert len(sources) == 37
    assert source_mass == 63
    assert target_hinge == 121
    assert excess == Fraction(2095, 528)
    assert excess > Fraction(len(sources), 10)
    assert bank_norm <= Fraction(3, 2) * source_mass
    assert source_mass - Fraction(len(sources), 10) - target_hinge == Fraction(-617, 10)
    print("Fixed-root example: n=37, S2=63, H=121, E=2095/528 > 37/10.")
    print("Congested positions and exact excesses:", congested)


def union_discrepancy_example():
    primes = (101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
              157, 163, 167, 173, 179, 181, 191, 193, 197, 199)
    length = 10000
    shift = 387216877841586952278455969563989265562028744
    residues = (81, 94, 62, 90, 75, 14, 128, 91, 80, 89, 131,
                96, 47, 60, 77, 133, 138, 13, 18, 158, 115)
    assert all((-shift) % p == residue for p, residue in zip(primes, residues))
    assert min(p * q for i, p in enumerate(primes) for q in primes[i + 1:]) > length
    prefix_union = sum(length // p for p in primes)
    shifted_positions = bytearray(length + 1)
    for p, residue in zip(primes, residues):
        first = residue if residue else p
        for position in range(first, length + 1, p):
            shifted_positions[position] = 1
    shifted_union = sum(shifted_positions)
    assert prefix_union == 1451
    assert shifted_union == 1354
    assert prefix_union - shifted_union == 97 > len(primes)
    print("Union example: 21 roots, prefix union=1451, shifted union=1354, deficit=97.")


if __name__ == "__main__":
    normalized_root_example()
    union_discrepancy_example()
