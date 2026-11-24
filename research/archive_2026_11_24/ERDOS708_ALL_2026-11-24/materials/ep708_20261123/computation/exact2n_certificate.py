#!/usr/bin/env python3
"""Exact finite sufficient certificates for an Erdős 708 cover of size <=2n.

Certificate checks use only Python integers and fractions.Fraction. SciPy is
imported only by the optional constructive witness routine. The finite
conditions are sufficient, not necessary; a failed check proves no obstruction.
A successful finite check is not a computational proof of the general theorem.

Examples:
  python exact2n_certificate.py --demo --output exact2n_demo_results.json
  python exact2n_certificate.py --verify exact2n_demo_results.json
  python exact2n_certificate.py --sources sources.json --construct --x 100000

Input JSON may be an integer list, or {"sources": [...], "M": ..., "x": ...}.
Large interval endpoints and selected values are serialized as decimal strings.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, combinations_with_replacement
import json
from math import isqrt, prod
from pathlib import Path
from typing import Any


@lru_cache(maxsize=None)
def factor(n: int) -> tuple[tuple[int, int], ...]:
    """Trial-division factorization; adequate for the finite examples here."""
    if n < 1:
        raise ValueError('Factorization requires a positive integer.')
    result: list[tuple[int, int]] = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            result.append((p, e))
        p = 3 if p == 2 else p + 2
    if n > 1:
        result.append((n, 1))
    return tuple(result)


def primes_between(lo: int, hi: int) -> list[int]:
    return [p for p in range(max(2, lo), hi + 1) if factor(p) == ((p, 1),)]


def rational_record(value: Fraction) -> dict[str, int | str]:
    return {'numerator': value.numerator, 'denominator': value.denominator,
            'exact': str(value)}


def source_data(sources: list[int], M: int | None = None) -> dict[str, Any]:
    if not sources:
        raise ValueError('Supply a nonempty set of sources.')
    if any(isinstance(a, bool) or not isinstance(a, int) or a < 2 for a in sources):
        raise ValueError('Every source must be an integer at least two.')
    if len(set(sources)) != len(sources):
        raise ValueError('The theorem requires distinct source integers.')
    A = sorted(sources)
    if M is None:
        M = max(A)
    if isinstance(M, bool) or not isinstance(M, int) or M < max(A):
        raise ValueError('M must be an integer at least max(A).')
    facts = {a: dict(factor(a)) for a in A}
    composites = [a for a in A if sum(facts[a].values()) >= 2]
    primes = [a for a in A if a not in composites]
    quotient = {a: a // max(facts[a]) for a in A}
    preimages: dict[int, list[int]] = {}
    for a in composites:
        d = quotient[a]
        preimages.setdefault(d, []).append(a)
        assert d > 1 and d * max(dict(factor(d))) <= a <= M
    # Prime-only sources are deliberately absent from P: they have no
    # preimages of a nonunit cofactor and are assigned after matching.
    P = sorted({p for a in composites for p in facts[a]})
    Q = sorted({q for d in preimages for q, _ in factor(d)})
    demand: Counter[int] = Counter()
    for a in A:
        demand.update(facts[a])
    return {'A': A, 'M': M, 'facts': facts, 'composites': composites,
            'prime_sources': primes, 'quotient': quotient,
            'preimages': preimages, 'P': P, 'Q': Q,
            'demand': dict(sorted(demand.items()))}


def check_certificate(sources: list[int], M: int | None = None) -> dict[str, Any]:
    """Check both sufficient criteria exactly, independently of the shift.

    Integer condition, for each distinct nonunit cofactor d:
      floor(M/d) - sum_{q in Q, dq<=M} ceil(M/(dq)) >= r_A(d).

    Rational cofactor-support condition, T=M/d:
      sum_{q in Q,q<=T}1/q + (pi_Q(T)+pi_P(T)+1)/T <= 1.
    """
    data = source_data(sources, M)
    A, M, P, Q = data['A'], data['M'], data['P'], data['Q']
    rows = []
    for d, preimages in sorted(data['preimages'].items()):
        eligible_q = [q for q in Q if d * q <= M]
        eligible_p = [p for p in P if d * p <= M]
        ceiling_terms = {q: (M + d * q - 1) // (d * q) for q in eligible_q}
        integer_lower = M // d - sum(ceiling_terms.values())
        multiplicity = len(preimages)
        mu_q = sum((Fraction(1, q) for q in eligible_q), Fraction(0))
        analytic = mu_q + Fraction((len(eligible_q) + len(eligible_p) + 1) * d, M)
        integer_pass = integer_lower >= multiplicity
        analytic_pass = analytic <= 1
        # The rational sufficient bound is weaker than the exact integer one.
        if analytic_pass and not integer_pass:
            raise AssertionError('Analytic criterion must imply the integer criterion.')
        # Distinct sources with this cofactor have distinct removed primes.
        removed = [a // d for a in preimages]
        assert len(set(removed)) == multiplicity
        assert all(p in eligible_p and factor(p) == ((p, 1),) for p in removed)
        rows.append({
            'd': d, 'T': rational_record(Fraction(M, d)),
            'source_preimages': preimages, 'r_A_d': multiplicity,
            'floor_M_over_d': M // d,
            'ceiling_terms': {str(q): v for q, v in ceiling_terms.items()},
            'integer_neighborhood_lower_bound': integer_lower,
            'integer_margin': integer_lower - multiplicity,
            'integer_criterion_passes': integer_pass,
            'pi_Q_T': len(eligible_q), 'pi_P_T': len(eligible_p),
            'mu_Q_T': rational_record(mu_q),
            'analytic_value': rational_record(analytic),
            'analytic_criterion_passes': analytic_pass,
        })
    integer_ok = all(row['integer_criterion_passes'] for row in rows)
    analytic_ok = all(row['analytic_criterion_passes'] for row in rows)
    worst = max((Fraction(row['analytic_value']['numerator'],
                          row['analytic_value']['denominator']) for row in rows),
                default=Fraction(0))
    return {
        'scope': 'Finite sufficient source certificate, valid for every positive shift.',
        'sources': A, 'n': len(A), 'M': M, 'M_equals_max_source': M == max(A),
        'composite_source_count': len(data['composites']),
        'prime_source_count': len(data['prime_sources']),
        'P_composite_source_support': P, 'Q_cofactor_support': Q,
        'distinct_nonunit_cofactors': len(rows),
        'integer_criterion_passes': integer_ok,
        'analytic_criterion_passes': analytic_ok,
        'max_analytic_value': rational_record(worst),
        'min_integer_margin': min((r['integer_margin'] for r in rows), default=None),
        'exact_2n_conclusion_certified': integer_ok,
        'conclusion_if_check_fails': 'No conclusion: these conditions are sufficient only.',
        'cofactors': rows,
    }


def valuation(n: int, p: int) -> int:
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def verify_cover(sources: list[int], M: int, x: int,
                 positions: list[int]) -> dict[str, Any]:
    """Independent exact check of the produced finite product-cover witness."""
    data = source_data(sources, M)
    if x < 0:
        raise ValueError('This checker uses positive intervals x+1,...,x+M.')
    if len(set(positions)) != len(positions):
        raise AssertionError('A target position was reused.')
    if any(j < 1 or j > M for j in positions):
        raise AssertionError('A selected target lies outside the interval.')
    demanded = data['demand']
    obtained = {p: sum(valuation(x + j, p) for j in positions) for p in demanded}
    if any(obtained[p] < demanded[p] for p in demanded):
        raise AssertionError('The selected product does not cover the source product.')
    if len(positions) > 2 * len(sources):
        raise AssertionError('The selected cover exceeds 2n.')
    return {
        'distinct_positions_verified': True,
        'all_positions_in_interval_verified': True,
        'product_divisibility_verified_by_exact_valuations': True,
        'size_at_most_2n_verified': True,
        'source_valuations': {str(p): e for p, e in demanded.items()},
        'cover_valuations': {str(p): e for p, e in obtained.items()},
    }


def construct_cover(sources: list[int], M: int | None = None,
                    x: int = 0) -> dict[str, Any]:
    """Build a quotient matching and repair at most n prime-valuation units.

    Only targets adjacent to composite rows are stored in the SciPy graph.
    Prime sources are assigned to unused positions afterward. No dense
    M-by-n matrix or multiplication of the enormous interval endpoints is used.
    """
    data = source_data(sources, M)
    A, M = data['A'], data['M']
    if not isinstance(x, int) or isinstance(x, bool) or x < 0:
        raise ValueError('x must be a nonnegative integer.')
    certificate = check_certificate(A, M)
    if not certificate['integer_criterion_passes']:
        raise ValueError('The sufficient criterion did not certify this input; '
                         'this is not a claim that no cover or matching exists.')
    composite_sources = data['composites']
    assignment: dict[int, int] = {}
    edge_count = 0
    graph_target_count = 0
    if composite_sources:
        import numpy as np
        from scipy.sparse import csr_matrix
        from scipy.sparse.csgraph import maximum_bipartite_matching
        neighbors: list[list[int]] = []
        target_union: set[int] = set()
        for a in composite_sources:
            d = data['quotient'][a]
            first = (-x) % d
            if first == 0:
                first = d
            row = list(range(first, M + 1, d))
            neighbors.append(row)
            target_union.update(row)
        targets = sorted(target_union)
        target_index = {j: i for i, j in enumerate(targets)}
        indptr = [0]
        indices = []
        for row in neighbors:
            indices.extend(target_index[j] for j in row)
            indptr.append(len(indices))
        graph = csr_matrix((np.ones(len(indices), dtype=np.int8),
                            np.asarray(indices, dtype=np.int32),
                            np.asarray(indptr, dtype=np.int32)),
                           shape=(len(composite_sources), len(targets)))
        matching = maximum_bipartite_matching(graph, perm_type='column')
        if len(matching) != len(composite_sources) or any(c < 0 for c in matching):
            raise AssertionError('Certified graph did not produce a complete matching.')
        assignment = {a: targets[int(c)] for a, c in zip(composite_sources, matching)}
        edge_count = len(indices)
        graph_target_count = len(targets)
    used = set(assignment.values())
    next_free = 1
    for a in data['prime_sources']:
        while next_free in used:
            next_free += 1
        if next_free > M:
            raise AssertionError('No position remains for a prime source.')
        assignment[a] = next_free
        used.add(next_free)
    assert len(used) == len(A)
    for a, j in assignment.items():
        assert (x + j) % data['quotient'][a] == 0
    initial_positions = sorted(used)
    demand = data['demand']
    current = {p: sum(valuation(x + j, p) for j in used) for p in demand}
    deficit = lambda: sum(max(demand[p] - current[p], 0) for p in demand)
    initial_deficit = deficit()
    if initial_deficit > len(A):
        raise AssertionError('Quotient matching left more than n prime units missing.')
    repairs = []
    while deficit():
        before = deficit()
        p = max((p for p in demand if current[p] < demand[p]),
                key=lambda q: (demand[q] - current[q], q))
        first = (-x) % p
        if first == 0:
            first = p
        j = next((j for j in range(first, M + 1, p) if j not in used), None)
        if j is None:
            raise AssertionError('Missing prime unit has no unused interval carrier.')
        used.add(j)
        for q in demand:
            current[q] += valuation(x + j, q)
        after = deficit()
        if after >= before:
            raise AssertionError('Repair did not reduce the integer valuation deficit.')
        repairs.append({'requested_prime': p, 'position': j,
                        'target_value': str(x + j),
                        'total_deficit_before': before, 'total_deficit_after': after})
    if len(repairs) > len(A):
        raise AssertionError('More than n repairs were used.')
    positions = sorted(used)
    verification = verify_cover(A, M, x, positions)
    return {
        'x': str(x), 'interval_first': str(x + 1), 'interval_last': str(x + M),
        'n': len(A), 'M': M, 'cover_size': len(positions), 'budget_2n': 2 * len(A),
        'scipy_graph_rows': len(composite_sources),
        'scipy_graph_compressed_columns': graph_target_count,
        'scipy_graph_edges': edge_count,
        'initial_matching_size': len(initial_positions),
        'initial_total_prime_deficit': initial_deficit,
        'repair_count': len(repairs),
        'matching': [
            {'source': a, 'removed_prime': max(data['facts'][a]),
             'cofactor': data['quotient'][a], 'position': assignment[a],
             'target_value': str(x + assignment[a])}
            for a in A],
        'initial_positions': initial_positions, 'repairs': repairs,
        'cover_positions': positions,
        'cover_values': [str(x + j) for j in positions],
        'verification': verification,
    }


def lcm_of_sources(sources: list[int]) -> int:
    max_exponents: dict[int, int] = {}
    for a in sources:
        for p, e in factor(a):
            max_exponents[p] = max(max_exponents.get(p, 0), e)
    return prod(p ** e for p, e in max_exponents.items())


def verify_recorded_result(document: dict[str, Any]) -> dict[str, Any]:
    """Recheck an exported result using the standard library only.

    This deliberately does not rerun, trust, or import the matching solver.
    It verifies the complete sufficient certificate and each actual cover,
    including the cofactor matching and the recorded prime-unit repair trace.
    """
    if 'certificate' in document:
        items = [('input', document)]
    else:
        items = [(name, item) for name, item in document.items()
                 if isinstance(item, dict) and 'certificate' in item]
    if not items:
        raise ValueError('No finite certificate was found in the JSON document.')
    reports = {}
    for name, item in items:
        recorded = item['certificate']
        A, M = recorded['sources'], recorded['M']
        regenerated = check_certificate(A, M)
        if regenerated != recorded:
            raise AssertionError('Recorded finite certificate differs from exact recomputation.')
        report = {'finite_certificate_recomputed_exactly': True,
                  'input_is_certified': regenerated['integer_criterion_passes']}
        if 'cover' in item:
            cover = item['cover']; x = int(cover['x'])
            positions = cover['cover_positions']
            checked = verify_cover(A, M, x, positions)
            assert checked == cover['verification']
            assert cover['cover_values'] == [str(x + j) for j in positions]
            assert cover['cover_size'] == len(positions)
            assert cover['n'] == len(A) and cover['M'] == M
            assert cover['budget_2n'] == 2 * len(A)
            assert cover['interval_first'] == str(x + 1)
            assert cover['interval_last'] == str(x + M)
            data = source_data(A, M)
            match = cover['matching']
            assert sorted(row['source'] for row in match) == A
            assigned = []
            for row in match:
                a, j = row['source'], row['position']
                assert 1 <= j <= M
                assert row['cofactor'] == data['quotient'][a]
                assert row['removed_prime'] == max(data['facts'][a])
                assert row['target_value'] == str(x + j)
                assert (x + j) % row['cofactor'] == 0
                assigned.append(j)
            assert len(set(assigned)) == len(A)
            assert sorted(assigned) == cover['initial_positions']
            assert cover['initial_matching_size'] == len(A)
            used = set(assigned); demand = data['demand']
            current = {p: sum(valuation(x + j, p) for j in used) for p in demand}
            deficit = lambda: sum(max(demand[p] - current[p], 0) for p in demand)
            assert deficit() == cover['initial_total_prime_deficit'] <= len(A)
            for step in cover['repairs']:
                p, j = step['requested_prime'], step['position']
                assert p in demand and current[p] < demand[p]
                assert 1 <= j <= M and j not in used
                assert (x + j) % p == 0
                assert step['target_value'] == str(x + j)
                before = deficit()
                assert step['total_deficit_before'] == before
                used.add(j)
                for q in demand:
                    current[q] += valuation(x + j, q)
                assert step['total_deficit_after'] == deficit() < before
            assert deficit() == 0 and sorted(used) == positions
            assert len(cover['repairs']) == cover['repair_count'] <= len(A)
            report['matching_and_repair_trace_verified_without_scipy'] = True
            report['exact_product_divisibility_verified'] = True
        reports[name] = report
    return reports


def demo() -> dict[str, Any]:
    # A genuine omega=3 family: triples of distinct primes, not repetitions.
    P = primes_between(101, 199)
    large_A = sorted(prod(t) for t in combinations(P, 3))
    assert len(P) == 21 and len(large_A) == 1330 and max(large_A) == 7566179
    assert all(sum(e for _, e in factor(a)) == 3 for a in large_A)
    large_cert = check_certificate(large_A)
    assert large_cert['integer_criterion_passes']
    assert large_cert['analytic_criterion_passes']

    # Includes all 35 cubic monomials, repeated powers, squares and prime sources.
    small_P = [11, 13, 17, 19, 23]
    small_A = sorted(set(prod(t) for t in combinations_with_replacement(small_P, 3))
                     | {p * p for p in small_P} | set(small_P))
    assert len(small_A) == 45 and max(small_A) == 12167
    small_cert = check_certificate(small_A)
    assert small_cert['integer_criterion_passes'] and small_cert['analytic_criterion_passes']
    center = lcm_of_sources(small_A)
    M = max(small_A)
    x = center - (M - 1) // 2 - 1
    assert x >= 0 and all(center % a == 0 for a in small_A)
    small_cover = construct_cover(small_A, M, x)

    # Q empty: quotient-one matching and subsequent prime-unit repair.
    prime_A = [11, 13, 17, 19, 23]
    prime_cert = check_certificate(prime_A)
    assert not prime_cert['Q_cofactor_support']
    prime_cover = construct_cover(prime_A, x=prod(prime_A) - 12)

    # Deliberately uncertified finite input: no assertion of nonexistence.
    failed_A = [60, 66, 70, 78, 84, 90]
    failed_cert = check_certificate(failed_A)
    assert not failed_cert['integer_criterion_passes']
    return {
        'status': 'Exact finite certificates and illustrative covers; no general-problem claim.',
        'large_distinct_triples': {
            'description': 'All products of three distinct primes in [101,199]; certificate only.',
            'full_interval_matching_built': False, 'certificate': large_cert},
        'small_cubic_and_prime_power_family': {
            'description': 'All cubic monomials plus squares and primes on {11,13,17,19,23}.',
            'center_lcm': str(center), 'certificate': small_cert, 'cover': small_cover},
        'prime_only_edge_case': {'certificate': prime_cert, 'cover': prime_cover},
        'uncertified_input_check': {
            'description': 'Failure of the sufficient criterion is not a counterexample.',
            'certificate': failed_cert},
    }


def summary(result: dict[str, Any]) -> dict[str, Any]:
    if 'large_distinct_triples' not in result:
        cert = result['certificate']
        ans = {k: cert[k] for k in ['n', 'M', 'integer_criterion_passes',
                                    'analytic_criterion_passes', 'min_integer_margin',
                                    'max_analytic_value']}
        if 'cover' in result:
            ans['cover_size'] = result['cover']['cover_size']
            ans['cover_verified'] = result['cover']['verification']
        return ans
    ans = {}
    for name in ['large_distinct_triples', 'small_cubic_and_prime_power_family',
                 'prime_only_edge_case', 'uncertified_input_check']:
        item = result[name]; cert = item['certificate']
        value = {k: cert[k] for k in ['n', 'M', 'integer_criterion_passes',
                                     'analytic_criterion_passes', 'min_integer_margin',
                                     'max_analytic_value']}
        if 'cover' in item:
            value.update({k: item['cover'][k] for k in
                          ['cover_size', 'budget_2n', 'repair_count',
                           'initial_total_prime_deficit', 'scipy_graph_edges']})
            value['exact_product_divisibility_verified'] = item['cover']['verification'][
                'product_divisibility_verified_by_exact_valuations']
        ans[name] = value
    return ans


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--demo', action='store_true')
    parser.add_argument('--verify', type=Path,
                        help='Verify an exported result without importing SciPy.')
    parser.add_argument('--sources', type=Path)
    parser.add_argument('--M', type=int)
    parser.add_argument('--x', type=int)
    parser.add_argument('--construct', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.verify:
        if args.demo or args.sources or args.construct:
            parser.error('--verify is a standalone read-only operation.')
        report = verify_recorded_result(json.loads(args.verify.read_text()))
        print(json.dumps({'verified_file': str(args.verify.resolve()),
                          'verification': report}, indent=2))
        return
    if args.demo and args.sources:
        parser.error('Choose --demo or --sources, not both.')
    if args.sources:
        raw = json.loads(args.sources.read_text())
        A = raw if isinstance(raw, list) else raw['sources']
        M = args.M if args.M is not None else (raw.get('M') if isinstance(raw, dict) else None)
        x = args.x if args.x is not None else (int(raw.get('x', 0)) if isinstance(raw, dict) else 0)
        result = {'certificate': check_certificate(A, M)}
        if args.construct:
            result['cover'] = construct_cover(A, M, x)
    else:
        result = demo()
    output = args.output or Path(__file__).with_name('exact2n_demo_results.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'output': str(output.resolve()), 'summary': summary(result)}, indent=2))


if __name__ == '__main__':
    main()
