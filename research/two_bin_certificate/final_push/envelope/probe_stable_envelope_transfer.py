"""Heuristic real-CRT phase search for C_source <= K_M_target; never computes g(n)."""
from pathlib import Path
import sys,random,json
import numpy as np
from math import prod
base=Path(__file__).resolve().parents[2]
dependency=base/'ep708_new_attempt_20261124/envelope'
if not dependency.is_dir():
    dependency=base/'new_attempt/envelope'
sys.path.insert(0,str(dependency))
from check_residual_capacity import envelope,factor,divisor_vectors

rng=random.Random(7082411)

def prepare(M,weights):
    ps=sorted(weights)
    caps=[]
    for p in ps:
        q=p
        while q<=M:q*=p
        caps.append(q)
    roots=[]
    source=0.
    cache={1:0.}
    for a in range(2,M+1):
        fs=factor(a)
        h=prod(p**e for p,e in fs.items() if p in weights)
        if h not in cache:cache[h]=envelope(h,weights)[0]
        source+=cache[h]
        if h!=a:continue
        es=tuple(fs.get(p,0) for p in ps)
        L=sum(weights[p]*e for p,e in zip(ps,es))
        if L<=1+1e-12:continue
        price=min(min(weights[p] for p,e in zip(ps,es) if e),(L-1)/sum(es))
        rows=[i for i,p in enumerate(ps) if es[i] and a*a<=M*p]
        if rows:roots.append((es,rows,price))
    return ps,caps,roots,source,cache

def evaluate(M,ps,caps,roots,phases):
    vals=np.zeros((len(ps),M),dtype=np.int16)
    for i,p in enumerate(ps):
        q=p
        while q<=caps[i]:
            start=(-phases[i])%q
            if start==0:start=q
            vals[i,start-1::q]+=1
            q*=p
    maxima=np.zeros((len(ps),M))
    for es,rows,price in roots:
        mask=np.ones(M,dtype=bool)
        for i,e in enumerate(es):
            if e:mask&=vals[i]>=e
        for i in rows:maxima[i,mask]=np.maximum(maxima[i,mask],price)
    return float(np.sum(vals*maxima))

def main():
    out=Path(__file__).with_name('probe_stable_envelope_results.json')
    results=[]
    catalog=[]
    for M in [30,60,100,200,400]:
        supports=[[2,3],[2,5],[2,3,5],[2,3,5,7],[3,5,7],[5,7,11]]
        for ps in supports:
            catalog.append((M,{p:1. for p in ps}))
            for _ in range(2):
                catalog.append((M,{p:rng.choice([.1,.2,.3,.4,.5,.6,.8,1.]) for p in ps}))
    for case,(M,w) in enumerate(catalog,1):
        ps,caps,roots,source,cache=prepare(M,w)
        if source<1e-9:continue
        phase=[0]*len(ps)
        best=evaluate(M,ps,caps,roots,phase)
        bestph=phase[:]
        for _ in range(50):
            ph=[rng.randrange(c) for c in caps]
            val=evaluate(M,ps,caps,roots,ph)
            if val<best:best,bestph=val,ph[:]
        for _ in range(200):
            ph=bestph[:]
            i=rng.randrange(len(ps));ph[i]=rng.randrange(caps[i])
            val=evaluate(M,ps,caps,roots,ph)
            if val<best-1e-10:best,bestph=val,ph
        row={'M':M,'weights':w,'source_envelope':source,'target_kernel':best,
             'margin':best-source,'phases':bestph,'caps':caps,'source_distinct_parts':len(cache)}
        results.append(row)
        print(json.dumps({'case':case,**row}),flush=True)
        out.write_text(json.dumps(results,indent=2))
        if best<source-1e-7:
            print('CANDIDATE COUNTEREXAMPLE: needs exact rational LP/CRT audit.',flush=True)
            break
    print('Done. Finite local searches do not prove uniform transfer.',flush=True)

if __name__=='__main__':main()
