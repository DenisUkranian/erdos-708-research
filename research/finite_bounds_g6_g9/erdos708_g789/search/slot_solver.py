import math, itertools, json, sys
from functools import lru_cache

def factor(a,ps):
    es=[]
    for p in ps:
        e=0
        while a%p==0:a//=p;e+=1
        es.append(e)
    assert a==1
    return tuple(es)

def cumulative_pack(demand,primes,M,B,node_limit=1000000):
    vals=[]
    def gen(i,a,es):
        if i==len(primes):
            if a>1:vals.append((a,tuple(es)))
            return
        p=primes[i]
        for e in range(demand[i]+1):
            if a>M:break
            gen(i+1,a,es+[e]);a*=p
    gen(0,1,[]);vals.sort(reverse=True)
    nodes=0
    @lru_cache(None)
    def go(rem,k):
        nonlocal nodes
        nodes+=1
        if nodes>node_limit:raise TimeoutError()
        if not any(rem):return ()
        if k==B:return None
        prodrem=math.prod(p**e for p,e in zip(primes,rem))
        if prodrem>M**(B-k):return None
        prev=tuple(a-b for a,b in zip(demand,rem))
        opts=[]
        for a,e in vals:
            if any(x>y for x,y in zip(e,rem)):continue
            overlap=math.prod(p**min(x,y) for p,x,y in zip(primes,e,prev))
            if k and overlap>M//(k+1):continue
            opts.append((a,e))
        for a,e in opts:
            nr=tuple(x-y for x,y in zip(rem,e))
            rr=go(nr,k+1)
            if rr is not None:return (a,)+rr
        return None
    try:r=go(tuple(demand),0)
    except TimeoutError:r=None
    return r,nodes

def verify_slots(A,hs,M,B):
    assert len(hs)<=B
    pref=1
    for j,h in enumerate(hs):
        assert 1<=h<=M
        assert j==0 or math.gcd(pref,h)<=M//(j+1)
        pref*=h
    assert pref%math.prod(A)==0

if __name__=='__main__':
    n=int(sys.argv[1]);B={6:8,7:10,8:12,9:14}[n]
    ps={6:[2,3,5],7:[2,3,5,7],8:[2,3,5,7],9:[2,3,5,7,11]}[n]
    rr=json.load(open(f'frontier_n{n}.json'));cert=[]
    for row in rr['bad']:
        for e in row['demands']:
            hs,nodes=cumulative_pack(e,ps,row['M'],B)
            if hs is None:raise RuntimeError((row['M'],e,nodes))
            pref=1
            for j,h in enumerate(hs):
                assert 1<=h<=row['M']
                assert math.gcd(pref,h)<=row['M']//(j+1)
                pref*=h
            assert pref%math.prod(p**z for p,z in zip(ps,e))==0
            cert.append([row['M'],e,hs])
    json.dump(cert,open(f'frontier_slots{n}.json','w'),indent=2)
    print('Verified explicit certificates:',len(cert))
