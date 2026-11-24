from fractions import Fraction as F
from itertools import combinations, product
import random,math
import numpy as np

def factors(n):
 d=2; out={}
 while d*d<=n:
  while n%d==0:out[d]=out.get(d,0)+1;n//=d
  d+=1
 if n>1:out[n]=out.get(n,0)+1
 return out

T=20000
fs=[{}]+[factors(i) for i in range(1,T+1)]
primes=[i for i in range(2,101) if fs[i]=={i:1}]

def kernel_array(M,ws):
 X=np.array([sum(ws.get(p,0)*e for p,e in f.items()) for f in fs])
 K=np.zeros(T+1)
 Kloc=np.zeros(M+1)
 for p,wp in ws.items():
  vals=np.zeros(T+1)
  local=np.zeros(M+1)
  for d in range(p,min(M,math.isqrt(M*p))+1,p):
   f=fs[d]
   if any(q not in ws for q in f):continue
   om=sum(f.values());xd=sum(ws[q]*e for q,e in f.items())
   r=max(0,min(min(ws[q] for q in f),(xd-1)/om))
   if r:
    vals[d::d]=np.maximum(vals[d::d],r)
    local[d*d//p::d]=np.maximum(local[d*d//p::d],r)
  K += vals*np.array([f.get(p,0) for f in fs])
  Kloc += local*np.array([f.get(p,0) for f in fs[:M+1]])
 return X,K,Kloc

rng=random.Random(708)
for M in [18,20,24,30,36,48,60,80,100]:
 for it in range(200):
  ps=primes[:rng.randrange(2, min(9,len([p for p in primes if p<=M])))]
  ws={p:rng.choice([.25,.5,.75,1]) for p in ps}
  X,K,Kl=kernel_array(M,ws)
  c=np.cumsum(K)
  sums=c[M:]-c[:-M]
  pref=Kl.sum()
  j=int(np.argmin(sums));diff=pref-sums[j]
  if diff>1e-9:
   print('LOCAL_PREFIX_FAIL',M,ws,'shift',j,'pref',pref,'target',sums[j],'diff',diff,flush=True)
   # Do not terminate: seek restricted-full-tail counterexample.
  A=X[1:M+1]>2.1
  sa=Kl[1:M+1][A].sum()
  if sa-sums[j]>1e-9:
   print('LOCAL_TAIL_FAIL',M,ws,'shift',j,'sourceA',sa,'target',sums[j],'diff',sa-sums[j], 'n',sum(A),flush=True)
   raise SystemExit
 print('DONE',M,flush=True)
