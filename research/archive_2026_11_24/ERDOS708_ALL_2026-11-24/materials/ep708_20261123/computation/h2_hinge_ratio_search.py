#!/usr/bin/env python3
"""Adversarial H2 search optimizing positive LHS/RHS, avoiding zero-weight traps."""
import argparse,json,time,math
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,eye
from h2_crt_search import primes_to,source_matrix,interval_from_phases,optimize_phases,exact_delta


def hinge_values(U,V,w):
    return float(np.maximum(U@w-2,0).sum()),float(np.maximum(V@w-1,0).sum())


def improve_ratio(U,V,w,rounds=8):
    M,k=U.shape;mat=hstack([csr_matrix(V),-eye(M,format='csr')],format='csr')
    lhs,rhs=hinge_values(U,V,w)
    if lhs<=1e-8:return w,0
    old=lhs/rhs if rhs else float('inf')
    for _ in range(rounds):
        active=U@w>2+1e-9;d=U[active].sum(axis=0)
        res=linprog(np.r_[-d,old*np.ones(M)],A_ub=mat,b_ub=np.ones(M),bounds=[(0,1)]*k+[(0,None)]*M,method='highs')
        if not res.success:raise RuntimeError(res.message)
        ww=res.x[:k];lhs,rhs=hinge_values(U,V,ww);ratio=lhs/rhs if rhs>1e-9 else float('inf')
        if ratio<old-1e-7:raise AssertionError((old,ratio,lhs,rhs))
        w=ww
        if ratio<=old+1e-8:return w,ratio
        old=ratio
    return w,old


def run(seconds,out):
    rng=np.random.default_rng(2708);start=time.monotonic();pr=primes_to(1500);best=0;records=[];trial=0
    while time.monotonic()-start<seconds:
        M=int(rng.choice([60,90,120,180,250,400,700,1200,2000,4000,8000,20000]))
        avail=[p for p in pr if p<=min(M//4,300)]
        k=min(len(avail),int(rng.integers(6,17)))
        if k<6:continue
        mode=trial%4
        if mode==0:ps=avail[:k]
        elif mode==1:ps=sorted(rng.choice(avail,k,replace=False).tolist())
        elif mode==2:ps=sorted(set(avail[:3]+rng.choice(avail[3:],k-3,replace=False).tolist()))
        else:
            near=[p for p in avail if p<=2*M**(1/3)]
            if len(near)<k:near=avail
            ps=sorted(rng.choice(near,k,replace=False).tolist())
        U=source_matrix(M,ps);w=np.ones(k) if trial%3 else rng.integers(2,5,k)/4
        if not np.any(U@w>2+1e-8):trial+=1;continue
        phases=[]
        for p in ps:
            q=p
            while q<=M:q*=p
            s=M//2 if trial%2==0 else int(rng.integers(0,q))
            if 1<=s<=M:s+=q
            phases.append((s,p*q))
        V=interval_from_phases(M,ps,phases);old=-1
        for it in range(10):
            V,phases=optimize_phases(U,V,w,ps,phases,rng,rounds=3)
            w,ratio=improve_ratio(U,V,w)
            if ratio>best+1e-8:
                best=ratio;exact=exact_delta(U,V,w)
                exact_ratio=Fraction(exact['lhs'])/Fraction(exact['rhs']) if Fraction(exact['rhs']) else 'infinity'
                rec={'trial':trial,'iteration':it,'M':M,'primes':ps,'phases':phases,'effective_support':int(np.sum(w>1e-8)),'ratio':str(exact_ratio),**exact}
                records.append(rec);Path(out).write_text(json.dumps({'trials':trial+1,'records':records},indent=2))
                print(json.dumps({'new_ratio':ratio,'M':M,'effective_support':rec['effective_support'],'weights':rec['weights'],'elapsed':round(time.monotonic()-start,1)}),flush=True)
            if ratio>1+1e-7:print('POSITIVE H2 CANDIDATE',flush=True);return
            if ratio<old-1e-7:raise AssertionError(('outer',old,ratio))
            if ratio<=old+1e-8:break
            old=ratio
        trial+=1
    Path(out).write_text(json.dumps({'trials':trial,'seconds':time.monotonic()-start,'best_ratio':best,'records':records,'positive_found':False},indent=2))
    print(json.dumps({'finished':True,'trials':trial,'seconds':round(time.monotonic()-start,1),'best_ratio':best}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--seconds',type=int,default=240);p.add_argument('--out',default=str(Path(__file__).with_name('h2_hinge_ratio_results.json')));a=p.parse_args();run(a.seconds,a.out)
