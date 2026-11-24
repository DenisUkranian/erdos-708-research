#!/usr/bin/env python3
"""Six-prime H2 search in the bad-density region, weights additionally >=1/10.
The positive lower weight bound is a search restriction, not a proved reduction.
Delta2<=M-sum_{a<=M}min(X(a),2); only the region with positive bound matters.
"""
import json,time,math,argparse
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
from h2_crt_search import primes_to,source_matrix,interval_from_phases,optimize_phases,exact_delta
from h2_hinge_ratio_search import hinge_values


def improve(U,V,w,rounds=8):
    M,k=U.shape;base=hstack([csr_matrix(V),-eye(M,format='csr')],format='csr')
    lhs,rhs=hinge_values(U,V,w)
    if lhs<=1e-8:return w,0
    old=lhs/rhs
    for _ in range(rounds):
        active=U@w>2+1e-9;n=int(active.sum());d=U[active].sum(axis=0);outside=U[~active].sum(axis=0)
        # min(X,2) is the minimum of these affine functions over active sets.
        # Enforcing this one affine upper bound is a sufficient bad-region restriction.
        mat=vstack([base,csr_matrix(np.r_[outside,np.zeros(M)][None,:])],format='csr')
        b=np.r_[np.ones(M),M-2*n-1e-5]
        res=linprog(np.r_[-d,old*np.ones(M)],A_ub=mat,b_ub=b,bounds=[(.1,1)]*k+[(0,None)]*M,method='highs')
        if not res.success:
            if res.status==2:return w,old
            raise RuntimeError(res.message)
        ww=res.x[:k];lhs,rhs=hinge_values(U,V,ww);ratio=lhs/rhs if rhs>1e-9 else float('inf')
        assert np.minimum(U@ww,2).sum()<=M+1e-6
        if ratio<old-1e-6:return w,old
        w=ww
        if ratio<=old+1e-8:return w,ratio
        old=ratio
    return w,old


def run(seconds,out):
    rng=np.random.default_rng(1708);start=time.monotonic();pr=primes_to(2000);best=0;records=[];trial=0;valid=0
    while time.monotonic()-start<seconds:
        M=int(rng.choice([120,180,250,400,700,1200,2000,4000,8000,20000]))
        center=M**(1/3)*float(rng.choice([.5,1,1.5,2,3]))
        avail=[p for p in pr if max(5,center/2)<=p<=min(M//6,center*2.5)]
        k=min(len(avail),4)
        if k<4:trial+=1;continue
        ps=sorted([2,3]+rng.choice(avail,k,replace=False).tolist());k=len(ps)
        U=source_matrix(M,ps);w=np.ones(k);w[:2]=rng.uniform(.1,.9,2)
        if trial%3==0:w[2:]=rng.integers(2,5,k-2)/4
        density=np.minimum(U@w,2).sum()
        while density>M*.98:
            w=np.maximum(.1,w*.95);density=np.minimum(U@w,2).sum()
        if not np.any(U@w>2+1e-8):trial+=1;continue
        valid+=1;phases=[]
        for p in ps:
            q=p
            while q<=M:q*=p
            s=M//2 if trial%2==0 else int(rng.integers(0,q))
            if 1<=s<=M:s+=q
            phases.append((s,p*q))
        V=interval_from_phases(M,ps,phases);old=-1
        for it in range(8):
            V,phases=optimize_phases(U,V,w,ps,phases,rng,rounds=3)
            w,ratio=improve(U,V,w)
            if ratio>best+1e-8:
                best=ratio;e=exact_delta(U,V,w)
                rr=Fraction(e['lhs'])/Fraction(e['rhs']) if Fraction(e['rhs']) else 'infinity'
                rec={'trial':trial,'M':M,'primes':ps,'phases':phases,'effective_support':int(np.sum(w>1e-8)),'ratio':str(rr),'capped_source_mass':float(np.minimum(U@w,2).sum()),**e}
                records.append(rec);Path(out).write_text(json.dumps({'trials':trial+1,'valid_starts':valid,'records':records},indent=2))
                print(json.dumps({'new_ratio':ratio,'M':M,'effective_support':rec['effective_support'],'weights':rec['weights'],'elapsed':round(time.monotonic()-start,1)}),flush=True)
            if ratio>1+1e-7:print('POSITIVE H2 CANDIDATE',flush=True);return
            if ratio<=old+1e-8:break
            old=ratio
        trial+=1
    Path(out).write_text(json.dumps({'trials':trial,'valid_starts':valid,'seconds':time.monotonic()-start,'best_ratio':best,'records':records,'positive_found':False},indent=2))
    print(json.dumps({'finished':True,'trials':trial,'valid_starts':valid,'seconds':round(time.monotonic()-start,1),'best_ratio':best}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--seconds',type=int,default=120);p.add_argument('--out',default=str(Path(__file__).with_name('h2_six_prime_results.json')));a=p.parse_args();run(a.seconds,a.out)
