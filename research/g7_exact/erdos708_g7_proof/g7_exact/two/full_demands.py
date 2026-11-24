import sys,math,json,itertools,time
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def smooth_numbers(limit):
    out=[]
    def visit(j,n):
        if j==4:
            out.append(n)
            return
        p=(2,3,5,7)[j]
        while n<=limit:
            visit(j+1,n)
            n*=p
    visit(0,1)
    return sorted(out)
SM=smooth_numbers(665)

@lru_cache(None)
def factors(a,p,q):
    out=[];e=[]
    for r in [q,p,7,5,3,2]:
        k=0
        while a%r==0:a//=r;k+=1;out.append(r)
        e.append(k)
    assert a==1
    return tuple(out),tuple(reversed(e))

@lru_cache(None)
def goodpair(a,b,M,p,q):
    fs=sorted(factors(a,p,q)[0]+factors(b,p,q)[0],reverse=True)
    caps=[M//7,M//8,M//9]
    for mode in range(3):
        bins=[1,1,1]
        for r in fs:
            opts=[j for j in range(3) if bins[j]*r<=caps[j]]
            if not opts:break
            take=opts[0]
            if mode:
                for j in opts[1:]:
                    if (mode==1 and caps[j]*bins[take]<caps[take]*bins[j]) or (mode==2 and caps[j]*bins[take]>caps[take]*bins[j]):take=j
            bins[take]*=r
        else:return True
    return False

def main():
    demands={};stats=defaultdict(int);start=time.monotonic()
    for line in open(ROOT/'g7_exact/two/nontrivial_unresolved.txt'):
        p,q,M,z,*A=map(int,line.split())
        stats['nontrivial_rows']+=1
        bs=[None] if z==0 else ([M] if M not in A else [b for b in SM if M//2<b<M])
        for b in bs:
            B=tuple(sorted(A+([] if b is None else [b])))
            assert len(B)==7 and max(B)==M and len(set(B))==7
            if math.gcd(*B)>1:stats['gcd_removed']+=1;continue
            if b is not None and any(goodpair(a,b,M,p,q) for a in A):stats['good_pair_removed']+=1;continue
            assert all(k*a in B for a in B for k in range(2,M//a+1))
            E=tuple(map(sum,zip(*(factors(a,p,q)[1] for a in B))))
            key=(p,q,M,E)
            demands.setdefault(key,B)
            stats['actual_sets']+=1
    rows=[{'p':p,'q':q,'M':M,'E':E,'A':A} for (p,q,M,E),A in demands.items()]
    rows.sort(key=lambda x:(x['p'],x['q'],x['M'],x['E']))
    json.dump(rows,open(ROOT/'g7_exact/two/full_demands.json','w'))
    # Keep Pareto-maximal demand vectors at a fixed maximum and prime pair.
    groups=defaultdict(list)
    for row in rows:groups[(row['p'],row['q'],row['M'])].append(row)
    frontier=[]
    for key,rs in groups.items():
        rs.sort(key=lambda r:sum(r['E']),reverse=True)
        kept=[]
        for r in rs:
            if not any(all(a<=b for a,b in zip(r['E'],s['E'])) for s in kept):kept.append(r)
        frontier.extend(kept)
    json.dump(frontier,open(ROOT/'g7_exact/two/frontier_demands.json','w'))
    stats.update({'demands':len(rows),'frontier':len(frontier),'seconds':time.monotonic()-start})
    print(json.dumps(dict(stats)),flush=True)

if __name__=='__main__':main()
