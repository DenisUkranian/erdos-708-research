# Arithmetic audit of the new all-occurrence kernel

Date: 24 November 2026.

## Status

This note does not prove the aggregate kernel transfer or Erdős 708. It
records a genuine obstruction to a row-by-row proof, an exact favorable
modulus property of the new kernel, and a signed-certificate criterion.
The obstruction is not a positive global optimizer and does not refute
the required optimizer inequality.

Write

    r(d)=max(0,min(min_{p|d} w_p,(X(d)-1)/Omega(d))).

For a prime occurrence p, a carrier d is eligible at scale x when

    p|d, d|b, d²/p<=x.

The source uses x=a, while the target uses the fixed x=M.

## 1. The level formulation

For t>0, let P_t={p:w_p>=t} and

    Y_t(d)=sum_{p in P_t}(w_p-t)v_p(d).

Then r(d)>=t exactly when d is supported on P_t and Y_t(d)>=1.
Writing d=pe gives the row-p source conditions

    a=peu, e<=u, Y_t(e)>=1-w_p+t.

On the target, the actual divisor condition remains and e²p<=M replaces
e<=u. This is an exact reduction; it does not transfer row balances to a
different source set.

## 2. Source-dependent eligibility does not repair rowwise transfer

Take N large, M=2N, c in (2,3), and w_p=1 for every prime p<=M. The full
strict source tail is A={a<=M:Omega(a)>=3}. Consider row p=2 at level
t=1/2.

For a=2x in A, the number x is composite. Its smallest prime factor q
satisfies q²<=x. Thus the carrier d=2q is eligible at the *actual source
scale*: d²/2=2q²<=2x=a. Conversely every row occurrence counted on A is
already one of these original row occurrences. The weighted source
level count is therefore exactly

    S= sum_{x<=N, x composite}(1+v_2(x))
     = 2N-s_2(N)-pi(N)-2,                         (1)

where s_2 is the binary digit sum.

On the target, a carrier of r-value at least 1/2 exists precisely when
x=b/2 has a prime divisor q<=sqrt(N). Indeed every carrier contains at
least two prime occurrences, and replacing it by 2q preserves eligibility.
For I={2x_0+1,...,2x_0+2N}, the target row-level count is

    U= sum_{x_0<x<=x_0+N}(1+v_2(x))
            1_{some prime q<=sqrt(N) divides x}.   (2)

Let V=product_{q<=sqrt(N)}(1-1/q). An average over genuine integer shifts
gives an actual shift satisfying

    U <= floor(2N-NV).                            (3)

For completeness, let Q be the product of the odd primes <=sqrt(N),
take L=2^k Q with 2^k>N, and average x_0 over 0,...,L-1. The unweighted
union count has exact mean N(1-V). Since the union includes every even x,
its v_2-weighted part is simply sum v_2(x). Legendre's formula and
s_2(L+i-1)=s_2(Q)+s_2(i-1), for 1<=i<=N, show that its mean is
N(1-s_2(Q)/L). Thus the mean in (2) is strictly below 2N-NV. No
independently chosen, unrealizable residues are used.

The prime number theorem and Mertens' product theorem imply

    S-U >= (2 exp(-EulerGamma)-1+o(1)) N/log N.

The coefficient is positive. This exceeds every fixed multiple of
sqrt(M). Hence a square-root transfer bound for each row and each
level fails even with the original full tail and the actual-source
eligibility condition.

### Fully explicit finite check

Take N=2,000,000, M=4,000,000 and

    I={2^101+1,...,2^101+4,000,000}.

The exact values are

    pi(N)=148,933, s_2(N)=7,
    source row-level count S=3,851,058,
    target row-level count U=3,845,378,
    S-U=5,680 > sqrt(M)=2,000.

The target rough count in the quotient interval
{2^100+1,...,2^100+2,000,000}, using primes <=1414, is exactly 154,615;
Legendre's formula gives its total v_2-weight 1,999,993. These are
integer sieve computations, not new values of g(n).

This example has an excessively dense source tail and is not a
positive global surplus optimum. Other prime rows, other price levels,
and the slack between the source kernel and the source hinge remain
available. The aggregate inequality is not disproved.

## 3. Every pair intersection within one unweighted row is short

If d,e are both eligible in row p at scale M, then

    lcm(d,e) <= de/p <= M.                          (4)

Thus every negative pair-intersection term in the first two terms of
inclusion-exclusion for the *unweighted* row union has an actual modulus
at most M, irrespective of the number or sizes of the prime factors of
d and e. This is stronger than restricting sources to three or four
prime factors.

Equation (4) does not control triple intersections. Nor does it directly
control all whole-row valuation layers: lcm(p^j,d,e) can exceed M. Those
terms cannot be omitted under a claim of exact whole-prime balance.

## 4. A precise sufficient signed certificate

For fixed M and w, suppose real coefficients alpha_d, 1<=d<=M, give

    P(b)=sum_{d|b,d<=M} alpha_d <= (X(b)-1)_+

for every positive integer b. Then exact interval counts give

    sum_{b in I}(X(b)-1)_+
       >= sum_{a<=M}P(a)-sum_{d<=M}(-alpha_d)_+.     (5)

Indeed every target divisibility count is either floor(M/d) or
floor(M/d)+1. Positive coefficients incur no loss; a negative one incurs
at most its absolute value once.

Consequently the following source inequality would suffice for the
exact fractional budget 2 at this instance:

    sum_{a<=M}[P(a)-(-alpha_a)_+]
       >= sum_{a<=M}(X(a)-2)_+.                     (6)

This records where the unused source budget can pay actual rounding
errors, rather than charging each root independently. Existence of a
uniform certificate satisfying (6) is **not proved**.

For orientation only: in a unit-price configuration where the complete
degree-3 Bonferroni polynomial is available with all its needed moduli
<=M, P(r)=binom(r,2)-binom(r,3) is below r-1 for all integer r>=1.
At a squarefree triple its value is 2 and its negative coefficient costs
1, leaving exactly the source hinge r-2=1. This shows that negative
coefficient errors can be paid by the budget-2 source reserve. It does
not extend the certificate to unrestricted profiles or forbidden large
moduli.

## Remaining gap

No proof of

    sum_{a<=M} K_a(a) <= sum_{b in I} K_M(b)+O(sqrt M)

or of the weaker full-tail/shared-reserve version was obtained. A valid
argument must combine rows or price levels, retain the difference
between the kernel and the source hinge, and control the higher
intersections and prime-power layers left out by (4).
