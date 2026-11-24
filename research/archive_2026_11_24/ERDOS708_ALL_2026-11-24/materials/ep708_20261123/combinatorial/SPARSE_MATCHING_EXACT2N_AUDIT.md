# Audit: sparse-support prime-quotient matching implies an exact 2n cover

Date: 2026-11-23 (Kyiv). Parent's matching argument: PASS.

## Hypothesis and the sharpened finite criterion

Let `P={p_1<...<p_k}` be finite, `p_1>=y>=2`, and write

`pi_P(t)=#{p in P:p<=t}`,

`mu_0(P<=t)=sum_{p in P,p<=t}1/p`.

It suffices that

`C_y(P):=sup_{t>=y}[mu_0(P<=t)+(2pi_P(t)+1)/t] <= 1`.              (1)

This supremum is the finite expression

`max(1/y, max_{1<=j<=k}[sum_{i<=j}1/p_i+(2j+1)/p_j])`.

Between consecutive support primes the numerator count and reciprocal
sum are constant, and the remaining term decreases. The displayed
formula also covers the initial interval before `p_1`.

The simpler condition `mu_0(P)+rho_y(P)+tau_y(P)<=1` implies (1), where

`rho_y(P)=sup_{t>=y}(pi_P(t)+1)/t`,

`tau_y(P)=sup_{t>=y}pi_P(t)/t`.

In turn, `mu_0(P)+2rho_y(P)<=1` is sufficient.

## 1. Hall for the largest-prime quotient graph

Fix an interval `I` of `M` positive consecutive integers. Let `A` be
any set of distinct `P`-smooth integers in `[2,M]`. For a composite
source `a`, give it all target neighbors `b in I` divisible by

`d(a)=a/Pmax(a)`.

Consider any subset `S` of the composite sources and its distinct
quotient set `D={d(a):a in S}`. Every `d in D` is composite or prime,
is greater than one, and satisfies

`d*Pmax(d)<=M`.

Indeed, the removed prime `p=Pmax(a)` is at least `Pmax(d)` and
`dp=a<=M`.

For a target integer `b in I` set

`K_D(b)=sum_{d in D}[1_{d|b}-sum_{p in P,p<=M/d}1_{dp|b}]`.

At most one summand is positive. Such a summand forces

`d=smooth_{P intersect [2,M/d]}(b)`.

The right side decreases as `d` increases, so there cannot be two
distinct fixed points. Outside the union of the divisibility
neighborhoods every summand vanishes. Hence, pointwise,

`K_D(b)<=1_{b in N(S)}`.

Writing `t=M/d`, interval counting gives

`|N(S)|>=sum_{d in D}[t(1-mu_0(P<=t))-pi_P(t)-1]`.

Under (1), each bracket is at least `pi_P(t)`. On the other hand,

`|S|<=sum_{d in D}pi_P(M/d)`,

because each source with quotient `d` has the form `dp` for a support
prime `p<=M/d`. Consequently `|N(S)|>=|S|`. Hall's theorem gives an
injective assignment for all composite sources.

Prime sources have quotient one and are adjacent to every target. They
can be assigned afterward to unused targets: `|A|<=M-1`, so there are
enough targets remaining. Thus all sources admit distinct assigned
targets `b_a`, each divisible by `a/Pmax(a)`.

## 2. The repair argument

Let `n=|A|`, `B_0={b_a:a in A}`, and

`Q=product_{a in A}(a/Pmax(a))`.

Then `|B_0|=n` and `Q|product B_0`. The total number of missing prime
valuation units relative to `product A` is therefore at most `n`,
because `product A/Q` is a product of exactly `n` primes with
multiplicity.

The full interval product is divisible by `M!`, while `product A`
divides `M!` since `A` consists of distinct integers in `[1,M]`.
Whenever the current chosen product is short in a prime valuation,
some unused target contains that prime; otherwise the full interval
would have the same deficient valuation. Add one such target. This
reduces the total remaining deficit by at least one and cannot
increase any deficit.

After at most `n` additions the chosen target product is divisible by
`product A`, and the number of distinct chosen targets is at most
`2n`.

Thus (1) proves an exact, unconditional `2n` cover for this support
class, for every interval length and every positive shift.

## 3. Asymptotic support class

For any fixed `delta>0`, all sufficiently large minimum support primes
and `sum_{p in P}1/p<=1-delta` satisfy (1), because

`sup_{t>=y}(2pi(t)+1)/t -> 0`.

Unlike the H2 transfer, the proof above gives the exact bound `2n`
directly in this class. It does not cover arbitrary prime supports and
does not prove the unrestricted problem.

