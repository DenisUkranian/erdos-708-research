# Prime banks and a sparse light-prime band in a minimal counterexample

Date: 2026-11-23. Research note; no priority claim. These lemmas do not
settle unrestricted Erdős problem 708.

## 1. Fixed-ambient minimality

Fix an integer `M`, a positive interval `I` of `M` consecutive integers,
and a distinct source set `A subset [2,M]`, with `|A|=n`. Write

`K=2n-1`, `D_p(A)=sum_{a in A}v_p(a)`.

Assume that `A` has no cover using at most `2n` positions, but each
`A\{a}` has a cover `B_a subset I` of size at most `2n-2=K-1`.
This is the only minimality hypothesis used below. It follows, for
example, from induction on cardinality with the ambient length `M`
held fixed. Full-interval supply is always available because

`product A | M! | product I`.

Any remaining single prime-valuation unit can therefore be supplied
by an unused interval position.

## 2. Forced prime banks

For a prime occurrence `q|a`, let

`C_q(a)={b in I: a/q divides b}`.

Then every cover `B_a` as above contains all of `C_q(a)`. Otherwise
add a fresh multiple of `a/q`; at most one `q`-unit remains missing,
and one further unused position supplies it. This would cover `A`
using at most `2n` positions.

Since `|C_q(a)|>=floor(M/(a/q))>=q`, every source prime satisfies

`q<=K-1<K`.                                                     (2.1)

The same argument with an entire source gives `N_I(a)<=K-1`, hence

`a>M/K`.                                                       (2.2)

Moreover every prime quotient satisfies

`a/q>M/K`,                                                     (2.3)

because otherwise its bank would have at least `K` positions.

## 3. Two-prime removal and full-demand saturation

### Lemma

Let `p,q` be two prime occurrences in `a` (they may be equal), so
`pq|a`. If `pq>=K`, then

`D_p(A)>v_p(product C_q(a))`

and consequently

`D_p(A)>v_p(a/q) floor(M/(a/q)) >= q v_p(a/q)`.                  (3.1)

### Proof

If the first strict inequality failed, the forced inclusion
`C_q(a) subset B_a` would mean that `B_a` already supplies the full
`p`-demand of `A`.

There are at least `pq>=K` interval multiples of `a/(pq)`, whereas
`|B_a|<=K-1`. Choose one fresh multiple `b`. The product on
`B_a union {b}` supplies every demand of `A` except possibly one
`q`-unit: the `p`-demand is already fully supplied, and all other
prime factors of `a` occur in `a/(pq)`. One unused `q`-bearing target
finishes the cover. If `p=q`, the entire `p`-demand is already supplied
and even this last repair is unnecessary. Either case contradicts
the assumed counterexample. The valuation lower bound follows because
each bank member contains `a/q`.

The implication is not justified merely by bank inclusion. The fresh
`a/(pq)` multiple and the one-unit repair are essential to its proof.

## 4. A directly checkable all-scale sufficient class

### Theorem

Suppose that for every `a in A`, either `Omega(a)<=2`, or there are
two prime occurrences `p,q` in `a` satisfying

`pq>=2n-1`, `D_p(A)<=q v_p(a/q)`.                              (4.1)

Then every positive interval of length at least `max A` has a product
cover using at most `2n` positions. No upper bound on `Omega` of the
sources in the second case is required.

### Proof

Induct on `n` at fixed ambient interval length. The hypothesis is
hereditary: deletion reduces the total demands and the threshold
`2n-1`. Obtain a cover of `A\{a}` with at most `2n-2` positions.
If `Omega(a)<=2`, supply its at most two missing prime units.

Otherwise, if `C_q(a)` contains a fresh target, add that target and
at most one `q`-unit repair. If the entire bank is already selected,
(4.1) says the full `p`-demand has been supplied; use the construction
in Section 3. In each case at most two additional positions suffice.

This theorem is a restricted all-scale class, not an unrestricted
solution. Condition (4.1) is sufficient, not necessary.

## 5. A sublinear core and at most one light-prime occurrence per source

