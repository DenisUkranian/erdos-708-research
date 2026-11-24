import itertools, math, json, sys, time, ctypes, os
from functools import lru_cache

def smooth(top, primes):
    out=[(1,(0,)*len(primes))]
    for i,p in enumerate(primes):
        new=[]
        for a,e in out:
            b=a; f=list(e)
            while b<top:
                new.append((b,tuple(f))); b*=p; f[i]+=1
        out=new
    return sorted(out)

def pareto(xs):
    if xs and len(xs[0])==5:
        lib=ctypes.CDLL(os.path.join(os.path.dirname(__file__),'skyline.so'))
        n=len(xs);d=5;typ=ctypes.c_int*(n*d)
        a=typ(*(z for x in xs for z in x));o=typ()
        k=lib.skyline(a,n,d,o)
        return [tuple(o[i*d+j] for j in range(d)) for i in range(k)]
    xs=sorted(set(xs),reverse=True)
    if not xs: return []
    dim=len(xs[0]); out=[]
    if dim==3:
        hi=max(x[1] for x in xs)+2
        tree=[-1]*(hi+1)
        for x in xs:
            j=hi-x[1]; q=j; best=-1
            while q: best=max(best,tree[q]);q-=q&-q
            if best>=x[2]:continue
            out.append(x)
            while j<=hi: tree[j]=max(tree[j],x[2]);j+=j&-j
    elif dim==4:
        h1=max(x[1] for x in xs)+2; h2=max(x[2] for x in xs)+2
        tree=[[-1]*(h2+1) for _ in range(h1+1)]
        for x in xs:
            a=h1-x[1];b=h2-x[2];q=a;best=-1
            while q:
                r=b
                while r:best=max(best,tree[q][r]);r-=r&-r
                q-=q&-q
            if best>=x[3]:continue
            out.append(x)
            while a<=h1:
                q=b
                while q<=h2:tree[a][q]=max(tree[a][q],x[3]);q+=q&-q
                a+=a&-a
    else:raise ValueError(dim)
    return out

def frontier(cands, k, eM):
    d=len(eM); dp=[[] for _ in range(k+1)]; dp[0]=[(0,)*d]
    for t,(_,e) in enumerate(cands):
        for j in range(min(k,t+1),0,-1):
            dp[j]=pareto(dp[j]+[tuple(x+y for x,y in zip(v,e)) for v in dp[j-1]])
    return [tuple(x+y for x,y in zip(v,eM)) for v in dp[k]]

def pack_greedy(exps,primes,M,B):
    caps=[M//j for j in range(1,B+1)]
    fs=[p for p,e in zip(primes,exps) for _ in range(e)][::-1]
    for mode in range(3):
        bins=[1]*B
        for p in fs:
            opts=[j for j in range(B) if bins[j]*p<=caps[j]]
            if not opts:break
            if mode==0:j=opts[0]
            elif mode==1:j=min(opts,key=lambda j:caps[j]/bins[j])
            else:j=max(opts,key=lambda j:caps[j]/bins[j])
            bins[j]*=p
        else:return bins
    return None

def pack_exact(exps,primes,M,B):
    caps=tuple(M//j for j in range(1,B+1))
    @lru_cache(None)
    def solve(exps,caps):
        if not any(exps):return ()
        i=max(i for i,e in enumerate(exps) if e)
        p=primes[i];nexp=list(exps);nexp[i]-=1;nexp=tuple(nexp)
        last=-1
        for j,c in enumerate(caps):
            if c==last or c<p:continue
            last=c
            nc=list(caps);nc[j]//=p;nc=tuple(sorted(nc,reverse=True))
            z=solve(nexp,nc)
            if z is not None:return (p,)+z
        return None
    return solve(tuple(exps),caps) is not None

def prime_union(exps,primes,M,B):
    s=0
    for d,p in zip(exps,primes):
        powers=[];q=p
        while q<=M:powers.append(M//q);q*=p
        for k in range(B+1):
            if sum(min(k,c) for c in powers)>=d:break
        else:return False
        s+=k
        if s>B:return False
    return True

def all_rough_envelopes(cands,n,eM,ps,M,B):
    if not ps or ps[-1]>M//B:return False
    for i,p in enumerate(ps):
        vals=sorted((math.prod(q**f for q,f in zip(ps[i:],e[i:])) for a,e in cands),reverse=True)
        U=math.prod(vals[:n-1])*math.prod(q**f for q,f in zip(ps[i:],eM[i:]))
        T=p*math.prod(max(M//(j*p)+1,p) for j in range(1,B+1))
        if U>=T:return False
    return True

def run(n,B,top,primes):
    nums=smooth(top,primes);bad=[];counts=[];t=time.time()
    for idx,(M,eM) in enumerate(nums):
        if M<=B or sum(eM)<3:continue
        cands=[(a,e) for a,e in nums if 2<=a<M and sum(e)>=3 and (B-1)*a>M*max(p for p,f in zip(primes,e) if f)]
        if len(cands)<n-1:continue
        if all_rough_envelopes(cands,n,eM,primes,M,B):
            counts.append([M,len(cands),0,0]);continue
        ff=frontier(cands,n-1,eM)
        failures=[]
        for e in ff:
            if not prime_union(e,primes,M,B) and pack_greedy(e,primes,M,B) is None:failures.append(e)
        if failures:bad.append({'M':M,'demands':failures,'candidate_count':len(cands)})
        counts.append([M,len(cands),len(ff),len(failures)])
        if failures or idx%15==0:print(n,M,'cands',len(cands),'frontier',len(ff),'bad',len(failures),'secs',round(time.time()-t,1),flush=True)
    result={'n':n,'B':B,'top':top,'primes':primes,'counts':counts,'bad':bad}
    with open(f'./frontier_n{n}.json','w') as f:json.dump(result,f,indent=2)
    print('DONE',n,'badM',len(bad),'seconds',time.time()-t,flush=True)

if __name__=='__main__':
    n=int(sys.argv[1])
    if n==6:run(6,8,9394,[2,3,5])
    elif n==7:run(7,10,19211,[2,3,5,7])
    elif n==8:run(8,12,12368,[2,3,5,7])
    elif n==9:run(9,14,24286,[2,3,5,7,11])
