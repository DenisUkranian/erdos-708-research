"""Portable complete replay of the three-large-prime g(7)<=9 component."""
from pathlib import Path
import hashlib,json,math,subprocess,sys,tempfile
HERE=Path(__file__).resolve().parent
FINITE=HERE.parent/'finite'

def check_slots(rows,expected):
    keys={tuple(r['A']) for r in rows}
    assert len(keys)==len(rows)==len(expected) and keys==expected
    for row in rows:
        A=row['A'];M=max(A);hs=row['slots'];H=1
        assert row['M']==M and len(A)==len(set(A))==7 and len(hs)<=9
        for j,h in enumerate(hs,1):
            assert isinstance(h,int) and 1<=h<=M
            assert math.gcd(H,h)<=M//j
            H*=h
        assert H%math.prod(A)==0

with tempfile.TemporaryDirectory(prefix='erdos708_three_') as td:
    temp=Path(td)
    (temp/'g7_exact'/'three').mkdir(parents=True)
    (temp/'g7_exact'/'finite').mkdir(parents=True)
    for family,script,count in [('low_support3','enumerate_low_support3.py',162),('high_c2','enumerate_high_c2.py',283)]:
        subprocess.run([sys.executable,str(HERE/script)],cwd=temp,check=True,stdout=subprocess.PIPE,text=True)
        expected_rows=json.loads((temp/'g7_exact'/'three'/(family+'_candidates.json')).read_text())
        expected={tuple(r['A']) for r in expected_rows}
        assert len(expected)==len(expected_rows)==count
        rows=json.loads((HERE/(family+'_slots.json')).read_text())
        check_slots(rows,expected)
        print('PASS',family,count,'complete source sets and certificates',flush=True)
    src=FINITE/'three_large_envelope.cpp'
    exe=temp/'three_envelope'
    subprocess.run(['g++','-std=c++17','-O2',str(src),'-o',str(exe)],check=True)
    result=subprocess.run([str(exe),'24696','1000000'],cwd=temp,check=True,stdout=subprocess.PIPE,text=True)
    summary=json.loads(result.stdout)
    for key,value in [('triples',6294),('maxima',656193),('classes',850366),('passed',850364),('unresolved',2)]:
        assert summary[key]==value,(key,summary)
    residual=[tuple(map(int,line.split())) for line in (temp/'g7_exact'/'finite'/'three_large_unresolved.tsv').read_text().splitlines()]
    expected_residual=[(11,13,23,M,0,0,0,2,0,0,0,3,1,1) for M in (1012,1035)]
    assert sorted(residual)==expected_residual
    print('PASS complete finite envelope:',summary,flush=True)
    print('SHA256 three_large_envelope.cpp',hashlib.sha256(src.read_bytes()).hexdigest(),flush=True)
subprocess.run([sys.executable,str(HERE/'verify_three_residual_independent.py')],check=True)
print('PASS: complete three-large-prime verification chain',flush=True)
