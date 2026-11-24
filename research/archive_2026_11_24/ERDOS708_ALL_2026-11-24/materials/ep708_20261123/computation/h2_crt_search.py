#!/usr/bin/env python3
"""Adversarial H2 search: exact optimal CRT phase in each prime coordinate.

Fixed rational/float weights; full high-valuation phases, not a squarefree
relaxation. Each emitted phase is a congruence x mod p**(E+2), E=floor(log_p M).
No assertion of a global maximum or of H2 follows from local optimization.
"""
import argparse, json, math, time
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.optimize import linprog


def primes_to(n):
    a=np.ones(n+1,dtype=bool);a[:2]=False
    for p in range(2,math.isqrt(n)+1):
        if a[p]:a[p*p::p]=False
    return np.flatnonzero(a).tolist()


def source_matrix(M,ps):
    v=np.zeros((M,len(ps)),dtype=np.int16)
    for c,p in enumerate(ps):
        q=p
        while q<=M:
            v[q-1::q,c]+=1;q*=p
    return v


def phase_vector(M,p,s,mod):
    # s is the residue of interval index j at which a high multiple lies.
    j=np.arange(1,M+1,dtype=np.int64)
    v=np.zeros(M,dtype=np.int16);q=p
    while q<=mod:
        v[(j-s)%q==0]+=1;q*=p
    return v


