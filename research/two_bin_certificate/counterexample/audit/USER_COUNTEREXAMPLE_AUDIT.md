# Audit of the user's counterexample to full-prefix kernel transfer

24 November 2026. **Audit result: the construction is correct.**

It disproves the proposed full-prefix active-part inequality

    sum_{a<=M} K_{h(a)}(a) <= sum_{b in I} K_M(b),

with a positive deficit of order M^(10/17), and therefore also disproves a
uniform O(sqrt(M)) error in that assertion. It does not disprove the
full-tail/genuine-positive-optimizer estimate needed for Erdos 708. Both
pointwise parts of the two-bin lemma remain valid.

The construction is the user's. The refinements below make the prime-power
count, actual CRT interval, and small-weight perturbation fully explicit.

## 1. Parameters and the zero-background comparison kernel

Let p tend to infinity through primes and put

    W=floor(p^(10/7)), M=pW,
    Q={q prime: W^(31/100)<q<=W^(8/25)}.

Write alpha=31/100 and beta=8/25. Then

    p=W^(7/10)(1+o(1)), W<p^2, p^2>W,
    p q>W for every q in Q,
    q^2<W for every q in Q,
    (q r)^2>W for all q,r in Q, including q=r.

The strict inequality p q>W follows directly from p>=W^(7/10) and
q>W^(31/100), so p q>W^(101/100).

Temporarily let w_p=1, w_q=1/100 on Q, and every other price be zero.
For this temporary vector define K_L^0 by the usual divisor kernel at
the explicitly supplied scale L. The source comparison below uses K_a^0(a),
NOT K_{h_0(a)}^0(a). Later all background prices become positive, making
h(a)=a exactly. This order of operations is necessary because h is
discontinuous at zero prices.

For a divisor d supported on {p} union Q, use

    r_0(d)=max(0,min(min_{q|d} w_q,(X_0(d)-1)/Omega(d))).

## 2. Complete classification of nonzero main-price witnesses

At the target scale M, the only witnesses with r_0(d)>0 are

    d=pq, q in Q, in row p,

and their price is r_0(pq)=1/200.

Here are all cases, including repeated prime occurrences.

* A pure Q-divisor with k occurrences can be eligible in a row q only if
  d^2<=M q. If k>=4, its square is greater than W^(8 alpha)=W^2.48,
  whereas Mq=W^(1.7+beta+o(1))=W^(2.02+o(1)). Thus k<=3 for large p.
  Its load is at most 3/100<1, so its price is zero.

* A divisor containing at least p^2 is ineligible in row p, since even
  (p^2)^2/p=p^3>M. In a Q-row, its sub-divisor pq is already ineligible,
  because (pq)^2/q=p^2q>M is equivalent to p q>W.

* A divisor containing p and at least two Q-occurrences is ineligible in
  row p: d^2/p>=p(qr)^2>pW=M. It is ineligible in any Q-row by the
  preceding p q>W observation.

* A divisor pq is eligible in row p because q^2<=W. It is ineligible in
  row q because p q>W. The single divisor p has load exactly one and
  price zero. Single Q-primes also have price zero.

Consequently, for every positive integer b, no restriction on its size,

    K_M^0(b)=(1/200) v_p(b)
                 1_{p|b and some q in Q divides b/p}.              (1)

At source scale a=pt<=M, the witness pq is eligible exactly when

    q|t and q^2<=t.                                               (2)

Any paid source in (2) has v_p(a)=1: if p|t as well as q|t, then
t>=p q>W, impossible. Therefore

    S_0:=sum_{a<=M} K_a^0(a)
      =(1/200) #{t<=W: some q in Q divides t and q^2<=t}.           (3)

## 3. The source count

Let k=|Q| and write e_j(Q) for the elementary symmetric polynomial of
degree j in the numbers {1/q:q in Q}. In particular e_1=H_Q=sum_Q 1/q.

