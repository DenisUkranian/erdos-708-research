# A uniform hereditary raw-LP bound implies an integer asymptotic bound

Date: 2026-11-23.

## Purpose and status

This note verifies the integer-transfer step needed after a source-specific
fractional gluing theorem. It does not prove that gluing theorem. The raw-LP
estimate below is an explicit hypothesis. No unrestricted solution of Erdős
708 follows unless that hypothesis has itself been proved for the class
under consideration.

The transfer is a direct proof using a least-cardinality failing subset at a
fixed ambient interval length. It uses the previously audited external
quadratic theorem `M>=16m^2 => tau<=2m` in its ambient form. It does not need a
general bound such as g(m)<=10m, or an additive constant in the minimality
argument. All statements concern positive intervals and integer shifts x>=0.

## 1. Definitions and precise uniform hypotheses

For every positive integer M, let C(M) be a family of finite sets of distinct
integers in {2,...,M}. Assume that C(M) is hereditary:

    A in C(M), B subset A  =>  B in C(M).                    (1)

The ambient M is retained in (1). In particular, a smaller source set is NOT
reclassified using its own smaller maximum.

Let I={x+1,...,x+M}, where x is a nonnegative integer. Write tau(A,I) for the
minimum size of a subset of I whose product is divisible by product A.
For source primes p, put D_p(A)=sum_{a in A}v_p(a). Define the raw boxed LP

    L_raw(A,I)=min sum_{b in I} y_b

subject to

    0<=y_b<=1,
    sum_{b in I}v_p(b)y_b >= D_p(A) for every source prime p. (2)

The LP is feasible because `product A | M! | product I`. The empty source
set has tau=L_raw=0.

Fix delta>0. Assume that there is a threshold M_raw(delta) such that, for
EVERY ambient M>=M_raw(delta), every A in C(M), and every shift x>=0,

    L_raw(A,I) <= (2+delta)|A|.                              (3)

The threshold must be independent of the particular source set, its size,
the shift, and any auxiliary support choices admitted by the class.

External long-interval input, valid for every distinct B subset {2,...,M}:

    M>=16|B|^2  =>  tau(B,I)<=2|B|.                          (4)

Reference: Ziming Wang, *Fractional-to-Integer Transference and Five-Prime
Bounds for Interval Divisor Covers*, section “The quadratic coefficient-two
gate”, <https://github.com/science-prince/erdos-708-interval-divisor-covers>.
Its displayed proof uses only a<=M, so the same argument applies when M is
an ambient bound exceeding the largest source. This ambient extension was
checked earlier in the project.

## 2. Quantitative transfer lemma

**Lemma.** Under (1)–(4), there exists M_int(delta) such that, for every
M>=M_int(delta), every A in C(M), and every x>=0,

    tau(A,I) <= (2+2delta)|A|.                               (5)

More explicitly, put c=2+2delta and choose any integer m_0>=1 for which

    pi(c m)<=delta m for every integer m>=m_0.               (6)

Such m_0 exists by the standard Chebyshev bound pi(t)=O(t/log t). Then

    M_int(delta)=max(M_raw(delta),16m_0^2)                   (7)

is sufficient, with an integer ceiling if needed.

**Proof.** Suppose M satisfies (7) and some A violates (5). Among subsets
of this A, choose a subset B of least positive cardinality m satisfying

    tau(B,I)>c m.                                          (8)

Every deletion B minus {a} consequently has a cover S_a in the SAME interval
I with

    |S_a|<=floor(c(m-1))=K-1,
    K=floor(c(m-1))+1.                                     (9)

Heredity also ensures B belongs to C(M), so the raw estimate (3) applies to
B at the original ambient M.

### Every source prime is below K

If a source a in B has a prime divisor p>=K, the interval contains at least

    floor(M/(a/p))>=p>=K

multiples of a/p, since a<=M. At least one such multiple lies outside S_a.
Add it. The chosen product then covers product B except possibly one p-unit.
If that unit is still missing, some UNUSED interval position contains p;
otherwise the full interval product would have the same deficient
valuation, contradicting full-interval supply. Add that position.

