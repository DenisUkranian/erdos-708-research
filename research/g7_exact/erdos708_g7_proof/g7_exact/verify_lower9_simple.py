"""Exact check of the simple nine-point lower witness for g(7)."""
from math import prod
import json
primes=(17,19,23,29)
A=(17**2,17*19,19**2,17*23,19*23,17*29,19*29)
M=max(A)
N=17**2*19**2*23*29
radius=(M-1)//2
I=range(N-radius,N+radius+1)
def v(a,p):
    e=0
    while a%p==0:
        a//=p;e+=1
    return e
D=tuple(sum(v(a,p) for a in A) for p in primes)
C=tuple(v(N,p) for p in primes)
assert len(set(A))==7 and M==551 and N==69587443
assert D==(5,5,2,2) and C==(2,2,1,1)
assert len(I)==M and min(I)>0
for b in I:
    if b==N:continue
    vb=tuple(v(b,p) for p in primes)
    assert sum(e>0 for e in vb)<=1
    assert vb[0]<=1 and vb[1]<=1
# If N is selected, the four disjoint off-center demands require 3+3+1+1 points.
# If N is not selected, the first two demands require 5+5 points, and the other two at least one each.
lower_with_center=1+3+3+1+1
lower_without_center=5+5+1+1
assert min(lower_with_center,lower_without_center)==9
B=[N+d for d in (0,17,34,51,19,38,57,23,29)]
assert len(set(B))==9 and all(b in I for b in B)
assert prod(B)%prod(A)==0
print(json.dumps(dict(status='PASS',A=list(A),M=M,N=N,interval=[min(I),max(I)],shift=min(I)-1,demand=D,center=C,lower_with_center=lower_with_center,lower_without_center=lower_without_center,cover=sorted(B),tau=9),indent=2))
