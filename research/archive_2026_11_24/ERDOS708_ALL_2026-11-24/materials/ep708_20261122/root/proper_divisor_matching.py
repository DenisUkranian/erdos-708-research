#!/usr/bin/env python3
"""Search a sufficient proper-divisor matching lemma for Erdos problem 708.

This tests an auxiliary statement, not the original conjecture.
For every m<=M with Omega(m)>=k, allow the targets b in (x,x+M]
divisible by m/p for at least one prime p dividing m.
A full matching for k=3 would imply the global weighted hinge H_2.
All edges and any exported Hall obstruction are checked with integer arithmetic.
"""
import argparse
import json
import math
import random
import time
from pathlib import Path

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching


def source_rows(M, k=3, largest_only=False):
    spf = list(range(M + 1))
    for p in range(2, math.isqrt(M) + 1):
        if spf[p] == p:
            for q in range(p*p, M + 1, p):
                if spf[q] == q:
                    spf[q] = p
    rows = []
    for m in range(2, M + 1):
        z, primes, omega = m, [], 0
        while z > 1:
            p = spf[z]
            primes.append(p)
            while z % p == 0:
                z //= p
                omega += 1
        if omega >= k:
            ds = [m // max(primes)] if largest_only else sorted({m // p for p in primes})
            rows.append((m, ds))
    return rows


def check(M, x, rows):
    indices, indptr, adjacency = [], [0], []
    residue = {d: (-x) % d for _, ds in rows for d in ds}
    for m, ds in rows:
        ns = set()
        for d in ds:
            first = residue[d] or d
            ns.update(j-1 for j in range(first, M + 1, d))
        neighbors = sorted(ns)
        indices.extend(neighbors)
        indptr.append(len(indices))
        adjacency.append(neighbors)
    graph = csr_matrix((np.ones(len(indices), dtype=np.int8), indices, indptr), shape=(len(rows), M))
    assignment = maximum_bipartite_matching(graph, perm_type='column')
    unmatched = [i for i, j in enumerate(assignment) if j < 0]
    if not unmatched:
        # Audit the returned witness independently of the sparse-matrix solver.
        assert len(set(int(j) for j in assignment)) == len(rows)
        assert all(any((x+int(j)+1) % d == 0 for d in rows[i][1]) for i,j in enumerate(assignment))
        return None
    inverse = {int(j): i for i, j in enumerate(assignment) if j >= 0}
    S, T, queue = set(unmatched), set(), list(unmatched)
    for i in queue:
        for j in adjacency[i]:
            if j not in T:
                T.add(j)
                if j in inverse and inverse[j] not in S:
                    S.add(inverse[j]); queue.append(inverse[j])
    assert len(S) > len(T)
    source = [rows[i][0] for i in sorted(S)]
    target = [x+j+1 for j in sorted(T)]
    independently_computed = set()
    for i in S:
        for d in rows[i][1]:
            first = (x // d + 1) * d
            independently_computed.update(range(first, x+M+1, d))
    assert independently_computed == set(target)
    return {'M': M, 'x': str(x), 'source': source, 'neighbors': [str(b) for b in target],
            'source_size': len(S), 'neighbor_size': len(T), 'matching_size':len(rows)-len(unmatched)}


def run(args):
    rng = random.Random(args.seed)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    tested = 0
    for M in range(args.start, args.stop+1, args.step):
        rows = source_rows(M, args.k, args.largest_only)
        if not rows: continue
        fixed = list(range(min(M, args.trials//4))) + [M*M, math.factorial(M)-M//2]
        for ti in range(args.trials):
            x = fixed[ti] if ti < len(fixed) else rng.getrandbits(max(64, 2*M))
            witness = check(M, x, rows)
            tested += 1
            if witness:
                result = {'status':'auxiliary_conjecture_refuted', 'k':args.k,
                          'largest_only':args.largest_only, 'tested':tested,
                          'seed':args.seed, 'witness':witness}
                out.write_text(json.dumps(result,indent=2)+'\n')
                print(json.dumps({key: value for key, value in result.items()
                                  if key != 'witness'} | {
                    'M': M, 'source_size': witness['source_size'],
                    'neighbor_size': witness['neighbor_size'],
                    'certificate_file': str(out)}), flush=True)
                return
        if M % max(10,args.step*10) == 0:
            print(json.dumps({'M':M,'tested':tested,'seconds':round(time.monotonic()-started,2)}),flush=True)
    result={'status':'no_counterexample_in_sample','k':args.k,'largest_only':args.largest_only,
            'tested':tested,'seed':args.seed,'start':args.start,'stop':args.stop,
            'step':args.step,'trials_per_M':args.trials,
            'seconds':round(time.monotonic()-started,2)}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)


if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--start',type=int,default=8)
    p.add_argument('--stop',type=int,default=200)
    p.add_argument('--step',type=int,default=1)
    p.add_argument('--trials',type=int,default=100)
    p.add_argument('--seed',type=int,default=70820261122)
    p.add_argument('--k',type=int,default=3)
    p.add_argument('--largest-only',action='store_true')
    p.add_argument('--output',default='matching_results.json')
    run(p.parse_args())
