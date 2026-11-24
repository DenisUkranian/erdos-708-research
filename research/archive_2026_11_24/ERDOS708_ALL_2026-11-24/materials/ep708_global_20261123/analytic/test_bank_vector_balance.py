"""Search for exact counterexamples to a proposed bank-union vector lemma.

This is not a search for counterexamples to Erdos 708.  A returned set only
meets the necessary bank-union demand inequalities, which are weaker than
full LP optimality.  Every returned arithmetic certificate is checked exactly.
"""

import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix


def prime_divisors(n):
    out = []
    q = 2
    while q * q <= n:
        if n % q == 0:
            out.append(q)
            while n % q == 0:
                n //= q
        q += 1
    if n > 1:
        out.append(n)
    return out


def vp(n, p):
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def investigate(M, shift, primes, seconds=4):
    candidates = [
        a for a in range(2, M + 1)
        if sum(vp(a, p) for p in primes) >= 3
    ]
    if not candidates:
        return {"M": M, "shift": shift, "status": "empty"}
    targets = list(range(shift + 1, shift + M + 1))
    na, nb = len(candidates), len(targets)
    rows, cols, vals, lower = [], [], [], []
    banks = []
    for ia, a in enumerate(candidates):
        ds = [a // q for q in prime_divisors(a)]
        bank = [ib for ib, b in enumerate(targets) if any(b % d == 0 for d in ds)]
        banks.append(bank)
        for ib in bank:
            row = len(lower)
            rows.extend([row, row])
            cols.extend([ia, na + ib])
            vals.extend([-1, 1])
            lower.append(0)
    for p in primes:
        row = len(lower)
        for ia, a in enumerate(candidates):
            v = vp(a, p)
            if v:
                rows.append(row)
                cols.append(ia)
                vals.append(v)
        for ib, b in enumerate(targets):
            v = vp(b, p)
            if v:
                rows.append(row)
                cols.append(na + ib)
                vals.append(-v)
        lower.append(0)
    row = len(lower)
    for ia in range(na):
        rows.append(row)
        cols.append(ia)
        vals.append(1)
    lower.append(1)
    matrix = coo_matrix(
        (vals, (rows, cols)), shape=(len(lower), na + nb)
    ).tocsc()
    objective = np.r_[-np.ones(na), np.full(nb, 1e-6)]
    result = milp(
        objective,
        integrality=np.ones(na + nb),
        bounds=Bounds(np.zeros(na + nb), np.ones(na + nb)),
        constraints=LinearConstraint(matrix, np.asarray(lower), np.inf),
        options={"time_limit": seconds, "mip_rel_gap": 0},
    )
    record = {
        "M": M, "shift": shift, "primes": primes,
        "candidate_count": na, "solver_status": int(result.status),
        "message": result.message,
    }
    if result.x is None:
        return record
    indices = [i for i in range(na) if result.x[i] > 0.5]
    A = [candidates[i] for i in indices]
    union_indices = sorted({ib for i in indices for ib in banks[i]})
    U = [targets[i] for i in union_indices]
    source_demand = [sum(vp(a, p) for a in A) for p in primes]
    union_supply = [sum(vp(b, p) for b in U) for p in primes]
    assert A and all(
        sum(vp(a, p) for p in primes) >= 3 for a in A
    )
    assert all(d >= v for d, v in zip(source_demand, union_supply))
    heavy_targets = [
        b for b in targets if sum(vp(b, p) for p in primes) > 1
    ]
    full_supply = [
        sum(vp(b, p) for b in heavy_targets) for p in primes
    ]
    record.update(
        A=A, U=U, source_demand=source_demand,
        union_supply=union_supply, full_heavy_supply=full_supply,
        full_heavy_count=len(heavy_targets),
    )
    return record


if __name__ == "__main__":
    cases = [
        (60, 1000, [2, 3, 5, 7]),
        (120, 2310, [2, 3, 5, 7, 11, 13]),
        (240, 30030, [2, 3, 5, 7, 11, 13, 17]),
        (400, 100000, [2, 3, 5, 7, 11, 13, 17, 19]),
    ]
    records = []
    for case in cases:
        record = investigate(*case)
        records.append(record)
        print(json.dumps(record), flush=True)
    Path(__file__).with_name("bank_vector_balance_cases.json").write_text(
        json.dumps(records, indent=2)
    )
