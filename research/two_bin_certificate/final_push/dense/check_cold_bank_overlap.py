"""Exact check of overlap after cold-gcd merging; no g(n) computation."""
from fractions import Fraction as F
from itertools import combinations
from math import gcd,prod

primes=[2,3,5,7,11,13,17,19,23,29,31,37]
C=F(12); delta=F(1,10); eps=F(1,20); c=2+delta
w=F(199,2200); x0=F(199,220)
B=prod(primes)
anchors=[prod(s) for s in combinations(primes,10)]
def X(a):
    val=F(0)
    for p in primes:
        while a%p==0:val+=w;a//=p
    return val
assert len(anchors)==66
assert x0==1-(1+delta-eps)/(C-1)
for g in anchors:
    assert X(g)==x0<1
    b=1-X(g)
    assert c-eps-X(g)==C*b
    assert max(X(B//g)-b,0)==max(X(B)-1,0)==F(47,550)
for g,h in combinations(anchors,2):assert X(gcd(g,h))<x0
assert sum(max(X(B)-1,0) for _ in anchors)==66*F(47,550)
print('PASS: 66 cold anchors pass the local scaled-raw threshold.')
print('PASS: no pair meets the cold-gcd merging threshold.')
print('PASS: all 66 banks charge the same target hinge 47/550.')
print('This diagnoses the missing joint allocation; it is not a positive optimizer.')
