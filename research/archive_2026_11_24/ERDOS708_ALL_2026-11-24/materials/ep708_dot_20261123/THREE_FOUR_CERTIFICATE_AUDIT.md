# Joint three/four-occurrence certificate: audit and repeated-prime repair

Status: the residual certificate below is proved, conditional on an actual
periodic core of period Q=o(log M). It does not establish that an arbitrary
708 obstruction admits that core reduction. It does not claim the general
asymptotic or the exact 2n bound.

The key repair is that repeated external primes need not be discarded.
Cap each external prime's total contribution at one. The only repeated
source pattern with positive residual is p^2 q r, and its two simple
prime rows already pay the residual. The same joint counting bound covers
it through a diagonal term of size o(1).

## 1. Setting and precise residual proposition

Let y=M^(1/5), let P be any subset of primes in (y,M], and let
0<=w_p<=1. Let Q be an integer coprime to every p in P, with
Q/log M -> 0. All asymptotic errors below are uniform in P, the weights,
the interval shift, the residue class modulo Q, and the price level.

Fix one residue class rho modulo Q and a number s in [0,1]. On sources
a<=M, and on an arbitrary positive M-term target interval I, put

    f_p(a)=min(w_p v_p(a),1),
    u_p=min(w_p,s),
    L(a)=(sum_p min(f_p(a),s)-1-s)_+,
    R(b)=(sum_p min(f_p(b),s)-s)_+.

Then there is an absolute kappa<1, for example kappa=0.995, such that
for all sufficiently large M along Q=o(log M),

    sum_{a<=M, a=rho mod Q} L(a)
       <= kappa sum_{b in I, b=rho mod Q} R(b).          (1)

No squarefreeness assumption and no deletion of sources near M are
needed for (1). The residuewise choice s=s(rho) may be arbitrary, since
the same sufficiently-large threshold works uniformly for all s.

The set P may omit primes. When counting the number of external prime
occurrences, count only occurrences of primes in P. There are at most
four, since each exceeds M^(1/5). In upper bounds, allowing any prime
greater than y only enlarges the source count.

## 2. Pointwise row payments

For distinct p,q in P define

    e_pq=(u_p+u_q-s)_+.

Call q eligible in row p when q<=U_p=sqrt(M/p). For p dividing an
integer b define

    g_p(b)=max{e_pq:q in P, q!=p, q|b, q<=U_p},

with maximum zero for an empty set; set g_p(b)=0 if p does not divide b.
Only rows p<=M^(3/5) are needed. A source with positive residual has
at least three distinct external primes, hence no larger row prime.

### The target budget is spent only once

For every target b,

    sum_p g_p(b)
       <=2(sum_{p|b}u_p-s)_+
       <=2R(b).                                        (2)

To prove the first inequality, removing eligibility restrictions only
increases the left side. Let U>=V be the two largest present weights.
If U+V<=s there is nothing to prove. Otherwise the row of U has value
U+V-s. The other positive rows have indices in a set T, |T|=k>=1,
and sum at most sum_{i in T}(u_i+U-s). Thus their combined cost is

    U+V-s + sum_{i in T}u_i + k(U-s).

Subtracting this from 2(U+sum_{i in T}u_i-s) gives

    sum_{i in T}u_i - V + (k-1)(s-U) >= 0.

All omitted weights are nonnegative, proving (2).

### Three external occurrences

If a has three distinct external primes p,q,r, then each pair price
is at least L(a), since the omitted weight is at most one. In each
row at least one of the other two primes is eligible: otherwise their
product would exceed M/p. Consequently

    sum_{p|a}g_p(a)>=3L(a).                             (3)

If a has at most two distinct external primes, its residual is zero:
the truncated external sum is at most 2s<=1+s. This covers all repeated
patterns with at most three total occurrences.

### Four external occurrences, including a repeated prime

If p q r t<=M and all four occurrences exceed y, every pair of SIMPLE
prime occurrences is mutually eligible. Indeed q<M^(2/5), while the
product r t of the remaining two occurrences exceeds M^(2/5); hence
q<r t and p q^2<=p q r t<=M. This proof permits r=t.

For four distinct primes, every perfect matching satisfies

    e_pq+e_rt >= (u_p+u_q+u_r+u_t-2s)_+ >= L(a).

Summing row maxima along that matching yields at least 2L(a).

