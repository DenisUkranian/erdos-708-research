from pathlib import Path
import subprocess, tempfile
root=Path(__file__).resolve().parent
with tempfile.TemporaryDirectory() as tmp:
    exe=Path(tmp)/'verify'
    subprocess.run(['g++','-O3','-std=c++17',str(root/'verify.cpp'),'-o',str(exe)],check=True)
    out=subprocess.run([str(exe)],capture_output=True,text=True,check=True)
    assert out.stdout == (root/'frontier.txt').read_text()
    assert out.stderr.strip() == 'ROWS EXCLUDED=23468 REMAIN=529 MAX=4361 PAIRS FAILED=26044729 ALL PAIRS=26897751 PASSED=569957 TRIPLE=283065'
    print(out.stderr.strip())
    print('PASS: high-high frontier only; not a proof of g(9)=12.')
