# Adaptive cold-complement transport: a precise closure ladder

## Status and purpose

This note continues the unrestricted asymptotic problem. It does **not** prove
`g(n) <= (2+o(1))n`. It isolates a sufficient arithmetic Hall statement, proves
several exact reductions of its cuts, and distinguishes the actual outstanding
inequality from stronger statements that are unnecessary or false.

All notation and optimizer inputs are those in
`ep708_dot_20261123/notes/GLOBAL_OPTIMIZER_INPUT.md`,
`FULL_TAIL_MGF_INPUT.md`, and `NEAR_QUADRATIC_PROOF.md`.

Fix `c=2+delta`, an interval `I` of `M` positive consecutive integers, and a
genuine global positive maximizer of `J_c`. Write

    A = {a <= M : X(a)>c},     n=|A|,
    X(a)=sum_p w_p v_p(a),     0<=w_p<=1.

The paired primal vector has saturated hot positions and tight active prime
rows. We may use, with constants depending only on delta,

    cn < M < 16 n^2,            K= #{b in I:X(b)>1} <= C_delta n,
    r = #{active source primes} = O_delta(n/log n),
    sum_{a in U}(X(a)-c) <= 2 B_delta |U| log(2n/|U|).       (0)

The near-quadratic branch has already been eliminated. The remaining interval
is `cn<M=o(n^2)`. No new rounding theorem is required.

### An easier graph specifically for the asymptotic goal

The exact complement threshold 1 is not necessary here. For any fixed
`0<epsilon<delta`, put `tau=1+epsilon` and allow

    X(a/gcd(a,b))<=tau.                                   (0a)

Every such target is still hot and pays at least `X(a)-(2+epsilon)`.
The exact matching implication becomes

    J_c(w) <= 2B_delta t log(2n/t)
                      -(delta-epsilon)(n-t).             (0b)

Thus the enlarged graph, for example with `epsilon=delta/2` or `delta/4`, has
the same sufficient small-deficiency target. This is the preferable version
when exact `2n` is not being attempted. All neighborhood inclusions and cut
closures below remain valid after replacing the complement threshold 1 by
`tau`.

It also changes the treatment of the two-hot-factor exception. If a source
contains a minimal hot divisor `d` with

    1<X(d)<=1+epsilon,

then deleting the **whole** `d` is permitted in (0a). Its carrier `a/d` is hot,
of load greater than `1+delta-epsilon`, and has numerical size at most `K`:
`d>T=M/(K+1)` implies `a/d<K+1`. No such source needs to be discarded merely
because both factors are hot. This enlarges the available carrier family; it
does not yet prove its Hall inequality.

## 1. The adaptive graph and the exact deficit required

Put an edge between a source `a in A` and a target `b in I` exactly when

    X(a/gcd(a,b)) <= 1.                                    (1)

Equivalently, some divisor `d|a,b` has cold complement `X(a/d)<=1`.
It is important to allow **all** these divisors. Fixing one cofactor or one hot
root in advance discards the adaptive repair that defeats the known union
counterexamples.

For every edge,

    X(b)-1 >= X(gcd(a,b))-1 >= X(a)-2 > delta.             (2)

Let `t` be the deficiency of a maximum matching. Summing (2) only over distinct
matched targets gives, without a capacity duplication,

    J_c(w) <= 2 B_delta t log(2n/t) - delta(n-t),           (3)

with the first term interpreted as zero when `t=0`.

Consequently **any** one of the following would close the remaining branch:

* `t=o_delta(n)` uniformly on genuine positive global extrema;
* the stronger `t<=C_delta r`;
* for this fixed delta only, `t<=epsilon_delta n`, where
  `2 B_delta epsilon_delta log(2/epsilon_delta)
   < delta(1-epsilon_delta)`.

The last form is the weakest useful cardinality target. An arbitrarily good
parameterized estimate, with constants allowed to depend on delta and the
desired deficiency fraction, is enough. Exact injectivity is unnecessary.

For example `t=O_delta(r)` would give an error
`O_delta(n log log n/log n)` in (3), which is strictly smaller than the fixed
linear gain. Establishing the source-prime bound and the full-tail moment bound
is already finished work; they must not be re-proved in place of this step.

## 2. Exact form of an extremal Hall cut

Write `N(a)` for the adaptive neighborhood. If `a|a'`, then

    a/gcd(a,b) | a'/gcd(a',b)

