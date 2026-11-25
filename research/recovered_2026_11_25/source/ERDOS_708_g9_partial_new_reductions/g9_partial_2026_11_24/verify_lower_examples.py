"""Three attained sharp bounds on a single explicit interval in the proved large regime."""
from math import prod
import json
small=(127,131,137,139)
large=(173,179)
M=max(small)*max(large)
radius=(M-1)//2
u,period=0,1
for p in (*small,*large):
    q=p*p
    residue=p if p in small else p*(p-1)//2
    u+=period*((residue-u)*pow(period,-1,q)%q)
    period*=q
assert u>radius and M==24881
for z in range(u-radius,u+radius+1):
    if z!=u:assert sum(z%p==0 for p in (*small,*large))<=1
    assert all(z%(p*p)!=0 for p in large)
assert all(u%p==0 and u%(p*p)!=0 for p in (*small,*large))
rows=[]
for n in (7,8,9):
    ps=(127,131,139) if n==7 else small
    h=len(ps)
    extra=n%2
    A=sorted([p*q for p in ps for q in large]+([large[0]] if extra else []))
    offsets=[0,*ps]+[j*q for k,q in enumerate(large) for j in range(1,h+(extra if k==0 else 0))]
    assert len(A)==len(set(A))==n and max(A)==M
    assert len(offsets)==len(set(offsets)) and max(map(abs,offsets))<=radius
    assert prod(u+j for j in offsets)%prod(A)==0
    lower_with=1+h+2*(h-1)+extra
    lower_without=3*h+extra
    assert len(offsets)==min(lower_with,lower_without)
    rows.append({'n':n,'A':A,'tau':len(offsets),'lower_with_center':lower_with,
                 'lower_without_center':lower_without,'offsets_from_center':offsets})
print(json.dumps({'M':M,'center':u,'first':u-radius,'last':u+radius,'cases':rows},indent=2))
