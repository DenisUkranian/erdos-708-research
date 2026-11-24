# Universal large-maximum cutoff for the nine-point bound

Research proof, 24 November 2026. Dependencies: `g(3)<=4`, `g(4)<=5`,
`g(5)<=6`, the independently checked `g(6)<=8`, and the previously proved
large-prime support/core reduction in `g89_theory/core_reductions.md`.

## Statement

If the nine-point bound fails, there is a counterexample with maximum
`M <= 24696`. More precisely, a counterexample of least possible maximum
cannot have `M >= 24697`. This includes all numbers of large primes.

Call primes at least 11 large; all other factors are 7-smooth. The
previous reduction says that every large prime in a counterexample has
source support at least three, satisfies `p^2 > M/9`, and that there are
at most three large primes. Every source contains at most two large
prime occurrences. In particular, the product of any three distinct
large primes exceeds `M`.

## 1. Removing a common divisor

A least-maximum counterexample has gcd one. If a prime `p` divides all
seven sources, the `p`-multiples of an interval of length `M` correspond,
after division by `p`, to an interval of exactly `M/p` consecutive positive
integers. The divided sources are distinct and have maximum `M/p`.
If none is one, minimality gives a cover of at most nine points. If one
is one, `g(6)<=8` covers the other six. Extend the cover to at least seven
points when necessary (the quotient interval has length at least seven),
then multiply the selected points by `p`. This supplies both the divided
source product and the extra factor `p^7`, using at most nine points.

Thus no large prime has support seven in the chosen counterexample.

## 2. A fresh-factor packing calculation

After covering five sources in six points, it suffices to pack the
product of the two removed sources into capacities

    floor(M/7), floor(M/8), floor(M/9).

Indeed, choose fresh multiples of the three resulting factors
successively. If some prime factors have already been assigned to these
bins, append all remaining prime factors, assumed at most seven, in any
order. If insertion fails at a prime `p <= 7`, each current bin product
`b_j` satisfies `p*b_j > floor(M/j)`, hence `p*b_j > M/j`. Consequently

    ab >= p*b_7*b_8*b_9 > M^3/(504*p^2).

But `ab <= M^2`, so failure is impossible when `M > 504*49 = 24696`.

A second version will be used below. A 7-smooth product `Q <= 6^7` packs
into capacities `floor(M/8), floor(M/9)` when `M >= 24697`. Failure at
`p <= 7` would give

    Q > M^2/(72*p) >= M^2/504 > 6^7,

where `504*6^7 = 141087744 < 24697^2`.

## 3. A prime greater than M/9

Suppose `p > M/9` is large and has source support `d`. Then
`3 <= d <= 6`. Since `p >= 11`, the inequality `M < 9p < p^2` holds.
The affected sources therefore have the form `p*c_i` with distinct
`c_i` in `{1,...,8}`. Let `c_*` be the largest cofactor and choose an
interval multiple `z` of `p*c_*`.

Cover the other `7-d` sources in `r` points, where

| d | 3 | 4 | 5 | 6 |
|---|---|---|---|---|
| r | 5 | 4 | 2 | 1 |
| r+d | 8 | 8 | 7 | 7 |

There are at least `d` interval multiples of `p`; choose `d` of them
including `z`. Their union with the old cover supplies the full `p`
demand without consuming any valuation required by the old, `p`-free
source product. If `z` is new, it additionally supplies `c_*`, with at
most `r+d` points used. If `z` was old, the union has at most `r+d-1`
points; append a fresh multiple of `c_*` to reach the same conclusion.
Such a fresh multiple exists since `c_* <= 8` and `M >= 24697`.

For `d=3,4`, at most three remaining cofactors must be supplied, and
their product is at most `7*6*5=210`. One fresh multiple suffices.
For `d=5,6`, at most five remaining cofactors can be divided into two
groups of at most three and two; their products are at most 210 and 42.
Two fresh multiples suffice. All needed factors are at most `M/9`.
Thus this case always closes in nine points.

## 4. All large primes are at most M/9

Suppose first some source has large-prime degree at most one. Pair it
with any other source. Their combined large-prime occurrences number
at most three, and each individual prime fits into every one of the
three bins from Section 2. Place these occurrences separately, and then
append all small-prime factors. Section 2 finishes the pair and hence
the entire instance in nine points.

Therefore every source in a counterexample has large-prime degree two.
Write the sources as `a_i = d_i*s_i`, with core `d_i` equal to a prime
square or a product of two distinct large primes.

If any core `d_i <= M/7`, choose another source and put `d_i` in the
first bin, with the two individual prime occurrences of the second
source in bins two and three. Appending the small factors again finishes.
Thus every core is greater than `M/7`, so all seven cofactors satisfy

    1 <= s_i <= 6.

## 5. Core groups and the exceptional triangle

For each distinct core `d`, let `m_d` be its source multiplicity. Select
`m_d` distinct interval multiples of `d`; this is possible because
`m_d <= floor(M/d)`. The core-group deficit argument from the cited
reduction proves a core cover of at most seven points unless all three
pair cores `pq,pr,qr` meet at the same selected point. The only possible
positive cycle contribution is this triangle, and there is at most one
potential triangle point because `pqr > M`.

If fewer than three large primes occur, or some pair core is absent,
there is no triangle. If a pair-core group has spare capacity
`floor(M/d) >= m_d+1`, choose that group to avoid the potential triangle
point. There is again no triangle. Thus the entire large-prime demand
is covered in at most seven points. The product of *all* small
cofactors is at most `6^7`; by the two-bin version of Section 2, two
fresh points supply this product. No small-prime valuation from the
core cover is counted or needed in this argument.

The remaining case has all three pair-core groups present and saturated:

    m_pq = floor(M/(pq)),
    m_pr = floor(M/(pr)),
    m_qr = floor(M/(qr)).

Distinctness forces the cofactors in each such group to be exactly
`1,...,m_d`. Let `t=m_pq+m_pr+m_qr`, so `3 <= t <= 7`; the other
`7-t` sources have loop cores. Require the core-group cover to contain
a multiple of a full source having largest small cofactor `s_*`.
The core theorem allows this prescription and uses at most eight points.
The product `Q` of the remaining six small cofactors is bounded as follows:

| t | bound on Q |
|---|------------|
| 3 | `6^3 = 216` |
| 4 | `2!*6^2 = 72` |
| 5 | `3!*6 = 36` |
| 6 | `4! = 24` |
| 7 | `5!/5 = 24` |

For `t<=6`, remove the largest loop cofactor (or a still larger cofactor)
and bound the product of the three edge-group factorials by `(t-2)!`.
For `t=7`, inspect the four unordered compositions of seven into three
positive integers, or directly maximize `a!*b!*c!/max(a,b,c)`.
Thus `Q<=216<M/9`. A fresh multiple of `Q` completes the cover in at
most nine points, since the prescribed full-source point supplied `s_*`.

All cases contradict the existence of a least-maximum counterexample
with `M>=24697`. A separate finite verification for `M<=24696` is still
required before asserting `g(7)<=9`.
