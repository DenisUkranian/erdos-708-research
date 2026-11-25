#!/usr/bin/env python3
"""Exact certificate for a bank-union discrepancy, not a g(n) computation."""
from fractions import Fraction
from math import isqrt

z = 1000
M = 4*z*z
N = M//2
sieve = bytearray(b'\x01')*(z+1)
sieve[:2] = b'\x00\x00'
for p in range(2,isqrt(z)+1):
    if sieve[p]:
        sieve[p*p:z+1:p] = b'\x00'*(((z-p*p)//p)+1)
primes = [p for p in range(2,z+1) if sieve[p]]
rough = bytearray(b'\x01')*(N+1)
rough[0] = 0
mean = Fraction(N)
for p in primes:
    rough[p:N+1:p] = b'\x00'*(N//p)
    mean *= Fraction(p-1,p)
prefix = sum(rough)
ceiling = -(-mean.numerator//mean.denominator)
assert len(primes) == 168
assert prefix == 152528
assert ceiling == 161931
assert ceiling-prefix == 9403
print('PASS: exact prefix rough count =',prefix)
print('ceil(exact rational CRT mean) =',ceiling)
print('An actual shifted hot-bank union has deficit at least',ceiling-prefix)
print('sqrt(M) =',isqrt(M))
print('This checks an intermediate transfer obstruction, not g(n) or (D).')
