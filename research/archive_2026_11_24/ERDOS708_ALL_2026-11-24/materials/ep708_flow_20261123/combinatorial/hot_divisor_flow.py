"""Exact finite flow probes, not a proof of J_weak.

Source a has demand X(a)-threshold; target b has capacity (X(b)-1)+.
Edges mean X(gcd(a,b))>1, implemented using minimal hot divisors.
Every phase pattern is lifted to a genuine positive integer interval.
"""
from __future__ import annotations

from collections import deque
import importlib.util
from itertools import combinations
import json
from math import gcd
from pathlib import Path
import random

HERE = Path(__file__).resolve().parent
# Resolve from the shared workspace, independently of the launch directory.
HELPER = HERE.parents[1] / "ep708_global_20261123/audit/joint_bank_closure.py"
spec = importlib.util.spec_from_file_location("old_bank_helpers", HELPER)
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)


def balanced_phases(M, primes, weights, denominator, rng):
    """Choose exact prime-power phases greedily against the total hinge."""
    loads = [0] * (M + 1)
    phases = []
    ordered = list(primes)
    rng.shuffle(ordered)
    for p in ordered:
        weight = weights.get(p, 0)
        power = p
        while power <= 3 * M:
            power *= p
        modulus = power * p
        choices = list(range(1, p + 1))
        rng.shuffle(choices)
        best = None
        for r in choices:
            representative = M + r
            additions = []
            increment = 0
            first = representative % p or p
            for i in range(first, M + 1, p):
                n = representative - i
                e = 0
                while n % p == 0:
                    n //= p
                    e += 1
                addition = weight * e
                additions.append((i, addition))
                increment += max(loads[i] + addition - denominator, 0) - max(loads[i] - denominator, 0)
            if best is None or increment < best[0]:
                best = (increment, representative, additions)
        _, representative, additions = best
        for i, addition in additions:
            loads[i] += addition
        residue = (power - representative) % modulus
        phases.append((p, modulus, residue))
    return sorted(phases), loads


def probe(M, weights, denominator, threshold, mode="center", seed=0):
    import numpy as np
    from scipy.sparse import coo_matrix
    from scipy.sparse.csgraph import maximum_flow

    primes, factors = helper.sieve(M)
    prefix = [0] * (M + 1)
    for a in range(2, M + 1):
        prefix[a] = sum(weights.get(p, 0) * e for p, e in factors[a].items())
    candidates = [a for a in range(2, M + 1) if prefix[a] > threshold]
    minimal_hot = [
        d for d in range(2, M + 1)
        if prefix[d] > denominator
        and all(prefix[d] - weights.get(p, 0) <= denominator for p in factors[d])
    ]
    if mode == "balanced":
        phases, loads = balanced_phases(M, primes, weights, denominator, random.Random(seed))
        assert loads == helper.target_loads(M, phases, weights)
    else:
        phases = helper.actual_phases(M, primes, mode, set(weights))
        loads = helper.target_loads(M, phases, weights)
    x, period = helper.crt(phases)

    source_id = {a: 1 + i for i, a in enumerate(candidates)}
    divisor_id = {d: 1 + len(candidates) + i for i, d in enumerate(minimal_hot)}
    target_start = 1 + len(candidates) + len(minimal_hot)
    sink = target_start + M
    profits = {a: prefix[a] - threshold for a in candidates}
    caps = [max(value - denominator, 0) for value in loads]
    total = sum(profits.values())
    infinity = total + sum(caps) + 1
    rows, cols, values = [], [], []

    def edge(u, v, cap):
        if cap:
            rows.append(u)
            cols.append(v)
            values.append(cap)

    for a in candidates:
        edge(0, source_id[a], profits[a])
    for d in minimal_hot:
        for a in range(d, M + 1, d):
            if a in source_id:
                edge(source_id[a], divisor_id[d], infinity)
        first = (-x) % d or d
        for i in range(first, M + 1, d):
            assert loads[i] > denominator
            edge(divisor_id[d], target_start + i - 1, infinity)
    for i in range(1, M + 1):
        edge(target_start + i - 1, sink, caps[i])
    capacity = coo_matrix(
        (np.array(values, dtype=np.int64), (rows, cols)),
        shape=(sink + 1, sink + 1),
    ).tocsr()
    assert int(capacity.data.max(initial=0)) < 2 ** 31
    result = maximum_flow(capacity, 0, sink)
    residual = (capacity - result.flow).tocsr()
    reached = {0}
    queue = deque([0])
    while queue:
        u = queue.popleft()
        for j in range(residual.indptr[u], residual.indptr[u + 1]):
            v = int(residual.indices[j])
            if residual.data[j] > 0 and v not in reached:
                reached.add(v)
                queue.append(v)
    A = [a for a in candidates if source_id[a] in reached]
    neighborhood = [
        i for i in range(1, M + 1)
        if any(prefix[gcd(a, (x + i) % a)] > denominator for a in A)
    ]
    profit = sum(profits[a] for a in A) - sum(caps[i] for i in neighborhood)
    assert profit == total - int(result.flow_value)
    return {
        "M": M,
        "denominator": denominator,
        "threshold_numerator": threshold,
        "mode": mode,
        "seed": seed,
        "candidate_count": len(candidates),
        "minimal_hot_divisor_count": len(minimal_hot),
        "maximum_cut_deficiency_numerator": profit,
        "cut_sources": A,
        "cut_target_offsets": neighborhood,
        "weights": {str(p): w for p, w in weights.items() if w},
        "x_hex": hex(x),
        "period_hex": hex(period),
        "phases": phases,
        "scope": "Auxiliary hot-divisor flow; no optimality or minimal-counterexample assertion is inferred from a finite probe.",
    }


def run_batch():
    records = []
    for M in (100, 250, 500, 1000):
        primes, _ = helper.sieve(M)
        profiles = [
            ("unit", 20, {p: 20 for p in primes}),
            ("half", 20, {p: 10 for p in primes}),
            ("light23", 20, {p: (1 if p <= 3 else 20) for p in primes}),
            ("heavy2", 20, {p: (20 if p == 2 else 11) for p in primes}),
        ]
        rng = random.Random(1937 + M)
        for j in range(4):
            profiles.append((f"random{j}", 20, {p: rng.randrange(1, 21) for p in primes}))
        for name, denominator, weights in profiles:
            for mode in ("center", "balanced"):
                record = probe(M, weights, denominator, 2 * denominator, mode, seed=47)
                if record["maximum_cut_deficiency_numerator"] > 0:
                    (HERE / "hot_divisor_flow_counterexample.json").write_text(json.dumps(record, indent=2) + "\n")
                    print(json.dumps({"found": True, "profile": name, **{k: record[k] for k in ("M", "mode", "candidate_count", "maximum_cut_deficiency_numerator")}}), flush=True)
                    return
                records.append({k: record[k] for k in ("M", "mode", "candidate_count", "minimal_hot_divisor_count", "maximum_cut_deficiency_numerator")} | {"profile": name})
        print(json.dumps({"completed_M": M, "probes": len(records)}), flush=True)
    (HERE / "hot_divisor_flow_probes.json").write_text(json.dumps(records, indent=2) + "\n")
    print(json.dumps({"found": False, "probes": len(records)}), flush=True)


if __name__ == "__main__":
    run_batch()
