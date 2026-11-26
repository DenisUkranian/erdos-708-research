"""Probe the stronger one-omitted-atom Hall condition with exact bipartite matching."""
from math import prod
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching
def atoms_all(m):
    atoms=[[] for _ in range(m+1)]
    for p in range(2,m+1):
        if atoms[p]: continue
        for a in range(p,m+1,p):
            q=p
            while a%(q*p)==0: q*=p
            atoms[a].append(q)
    return atoms
for m in (512,2048,8192,32768):
    atoms=atoms_all(m)
    rows=[a for a in range(2,m+1) if len(atoms[a])>=3]
    hub=prod(p for p in range(2,150) if atoms[p]==[p] and all(p%d for d in range(2,int(p**0.5)+1)))
    for x in (m,10**24+271,hub-m//2):
        cols=[]; ind=[0]
        for a in rows:
            eligible=set()
            for power in atoms[a]:
                d=a//power
                eligible.update(range((-x-1)%d,m,d))
            cols.extend(sorted(eligible));ind.append(len(cols))
        graph=csr_matrix(([1]*len(cols),cols,ind),shape=(len(rows),m))
        match=maximum_bipartite_matching(graph,perm_type='column')
        used=set()
        for a,b in zip(rows,match):
            if b<0:continue
            assert b not in used and any((x+1+int(b))%(a//q)==0 for q in atoms[a])
            used.add(b)
        print(m,x,len(rows),len(used),flush=True)
