#!/usr/bin/env python3
"""Finite abstract high-prime type check; no interval shifts are sampled.
Proof and assumptions: REDUCTION.md. Standard library only.
"""
from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations
from math import isqrt
import json


def type_patterns(v):
    for l in range(v+1):
        if 3*(v-l)>9 or 3*v+2*l>18:
            continue
        types=[()]+[(i,) for i in range(v)]
        types += [(i,i) for i in range(l)]
        types += [(i,j) for i,j in combinations(range(v),2) if i<l]
        for A in combinations_with_replacement(types,9):
            m=Counter(A)
            d=[sum(i in x for x in A) for i in range(v)]
            s=[m[i,i] for i in range(v)]
            if any(d[i]<(5 if i<l else 3) for i in range(v)):
                continue
            C=[0]*v
            for i in range(l):
                D=d[i]+s[i]
                C[i]=(D-min(2,s[i])-1)//2
                if d[i]==5 and s[i]<=1:
                    C[i]=min(C[i],1)
            if any(C[i]<max(1,s[i]) for i in range(l)):
                continue
            if any(m[x]>(C[x[0]] if x[0]==x[1] else
                         isqrt((C[x[0]]+1)*(C[x[1]]+1)-1))
                   for x in m if len(x)==2):
                continue
            yield l,A,d,C


def product_rule(l,A,d):
    m=Counter(A)
    for i in range(l,len(d)):
        if d[i]!=3:
            continue
        u=[tuple(j for j in x if j!=i) for x in A if i in x]
        req=Counter(tuple(sorted(a+b)) for a,b in combinations(u,2))
        if any(m[x]<n for x,n in req.items()):
            return False
    return True


def square_rule(l,A,d):
    """Among 3 cofactors' 3 products and >=2 squares only possible equality
    is middle square = outer pair product. Unknown order is overenumerated.
    """
    m=Counter(A)
    for i in range(l,len(d)):
        if d[i]!=3:
            continue
        U=[tuple(j for j in x if j!=i) for x in A if i in x]
        ok=False
        for u in set(permutations(U)):
            pairs=Counter(tuple(sorted(u[j]+u[k])) for j,k in combinations(range(3),2))
            for js in combinations(range(3),2):
                req=pairs.copy()
                for j in js:
                    # Permit equality only in the one possible numerical case,
                    # and only when the corresponding high-part types agree.
                    square=tuple(sorted(u[j]+u[j]))
                    if j==1 and square==tuple(sorted(u[0]+u[2])):
                        continue
                    req[square]+=1
                if all(m[x]>=n for x,n in req.items()):
                    ok=True
        if not ok:
            return False
    return True


def main():
    report={}
    for v in (1,2,3,4):
        rows=list(type_patterns(v))
        after_product=[x for x in rows if product_rule(*x[:3])]
        after_square=[x for x in after_product if square_rule(*x[:3])]
        # No dependence on minimality for v>=3. Exclude common prime only
        # for counts of possible minimal counterexamples in v=1,2.
        minimal=[x for x in after_square if max(x[2])<9]
        report[str(v)]={"type_patterns":len(rows),"after_product":len(after_product),
                        "after_square":len(after_square),"after_common_prime":len(minimal)}
        if v>=3:
            assert not after_product, (v,after_product)
    print(json.dumps(report,indent=2))
    print('PASS: no possible type patterns for v=3 or v=4.')

if __name__=='__main__':
    main()