for every integer `b`. Hence

    N(a') subseteq N(a).                                  (4)

The strict full tail `A` is upward closed under divisibility in `[1,M]`.
Therefore a set maximizing `|S|-|N(S)|` can be chosen upward closed in the
whole prefix: adding an omitted multiple of an existing source adds no new
neighbor and increases the deficit. This is stronger than declaring `S` to be
an arbitrary collection of source rows.

Put

    C=[1,M] \ S,          B=I \ N(S).

Then `C` is a divisor down-set, contains every integer of load at most `c`, and

    |S|-|N(S)| = |B|-|C|.                                 (5)

Moreover, whenever `b in B`, `d|b`, `u>=1`, `du<=M`, and `X(u)<=1`, necessarily

    du in C.                                             (6)

Indeed, otherwise `du in S`, and `d` gives an adaptive edge to `b`.

Let `T=M/(K+1)`. Every integer `u<=T` is cold, by the already-proved mandatory
bank bound. Thus each missing target `b` forces, for each divisor `d|b`, the
entire initial multiplicative segment

    d, 2d, ..., floor(min(T,M/d))d

into `C`. A proof of

    |B| <= |C| + epsilon_delta n                           (7)

for these **arithmetic** down-sets, with the optimizer restrictions retained,
is the exact remaining cardinality statement. No known estimate here proves
(7). The closure relation alone is not a Hall bound.

## 3. A weaker capacity version, if cardinal matching is too strong

Use the same adaptive graph but give source `a` the demand `X(a)-2` and target
`b` the capacity `(X(b)-1)_+`. A fractional flow sending all but `eta n` of the
total source demand would imply

    J_c(w) <= eta n - delta n.                            (8)

By the max-flow/min-cut theorem this is equivalent to the family of cut bounds

    sum_{a in S}(X(a)-2)
        <= sum_{b in N(S)}(X(b)-1)_+ + eta n
                     for every S subseteq A.             (9)

This route is genuinely weaker than demanding one different target per source:
a target with a large actual penalty may pay several smaller source demands.
However (9) has to be proved arithmetically. For `S=A`, its left-minus-right is
at least `delta n+J_c(w)` at a putative positive optimizer, because
`N(A)` is a subset of the hot targets. Writing (9) is not a proof and does not
extract a new inequality from the exact prime balances.

The divisibility closure of Section 2 is a cardinal cut reduction. One cannot
automatically use the identical upward-closure claim for the weighted cut
objective: adding a multiple changes its source demand, and the neighborhood
inclusion is still useful, but a maximum weighted-deficit set does become
upward closed because every source demand `X(a)-2` is positive. Thus (5) changes
to the weighted sums in (9), while (4) and (6) remain valid.

## 4. An exact one-bank inequality (proved)

This elementary observation uses all raw prime powers and is independent of
optimality. It is useful for testing whether a proposed cluster really needs
an injective carrier assignment.

**Lemma.** Let `g` be hot, `X(g)>1`, and let `S` be any set of distinct source
integers at most `M` divisible by `g`. Then

    sum_{b in I, g|b}(X(b)-1)
        >= sum_{a in S}(X(a)-2) + |S|.                    (10)

**Proof.** Put `m=floor(M/g)` and let `N>=m` be the number of target multiples
of `g`. Their quotients form an interval of `N` consecutive positive integers.
The source quotients form a distinct subset of `[1,m]`. For every prime power,
the target quotient interval contains at least as many multiples as `[1,m]`.
All coefficients in the raw additive load are nonnegative, so

    sum_{b in I,g|b} X(b/g) >= sum_{a in S} X(a/g).

Writing `s=X(g)>1` gives

    target - sum_{a in S}(X(a)-2)
        >= N(s-1)-|S|(s-2)
        = |S|+(N-|S|)(s-1) >= |S|.

This proves (10). In particular a common hot root pays an entire cluster with
one unit of margin per source, even if its complements are hot. The missing
step is allocating **overlapping banks** among different clusters. Summing
(10) over roots is invalid.

## 5. Minimal hot roots: a proved overshoot dichotomy

Call `d` a minimal hot divisor if `X(d)>1` and every proper divisor is cold.
Set `epsilon(d)=X(d)-1`.

For every prime occurrence dividing `d`, deleting that occurrence leaves load
at most 1, and therefore

    w_p >= epsilon(d).                                   (11)

Deleting one occurrence and summing the lower bounds for the remaining ones
gives

    Omega(d) <= 1+1/epsilon(d),                           (12)

where multiplicities are counted. Consequently, for every fixed `B,epsilon>0`,

    #{d<=Bn : d minimal hot, epsilon(d)>=epsilon}=o(n),    (13)

uniformly over all supports and weight profiles. Indeed these `d` lie in the
weight-independent set of integers with a fixed bounded number of prime
factors. That set has density zero.

One elementary proof of the last assertion is to fix a finite prime set `P`.
For uniform integers modulo their product, the number of primes in `P` dividing
the integer is a sum of independent Bernoulli variables with mean
`sum_{p in P}1/p` and variance no greater than that mean. The density with at
most `k` prime factors is at most the probability this sum is at most `k`.
Let the finite prime set grow and use the divergence of the prime reciprocal
sum, followed by Chebyshev. First take the integer interval length to infinity
for the fixed modulus. This proves density zero without needing a uniform
asymptotic formula for almost-primes.

For a source `X(a)>2+delta`, any minimal hot divisor with
`epsilon(d)<=delta/2` yields the exact factorization

    a=d e,       X(d)>1,       X(e)>1+delta/2.             (14)

Thus, among the small hot-root part of the previous two-group argument, the
uncontrolled sources can be reorganized into:

* roots with substantial overshoot, of which there are only `o(n)` below `Bn`;
* sources with two disjoint hot factors, one of them of load `>1+delta/2`.

This is an unrestricted structural reduction, not a completed error estimate.
An `o(n)` number of roots does **not** imply that their banks have `o(n)` union
discrepancy. Nor is it legitimate to discard all products of two hot roots.
Those are exactly the joint capacity issues in (7) or (9).

The companion `SMALL_ROOT_UNION_COUNTEREXAMPLE.md` now proves this warning by
an actual family of minimal hot roots with `Omega(d)=2`, constant overshoot,
`K=O(n)`, `r=O(n/log n)`, and an actual full tail: its union-transfer error is
`Omega(n)`. A direct calculation also shows why its active 2-row cannot be
tight, so it identifies the indispensable optimizer hypothesis rather than
refuting the desired genuine-optimizer statement.

## 6. Why pairwise cold intersections are insufficient

Take the four primes `2,3,5,7`, each with weight `0.4`, and the four minimal hot
roots

    30, 42, 70, 105.

Each root has load `1.2`, every pairwise gcd has load `0.8`, and all divide
`210`. Paying the four root excesses uses `4*0.2=0.8`, while the actual target
penalty at `210` is only `1.6-1=0.6`. Therefore a multi-root cluster allocation
cannot follow merely from pairwise cold gcds.

For roots `d_1,...,d_s` at one target the exact overcharge over their common lcm
is

    sum_i (X(d_i)-1) - (X(lcm(d_1,...,d_s))-1)
      = sum_p w_p [sum_i v_p(d_i)-max_i v_p(d_i)] -(s-1).  (15)

Any prospective recursive clustering proof must control this **multiway**
quantity, rather than only its pairwise projections.

## 7. Ordered implementation ladder

1. Keep the true optimizer, full tail, paired raw rows, and moment estimate
   (0). Do not replace `A` by another threshold set without reoptimization.
2. Use the complete graph (1), not one fixed carrier per source. Extract a
   maximum-deficit upset cut and impose (6), including every cold quotient.
3. First attempt (7) with an arbitrary fixed deficiency fraction. The stronger
   `O_delta(r)` target would be especially convenient, but it is not required.
4. If cardinality is the obstruction, switch to the capacity cut (9), keeping
   the actual penalty at every position. Formula (10) can pay a whole common
   hot-root cluster, so a repeated cofactor is not automatically a loss.
5. In the small-root branch use (12)--(14): substantial-overshoot roots have
   bounded multiplicative degree; the remaining sources are products of two
   hot factors. A valid recursion must allocate their joint banks and account
   for (15). Root count alone is not sufficient.
6. Once either (7) or (9) is proved with an error small relative to delta,
   apply (3) or (8) immediately. This is the required contradiction. Invoke
   the already available raw-fractional transfer only afterwards.

The earliest genuinely open step remains Step 3 (or its weaker capacity
replacement at Step 4). No asymptotic result follows from the reductions alone.

## 8. Structural falsification search

`test_adaptive_hall.py` constructs the full tail, every cold-complement edge,
and exact maximum bipartite matchings. Target residues are chosen independently
modulo the maximal relevant prime powers; CRT makes every tested configuration
an actual shifted interval. These are tests of an intermediate Hall statement,
not computations of `g(n)`.

At `M=500`, seven weight profiles and forty residue choices per profile produced
zero deficiency in every test. Profiles included all weights 1, all 0.51, all
0.4, several mixed profiles, and both small and full prime supports. This is
weak computational evidence only; it neither proves exact matching nor the
`O(r)` bound. The old full-prefix prime-deletion counterexample uses all source
integers, including load-two sources. It does not, by itself, refute the actual
strict load-`>2` full-tail matching statement.

The same outcome held for seven profiles with thirty residue choices at
`M=2000,c=2.05`, and seven profiles with forty residue choices at
`M=1000,c=2.001`. These tests were stopped after no structural counterexample
emerged; increasing such experiments would not supply the missing proof.
