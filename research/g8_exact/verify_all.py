#!/usr/bin/env python3
"""Reproduce the computer-assisted proof that g(8)=11 (at-most convention).

Requires Python >= 3.9 and a C++17 compiler. This script verifies the new
finite component and the lower witness. It takes the previously established
g(7)=9 as an explicit mathematical dependency; the full g7 package is bundled
in dependencies/ and can be replayed separately.
"""
from __future__ import annotations
import collections
import os
import pathlib
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent
PRIMES = (2, 3, 5, 7)
LOWER_PRIMES = (37, 41, 43, 47, 53)
LOWER_DEMAND = (6, 2, 2, 2, 4)
LOWER_A = (1369, 1517, 1591, 1739, 1961, 2173, 2279, 2491)
X = 246043396342067361
M0 = 2491
OFFSETS = (25, 27, 62, 80, 99, 133, 136, 1199, 1203, 1205, 1246)


def run(command, *, output=False):
    p = subprocess.run(command, check=True, text=True, capture_output=True)
    if output:
        print(p.stdout.strip(), p.stderr.strip(), flush=True)
    return p


def read_demands(path):
    result = set()
    for line in path.read_text().splitlines():
        row = tuple(map(int, line.split()))
        assert len(row) == 5, row
        assert row not in result, ('duplicate demand', row)
        result.add(row)
    return result


def valuations(value, primes):
    exps = []
    for p in primes:
        count = 0
        while value % p == 0:
            value //= p
            count += 1
        exps.append(count)
    return tuple(exps)


def validate_slot_certificates(certfile):
    covered = set()
    for line in certfile.read_text().splitlines():
        row = list(map(int, line.split()))
        assert len(row) >= 6
        M, *rest = row
        demand = tuple(rest[:4]); count = rest[4]; hs = rest[5:]
        assert len(hs) == count <= 11
        assert count >= 1
        demand_key = (M, *demand)
        assert demand_key not in covered, ('duplicate certificate', demand_key)
        got = [0, 0, 0, 0]
        for j, h in enumerate(hs, start=1):
            assert 1 <= h <= M, (M, h)
            exp = valuations(h, PRIMES)
            # All h must be 7-smooth, not just carry the listed valuations.
            assert __import__('math').prod(p**v for p, v in zip(PRIMES, exp)) == h
            gcd = __import__('math').prod(p**min(u,v) for p,u,v in zip(PRIMES,got,exp))
            assert gcd <= M//j, (demand_key, j, gcd, M//j)
            got = [u+v for u,v in zip(got,exp)]
        assert all(u >= need for u,need in zip(got,demand)), (demand_key,got)
        covered.add(demand_key)
    return covered


def validate_lower_witness():
    from math import prod
    assert max(LOWER_A) == M0 and len(LOWER_A)==len(set(LOWER_A))==8
    d=tuple(sum(valuations(a,LOWER_PRIMES)[i] for a in LOWER_A) for i in range(5))
    assert d == LOWER_DEMAND
    assert len(OFFSETS)==len(set(OFFSETS))==11
    assert all(1<=t<=M0 for t in OFFSETS)
    got=[0]*5
    center=1246
    for t in range(1,M0+1):
        e=valuations(X+t,LOWER_PRIMES)
        if t!=center:
            assert sum(q>0 for q in e) <=1, ('mixed noncentral point',t,e)
            assert e[0]<=1 and e[4]<=1, ('unpermitted pure square',t,e)
        else:
            assert e==(2,1,1,1,1)
        if t in OFFSETS:
            got=[u+v for u,v in zip(got,e)]
    assert all(u>=need for u,need in zip(got,LOWER_DEMAND))
    print('PASS lower construction: 11 required (elementary counting), 11 suffice, exponents=',got,flush=True)


def main():
    finite_dir = ROOT/'certificates'
    original = read_demands(finite_dir/'finite_demands.txt')
    assert len(original)==57515
    covered = validate_slot_certificates(finite_dir/'slot_certificates.txt')
    exceptional = read_demands(finite_dir/'crt_exceptions.txt')
    assert len(covered)==57487 and len(exceptional)==28
    assert not (covered & exceptional)
    assert original == covered | exceptional
    print('PASS 57,487 cumulative-gcd certificates, exact partition of 57,515 demands',flush=True)
    validate_lower_witness()
    with tempfile.TemporaryDirectory(prefix='erdos708_g8_') as workstr:
        work=pathlib.Path(workstr)
        binaries={}
        for name in ('enumerate','make_gcd_certificates','crt11','lower8'):
            binary=work/name
            run(['g++','-std=c++17','-O2','-UNDEBUG',str(ROOT/'src'/(name+'.cpp')),'-o',str(binary)])
            binaries[name]=binary
        regen=work/'demands.txt'
        got=run([str(binaries['enumerate']),str(regen)])
        assert 'M_with_uncleared=50 last=252 total_sets=1691461 total_demand_vectors=57515' in got.stderr
        independently_generated=read_demands(regen)
        assert independently_generated==original
        print('PASS exhaustive finite enumeration: 50 maxima <= 252, 1,691,461 source sets, 57,515 demands',flush=True)
        recomputed_slots=work/'slots.txt'
        recomputed_residual=work/'residual.txt'
        got=run([str(binaries['make_gcd_certificates']),str(regen),str(recomputed_slots),str(recomputed_residual)])
        assert 'CERTIFICATES=57487 CRT_RESIDUAL=28' in got.stdout
        recreated_covered=validate_slot_certificates(recomputed_slots)
        recreated_exceptions=read_demands(recomputed_residual)
        assert recreated_covered==covered and recreated_exceptions==exceptional
        print('PASS independently regenerated exhaustive slot witnesses and CRT exceptional cases',flush=True)
        crt=run([str(binaries['crt11']),str(recomputed_residual)])
        assert 'ALL_PASS rows=28 ' in crt.stdout.splitlines()[-1]
        print('PASS exhaustive CRT over 28 residual demands: '+crt.stdout.splitlines()[-1],flush=True)
        lower=run([str(binaries['lower8'])])
        assert 'optimal=11' in lower.stdout
        print('PASS independent 0-1 dynamic program for lower witness: optimal=11',flush=True)
        # Confirm the elementary analytic cutoff using only integer arithmetic.
        assert 7*8*9*10*11*7**4==133111440
        assert 11537**2<133111440<11538**2
        print('PASS analytic gate: all M >= 11538',flush=True)
    print('ALL CHECKS PASS: upper g(8)<=11 conditional on g(7)<=9,g(6)<=8,g(5)<=6; lower g(8)>=11 unconditional',flush=True)

if __name__=='__main__':main()
