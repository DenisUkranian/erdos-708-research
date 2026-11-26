cost=(30,30,30,39,39,68)
U=[7,7,11,13,14,19,21,22,24,33,33,34,36,36]
V=[0,3,3,5,5,6,6,15,23,41,44,49,52,58]
def feasible(mask):
    return sum(c for i,c in enumerate(cost) if mask>>i&1)<=100
for subset in range(64):
    if feasible(subset):
        assert sum((x&subset)==subset for x in U) == sum((x&subset)==subset for x in V)
assert all(feasible(x) and x.bit_count()>=2 for x in U)
assert len(U)==len(V)==14 and sum(x!=0 for x in V)==13
print(sum(feasible(x) for x in range(64)),14,13)
