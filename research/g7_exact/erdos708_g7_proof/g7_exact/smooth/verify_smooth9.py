#!/usr/bin/env python3
"""Reproduce the complete 7-smooth-source nine-point upper bound.

Requires Python 3 and a C++17 compiler. The only mathematical prior bounds
are g(5)<=6 and g(6)<=8, as detailed in SMOOTH9_PROOF.md.
"""
from pathlib import Path
from math import prod
import json
import subprocess
import tempfile
import time

ROOT=Path(__file__).resolve().parent


def main():
    started=time.monotonic()
    rows=[]
    for p in [2,3,5,7]:
        denominator=2 if p==7 else 1
        last_bad=None
        for M in range(63,12601):
            T=p*prod(max(M//(j*p)+1,p) for j in [7,8,9])
            if denominator*T<=M*M:
                last_bad=M
        assert last_bad is None or last_bad<12555
        rows.append({'prime':p,'last_bad_sufficient_estimate':last_bad})
        # For every M>=12601, T > M^3/(504*p^2) > M^2/denominator.
        assert 12601*denominator>504*p*p

    with tempfile.TemporaryDirectory(prefix='smooth9_verify_') as temp:
        builds={}
        for name in ['check_smooth9','crt9']:
            binary=Path(temp)/name
            subprocess.run(['g++','-O3','-std=c++17',str(ROOT/(name+'.cpp')),'-o',str(binary)],check=True)
            builds[name]=binary
        finite=subprocess.run([str(builds['check_smooth9']),str(ROOT/'slots9.txt'),str(ROOT/'crt_demands9.txt')],check=True,capture_output=True,text=True)
        finite_result=json.loads(finite.stdout)
        assert finite_result['status']=='PASS_PENDING_CRT_VERIFICATION'
        assert finite_result['actual_seven_cliques']==3413772
        crt_result=subprocess.run([str(builds['crt9']),str(ROOT/'crt_demands9.txt')],check=True,capture_output=True,text=True)
        assert crt_result.stdout.splitlines()[-1].startswith('ALL_PASS rows=318 ')
        (ROOT/'crt9_verified.log').write_text(crt_result.stdout)
    result={
        'status':'PASS',
        'theorem':'For every set of seven distinct 7-smooth integers >=2 and every interval of max(A) consecutive positive integers, a product cover of at most nine points exists.',
        'prior_bounds':['g(5)<=6','g(6)<=8'],
        'analytic_tail_from':12555,
        'analytic_rows':rows,
        'finite':finite_result,
        'CRT':crt_result.stdout.splitlines()[-1],
        'seconds':round(time.monotonic()-started,3),
    }
    (ROOT/'verification_result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
