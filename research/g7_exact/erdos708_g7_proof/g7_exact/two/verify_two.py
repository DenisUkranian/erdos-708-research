#!/usr/bin/env python3
"""Portable replay of the complete two-large-prime finite component.

Only Python's standard library and a C++17 compiler are required. This
checks explicit certificates, not the certificate-search algorithm.
"""
from pathlib import Path
from collections import defaultdict
import hashlib,json,math,shutil,subprocess,sys,tempfile,time
HERE=Path(__file__).resolve().parent

def valuation(n,primes):
    out=[]
    for p in primes:
        e=0
        while n%p==0:n//=p;e+=1
        out.append(e)
    assert n==1
    return tuple(out)

def main():
    start=time.monotonic()
    with tempfile.TemporaryDirectory(prefix='erdos708_two_') as td:
        temp=Path(td);dest=temp/'g7_exact'/'two';dest.mkdir(parents=True)
        for name in ['envelope','enumerate_nontrivial']:
            binary=temp/name
            subprocess.run(['g++','-O3','-std=c++17',str(HERE/(name+'.cpp')),'-o',str(binary)],check=True,capture_output=True,text=True)
            result=subprocess.run([str(binary)],cwd=temp,check=True,capture_output=True,text=True)
            if name=='envelope':
                summary=json.loads(result.stdout)
                assert summary=={'pairs':1123,'configs':128915,'eligible':2980414,'closed':2784139,'residual':196275,'maxM':24696,'z':[162482,33781,0,12]},summary
                print('PASS complete two-prime envelope:',summary,flush=True)
            else:
                assert result.stdout.strip()=='configs=50660 cliques=112998 closed=67663 unresolved=45335',result.stdout
                print('PASS complete colored-clique replay:',result.stdout.strip(),flush=True)
        shutil.copy2(HERE/'full_demands.py',dest/'full_demands.py')
        result=subprocess.run([sys.executable,str(dest/'full_demands.py')],cwd=temp,check=True,capture_output=True,text=True)
        expansion=json.loads(result.stdout)
        for k,v in [('nontrivial_rows',45335),('actual_sets',116394),('good_pair_removed',25782),('demands',33939),('frontier',24511)]:assert expansion[k]==v,(k,expansion)
        full=json.loads((dest/'full_demands.json').read_text())
        frontier=json.loads((dest/'frontier_demands.json').read_text())
        assert frontier==json.loads((HERE/'frontier_demands.json').read_text())
        print('PASS full-source expansion: 116394 sets, 33939 demands',flush=True)
        certificates={}
        for line in (HERE/'slot_certificates.txt').read_text().splitlines():
            i,k,*hs=map(int,line.split())
            assert i not in certificates and k==len(hs)<=9
            certificates[i]=hs
        assert set(certificates)==set(range(len(frontier)))
        dominating=defaultdict(list)
        for i,row in enumerate(frontier):
            p,q,M=row['p'],row['q'],row['M'];A=row['A'];E=tuple(row['E']);primes=[2,3,5,7,p,q]
            assert len(A)==len(set(A))==7 and min(A)>=2 and max(A)==M
            expected=tuple(map(sum,zip(*(valuation(a,primes) for a in A))))
            assert expected==E
            H=1
            for j,h in enumerate(certificates[i],1):
                assert 1<=h<=M and math.gcd(H,h)<=M//j,(i,j,H,h,M)
                H*=h
            assert H%math.prod(A)==0
            dominating[p,q,M].append(E)
        print('PASS all 24511 nine-slot certificates by exact gcd and divisibility',flush=True)
        for row in full:
            E=row['E'];key=(row['p'],row['q'],row['M'])
            assert any(all(a<=b for a,b in zip(E,F)) for F in dominating[key]),row
        print('PASS independent certificate domination of all 33939 demands',flush=True)
    result={'status':'PASS','seconds':round(time.monotonic()-start,3),'finite_maximum':24696,'residual_actual_maximum':665,'full_source_sets':116394,'demands':33939,'certificates':24511,'source_sha256':{n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in ['envelope.cpp','enumerate_nontrivial.cpp','full_demands.py']}}
    (HERE/'verification_result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':main()
