"""Directed tests of a global bank-union inequality, not of g(n).

For an actual CRT-realizable interval and fixed rational clipped weights,
maximize sum_A X(a)-sum_{b in U(A)} X(b), restricting candidates to X(a)>2.
The optimization is an exact integral maximum-closure / minimum-cut problem.
SciPy is used only to solve the integral flow. Any nonempty witness can be
checked using the standard-library-only verify_witness function.
"""

from __future__ import annotations

import argparse
from collections import deque
from fractions import Fraction
import json
from math import isqrt, lcm
from pathlib import Path


def sieve(M):
    spf = list(range(M + 1))
    for p in range(2, isqrt(M) + 1):
        if spf[p] == p:
            for a in range(p * p, M + 1, p):
                if spf[a] == a:
                    spf[a] = p
    primes = [p for p in range(2, M + 1) if spf[p] == p]
    factors = [{} for _ in range(M + 1)]
    for a in range(2, M + 1):
        p = spf[a]
        factors[a] = dict(factors[a // p])
        factors[a][p] = factors[a].get(p, 0) + 1
    return primes, factors


def actual_phases(M, primes, mode, active=None):
    """Specify one residue modulo a large power of EACH source prime.

    No target is zero modulo that specified power, so the weighted target
    valuations are determined exactly for every CRT solution, not truncated.
    """
    center = (M + 1) // 2
    uncovered = [True] * (M + 1)
    phases = []
    for p in primes:
        if mode == "prefix":
            representative = 0
        elif mode == "center" or p <= isqrt(M) or (active is not None and p not in active):
            representative = center
        else:
            counts = [0] * p
            for i in range(1, M + 1):
                if uncovered[i]:
                    counts[i % p] += 1
            if mode in {"spread", "park"}:
                residue = min(range(p), key=lambda r: (-counts[r], r))
            else:
                residue = min(range(p), key=lambda r: (counts[r], r))
            # Put the selected zero just outside the interval. This avoids
            # an artificial high-valuation spike for each large prime.
            representative = residue + ((M - residue) // p + 1) * p
        power = p
        while power <= 2 * M:
            power *= p
        modulus = power * p
        residue = (power - representative) % modulus
        assert all((residue + i) % modulus for i in range(1, M + 1))
        phases.append((p, modulus, residue))
        if (active is None or p in active) and not (mode == "park" and p > isqrt(M)):
            for i in range(1, M + 1):
                if (residue + i) % p == 0:
                    uncovered[i] = False
    return phases


def crt(phases):
    x, modulus = 0, 1
    for _, q, r in phases:
        step = ((r - x) * pow(modulus, -1, q)) % q
        x += modulus * step
        modulus *= q
    return x, modulus


def target_loads(M, phases, weights):
    loads = [0] * (M + 1)
    for p, modulus, residue in phases:
        w = weights.get(p, 0)
        if not w:
            continue
        power = p
        while power <= modulus:
            first = (-residue) % power
            if first == 0:
                first = power
            for i in range(first, M + 1, power):
                loads[i] += w
            power *= p
    return loads


def closure(M, weights, denominator, mode="greedy", force=None):
    import numpy as np
    from scipy.sparse import coo_matrix
    from scipy.sparse.csgraph import maximum_flow

    primes, factors = sieve(M)
    source_load = {
        a: sum(weights.get(p, 0) * e for p, e in factors[a].items())
        for a in range(2, M + 1)
    }
    candidates = [a for a in range(2, M + 1)
                  if source_load[a] > 2 * denominator]
    active = {p for a in candidates for p in factors[a] if weights.get(p, 0)}
    # Removing unused weighted coordinates leaves the candidate set unchanged
    # and can only make a counterexample to the proposed inequality easier.
    weights = {p: w for p, w in weights.items() if p in active}
    phases = actual_phases(M, primes, mode, active)
    x, period = crt(phases)
    if force is not None and force not in candidates:
        raise ValueError("The forced source is not strictly above load two")
    cofactors = sorted({a // p for a in candidates for p in factors[a]})
    loads = target_loads(M, phases, weights)
    source_id = {a: 1 + j for j, a in enumerate(candidates)}
    cofactor_id = {d: 1 + len(candidates) + j
                   for j, d in enumerate(cofactors)}
    target_start = 1 + len(candidates) + len(cofactors)
    sink = target_start + M
    total = sum(source_load[a] for a in candidates)
    infinity = total + sum(loads) + 1
    rows, cols, caps = [], [], []

    def edge(u, v, c):
        if c:
            rows.append(u)
            cols.append(v)
            caps.append(c)

    for a in candidates:
        edge(0, source_id[a], source_load[a])
        for p in factors[a]:
            edge(source_id[a], cofactor_id[a // p], infinity)
    if force is not None:
        edge(0, source_id[force], infinity)
    for d in cofactors:
        first = (-x) % d
        if not first:
            first = d
        for i in range(first, M + 1, d):
            edge(cofactor_id[d], target_start + i - 1, infinity)
    for i in range(1, M + 1):
        edge(target_start + i - 1, sink, loads[i])
    capacity = coo_matrix((np.array(caps, dtype=np.int64), (rows, cols)),
                          shape=(sink + 1, sink + 1)).tocsr()
    # SciPy's flow kernel uses signed 32-bit edge capacities. Never allow
    # silent overflow to masquerade as an exact certificate.
    assert int(capacity.data.max(initial=0)) < 2**31
    assert total + (infinity if force is not None else 0) < 2**31
    result = maximum_flow(capacity, 0, sink)
    residual = (capacity - result.flow).tocsr()
    reverse_residual = residual.transpose().tocsr()
    reaches_sink, queue = {sink}, deque([sink])
    while queue:
        u = queue.popleft()
        for j in range(reverse_residual.indptr[u], reverse_residual.indptr[u + 1]):
            v = int(reverse_residual.indices[j])
            if reverse_residual.data[j] > 0 and v not in reaches_sink:
                reaches_sink.add(v)
                queue.append(v)
    # This is the MAXIMAL source side of an optimum cut. It detects a
    # nonempty zero-profit witness as well as a positive-profit witness;
    # using only vertices reachable from the flow source can return the
    # empty optimum and conceal equality cases.
    A = [a for a in candidates if source_id[a] not in reaches_sink]
    U = sorted({i for a in A for p in factors[a]
                for i in range(((-x) % (a // p)) or (a // p), M + 1, a // p)})
    profit = sum(source_load[a] for a in A) - sum(loads[i] for i in U)
    expected = total - int(result.flow_value)
    assert profit == expected
    return {
        "kind": "joint_bank_maximum_closure",
        "scope": "An auxiliary bank-union inequality; not an Erdos 708 counterexample",
        "M": M, "mode": mode, "denominator": denominator,
        "weights": {str(p): w for p, w in weights.items() if w},
        "candidate_count": len(candidates), "source_count": len(A),
        "bank_union_count": len(U), "profit_numerator": profit,
        "forced_source": force, "A": A, "U_offsets": U,
        "x_hex": hex(x), "period_hex": hex(period),
        "phases": phases,
        "source_load_numerator": sum(source_load[a] for a in A),
        "union_load_numerator": sum(loads[i] for i in U),
    }


def verify_witness(record):
    M = int(record["M"])
    weights = {int(p): int(w) for p, w in record["weights"].items()}
    denominator = int(record["denominator"])
    assert all(0 <= w <= denominator for w in weights.values())
    x = int(record["x_hex"], 16)
    primes, factors = sieve(M)
    phases = [tuple(map(int, t)) for t in record["phases"]]
    assert [p for p, _, _ in phases] == primes
    for p, modulus, r in phases:
        assert x % modulus == r
        q = modulus
        while q % p == 0:
            q //= p
        assert q == 1
        assert all((r + i) % modulus for i in range(1, M + 1))
    A = list(map(int, record["A"]))
    assert len(A) == len(set(A)) and all(2 <= a <= M for a in A)
    src = 0
    for a in A:
        load = sum(weights.get(p, 0) * e for p, e in factors[a].items())
        assert load > 2 * denominator
        src += load
    U = sorted({i for a in A for p in factors[a]
                for i in range(((-x) % (a // p)) or (a // p), M + 1, a // p)})
    assert U == record["U_offsets"]
    loads = target_loads(M, phases, weights)
    dst = sum(loads[i] for i in U)
    assert src == record["source_load_numerator"]
    assert dst == record["union_load_numerator"]
    assert src - dst == record["profit_numerator"]
    return {"valid": True, "M": M, "source_count": len(A),
            "profit": str(Fraction(src - dst, denominator)),
            "nonempty_counterexample_to_strict_surplus": bool(A) and src >= dst}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--M", type=int, default=1000)
    parser.add_argument("--mode", choices=["prefix", "center", "greedy", "spread", "park"], default="greedy")
    parser.add_argument("--profile", choices=["unit", "half", "light23", "heavy2", "large", "rough"], default="light23")
    parser.add_argument("--force", type=int)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args()
    if args.verify:
        record = json.loads(args.verify.read_text())
        print(json.dumps(verify_witness(record), indent=2))
        return
    primes, _ = sieve(args.M)
    if args.profile == "unit":
        denominator, weights = 1, {p: 1 for p in primes}
    elif args.profile == "half":
        denominator, weights = 2, {p: 1 for p in primes}
    elif args.profile == "light23":
        denominator, weights = 4, {p: (1 if p <= 3 else 4) for p in primes}
    elif args.profile == "heavy2":
        denominator, weights = 100, {p: (100 if p == 2 else 51) for p in primes}
    elif args.profile == "large":
        denominator, weights = 100, {p: (51 if p <= isqrt(args.M) else 100) for p in primes}
    else:
        denominator, weights = 1, {p: 1 for p in primes if p >= 5}
    record = closure(args.M, weights, denominator, args.mode, args.force)
    assert verify_witness(record)["valid"]
    if args.output:
        args.output.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({k: record[k] for k in ["M", "mode", "denominator",
                    "candidate_count", "source_count", "bank_union_count",
                    "profit_numerator", "forced_source"]}, indent=2))


if __name__ == "__main__":
    main()
