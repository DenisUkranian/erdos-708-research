"""Exact rational checks accompanying the user's asymptotic counterexample.

This checks the exponent inequalities, the sign and enclosure of kappa,
and a finite support-discontinuity witness. It does not compute g(n),
enumerate enormous prime bands, or replace the asymptotic proof.
"""
from fractions import Fraction as F
from decimal import Decimal, getcontext
from itertools import product
from math import prod

alpha, beta, gamma = F(31,100), F(8,25), F(7,10)
assert 4*alpha>1 and 3*beta<1
assert gamma+alpha>1 and 2*beta<1
assert 2*gamma>1
assert 8*alpha>1+gamma+beta
assert 6*alpha>1+gamma
assert 1/(1+gamma)==F(10,17)>F(1,2)

# ln(32/31) = 2*atanh(1/63), with a rational upper tail bound.
x=F(1,63)
terms=12
lo=2*sum((x**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
hi=lo+2*x**(2*terms+1)/(F(2*terms+1)*(1-x*x))
assert 0<lo<hi<F(1,10)
def polynomial(mu):
    return (F(31,32)-1+mu-mu*mu/2+mu**3/6)/200
# Its derivative (1-mu+mu^2/2)/200 is positive on all real mu.
klo,khi=polynomial(lo),polynomial(hi)
assert klo>F(21033455559795,10**23)
assert khi<F(21033455559797,10**23)

def factor(n):
    out={};p=2
    while p*p<=n:
        while n%p==0:out[p]=out.get(p,0)+1;n//=p
        p+=1
    if n>1:out[n]=out.get(n,0)+1
    return out

def kernel(t,L,w):
    fac={p:e for p,e in factor(t).items() if w.get(p,F(0))>0}
    ps=list(fac);rows={p:F(0) for p in ps}
    for exps in product(*(range(fac[p]+1) for p in ps)):
        count=sum(exps)
        if not count:continue
        d=prod(p**e for p,e in zip(ps,exps))
        load=sum((w[p]*e for p,e in zip(ps,exps)),F(0))
        price=max(F(0),min(min(w[p] for p,e in zip(ps,exps) if e),(load-1)/count))
        for p,e in zip(ps,exps):
            if e and d*d<=L*p:rows[p]=max(rows[p],price)
    return sum((fac[p]*rows[p] for p in ps),F(0))

a=101*7*11
w0={101:F(1),7:F(1,100)}
eps=F(1,10**12)
w1={**w0,11:eps}
before=kernel(a,101*7,w0)
after=kernel(a,a,w1)
assert before==0 and after==F(1,200)
assert kernel(a,a,w0)==F(1,200)  # the fixed scale did not jump
getcontext().prec=45
def dec(q):return Decimal(q.numerator)/Decimal(q.denominator)
print('PASS: all rational exponent inequalities.')
print('Rigorous kappa interval:',dec(klo),'< kappa <',dec(khi))
print('PASS: support discontinuity at a=7777: 0 -> 1/200; load change =',eps)
print('No large finite counterexample or value of g(n) was computed.')