Under the minimal-counterexample hypotheses of Section 1, define

`E={source primes p:p<=sqrt(K)} union {source primes p:D_p(A)>p}`,

`R={all other source primes}`.

Then every source contains at most one occurrence of a prime from
`R`; in particular, that occurrence has exponent one.

Indeed, suppose a source contained two `R` occurrences `p<=q`.
Both exceed `sqrt(K)`, so `pq>K`, while

`D_p(A)<=p<=q<=q v_p(a/q)`.

This contradicts (3.1), including the repeated-prime case `p=q`.

In fact, an `R` prime is the unique largest prime of its source. If
`r in R` and another prime occurrence `q>=r` occurred in the same
source, even with `q in E`, then `rq>K` and
`D_r(A)<=r<=q v_r(a/q)`, again contradicting (3.1). Thus a source
containing `r in R` has the form `a=r d`, where `d` is `E`-smooth and
`Pmax(d)<r` (with the natural convention when `d=1`). This strengthening
was observed in the independent analytic audit.

Let `H={p:D_p(A)>p}` and `h=|H|`. Since the primes in `H` are distinct,

`h(h+1)/2 <= sum_{p in H}p < sum_pD_p(A)`

and

`sum_pD_p(A)=sum_{a in A}Omega(a)<=n log_2 M`.

Thus

`|E|<=floor(sqrt(K))+sqrt(2n log_2 M)`.                          (5.1)

In the range `M<16n^2`, which remains after the known quadratic
long-interval theorem, this is `O(sqrt(n log n))=o(n)`.

The forced-bank restriction (2.1) also gives

`R subset (sqrt(K),K)`.

Consequently the reciprocal-prime asymptotic implies

`sum_{r in R}1/r <= log 2+o(1)<1`.                              (5.2)

Equations (5.1)--(5.2) are a structural reduction: any such minimal
counterexample consists of a growing but sublinear prime core, plus
at most one simple light-prime occurrence per source from a band of
reciprocal mass below one. The existing fixed-anchor certificate does
not handle the growing core: its exact coprimality error contains an
exponential factor in the number of anchors. No fractional-cover or
rounding conclusion follows from (5.1)--(5.2) alone.

## 6. Forced unions and valuation lower bounds

Put

`C(a)=union_{q|a, q prime} C_q(a)`,

`L(a)=1+sum_{q|a, q prime}(q-1)`, `t=floor(M/a)`.

Two distinct prime banks intersect exactly in the multiples of `a`,
because `lcm(a/p,a/q)=a` for distinct primes `p,q`. Therefore

`|C(a)|=sum_{q|a}N_I(a/q)-(omega(a)-1)N_I(a)`.

In every complete residue period of length `a`, the union has exactly
`L(a)` members. Hence

`t L(a)<=|C(a)|<=K-1`.                                         (6.1)

For a fixed `p|a`, write `e_p=v_p(a)`. The same residue-period
decomposition gives the valuation bound

`v_p(product C(a)) >= t[e_p L(a)-(p-1)] =: F_p(a)`.              (6.2)

The `p-1` nonzero multiples of `a/p` modulo `a` each have valuation
`e_p-1`; all other bank residue classes have valuation at least
`e_p`. Contributions from additional factors in the residue
representatives can only improve this bound.

Since `C(a) subset B_a`, a necessary condition for a counterexample is

`sum_{p|a} min(e_p, (D_p(A)-F_p(a))_+) >= 3`.                    (6.3)

Otherwise the cover of `A\{a}` would have at most two remaining prime
units, each supplied by one unused target.

If `Omega(a)=3`, every cover `B_a` must have exactly the other-source
valuation at each prime of `a`:

`v_p(product B_a)=D_p(A)-e_p`.

In particular (6.2) implies

`D_p(A)>=F_p(a)+e_p`.                                          (6.4)

For a squarefree triple `a=pqr`, this includes
`D_p(A)>=floor(M/a)(q+r-1)+1`, and cyclically. These are necessary
conditions only; their aggregation has not yet ruled out the general
counterexample class.

