"""Exact rational checks of the proved certificate; no g(n) calculation."""
from fractions import Fraction as F
from itertools import product
from random import Random
from math import prod

def r_of(E,u):
 return max(F(0),min(min(u[i] for i in E),(sum(u[i] for i in E)-1)/len(E)))

def verify(u,l):
 n=len(u);L=sum(l);m=[F(0)]*n
 for mask in range(1,1<<n):
  E=[i for i in range(n) if mask>>i&1]
  r=r_of(E,u);size=sum(l[i] for i in E)
  for i in E:
   if 2*size-l[i]<=L:m[i]=max(m[i],r)
 assert max(sum(u)-2,0)<=sum(m)<=max(sum(u)-1,0),(u,l,m)
 return m

count=0
for n in range(1,4):
 for u in product((F(0),F(1,4),F(1,2),F(3,4),F(1)),repeat=n):
  for l in product((1,2,5),repeat=n):verify(u,l);count+=1
rng=Random(708)
for n in range(4,11):
 for _ in range(160):
  u=[F(rng.randrange(0,21),20) for i in range(n)]
  l=[rng.randrange(1,1001) for i in range(n)]
  verify(u,l);count+=1
# Equality in the source constant 2, with arbitrarily many factors.
for k in range(2,9):
 u=[F(1,k)+F(1,100*k)]*(2*k)
 m=verify(u,[1]*(2*k))
 assert sum(m)==sum(u)-2
 count+=1

def factors(t):
 d=2;out={}
 while d*d<=t:
  while t%d==0:out[d]=out.get(d,0)+1;t//=d
  d+=1
 if t>1:out[t]=out.get(t,0)+1
 return out

def kernel(t,M,w):
 f={p:e for p,e in factors(t).items() if w.get(p,F(0))>0}
 row={p:F(0) for p in f}
 ps=list(f)
 for es in product(*[range(f[p]+1) for p in ps]):
  if not sum(es):continue
  d=prod(p**e for p,e in zip(ps,es));om=sum(es)
  ud=sum(w[p]*e for p,e in zip(ps,es))
  rr=max(F(0),min(min(w[p] for p,e in zip(ps,es) if e),(ud-1)/om))
  for p,e in zip(ps,es):
   if e and d*d<=M*p:row[p]=max(row[p],rr)
 return sum(f[p]*row[p] for p in ps)

w={2:F(1),3:F(1)};M=18;I=range(9,27)
prefix=sum(kernel(a,M,w) for a in range(1,M+1))
target=sum(kernel(b,M,w) for b in I)
A=[a for a in range(1,M+1) if sum(w.get(p,0)*e for p,e in factors(a).items())>F(21,10)]
restricted=sum(kernel(a,M,w) for a in A)
local=sum(kernel(a,a,w) for a in range(1,M+1))
assert prefix==F(17,2) and target==8 and restricted==F(13,2)
assert A==[8,12,16,18]
print('PASS:',count,'exact weighted-size profiles, including source-sharp families.')
print('Exact whole-prefix ambient-kernel obstruction: M=18, w2=w3=1, I=[9,26].')
print('ambient prefix=',prefix,'target=',target,'full-tail source=',restricted,'actual-size prefix=',local)
print('The obstruction does not refute actual-size-kernel or full-tail transfer.')
