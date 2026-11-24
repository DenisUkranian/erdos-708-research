#!/usr/bin/env python3
"""Replay every computational component of the proof g(7)=9.

Run `python3 g7_exact/verify_all.py` from the unpacked proof bundle.
Python 3 and a C++17 compiler are required. Do not disable assertions.
The mathematical reduction lemmas and external small-n inputs are stated
in PROOF.md; this script checks all finite certificates and analytic
cutoff arithmetic in their prescribed order.
"""
from pathlib import Path
import importlib.util,json,subprocess,sys,time
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent

def main():
    start=time.monotonic()
    spec=importlib.util.spec_from_file_location('analytic_cutoffs',ROOT/'g7_theory'/'analytic_cutoffs.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    tail=module.threshold(6,8,[2,3,5])
    assert tail['proved_packing_for_all_M_from']==9360
    assert 504*7**2==24696
    assert 504*6**7<24697**2
    assert 9*216<24697
    print('PASS analytic cutoff arithmetic',flush=True)
    scripts=[
        ROOT/'g7_theory'/'check_g6_independent.py',
        HERE/'verify_lower9_simple.py',
        HERE/'smooth'/'verify_smooth9.py',
        HERE/'one'/'verify_one.py',
        HERE/'two'/'verify_two.py',
        HERE/'three'/'verify_all_three.py',
    ]
    for script in scripts:
        print('\nVERIFY',script.relative_to(ROOT),flush=True)
        subprocess.run([sys.executable,str(script)],cwd=ROOT,check=True)
    result={
        'status':'PASS',
        'theorem':'g(7)=9 in the at-most covering convention',
        'mathematical_inputs':['g(2)<=2','g(3)<=4','g(4)<=5','g(5)<=6'],
        'external_finite_source':'https://hexagonmath.org/pdf/2611.00694v1',
        'g6_upper_bound':'independently replayed in this bundle',
        'analytic_general_cutoff':24697,
        'finite_maximum':24696,
        'all_computational_components_passed':True,
        'scope':'Computer-assisted proof with exact integer checks; not a Lean formalization of the new result.',
        'seconds':round(time.monotonic()-start,3),
    }
    (HERE/'VERIFICATION_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print('\n'+json.dumps(result,indent=2),flush=True)

if __name__=='__main__':main()
