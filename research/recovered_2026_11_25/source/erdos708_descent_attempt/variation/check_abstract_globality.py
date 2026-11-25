#!/usr/bin/env python3
"""Exact audit of a NONARITHMETIC method obstruction; not a g(n) computation."""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json

root = Path(__file__).resolve().parent
data = json.loads((root / 'abstract_global_certificates.json').read_text())
edges = list(combinations(range(6), 2))
expected_columns = [[2]*6]
expected_columns += [[2*int(i == j) for i in range(6)] for j in range(6)]
expected_columns += [[int(i in e) for i in range(6)] for e in edges]
assert data['columns'] == expected_columns
assert data['caps'] == [6] + [4]*6 + [3]*15
assert F(data['c']) == F(21, 10)
assert F(data['upper']) == F(6, 5)
degree_types = set()
for mask in range(1 << len(edges)):
    degree = [0] * 6
    for j, (u, v) in enumerate(edges):
        if mask >> j & 1:
            degree[u] += 1
            degree[v] += 1
    degree_types.add(tuple(sorted(degree)))

expected = {(deg, h) for deg in degree_types for h in (0, 1)}
seen = set()
for cert in data['certificates']:
    deg, h = tuple(cert['degree_sequence']), cert['h']
    assert (deg, h) in expected and (deg, h) not in seen
    seen.add((deg, h))
    k = sum(deg) // 2
    demand = [3*h + 2*(k-deg[i]) for i in range(6)]
    assert demand == cert['demand']
    n = k + 3*h
    assert n == cert['source_count']
    z = list(map(F, cert['z']))
    assert all(0 <= z[j] <= data['caps'][j] for j in range(22))
    for i in range(6):
        assert sum(z[j]*data['columns'][j][i] for j in range(22)) >= demand[i]
    assert sum(z) == F(cert['cost'])
    surplus = sum(z) - F(21, 10)*n
    assert surplus == F(cert['surplus_upper']) <= F(6, 5)
    if surplus == F(6, 5):
        assert h == 1 and deg == (5,)*6
    elif n:
        assert surplus <= F(-7, 10)
assert seen == expected

source = [((1,)*6, 3)]
source += [(tuple(2*int(i in S) for i in range(6)), 1)
           for S in combinations(range(6), 4)]
source += [(tuple(int(i == j) for i in range(6)), 12) for j in range(6)]
target = [((2,)*6, 6)]
target += [(tuple(2*int(i == j) for i in range(6)), 4) for j in range(6)]
target += [(tuple(int(i in e) for i in range(6)), 3) for e in edges]
target += [((0,)*6, 15)]
for threshold in product(range(3), repeat=6):
    s_count = sum(m for v,m in source if all(v[i]>=threshold[i] for i in range(6)))
    t_count = sum(m for v,m in target if all(v[i]>=threshold[i] for i in range(6)))
    assert t_count >= s_count

def surplus(weights, sources, targets):
    c = F(21, 10)
    def load(v): return sum(x*y for x,y in zip(weights,v))
    return sum(m*max(load(v)-c,0) for v,m in sources) - sum(m*max(load(v)-1,0) for v,m in targets)

assert surplus([F(1,2)]*6, source, target) == F(6,5)
z_star = [F(6)] + [F(4)]*6 + [F(3,5)]*15
assert sum(z_star) == 39
assert all(sum(z_star[j]*expected_columns[j][i] for j in range(22)) == 23
           for i in range(6))
assert all(0 < z_star[j] < 3 for j in range(7,22))
for p in range(6):
    def quotient(rows):
        ans=[]
        for v,m in rows:
            if v[p]:
                u=list(v); u[p]-=1; ans.append((tuple(u),m))
        return ans
    sq,tq=quotient(source),quotient(target)
    assert sum(m for _,m in sq)==sum(m for _,m in tq)==25
    assert surplus([F(1)]*6,sq,tq)==F(-23,10)
print('PASS: 204 rational primal certificates; all 729 divisor orthants;')
print('unique global surplus 6/5 at all weights 1/2; all six formal cold quotients -23/10.')
print('This is a nonarithmetic obstruction. It is NOT a counterexample to (D) or Erdős 708.')
