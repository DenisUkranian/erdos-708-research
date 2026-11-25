#!/usr/bin/env python3
"""Independently recheck the full 162-case integer certificates.
A success depends only on the supplied JSON and the stated small-case
upper bounds f(k) for k<=8, not on the search algorithm.
"""
import json,itertools,math,sys
from pathlib import Path
F={1:1,2:2,3:4,4:5,5:6,6:8,7:9,8:11}
ROWS={5:121,6:144,7:240,8:360}
file=sys.argv[1] if len(sys.argv)>1 else str(Path(__file__).resolve().parent / 'prime_band_certificates.json')
with open(file) as f:all_entries=json.load(f)
assert [entry['k'] for entry in all_entries]==list(ROWS)
validated=0
for entry in all_entries:
 k=entry['k'];M=entry['M_min'];assert M==ROWS[k]
 expected={tuple(x) for r in range(3,k) for x in itertools.combinations(range(1,k),r)}
 received=set()
 for case in entry['cases']:
  us=tuple(case['u']);assert us in expected and us not in received
  received.add(us);d=len(us);f=F[9-d];s=12-f-d
  anchor=case['anchor'];assert anchor in us
  bins=case['bins'];assert len(bins)==s
  supplied=[v for bin in bins for v in bin]
  other=list(us);other.remove(anchor)
  assert sorted(supplied)==sorted(other)
  for j,b in enumerate(bins,start=1):
   assert (f+d+j)*math.prod(b)<=M
  validated+=1
 assert expected==received
 print('PASS','k',k,'M_min',M,'cases',len(received))
print('ALL PASS',validated,'cases')
