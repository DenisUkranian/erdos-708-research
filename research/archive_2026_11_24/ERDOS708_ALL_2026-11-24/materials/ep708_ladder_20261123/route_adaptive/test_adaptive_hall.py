"""Structural falsification search for the adaptive full-tail Hall conjecture.

This does not compute g(n). Target residues are independently chosen modulo the
maximal relevant prime powers and are realizable by the Chinese remainder theorem.
"""
import argparse, json, math
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching

def factor_table(M):
    spf=list(range(M+1))
    for p in range(2,math.isqrt(M)+1):
        if spf[p]==p:
            for a in range(p*p,M+1,p):
                if spf[a]==a: spf[a]=p
    primes=[p for p in range(2,M+1) if spf[p]==p]
    factors=[[] for _ in range(M+1)]
    for a in range(2,M+1):
        b=a
        while b>1:
            p=spf[b];e=0
            while b%p==0:b//=p;e+=1
            factors[a].append((p,e))
    return primes,factors

class Instance:
    def __init__(self,M,w,c=2.05):
        self.M=M; self.w=w; self.c=c
        ps,self.fac=factor_table(M)
        self.ps=[p for p in ps if w.get(p,0)>0]
        self.powers={p:p**int(math.log(M,p)) for p in self.ps}
        for p in self.ps:
            while self.powers[p]*p<=M:self.powers[p]*=p
        self.X=[sum(w.get(p,0)*e for p,e in f) for f in self.fac]
        self.A=[a for a in range(2,M+1) if self.X[a]>c+1e-9]
        self.roots={}
        for a in self.A:
            divisors=[(1,0.)]
            ap=1
            for p,e in self.fac[a]:
                if not w.get(p,0):continue
                ap*=p**e
                divisors=[(d*p**j,x+j*w[p]) for d,x in divisors for j in range(e+1)]
            self.roots[a]=sorted({ap//d for d,x in divisors if x<=1+1e-9})
        self.used=sorted(set(d for ds in self.roots.values() for d in ds))
        self.r=len(set(p for a in self.A for p,e in self.fac[a] if w.get(p,0)))
    def evaluate(self,res,details=False):
        M=self.M
        ix=np.arange(1,M+1,dtype=np.int64)
        masks={}
        for d in self.used:
            v=np.ones(M,dtype=bool)
            for p,e in self.fac[d]:
                q=p**e
                v &= ((ix+int(res[p]))%q==0)
            masks[d]=v
        rows=[];cols=[]
        for i,a in enumerate(self.A):
            v=np.zeros(M,dtype=bool)
            for d in self.roots[a]:v|=masks[d]
            js=np.flatnonzero(v)
            rows.extend([i]*len(js));cols.extend(js.tolist())
        graph=csr_matrix((np.ones(len(rows),dtype=np.int8),(rows,cols)),shape=(len(self.A),M))
        match=maximum_bipartite_matching(graph,perm_type='column')
        deficiency=int(np.sum(match<0))
        if details:return deficiency,match,graph
        return deficiency

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--M',type=int,default=300)
    ap.add_argument('--trials',type=int,default=30);ap.add_argument('--seed',type=int,default=708)
    ap.add_argument('--c',type=float,default=2.05)
    args=ap.parse_args();rng=np.random.default_rng(args.seed)
    primes,_=factor_table(args.M)
    best=[]
    for style in range(7):
        if style==0:w={p:1. for p in primes}
        elif style==1:w={p:.51 for p in primes}
        elif style==2:w={p:.4 for p in primes}
        elif style==3:w={p:float(rng.choice([.3,.5,.7,1])) for p in primes}
        elif style==4:w={p:1. for p in primes if p<=math.sqrt(args.M)}
        elif style==5:w={p:float(rng.choice([.2,.4,.6,.8,1])) for p in primes if p<=math.sqrt(args.M)}
        else:w={p:float(rng.uniform(.05,1)) for p in primes}
        obj=Instance(args.M,w,args.c)
        if not obj.A:continue
        maxd=0;arg=None
        for trial in range(args.trials):
            if trial<3:
                center=[0,args.M//2,args.M][trial]
                res={p:(-center)%q for p,q in obj.powers.items()}
            elif trial<8:
                centers=rng.integers(0,args.M+1,3)
                res={p:int(-rng.choice(centers))%q for p,q in obj.powers.items()}
            else:res={p:int(rng.integers(q)) for p,q in obj.powers.items()}
            d=obj.evaluate(res)
            if d>maxd:maxd=d;arg=res
        record={'M':args.M,'c':args.c,'style':style,'n':len(obj.A),'r':obj.r,'max_deficiency':maxd}
        print(json.dumps(record),flush=True)
        if maxd>obj.r:
            print(json.dumps({'COUNTEREXAMPLE':record,'weights':w,'residues':arg}),flush=True)
        best.append(record)
    return best
if __name__=='__main__':main()
