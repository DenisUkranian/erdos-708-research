#!/usr/bin/env python3
"""Replay the newly closed branches, without relying on saved search outputs."""
from itertools import permutations
from math import isqrt
from pathlib import Path
from collections import Counter
import subprocess, tempfile, re

HERE=Path(__file__).resolve().parent

def divs(a):return [i for i in range(1,a+1) if a%i==0]
def smooth(a):
    for p in (2,3,5,7,11):
        while a%p==0:a//=p
    return a==1
u=[a for a in range(11,111) if smooth(a) and max(divs(a)[:-1])<11]
assert u==[11,12,14,15,16,18,20,21,25,27,35,49]
assert max(min(k*d*e for i,j,k in permutations((10,11,12)) for d in divs(a) if d>=i for e in divs(b) if e>=j) for a in u for b in u)==24010

def run(args, outfile=None):
    r=subprocess.run(list(map(str,args)), text=True, capture_output=True, check=True)
    if outfile is not None:outfile.write_text(r.stdout)
    else:print(r.stdout,end='')
    print(r.stderr,end='')
    return r

with tempfile.TemporaryDirectory() as tmp:
    t=Path(tmp)
    names=('smooth_frontier','filter','gcd_dp','crt12','high3_full','high3check','high3_dp','crt9')
    for name in names:
        subprocess.run(['g++','-O3','-std=c++17',str(HERE/'src'/f'{name}.cpp'),'-o',str(t/name)],check=True)
    d=t/'smooth.txt'
    r=run([t/'smooth_frontier','13','24009'],d)
    assert 'ROWS=205 BAD=2181725' in r.stderr
    assert len(d.read_text().splitlines())==2181725
    totals=[0,0,0]
    miss=[]
    lines=d.read_text().splitlines()
    intervals=[(13,378),(379,616),(617,850),(851,1176),(1177,24009)]
    for lo,hi in intervals:
        inp=t/'chunk.txt';out=t/'miss.txt'
        inp.write_text(''.join(s+'\n' for s in lines if lo<=int(s.split()[0])<=hi))
        r=run([t/'filter',inp],out)
        c=list(map(int,re.search(r'PACK=(\d+) GCD=(\d+) BAD=(\d+)',r.stderr).groups()))
        assert sum(c)==len(inp.read_text().splitlines())
        totals=[x+y for x,y in zip(totals,c)]
        miss.extend(out.read_text().splitlines())
    assert totals==[196177,1949872,35676]
    assert len(miss)==35676
    crt=[]
    for lo,hi in [(13,196),(197,240),(241,350),(351,24009)]:
        inp=t/'dp_in.txt';out=t/'dp_out.txt'
        inp.write_text(''.join(s+'\n' for s in miss if lo<=int(s.split()[0])<=hi))
        r=run([t/'gcd_dp',inp,hi,out])
        n,m=map(int,re.search(r'TOTAL demands=(\d+) misses=(\d+)',r.stderr).groups())
        assert n==len(inp.read_text().splitlines()) and m==len(out.read_text().splitlines())
        crt.extend(out.read_text().splitlines())
    assert len(crt)==1696
    inp=t/'crt_in.txt';inp.write_text('\n'.join(crt)+'\n')
    r=run([t/'crt12',inp]);assert 'ALL_PASS rows=1696 ' in r.stdout
    print('PASS: corrected smooth branch')
    d=t/'high3.txt';r=run([t/'high3_full'],d)
    assert 'GROUPS=722 SETS=4970 DEMANDS=4882 MAX_M=960' in r.stderr
    out=t/'high3_miss.txt';r=run([t/'high3check',d],out)
    assert 'ROWS=4882 PASS=4855 MISS=27' in r.stderr
    rows=sorted({' '.join([s.split()[0],*s.split()[2:7]]) for s in out.read_text().splitlines()})
    assert len(rows)==26
    inp=t/'high3_dp_in.txt';inp.write_text('\n'.join(rows)+'\n')
    out=t/'high3_dp_out.txt';r=run([t/'high3_dp',inp,24009,out]);assert 'TOTAL demands=26 misses=3' in r.stderr
    r=run([t/'crt9',out]);assert 'ALL_PASS rows=3 ' in r.stdout
    print('PASS: normalized obstruction with one high prime of support three excluded')
    print('These are partial closures, not global g(9)=12.')
