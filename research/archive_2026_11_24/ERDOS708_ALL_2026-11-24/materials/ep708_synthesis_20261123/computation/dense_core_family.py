#!/usr/bin/env python3
"""A source-only relaxation witness, emphatically NOT a counterexample.

The family passes the arithmetic filters in necessary_core.py without
constructing all M potential sources or any CRT interval search. It proves
that those particular filters alone cannot finish the central range.
"""
from __future__ import annotations
import argparse,json,math
from collections import Counter
from fractions import Fraction
from itertools import combinations_with_replacement
from pathlib import Path


def primes_to(y):
    return [p for p in range(2,y+1) if all(p%d for d in range(2,math.isqrt(p)+1))]


def factor_on(n,ps):
    out={}
    for p in ps:
        e=0
        while n%p==0:n//=p;e+=1
        if e:out[p]=e
    assert n==1
    return out


def factorial_v(N,p):
    s=0
    while N:N//=p;s+=N
    return s


def forced_union_valuation_at_zero(M,a,facts,p):
    """Exact v_p of the forced union in I=[1,M], by inclusion-exclusion."""
    e=facts.get(p,0)
    value=0
    for q in facts:
        d=a//q;N=M//d
        value+=(e-(q==p))*N+factorial_v(N,p)
    N=M//a
    value-=(len(facts)-1)*(e*N+factorial_v(N,p))
    return value


def make(n=16384,cutoff=113):
    assert n>=16 and n&(n-1)==0
    M=n*n;K=2*n-1;ps=primes_to(cutoff);odd=[p for p in ps if p!=2]
    assert cutoff*cutoff<K
    def normalize(m):
        a=m
        while 2*a<=M:a*=2
        return a
    special_odd=1
    while 3*special_odd<=M:special_odd*=3
    mandatory={3*p**3 for p in odd}
    assert all(2*m<=M for m in mandatory)
    selected=set(mandatory)
    for tup in combinations_with_replacement(odd,4):
        m=math.prod(tup)
        if 2*m<=M:selected.add(m)
        if len(selected)>=n-2:break
    assert len(selected)==n-2
    A=sorted({M,special_odd}|{normalize(m) for m in selected})
    assert len(A)==n and max(A)==M and math.gcd(*A)==1
    facts={a:factor_on(a,ps) for a in A}
    P=sorted({p for f in facts.values() for p in f})
    Q=sorted({p for a,f in facts.items() for p in factor_on(a//max(f),ps)})
    assert P==ps and Q==ps
    # Every prime is linked to 2 by a selected normalized 3*p^3 source.
    for p in odd:
        bridge=normalize(3*p**3)
        assert bridge in facts and 2 in facts[bridge] and p in facts[bridge]
    assert M//K<K+1 # the forbidden divisor interval is empty
    demand=Counter()
    for f in facts.values():demand.update(f)
    max_card_upper=0;min_cofactor_margin=None;min_unsaturated_margin=None
    total_charge=0
    for a,f in facts.items():
        assert sum(f.values())>=3
        assert a*K>M*max(f)
        # In fact no prime-deletion bank has as many as n multiples.
        for q in f:
            d=a//q
            assert n*d>M
            margin=n*d-M
            min_cofactor_margin=margin if min_cofactor_margin is None else min(min_cofactor_margin,margin)
        # Every product of two prime occurrences is below K: no critical pair.
        assert max(f)**2<K
        c=1+sum(p-1 for p in f)
        upper=((M+a-1)//a)*c
        assert upper<K
        max_card_upper=max(max_card_upper,upper)
        # A diagnostic for the stronger all-demand-saturated shortcut.
        p=2 if a%2==0 else 3
        actual=forced_union_valuation_at_zero(M,a,f,p)
        assert demand[p]>actual
        gap=demand[p]-actual
        min_unsaturated_margin=gap if min_unsaturated_margin is None else min(min_unsaturated_margin,gap)
        total_charge+=len(f)
    assert total_charge>2*n
    # A concrete failure of our sufficient exact-2n source certificate.
    witness=normalize(3**4)
    assert witness in facts
    d=witness//3
    term=M//d-sum((M+d*q-1)//(d*q) for q in Q if d*q<=M)
    fibre=sum(a//max(facts[a])==d for a in A)
    assert term<fibre
    mu=sum((Fraction(1,p) for p in Q),Fraction(0))
    assert mu>1
    return {
      'status':'Exact witness to survival of a source-only arithmetic relaxation; NOT a counterexample to 708 or H2.',
      'n':n,'M':M,'K':K,'prime_cutoff':cutoff,'sources':A,
      'gcd_of_all_sources':1,'prime_support_connected':True,
      'full_source_prime_support':P,'cofactor_prime_support':Q,
      'cofactor_reciprocal_mass':str(mu),'cofactor_mass_exceeds_one':True,
      'all_sources_have_Omega_at_least_three':True,
      'forbidden_divisor_interval_is_empty':True,
      'all_prime_cofactors_exceed_M_over_n':True,
      'minimum_integer_n_cofactor_minus_M':min_cofactor_margin,
      'all_two_prime_occurrence_products_below_K':True,
      'critical_two_prime_demand_constraints':'vacuous on every member',
      'maximum_uniform_forced_union_cardinality_upper_bound':max_card_upper,
      'forced_union_cardinality_budget':K-1,
      'total_distinct_prime_charge':total_charge,
      'minimum_demand_minus_forced_valuation_at_zero_for_selected_prime':min_unsaturated_margin,
      'finite_exact2n_certificate_failure':{
          'source':witness,'cofactor':d,'floor_ceiling_lower_bound':term,
          'actual_fibre_size':fibre},
      'limitations':[
        'No cover B_a with all the universal minimal-counterexample properties is asserted to exist.',
        'The universal closure requirement concerns every small cover, not merely source arithmetic.',
        'At x=0 the original product-cover instance is trivially covered by A itself.',
        'Failure of a sufficient sparse certificate is not a counterexample.',
        'This witness shows only that the listed arithmetic filters cannot by themselves eliminate this family.'
      ]}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path)
    parser.add_argument('--verify',type=Path);args=parser.parse_args()
    result=make()
    if args.verify:
        assert json.loads(args.verify.read_text())==result
        print('Exact dense-core-family certificate reverified.')
    else:
        target=args.output or Path(__file__).with_name('dense_core_family_certificate.json')
        target.write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps({k:v for k,v in result.items() if k!='sources'},indent=2))
