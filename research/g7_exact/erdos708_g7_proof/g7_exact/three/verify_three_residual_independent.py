from pathlib import Path
from itertools import combinations,product
from math import gcd,prod
import json
base=Path(__file__).resolve().parent.parent/'finite'
def small(x):
 for p in (2,3,5,7):
  while x%p==0:x//=p
 return x==1
expected=set();raw=0
for M in (1012,1035):
 cores=(23,143,253,299)
 pools=[[a for a in range(2,M+1) if a%d==0 and small(a//d) and 7*a>M] for d in cores]
 for singles in combinations(pools[0],2):
  for pairs in combinations(pools[1],3):
   for a,b in product(pools[2],pools[3]):
    A=tuple(sorted((*singles,*pairs,a,b)))
    if A[-1]!=M:continue
    raw+=1
    if gcd(*A)!=1:continue
    S=set(A)
    if any(k*x not in S for x in A for k in range(2,M//x+1)):continue
    assert len(S)==7
    expected.add(A)
cert=json.loads((base/'three_residual_slots.json').read_text())
claimed={tuple(x['A']) for x in cert}
assert raw==17640 and len(expected)==1096
assert len(cert)==len(claimed)==1096 and claimed==expected
for row in cert:
 A=row['A'];M=A[-1];ss=row['slots'];H=1
 assert row['M']==M and len(ss)<=9
 for j,h in enumerate(ss,1):
  assert isinstance(h,int) and 1<=h<=M
  assert gcd(H,h)<=M//j
  H*=h
 assert H%prod(A)==0
print('PASS: independent enumeration',raw,'raw;',len(expected),'complete eligible sets')
print('PASS: all',len(cert),'nine-slot certificates, arbitrary interval shifts')