If the source has the repeated pattern p^2 q r, with p,q,r distinct,
write u_p,2=min(2w_p,s). Since u_p,2<=1,

    L(a)=(u_p,2+u_q+u_r-1-s)_+ <= e_qr.                (4)

The two simple rows q,r therefore pay at least 2L(a). Patterns p^4,
p^3 q and p^2 q^2 have at most two distinct external primes and zero
residual after the per-prime cap.

For four-occurrence sources define g_p^simp(a) as the same maximum but
only when v_p(a)=1 and only over partners q with v_q(a)=1. Then

    sum_p g_p^simp(a)>=2L(a)                            (5)

for every four-occurrence source. This restriction is important:
the repeated row is not silently charged by a first-occurrence price.

## 3. Uniform target union count, with a relative error

Fix a needed row p and a price level z>=0, and put

    B={q in P:q!=p, y<q<=U_p, e_pq>z},
    h=sum_{q in B}1/q, k=|B|, N=M/(Qp).

If B is empty all relevant quantities vanish. Otherwise
M^(1/5)<=U_p<=M^(2/5), and

    k<=U_p h,   k<<U_p/log M,
    k^2<<U_p^2 h/log M=(M/p)h/log M.                   (6)

The elementary congruence count for each modulus Qp q or Qp q r is
M divided by that modulus, with error at most one. The moduli are
coprime products except for the prescribed residue modulo Q.

Let T_p(z) count target b in I, b=rho mod Q, with g_p(b)>z. The first
and second moments of the number of B-divisors of such a target obey

    first moment = Nh+O(k),
    second moment <=N(h+h^2)+O(k+k^2).

Cauchy--Schwarz and (6) give

    T_p(z)>=(1-o(1)) Nh/(1+h).                         (7)

The error is uniform even when h tends to zero: k/(Nh)<=Q/U_p and
k^2/(Nh)<<Q/log M. This is a relative o(Nh), not an absolute o(M).
Also h<=log 2+o(1), uniformly, by the prime reciprocal estimate.

## 4. The three-occurrence source count

Let D3_p(z) count sources a<=M, a=rho mod Q, having exactly three
external occurrences and satisfying g_p(a)>z. Repeated patterns with
zero residual may be ignored; thus D3 uses three distinct primes.

Count all pairs (q,r) of distinct external primes other than p, with
q in B and p q r<=M, and subtract the pairs with both q,r in B once.
On each source this is the number of unordered pairs containing a
B-prime, hence is nonnegative. Every source counted by D3 contributes
at least one. By congruence counts,

    D3_p(z) <= N sum_{q in B}(1/q)
                       sum_{y<r<=M/(pq)}1/r
                  - (N/2)h^2 + o(Nh).                 (8)

The harmless diagonal correction is at most N sum_{q in B}1/q^2
<=Nh/y. The positive floor-error count is

    <=sum_{q in B} pi(M/(pq))
     <<(M/p)h/log M,

because M/(pq)>=q>y. The negative floor errors cost O(k^2), already
controlled by (6). Both are O(QNh/log M).

For the main term, write alpha=log p/log M>=1/5 and
x(q)=5 log q/log M in [1,2]. Uniform Mertens estimates give

    sum_{y<r<=M/(pq)}1/r
       <=log(4-x(q))+epsilon_M,

where epsilon_M->0 independently of p and q. Since

    d/d(log x) log(4-x) = -x/(4-x) <=-1/3,

we have log(4-x)<=log 3-(1/3)log x.

The reciprocal-prime measure in the variable log x has cumulative mass
at most t+epsilon_M on [0,t], uniformly for 0<=t<=log 2.
Therefore every subset B of mass h satisfies the rearrangement bound

    sum_{q in B}(log x(q))/q >=h^2/2-O(epsilon_M h).

For example, integrate the lower quantile bound (r-epsilon_M)_+ for
0<=r<=h. Crucially the error is proportional to h.

Substitution in (8) proves

    D3_p(z) <=Nh[log 3-(2/3)h+o(1)].                  (9)

The coefficient 2/3 consists of 1/6 from the size-sensitive partner
bound and 1/2 from duplicate partner subtraction. Dropping either
effect loses the stated constant.

## 5. The four-occurrence source count, with diagonal prime squares

