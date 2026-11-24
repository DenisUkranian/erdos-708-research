#!/usr/bin/env python3
"""Exact integer/rational sanity checks for the adaptive-cutoff certificate.
These tests supplement, and do not replace, the mathematical proof.
"""
from fractions import Fraction as F
import math,json
from pathlib import Path

DEN=20

def data(n,ps,ws):
    s=1;x=0;largest=1
    for p,w in zip(ps,ws):
        while n%p==0:
            n//=p;s*=p;x+=w;largest=p
    return s,x,largest

def check(M,ps,ws):
    y=min(ps);fam=[]
    for d in range(1,M//y+1):
        s,x,pmax=data(d,ps,ws)
        if s==d and DEN<x<=2*DEN and d*pmax<=M:
            fam.append((d,x-DEN,x,pmax))
    lookup={d:(h,x,pmax) for d,h,x,pmax in fam}
    prefix=0;low=0;high=0
    for a in range(1,M+1):
        s,x,pmax=data(a,ps,ws)
        lhs=max(x-2*DEN,0);prefix+=lhs
        if not lhs:continue
        remainder=s//pmax;_,u,_=data(remainder,ps,ws)
        assert u>DEN
        if 3*u>=4*DEN:
            cand=[d for d,h,xd,pm in fam if remainder%d==0 and 3*xd>=4*DEN]
            assert cand,(M,ps,ws,a,remainder,u)
            d=cand[0];high+=1
        else:
            d=remainder;low+=1
            assert d in lookup
            h,xd,pm=lookup[d]
            assert lhs*DEN<=h*(x-xd)
        h,xd,pm=lookup[d]
        assert d*pm<=a
        assert lhs*DEN<=3*h*(x-xd)
    center=math.prod(p*p for p in ps)
    bs=list(range(1,2501))+[center+j for j in range(-M,min(M,1000)+1) if center+j>0]
    for b in bs:
        val=0;positives=[]
        for d,h,xd,pm in fam:
            if b%d:continue
            coeff=1-sum(b%(d*p)==0 for p in ps if p<=M//d)
            val+=h*coeff
            if coeff>0:positives.append(d)
        assert len(positives)<=1,(M,ps,ws,b,positives)
        assert val<=max(data(b,ps,ws)[1]-DEN,0),(M,ps,ws,b,val)
    mu0=sum((F(1,p) for p in ps),F(0));muw=sum((F(w,DEN*(p-1)) for p,w in zip(ps,ws)),F(0))
    rho=max(F(i+2,p) for i,p in enumerate(ps));beta=1-mu0-rho
    S=sum((F(h,DEN*d) for d,h,_,_ in fam),F(0))
    assert F(prefix,DEN)<=3*M*muw*S
    for x in [0,M*M,max(0,center-M//2)]:
        totalK=F(0)
        for d,h,xd,pm in fam:
            n=(x+M)//d-x//d
            n-=sum((x+M)//(d*p)-x//(d*p) for p in ps if p<=M//d)
            assert F(n)>=F(M,d)*beta
            totalK+=F(h,DEN)*n
        assert totalK>=M*beta*S
        if 3*muw+mu0+rho<=1:
            rhs=sum(max(data(b,ps,ws)[1]-DEN,0) for b in range(x+1,x+M+1))
            assert prefix<=rhs
    return {'M':M,'primes':ps,'weights':[str(F(w,DEN)) for w in ws], 'carriers':len(fam),'high_cases':high,'low_cases':low,'prefix_hinge':str(F(prefix,DEN)),'criterion':str(3*muw+mu0+rho),'certificate_positions_checked':len(bs)}

if __name__=='__main__':
    records=[]
    for ps in [[2,3,5,7],[2,3,5,7,11,13],[5,11,37,101]]:
        for M in [30,60,120,400]:
            for pattern in [[20]*6,[11,12,19,3,5,0],[14,14,14,1,7,9],[13,13,13,1,7,9],[0]*6]:
                records.append(check(M,ps,pattern[:len(ps)]))
    records.append(check(20000,[17,19,23],[20,20,20]))
    result={'cases':len(records),'certificate_positions_checked':sum(r['certificate_positions_checked'] for r in records),'low_U_sources_checked':sum(r['low_cases'] for r in records),'high_U_sources_checked':sum(r['high_cases'] for r in records),'records':records}
    Path(__file__).with_name('adaptive_certificate_checks.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({k:v for k,v in result.items() if k!='records'}))
    print(json.dumps(records[-1]))
