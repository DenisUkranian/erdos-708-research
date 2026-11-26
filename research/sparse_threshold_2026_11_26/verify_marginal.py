"""Check both product-cover optima using integer upper and lower certificates."""
from itertools import combinations
from math import prod


def valuation(number, prime):
    exponent = 0
    while number % prime == 0:
        number //= prime
        exponent += 1
    return exponent


def check_optimum(source, cover, window, prices):
    assert len(cover) == len(set(cover)) and set(cover) <= set(window)
    assert prod(cover) % prod(source) == 0
    def load(number):
        return sum(valuation(number, prime) for prime in prices)
    price_bound = sum(map(load, source)) - sum(max(0, load(b) - 1) for b in window)
    assert price_bound == len(cover)
    return price_bound


def small_example():
    window = range(101, 125)
    residual = {2, 4, 5, 6, 8, 12, 14, 15, 16, 24}
    heavy = {104, 108, 110, 112, 116, 120, 124}
    full = heavy | {102, 106, 114, 105, 115}
    before = check_optimum(residual, heavy, window, (2, 5))
    after = check_optimum(residual | {10, 20}, full, window, (2, 5))
    assert (before, after) == (7, 12)
    return before, after


def subset_example():
    maximum = 128
    prefix = range(1, maximum + 1)
    prices = (2, 5, 7)
    shift = 1802870856408795970779697568000000
    window = range(shift + 1, shift + maximum + 1)
    heavy = {i for i in prefix if sum(valuation(i, p) for p in prices) >= 2}
    cell = (35, 70, 105)
    residual = heavy - set(cell)
    banks = {}
    for prime in prices:
        required = sum(valuation(i, prime) for i in cell)
        bank = [i for i in prefix if i not in heavy and i % prime == 0]
        banks[prime] = bank[:required]
        assert len(banks[prime]) == required
        residual.update(banks[prime])
    results = []
    for size in range(1 + len(cell)):
        for subset in combinations(cell, size):
            positions = set(heavy)
            for prime in prices:
                count = sum(valuation(i, prime) for i in subset)
                positions.update(banks[prime][:count])
            results.append(check_optimum(residual | set(subset),
                                         [shift + i for i in positions], window, prices))
    assert results == [48, 50, 51, 50, 53, 52, 53, 55]
    return results


if __name__ == "__main__":
    print("M=24, before and after:", small_example())
    print("M=128, all eight exact optima:", subset_example())
