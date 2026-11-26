"""Exact rechecks of finite price certificates and concrete primal constructions."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, product
from math import comb, lcm, prod
from random import Random
import numpy as np
from scipy.optimize import linprog


def moment_lp(costs, prices):
    masks = range(1 << len(costs))
    def total(mask, values):
        return sum(v for i,v in enumerate(values) if mask >> i & 1)
    admissible = [s for s in masks if total(s,costs) <= 100]
    evaluation = np.array([[int(s&t == s) for s in admissible] for t in masks])
    w = [total(t,prices) for t in masks]
    # Prices and all primal polynomial coefficients use twelfths as units.
    bounds = [-min(12,v) for v in w]+[min(24,w[t]) for t in admissible]
    mat = np.vstack((-evaluation,evaluation[admissible]))
    signed = np.hstack((mat,-mat))
    answer = linprog(np.ones(signed.shape[1]),A_ub=signed,b_ub=bounds,method='highs')
    assert answer.success
    d = len(admissible)
    coef = [F(float(x)).limit_denominator(100000)/12 for x in answer.x[:d]-answer.x[d:]]
    poly = {s:c for s,c in zip(admissible,coef) if c}
    for t in masks:
        v = sum(c for s,c in poly.items() if s&t == s)
        assert v >= min(1,F(w[t],12))
        if t in admissible:
            assert v <= min(2,F(w[t],12))
    print('moment costs',costs,'prices/12',prices,'profiles',len(admissible),
          'nonzero',len(poly),'L1',sum(abs(c) for c in coef))


def price_intervals():
    primes=(2,3,5,7,11,13)
    configs=np.array([w for w in product((0,4,9),repeat=len(primes)) if 4 in w and 9 in w]).T
    for m in (30,120,504,1024):
        def load(x):
            data=np.zeros((m,len(primes)),dtype=np.int64)
            for j,p in enumerate(primes):
                power=p
                while power<=x+m:
                    offset=(-x-1)%power
                    if offset<m:
                        if power<m:
                            data[offset::power,j]+=1
                        else:
                            data[offset,j]+=1
                    power*=p
            return data@configs
        canonical=load(0)
        over=np.maximum(canonical-24,0).sum(axis=0)
        # Maximizing the source surplus over every subset includes every positive term.
        period=lcm(*range(1,m+1))
        starts=[0,7207,920168185,period-m//2,prod(primes)**5-m//2]
        maxima=[]
        for x in starts:
            excess=over-np.maximum(load(x)-12,0).sum(axis=0)
            maxima.append(int(excess.max()))
        print(f'two-price interval M={m} profiles={configs.shape[1]} max excess in twelfths {maxima}')
        assert max(maxima)<=0


def centered():
    for r,k in ((2,6),(3,7),(4,8)):
        ps = [1009,1013,1019,1021,1031,1033,1039,1049][:k]
        rows = [prod(c) for c in combinations(ps,r)]
        m,n,N = max(rows),len(rows),prod(ps)**r
        start = N-m//2-1  # use offsets t=-(m//2),...,m-1-(m//2)
        assert max(N-(start+1),start+m-N) < min(ps)**r
        for cap in (r,1):
            d = comb(k-1,r-1)-cap
            tokens = ps*d
            used = {N}
            for i in range(0,len(tokens),r-1):
                chunk = tokens[i:i+r-1]
                assert len(chunk)==len(set(chunk))
                div = prod(chunk)
                b = (start//div+1)*div
                while b in used:
                    b += div
                assert start < b <= start+m
                used.add(b)
            expected = 1+(r*n-cap*k+r-2)//(r-1)
            assert len(used)==expected
            if cap==1:
                assert all(sum(b%p==0 for b in used)>=comb(k-1,r-1) for p in ps)
            else:
                assert prod(used)%prod(rows)==0
            print(f'center r={r} k={k} n={n} cap={cap} optimum={expected}')


def crt(residues):
    x, modulus = 0,1
    for residue, period in residues:
        x += modulus*((residue-x)*pow(modulus,-1,period) % period)
        modulus *= period
    return x+modulus


def twin_centers():
    ps=[1009,1013,1019,1021,1031,1033,1039]
    r=3
    rows=[prod(c) for c in combinations(ps,r)]
    m=max(rows)
    d=comb(len(ps)-1,r-1)
    chunks=[ps[i:i+r-1] for i in range(0,len(ps),r-1)]
    cheap=crt([(-prod(chunk),p**d) for chunk in chunks for p in chunk])
    expensive=crt([(p*(p**r-1)//2,p**(r+1)) for p in ps])
    assert all(N % p==0 and N % (p*p)!=0 for N in (cheap,expensive) for p in ps)
    assert (cheap-expensive) % prod(ps)==0
    offsets=[prod(chunk) for chunk in chunks]
    assert len(set(offsets))==4 and max(offsets)<m//2
    assert prod(cheap+b for b in offsets)%prod(rows)==0
    for p in ps:
        center=expensive % p**(r+1)
        assert min(center,p**(r+1)-center)>m//2
    print('twin CRT centers: r=3 k=7 n=35 cheap tau=4, both H=50; offsets',offsets)


def cycle_and_slots():
    def cost(blocks,sites):
        return len(set(sites))+sum(len(entries)-len(set(entries)) for site in set(sites)
                                   for entries in [[p for a,b in zip(blocks,sites) if b==site
                                                    for p in (2,3,5) if a%p==0]])
    labels = (2,3,10)
    initial = (4,9,10)
    opts = [list(range(a,11,a)) for a in labels]
    assert cost(labels,initial)==3
    assert min(cost(labels,s) for s in product(*opts) if
               sum(a!=b for a,b in zip(s,initial))<=1)==3
    assert min(cost(labels,s) for s in product(*opts))==cost(labels,(6,6,10))==2
    # One existing credit of 2 at 6. Assign the other five row atoms
    # from (6,10,15) to the remaining free base at 6 and two fresh points.
    tokens = (3,2,5,3,5)
    free = (9,10,12,15)
    paid = (6,3)
    @lru_cache(None)
    def savings(i,mask):
        if i>len(free):
            return 0
        choices = [(0,0)]
        if i==0:
            choices += [(1 << j,1) for j,t in enumerate(tokens) if mask>>j&1 and t==paid[1]]
        else:
            b=free[i-1]
            choices += [((1<<j)|(1<<k),1) for j,k in combinations(range(len(tokens)),2)
                        if mask>>j&1 and mask>>k&1 and tokens[j]!=tokens[k] and b%(tokens[j]*tokens[k])==0]
        return max(score+savings(i+1,mask^used) for used,score in choices)
    assert savings(0,(1<<len(tokens))-1)==3
    print('single relocations 3; joint optimum 2; five residual tokens give three savings')


def gadget_check():
    rng=Random(708)
    for trial in range(60):
        n=rng.randint(2,6)
        tokens=[rng.choice(((2,2),(2,4),(3,3),(5,5))) for _ in range(n)]
        sites=rng.sample(range(6,61),3)
        old=sites[0]
        # One old 2-slot is already credited when it exists.
        oldmask=sum(1<<j for j,(p,d) in enumerate(tokens) if p!=2 and old%d==0)
        edges=[]
        new_vertex=n
        mandatory=0
        def vertex(required):
            nonlocal new_vertex,mandatory
            v=new_vertex
            new_vertex+=1
            if required:
                mandatory |= 1<<v
            return v
        actions=[]
        for p in {p for p,d in tokens}:
            options=[j for j,(q,d) in enumerate(tokens) if q==p and oldmask>>j&1]
            if options:
                u=vertex(False)
                edges.extend((u,j,2) for j in options)
                actions.append([1<<j for j in options])
        for b in sites[1:]:
            left,right=vertex(True),vertex(True)
            edges.append((left,right,0))
            eligible=[j for j,(p,d) in enumerate(tokens) if b%d==0]
            actions.append([(1<<j)|(1<<k) for j,k in combinations(eligible,2) if tokens[j][0]!=tokens[k][0]])
            for p in {tokens[j][0] for j in eligible}:
                u,v=vertex(True),vertex(True)
                edges.extend([(left,u,0),(right,u,0),(u,v,0)])
                edges.extend((v,j,1) for j in eligible if tokens[j][0]==p)
        adj=[[] for _ in range(new_vertex)]
        for v,u,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        @lru_cache(None)
        def matching(rem):
            if not rem:
                return 0
            must=rem&mandatory
            first=must if must else rem
            v=(first&-first).bit_length()-1
            rest=rem^(1<<v)
            best=-10000 if must else matching(rest)
            for u,w in adj[v]:
                if rest>>u&1:
                    best=max(best,w+matching(rest^(1<<u)))
            return best
        @lru_cache(None)
        def packing(i,mask):
            if i==len(actions):
                return 0
            return max([packing(i+1,mask)]+[1+packing(i+1,mask^part)
                                            for part in actions[i] if mask&part==part])
        assert matching((1<<new_vertex)-1)==2*packing(0,(1<<n)-1)
    print('ordinary matching gadget equals direct packing on 60 seeded arithmetic instances')


if __name__=='__main__':
    for costs,prices in [
            ([60,60,30,30,30,30],[4,9,4,9,9,9]),
            ([46,35,31,28,24,22,19,17],[4,9,9,4,9,4,9,4]),
            ([57,44,39,33,29,23,21,18,16,13],[9,4,9,9,4,9,4,9,4,9])]:
        moment_lp(costs,prices)
    price_intervals()
    centered()
    twin_centers()
    cycle_and_slots()
    gadget_check()
