"""Exact small-period checks of the harmonic kernel and all adaptive cuts."""
from fractions import Fraction
from math import gcd, lcm

from collections import defaultdict, deque


def maximum_flow(edges):
    residual = defaultdict(dict)
    for (a, b), capacity in edges.items():
        residual[a][b] = capacity
        residual[b][a] = 0
    value = 0
    while True:
        parent = {'source': None}
        queue = deque(['source'])
        while queue and 'target' not in parent:
            a = queue.popleft()
            for b, capacity in residual[a].items():
                if capacity and b not in parent:
                    parent[b] = a
                    queue.append(b)
        if 'target' not in parent:
            return value, {edge: cap - residual[edge[0]][edge[1]]
                           for edge, cap in edges.items()}
        path = []
        b = 'target'
        while parent[b] is not None:
            path.append((parent[b], b))
            b = parent[b]
        amount = min(residual[a][b] for a, b in path)
        for a, b in path:
            residual[a][b] -= amount
            residual[b][a] += amount
        value += amount


def check(size):
    period = lcm(*range(1, size + 1))
    harmonic = sum(Fraction(1, d) for d in range(1, size + 1))
    weights = [Fraction(1, d) / harmonic for d in range(1, size + 1)]
    scale = lcm(period, *(w.denominator for w in weights))
    profiles = [gcd(b, period) for b in range(period)]
    counts = {z: profiles.count(z) for z in set(profiles)}
    edges = {}
    for d, w in enumerate(weights, 1):
        edges['source', ('d', d)] = int(scale * w)
        for z in counts:
            if z % d == 0:
                edges[('d', d), ('z', z)] = scale
    for z, count in counts.items():
        edges[('z', z), 'target'] = scale * count // period
    value, flow = maximum_flow(edges)
    assert value == scale
    capacities = {
        z: [Fraction(flow.get((('d', d), ('z', z)), 0) * period, scale * count)
            for d in range(1, size + 1)]
        for z, count in counts.items()
    }
    assert all(sum(row) == 1 for row in capacities.values())
    # Integer cut weights give exact comparisons for every subset of the interval.
    units = [int(scale * w) for w in weights]
    worst = Fraction(0)
    for x in range(period):
        points = range(x + 1, x + 1 + size)
        banks = [sum(1 << i for i, b in enumerate(points) if b % d == 0)
                 for d in range(1, size + 1)]
        empirical = [sum(capacities[gcd(b, period)][d] for b in points) / size
                     for d in range(size)]
        deficit = sum(max(0, w - obs) for w, obs in zip(weights, empirical))
        cut = max(
            sum(w for w, bank in zip(units, banks) if bank & ~t == 0) * size
            - t.bit_count() * scale for t in range(1 << size)
        )
        excess = Fraction(cut, size * scale)
        assert excess <= deficit
        worst = max(worst, excess)
    return period, worst


if __name__ == '__main__':
    for size in range(2, 9):
        period, worst = check(size)
        print(f'M={size}, shifts={period}, maximum exact cut excess={worst}')
