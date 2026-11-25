#!/usr/bin/env python3
"""Build small exact source-combinatorial certificates for the four prime cutoffs."""
import json
from pathlib import Path
from itertools import combinations
from math import prod
F={1:1,2:2,3:4,4:5,5:6,6:8,7:9,8:11}
ROWS=((5,121),(6,144),(7,240),(8,360))

def certificate(M,us):
 d=len(us);f=F[9-d];s=12-f-d
 slots=range(f+d+1,13)
 for i,anchor in enumerate(us):
  rem=[u for j,u in enumerate(us) if j!=i]
  bins=[[] for _ in slots]
  def go(j):
   if j==len(rem):
    return {'u':list(us),'anchor':anchor,'bins':[list(b) for b in bins]}
   for k,t in enumerate(slots):
    if t*prod(bins[k])*rem[j]<=M:
     bins[k].append(rem[j]);ans=go(j+1)
     if ans is not None:return ans
     bins[k].pop()
   return None
  ans=go(0)
  if ans is not None:return ans
 raise AssertionError(f'No proof for {M=} {us=}')

entries=[]
for k,M in ROWS:
 checks=[certificate(M,us) for d in range(3,k) for us in combinations(range(1,k),d)]
 entries.append({'k':k,'M_min':M,'cases':checks})
with open(Path(__file__).resolve().parent / 'prime_band_certificates.json','w') as f:
 json.dump(entries,f,indent=1)
print([(e['k'],len(e['cases'])) for e in entries])
