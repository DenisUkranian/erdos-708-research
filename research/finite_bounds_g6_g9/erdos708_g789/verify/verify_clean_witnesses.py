"""Exact constructive certificates for Erdős 708: g(6)>=8,g(7)>=9,g(8)>=11,g(9)>=12.
The n=6 witness is from C. Bergström, DOI 10.5281/zenodo.24366897, Proposition 3.
The n=7,8,9 witnesses below were derived independently on 2026-11-24.
Standard-library Python only. All arithmetic is integer arithmetic.
"""
from math import prod, isqrt
import json
from pathlib import Path


def vp(a,p):
    e=0
    while a%p == 0:
        a//=p
        e+=1
    return e


def crt(residues, moduli):
    r=0
    m=1
    for a,q in zip(residues,moduli):
        r += m*((a-r)*pow(m,-1,q)%q)
        m *= q
    assert all(r%q == a%q for a,q in zip(residues,moduli))
    return r,m


def make_odd(n, p,q, highs):
    A=sorted([p*p,p*q,q*q]+[r*s for r in (p,q) for s in highs])
    M=max(A); center=(M+1)//2
    y,period=crt([p*p,q*q]+list(highs),[p**3,q**3]+[r*r for r in highs])
    while y<center:y+=period
    x=y-center
    demand=len(highs)+1
    offsets=[center]
    for r in (p,q):
        for k in range(1,demand+1):
            t=(k+1)//2 * (-1 if k%2 else 1)
            offsets.append(center+t*r)
    offsets += [center-r for r in highs]
    return dict(n=n,A=A,M=M,x=x,center=center,primes=[p,q]+list(highs),
                central=[2,2]+[1]*len(highs),off_caps=[1,1]+[2]*len(highs),
                offsets=offsets,lower=3*len(highs)+3)


def make_eight():
    p=37; others=(41,43,47); q=53
    A=sorted([p*p]+[p*r for r in others]+[p*q]+[r*q for r in others])
    M=max(A);center=(M+1)//2
    y,period=crt([p*p]+list(others)+[((q-1)//2)*q],
                 [p**3]+[r*r for r in others]+[q*q])
    while y<center:y+=period
    offsets=[center,center-p,center+p,center-2*p,center+2*p]
    offsets += [center-r for r in others]
    offsets += [center-q,center+q,center-2*q]
    return dict(n=8,A=A,M=M,x=y-center,center=center,primes=[p]+list(others)+[q],
                central=[2,1,1,1,1],off_caps=[1,2,2,2,1],offsets=offsets,lower=11)


def verify(w):
    A=w['A'];M=w['M'];x=w['x'];c=w['center'];P=w['primes']
    assert len(A)==len(set(A))==w['n'] and max(A)==M
    assert all(all(p%k for k in range(2,isqrt(p)+1)) for p in P)
    D=[sum(vp(a,p) for a in A) for p in P]
    assert prod(p**d for p,d in zip(P,D))==prod(A)
    V=[[min(d,vp(x+j,p)) for p,d in zip(P,D)] for j in range(1,M+1)]
    assert V[c-1]==w['central']
    assert all(sum(v>0 for v in row)<=1 for j,row in enumerate(V,1) if j!=c)
    assert all(all(v<=cap for v,cap in zip(row,w['off_caps']))
               for j,row in enumerate(V,1) if j!=c)
    without=sum((d+cap-1)//cap for d,cap in zip(D,w['off_caps']))
    with_center=1+sum((max(0,d-e)+cap-1)//cap
                      for d,e,cap in zip(D,w['central'],w['off_caps']))
    assert min(without,with_center)==w['lower']
    offsets=w['offsets']
    assert len(offsets)==len(set(offsets))==w['lower']
    assert all(1<=j<=M for j in offsets)
    assert prod(x+j for j in offsets)%prod(A)==0
    w.update(demand=D,lower_with_center=with_center,lower_without_center=without)
    print(f"VERIFIED n={w['n']}: tau={w['lower']}, M={M}, x={x}, center={c}")
    print(' A =',A)
    print(' demand =',D,'central =',w['central'],'off-center caps =',w['off_caps'])
    print(' cover offsets =',offsets)
    return w


witnesses=[dict(n=6,A=[221,289,299,323,391,437],M=437,x=581200167,center=219,
               primes=[13,17,19,23],central=[1,2,1,1],off_caps=[2,1,2,1],
               offsets=[12,15,32,35,49,86,128,219],lower=8),
           make_odd(7,17,19,(23,29)),make_eight(),make_odd(9,29,31,(37,41,43))]
for w in witnesses:verify(w)
Path(__file__).with_name('clean_witnesses.json').write_text(json.dumps(witnesses,indent=2)+'\n')
