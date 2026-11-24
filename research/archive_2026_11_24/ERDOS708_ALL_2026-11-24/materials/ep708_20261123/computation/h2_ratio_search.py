#!/usr/bin/env python3
"""Local adversarial search for the raw fractional coefficient.
The reported value L(A,I)/|A| is a *lower bound* on the worst coefficient,
not a verified upper bound. Prime phases are optimized exactly one at a time.
"""
import json, time, math, argparse
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,eye
from h2_crt_search import primes_to,source_matrix,interval_from_phases,optimize_phases,exact_delta

def best_set(U,V,w):
    vals=U@w;R=np.maximum(V@w-1,0).sum()
    order=np.argsort(-vals,kind='stable')
    ratios=(np.cumsum(vals[order])-R)/np.arange(1,len(vals)+1)
    n=int(np.argmax(ratios))+1
    return order[:n],float(ratios[n-1])

def ratio_weights(U,V,A):
    M,k=U.shape;d=U[A].sum(axis=0)
    mat=hstack([csr_matrix(V),-eye(M,format='csr')],format='csr')
    lp=linprog(np.r_[-d,np.ones(M)],A_ub=mat,b_ub=np.ones(M),bounds=[(0,1)]*k+[(0,None)]*M,method='highs')
    if not lp.success:raise RuntimeError(lp.message)
    return lp.x[:k]

def exact_ratio(U,V,w,A):
    fw=[Fraction(float(v)).limit_denominator(100000) for v in w]
    sc=math.lcm(*(z.denominator for z in fw));nums=np.array([int(z*sc) for z in fw],dtype=object)
    X=U[A].astype(object)@nums;Y=V.astype(object)@nums
    value=Fraction(sum(X)-sum(max(int(y)-sc,0) for y in Y),sc*len(A))
    return {'weights':[str(z) for z in fw],'ratio':str(value),'source_count':len(A),'sources':(A+1).tolist(),**exact_delta(U,V,w)}

def run(seconds,out):
    rng=np.random.default_rng(19708);start=time.monotonic();pr=primes_to(1000);trial=0;best=0;records=[]
    while time.monotonic()-start<seconds:
        M=int(rng.choice([40,60,90,120,180,250,400,700,1200,2000,4000]))
        avail=[p for p in pr if p<=min(M//2,150)]
        k=min(len(avail),int(rng.integers(6,21)))
        if k<6:continue
        if trial%3==0:ps=avail[:k]
        elif trial%3==1:ps=sorted(rng.choice(avail,k,replace=False).tolist())
        else:ps=sorted(set(avail[:3]+rng.choice(avail[3:],k-3,replace=False).tolist()))
        U=source_matrix(M,ps)
        w=np.ones(k) if trial%2==0 else rng.integers(1,5,k)/4
        phases=[]
        for p in ps:
            q=p
            while q<=M:q*=p
            s=M//2 if trial%2==0 else int(rng.integers(0,q))
            if 1<=s<=M:s+=q
            phases.append((s,p*q))
        V=interval_from_phases(M,ps,phases)
        old=-1
        for it in range(12):
            V,phases=optimize_phases(U,V,w,ps,phases,rng,rounds=3)
            A,ratio=best_set(U,V,w)
            w=ratio_weights(U,V,A)
            A,ratio=best_set(U,V,w)
            if ratio>best+1e-8:
                best=ratio
                rec={'trial':trial,'iteration':it,'M':M,'primes':ps,'phases':phases,'effective_support':int(np.sum(w>1e-8)),**exact_ratio(U,V,w,A)}
                records.append(rec)
                print(json.dumps({'new_ratio':float(ratio),'record':rec,'elapsed':round(time.monotonic()-start,1)}),flush=True)
                Path(out).write_text(json.dumps({'trials':trial+1,'records':records},indent=2))
            if ratio>2+1e-7:
                print('POSITIVE H2 CANDIDATE',flush=True);return
            if ratio<old-1e-6:raise AssertionError(('nonmonotone',old,ratio))
            if ratio<=old+1e-8:break
            old=ratio
        trial+=1
        if trial%20==0:print(json.dumps({'trials':trial,'elapsed':round(time.monotonic()-start,1),'best_ratio':best}),flush=True)
    Path(out).write_text(json.dumps({'trials':trial,'seconds':time.monotonic()-start,'best_ratio':best,'records':records,'positive_found':False},indent=2))
    print(json.dumps({'finished':True,'trials':trial,'seconds':round(time.monotonic()-start,1),'best_ratio':best}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--seconds',type=int,default=240);p.add_argument('--out',default=str(Path(__file__).with_name('h2_ratio_search_results.json')));a=p.parse_args();run(a.seconds,a.out)