Let D4_p(z) count four-occurrence sources with v_p(a)=1 and
g_p^simp(a)>z. A counted source has a simple partner q in B, and its
remaining two external occurrences r,t may be equal. Thus

    D4_p(z) <= sum_{q in B}
                 sum_{y<r<=t, rt<=M/(pq)}
                    #{a<=M:a=rho mod Q, p q r t|a}.    (10)

Coincidences with p or q can be omitted in the exact sum and then
allowed in an upper bound. A possible small-prime cofactor is already
included in each multiple count; no source fibre is identified with
only its active part.

Since p,q>y, M/(pq)<y^3. The main reciprocal sum in (10) is at most

    Nh[gamma+o(1)],
    gamma=(1/2) integral_1^2 log(3-x) dx/x <0.15.        (11)

This follows from uniform Mertens estimates in both variables. The
unordered diagonal adds at most (1/2)sum_{r>y}1/r^2=o(1), uniformly;
therefore allowing r=t is legitimate.

The number of pair moduli rt<=T, r,t>y, is O(T/log M), uniformly for
y^2<=T<=y^3: sum the Chebyshev bound pi(T/r) over y<r<=T/y and use
sum_{y<r<=y^2}1/r=O(1). Consequently the total floor error in (10)
is O((M/p)h/log M)=O(QNh/log M). We obtain

    D4_p(z) <=Nh[0.15+o(1)].                           (12)

The strict bound in (11) can be certified without numerical integration.
The function f(x)=log(3-x)/x is convex on [1,2]. Its four-panel
trapezoid upper sum gives

    gamma <= (1/8)[(log 2)/2 +(4/5)log(7/4)
                        +(2/3)log(3/2)+(4/7)log(5/4)]
          <0.149011<0.15.

For convexity, set v=x/(3-x). The sign of x^3 f''(x) is the sign of
2log(3/(1+v))+2v-v^2, which decreases to zero on v in [1/2,2].

## 6. Joint allocation and integration over price levels

Put A0=(2/3)log 3+0.15 and B0=4/9. A direct quadratic calculation gives

    max_{h>=0}(1+h)(A0-B0 h)
       =A0+(A0-B0)^2/(4B0)
       <0.990304<0.991.                               (13)

For a rational verification of the displayed strict bound, substitute
log 3<1098613/10^6 into A0; the resulting rational expression is less
than 0.990304. The maximum expression is increasing in A0 here.

Equations (7),(9),(12), all with uniform relative errors, imply for
all sufficiently large M along Q=o(log M),

    (2/3)D3_p(z)+D4_p(z) <=0.995 T_p(z)                (14)

simultaneously in every row, level, residue and choice of weights.
Integrate (14) over z>=0. Sum over rows p. By (3),(5),(2),

    2 sum_{source residue}L
      <=(2/3)sum_p sum_{3-occurrence sources}g_p
           +sum_p sum_{4-occurrence sources}g_p^simp
      <=0.995 sum_p sum_{target residue}g_p
      <=1.99 sum_{target residue}R.

This proves (1). The target capacity is counted through the sum of row
maxima and its single pointwise bound (2); the three- and four-occurrence
source estimates are not separately assigned the full target budget.

## 7. Why the external per-prime cap is legitimate for J_c

Suppose the actual load is X=S+sum_{p in P}w_pv_p, and let
Y=S+sum_{p in P}min(w_pv_p,1), T=X-Y.
The function T is a sum of nonnegative prime-power divisor increments.
Thus sum_{a<=M}T(a)<=sum_{b in I}T(b), for every actual M-term interval.
Whenever T(b)>0, some capped prime contributes one, so Y(b)>=1 and

    (X(b)-1)_+=(Y(b)-1)_+ +T(b).

Also (X(a)-c)_+<=(Y(a)-c)_++T(a). Subtracting sums yields

    J_c(X)<=J_c(Y).                                    (15)

Only the external primes need be capped. The core function S is
unchanged. Equation (15) is an analytic comparison, not a claim that
the capped profiles are another raw dual with transferred row balances.

## 8. Full hinge theorem under the stated periodic-core hypothesis

Let S(t)>=0 be an actual Q-periodic function and let

    X(t)=S(t)+sum_{p in P}w_p v_p(t),
    r=|{p in P:w_p>0}|,   Smax=max_t S(t).

Retain all hypotheses above: each active external p exceeds M^(1/5),
Q is coprime to them, and Q=o(log M). Then, uniformly in the shift
and weights, for all sufficiently large M,

    J_2(X) <= Q(r+Smax).                               (16)

