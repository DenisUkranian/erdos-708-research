#!/usr/bin/env python3
"""Exact independent finite checks for the conditional structural/tail proof.
Run without Python -O. Standard library only. This does NOT prove g(9)=12.
"""
from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations, product
from math import isqrt
from bisect import bisect_left, bisect_right


def types(v):
    for l in range(v+1):
        if 3*(v-l)>9 or 3*v+2*l>18:
            continue
        ts=[()]+[(i,) for i in range(v)]+[(i,i) for i in range(l)]
        ts += [x for x in combinations(range(v),2) if x[0]<l]
        for xs in combinations_with_replacement(ts,9):
            m=Counter(xs)
            D=[sum(x.count(i) for x in xs) for i in range(v)]
            support=[sum(i in x for x in xs) for i in range(v)]
            if min(support)<3 or any(support[i]<5 for i in range(l)):
                continue
            F=[]
            for i in range(l):
                t=m[i,i]
                fs=[f for f in range(max(1,t),(D[i]-2)//2+1)
                    if (t==0 or D[i]>=2*f+3)
                    and not(t>=2 and f==t and D[i]<=2*f+3)]
                if not fs:
                    break
                F.append(max(fs))
            if len(F)!=l:
                continue
            c=[f+1 for f in F]+[1]*(v-l)
            caps={x:isqrt(c[x[0]]*c[x[1]]-1) for x in m if len(x)==2}
            if any(m[x]>k for x,k in caps.items()):
                continue
            yield l,m,D,support,c,caps


def verify_types():
    expected={1:Counter({0:7,1:20}),2:Counter({0:10,1:25,2:16}),3:Counter({0:1,1:2}),4:Counter()}
    for v in range(1,5):
        ct=Counter()
        for l,m,D,support,c,caps in types(v):
            ct[l]+=1
            if v==3:
                if l==0:
                    assert m==Counter({(0,):3,(1,):3,(2,):3})
                else:
                    assert l==1 and m[(0,0)] in (0,1)
                    t=m[(0,0)]
                    want=Counter({(0,):3-t,(1,):2,(2,):2,(0,1):1,(0,2):1})
                    if t:want[(0,0)]=1
                    assert m==want and all(a==1 for a in caps.values())
                print('v=3 low=',l,'pattern=',sorted(m.items()))
        assert ct==expected[v],(v,ct)
        print('type counts',v,sorted(ct.items()))
    for v in (5,6):
        assert all(3*(v-l)>9 or 3*v+2*l>18 for l in range(v+1))


def factors(n):
    a=[]
    p=2
    while p*p<=n:
        while n%p==0:a.append(p);n//=p
        p+=1
    if n>1:a.append(n)
    return a


def divs(n):
    return [d for d in range(1,n+1) if n%d==0]


def verify_costs():
    # A divisibility-minimal divisor >=11 of an 11-smooth number is <=110.
    U=[d for d in range(11,111) if max(factors(d))<=11
       and all(e<11 for e in divs(d)[:-1])]
    assert U==[11,12,14,15,16,18,20,21,25,27,35,49]
    C={}
    for a,b in product(U,repeat=2):
        C[a,b]=min(k*d*e for i,j,k in permutations((10,11,12))
                   for d in divs(a) if d>=i for e in divs(b) if e>=j)
    assert max(C.values())==24010
    bad={(a,b):z for (a,b),z in C.items() if a<=b and z>9450}
    assert bad=={(21,49):10290,(25,49):12250,(27,49):13230,
                 (35,35):12250,(35,49):17150,(49,49):24010}
    print('pair thresholds above 9450:',bad)


def prime_sieve(N):
    s=bytearray(b'\x01')*(N+1);s[:2]=b'\0\0'
    for p in range(2,isqrt(N)+1):
        if s[p]:s[p*p:N+1:p]=b'\0'*((N-p*p)//p+1)
    return [i for i in range(13,N+1) if s[i]]

P=prime_sieve(24010)


def power_list(M,factor,start):
    """Overestimate of source valuations for s=factor*7^e, h=1 or one large prime.
    Uses at most three active large primes and 12*a>M, 9*p^2>M.
    """
    arr=[];e=start
    while factor*7**e<=M:
        s=factor*7**e
        if 12*s>M:arr.append(e)
        L=max(13,isqrt(M//9)+1,M//(12*s)+1)
        H=M//s
        count=max(0,bisect_right(P,H)-bisect_left(P,L))
        arr += [e]*min(3,count)
        e+=1
    return sorted(arr+[1]*9,reverse=True)


def supply(M,h,p):
    n=M//h;v=0;t=h
    while t%p==0:t//=p;v+=1
    out=n*v
    while n:n//=p;out+=n
    return out


def verify_tail():
    margins={}
    def upd(key,v,M,allow=0):
        assert v>=allow,(key,v,M)
        if key not in margins or v<margins[key][0]:margins[key]=(v,M)
    for M in range(9450,24010):
        pur=power_list(M,1,2)
        mix=power_list(M,5,1)
        E=sum(pur[2:9])
        # A deficit of one is repaired by one additional prime unit in the SAME slot.
        upd('49,49 p7',supply(M,2401,7)-E-4,M,-1)
        for d,h,p,ep,e7,end in [(21,1029,3,1,3,10289),(25,1225,5,2,2,12249),
                                (27,1323,3,3,2,13229),(35,1715,5,1,3,17149)]:
            if M>end:continue
            E=sum(pur[1:8])
            upd(f'{d},49 p7',supply(M,h,7)-E-e7,M)
            Eother=10 if p==3 else 5
            upd(f'{d},49 p{p}',supply(M,h,p)-Eother-ep,M)
        if M<=12249:
            E=sum(sorted(pur+mix[2:],reverse=True)[:7])
            upd('35,35 p7',supply(M,1225,7)-E-2,M)
            upd('35,35 p5',supply(M,1225,5)-9,M)
    print('minimum exact supply margins (margin, M):')
    for key,value in sorted(margins.items()):print(key,value)
    assert 9450>=max(2*10**3,3*10**3,4*10**2)


def witness():
    from math import prod
    A=[841,899,961,1073,1147,1189,1247,1271,1333]
    x=155833862424257354;M=max(A);center=667
    ps=[29,31,37,41,43]
    D=[6,6,2,2,2];central=[2,2,1,1,1];caps=[1,1,2,2,2]
    def vp(n,p):
        e=0
        while n%p==0:n//=p;e+=1
        return e
    assert len(A)==len(set(A))==9
    assert prod(A)==prod(p**d for p,d in zip(ps,D))
    for j in range(1,M+1):
        v=[vp(x+j,p) for p in ps]
        if j==center:assert v==central
        else:assert sum(e>0 for e in v)<=1 and all(e<=c for e,c in zip(v,caps))
    lb=min(sum((d+c-1)//c for d,c in zip(D,caps)),
           1+sum((max(0,d-e)+c-1)//c for d,e,c in zip(D,central,caps)))
    offsets=[667,638,696,609,725,636,698,605,729,630,626,624]
    assert lb==len(offsets)==len(set(offsets))==12
    assert all(1<=j<=M for j in offsets)
    assert prod(x+j for j in offsets)%prod(A)==0
    print('lower witness: exact tau=12')

if __name__=='__main__':
    verify_types();verify_costs();verify_tail();witness()
    print('PASS: conditional structural and tail checks; global exact g(9) is NOT established.')
