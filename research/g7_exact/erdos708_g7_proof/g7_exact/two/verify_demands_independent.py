"""Independent expansion, domination and slot-certificate checks for TWO."""
from pathlib import Path
from itertools import combinations
from functools import lru_cache
from collections import defaultdict
from math import gcd,prod
import json,time
base=Path(__file__).resolve().parent
start=time.time()
def smooth7(a):
 for r in (2,3,5,7):
  while a%r==0:a//=r
 return a==1
small=[a for a in range(1,666) if smooth7(a)]
@lru_cache(None)
def valuations(a,p,q):
 es=[]
 for r in (2,3,5,7,p,q):
  e=0
  while a%r==0:a//=r;e+=1
  es.append(e)
 assert a==1
 return tuple(es)
@lru_cache(None)
def pair(a,b,M,p,q):
 es=[x+y for x,y in zip(valuations(a,p,q),valuations(b,p,q))]
 factors=[]
 for r,e in zip((2,3,5,7,p,q),es):factors.extend([r]*e)
 factors.sort(reverse=True);caps=[M//7,M//8,M//9]
 for mode in range(3):
  bins=[1,1,1]
  for r in factors:
   choices=[i for i in range(3) if bins[i]*r<=caps[i]]
   if not choices:break
   take=choices[0]
   for j in choices[1:]:
    if mode==1 and caps[j]*bins[take]<caps[take]*bins[j]:take=j
    if mode==2 and caps[j]*bins[take]>caps[take]*bins[j]:take=j
   bins[take]*=r
  else:
   assert prod(bins)==a*b and all(x<=y for x,y in zip(bins,caps))
   return True
 return False
expected=set();actual=0;rows=0;removed=0
for line in (base/'nontrivial_unresolved.txt').read_text().splitlines():
 p,q,M,z,*A=map(int,line.split());rows+=1
 assert z in (0,1) and M<=665
 if z==0:
  choices=[None]
 elif M not in A:
  assert smooth7(M)
  choices=[M]
 else:choices=[b for b in small if M<2*b and b<M]
 for b in choices:
  B=tuple(sorted(A if b is None else A+[b]))
  assert len(B)==len(set(B))==7 and max(B)==M
  if gcd(*B)!=1:continue
  if b is not None and any(pair(a,b,M,p,q) for a in A):removed+=1;continue
  assert all(k*a in B for a in B for k in range(2,M//a+1))
  E=tuple(sum(es) for es in zip(*(valuations(a,p,q) for a in B)))
  expected.add((p,q,M,E));actual+=1
full=json.loads((base/'full_demands.json').read_text())
claimed={(x['p'],x['q'],x['M'],tuple(x['E'])) for x in full}
assert len(full)==len(claimed)==33939 and expected==claimed
assert rows==45335 and actual==116394 and removed==25782
front=json.loads((base/'frontier_demands.json').read_text())
assert len(front)==24511
fg=defaultdict(list)
for row in front:
 p,q,M=row['p'],row['q'],row['M'];E=tuple(row['E']);A=row['A']
 assert (p,q,M,E) in claimed
 assert max(A)==M and E==tuple(sum(es) for es in zip(*(valuations(a,p,q) for a in A)))
 fg[p,q,M].append(E)
for p,q,M,E in expected:
 assert any(all(a<=b for a,b in zip(E,F)) for F in fg[p,q,M]),(p,q,M,E)
cert={}
for line in (base/'slot_certificates.txt').read_text().splitlines():
 idx,n,*hs=map(int,line.split())
 assert len(hs)==n<=9 and idx not in cert and 0<=idx<len(front)
 cert[idx]=hs
assert len(cert)==len(front)
for idx,row in enumerate(front):
 M=row['M'];H=1
 for j,h in enumerate(cert[idx],1):
  assert 1<=h<=M and gcd(H,h)<=M//j
  H*=h
 demand=prod(p**e for p,e in zip((2,3,5,7,row['p'],row['q']),row['E']))
 assert H%demand==0
print(json.dumps(dict(status='PASS',nontrivial_rows=rows,actual_sets=actual,good_pair_removed=removed,full_demands=len(expected),dominating_frontiers=len(front),slot_certificates=len(cert),seconds=time.time()-start),indent=2))
