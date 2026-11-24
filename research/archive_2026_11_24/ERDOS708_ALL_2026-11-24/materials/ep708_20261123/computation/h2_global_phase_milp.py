#!/usr/bin/env python3
"""Global finite CRT-phase MILP at fixed rational weights.
Each prime admits <=2M relevant valuation patterns for minimization.
An exact rational primal evaluation is included. Solver lower bounds are
floating-point numerical bounds, not independently formal certificates.
"""
import argparse,json,math,time
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import csc_matrix,hstack,vstack,eye
from h2_crt_search import source_matrix,phase_vector


def patterns(M,p):
    d=p
    while d*p<=M:d*=p
    Q=d*p;mod=Q*p
    result=[]
    for r in range(d):
        inds=list(range(r if r>0 else d,M+1,d))
        for j in inds:
            s=j+Q
            result.append((s,mod,phase_vector(M,p,s,mod)))
        if len(inds)<p:
            occupied={(j-r)//d for j in inds}
            digit=next(a for a in range(p) if a not in occupied)
            s=r+digit*d
            result.append((s,mod,phase_vector(M,p,s,mod)))
    assert len(result)<=2*M
    return result


def run(M,ps,weights,seconds):
    start=time.monotonic();k=len(ps);allpat=[patterns(M,p) for p in ps]
    starts=np.cumsum([0]+[len(a) for a in allpat]);ny=int(starts[-1])
    mats=[];one=np.zeros((k,ny))
    for c,pat in enumerate(allpat):
        mats.append(np.stack([v for _,_,v in pat],axis=1)*float(weights[c]))
        one[c,starts[c]:starts[c+1]]=1
    load=csc_matrix(np.concatenate(mats,axis=1))
    mat=vstack([hstack([csc_matrix(one),csc_matrix((k,M))]),hstack([load,-eye(M)])],format='csc')
    constraints=LinearConstraint(mat,np.r_[np.ones(k),np.full(M,-np.inf)],np.r_[np.ones(k),np.ones(M)])
    result=milp(np.r_[np.zeros(ny),np.ones(M)],integrality=np.r_[np.ones(ny),np.zeros(M)],bounds=Bounds(np.zeros(ny+M),np.r_[np.ones(ny),np.full(M,np.inf)]),constraints=constraints,options={'time_limit':seconds,'mip_rel_gap':0})
    record={'M':M,'primes':ps,'weights':[str(a) for a in weights],'patterns_per_prime':[len(a) for a in allpat],'seconds':time.monotonic()-start,'status':int(result.status),'message':result.message,'dual_bound':float(getattr(result,'mip_dual_bound',float('nan')))}
    if result.x is not None:
        chosen=[int(np.argmax(result.x[starts[c]:starts[c+1]])) for c in range(k)]
        phases=[allpat[c][a][:2] for c,a in enumerate(chosen)]
        V=np.stack([allpat[c][a][2] for c,a in enumerate(chosen)],axis=1)
        U=source_matrix(M,ps)
        sc=math.lcm(*(a.denominator for a in weights));ww=np.array([int(a*sc) for a in weights],dtype=np.int64)
        lhs=int(np.maximum(U@ww-2*sc,0).sum());rhs=int(np.maximum(V@ww-sc,0).sum())
        record.update({'phases':phases,'lhs':str(Fraction(lhs,sc)),'rhs':str(Fraction(rhs,sc)),'delta':str(Fraction(lhs-rhs,sc)),'incumbent_float':float(result.fun)})
    return record

if __name__=='__main__':
    records=[]
    cases=[(40,[2,3,5,7,11,13],[1,1,1,1,1,1]),(60,[2,3,5,7,11,13],[Fraction(1,2),Fraction(1,2),1,1,1,1]),(90,[2,3,5,7,11,13],[1,1,1,1,1,1]),(120,[2,3,5,7,11,13,17,19],[Fraction(1,2)]*3+[1]*5),(180,[2,3,5,7,11,13],[Fraction(1,2),Fraction(2,3),Fraction(3,4),1,1,1])]
    for M,ps,w in cases:
        r=run(M,ps,[Fraction(a) for a in w],15);records.append(r);print(json.dumps(r),flush=True)
        Path(__file__).with_name('h2_global_phase_results.json').write_text(json.dumps(records,indent=2))
