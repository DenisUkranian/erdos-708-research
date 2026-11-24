import json,math,itertools
from pathlib import Path

def prime(p):return p>=2 and all(p%d for d in range(2,math.isqrt(p)+1))
PS=[p for p in range(11,250) if prime(p)]
rows=[]
pre=0
for p in [11,13]:
 for u in range(1,9):
  if p>=2*u:continue
  top=2*p*p*u-1
  choices=[(q,a,q*a) for q in PS if q!=p for a in range(1,9) if p*q*a<=top]
  for (q,a,v),(r,b,w) in itertools.combinations(choices,2):
   if q>=r:continue
   for c,d in itertools.combinations(range(1,9),2):
    A=sorted([p*p*u,p*v,p*w,u*v,u*w,q*r*c,q*r*d])
    M=A[-1]
    if M>top or len(set(A))<7:continue
    if any(9*t*t<=M for t in (p,q,r)):continue
    if M//(u*v)!=1 or M//(u*w)!=1:continue
    if M//(p*p*u)!=1:continue
    pre+=1
    if any(k*x not in A for x in A for k in range(2,M//x+1)):continue
    rows.append(dict(A=A,p=p,u=u,q=q,r=r,a=a,b=b,c=c,d=d,M=M))
print('preclosure',pre,'closed',len(rows))
Path('g7_exact/three/low_support3_candidates.json').write_text(json.dumps(rows,indent=2))
for x in rows[:20]:print(x)
