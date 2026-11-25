#!/usr/bin/env python3
"""Reproduce the unconditional lower g(9)>=12 and the conditional upper g(9)<=13.

Requires python3, g++ (C++17). Does not rely on floating-point optimization.
For the upper bound, use the bundled preceding g(8)<=11 proof separately.
"""
from pathlib import Path
from collections import Counter
from itertools import combinations
import hashlib
import math
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent
SRC=ROOT/'src'
DATA=ROOT/'data'
PR=(2,3,5,7,11)

def cmd(args,cwd,expected=None, logfile=None):
    r=subprocess.run(list(map(str,args)),cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,check=True)
    if logfile:
        Path(logfile).write_text(r.stdout+'\nSTDERR:\n'+r.stderr)
    if expected is not None and expected not in r.stdout+r.stderr:
        raise AssertionError('Expected '+expected+' not found. Output: '+(r.stdout+r.stderr)[-1600:])
    print('  ',args[0],args[-1] if len(args)>1 else '',(r.stdout+r.stderr)[-260:].strip())
    return r

def check_lower():
    A=[841,899,961,1073,1147,1189,1247,1271,1333]
    M=max(A)
    N=155833862424258021
    x=N-667
    assert M==1333 and x==155833862424257354
    Q=(29,31,37,41,43)
    def val(k,p):
        z=0
        while k%p==0:
            z+=1;k//=p
        return z
    need=tuple(sum(val(a,p) for a in A) for p in Q)
    assert need==(6,6,2,2,2),need
    center=tuple(val(N,p) for p in Q)
    assert center==(2,2,1,1,1),center
    for delta in range(-666,667):
        if delta==0:continue
        v=tuple(val(N+delta,p) for p in Q)
        assert sum(z>0 for z in v)<=1 and v[0]<=1 and v[1]<=1,(delta,v)
    # Each noncentral target has at most one active prime; p=29,31 carry at most
    # one exponent each. For p=37,41,43, each remaining demand needs one position.
    # With center: 1+4+4+1+1+1=12; without: 6+6+1+1+1=15.
    assert 1+(need[0]-center[0])+(need[1]-center[1])+3==12
    assert need[0]+need[1]+3==15
    offsets=(0,29,58,87,116,31,62,93,124,37,41,43)
    assert len(set(offsets))==12 and len(offsets)==12 and max(map(abs,offsets))<=666
    covered=tuple(sum(val(N+d,p) for d in offsets) for p in Q)
    assert all(v>=n for v,n in zip(covered,need)),(need,covered)
    print('LOWER VERIFIED: tau(A,I)=12 for explicit n=9, M=1333.')

def prime_exponents(n):
    a=[]
    for p in PR:
        r=0
        while n%p==0:
            n//=p;r+=1
        a.append(r)
    return n,tuple(a)

def easy(a,M):
    for d in range(1,math.isqrt(a)+1):
        if a%d:continue
        c=a//d
        if (d<=M//12 and c<=M//13) or (c<=M//12 and d<=M//13):return True
    return False

def check_finite_gate():
    sm=[(a,prime_exponents(a)[1]) for a in range(2,1573) if prime_exponents(a)[0]==1]
    possible=[]
    for M,e in sm:
        if M<=13 or easy(M,M):continue
        n=1+sum(a<M and not easy(a,M) for a,_ in sm)
        if n>=9:possible.append(M)
    assert len(possible)==65 and max(possible)==250,(len(possible),max(possible),possible)
    print('REDUCTION VERIFIED: only 65 possible hard maxima, all M<=250.')
    # Independent check of analytic M>=1573 split: each 11-smooth M has a factor
    # d in [12,121] and d<=M//13, complementary factor <=M//12.
    for M in range(1573,300000):
        if prime_exponents(M)[0]!=1:continue
        assert easy(M,M),M
    print('ANALYTIC GATE SPOT-CHECK: all 11-smooth M<=300000 split at 12,13.')

def check_file_same(a,b):
    aa=hashlib.sha256(Path(a).read_bytes()).hexdigest()
    bb=hashlib.sha256(Path(b).read_bytes()).hexdigest()
    assert aa==bb,(a,b,aa,bb)
    print('MATCH:', Path(a).name, aa[:16])

def main():
    check_lower()
    check_finite_gate()
    with tempfile.TemporaryDirectory(prefix='g9_upper13_') as p:
        path=Path(p)
        for n in ('hard13','pareto5','gcd13_5d','crt13_5d'):
            cmd(['g++','-std=c++17','-O3','-UNDEBUG',SRC/(n+'.cpp'),'-o',path/n],path)
        t=path/'raw.txt'
        cmd([path/'hard13',t],path,expected='DEMANDS=658192',logfile=path/'enumeration.log')
        check_file_same(t,DATA/'hard13_demands.txt')
        f=path/'frontier.txt'
        cmd([path/'pareto5',t,f],path,expected='FRONTIER=89666',logfile=path/'pareto.log')
        check_file_same(f,DATA/'hard13_frontier.txt')
        missing=path/'missing.txt'
        cmd([path/'gcd13_5d',f,250,missing],path,expected='misses=5170',logfile=path/'gcd.log')
        check_file_same(missing,DATA/'hard13_misses.txt')
        cmd([path/'crt13_5d',missing],path,expected='ALL_PASS rows=5170',logfile=path/'crt.log')
    print('ALL CHECKS PASS: g(9)>=12; g(9)<=13 conditional on verified previous g(8)<=11.')
    print('THE EXACT VALUE (12 OR 13) IS NOT DETERMINED BY THIS PACKAGE.')

if __name__=='__main__':main()
