#!/usr/bin/env python3
"""Exact, shift-uniform sufficient recognition certificates for Erdos 708.

This program recognizes some source sets A, with a FIXED ambient M>=max(A),
for which every positive M-term interval has a product cover of size <=2|A|.
It does not construct the cover or solve the unrestricted problem. Failure
returns UNKNOWN, never a counterexample. All arithmetic and verification use
the Python standard library. The Wang base case invokes an external theorem;
verification checks its numerical hypothesis, not a formal proof of it.

Usage:
  python exact2n_recognition.py --sources input.json --output certificate.json
  python exact2n_recognition.py --verify certificate.json
  python exact2n_recognition.py --demo --output recognition_examples.json
  python exact2n_recognition.py --verify recognition_examples.json

Input is an integer list or {"sources": [...], "M": integer}. Distinct sources
must be >=2. If omitted, M defaults to max(A), or 1 for the empty set.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from copy import deepcopy
from fractions import Fraction
from functools import lru_cache
from itertools import combinations_with_replacement
import json
from math import prod
from pathlib import Path
from typing import Any


SCHEMA = "erdos708-exact2n-recognition-v1"
WANG_REFERENCE = {
    "author": "Ziming Wang",
    "work": "Fractional-to-Integer Transference and Five-Prime Bounds for Interval Divisor Covers",
    "section": "The quadratic coefficient-two gate",
    "url": "https://github.com/science-prince/erdos-708-interval-divisor-covers",
    "input": "M >= 16*m^2 implies a cover of size at most 2*m; ambient form of the proof",
    "status": "External mathematical theorem; its proof is not formally verified by this program.",
}


@lru_cache(maxsize=None)
def factor(a: int) -> tuple[tuple[int, int], ...]:
    """Exact trial division; no enumeration of interval shifts is used."""
    if isinstance(a, bool) or not isinstance(a, int) or a < 1:
        raise ValueError("Factorization requires a positive integer.")
    result = []
    p = 2
    while p * p <= a:
        if a % p == 0:
            e = 0
            while a % p == 0:
                a //= p
                e += 1
            result.append((p, e))
        p = 3 if p == 2 else p + 2
    if a > 1:
        result.append((a, 1))
    return tuple(result)


def normalize_sources(sources: list[int], M: int | None = None) -> tuple[list[int], int]:
    if not isinstance(sources, list):
        raise ValueError("Sources must be a JSON/Python list.")
    if any(isinstance(a, bool) or not isinstance(a, int) or a < 2 for a in sources):
        raise ValueError("Each source must be an integer at least two.")
    if len(sources) != len(set(sources)):
        raise ValueError("Source integers must be distinct.")
    A = sorted(sources)
    if M is None:
        M = max(A, default=1)
    if isinstance(M, bool) or not isinstance(M, int) or M < max(A, default=1):
        raise ValueError("The ambient M must be a positive integer >=max(A).")
    return A, M


def demand(A: list[int]) -> Counter[int]:
    total: Counter[int] = Counter()
    for a in A:
        total.update(dict(factor(a)))
    return total


def cofactor_hall_data(A: list[int], M: int) -> dict[str, Any]:
    """Recompute the exact floor/ceiling Hall condition from the sources.

    For each distinct d=a/Pmax(a)>1, with fibre size r_A(d), require
      floor(M/d) - sum_{q in Q, d*q<=M} ceil(M/(d*q)) >= r_A(d),
    where Q is the union of prime supports of all these cofactors.
    Prime sources are assigned to unused positions after the matching.
    The proof needs a<=M, not M=max(A).
    """
    fibres: dict[int, list[int]] = defaultdict(list)
    for a in A:
        fa = factor(a)
        d = a // fa[-1][0]
        if d > 1:
            if d * factor(d)[-1][0] > M:
                raise AssertionError("Cofactor smooth-part cutoff is invalid.")
            fibres[d].append(a)
    Q = sorted({p for d in fibres for p, _ in factor(d)})
    rows = []
    for d, members in sorted(fibres.items()):
        terms = {str(q): (M + d * q - 1) // (d * q) for q in Q if d * q <= M}
        lower = M // d - sum(terms.values())
        rows.append({
            "d": d,
            "source_preimages": members,
            "r_A_d": len(members),
            "floor_M_over_d": M // d,
            "ceiling_terms": terms,
            "neighborhood_lower_bound": lower,
            "margin": lower - len(members),
        })
    return {
        "Q_cofactor_prime_support": Q,
        "rows": rows,
        "passes": all(r["margin"] >= 0 for r in rows),
        "minimum_margin": min((r["margin"] for r in rows), default=None),
    }


def peel_evidence(A: list[int], M: int, a: int, rule: str,
                  p: int | None = None, q: int | None = None,
                  current_demand: Counter[int] | None = None,
                  current_members: set[int] | None = None) -> dict[str, Any] | None:
    """Check one proposed extension rule by recomputing current-set demands.

    Returns a numerical witness, or None if the chosen rule does not apply.
    No minimal-counterexample assumption is used: a cover of A minus {a} is
    supplied by the remainder of the certificate and extends by <=2 points.
    """
    if a not in (A if current_members is None else current_members):
        return None
    m = len(A)
    fa = dict(factor(a))
    if rule == "omega_at_most_two":
        omega = sum(fa.values())
        return {"Omega_source": omega} if omega <= 2 else None
    if rule == "two_prime_saturation":
        if (isinstance(p, bool) or not isinstance(p, int) or isinstance(q, bool)
                or not isinstance(q, int) or p not in fa or q not in fa or a % (p * q)):
            return None
        exponent = fa[p] - int(p == q)
        Dp = (demand(A) if current_demand is None else current_demand)[p]
        if p * q < 2 * m - 1 or Dp > q * exponent:
            return None
        return {
            "p": p, "q": q, "p_times_q": p * q,
            "required_candidate_threshold": 2 * m - 1,
            "D_p_current_sources": Dp,
            "v_p_source_over_q": exponent,
            "q_times_v_p_source_over_q": q * exponent,
            "source_over_pq": a // (p * q),
        }
    if rule == "prime_power_bank_saturation":
        if (isinstance(p, bool) or not isinstance(p, int) or isinstance(q, bool)
                or not isinstance(q, int) or p not in fa or q not in fa or a % q):
            return None
        d = a // q
        fd = factor(d)
        if len(fd) != 1 or fd[0][0] != p or m * d > M:
            return None
        return {
            "p": p, "q": q, "e": fd[0][1], "prime_power_bank": d,
            "floor_M_over_bank": M // d,
            "required_bank_count": m,
        }
    return None


def possible_peels(A: list[int], M: int) -> list[dict[str, Any]]:
    """Find one valid rule per removable source; no random trials or DFS."""
    choices = []
    current_demand = demand(A)
    current_members = set(A)
    for a in A:
        evidence = peel_evidence(A, M, a, "omega_at_most_two", current_members=current_members)
        if evidence is not None:
            choices.append({"source": a, "rule": "omega_at_most_two", "evidence": evidence})
            continue
        fa = factor(a)
        found = None
        for p, _ in fa:
            for q, _ in fa:
                evidence = peel_evidence(A, M, a, "two_prime_saturation", p, q,
                                         current_demand, current_members)
                if evidence is not None:
                    found = {"source": a, "rule": "two_prime_saturation", "evidence": evidence}
                    break
            if found is not None:
                break
        if found is not None:
            choices.append(found)
            continue
        for q, _ in fa:
            fd = factor(a // q)
            if len(fd) == 1:
                evidence = peel_evidence(A, M, a, "prime_power_bank_saturation", fd[0][0], q,
                                         current_members=current_members)
                if evidence is not None:
                    choices.append({"source": a, "rule": "prime_power_bank_saturation", "evidence": evidence})
                    break
    return choices


def pick_peel(A: list[int], choices: list[dict[str, Any]]) -> dict[str, Any]:
    """Prefer removing an exclusive small cofactor prime, then smaller a.

    This only chooses between already proven rules and has no role in proof
    verification. It makes mixed sparse-support examples easier to inspect.
    """
    owners: dict[int, set[int]] = defaultdict(set)
    for a in A:
        d = a // factor(a)[-1][0]
        for p, _ in factor(d):
            owners[p].add(a)
    scores = Counter()
    for p, members in owners.items():
        if len(members) == 1:
            scores[next(iter(members))] += Fraction(1, p)
    return max(choices, key=lambda c: (scores[c["source"]], -c["source"]))


def find_base(A: list[int], M: int) -> dict[str, Any] | None:
    m = len(A)
    common = {"m": m, "sources": A.copy()}
    if not A:
        return {**common, "rule": "empty", "evidence": {}}
    if M <= 2 * m:
        return {**common, "rule": "full_interval", "evidence": {"M": M, "cover_budget": 2 * m}}
    if M >= 16 * m * m:
        return {**common, "rule": "wang_quadratic", "evidence": {"M": M, "required_M": 16 * m * m}}
    hall = cofactor_hall_data(A, M)
    if hall["passes"]:
        return {**common, "rule": "cofactor_hall", "evidence": hall}
    return None


def recognize(sources: list[int], M: int | None = None) -> dict[str, Any]:
    original, M = normalize_sources(sources, M)
    A = original.copy()
    steps = []
    while True:
        base = find_base(A, M)
        if base is not None:
            status = "CERTIFIED"
            break
        choices = possible_peels(A, M)
        if not choices:
            status = "UNKNOWN"
            hall = cofactor_hall_data(A, M)
            base = {"rule": "unresolved", "m": len(A), "sources": A.copy(),
                    "evidence": {"first_failed_hall_row": next(r for r in hall["rows"] if r["margin"] < 0)}}
            break
        selected = pick_peel(A, choices)
        steps.append({"m_before": len(A), **selected})
        A.remove(selected["source"])
    return {
        "schema": SCHEMA,
        "status": status,
        "sources": original,
        "ambient_M": M,
        "initial_n": len(original),
        "cover_budget": 2 * len(original),
        "shift_scope": "Every integer x>=0; targets x+1,...,x+M.",
        "claim": ("For every stated shift there exists a subset of at most 2*n distinct targets whose product is divisible by the source product."
                  if status == "CERTIFIED" else "No conclusion; this sufficient recognition procedure stopped."),
        "peeled_sources_in_order": [s["source"] for s in steps],
        "steps": steps,
        "base_case": base,
        "external_theorems_used": [WANG_REFERENCE] if base["rule"] == "wang_quadratic" else [],
        "method": "Exact sufficient rules at fixed ambient M; deterministic peeling, no interval or CRT search.",
        "limitations": [
            "This is recognition, not a constructed interval cover.",
            "UNKNOWN is not a mathematical obstruction or counterexample.",
            "Unrestricted exact and asymptotic Erdos 708 remain unresolved by this work.",
            "Proofs have internal AI-assisted audits, not formal verification or external referee approval; no priority claim.",
        ],
    }


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError("Certificate rejected: " + message)


def verify_certificate(cert: dict[str, Any]) -> dict[str, Any]:
    """Replay and independently recompute all criteria from the initial A.

    Does not call recognize, find_base, possible_peels, or pick_peel to validate
    a CERTIFIED result. It accepts any valid deletion order. All witness totals
    and Hall rows are recomputed, rather than trusting stored pass flags.
    """
    require(cert.get("schema") == SCHEMA, "unknown schema")
    A, M = normalize_sources(cert["sources"], cert["ambient_M"])
    require(cert["sources"] == A, "initial sources must be sorted and distinct")
    n = len(A)
    require(cert.get("initial_n") == n and cert.get("cover_budget") == 2 * n, "incorrect initial count/budget")
    steps = cert["steps"]
    require(cert.get("peeled_sources_in_order") == [s["source"] for s in steps], "deletion order disagrees")
    for index, step in enumerate(steps):
        a, rule = step["source"], step["rule"]
        require(step.get("m_before") == len(A), f"wrong current size at step {index}")
        require(a in A, f"source {a} absent/reused at step {index}")
        recorded = step["evidence"]
        computed = peel_evidence(A, M, a, rule, recorded.get("p"), recorded.get("q"))
        require(computed is not None, f"invalid extension rule at step {index}")
        require(recorded == computed, f"incorrect numerical witness at step {index}")
        A.remove(a)
    base = cert["base_case"]
    require(base.get("sources") == A and base.get("m") == len(A), "incorrect residual sources")
    m, rule, evidence = len(A), base["rule"], base["evidence"]
    if rule == "empty":
        require(m == 0 and evidence == {}, "invalid empty base")
    elif rule == "full_interval":
        require(M <= 2 * m, "full interval exceeds residual budget")
        require(evidence == {"M": M, "cover_budget": 2 * m}, "wrong full-interval evidence")
    elif rule == "wang_quadratic":
        require(m > 0 and M >= 16 * m * m, "Wang numerical hypothesis fails")
        require(evidence == {"M": M, "required_M": 16 * m * m}, "wrong Wang evidence")
    elif rule == "cofactor_hall":
        computed = cofactor_hall_data(A, M)
        require(computed["passes"], "Hall inequality fails")
        require(evidence == computed, "Hall numerical data disagree with sources")
    elif rule == "unresolved":
        require(m > 0 and M > 2 * m and M < 16 * m * m, "an elementary base already applies")
        hall = cofactor_hall_data(A, M)
        require(not hall["passes"], "Hall already certifies the residual")
        require(not possible_peels(A, M), "a stated peeling rule remains applicable")
        first = next(r for r in hall["rows"] if r["margin"] < 0)
        require(evidence == {"first_failed_hall_row": first}, "incorrect UNKNOWN diagnostic")
    else:
        require(False, "unknown base rule")
    status = "UNKNOWN" if rule == "unresolved" else "CERTIFIED"
    require(cert.get("status") == status, "incorrect conclusion status")
    external = [WANG_REFERENCE] if rule == "wang_quadratic" else []
    require(cert.get("external_theorems_used") == external, "external theorem use is not accurately disclosed")
    return {
        "status": status,
        "n": n, "ambient_M": M, "verified_peel_count": len(steps),
        "base_rule": rule, "residual_m": m,
        "all_numerical_criteria_recomputed_from_sources": True,
        "fixed_ambient_M_preserved": True,
        "invokes_external_Wang_theorem": rule == "wang_quadratic",
        "conclusion": "Exact 2*n existence bound certified for every x>=0." if status == "CERTIFIED" else "UNKNOWN; no impossibility claim.",
    }


def demo() -> dict[str, Any]:
    """Structured examples, including genuine peeling-to-Hall combinations."""
    P = [11, 13, 17, 19, 23]
    R = sorted(prod(t) for t in combinations_with_replacement(P, 3))
    require(len(R) == 35 and max(R) == 12167, "demo cubic family changed")
    cases = {}
    inputs = [
        ("mixed_omega_then_hall", sorted(R + [6, 9]), 12167, "omega_at_most_two", 6),
        ("mixed_prime_power_then_hall", sorted(R + [8, 27]), 12167, "prime_power_bank_saturation", 8),
        ("mixed_pair_then_hall", sorted(R + [4096, 11875]), 12167, "two_prime_saturation", 11875),
        ("remove_maximum_keep_ambient", sorted(R + [27, 128 * 101]), 128 * 101, "two_prime_saturation", 128 * 101),
    ]
    for name, A, M, expected_rule, expected_source in inputs:
        before = cofactor_hall_data(A, M)
        require(not before["passes"], f"{name}: direct Hall unexpectedly passes")
        result = recognize(A, M)
        checked = verify_certificate(result)
        require(result["status"] == "CERTIFIED", f"{name}: recognition failed")
        require(len(result["steps"]) == 1, f"{name}: expected one meaningful deletion")
        require(result["steps"][0]["source"] == expected_source, f"{name}: wrong deletion")
        require(result["steps"][0]["rule"] == expected_rule, f"{name}: wrong rule")
        require(result["base_case"]["rule"] == "cofactor_hall", f"{name}: not a Hall residual")
        require(M < 16 * result["base_case"]["m"] ** 2, f"{name}: already in Wang range")
        cases[name] = {
            "description": "35 cubic monomials on {11,13,17,19,23}, plus the two displayed exceptional sources.",
            "exceptional_sources": sorted(set(A) - set(R)),
            "direct_hall_passes": False,
            "first_direct_hall_failure": next(r for r in before["rows"] if r["margin"] < 0),
            "certificate": result, "verification": checked,
        }
    require(max(cases["remove_maximum_keep_ambient"]["certificate"]["base_case"]["sources"]) < 12928,
            "ambient example did not remove the maximum source")
    # A genuinely recursive trace: the current source count is recomputed at
    # both steps, while the ambient interval remains unchanged.
    recursive_A = sorted(R + [8, 27, 125])
    recursive = recognize(recursive_A, 12167)
    require([(s["source"], s["m_before"]) for s in recursive["steps"]] == [(8, 38), (27, 37)],
            "recursive trace changed")
    require(recursive["base_case"]["rule"] == "cofactor_hall", "recursive residual did not pass Hall")
    before = cofactor_hall_data(recursive_A, 12167)
    require(not before["passes"], "recursive direct Hall unexpectedly passes")
    cases["recursive_prime_power_then_hall"] = {
        "description": "The same 35 cubic monomials plus 8,27,125; delete 8 then 27 at current sizes 38 and 37.",
        "exceptional_sources": [8, 27, 125],
        "direct_hall_passes": False,
        "first_direct_hall_failure": next(r for r in before["rows"] if r["margin"] < 0),
        "certificate": recursive, "verification": verify_certificate(recursive),
    }
    # Purposeful unresolved smooth source family, with no eligible pair product.
    # This is NOT an original counterexample or a randomized cover search.
    smooth = [a for a in range(2049, 4096) if factor(a)[-1][0] <= 11]
    unresolved_A = sorted(smooth[:63] + [4096])
    require(len(unresolved_A) == 64, "too few smooth sources")
    unknown = recognize(unresolved_A, 4096)
    require(unknown["status"] == "UNKNOWN", "the deliberately unresolved example changed")
    cases["unresolved_smooth_core"] = {
        "description": "64 sources in (2048,4096] with all prime factors <=11; tests UNKNOWN semantics only.",
        "certificate": unknown, "verification": verify_certificate(unknown),
    }
    for name, A, M, expected in [
        ("direct_hall", R, 12167, "cofactor_hall"),
        ("whole_interval_base", list(range(2, 11)), 10, "full_interval"),
        ("external_wang_base", [8, 27, 125], 144, "wang_quadratic"),
        ("empty_base", [], 17, "empty"),
    ]:
        result = recognize(A, M)
        require(result["base_case"]["rule"] == expected, "incorrect elementary base in demo")
        cases[name] = {"certificate": result, "verification": verify_certificate(result)}
    # Reject a forged demand, a changed fixed M, and a changed Hall row.
    rejected = []
    original = cases["mixed_pair_then_hall"]["certificate"]
    bad = deepcopy(original)
    bad["steps"][0]["evidence"]["D_p_current_sources"] += 1
    for label, forged in [("altered_source_demand", bad)]:
        try:
            verify_certificate(forged)
        except ValueError:
            rejected.append(label)
        else:
            raise AssertionError("Forged certificate accepted.")
    bad = deepcopy(cases["remove_maximum_keep_ambient"]["certificate"])
    bad["ambient_M"] = 12167
    try:
        verify_certificate(bad)
    except ValueError:
        rejected.append("changed_ambient_below_original_maximum")
    else:
        raise AssertionError("Changed ambient length was accepted.")
    bad = deepcopy(original)
    bad["base_case"]["evidence"]["rows"][0]["neighborhood_lower_bound"] += 1
    try:
        verify_certificate(bad)
    except ValueError:
        rejected.append("altered_Hall_lower_bound")
    else:
        raise AssertionError("Forged Hall row accepted.")
    return {
        "schema": "erdos708-exact2n-recognition-examples-v1",
        "purpose": "Structured demonstrations of sufficient recognition and exact verification; no claim about general g(n).",
        "cases": cases,
        "invalid_certificate_rejection_checks": rejected,
    }


def verify_document(document: dict[str, Any]) -> dict[str, Any]:
    if document.get("schema") == SCHEMA:
        return verify_certificate(document)
    require(document.get("schema") == "erdos708-exact2n-recognition-examples-v1", "unknown document type")
    results = {}
    for name, case in document["cases"].items():
        cert = case["certificate"]
        results[name] = verify_certificate(cert)
        if "direct_hall_passes" in case:
            recomputed = cofactor_hall_data(cert["sources"], cert["ambient_M"])
            require(case["direct_hall_passes"] == recomputed["passes"], "incorrect direct-Hall comparison")
            require(case["first_direct_hall_failure"] == next(r for r in recomputed["rows"] if r["margin"] < 0),
                    "incorrect direct-Hall failure witness")
        require(case["verification"] == results[name], "stored verification summary disagrees")
    return {"examples_reverified": results}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--sources", type=Path)
    modes.add_argument("--verify", type=Path)
    modes.add_argument("--demo", action="store_true")
    parser.add_argument("--M", type=int, help="Override input ambient length; it is retained after deletions.")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.verify:
        if args.M is not None or args.output:
            parser.error("Verification reads the original M from the certificate and writes no new artifact.")
        print(json.dumps(verify_document(json.loads(args.verify.read_text())), indent=2))
    else:
        if args.demo:
            if args.M is not None:
                parser.error("The structured demo has fixed inputs.")
            result = demo()
            default_name = "recognition_examples.json"
            summary = {name: case["verification"] for name, case in result["cases"].items()}
        else:
            raw = json.loads(args.sources.read_text())
            A = raw if isinstance(raw, list) else raw["sources"]
            ambient = args.M if args.M is not None else (None if isinstance(raw, list) else raw.get("M"))
            result = recognize(A, ambient)
            summary = verify_certificate(result)
            default_name = "recognition_certificate.json"
        target = args.output or Path(__file__).with_name(default_name)
        target.write_text(json.dumps(result, indent=2) + "\n")
        print(json.dumps({"saved": str(target), "verification": summary}, indent=2))
