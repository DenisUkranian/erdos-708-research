import math,json,itertools
from pathlib import Path

def prime(p):return p>=2 and all(p%d for d in range(2,math.isqrt(p)+1))
ps=[p for p in range(11,420) if prime(p)]
def smooth7(a):
 for p in (2,3,5,7):
  while a%p==0:a//=p
 return a==1
ss=[s for s in range(2,68) if smooth7(s)]
rows=[];pre=0
for q,r in itertools.combinations([t for t in ps if t*t<4608],2):
 for p in ps:
  if p<=r:continue
  for a,b in itertools.product((1,2),repeat=2):
   if a==b==1:continue
   for c in range(1,9):
    if c==a*b:continue
    K=a**3*b**3*c
    top=min(4607,9*K-1)
    if max(p*q*a,p*r*b,q*r*c)>=min(top+1,p*p):continue
    for s in ss:
     A=sorted([p*q*a,p*r*b,p*s,q*r*a*b,q*a*s,r*b*s,q*r*c])
     M=A[-1]
     if M>top or p*p<=M or q*q>M or r*r>M:continue
     if min(9*q*q,9*r*r)<=M:continue
     if len(set(A))<7:continue
     pre+=1
     if any(k*x not in A for x in A for k in range(2,M//x+1)):continue
     rows.append(dict(A=A,M=M,p=p,q=q,r=r,a=a,b=b,c=c,s=s,K=K))
print('preclosure',pre,'closed',len(rows))
Path('g7_exact/three/high_c2_candidates.json').write_text(json.dumps(rows,indent=2))
for x in rows[:15]:print(x)
