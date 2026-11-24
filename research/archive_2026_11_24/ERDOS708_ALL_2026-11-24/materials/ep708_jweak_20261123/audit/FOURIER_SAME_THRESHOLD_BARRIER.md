# An actual-interval barrier for a same-threshold capped-hinge discrepancy

## Exact scope

The theorem below disproves a universal bound polynomial in the number of
primes for the discrepancy of a capped hinge at the SAME threshold one on
the prefix and on a shifted interval. It strengthens the earlier observation
about exponential absolute divisor-coefficient variation by using actual
integer intervals.

It does **not** refute formula (91), J_weak, a source-threshold-two versus
target-threshold-one comparison, or a bound using actual minimal-obstruction
demands. The constructed parameter relation is recorded explicitly in
Section 5: its discrepancy is o(sqrt(M)), so it is harmless on its own at
the scale m>sqrt(M)/4 relevant to a minimal obstruction.

The Fourier derivation, symmetry argument and hinge conversion have passed
an independent internal audit by the combinatorial agent. No numerical
search or external publication is involved.

## 1. The precise statement

Let Q be the product of k distinct primes, let

    theta=phi(Q)/Q,
    Y(n)=sum_{p|Q} 1[p|n].

Thus Y is a per-prime capped load, not the unbounded raw valuation sum.
There exist an integer length `Q<=M<2Q` and a shift `0<=x<Q` such that

    sum_{n=1}^M (Y(n)-1)_+
       -sum_{n=x+1}^{x+M}(Y(n)-1)_+
      >= theta sqrt(2^k-1)/(2 pi)-k.                     (1)

Every support prime is at most M. Since ordered primes satisfy p_i>=i+1,

    theta=product_i(1-1/p_i)>=1/(k+1),                   (2)

the lower bound in (1) eventually exceeds every fixed polynomial in k.
There is consequently no universal O(k^2) bound for this same-threshold
auxiliary discrepancy without further hypotheses.

## 2. Periodic rough-count discrepancy

On the cyclic group of order Q, put

    f(n)=1[gcd(n,Q)=1],
    Phi(n)=sum_{j=1}^n f(j),
    S(n)=Phi(n)-theta n,   0<=n<=Q-1.

Because S(Q)=S(0)=0, extend S periodically. Its cyclic first difference
is `f(n)-theta`, including at n=0.

Use normalized Fourier coefficients

    hat{S}(a)=(1/Q)sum_{n=0}^{Q-1} S(n) exp(-2 pi i a n/Q).

For a nonzero frequency,

    hat{S}(a)
      = c_Q(a)/[Q(1-exp(-2 pi i a/Q))],                  (3)

where `c_Q(a)` is the Ramanujan sum of f. For each divisor d|Q with d>1,
the distinct frequency a=Q/d satisfies

    |c_Q(Q/d)|=phi(Q/d).

This identity follows directly by the Chinese remainder factorization of
the sum: a prime dividing Q/d contributes p-1, and a prime dividing d
contributes -1 in absolute value.

Since `sin(pi/d)<=pi/d`, equation (3) gives

    |hat{S}(Q/d)|
      >= [phi(Q/d)/(Q/d)]/(2 pi)
      >= theta/(2 pi).                                  (4)

There are 2^k-1 such nonzero frequencies. Parseval therefore yields

    Var_{n mod Q} S(n)
      >= theta^2(2^k-1)/(4 pi^2).                        (5)

## 3. A large POSITIVE prefix discrepancy

The reflection symmetry f(Q-n)=f(n), with f(0)=0, implies

    S(n)+S(Q-1-n)=theta.

Thus the mean of S is theta/2, and its distribution is symmetric about
that mean. Its largest positive deviation from the mean is at least its
standard deviation. There is some N with 0<=N<Q for which

    S(N)>=theta/2+theta sqrt(2^k-1)/(2 pi).               (6)

Take `M=N+Q`. Adding a whole period preserves the discrepancy, so

    Phi(M)-theta M=S(N).

This padding ensures all support primes are at most M; it also makes the
eventual parameter comparison transparent.

The average rough count over all Q shifted M-term intervals is exactly
theta M. Hence at least one shift x in [0,Q-1] satisfies

    sum_{n=x+1}^{x+M} f(n)<=theta M.

For this actual positive interval, the prefix-minus-interval rough-count
excess is at least S(N).

## 4. Convert the rough-count excess to the capped hinge

Since Y is integer-valued and nonnegative,

    (Y(n)-1)_+=Y(n)-1+f(n).                             (7)

For each prime p|Q, an M-term interval has either floor(M/p) or
floor(M/p)+1 multiples. The prefix has floor(M/p). Consequently

    0<=sum_{n=x+1}^{x+M}Y(n)-sum_{n=1}^M Y(n)<=k.

Combining this with (6)--(7) proves (1), even after dropping the additional
positive theta/2 term. Both hinges in this theorem are at threshold ONE.
No source-threshold-two inequality has been inferred.

## 5. Parameter relation and why this is not a J_weak obstruction

The theorem deliberately chooses M=N+Q, so Q<=M<2Q. By inclusion-exclusion,
the absolute rough-count discrepancy between two such intervals is at
most 2^k; adding the linear prime-count contribution bounds the absolute
hinge discrepancy by `2^k+k`.

Also the ordered-prime inequality p_i>=i+1 gives

    M>=Q>=product_{i=1}^k(i+1)=(k+1)!.

Therefore, uniformly in the actual prime values,

    |hinge discrepancy|/sqrt(M)
       <=(2^k+k)/sqrt((k+1)!) -> 0.                     (8)

The discrepancy is exponentially large compared with k^2 but still
o(sqrt(M)) along these constructed lengths. If it were placed next to
the actual-minimality scale m>sqrt(M)/4, it would be o(m), not a linear
obstruction to the needed asymptotic budget.

Furthermore the construction imposes none of the required source-load,
optimality, prime-demand or bank-balance conditions. It does not compare
the source hinge at 2+delta with the target hinge at one. It only rules
out a blanket SAME-threshold polynomial discrepancy claim detached from
those arithmetic and variational conditions.
