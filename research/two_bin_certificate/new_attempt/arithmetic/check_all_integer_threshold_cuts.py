"""Exact abstract-model audit; not an integer-interval construction or g(n)."""
from fractions import Fraction as Q
from itertools import combinations

h=0
lights=range(1,5)
coords=range(5)
allset=frozenset(coords)
base_sources=[allset]*3+[frozenset()]*10
main=[frozenset([h])]*3
triples=[frozenset(s) for s in combinations(lights,3)]
pairs=[frozenset(s) for s in combinations(lights,2)]
base_targets=main+triples+pairs
sources=base_sources+[frozenset([p]) for p in lights for _ in range(3)]
targets=base_targets+[frozenset()]*12
z=[1]*7+[0]*(len(targets)-7)
prices=[Q(1)]+[Q(1,3)]*4
c=Q(21,10)
pos=lambda x:max(x,0)
load=lambda a:sum(prices[p] for p in a)
A=[a for a in sources if load(a)>c]
assert len(base_sources)==len(base_targets)==13
assert len(sources)==len(targets)==25
assert len(A)==3
assert max(load(allset-{p}) for p in coords)==2<c
for p in coords:
    assert sum(p in a for a in A)==sum(zb*(p in b) for b,zb in zip(targets,z))==3
    assert sum(p in a for a in sources)==sum(p in b for b in targets)
for b,zb in zip(targets,z):
    assert not (load(b)>1 and zb!=1)
    assert not (load(b)<1 and zb!=0)
J=sum(pos(load(a)-c) for a in sources)-sum(pos(load(b)-1) for b in targets)
assert J==Q(7,10)
checked=0
for s in range(6):
    for tup in combinations(coords,s):
        B=frozenset(tup)
        for k in range(1,6):
            source=sum(pos(len(a&B)-2*k) for a in sources)
            target=sum(pos(len(b&B)-k) for b in targets)
            assert source<=target
            # The equivalent strong selected-target form.
            lhs=sum(zb*min(len(b&B),k) for b,zb in zip(targets,z))
            rhs=sum(min(len(a&B),2*k) for a in A)
            rhs-=sum(pos(len(a&B)-2*k) for a in sources if load(a)<=c)
            rhs+=sum((1-zb)*pos(len(b&B)-k) for b,zb in zip(targets,z))
            assert lhs<=rhs
            checked+=1
# For k>=3 all source hinges vanish; checking up to5 also covers all
# breakpoints in the equivalent strong form.
def upper(s):
    return 3*pos(1+s-c)-4*pos(Q(3,4)*s-1)-6*pos(s/2-1)
breakpoints=[Q(0),c-1,Q(4,3),Q(2),Q(4)]
assert max(upper(s) for s in breakpoints)==J
for p in lights:
    mixed=frozenset([h,p])
    assert load(mixed)>1
    assert sum(mixed<=a for a in A)==3
    assert sum(mixed<=b for b in targets)==0
print('PASS: own full tail, minimal source profiles, exact selected rows.')
print('PASS: total prime counts agree in the M=25 augmentation.')
print(f'PASS: {checked} exact subset/integer-threshold checks and strong forms.')
print('PASS: Jensen envelope proves global maximum J=7/10; n=3, cost=7.')
print('Mandatory mixed banks are absent: the model is NOT arithmetic.')
