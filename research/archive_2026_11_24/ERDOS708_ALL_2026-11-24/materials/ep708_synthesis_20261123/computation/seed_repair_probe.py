#!/usr/bin/env python3
"""Explore the stronger n-position seed / n-unit repair conjecture.

This is a probe of an auxiliary lemma, not a solution of Erdos 708.
Every saved phase vector is realizable by CRT. A positive reported gap is
only a numerical candidate until independently certified.
"""
import json, math, time, sys
from pathlib import Path
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import csr_matrix, hstack, vstack, eye

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'ep708_20261123' / 'computation'))
from h2_crt_search import primes_to, source_matrix, phase_vector

def run(seconds=120):
    rng=np.random.default_rng(7082301); started=time.monotonic(); rows=[]
    best=None; attempts=0
    while time.monotonic()-started<seconds:
        M=int(rng.choice([60,90,120,180,250,400,600]))
        n=int(rng.choice([max(3,M//12), max(3,M//8), max(3,M//5),max(3,M//3)]))
        K=2*n-1; ps=primes_to(min(M//4,K-1)); U=source_matrix(M,ps)
        complete=np.ones(M,dtype=np.int64)
        for j,p in enumerate(ps): complete*=np.power(p,U[:,j],dtype=np.int64)
        largest=np.zeros(M,dtype=np.int64)
        for j,p in enumerate(ps): largest[U[:,j]>0]=p
        good=(complete==np.arange(1,M+1)) & (U.sum(axis=1)>=3)
        good &= np.arange(1,M+1)*K > M*np.maximum(largest,1)
        pool=np.flatnonzero(good)
        if len(pool)<n: continue
        aa=np.sort(rng.choice(pool,n,replace=False)); demand=U[aa].sum(axis=0)
        keep=demand>0; ps=[p for p,k in zip(ps,keep) if k]; demand=demand[keep]
        phases=[]; cols=[]
        for p in ps:
            Q=p
            while Q<=M: Q*=p
            s=int(rng.integers(0,Q))
            if 1<=s<=M:s+=Q
            mod=p*Q; phases.append([s,mod]); cols.append(phase_vector(M,p,s,mod))
        V=np.stack(cols,axis=1); k=len(ps)
        mat=vstack([hstack([csr_matrix(np.ones((1,M))),csr_matrix((1,k))]),
                    hstack([-csr_matrix(V.T),eye(k,format='csr')])],format='csr')
        con=LinearConstraint(mat, np.full(k+1,-np.inf),np.r_[n,np.zeros(k)])
        res=milp(np.r_[np.zeros(M),-np.ones(k)],integrality=np.r_[np.ones(M),np.zeros(k)],
            bounds=Bounds(np.zeros(M+k),np.r_[np.ones(M),demand]),constraints=con,
            options={'time_limit':5,'mip_rel_gap':0})
        attempts+=1
        if res.x is None:continue
        selected=np.flatnonzero(res.x[:M]>.5)
        covered=np.minimum(demand,V[selected].sum(axis=0)); deficit=int((demand-covered).sum())
        row={'M':M,'n':n,'sources':(aa+1).tolist(),'primes':ps,'phases':phases,
             'selected_indices':(selected+1).tolist(),'deficit':deficit,
             'seed_cost':len(selected),'candidate_gap':deficit-n,
             'milp_status':int(res.status),'numerical_dual_bound':float(res.mip_dual_bound),
             'not_a_proof_of_nonexistence':True}
        if best is None or row['candidate_gap']>best['candidate_gap']:
            best=row;rows.append(row);print(json.dumps({'attempt':attempts,'M':M,'n':n,'gap':row['candidate_gap'],'status':int(res.status)}),flush=True)
        if row['candidate_gap']>0 and res.status==0:break
    out={'scope':'Auxiliary seed lemma probe; not an Erdos708 counterexample search certificate',
         'attempts':attempts,'elapsed_seconds':time.monotonic()-started,'records':rows,'best':best}
    Path(__file__).with_name('seed_repair_probe_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'attempts':attempts,'best_gap':None if best is None else best['candidate_gap']}),flush=True)

if __name__=='__main__':run(float(sys.argv[1]) if len(sys.argv)>1 else 120)
