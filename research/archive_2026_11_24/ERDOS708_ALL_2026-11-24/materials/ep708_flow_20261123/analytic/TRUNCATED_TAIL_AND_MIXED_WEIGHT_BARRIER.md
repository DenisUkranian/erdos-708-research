# Truncated reciprocal tails: the constant-weight calculation and the exact mixed-weight barrier

## Status and scope

This note checks the last truncated-tail refinement of the rooted-star certificate. The refinement is valid and gives a uniform margin in the constant-weight calculation. The same local argument does not extend automatically to heterogeneous weights: an explicit family below has a sparse hot set, vanishing low-prime reciprocal mass, and weighted mean below one, while the proposed per-root exclusion cost exceeds one.

The family is **not** an optimal or minimal obstruction. It is not a counterexample to H_2 or J_weak. Its role is to identify the precise implication that is unavailable in the mixed-weight argument. J_weak remains unproved.

The underlying finite rooted-star certificate, including repeated occurrences and its exact source fibres, is proved in `WEIGHTED_ROOTED_STAR_CERTIFICATE.md` in this directory. The aggregate-low-cap comparison used in the sparse application is proved in `../audit/LOW_HEAVY_HINGE_COMPARISON.md` and `../audit/LOW_HEAVY_STATE_MATCHING.md`.

## 1. The reciprocal tail really can be truncated

For a carrier d, write T=M/d. In the earlier source upper bound, only prime powers at most T can occur in a source cofactor. Therefore the valid bound is

    sum_{t<=T} X_{>=p}(t)
      = sum_{r>=p} w_r sum_{j>=1} floor(T/r^j)
      <= T sum_{p<=r<=T} w_r/(r-1).                    (1)

No source is assumed to have a prime cofactor. The floor sum includes all inactive cofactors and all repeated prime occurrences. The upper endpoint r<=T is important.

## 2. One bounded low state and constant high weight

Fix b in (0,1] and put

    s=floor(1/b)+1,       y=M^{1/(s+1)}.

Let P_0 be any set of primes at most y, and let P_1 be any set of primes greater than y. Let U be a nonnegative additive raw load supported on P_0. Define

    alpha(n)=min(U(n),1),
    Y(n)=alpha(n)+b sum_{p in P_1}v_p(n).

Here alpha is one bounded **composite** state coordinate, not an additive prime coordinate. Suppose the reciprocal mass

    mu_0=sum_{p in P_0}1/p

tends to zero. All assertions below are uniform in the choice of these prime sets, the low weights, and the interval shift; b is fixed.

Every n<=M has at most s occurrences from P_1, because each such prime is strictly greater than M^{1/(s+1)}. Moreover,

    Y(n)>2
      implies Omega_{P_1}(n)=s,
      implies alpha(n)+b>1.                             (2)

Indeed, (s-1)b<=1. If there were at most s-1 high occurrences, Y(n)<=2. If there are s, then alpha(n)+sb>2 gives

    alpha(n)+b > 2-(s-1)b >=1.

Thus the first crossing after the low state occurs at the **first high occurrence**. There is only a base-root contribution; all later rooted-star contributions vanish. Their current piece plus right tail has load at most (s-1)b<=1.

Let l be the full P_0-part of n and let p be its least P_1 prime. The only relevant carrier and coefficient are

    d=l p,       h_l=alpha(l)+b-1 in (0,b].

Eligibility is stronger than T>=p:

    l p^s<=M,       T=M/(lp)>=p^{s-1},
    y<p<=M^{1/s}.                                     (3)

These statements include the case where all s high occurrences are copies of the same prime.

## 3. Exact root uniqueness survives the composite low cap

For every eligible pair (l,p), define

    Q_{l,p}=P_0 union {r in P_1:r<p},
    K_{l,p}(n)=1[lp|n]-sum_{r in Q_{l,p}}1[lpr|n].       (4)

