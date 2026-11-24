#!/usr/bin/env python3
"""Exact arithmetic necessary cores for a least-cardinality 2n counterexample.

This is NOT an original-instance counterexample search. Every filter is a
necessary condition under the explicitly recorded minimal-cardinality
assumption. A nonempty core is not evidence that a counterexample exists.
All interval bounds and prime-valuation demand bounds use integer arithmetic.
"""
from __future__ import annotations
import argparse,json,math,time,heapq
from collections import Counter
from array import array
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path


def sieve(M):
    spf=array('I',range(M+1))
    if M>=1:spf[1]=1
    for p in range(2,math.isqrt(M)+1):
        if spf[p]==p:
            for m in range(p*p,M+1,p):
                if spf[m]==m:spf[m]=p
    return spf


def factor_spf(a,spf):
    out=[]
    while a>1:
        p=spf[a];e=0
        while a%p==0:a//=p;e+=1
        out.append((int(p),e))
    return tuple(out)


def gap_divisor(facts,K,cap):
    if cap<=K:return None
    ds=[1]
    for p,e in facts:
        old=ds[:];power=1
        for _ in range(e):
            power*=p
            for d in old:
                z=d*power
                if K<z<=cap:return z
                if z<=cap:ds.append(z)
    return None


def star_min(M,L,ps):
    """Exact minimum count in M consecutive integers of Star(L,ps).

    Star comprises multiples of L and of L/q for q in ps. Distinct q
    are primes dividing L. Its one-period population is 1+sum(q-1).
    """
    ps=tuple(ps)
    if not ps:return M//L
    if len(ps)==1:return M//(L//ps[0])
    if L//ps[-1]>M:return 0 # An actual gap of this length occurs after 0.
    full,rem=divmod(M,L)
    count=1+sum(p-1 for p in ps)
    if rem==0:return full*count
    marks=[0]+list(heapq.merge(*(range(L//p,L,L//p) for p in ps)))
    assert len(marks)==count and len(set(marks))==count
    # A minimum occurs immediately after a marked integer. Count marks in
    # (marks[i],marks[i]+rem], on the periodically extended list.
    best=count;j=1
    for i,s in enumerate(marks):
        j=max(j,i+1)
        while j<i+count and marks[j%count]+(j//count)*L<=s+rem:j+=1
        best=min(best,j-i-1)
    return full*count+best


def forced_valuation_lower(M,a,facts,p):
    """Sum of exact level-count minima; a rigorous common-shift lower bound.

    It need not equal the minimum total valuation: individual level minima
    are permitted to occur at different shifts, which only weakens the bound.
    """
    ps=tuple(q for q,_ in facts);e=dict(facts)[p]
    base=star_min(M,a,ps)
    ans=(e-1)*base
    other=tuple(q for q in ps if q!=p)
    qmax=max(other,default=1)
    L=a
    levels=[]
    while L<=M*qmax:
        term=star_min(M,L,other)
        ans+=term;levels.append(term)
        L*=p
    return ans,base,levels


def max_unrestricted_p_demand(M,n,p):
    value=0;power=p
    while power<=M:
        value+=min(n,M//power);power*=p
    return value


def prime_power_bank_witness(a,facts,M,n):
    for removed,_ in facts:
        d=a//removed
        remaining=[(p,e-(p==removed)) for p,e in facts if e-(p==removed)>0]
        if len(remaining)==1 and n*d<=M:
            return {'removed_prime':removed,'prime_power_bank':d,
                    'bank_prime':remaining[0][0],'bank_exponent':remaining[0][1],
                    'floor_bank_count':M//d}
    return None


def critical_primes(facts,K):
    answer=[]
    for p,e in facts:
        qs=[q for q,f in facts if q!=p or f>=2]
        if qs and p*max(qs)>=K:answer.append(p)
    return answer


@dataclass
class Source:
    a:int
    facts:tuple
    card:int
    lower:dict


def all_demand_hist(pool):
    hist={}
    for s in pool.values():
        for p,e in s.facts:hist.setdefault(p,Counter())[e]+=1
    for p,h in hist.items():h[0]=len(pool)-sum(h.values())
    return hist


def max_pool_demand(hist,p,n,mandatory):
    h=hist.get(p,Counter({0:sum(next(iter(hist.values())).values()) if hist else 0})).copy()
    total=0
    for s in mandatory:
        e=dict(s.facts).get(p,0);h[e]-=1;total+=e
    slots=n-len(mandatory)
    for e in sorted(h,reverse=True):
        take=min(slots,h[e]);total+=take*e;slots-=take
        if not slots:return total
    if slots:raise AssertionError('Insufficient source candidates for the cardinality.')
    return total


def component_filter(pool,M):
    parent={}
    def find(x):
        parent.setdefault(x,x)
        while parent[x]!=x:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    def union(x,y):
        x,y=find(x),find(y)
        if x!=y:parent[y]=x
    for s in pool.values():
        ps=[p for p,_ in s.facts]
        for p in ps[1:]:union(ps[0],p)
        find(ps[0])
    if M not in pool:return []
    root=find(pool[M].facts[0][0])
    return [a for a,s in pool.items() if find(s.facts[0][0])!=root]


def generate(n,M,require_max=True):
    if n<2 or M<=2*n:raise ValueError('Use n>=2 and the nontrivial range M>2n.')
    start=time.monotonic();K=2*n-1;spf=sieve(M);pool={};rejected=Counter();details=[]
    maximum_rejection=None
    for a in range(2,M+1):
        facts=factor_spf(a,spf);ps=tuple(p for p,_ in facts)
        if sum(e for _,e in facts)<=2:
            rejected['at_most_two_prime_units']+=1
            if a==M:maximum_rejection={'reason':'at_most_two_prime_units','factorization':facts}
            continue
        if a*K<=M*ps[-1]:
            rejected['fresh_prime_cofactor_bank']+=1
            if a==M:maximum_rejection={'reason':'fresh_prime_cofactor_bank','removed_prime':ps[-1],'cofactor':a//ps[-1]}
            continue
        gd=gap_divisor(facts,K,M//K)
        if gd is not None:
            rejected['two_factor_divisor_gap']+=1
            if a==M:maximum_rejection={'reason':'two_factor_divisor_gap','divisor':gd,'complement':a//gd}
            continue
        pp=prime_power_bank_witness(a,facts,M,n)
        if pp is not None:
            rejected['prime_power_bank_saturation']+=1
            if a==M:maximum_rejection={'reason':'prime_power_bank_saturation',**pp}
            continue
        card=star_min(M,a,ps)
        if card>=K:
            rejected['forced_union_too_large']+=1
            if a==M:maximum_rejection={'reason':'forced_union_too_large','minimum_cardinality':card,'budget':K-1}
            continue
        lower={};bad=None
        for p in critical_primes(facts,K):
            val,_,_=forced_valuation_lower(M,a,facts,p)
            upper=max_unrestricted_p_demand(M,n,p)
            if val>=upper:
                bad={'source':a,'prime':p,'forced_valuation_lower':val,
                     'all_source_demand_upper':upper};break
            lower[p]=val
        if bad:
            rejected['unrestricted_critical_demand']+=1
            if a==M:maximum_rejection={'reason':'unrestricted_critical_demand',**bad}
            details.append({'reason':'unrestricted_critical_demand',**bad});continue
        pool[a]=Source(a,facts,card,lower)
    initial=list(pool);rounds=[];impossible=None
    if require_max and M not in pool:impossible='The required maximum source M was excluded.'
    elif len(pool)<n:impossible='Fewer than n source candidates remain.'
    round_id=0
    while impossible is None:
        removed=[]
        if require_max:
            for a in component_filter(pool,M):
                removed.append({'source':a,'reason':'outside_maximum_prime_component'})
        if not removed:
            hist=all_demand_hist(pool)
            for a,s in pool.items():
                mandatory=[s]
                if require_max and a!=M:mandatory.append(pool[M])
                for p,lo in s.lower.items():
                    upper=max_pool_demand(hist,p,n,mandatory)
                    if upper<=lo:
                        removed.append({'source':a,'reason':'critical_demand_exceeds_pool',
                                        'prime':p,'forced_valuation_lower':lo,
                                        'source_demand_upper':upper,
                                        'mandatory_sources':[z.a for z in mandatory]})
                        break
        if not removed:break
        rounds.append({'round':round_id,'pool_size_before':len(pool),'removed':removed})
        for record in removed:pool.pop(record['source'])
        round_id+=1
        if require_max and M not in pool:impossible='The required maximum source M was excluded.'
        elif len(pool)<n:impossible='Fewer than n source candidates remain.'
    if impossible is None:
        omega_max=sum(sorted((len(s.facts) for s in pool.values()),reverse=True)[:n])
        if omega_max<=2*n:
            impossible='Every n-source selection has total distinct-prime charge at most 2n.'
    return {
      'assumptions':['A hypothetical least-cardinality counterexample to the unrestricted exact 2n conjecture',
                     'Every smaller source cardinality has a 2m cover on every admissible interval',
                     'M is the interval length and an upper bound for all source integers']+
                     (['The maximum source M belongs to A'] if require_max else []),
      'n':n,'M':M,'K':K,'require_maximum_source':require_max,
      'source_filters_are_shift_uniform':True,
      'direct_filter_rejection_counts':dict(rejected),
      'maximum_source_direct_exclusion':maximum_rejection,
      'direct_critical_demand_witnesses':details,
      'initial_core_size':len(initial),'initial_core':initial,
      'pruning_rounds':rounds,'final_core_size':len(pool),'final_core':list(pool),
      'least_cardinality_counterexample_parameters_excluded':impossible is not None,
      'exclusion_reason':impossible,
      'necessary_demand_constraints':[
        {'source':a,'forced_union_minimum':s.card,
         'if_source_selected_then_D_p_at_least':{str(p):lo+1 for p,lo in s.lower.items()}}
        for a,s in pool.items() if s.lower],
      'elapsed_seconds':time.monotonic()-start,
      'limitations':'A surviving core is a necessary arithmetic relaxation, not a counterexample. Exclusion is conditional on the least-cardinality assumptions, not a standalone proof for this cardinality.'}


def validate_star():
    tests=0
    for a in range(2,81):
        spf=sieve(a);facts=factor_spf(a,spf);ps=tuple(p for p,_ in facts)
        for M in [1,a//2,a,2*a+3]:
            got=star_min(M,a,ps)
            brute=min(sum(any((x+j)%(a//p)==0 for p in ps) for j in range(1,M+1)) for x in range(a))
            assert got==brute,(M,a,ps,got,brute);tests+=1
    return tests


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--n',type=int);ap.add_argument('--M',type=int)
    ap.add_argument('--no-max-source',action='store_true');ap.add_argument('--test-star',action='store_true')
    ap.add_argument('--verify',type=Path)
    ap.add_argument('--output',type=Path);args=ap.parse_args()
    if args.test_star:
        print(json.dumps({'exact_star_tests':validate_star()}))
    elif args.verify:
        saved=json.loads(args.verify.read_text())
        result=generate(saved['n'],saved['M'],saved['require_maximum_source'])
        saved.pop('elapsed_seconds',None);result.pop('elapsed_seconds',None)
        # Normalize tuples in the newly computed witness to JSON arrays.
        assert saved==json.loads(json.dumps(result))
        print('Exact necessary-core certificate reverified (conditional minimality assumptions unchanged).')
    else:
        if args.n is None or args.M is None:ap.error('Supply --n and --M.')
        result=generate(args.n,args.M,not args.no_max_source)
        target=args.output or Path(__file__).with_name(f'core_n{args.n}_M{args.M}.json')
        target.write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps({k:result[k] for k in ['n','M','direct_filter_rejection_counts','initial_core_size','final_core_size','least_cardinality_counterexample_parameters_excluded','exclusion_reason','elapsed_seconds']},indent=2))
