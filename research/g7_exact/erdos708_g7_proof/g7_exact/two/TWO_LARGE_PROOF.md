# The two-large-prime component of the nine-point theorem

This component proves that a least-maximum, maximum-sum counterexample to
`g(7)<=9` cannot have exactly two prime divisors at least 11. The general
large-maximum proof reduces the calculation to `M<=24696`. This document
describes the complete finite coverage and its replayable certificates.

The previous bounds used are `g(1)=1`, `g(2)=2`, `g(3)<=4`, `g(4)<=5`,
`g(5)<=6`, and the independently verified `g(6)<=8`. All covers have the
at-most cardinality convention, and all shifts of the target interval
are quantified universally.

## 1. Safe reductions and the occurrence of a pair core

Choose a counterexample of smallest maximum `M`, and among those choose
the source set `A` with greatest sum. The common-divisor argument in
`../root/LARGE_M_CUTOFF.md`, including padding the divided cover to at
least seven points, gives `gcd(A)=1`.

If `a` is a source and `ka<=M` is absent, replacing `a` by `ka` strictly
increases the sum and multiplies the target product by `k`. The same
interval remains a counterexample. Therefore `A` is closed under taking
integer multiples within `[1,M]`. This implies `a>M/7` for every source:
otherwise the seven distinct multiples `a,2a,...,7a` exhaust the source
set, contradicting gcd one.

Write the two large primes as `p<q`. Each has source support at least
three, satisfies `p^2>M/9` or `q^2>M/9`, and every source has large-prime
core in

    1, p, q, p^2, pq, q^2.

At least one source has core `pq`. Here is a proof that does not assume
any inequality between `pq` and `M`. If no source contains both primes,
their supports are disjoint. Both supports have size at least three, so
one, say the support of `p`, has size exactly three. Write its sources
as `p^{e_i}c_i`, where `e_i` is one or two and `p` does not divide `c_i`.
All three cofactors are also `q`-free.

If all exponents are one and `p^2<=M`, the square-gain lemma already
closes the instance in nine points. If `p^2>M`, the three distinct
cofactors have all their pair products at most `(M/p)^2<M`, and these
three products are distinct. If a squared source occurs, its cofactor
is at most eight. When there is one or two squared sources, multiply a
cofactor from the exponent group of size one by the two distinct
cofactors in the other exponent group; this gives two distinct products
at most `8M/p<M`. When all three sources are squared, any two pair
products are distinct and at most `64<M`.

Thus at least two distinct `q`-free pair products `H<=M` are available.
Among the other four sources at least three contain `q`, so at most one
is `q`-free. Choose an available `H` not equal to an old source. Cover
the other four sources together with `H` in at most six points, using
`g(5)<=6` (drop `H` if it is one).

Supply the entire `p` demand in at most three points, including a
multiple `z` of the remaining full `p`-source. Such a prescribed point
can always be included: first match the three required prime powers to
distinct interval points; if `z` is not already in the matching, replace
the point assigned to that remaining source by `z`. If `z` was outside
the six-point cover, its cofactor is supplied as well. If `z` was inside,
the overlap saves one point, and a fresh multiple of its cofactor uses
that saved point. The cofactor has at least `p>=11` multiples in the
interval. Both cases use at most nine points, a contradiction.

Consequently

    11 <= p < q,    pq <= M <= 24696,    M < 9p^2.

In particular `p<=157` and `q<3*sqrt(M)<472`. A prime table through 1500
is more than sufficient. Source support also implies `M>=3q`.

## 2. Exhaustive core classes

The six core multiplicities `c_0,...,c_5` sum to seven. The code requires
`c_4>=1`, both supports at least three and less than seven, and `c_0<=3`.
The last condition loses no counterexample: four core-one sources would
leave three nontrivial sources; both supports of size three force all
three cores to be `pq`. The smaller prime has square at most `M` and
three simple occurrences, so the square-gain lemma closes that case.

The maximum is itself a 7-smooth integer times one of the six cores.
For a core `d`, its possible cofactors are exactly the 7-smooth positive
integers `s` such that

    M/7 < d*s <= M.

Coefficients in the same core class must be distinct. If support is
three, all its exponents are one, and the square fits in the interval,
that class is again eliminated by the square-gain lemma.

The exhaustive core scan has the following sizes:

| Quantity | Count |
|---|---:|
| prime pairs | 1,123 |
| pair-and-maximum configurations | 128,915 |
| admissible core classes | 2,980,414 |
| classes closed by the bounds below | 2,784,139 |
| classes passed to the graph enumeration | 196,275 |

## 3. Combining an old smooth cover with a core cover

Let `z=c_0` and `m=7-z`. Cover the `z` core-one sources in
`r=g(z)` points, taking `r=0,1,2,4` for `z=0,1,2,3`.

The two-prime core-group lemma covers the entire large-prime demand in
at most `m` points. A second valid bound is the sum of the independent
prime-supply costs. For a prime `p`, the best `k` positions in an interval
have total `p` valuation at least

    sum_{e>=1} min(k, floor(M/p^e)).

Prime-specific covers can overlap because their demands involve
different primes. The code takes the better of these two core bounds.

The remaining 7-smooth cofactor product can be supplied using positions
outside the old smooth cover. These positions may overlap the core
cover freely: small-prime and large-prime valuations are disjoint.

