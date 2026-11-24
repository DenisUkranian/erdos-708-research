import math
import numpy as np
from scipy.optimize import linprog

def probe(r,c=2.1):
    types=[(i,j) for j in range(r+1) for i in range(r-j+1)]
    C=math.comb
    A=[]
    for u,v in types:
        if u+v==0:continue
        row=[]
        for i,j in types:
            if j<v or i+j<u+v:
                row.append(0.0);continue
            n=C(r,j)*C(r-j,i)
            m=0
            for t in range(u+1):
                if 0<=j-v-t<=r-u-v and 0<=i-u+t<=r-v-u-(j-v-t):
                    m+=C(u,t)*C(r-v-u,j-v-t)*C(r-v-u-j+v+t,i-u+t)
            row.append(m/n)
        A.append(row)
    A=np.array(A)
    # Variables a(type) and b(type) are TOTAL orbit masses.
    n=len(types)
    eq=np.r_[np.ones(n),-np.ones(n)][None,:]
    ub=np.block([[-A,A],[A,-A]])
    rhs=np.r_[np.ones(len(A)),np.zeros(len(A))]
    obj=np.r_[-np.maximum(np.array([i/2+j for i,j in types])-c,0),np.maximum(np.array([i/2+j for i,j in types])-1,0)]
    sol=linprog(obj,A_ub=ub,b_ub=rhs,A_eq=eq,b_eq=[0],bounds=(0,None),method='highs')
    if not sol.success:return {'r':r,'error':sol.message}
    supp=[]
    for side,off in [('source',0),('target',n)]:
        for k,t in enumerate(types):
            if sol.x[off+k]>1e-7:supp.append([side,*t,sol.x[off+k]])
    return {'r':r,'maxJ':-sol.fun,'total':sum(sol.x[:n]),'support':supp}

if __name__=='__main__':
    import json
    result=[probe(r) for r in range(3,17)]
    print(json.dumps(result,indent=2))