The set Q_{l,p} includes low primes already dividing l; excluding them from n/(lp) fixes their exponents exactly.

If K_{l,p}(n)>0, then l is the full P_0-part of n and p is the least P_1 prime dividing n. Hence at most one pair (l,p) has a positive term at a given target. Its positive coefficient is h_l, which is at most (Y(n)-1)_+. Other pairs have nonpositive terms. Consequently

    sum_{eligible (l,p)} h_l K_{l,p}(n)<=(Y(n)-1)_+.     (5)

There is no sum of separate target budgets over possible low states.

For a source contributing to a particular carrier, put

    R=b sum_{r in P_1,r>=p}v_r(n/(lp)).

Its excess over two is (h_l+R-1)_+. Since n has at most s high occurrences, R<=b(s-1)<=1. Therefore

    (h_l+R-1)_+ <= h_l R.                               (6)

One may first retain the exact low-part and first-high-prime restrictions on n/(lp), and then drop them in this nonnegative upper bound. By (1), the total source contribution of this carrier is at most

    h_l b T sum_{p<=r<=T}1/(r-1).                       (7)

The same argument applies to a threshold 2+delta, with an additional nonnegative source subtraction; no stronger conclusion is needed here.

## 4. The uniform log(2) margin

Divisibility counts on every interval I of length M give

    sum_{n in I}K_{l,p}(n)
      >= T[1-mu_0-sum_{y<r<p}1/r]
           -( |P_0|+pi(p)+1 ).                          (8)

The sums over primes in (7)--(8) may be enlarged to all primes in the stated ranges. The rounding loss divided by T is o(1), uniformly in eligible carriers: by (3), T>=p and p>y, while |P_0|<=pi(y).

Write a=log p/log M. Then

    1/(s+1)<a<=1/s.

Mertens' reciprocal-prime estimate, together with T<=M/p, bounds the combined main-term loss in (7)--(8) by

    mu_0 + f_{s,b}(a)+o(1),
    f_{s,b}(a)=log((s+1)a)+b log((1-a)/a).               (9)

The error is uniform on this closed exponent range for fixed s. Replacing 1/(r-1) by 1/r costs o(1), because every such r exceeds y.

For s=2, one has b<=1 and a in [1/3,1/2]. The expression is increasing in b, so

    f_{2,b}(a)<=log(3a)+log((1-a)/a)
               =log(3(1-a))<=log 2.

For s>=3, b<=1/(s-1), and

    d f_{s,b}(a)/da = (1-b-a)/(a(1-a))>=0.

Thus

    f_{s,b}(a)
      <=log((s+1)/s)+b log(s-1)
      <=log(4/3)+1/e < log 2.                            (10)

The elementary bound log t/t<=1/e was used in the last step. Equations (9)--(10) leave the fixed positive margin 1-log 2. Consequently, for sufficiently large M, every source upper bound (7) is paid by its signed target average (8). Summing and using (5) proves the corresponding H_2 comparison for Y.

This calculation explains why the truncated tail is materially stronger than the untruncated harmonic tail. It does not by itself handle different high weights.

## 5. What fails for heterogeneous high weights

Keep the substantial-weight cutoff eta=1/10, so s=11 and y=M^{1/12}. If high weights vary in [eta,1], a positive source need not have s high occurrences. A low state alpha=1/10 and two high weights equal to one already give total load 21/10.

Thus implication (2) fails. In particular, p^s<=M is no longer available. The smaller weights that precede a large root weight can have a large **unweighted** reciprocal mass, even though their weighted reciprocal mass is small.

The following family shows that adding the coarse sparse-hot and weighted-mean conditions does not repair this individual-carrier estimate.

### An explicit asymptotic family

Fix beta in (0,1/12). For each sufficiently large integer M, choose primes

    q ~ M^beta,
    p ~ M^{1/3}, with p greater than M^{1/3}.

Give q weight 1/10. Give every prime r in

    M^{1/10}<r<M^{1/3}

