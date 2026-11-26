"""Check the sharpness construction, the CRT obstruction, and both signs of the effective offset."""
from math import gcd, lcm, prod
from itertools import combinations_with_replacement

def is_prime(number):
    return number >= 2 and all(number % k for k in range(2, int(number**0.5) + 1))

def valuation(number, prime):
    power = 0
    while number % prime == 0:
        power += 1
        number //= prime
    return power

primes = [101, 103, 107, 109]
sources = [p * q for p, q in combinations_with_replacement(primes, 2)]
maximum = max(sources)
center = prod(primes) ** 2
start = center - maximum // 2
assert lcm(*sources) == center
for b in range(start + 1, start + maximum + 1):
    total = sum(valuation(b, p) for p in primes)
    assert total == 2 * len(primes) if b == center else total <= 1
for padding in range(len(primes) + 1):
    assert lcm(*sources, *primes[:padding]) == center
print("Centered lower construction and padding checked.")

m = 31
large = [p for p in range(m + 1, 1000) if is_prime(p)][:2*m]
shift, period = 0, 1
for i in range(m):
    modulus = large[2*i] * large[2*i + 1]
    shift += period * (((-i - 1 - shift) * pow(period, -1, modulus)) % modulus)
    period *= modulus
for i in range(m):
    for d in range(1, m+1):
        if (shift + i + 1) % d == 0:
            quotient = (shift + i + 1) // d
            assert all(quotient % p == 0 for p in large[2*i:2*i+2])
print("Every uncentered prime-power target column vanishes in the CRT example.")

for k in (2, 3, 5, 8):
    a_set = [a for a in range(2, 45) if gcd(a, k) == 1]
    m, center = max(a_set), lcm(*a_set)
    x = center // k - m // 2
    for d in a_set:
        for b in range(x+1, x+m+1):
            t = k*b - center
            if t and abs(t) % d == 0:
                assert b % d == 0
                q = abs(t) // d
                sign = -1 if t > 0 else 1
                assert q % k == sign * center * pow(d, -1, k) % k
print("Rational-center congruences checked on both sides of zero.")
