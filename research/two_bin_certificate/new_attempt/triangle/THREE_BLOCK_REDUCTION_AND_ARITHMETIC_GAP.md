# Three robust pairwise-hot factors and the missing arithmetic triangle inequality

24 November 2026. The three-block lemma below is proved for all weights
and all prime powers. The numerical interval triangle inequality is not
proved. In particular this note does not close the sparse branch or the
general asymptotic conjecture.

## 1. A robust three-block partition

Let a be a positive integer, let 0<=w_p<=1, and write

    X(t)=sum_p w_p v_p(t).

Fix delta>0. If U=X(a)>2+delta, there exist positive integers u,v,t with

    a=u*v*t,
    X(uv)>1+delta/2,
    X(ut)>1+delta/2,
    X(vt)>1+delta/2.                                   (1)

An empty factor is allowed to equal one. Every occurrence of every prime
is assigned to exactly one factor; no squarefree assumption is made.

**Proof.** List all positive-weight prime occurrences in nonincreasing
order of their weights. Put

    C=(3U-2-delta)/4.

Then

    C>1,        U<2C,        C<U-1-delta/2.             (2)

Pack the listed weights by first-fit decreasing into bins of capacity C.
Suppose a fourth bin must be opened for an item of weight x.

If x<=C/2, the three earlier bins each have load greater than C-x.
Together with x their total load exceeds 3C-2x>=2C, contradicting U<2C.

If x>C/2, each earlier bin contains its first item, whose weight is at
least x because the order is nonincreasing. These three items and the new
one have total weight at least 4x>2C, again a contradiction.

Thus three bins suffice. Assign the prime occurrences in the bins to
u,v,t, and distribute all zero-weight prime occurrences arbitrarily.
Every bin has load at most C. Consequently each complementary product
has load at least

    U-C=(U+2+delta)/4>1+delta/2,

proving (1).

The strict upper choice of C matters. Taking C=U-1-delta/2 would only
give weak inequalities at the desired pair threshold.

## 2. The arithmetic triangle set

For a threshold tau>1 define

    R_tau(M)={a<=M: a=u*v*t for some u,v,t>=1,
                         X(uv),X(ut),X(vt)>tau}.

For tau=1+delta/2, (1) gives

    {a<=M:X(a)>2+delta} subset R_tau(M).                (3)

The three hot divisors

    d_1=uv, d_2=ut, d_3=vt

satisfy the exact numerical relation

    d_1*d_2*d_3=a^2<=M^2.                              (4)

Thus at least one is at most M^(2/3). This reduction does not assert that
two are at most sqrt(M); a balanced triple of distinct primes shows why
that stronger numerical assertion would fail.

Let I be an arbitrary interval of length M and put

    K_tau=#{b in I:X(b)>tau}.

A sufficient new arithmetic estimate for the sparse branch would be

    |R_tau(M)| <= C_delta K_tau^(3/2)/sqrt(M)
                   +o_delta(n),                       (5)

on the genuine extremal class, or a corresponding bound with a uniform
O_delta(sqrt(M)) remainder. In the already-reduced subquadratic sparse
branch, K_tau<=K_1=O_delta(n), sqrt(M)=o(n), and n/M->0. Equations
(3)--(5) would then imply

    n <= O_delta(n sqrt(n/M))+o_delta(n)=o_delta(n),

a contradiction. This explains exactly why (5), if proved in this
arithmetic setting, would be sufficient for all of that sparse branch.

## 3. Why a direct invocation of Finner is not a proof

For fixed independent factor variables u,v,t, a Finner or Loomis--Whitney
inequality controls a triangle by the sizes of its three pair projections.
Here the uniform integer a<=M is not a product of three independent
variables. A factorization of a may be nonunique, and the region u*v*t<=M
is not a Cartesian product. Choosing the first-fit factorization removes
source multiplicity but does not make its projections independent.

More decisively, a projection consists of factor pairs (u,v) for which
uv is hot. Its cardinality is not K_tau, nor K_tau*UV/M for a dyadic box
u~U,v~V. Several pairs can have the same product, and the target interval
counts multiples of those products with intersections. Passing from
these projections to a single target cardinality is an additional
arithmetic inequality, not an application of Finner.

The short-window lemma only gives, for y<=M/2,

    #{d<=y:X(d)>tau} <= 8(K_tau*y/M)^2.                 (6)

Inserting this quadratic bound into a dyadic projection count does not
give the desired exponent 3/2. Even with divisor multiplicities omitted,
the product of three square-root projection bounds has scale

    (K_tau/M)^3 (UVT)^2 <= K_tau^3/M,