def best_prime_phase(other,w,p):
    """Exact coordinate minimum for sum_j (other[j]+w*vp(x+j)-1)_+.

    Layer increments, then min-plus dynamic programming on compatible
    p-adic residues. Levels above E+1 can always be avoided; those at E+1
    cannot simply be discarded when all p children contain positions.
    """
    M=len(other);j=np.arange(1,M+1,dtype=np.int64)
    powers=[];q=p
    while q<=M:powers.append(q);q*=p
    E=len(powers)
    assert E>=1
    d=powers[-1]
    # Minimum next digit. Empty children have zero cost; when all p occur,
    # one position must receive valuation E+1, so choose its least increment.
    inc=np.maximum(other+w*(E+1)-1,0)-np.maximum(other+w*E-1,0)
    cnt=np.bincount(j%d,minlength=d)
    least=np.full(d,np.inf);np.minimum.at(least,j%d,inc)
    cost=np.where(cnt==p,least,0.0)
    choices={}
    for h in range(E,0,-1):
        d=powers[h-1]
        inc=np.maximum(other+w*h-1,0)-np.maximum(other+w*(h-1)-1,0)
        cost=cost+np.bincount(j%d,weights=inc,minlength=d)
        if h>1:
            parent=powers[h-2]
            resh=cost.reshape((p,parent))
            choices[h]=np.argmin(resh,axis=0)
            cost=resh.min(axis=0)
    s=int(np.argmin(cost))
    for h in range(2,E+1):s+=int(choices[h][s])*powers[h-2]
    d=powers[-1]
    inds=j[j%d==s]
    if len(inds)<p:
        occupied={int((a-s)//d) for a in inds}
        digit=next(a for a in range(p) if a not in occupied)
    else:
        # All p digits occur, each at one position.
        inc=np.maximum(other[inds-1]+w*(E+1)-1,0)-np.maximum(other[inds-1]+w*E-1,0)
        digit=int((inds[int(np.argmin(inc))]-s)//d)
    s+=digit*d
    Q=p*d
    # A unique level E+1 position can be kept from level E+2.
    if 1<=s<=M:s+=Q
    modulus=p*Q
    v=phase_vector(M,p,s,modulus)
    actual=float(np.maximum(other+w*v-1,0).sum())
    expected=float(np.maximum(other-1,0).sum()+cost.min())
    if abs(actual-expected)>1e-7*(1+abs(expected)):
        raise AssertionError((M,p,w,s,actual,expected))
    return v,int(s),int(modulus),actual


def interval_from_phases(M,ps,phases):
    return np.stack([phase_vector(M,p,s,mod) for p,(s,mod) in zip(ps,phases)],axis=1)


def objective(U,V,w,c=2):
    return float(np.maximum(U@w-c,0).sum()-np.maximum(V@w-1,0).sum())


def optimize_phases(U,V,w,ps,phases,rng,rounds=4):
    current=V@w
    for _ in range(rounds):
        previous=float(np.maximum(current-1,0).sum())
        for k in rng.permutation(len(ps)):
            other=current-w[k]*V[:,k]
            v,s,mod,_=best_prime_phase(other,w[k],ps[k])
            V[:,k]=v;phases[k]=(s,mod);current=other+w[k]*v
        now=float(np.maximum(current-1,0).sum())
        if previous-now<1e-8:break
    return V,phases


def improve_weights(U,V,w,c=2,max_rounds=5):
    # Exact LP on the current positive source set; iterations are local DC.
    from scipy.sparse import csr_matrix,hstack,eye
    M,k=U.shape
    mat=hstack([csr_matrix(V),-eye(M,format='csr')],format='csr')
    old=objective(U,V,w,c)
    for _ in range(max_rounds):
        active=U@w>c+1e-9
        demand=U[active].sum(axis=0)
        cost=np.r_[-demand,np.ones(M)]
        lp=linprog(cost,A_ub=mat,b_ub=np.ones(M),bounds=[(0,1)]*k+[(0,None)]*M,method='highs')
        if not lp.success:raise RuntimeError(lp.message)
        ww=lp.x[:k];new=objective(U,V,ww,c)
        if new<old-1e-7:raise AssertionError(('nonmonotone',old,new))
        if new<=old+1e-8:break
        w=ww;old=new
    return w,old


def exact_delta(U,V,w,c=2):
    fw=[Fraction(float(v)).limit_denominator(100000) for v in w]
    scale=math.lcm(*(v.denominator for v in fw));nums=np.array([int(v*scale) for v in fw],dtype=object)
    lhs=sum(max(int(a)-c*scale,0) for a in U.astype(object)@nums)
    rhs=sum(max(int(a)-scale,0) for a in V.astype(object)@nums)
    return {'weights':[str(a) for a in fw],'lhs':str(Fraction(lhs,scale)),'rhs':str(Fraction(rhs,scale)),'delta':str(Fraction(lhs-rhs,scale))}


def test_coordinate():
    rng=np.random.default_rng(708)
    cases=0
    for M in range(2,16):
      for p in primes_to(M):
        other=rng.integers(0,8,M)/4;w=float(rng.integers(1,5))/4
        v,s,mod,cost=best_prime_phase(other,w,p)
        brute=min(float(np.maximum(other+w*phase_vector(M,p,a,mod)-1,0).sum()) for a in range(mod))
        assert abs(cost-brute)<1e-8,(M,p,cost,brute)
        cases+=1
    print(json.dumps({'coordinate_exhaustive_tests':cases,'max_M':15}),flush=True)


def search(seconds,out):
    rng=np.random.default_rng(261123);t0=time.monotonic();allprimes=primes_to(2000)
    records=[];best=-1e100;trial=0;nontriv_best=-1e100
    while time.monotonic()-t0<seconds:
        M=int(rng.choice([40,60,90,120,180,250,400,700,1200,2000]))
        avail=[p for p in allprimes if p<=min(M//2,100)]
        k=min(len(avail),int(rng.integers(6,13)))
        if k<6:continue
        if trial%3==0:ps=avail[:k]
        elif trial%3==1:ps=sorted(rng.choice(avail,k,replace=False).tolist())
        else:ps=sorted(set(avail[:3]+rng.choice(avail[3:],k-3,replace=False).tolist()))
        U=source_matrix(M,ps)
        if trial%4==0:w=np.ones(k)
        elif trial%4==1:w=rng.integers(1,5,k)/4
        else:w=rng.uniform(.25,1,k)
        phases=[]
        for p in ps:
            q=p
            while q<=M:q*=p
            s=M//2 if trial%2==0 else int(rng.integers(0,q))
            if 1<=s<=M:s+=q
            phases.append((s,p*q))
        V=interval_from_phases(M,ps,phases)
        for it in range(4):
            V,phases=optimize_phases(U,V,w,ps,phases,rng)
            d=objective(U,V,w)
            active=int(np.sum(U@w>2+1e-8))
            if active and d>nontriv_best:
                nontriv_best=d
                rec={'trial':trial,'M':M,'primes':ps,'phases':phases,'active_sources':active,**exact_delta(U,V,w)}
                records.append(rec)
                print(json.dumps({'new_nontrivial_best':rec,'elapsed':round(time.monotonic()-t0,1)}),flush=True)
            w,d=improve_weights(U,V,w)
            if d>1e-7:
                rec={'trial':trial,'M':M,'primes':ps,'phases':phases,**exact_delta(U,V,w)}
                print(json.dumps({'POSITIVE_CANDIDATE':rec}),flush=True);records.append(rec)
                Path(out).write_text(json.dumps({'trials':trial+1,'records':records},indent=2));return
            if not np.any(U@w>2+1e-8):break
        trial+=1
        if trial%20==0:print(json.dumps({'trials':trial,'elapsed':round(time.monotonic()-t0,1),'best_active_delta':nontriv_best}),flush=True)
    Path(out).write_text(json.dumps({'seconds':time.monotonic()-t0,'trials':trial,'records':records,'positive_found':False},indent=2))
    print(json.dumps({'finished':True,'trials':trial,'seconds':round(time.monotonic()-t0,1),'best_active_delta':nontriv_best}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--seconds',type=int,default=240);p.add_argument('--out',default=str(Path(__file__).with_name('h2_crt_search_results.json')));p.add_argument('--test',action='store_true');a=p.parse_args()
    if a.test:test_coordinate()
    else:search(a.seconds,a.out)
