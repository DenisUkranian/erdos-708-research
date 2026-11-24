"""Exact check of an abstract incidence obstruction; does not compute g(n)."""
from fractions import Fraction as Q
from itertools import combinations

P=range(7)
sources=[frozenset(P)]*15+[frozenset()]*41
hot=[frozenset(s) for s in combinations(P,3)]
cold=[frozenset(s) for s in combinations(P,2)]
targets=hot+cold
w=Q(2,5)
c=Q(21,10)
hinge=lambda x:max(x,0)
assert len(sources)==len(targets)==56
for p in P:
    assert sum(p in a for a in sources)==sum(p in b for b in hot)==15
A=[a for a in sources if len(a)*w>c]
assert len(A)==15
surplus=sum(hinge(len(a)*w-c) for a in sources)-sum(hinge(len(b)*w-1) for b in targets)
assert surplus==Q(7,2)
table=[]
for s in range(8):
    vals=set()
    for subset in combinations(P,s):
        B=frozenset(subset)
        lhs=sum(hinge(len(a&B)-2) for a in sources)
        rhs=sum(hinge(len(b&B)-1) for b in targets)
        assert lhs<=rhs
        vals.add((lhs,rhs))
    assert len(vals)==1
    table.append((s,*vals.pop()))
# The Jensen upper envelope is piecewise linear in s=sum prices.
# Its breakpoints suffice for exact maximization.
def upper(s):
    return 15*hinge(s-c)-35*hinge(Q(3,7)*s-1)-21*hinge(Q(2,7)*s-1)
breakpoints=[Q(0),c,Q(7,3),Q(7,2),Q(7)]
assert max(map(upper,breakpoints))==surplus
v=Q(17,50)
assert 6*v<c<7*v
assert 2*v<1<3*v
assert sum(hinge(len(a)*v-c) for a in sources)-sum(hinge(len(b)*v-1) for b in targets)==surplus
print('PASS: exact rows, own full tail, all 128 binary subset inequalities.')
print('PASS: global maximum certified by the Jensen piecewise-linear envelope.')
print('PASS: price17/50 variant has threshold-minimal source profiles.')
print('n=15, cost=35, c=21/10, surplus=7/2; abstract only.')
print('subset size / source binary hinge / target binary hinge:')
for row in table:print(*row)