More precisely, after capping the external contributions to form Y,

    J_2(Y) <= Q(r+Smax) -(1-kappa)sum_{b in I}R(b),      (17)

where R is the residuewise residual below and kappa=0.995 is allowed.
No source deletion occurs in these inequalities.

To prove them, put B(t)=(S(t)-1)_+ and, for every external prime,

    G_p(t)=(S(t)+f_p(t)-1)_+ -B(t).

For a residue rho with S(rho)>=1, set L=R=0. On that residue,

    (Y-1)_+=B+sum_p G_p,
    (Y-2)_+<=B+sum_p G_p.

For S(rho)<1 put s=1-S(rho). The elementary truncation decomposition is

    (Y-1)_+=sum_p(f_p-s)_+ +(sum_p min(f_p,s)-s)_+
            =B+sum_p G_p+R,

    (Y-2)_+<=sum_p(f_p-s)_+
                  +(sum_p min(f_p,s)-1-s)_+
            =B+sum_p G_p+L.

The second inequality follows from (A+B-T)_+<=A+(B-T)_+ for A>=0.
Summing (1) over the residue classes proves sum_prefix L<=kappa sum_I R.

The base B is periodic, so its prefix/interval discrepancy in absolute
value is at most sum_rho B(rho)<=Q Smax.
For each fixed residue rho, G_p is a nondecreasing function of v_p,
vanishes at v_p=0, and has total increment mass at most one. Expand it
in all prime-power indicators. The count of positions of a fixed
residue modulo Q divisible by p^j differs between the prefix and the
target interval by at most one, since gcd(Q,p)=1. Summing the increments
therefore bounds the discrepancy for G_p by Q, regardless of the number
of nonzero prime-power levels. Summing over the r active external primes
costs Qr. This proves (17), and (15) proves (16) for X.

### Consequence on a genuine raw global surplus optimum

Suppose a sequence of original raw global maxima at c=2+delta has full
tails A of size n tending to infinity. Use the previously established
source-prime normalization r_total<=pi(C0 n), the gate M<16n^2, and
M>cn from positive surplus. Suppose in addition that the relevant
load really has the representation above with Q=o(log M), or that a
valid one-sided cap comparison has already reduced it to such a load.
Assume Smax<=log_2 M; this holds for a genuine capped small-prime core
when Q<=M, since every residue has a representative a<=Q<=M and its
core load is at most the full raw prefix load.

Then

    Q(r+Smax)=o(n).

For the ORIGINAL raw load, however,

    J_2(X)-J_(2+delta)(X)
       =sum_{a<=M}[(X(a)-2)_+-(X(a)-2-delta)_+]
       >=delta n.

Thus a positive J_(2+delta) contradicts (16). This excludes the stated
periodic-core branch uniformly at the n scale, including sparse tails.
It does not assume that a newly capped tail has the same cardinality
or inherits raw optimality: the surplus comparison and the original
tail's delta n margin are used directly.

Care is needed with the phrase 'raw periodic core': a nonzero raw
valuation v_p on unbounded integers is not periodic. The hypothesis is
an actual bounded periodic component (for example one obtained by a
justified prime-profile cap), with the indicated one-sided comparison.
Merely writing a raw small-prime sum as S does not make it periodic.

## 9. A conditional replacement for residue conditioning

There is a relative exact-state estimate which avoids the product of
the small-prime moduli. It does not by itself transfer the entire core.

Let P0 be a finite set of primes at most y, let

    mu=sum_{q in P0}1/q,   k=|P0|<=y mu,

and fix an exact P0-state d=prod_{q in P0}q^{e_q}, with every e_q a
nonnegative integer. Let ell be coprime to every q in P0 and put
L=M/(d ell). Then, in every length-M interval I,

    #{b in I: d ell | b, v_q(b)=e_q for all q in P0}
       >= L(1-mu)-k-1.                                  (18)

Indeed there are at least L-1 multiples of d ell. A multiple has the
wrong exact state only if d ell q divides it for at least one q in P0.
For each q there are at most L/q+1 such positions. Subtract their union
by the sum of these upper bounds. This proves (18), including zero
coordinates e_q=0 and arbitrary powers in d.

In particular, if L>=y, then

    target exact-state count >=L(1-2mu)-1,               (19)