## 7. Budget generalization and a justified asymptotic obstruction reduction

The structural argument also applies to a linear budget

`L(n)=c n+C`, with `c>=2`, `C>=0`.

Suppose `A` is a failing instance at cardinality `n`, while deleting
any source leaves a cover of size at most

`floor(c(n-1)+C)=K-1`.

Use this definition of `K` in Sections 2--3 and 5. Adding two targets
would use at most

`K+1=floor(c(n-1)+C)+2 <= floor(cn+C)`,

so every forcing and two-prime-removal contradiction remains valid.
In particular all source primes are below `K`, and with

`E={p<=sqrt(K)} union {p:D_p(A)>p}`,

every source contains at most one occurrence from `R=P\E`.

To apply this to a possible failure of the unrestricted asymptotic
conjecture, one must do more than choose a smallest exact-`2n`
counterexample. Assume for some fixed `c=2+epsilon`, `2<c<10`, that
there is no finite `C` for which `g(n)<=cn+C` for all `n`. For each
`C->infinity`, choose a globally smallest failing cardinality `n_C`
and an actual instance with `M=max A`. A cover of any deletion follows
from the smaller-cardinality budget, embedded into the original
interval if necessary.

The known uniform upper bound `g(n)<=10n` gives

`C<(10-c)n_C`,

so `n_C->infinity` and `K=O(n_C)`. The known exact long-interval
theorem forces `M<16n_C^2`, because otherwise `tau<=2n_C<=cn_C+C`.
Thus the heavy-core estimate gives

`|E|=O(sqrt(n_C log n_C))=o(n_C)`,

while

`R subset (sqrt(K),K)`, `sum_{r in R}1/r<=log 2+o(1)`.

Every source has at most one simple `R` factor. This establishes the
stated structural reduction for a possible asymptotic obstruction
family, using explicit external inputs `g(n)<=10n` and the quadratic
long-interval gate. It does not prove that the growing core can be
absorbed into a coefficient-two cover. The exact and asymptotic
minimality arguments are therefore distinguished rather than
silently identified.

The unique-largest-prime conclusion from Section 5 also persists in
this generalized-budget reduction.

## 8. Sharper core size and negligible harmonic mass of its large primes

In the same remaining range, use the logarithmic demand budget

`sum_{p in H} p log p < sum_p D_p(A)log p`
`                         =sum_{a in A}log a <=n log M`,       (8.1)

where `H={p:D_p(A)>p}`. Chebyshev's prime-counting bound implies
`p_j>=c j log(j+1)` for the `j`-th prime, with an absolute positive
constant. Therefore the sum of `p log p` over any `h` distinct primes
is at least `c' h^2 log^2(h+1)` for another absolute constant.

When `M<16n^2`, (8.1) consequently gives

`|H|=O(sqrt(n/log n))`.

For example, separate `h<n^(1/4)`, where this is immediate for large
`n`, from `h>=n^(1/4)`, where `log(h+1)>=log(n)/4` can be inserted
in (8.1). Since `K=O(n)` and `pi(sqrt K)=O(sqrt n/log n)`, the core
satisfies the sharper bound

`|E|=O(sqrt(n/log n))`.                                        (8.2)

Moreover, its large-prime part `H intersect (sqrt K,infinity)` has
reciprocal mass `o(1)`. To see this, put `T=sqrt K log n`. On the
lower band `(sqrt K,T]`, the sum over all primes tends to zero by
the reciprocal-prime asymptotic, since

`log T/log(sqrt K) -> 1`.

On the upper band use (8.1):

`sum_{p in H,p>T}1/p <= [n log M]/[T^2 log T]`
`                    =O(1/log^2 n)`.

Here `K` is between positive constant multiples of `n` in both the
exact minimal-counterexample case and the budget family of Section 7.
Thus

`sum_{p in E,p>sqrt K}1/p=o(1)`.                               (8.3)

The estimates (8.2)--(8.3) improve the description of the remaining
core. They do not replace the missing argument for its interaction
with the light-prime band.