rather than K_tau^(3/2)/sqrt(M). Actual divisor multiplicities introduce
an additional issue. Therefore that calculation does not close (5).

## 4. Uniform floor errors in weighted bank second moments

One useful exact observation concerns a set of carriers h<=sqrt(M).
Assign nonnegative demands m_h and assume sum_h m_h<=n. Put

    alpha_h=m_h*h/M,
    Z(b)=sum_h alpha_h 1_{h|b}.

Every interval intersection satisfies

    #(I intersect hZ intersect kZ)
      <= M*gcd(h,k)/(h*k)+1.

Consequently the entire contribution of the '+1' errors to
sum_{b in I} Z(b)^2 is at most

    (sum_h alpha_h)^2 <= n^2/M.                        (7)

This is o(n) in the sparse regime n/M->0 and does not charge separate
root families independently. It remains valid with repeated carriers
represented by their total demand m_h.

However the main gcd contribution is

    (1/M) sum_{h,k} m_h m_k gcd(h,k),                    (8)

and is not controlled by (7). Coldness of a gcd does not imply that its
numerical size is O(M/n). Removing (8), or using its cold load against a
single shared payment budget, is a substantive remaining task.

## 5. Consequences of the existing minimal-hot overshoot dichotomy

This section is a consequence and sharpening of the earlier
`ep708_ladder_20261123/route_adaptive/ADAPTIVE_HALL_LADDER.md`, Section 5;
it is not presented as an independent closing route.

Let a satisfy S=X(a)>2+delta. Either a has a factorization a=h*k with
both X(h)>1 and X(k)>1, or it is E-free: no such factorization exists.
In the latter case all of the following assertions hold:

    S<=3;                                              (9)

    every inclusion-minimal hot divisor m|a has
       X(m)>=S-1,
       w_p>=X(m)-1>=S-2>delta for every p|m;           (10)

    deleting all prices <=delta preserves the hot
       predicate X(d)>1 for every divisor d|a;          (11)

    the entire deleted-price part of a has load <=1,
       and a has fewer than 3/delta retained
       prime occurrences.                             (12)

**Proof.** If S>3, accumulate prime occurrences until their load first
exceeds one. The resulting hot divisor has load at most two, since each
individual weight is at most one. Its complement has load greater than
one, contradicting E-freeness. This proves (9).

For a minimal hot m, its complement is cold, so X(m)>=S-1. Deleting any
one prime occurrence from m leaves a cold divisor. Thus
w_p>=X(m)-1>=S-2>delta, proving (10). Every hot divisor d|a contains such
a minimal hot m. All its prices survive deletion of prices <=delta,
so d remains hot. The converse follows from monotonicity, proving (11).

If the entire deleted-price factor of a were hot, it would contain a
minimal hot divisor consisting only of prices <=delta, contrary to
(10). Hence its load is at most one. Every retained occurrence has
weight greater than delta, and their total load is at most S<=3, giving
the strict occurrence bound in (12).

The statement includes all multiplicities and does not assume a bounded
factorization class in advance. If delta>=1, E-freeness is impossible,
because S>2+delta>=3 contradicts (9).

### Exact limitation of this cleanup

This is only a divisorwise threshold-one preservation theorem. It does
not preserve the full source tail X(a)>2+delta or the raw objective.
For example, set delta=1/10 and take seven distinct primes in a. Give
three occurrences weight 3/5 and the other four weight 1/10. Then

    X(a)=11/5>21/10.

The integer is E-free: a part with at most one large occurrence has
load at most 3/5+4/10=1; hence two disjoint hot parts would need at least
four large occurrences, while only three exist. All its hot divisors
contain at least two large occurrences. Deleting the four small prices
preserves precisely those hot divisors, but changes X(a) from 11/5 to
9/5 and removes a from the source tail.

One concrete realization is a=2*3*5*7*11*13*17, with large prices at
2,3,5. This is a local arithmetic example, not a positive global optimum
or a counterexample to the Erdős 708 asymptotic.

Consequently the low-price demand may be of order n over E-free sources.
No estimate of the form o(n) follows from (12). Nor is the threshold-one
predicate asserted to be preserved at arbitrary target integers that
combine primes from different sources. Any use in a global objective
must still retain the genuine paired balances and the exact pruning
loss.

## 6. Status

The robust three-block reduction and the joint floor-error bound (7)
are proved. No injective arithmetic counting map establishing (5) was
found, and no counterexample to (5) on genuine positive global optima was
found. An independent product/CRT-average calculation cannot replace the
uniform assertion for the actual given interval.

The dense branch remains separate. No numerical g(n) was computed.
