# Full-prefix cofactor transport: exact cut structure and its conditional implication

## Status

The proposed asymptotic transport statement is

    D(M,I)=o(M) uniformly over M-term intervals I,         (A)

where D is the maximum Hall deficiency of the graph defined below. No proof or counterexample to (A) was obtained in this audit. The exact injection is false. No estimate for the high-tail deficiency on the smaller n scale is proved here.

## 1. The full graph and its extremal cuts

The source vertices are [2,M]. A source a is adjacent to b in I if

    a/q divides b for at least one prime q dividing a.

Let N(S) be the union of all such neighbors and put

    D(M,I)=max_{S subset [2,M]} (|S|-|N(S)|)_+.

The matching deficiency is exactly D(M,I). Omitting or adjoining the conventional universal source 1 changes this by at most one.

**Divisibility closure.** If a divides a', then

    N(a') subset N(a).

Indeed, for a witness prime q of a', if q divides a then a/q divides a'/q. If q does not divide a, then a divides a'/q and any prime deletion of a divides it as well.

Consequently a source set maximizing a positive Hall deficiency must be upward closed under divisibility in [2,M]. Adding a missing multiple changes no neighbor union and increases the deficiency. Such a set contains no primes: a prime has cofactor one and is adjacent to the entire interval.

For an extremal upset S and its complement C=[1,M]\S, C is divisor closed, contains 1 and all primes, and

    |S|-|N(S)|=|I\N(S)|-|C|.                            (1)

These exact restrictions do not yet bound the right side by o(M).

## 2. What the examined primary sources establish

Chen's main manuscript, Proposition labelled `prop:false`, part (a), gives an actual length-20000 interval with 2270 integers free of every prime at most 10000, whereas pi(20000)+1=2263. This disproves a perfect full-prefix prime-deletion transport. The quoted proposition does not give an asymptotic upper bound for its Hall deficiency.

Local source: `ep708_20261122/analytic/chen-main.tex`, subsection “Three strengthenings that fail”.

The related van Doorn–Li–Tang paper proves a different result: for arbitrary n fixed moduli and an open interval of length twice their maximum, the exact guaranteed matching size is min(n,ceil(2 sqrt(n))). Therefore merely retaining distinct cofactors at most M/2 is insufficient for a near-perfect global matching. A proof of (A) would have to use all prime deletions and their relation to the original prefix sources.

Primary reference: W. van Doorn, Y. Li and Q. Tang, *Optimal bounds for an Erdős problem on matching integers to distinct multiples*, arXiv:2603.28636v1, Theorem 2.1 and Section 3, https://arxiv.org/html/2603.28636v1 . This is the matching problem #650, not a resolution of #708.

No theorem proving (A) was located in the examined primary material. This is a limited search statement, not a claim that all literature has been exhausted.

## 3. The correct direct hinge implication

Let 0<=w_p<=1, c=2+delta, and

    A={a<=M:X_w(a)>c},  n=|A|.

Restrict any full-prefix matching to A. At most t<=D(M,I) of these sources are unmatched. For each matched source choose its witnessing deleted prime q. Distinct assigned targets satisfy

    (X_w(b)-1)_+ >= X_w(a)-2
                       =(X_w(a)-c)+delta.

Summing gives the exact estimate

    J_c(w)
      <=sum_{a unmatched}(X_w(a)-c)-delta(n-t)
      <=sum_{a unmatched}X_w(a)-delta(n-t).              (2)

This uses the target hinge only once per distinct matched target. It does not combine independent product covers or spend the same valuation twice.

If mu=sum_p w_p/(p-1) is bounded, the elementary prefix second moment gives

    sum_{a<=M}X_w(a)^2 <= M(mu^2+2mu).

To verify it, expand positive prime-power indicators. The diagonal contribution for one p is w_p^2(p+1)/(p-1)^2, and the cross-prime terms are bounded by their geometric means. The result is mu^2+sum_p w_p^2 p/(p-1)^2<=mu^2+2mu.

Therefore

    J_c(w)<=sqrt((mu^2+2mu)Mt)-delta(n-t).               (3)

In the dense regime n>=rho0 M, a uniform t=o(M) would make the first term o(M), and (3) would exclude a positive surplus for fixed delta,rho0>0. This is a conditional implication of (A), not its proof and not a completion of the full problem.

In the sparse regime, t=o(n) alone is not enough for this argument. A useful sharper subset bound is

    sum_{a in T}X_w(a)
       <= |T|/log(3/2) * [log(M/|T|)+mu],

which follows from the previously established positive-divisor MGF bound. Thus it would suffice that

    (t/n)[log(M/n)+log(n/t)+O(1)] ->0,                  (4)

or, directly, that the unmatched weighted source load is o(n). The weaker cardinal statement t=o(n) does not automatically imply (4) when M/n diverges.

## 4. A repair claim that is not used

A separate linear-size product cover of the unmatched sources cannot simply be united with selected cofactor carriers: their common target valuations may be counted twice. A valid integer augmentation would require an additional extension argument.

Equations (2)--(4) avoid that issue by working directly with the raw hinge. No independent-cover repair estimate is asserted here.

## Remaining obligation

The arithmetic task left by this route is a quantitative bound for all divisibility-upset Hall cuts, using their complete prime-deletion neighborhoods. The finite rough-number counterexample and fixed-modulus matching theorem do not settle that asymptotic task. No bound D=o(M), no sufficient sparse weighted-deficiency bound, and no uniform J_c<=C_delta theorem is claimed.