An improved version prescribes a multiple `w` of a full nontrivial
source with cofactor `s_*`. If `w` is outside the old smooth cover, it
supplies `s_*` in addition to the core. If it is inside, the overlap saves
a point; use that point to select a multiple of `s_*` outside the old
cover. There are at least eleven such multiples. In either case the
remaining small product is `Q/s_*`, and its new positions need avoid
at most `r+1` points, not the entire core cover.

For the prescribed-point prime-supply bound, the program considers every
possible valuation `v` of the prescribed point, from its guaranteed
valuation up to the relevant demand. After excluding that point, at
least `floor(M/p^e)-[v>=e]` multiples of `p^e` remain. The sum of their
largest `k` valuations is bounded below by the corresponding sum of
minima. Taking the worst required `k` over all `v` gives a valid bound
uniformly in the interval and in the prescribed point.

## 4. Product and rough-product bounds

With `f` points forbidden, products bounded by `floor(M/(f+j))` can be
placed in fresh positions successively, for `j=1,...,k`.

For a cofactor product with prime factors at most seven, descending greedy
packing into these capacities can fail at a prime `u` only if

    Q_{>=u} >= u * product_{j=1}^k
        max(floor(M/((f+j)u))+1, u),

provided `u` fits the smallest empty bin. The program checks that
condition explicitly. Here `Q_{>=u}` is the part of `Q` supported on
primes at least `u`. It suffices to have a strict upper bound below this
threshold for each `u` in `{2,3,5,7}`.

Within each core group, products of the largest available coefficients
bound the product of every selection of the required size. For an
anchor group, prescribe the largest coefficient actually selected in
that group. The remaining coefficients form a subset of the complete
candidate pool with its numerically largest coefficient removed: if
that maximum was selected, it is the prescribed one; if it was not
selected, it is absent anyway. This statement is also valid when taking
prime rough parts. Sorting the rough parts of the remaining candidate
pool therefore supplies a rigorous bound for each threshold prime.

The actual combinations attaining different rough bounds need not be
the same. They are used only as independent upper bounds. Integer
arithmetic uses unsigned 128-bit values; all relevant products are
well within that range.

## 5. Graph enumeration of the remaining source sets

For two distinct sources `a,b`, a packing of `ab` into capacities
`floor(M/7), floor(M/8), floor(M/9)` proves a nine-point cover: cover the
other five sources in at most six points and append three fresh
multiples. A candidate counterexample must therefore have every source
pair fail this sufficient packing test.

For every residual configuration, the code first removes sources that
form a certified good pair with `M`. It then repeatedly removes any
source whose required larger multiple has been removed. All required
multipliers are at most six because sources exceed `M/7`, so they
preserve the large-prime core.

The remaining bad-pair graph is enumerated by exact core multiplicities.
If `M` has a nontrivial core, it is fixed as one selected vertex. Every
resulting clique is checked for upward closure. Core-one sources are
temporarily covered by the general `g(z)` bound rather than enumerated.
The actual nontrivial cofactor product is tested using the bounds above,
exact two-bin divisor packing, and independent small-prime supply
outside the forbidden old points.

Positive product caching is valid: its key specifies `z`, all four small
prime exponents, and both large prime exponents. Two entries with the
same key have the same nontrivial product. The successful auxiliary
factorization and cover construction for one entry proves the same
target product for the other, with any old smooth-source product.
The exponent encoding is injective: each small exponent is below 64
and each large exponent is at most 14.

This stage checks 50,660 configurations and 112,998 actual nontrivial
cliques. It covers 67,663 of them directly and leaves 45,335 nontrivial
sets. Their maxima are at most 665. Every residual set has either zero
or one core-one source; none has two or three.

## 6. Full source expansion and explicit certificates

For the residual six-element nontrivial sets with one missing smooth
source `b`, upward closure implies `b>M/2`. If `M` is not already among
the six sources, then `b=M`; otherwise every 7-smooth `b` in `(M/2,M)`
is considered. Common-divisor cases and explicitly certified good pairs
are removed. Every surviving set is checked to contain seven distinct
sources, to have maximum `M`, and to be upward closed.

This gives 116,394 complete source sets and 33,939 distinct product
demands. At each fixed prime pair and maximum, coordinatewise maximal
demands form a set of 24,511 vectors. Every one has an explicit list of
at most nine factors `h_j` satisfying

    1 <= h_j <= M,
    gcd(h_1*...*h_{j-1}, h_j) <= floor(M/j),
    product(A) divides product(h_j).

The cumulative-GCD lemma turns each such list into a cover for every
interval shift. The verifier checks these integer conditions directly,
without trusting the search program, and separately checks that every
one of the 33,939 demands is dominated by a validated certificate at
the same maximum and prime pair.

## 7. Reproduction and outcome

Run from any working directory:

    python3 g7_exact/two/verify_two.py

The verifier compiles and reruns both complete C++ enumerations in a
temporary directory, regenerates the full source expansion, checks the
24,511 certificates exactly, and checks coverage of all 33,939 demands.
It needs only Python 3 and a C++17 compiler; no optimization solver,
floating-point numerical evidence, or sampling of interval shifts is
used.

The complete replay returned **PASS**. The two-large-prime component
therefore leaves no counterexample to the nine-point upper bound.
