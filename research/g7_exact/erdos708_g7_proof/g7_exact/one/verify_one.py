#!/usr/bin/env python3
"""Replay the finite one-large-prime branch of the proof g(7)<=9.

Python 3 and a C++17 compiler are required. Mathematical reductions and the
single hand-proved demand are stated in ONE_LARGE_PROOF.md. This script does
not run or trust the heuristic slot-search program: it checks its witnesses.
"""
from pathlib import Path
from math import gcd, prod
import json
import re
import subprocess
import tempfile
import time

ROOT = Path(__file__).resolve().parent
HAND_DEMAND = (55, 11, 4, 9, 2, 0, 4)


def exponents(a, primes):
    out = []
    for p in primes:
        e = 0
        while a % p == 0:
            a //= p
            e += 1
        out.append(e)
    assert a == 1
    return out


def pack(e, primes, capacities):
    """Return success only after constructing a complete valid packing."""
    for mode in range(3):
        bins = [1] * len(capacities)
        success = True
        for i in range(len(primes) - 1, -1, -1):
            for _ in range(e[i]):
                eligible = [j for j, b in enumerate(bins)
                            if b * primes[i] <= capacities[j]]
                if not eligible:
                    success = False
                    break
                chosen = eligible[0]
                for j in eligible[1:]:
                    left = capacities[j] * bins[chosen]
                    right = capacities[chosen] * bins[j]
                    if (mode == 1 and left < right) or (mode == 2 and left > right):
                        chosen = j
                bins[chosen] *= primes[i]
            if not success:
                break
        if success:
            assert all(b <= c for b, c in zip(bins, capacities))
            assert prod(bins) == prod(p ** d for p, d in zip(primes, e))
            return True
    return False


def valuation_supply(M, p, k):
    total, power = 0, p
    while power <= M:
        total += min(k, M // power)
        power *= p
    return total


def prime_union(M, primes, demand):
    used = 0
    for p, d in zip(primes, demand):
        for k in range(10 - used):
            if valuation_supply(M, p, k) >= d:
                used += k
                break
        else:
            return False
    return True


def core_cover(M, primes, sources):
    groups = [(a, exponents(a, primes)) for a in sources]
    nontrivial = [(a, e) for a, e in groups if e[4]]
    zeros = [(a, e) for a, e in groups if not e[4]]
    d, z = len(nontrivial), len(zeros)
    assert 3 <= d <= 6 and z == 7 - d
    r = {1: 1, 2: 2, 3: 4, 4: 5}[z]
    total = [sum(e[i] for a, e in nontrivial) for i in range(5)]
    largest = max(nontrivial, key=lambda ae: ae[0] // primes[4] ** ae[1][4])[1]
    residual = [total[i] - largest[i] for i in range(4)] + [0]
    k = 9 - r - d
    if pack(residual, primes, [M // j for j in range(r + 2, r + k + 2)]):
        return True
    kp = next((k for k in range(10)
               if valuation_supply(M, primes[4], k) >= total[4]), 10)
    k = 9 - r - kp
    if k >= 0 and pack(total[:4] + [0], primes,
                       [M // j for j in range(r + 1, r + k + 1)]):
        return True
    gm = {3: 4, 4: 5, 5: 6, 6: 8}[d]
    small_zeros = [sum(e[i] for a, e in zeros) for i in range(5)]
    return pack(small_zeros, primes, [M // j for j in range(gm + 1, 10)])


def validate_slots():
    keys = set()
    files = {}
    for name in ['slots9.txt', 'slots9_extra.txt']:
        rows = 0
        for line in (ROOT / name).read_text().splitlines():
            data = list(map(int, line.split()))
            M, budget, dim = data[:3]
            assert budget == 9 and dim == 5
            primes = data[3:8]
            demand = data[8:13]
            length = data[13]
            slots = data[14:]
            assert primes[:4] == [2, 3, 5, 7] and primes[4] >= 11
            assert len(slots) == length <= budget
            product = 1
            for j, h in enumerate(slots, 1):
                assert 1 <= h <= M
                assert gcd(product, h) <= M // j
                product *= h
            assert product % prod(p ** d for p, d in zip(primes, demand)) == 0
            key = (M, primes[4], *demand)
            assert key not in keys
            keys.add(key)
            rows += 1
        files[name] = rows
    assert len(keys) == 252175
    return keys, files


def main():
    start = time.monotonic()
    certified, certificate_files = validate_slots()
    with tempfile.TemporaryDirectory(prefix='one_large_verify_') as temp_name:
        temp = Path(temp_name)
        executable = temp / 'close_one'
        subprocess.run(['g++', '-O3', '-std=c++17', str(ROOT / 'close_one.cpp'),
                        str(ROOT / 'skyline.cpp'), '-o', str(executable)], check=True)
        run = subprocess.run([str(executable), str(temp)], check=True,
                             capture_output=True, text=True)
        stats = {k: int(v) for k, v in re.findall(r'(\w+)=(\d+)(?![\d.])', run.stderr)
                 if k != 'seconds'}
        assert stats['configs'] == 59982
        assert stats['residual'] == 623
        assert stats['leaves'] == 7006656
        assert stats['unique'] == 658925
        assert stats['unknown'] == 252176
        checked_unknown, hand_cases = 0, 0
        used_certificates = set()
        for line in (temp / 'unknown9.txt').read_text().splitlines():
            data = list(map(int, line.split()))
            assert len(data) == 14
            key = tuple(data[:7])
            if key == HAND_DEMAND:
                hand_cases += 1
            else:
                assert key in certified, ('Uncertified maximal demand', key)
                used_certificates.add(key)
            checked_unknown += 1
        assert checked_unknown == 252176 and hand_cases == 1
        assert used_certificates == certified
        # Recheck all maximal demands proved without slot lists, independently
        # in Python, including the representative source-set witness.
        checked_passed = 0
        for line in (temp / 'frontier_pass9.txt').read_text().splitlines():
            data = list(map(int, line.split()))
            assert len(data) == 14
            M, P = data[:2]
            demand, sources = data[2:7], data[7:]
            primes = [2, 3, 5, 7, P]
            assert len(sources) == len(set(sources)) == 7
            assert min(sources) >= 2 and max(sources) == M
            actual = [sum(exponents(a, primes)[i] for a in sources) for i in range(5)]
            assert actual == demand
            assert (core_cover(M, primes, sources)
                    or prime_union(M, primes, demand)
                    or pack(demand, primes, [M // j for j in range(1, 10)])), data
            checked_passed += 1
        assert checked_passed == 120285
    result = {
        'status': 'PASS',
        'theorem': 'No least-M, maximal-sum counterexample to g(7)<=9 with exactly one active prime >=11 exists, subject to the stated global reductions.',
        'prior_bounds': ['g(2)<=2', 'g(3)<=4', 'g(4)<=5', 'g(5)<=6', 'g(6)<=8'],
        'global_finite_cutoff': 24696,
        'enumeration': stats,
        'certificate_files': certificate_files,
        'slot_certificates_independently_checked': len(certified),
        'passed_maximal_demands_rechecked_in_python': checked_passed,
        'hand_proved_exception': {
            'M': 55, 'primes': [2, 3, 5, 11], 'demand': [4, 9, 2, 4],
            'reference': 'ONE_LARGE_PROOF.md, final hand lemma'
        },
        'seconds': round(time.monotonic() - start, 3)
    }
    (ROOT / 'verification_result.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
