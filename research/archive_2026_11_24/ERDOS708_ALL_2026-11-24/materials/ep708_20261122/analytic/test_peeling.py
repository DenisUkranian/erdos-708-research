from math import gcd, isqrt, prod
from random import Random

def prime_factors(a):
 out={}
 p=2
 while p*p<=a:
  while a%p==0: out[p]=out.get(p,0)+1;a//=p
  p+=1
 if a>1:out[a]=out.get(a,0)+1
 return out

def vp(a,p):
 e=0
 while a%p==0: e+=1;a//=p
 return e

def extend(I,B,H,h):
 if h==1:return H
 for b in I:
  if b%h==0 and b not in B:
   B.add(b);return H*h
 g=gcd(H,h)
 for b in I:
  if b%g==0 and b not in B:
   B.add(b)
   assert prod(B)%(H*h)==0
   return H*h
 raise ValueError(('no extension',len(I),len(B),h,g))

def peel(A,x,Z,B0):
 M=max(A);I=range(x+1,x+M+1);sm=[a for a in A if max(prime_factors(a))<=Z]
 groups={}
 for a in A:
  p=max(prime_factors(a))
  if p>Z:groups.setdefault(p,[]).append(a)
 r=sum(map(len,groups.values()));t=len(groups);K=len(B0)+2*r-t
 assert Z>=K
 B=set(B0);H=prod(sm)
 assert prod(B)%H==0
 for p in sorted(groups):
  groups[p].sort()
  H=extend(I,B,H,groups[p][0])
 for p in sorted(groups):
  count=len(groups[p])-1
  if p*p<=M:
   for _ in range(count):H=extend(I,B,H,p)
  else:
   assert vp(H,p)==1
   target=count+1
   current=vp(prod(B),p)
   for b in I:
    if current>=target:break
    if b%p==0 and b not in B:
     B.add(b);current+=vp(b,p)
   assert current>=target
   H*=p**count
   assert prod(B)%H==0
 for p in sorted(groups):
  for a in groups[p][1:]:H=extend(I,B,H,a//p)
 assert H==prod(A)
 assert prod(B)%prod(A)==0
 assert len(B)<=K
 return len(B)

rng=Random(708)
count=0
for _ in range(12000):
 n=rng.randint(1,8);M=rng.randint(max(2,n+1),500);Z=rng.randint(2*n,4*n)
 pool=[a for a in range(2,M+1) if max(prime_factors(a))>Z]
 if len(pool)<n:continue
 A=rng.sample(pool,n);x=rng.randint(0,10**7)
 peel(A,x,Z,set());count+=1
print('rough-only cases passed',count)
# Initial smooth covers constructed by per-prime distinct-power assignment.
count=0
for _ in range(6000):
 n=rng.randint(1,8);M=rng.randint(max(2,n+1),500);A=rng.sample(range(2,M+1),n);M=max(A);x=rng.randint(0,10**7)
 Z=4*n+8;sm=[a for a in A if max(prime_factors(a))<=Z]
 pp={}
 for a in sm:
  for p,e in prime_factors(a).items():pp.setdefault(p,[]).append(e)
 B0=set()
 for p,es in pp.items():
  used=set()
  for e in sorted(es,reverse=True):
   b=next(b for b in range(x+1,x+M+1) if b%p**e==0 and b not in used)
   used.add(b)
  B0.update(used)
 r=n-len(sm);t=len({max(prime_factors(a)) for a in A if max(prime_factors(a))>Z})
 if Z<len(B0)+2*r-t:continue
 peel(A,x,Z,B0);count+=1
print('mixed cases passed',count)