## 4. Parent's cofactor-support refinement

Let `P` be the prime support of the sources, but let `Q` be only the
union of prime supports of the composite-source quotients
`a/Pmax(a)`. The fixed-point certificate in Section 1 needs to exclude
only primes from `Q`, because every divisor in `D` is `Q`-smooth.
The number of source preimages of a quotient is still bounded by
`pi_P(M/d)`. Thus the sufficient criterion improves to

`sup_{t>=min Q}[mu_0(Q<=t)+(pi_Q(t)+pi_P(t)+1)/t] <= 1`,          (4)

or, more simply,

`mu_0(Q)+sup_{t>=min Q}(pi_Q(t)+pi_P(t)+1)/t <= 1`.

The empty-`Q` case, in which every source is prime, is handled directly
by quotient-one matching followed by prime-unit repairs.

Every `q in Q` satisfies `q<=sqrt(M)`: if `q` divides a quotient
`a/p` with `p=Pmax(a)`, then `q<=p` and `q^2<=qp<=a<=M`.

Consequently, for any fixed

`alpha>1/(2e)`,

all sufficiently large `M` satisfy an exact `2n` cover theorem for
every distinct source set whose prime factors are all at least
`M^alpha`. Indeed,

`Q subset [M^alpha,sqrt(M)]`,

`mu_0(Q)<=log((1/2)/alpha)+o(1)<1`,

and the density-error term in (4) tends to zero uniformly for
`t>=M^alpha`. The case `alpha>=1/2` is immediate or has empty `Q`
apart from a possible square at the boundary.

This refinement is valid and strictly improves the rough-support
exponent obtainable by applying the full-support criterion directly.

## 5. Exact coprimality can absorb an arbitrary fixed set of small anchors

Let `Q` be a finite anchor-prime set and let `R` be disjoint, with all
primes of `R` at least `y>max Q`. In this section restrict the matched
composite sources to those containing an `R` prime. Their removed
largest prime lies in `R`, so every associated quotient `d` has
`T=M/d>=y`.

Write `delta_Q=product_{q in Q}(1-1/q)` and `C_Q=2^|Q|`. For a quotient
family `D` use

`K_D(b)=sum_{d in D} 1[d|b] 1[gcd(b/d,product Q)=1]`
`                  *[1-sum_{r in R,r<=M/d}1[r|b/d]]`.

Any positive summand forces

`d=smooth_{Q union (R intersect [2,M/d])}(b)`.

The same monotone fixed-point argument shows uniqueness, so
`K_D<=1_{N(S)}`. Counting coprime integers by Möbius inversion gives

`|N(S)|>=sum_{d in D}[delta_Q T(1-mu_0(R<=T))`
`                          -C_Q(pi_R(T)+1)]`.

Every quotient has at most `pi_R(T)` source preimages. Thus

`delta_Q[1-mu_0(R)] >= C_Q rho_y(R)+tau_y(R)`                      (5)

suffices for Hall. For fixed anchors and fixed positive mass margin,
(5) holds for all sufficiently large `y`.

As before, the negative exclusion set can be reduced to the union `R_0`
of non-anchor primes in the quotients, while the preimage prime count
uses `R`. Hence one may replace (5) by

`delta_Q[1-mu_0(R_0)]`
` >= sup_{T>=y}[C_Q(pi_{R_0}(T)+1)+pi_R(T)]/T`.                   (6)

Here `R_0 subset [y,sqrt(M)]`.

Prime sources containing `R` can be assigned to unused targets after
the composite-source matching. If `n_R` sources contain an `R` prime
and the remaining source subset is `A_Q`, the matching and prime-unit
repairs yield a cover of size at most

`2 n_R + sum_{a in A_Q}Omega(a)`.

There is no overlap issue in this estimate: begin with the `n_R`
assigned cofactor targets, then repair all still-missing prime
valuation units relative to the product of the entire source set.
Their total is at most `n_R+sum_{a in A_Q}Omega(a)`. The full interval
product covers that entire source product, so every needed unit can
be supplied by an unused target.

For fixed `Q`, the last sum is `O_Q((log M)^(|Q|+1))`. In the remaining
regime `M<=16n^2`, it is `o(n)`. Combining (6) with the cofactor cutoff
therefore proves a restricted asymptotic `2n+o(n)` class in which every
source prime is either in a fixed finite set `Q` or at least
`M^alpha`, for any fixed `alpha>1/(2e)`. The large-`M` regime is covered
by the already known `2n` theorem cited in the main research notes.

This extension still leaves the intermediate prime ranges untreated.