No number t<=W has four distinct Q-prime divisors, since their product
is greater than W^(4 alpha)=W^1.24. Every triple product is at most
W^(3 beta)=W^.96. Thus inclusion-exclusion terminates exactly at degree
three on the source interval:

    U_0:=#{t<=W: some q in Q divides t}
      =sum_q floor(W/q)-sum_{q<r}floor(W/(qr))
                         +sum_{q<r<s}floor(W/(qrs))
      =W(e_1-e_2+e_3)+O(k^3).                                   (4)

The delay q^2<=t deletes at most sum_q(q-1) positions. In particular the
loss is O(W^(2 beta))=O(W^.64)=o(W), using k<=W^beta. Floor errors are
O(W^(3 beta))=O(W^.96)=o(W).

The classical prime harmonic asymptotic gives

    H_Q -> mu=log(beta/alpha)=log(32/31).

Also sum_Q q^(-2)<=W^(-alpha) H_Q=o(1), so e_2->mu^2/2 and
e_3->mu^3/6. Hence

    S_0=(W/200)(mu-mu^2/2+mu^3/6+o(1)).                          (5)

A useful exact one-sided version of (4), including the delay, is

    200 S_0 >= W(e_1-e_2+e_3)-binom(k,3)-sum_Q q.                (6)

Indeed the positive floor errors from the subtracted pair counts need
not be charged. The k single-count rounding losses and the sum(q-1)
delay bound combine to sum q.

## 4. A genuine target interval and its exact CRT mean

Choose an integer x>=0 subject to x=0 mod p^2, and let

    I_x={p x+1,...,p x+M}.

Its p-multiples are p(x+t), 1<=t<=W. Since W<p^2 and x=0 mod p^2,

    v_p(p(x+t))=1+1_{p|t}.                                     (7)

This is exact: no term x+t in that range is divisible by p^2. Thus
arbitrarily large target p-adic exponents do not enter this construction.

Vary x uniformly through the CRT solutions to x=0 mod p^2 and all
independent residue choices modulo q, q in Q. These are actual integers
modulo p^2 product_Q q. For each fixed t, the probability that some Q-prime
divides x+t is exactly

    U_Q=1-product_Q(1-1/q).

No independence between different t is required. Equations (1) and (7)
give the exact mean

    E_x sum_{b in I_x}K_M^0(b)
       =(1/200)(W+floor(W/p)) U_Q.                             (8)

There is consequently an actual shift x with target sum no larger than
the right side. Since U_Q->1-exp(-mu)=1/32 and W/p=o(W), that interval
satisfies

    T_0:=sum_{b in I_x}K_M^0(b)
       <=(W/200)(1-exp(-mu)+o(1)).                             (9)

## 5. Positive deficit and an exact finite sufficient criterion

Combining (5) and (9),

    S_0-T_0 >= (kappa+o(1)) W,

where

    kappa=(1/200)[exp(-mu)-1+mu-mu^2/2+mu^3/6]>0,
    mu=log(32/31).

Taylor's integral remainder yields

    exp(-mu) mu^4/(24*200) <= kappa <= mu^4/(24*200).

For orientation only (positivity does not depend on floating arithmetic),

    mu = 0.0317486983145803011569962827485...,
    kappa = 2.1033455559795809053722827446... * 10^(-10).

The constant is very small but fixed and strictly positive. No claim is
made that moderate parameter sizes numerically witness the asymptotic.

There is also a finite expression that avoids replacing H_Q by its limit.
Set R_Q=e_1-e_2+e_3-U_Q. The Bonferroni inequalities give

    R_Q>=e_4-e_5>=e_4(1-H_Q/5).

Equations (6) and (8), and U_Q<=1, therefore imply for some actual x

    S_0-T_0 >= (1/200)[W(e_4-e_5)
                         -binom(k,3)-sum_Q q-floor(W/p)].       (10)

The main term tends to a positive constant times W; all displayed
subtractions are o(W). This supplies a direct sufficient arithmetic
certificate for each finite parameter choice if desired.

