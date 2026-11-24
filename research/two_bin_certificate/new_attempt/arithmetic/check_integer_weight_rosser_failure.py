"""Self-contained exact audit of a weighted coefficient recurrence, not g(n)."""
from math import prod

prices={2:1,3:1,5:3,7:1}
r=10

def recurrence(M):
    coeff={1:tuple(range(r+1))}
    states={}
    for p in sorted(prices,reverse=True):
        k=prices[p]
        new={}
        for d,q in coeff.items():
            powers=[1]
            if d==1:
                for _ in range((r+k-1)//k):powers.append(powers[-1]*p)
            else:
                while d*powers[-1]*p<=M:powers.append(powers[-1]*p)
            J=len(powers)-1
            previous=(0,)*(r+1)
            for j,pp in enumerate(powers):
                if d!=1 and j==J:
                    current=tuple(min(q[max(0,t-e*k)] for e in
                                      range(j,max(j,(t+k-1)//k)+1))
                                  for t in range(r+1))
                else:
                    current=tuple(q[max(0,t-j*k)] for t in range(r+1))
                diff=tuple(x-y for x,y in zip(current,previous))
                if any(diff):new[d*pp]=diff
                previous=current
        coeff=new
        states[p]=dict(coeff)
    return coeff,states

def valuation(a,p):
    e=0
    while a%p==0:a//=p;e+=1
    return e

def Y(a):return sum(k*valuation(a,p) for p,k in prices.items())
def positive(x):return max(x,0)
def closed(a):
    return sum(positive(k*valuation(a,p)-r) for p,k in prices.items())-int(a%105==0)
def is_pure(d):
    return any(d==p**valuation(d,p) for p in prices)

for M in [105,106]:
    C,states=recurrence(M)
    plateau=(0,1,1,1,0,0,0,0,0,0,0)
    assert states[5][35]==plateau
    assert states[3][105]==tuple(-x for x in plateau)
    assert states[2][105][r]==-1
    mixed={d:q[r] for d,q in C.items() if d>1 and not is_pure(d) and q[r]}
    assert mixed=={105:-1}
    # Audit every prefix evaluation, not a floating-point coefficient sum.
    F=lambda a:Y(a)-r+sum(q[r] for d,q in C.items() if a%d==0)
    for a in range(1,211):
        assert F(a)==closed(a)
        assert F(a)<=positive(Y(a)-r)
    assert max(Y(a) for a in range(1,M+1))==8
    assert sum(F(a) for a in range(1,M+1))==-1
    assert sum(positive(Y(a)-2*r) for a in range(1,M+1))==0
    if M==106:
        I=range(105,211)
        assert len(I)==M
        assert sum(F(a) for a in I)==-2
        assert sum(positive(Y(a)-r) for a in I)==0
        assert sum(a%105==0 for a in I)-(M//105)==1
print('PASS: exact integer-threshold recurrence and the local boundary trace.')
print('PASS: M=105/106 prefix certificate sum -1; desired source hinge 0.')
print('PASS: I=[105,210] has certificate sum -2 and actual target hinge 0.')
print('This disproves the certificate reserve, not the desired arithmetic inequality.')
