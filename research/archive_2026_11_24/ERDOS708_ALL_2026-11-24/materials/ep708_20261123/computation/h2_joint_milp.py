#!/usr/bin/env python3
"""Finite global MILP for H2, optimizing both weights and CRT phases.
This is a search implementation, not an exact-arithmetic branch certificate.
A negative minimization objective is checked by exact rational arithmetic.
"""
import math,json,time,argparse
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import coo_matrix
from h2_crt_search import source_matrix,exact_delta
from h2_global_phase_milp import patterns


def run(M,ps,seconds):
    start=time.monotonic();k=len(ps);pat=[patterns(M,p) for p in ps]
    starts=np.cumsum([0]+[len(z) for z in pat]);ny=int(starts[-1])
    U=source_matrix(M,ps);active=np.flatnonzero(U.sum(axis=1)>2);na=len(active)
    iw=0;iy=k;iu=iy+ny;iz=iu+ny;it=iz+na;ih=it+na;nv=ih+M
    rr=[];cc=[];vv=[];low=[];high=[]
    def row(vals,lo,hi):
        r=len(low)
        for c,v in vals:
            if v:rr.append(r);cc.append(c);vv.append(v)
        low.append(lo);high.append(hi)
    for c in range(k):
        row([(iy+j,1) for j in range(starts[c],starts[c+1])],1,1)
        for j in range(starts[c],starts[c+1]):
            row([(iu+j,1),(iw+c,-1)],-np.inf,0)
            row([(iu+j,1),(iy+j,-1)],-np.inf,0)
            row([(iw+c,1),(iy+j,1),(iu+j,-1)],-np.inf,1)
    for z,a in enumerate(active):
        demand=[(iw+c,-int(U[a,c])) for c in range(k) if U[a,c]]
        row([(it+z,1)]+demand,-2,np.inf)
        row([(it+z,1),(iz+z,2)]+demand,-np.inf,0)
        row([(it+z,1),(iz+z,-int(U[a].sum()-2))],-np.inf,0)
    loads=[[] for _ in range(M)]
    for c,ls in enumerate(pat):
        for a,(_,_,v) in enumerate(ls):
            index=iu+int(starts[c])+a
            for j in np.flatnonzero(v):loads[j].append((index,int(v[j])))
    for j in range(M):row(loads[j]+[(ih+j,-1)],-np.inf,1)
    mat=coo_matrix((vv,(rr,cc)),shape=(len(low),nv)).tocsc()
    upper=np.ones(nv);upper[it:it+na]=U[active].sum(axis=1)-2;upper[ih:]=np.inf
    integ=np.zeros(nv);integ[iy:iy+ny]=1;integ[iz:iz+na]=1
    obj=np.zeros(nv);obj[it:it+na]=-1;obj[ih:]=1
    result=milp(obj,integrality=integ,bounds=Bounds(np.zeros(nv),upper),constraints=LinearConstraint(mat,np.array(low),np.array(high)),options={'time_limit':seconds,'mip_rel_gap':0})
    rec={'M':M,'primes':ps,'source_hinges':na,'binary_phase_variables':ny,'seconds':time.monotonic()-start,'status':int(result.status),'message':result.message,'dual_bound':float(getattr(result,'mip_dual_bound',float('nan')))}
    if result.x is not None:
        chosen=[int(np.argmax(result.x[iy+starts[c]:iy+starts[c+1]])) for c in range(k)]
        phases=[pat[c][a][:2] for c,a in enumerate(chosen)];V=np.stack([pat[c][a][2] for c,a in enumerate(chosen)],axis=1)
        rec.update({'phases':phases,'incumbent_float':float(result.fun),**exact_delta(U,V,result.x[:k])})
    return rec

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--seconds',type=int,default=30);a=p.parse_args()
    records=[]
    for M,ps in [(20,[2,3,5,7,11,13]),(40,[2,3,5,7,11,13]),(60,[2,3,5,7,11,13,17,19])]:
        r=run(M,ps,a.seconds);records.append(r);print(json.dumps(r),flush=True)
        Path(__file__).with_name('h2_joint_milp_results.json').write_text(json.dumps(records,indent=2))
