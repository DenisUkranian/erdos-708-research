# A two-carrier reduction using part of the asymptotic slack

## Status

The reduction below is proved for every full-tail source at a genuine positive
optimizer, with no deletion of a diffuse source component. It is a structural
reduction of the remaining Hall/capacity problem, not a proof of its sufficient
deficiency bound.

## 1. Setup

Let `c=2+delta`, let `A={a<=M:X(a)>c}`, and let `K` be the number of hot target
positions. Put `T=M/(K+1)`. Hot saturation implies

    d<=T  =>  X(d)<=1.                                    (1)

Choose `0<eta<=delta/8`. An active prime is called light when `w_p<=eta`, and
heavy otherwise. Denote the light contribution by `V`; inactive primes have
weight zero and are kept separate. We use the enlarged complement allowance

    tau=1+delta/2.                                        (2)

Write `a=a_H a_L a_0`, where the three factors contain respectively the heavy,
light, and inactive prime occurrences, with multiplicity.

## 2. Two-carrier lemma

**Lemma.** Every source `a in A` has an active carrier `h|a` with

    X(a/h)<=tau,            X(h)>1+delta/2,                (3)

and at least one of the following properties:

* `h` contains heavy primes only;
* `h<=K`.

If `X(a)<=L`, the pure-heavy carrier has `Omega(h)<L/eta`, so the first
alternative has bounded multiplicative degree independent of `n,M`, the
support, and the shift.

**Proof.** There are two cases.

If `V(a)<=1+delta/4`, delete `a_L a_0` and put `h=a_H`. Then

    X(a/h)=V(a)<=1+delta/4<tau,
    X(h)=X(a)-V(a)>1+3delta/4.                            (4)

Every prime occurrence of `h` has weight greater than `eta`, and hence
`eta Omega(h)<X(h)<=X(a)<=L` when the load cutoff applies.

If `V(a)>1+delta/4`, multiply light prime occurrences in any fixed order until
their load first exceeds `1+delta/4`. Let `d` be that partial product. Each
increment is at most `eta`, including a repeated occurrence of the same prime,
so

    1+delta/4<X(d)<=1+delta/4+eta
                         <=1+3delta/8<tau.                (5)

Delete `d a_0` and put `h=a/(d a_0)`. This divisor is active, and

    X(a/h)=X(d)<tau,
    X(h)=X(a)-X(d)>1+5delta/8.                            (6)

Because `d` is hot, (1) forces `d>T`, and therefore

    h<=a/d<=M/d<K+1.

As `h` is an integer, `h<=K`. This proves the lemma. Inactive prime factors
play no role in the load and deleting all of them can only decrease the
numerical carrier.

## 3. Quantifiers and the common high-load deletion

Fix delta, then choose eta, and finally a fixed source cutoff L. The already
proved full-tail exponential moment implies that the total ORIGINAL source
load above L is at most `epsilon n`, for L sufficiently large in terms of
delta and epsilon. No independent target exponential estimate is used.

For the remaining sources the lemma gives a carrier family contained in

    {h<=K : X(h)>1+delta/2}
      union
    {h : Omega(h)<=ceil(L/eta), all prime weights>eta,
                                    X(h)>1+delta/2}.       (7)

The multiplicity of a carrier is retained: different original sources may
have the same active carrier. Their full source loads and the exact raw rows
remain those of the original optimizer. Equation (7) neither bounds the
number of distinct small carriers nor asserts separate matching capacities
for the two alternatives.

Each matched source is paid at its original load:

    X(b)-1>=X(a)-(2+delta/2),                             (8)

so the remaining gain is `delta/2` per matched source. The enlarged graph
should retain all admissible carriers satisfying (3), not just the carrier
chosen by this proof.

## 4. The resulting cut obligation

For an upward-closed Hall cut `S`, set `B=I\N(S)` and `C=[1,M]\S`. Every
`b in B` must avoid all carriers of sources in S. Equivalently, whenever
`d|b`, `du<=M`, and `X(u)<=tau`, the integer `du` lies in C.

The next sufficient statement remains

    |B|<=|C|+epsilon_delta n,                             (9)

or the weaker source-demand/target-capacity cut bound described in
`ADAPTIVE_HALL_LADDER.md`.

The two alternatives in (7) must be handled by ONE joint allocation. The small
carrier part still has no uniform small root count in the subquadratic branch.
The bounded-degree part still has repeated carriers, source cofactors, and
overlapping banks. Both types can occur at the same target, and pairwise cold
gcds do not justify paying them separately.

## 5. A useful necessary prime-row inequality for every saturated bank

For any hot divisor `h`, the whole target bank of h is saturated. For every
active prime p and every j>=1,

    #{b in I: h|b, p^j|b} >= floor(M/lcm(h,p^j)).

Consequently exact active rows give the simultaneous requirements

    D_p(A) >= sum_{j>=1} floor(M/lcm(h,p^j)).              (10)

This includes all raw powers, including the powers already present in h.
For a family of hot carriers, the correct joint version is

    D_p(A) >= sum_{j>=1}
       #{b in I: p^j|b and h|b for at least one carrier h}. (11)

It is (11), with a UNION before summing, that can be used against (9).
Adding the separate right sides of (10) spends the same active row repeatedly.

Equations (7) and (11) are compatible and may support a joint proof; they do
not yet imply (9). The arithmetic union counterexample in this directory
shows that (9) cannot be replaced by a union-transfer estimate that omits the
row demands. In that example the active 2-row has a linear forced oversupply,
which explains exactly why true optimizer balances matter.

## 6. Two further exact reductions of the large-carrier alternative

Suppose a pure-heavy carrier `h` in (7) exceeds K. Since it is an integer,

    M/h<=M/(K+1)=T.

Every possible integer cofactor `u<=M/h` is therefore cold by (1), regardless
of whether it actually supplies a source. In particular its actual complement
satisfies `X(a/h)<=1`, and

    X(h)>1+delta.                                        (12)

This improves the complement allowance on that alternative without discarding
any light contribution.

Next suppose a source a has **no** admissible carrier of numerical size at most
K in the full enlarged graph. Deleting any single prime occurrence is allowed,
since every prime weight is at most 1. Therefore `a/p>K` for every prime `p|a`,
and

    p<a/K<=M/K.                                         (13)

Thus genuinely inaccessible small carriers force every source prime into the
smaller scale `M/K`. If, in addition, its pure-heavy carrier has degree at most
k, then

    K<h<=(M/K)^k.                                       (14)

This is a necessary condition for the remaining large-carrier alternative.
It is not a bound for the small-carrier Hall cuts: sources with available small
carriers may still compete for the same target positions.

Finally, for any fixed heavy cutoff eta, every heavy prime satisfies

    p>T^(1/k_0),       k_0=floor(1/eta)+1,                (15)

because `p<=T^(1/k_0)` would make `p^k_0<=T` hot, contrary to (1). In the sparse
branch `M/n->infinity`, all heavy primes therefore tend to infinity. Equations
(13)--(15) delimit the bounded-degree arithmetic problem; none supplies its
missing joint Hall estimate.
