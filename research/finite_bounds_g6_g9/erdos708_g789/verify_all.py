#!/usr/bin/env python3
"""Reproduce the exact-arithmetic proof checks; Python 3 and a C++17 compiler."""
from pathlib import Path
import argparse, json, shutil, subprocess, sys, tempfile

ROOT = Path(__file__).resolve().parent
CONFIG = {6:(8,9360,3),7:(10,19170,4),8:(12,12320,4),9:(14,24206,5)}
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--cases',type=int,nargs='+',choices=CONFIG,default=list(CONFIG))
args=parser.parse_args()

subprocess.run([sys.executable,str(ROOT/'verify/analytic_cutoffs.py')],check=True)
subprocess.run([sys.executable,str(ROOT/'verify/verify_clean_witnesses.py')],check=True)
compiler=shutil.which('g++') or shutil.which('clang++')
if not compiler:raise SystemExit('A C++17 compiler (g++ or clang++) is required.')
with tempfile.TemporaryDirectory(prefix='erdos708-check-') as d:
    binary=Path(d)/'check_bounds'
    subprocess.run([compiler,'-std=c++17','-O3',str(ROOT/'verify/check_smooth_exhaustive.cpp'),'-o',str(binary)],check=True)
    for n in args.cases:
        B,top,dim=CONFIG[n]
        print(f'Checking the universal bound g({n}) <= {B}...',flush=True)
        subprocess.run([str(binary),str(n),str(B),str(top),str(dim),str(ROOT/f'certificates/slots{n}.txt')],check=True)
print('All requested checks passed. The proof uses the external theorem g(5) <= 6.')