whereas the corresponding prefix count is at most L. Thus when
mu=o(1) and y tends to infinity the transfer has a relative o(1)
error, uniformly in d, ell and the interval shift. Different exact
states d are disjoint on the target side.

For the residual row argument, put N=M/(d p) and U=sqrt(N). At a
fixed price level let B be the eligible external partners q<=U,
q>y. The bank d p q has L=N/q>=U>=y, so (19) applies to every one
of its summands. Consequently its first moment restricted to the
exact state d is at least

    (1-2mu-1/U) N h,   h=sum_{q in B}1/q.

For an upper bound on the second moment one may drop the exact-state
condition and count multiples of d p q r. The same prime-counting
estimate used earlier gives the unit-error bound O(N h/log y).
Cauchy--Schwarz therefore gives the relative union estimate

    target exact-state union
       >=(1-O(mu+1/log y)) N h/(1+h).                    (20)

This remains relative when h tends to zero. Source counts are bounded
using multiples of d times the external products, so the previous
three/four-prime arithmetic majorants do not worsen when M is
replaced by M/d. This is a genuine conditional alternative to residue
conditioning for those residual banks.

It does not supply the missing general reduction. In the established
low-substantial-prime argument, mu=o(1) is available for

    P0={p<=M^{1/(s+1)}:w_p>=eta},
    s=floor(1/eta)+1,

with fixed eta and sparse source density. It has not been proved for
the entire weighted core up to M^{1/5}. Nor does (20) alone pay the
base and single-prime parts for all core states. A state matching
that disregards the external coordinates is insufficient: its
permutation of target positions need not preserve external prime
divisibility or the remaining target budget.

## 10. Exact limitations of the general reduction

The proof requires an actual core period Q=o(log M), with all remaining
nonzero prime weights on primes >M^(1/5). The product of all small-prime
moduli up to M^(1/5) does not satisfy that requirement. No proof that a
general positive global surplus optimum can be reduced to this setting
has been supplied here.

The base and single-prime payments have been transferred in Section 8
with error Q(r+Smax). This does not construct the required periodic core.

No o(M) repeated-source deletion is used in this corrected residual
certificate, so that particular sparse-scale obstruction is removed.
The relative row errors are uniform even for arbitrarily small h.
The remaining obstruction to the unrestricted result is the actual
core/diffuse-prime reduction and its single shared target budget.

### Why replacing an active core by its mean is not an available shortcut

Suppose S is a sum of genuinely balanced active prime coordinates of
the original optimum. Write F=sum_{b in I}z(b), |A|=n. Whole-row
balance gives

    sum_{a in A}S(a)=sum_{b in I}z(b)S(b).

For any nonnegative constant t define the two selected L1 errors

    E(t)=sum_{a in A}|S(a)-t|
             +sum_{b in I}z(b)|S(b)-t|.

Subtracting the two centered sums and using the triangle inequality
gives the exact necessary inequality

    E(t)>=(F-n)t.                                      (21)

At a positive surplus optimum F>(2+delta)n. Hence E(t)=o(n) would
force t=o(1), and then

    sum_A S <= n t+E(t)=o(n).

Thus a core carrying a positive proportion of the source weighted
demand cannot be replaced by a constant with o(n) error in both
selected budgets. This is an obstruction to that normalization
argument, not a counterexample to the requested asymptotic theorem.
Full-tail integrability and the existing price-band cleanup provide
O(n) bounds for the full discarded core; they do not turn this into
the o(n) estimate needed here. The 0.005 residual margin cannot absorb
an unspecified O(n) loss.

### A precise sufficient missing estimate

One does not need the stronger two-sided L1 approximation. It would
suffice to construct an admissible periodic-core load Y for which
Q(r+Smax)=o_delta(n), together with the one-sided comparison

    J_2(X)<=J_2(Y)+lambda sum_{b in I}R_Y(b)+o_delta(n),  (22)

where lambda<1-kappa=0.005, uniformly in M, the shift, and the genuine
optimal weights. Equation (17) would then imply J_2(X)<=o_delta(n),
contradicting J_2(X)>=J_(2+delta)(X)+delta n>delta n.
No proof of (22), or another unrestricted arithmetic replacement for
it, is supplied by the current certificate. In particular, neither a
small number of core primes nor their separate row balances is a
proof of (22).