The resulting cover has at most

    floor(c(m-1))+2 <= floor(c m)

positions, because c>=2. This contradicts (8). Hence every source prime is
strictly below K, and the number r of source-prime rows in (2) obeys

    r<=pi(K-1)<=pi(c m).                                    (10)

No assumption about the sizes or identities of the auxiliary prime supports
is used in this row bound.

### Round only the finitely many fractional coordinates

An optimal basic feasible solution of the finite boxed LP (2) has at most r
coordinates strictly between zero and one. Indeed, if more than r coordinates
were fractional, the at most r covering constraints could not eliminate all
nonzero perturbations on those coordinates while the other coordinates were
held fixed. A sufficiently small perturbation in either direction would
preserve all active constraints and remain feasible, contradicting that the
point is a vertex.

Round every fractional coordinate up to one. All constraint coefficients
are nonnegative, so this gives an integer cover, and the increase in cost is
at most r. Equations (3) and (10) yield

    tau(B,I) <= (2+delta)m + pi(c m).                        (11)

### A failing subset must be large when the ambient interval is large

If M>=16m^2, (4) would give tau(B,I)<=2m<=c m, contrary to (8). Thus

    M<16m^2,     m>sqrt(M)/4>=m_0.                          (12)

Condition (6) now applies to (11), giving tau(B,I)<=c m. This is the final
contradiction. End proof.

The integer floor in (9) and the strict inequality in (12) cause no endpoint
loss. The argument also excludes a one-source failing subset directly.

## 3. Uniform asymptotics and optional additive formulation

Suppose (3) holds for every delta>0, each with its own uniform threshold.
For any epsilon>0, apply the lemma with delta=epsilon/2. Then every source
set in the class at ambient M>=M_int(epsilon/2) has

    tau(A,I)<=(2+epsilon)|A|.                               (13)

If n=|A| tends to infinity, distinctness of sources in {2,...,M} gives
M>=n+1. Hence M also tends to infinity. This proves the uniform statement

    tau(A,I)<=(2+o(1))n                                    (14)

over the hereditary class and all allowed shifts and ambient lengths.
The little-o assertion means the quantified assertion (13); no explicit
rate is obtained merely by this transfer.

If an all-cardinality additive statement is wanted, choose
`C_epsilon=ceil(M_int(epsilon/2))`. When M is below that threshold, the full
interval gives tau<=M<=C_epsilon; when M is above it, (13) applies. Therefore

    tau(A,I)<=(2+epsilon)n+C_epsilon

holds for all instances in the class.

The additive constant is introduced only AFTER the zero-offset argument.
This avoids choosing a threshold that depends on an additive constant and
then enlarging that same constant to absorb all smaller lengths. There is
no circular dependence on C in (6)–(7).

## 4. Application checklist for the separated-band gluing theorem

For the proposed separated class, retain the original M and the same support
sets Q,R when deleting sources. If every source is either Q-smooth or has
the form d*r with d Q-smooth and exactly one prime r in R, every subset has
the same property. Conditions on Y(M),Z(M) also remain unchanged. Heredity
therefore holds, including subsets containing no mixed sources or no pure
sources.

Once a SEPARATE proof establishes the uniform raw bound (3) for arbitrary
pure Q sources together with these mixed sources, the lemma supplies the
integer asymptotic bound. It is not necessary to combine independent pure
and mixed covers or to reserve target capacities a second time.

The following weaker statements would not, by themselves, justify this
application:

* a raw bound only when M equals the current maximum source, without a
  valid argument for retaining the original ambient M;
* a threshold depending on the particular subset or on its cardinality;
* a nonhereditary requirement excluding pure-only or mixed-only subsets;
* an informal claim that arbitrary LPs can always be rounded at o(n) cost.

Here the small rounding cost is proved for a hypothetical minimal failing
subset by the prime-deletion argument. The long-interval theorem then forces
that subset to be large. Those two steps are what make the transfer uniform.