weight 1/10, and give p weight one. All other weights are zero. The existence of such asymptotic choices follows from the usual prime asymptotics; a fixed-factor choice for q would also suffice.

Use the actual interval I={1,...,M}. The primes q and p are outside the middle band. Every n<=M has at most nine band occurrences, because ten primes strictly greater than M^{1/10} have product greater than M. Thus the band load alone is at most 9/10. It follows that the raw hot set satisfies

    {n<=M:X(n)>1} subset {n:q|n} union {n:p|n},
    h/M <=1/q+1/p ->0.                                  (11)

The only active prime below y is q, so its unweighted reciprocal mass tends to zero. The full weighted reciprocal mean satisfies

    sum_r w_r/(r-1)
       -> (1/10) log(10/3) <1.                          (12)

Nevertheless, the valid source

    a=q p^2<=M

has load 21/10. Its low state is alpha(a)=1/10, its first-crossing root is d=qp, and its positive excess over two is 1/10. The corresponding unweighted prefix exclusion contains the entire middle band. Hence

    sum_{M^{1/10}<r<M^{1/3}}1/r -> log(10/3)>1.           (13)

The local first-order condition is already violated before adding the nonnegative weighted tail and rounding terms. Truncating that tail cannot fix (13).

Every middle-band weight here is **substantial** relative to eta=1/10. It must not be described as a diffuse or below-cutoff weight.

### A finite arithmetic instance of the same failed criterion

Take M=5,000,000, q=3, p=173, weight w_3=1/10, w_173=1, and weight 1/10 on every prime from 5 through 167. Then

    y=M^{1/12}=3.61615885...,
    a=3*173^2=89,787<=M,
    X(a)=21/10,
    d=519,
    sum_{5<=r<173, r prime}1/r=1.0782907237...>1,
    sum_r w_r/(r-1)=0.1741969022...<1.

These inequalities were checked by exact rational summation; the displayed decimals are only for readability. There are 37 middle-band primes. Since 5^10=9,765,625>M, that band alone again has load at most 9/10 on the prefix. The finite example illustrates the local failure; (11) establishes actual sparse-hot behavior for the asymptotic family.

## 6. What the example does and does not establish

The example refutes the inference

    sparse hot set + vanishing low mass + weighted mean below one
       => every mixed rooted carrier satisfies the first-order
          prefix-plus-truncated-tail inequality.

It does not refute any desired global hinge comparison. In fact, the example uses I={1,...,M}, where the global source-threshold-two versus target-threshold-one comparison is immediate.

It is not asserted to satisfy the exact active-row balances of an optimal raw solution, the minimal-failure source-load conditions, or the source cardinality needed for an obstruction. Those additional conditions could still force compensation between the roots, but no such compensation has been proved here.

There is also a relevant reduction caveat: removing the low q contribution from the particular source a leaves p^2 with load exactly two, so its positive source excess disappears. Capping the low state at one does not itself remove q (the state on a is still 1/10), but a further permitted deletion or treatment of that low contribution might do so. Therefore the example must not be presented as a counterexample to a separate residual-heavy-load theorem after such a modification.

The exact remaining issue is the mixed-weight transfer between roots, with the single target hinge budget and the actual optimal-row balances retained. The constant-weight log(2) margin and the failed mixed local criterion identify that issue; they do not resolve J_weak.

## References for the standard prime estimates

The only asymptotic prime inputs in this ancillary note are the usual existence of primes on fixed power scales, pi(x)=O(x/log x), and Mertens' reciprocal-prime estimate. They are the same inputs already sourced in the main continuation report. See T. Tao, [Mertens' theorems](https://terrytao.wordpress.com/2013/12/11/mertens-theorems/), and A. Granville and K. Soundararajan, [author-hosted text](https://dms.umontreal.ca/~andrew/PDF/Book.To1.4.pdf), Chapter 1.