## 6. Making every source active without changing the conclusion

Fix the actual shift x selected above. Give every prime r<=M outside
{p} union Q the same positive weight epsilon, leaving the main prices
unchanged. Then h_epsilon(a)=a for every a<=M.

Every new divisor witness contains a background prime, so its price is
at most epsilon. Old main-only witnesses and their prices are unchanged.
For every fixed scale L and integer t,

    0<=K_L^epsilon(t)-K_L^0(t)<=epsilon Omega_{<=M}(t).          (11)

Here Omega_{<=M} counts all occurrences of primes at most M. Inactive
primes above M cannot occur in sources and have weight zero throughout.

Both finite sums

    B=sum_{a<=M}Omega(a)+sum_{b in I_x}Omega_{<=M}(b)

are finite after x is fixed. Given any fixed delta>0, choose

    0<epsilon<min(1/400, 1/(1+B), delta/(2 log_2 M)).           (12)

Then the total perturbation of either kernel sum is at most one, and

    sum_{a<=M}K_{h_epsilon(a)}^epsilon(a)
          -sum_{b in I_x}K_M^epsilon(b)
       >= (kappa+o(1))W-1.                                  (13)

The opposite bound is O(W), because (3) is at most W/200 and the source
perturbation is at most one, while the target is nonnegative. Thus the
positive deficit is Theta(W), not merely an unspecified unbounded error.

Finally W~p^(10/7), M~p^(17/7), so

    W~M^(10/17),
    W/sqrt(M)~M^(3/34) -> infinity.

This proves the claimed failure of (8), including its O(sqrt(M)) variant.

## 7. The full tail is empty and no optimizer claim is contradicted

For sufficiently large p, every source a<=M has X_0(a)<=2:

* v_p(a)>=3 is impossible, because p^3>M.
* If v_p(a)=2, it has no Q-prime factor, since p^2q>M.
* If v_p(a)=1, its cofactor is <=W and has at most three Q-occurrences,
  so X_0(a)<=1+3/100.
* If v_p(a)=0, it has at most five Q-occurrences for large p, because
  six have product greater than W^1.86>M=W^(1.7+o(1)); its load is <=5/100.

By (12), the background addition to any source is less than delta/2.
Therefore A={a<=M:X_epsilon(a)>2+delta} is empty.

In the full-tail identity, R_A=0 and

    Gamma=-sum_I K_M<=0,
    Gamma-R_A-R_I=-sum_I(X-1)_+=J_c<=0.

All positive full-prefix source payments in this counterexample lie
outside the actual upper tail. At a normalized genuine positive joint
optimizer, positive prices on zero-demand coordinates would be removed;
here that removes every coordinate. Thus neither the desired
full-tail estimate nor the original Erdos asymptotic is disproved.

## Audit conclusion

The user's argument is correct. The exact refinements (7)--(8) handle all
p-adic occurrences, (11)--(12) justify the tiny positive background prices
without a continuity mistake, and (10) provides a finite sufficient
criterion. Full-prefix transfer (8) should be retired as a research target.
The valid two-bin inequalities and the own-full-tail identity remain.

### Consequence for future small-weight cleanup

The map w -> K_{h_w(a)}^w(a) is not continuous when prices become zero.
Equation (11) controls a FIXED scale L, not the moving scale h_w(a).
For example, take a=p q s with q in Q, s>=q having only zero-background
prime factors, and a<=M. Before perturbation h_0(a)=p q and the witness
pq is not source-eligible; after arbitrarily small positive background
prices h_epsilon(a)=a, and that same witness is eligible with unchanged
price 1/200. The previous cleanup lemma for a small weighted demand
controls raw loads and raw objective values, but does not directly
control this moving-scale kernel. A valid revised argument may first
perform such cleanup with its raw budget, then construct the kernel
using the retained active support; it must not assume continuity of the
old kernel through the deletion.
