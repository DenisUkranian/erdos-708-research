#!/usr/bin/env python3
"""Exact, standard-library-only obstruction to a hub-budget proof of Erdos 708.

This is NOT a counterexample to Erdos 708.  It computes the actual covering
number and the stronger prime-power matching covering number on a genuine
interval, and checks that every hub assignment exceeds the proposed budget.
"""

import json
from math import lcm, prod
from pathlib import Path


def factor(n):
    result = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def exact_cover(items, vectors, demand):
    """0/1 dynamic programming; all arithmetic and comparisons are exact.

    State is the componentwise capped total covered demand.  Keeping only the
    cheapest subset per state is valid: every future transition depends only
    on that state.  Process each interval integer once, enforcing distinctness.
    """
    zero = (0,) * len(demand)
    states = {zero: (0, ())}
    for b, v in zip(items, vectors):
        if not any(v):
            continue
        old = list(states.items())
        for s, (cost, witness) in old:
            new = tuple(min(d, q + r) for d, q, r in zip(demand, s, v))
            if new == s:
                continue
            incumbent = states.get(new)
            if incumbent is None or cost + 1 < incumbent[0]:
                states[new] = (cost + 1, witness + (b,))
    assert demand in states
    cost, witness = states[demand]
    return {"minimum": cost, "witness": list(witness), "states": len(states)}


def main():
    A = [60, 66, 70, 78, 84, 90]
    n, M = len(A), max(A)
    L = lcm(*A)
    low, high = L - 44, L + 45
    I = list(range(low, high + 1))
    assert len(I) == M
    assert 2 * n < M < 16 * n * n
    sources = {a: factor(a) for a in A}
    primes = sorted(set().union(*(set(x) for x in sources.values())))
    assert all([b for b in I if b % a == 0] == [L] for a in A)
    K = sum(map(len, sources.values()))
    forced_hub_budget = 1 + K - len(primes)
    assert forced_hub_budget == 13 > 2 * n

    targets = {b: factor(b) for b in I}
    product_demand = tuple(sum(sources[a].get(p, 0) for a in A) for p in primes)
    product_vectors = [tuple(targets[b].get(p, 0) for p in primes) for b in I]
    product_result = exact_cover(I, product_vectors, product_demand)
    assert prod(product_result["witness"]) % prod(A) == 0

    powers = sorted({p ** e for f in sources.values() for p, v in f.items()
                     for e in range(1, v + 1)})
    slot_demand = tuple(sum(a % q == 0 for a in A) for q in powers)
    slot_vectors = [tuple(int(b % q == 0) for q in powers) for b in I]
    slot_result = exact_cover(I, slot_vectors, slot_demand)
    assert all(sum(b % q == 0 for b in slot_result["witness"]) >= d
               for q, d in zip(powers, slot_demand))

    report = {
        "scope": "Counterexample to a proposed sufficient hub budget, not to Erdos 708",
        "A": A, "n": n, "M": M, "x": low - 1,
        "interval": [low, high], "lcm_A": L,
        "factorizations": sources, "primes": primes,
        "sum_omega": K, "forced_hubs": [L],
        "forced_hub_bound": forced_hub_budget, "conjectured_bound_2n": 2 * n,
        "product_demand": dict(zip(primes, product_demand)),
        "product_cover": product_result,
        "prime_power_slot_demand": dict(zip(powers, slot_demand)),
        "prime_power_slot_cover": slot_result,
    }
    output = Path(__file__).with_name("hub_obstruction_certificate.json")
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
