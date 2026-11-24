# Verified prior upper bound g(6) <= 8

This prior result is proved independently of the seven-source theorem.
Its only non-elementary numerical input is `g(5)<=6`, Theorem 1.6 in
John Tripodo, *Sharp finite cases of the Erdos-Suranyi interval-product
problem: g(4)=5 and g(5)=6*, 19 November 2026, manuscript version 1.8:
https://hexagonmath.org/pdf/2611.00694v1 . The cited source reports Lean
verification; that external formalization was not rebuilt here.

## Reduction to 5-smooth sources

If a source `a` has a prime divisor `p` and `floor(M/(a/p))>=7`, cover the
other five sources in six points. A fresh multiple of `a/p` gives seven
points covering the target product divided by one occurrence of `p`.
The complete interval product covers the full target, so if necessary an
unselected point divisible by `p` repairs the remaining unit. Eight points
suffice. In particular every source prime `p>=7` is eliminated.

A source with at most two prime occurrences is also eliminated: cover
the other five in six points, then repair its at most two missing prime
units individually. Any remaining counterexample therefore has every
source 5-smooth, with at least three prime occurrences, and satisfies

    7a > M*Pplus(a)

for every source, where `Pplus(a)` is its largest prime divisor.

## Analytic tail

Pack all prime factors of the six-source product, in descending order,
into eight capacities `floor(M/j)`, `1<=j<=8`. For `M>=40`, failure at
`p` forces its rough part to be at least

    T_p(M) = p*product_{j=1}^8 max(floor(M/(jp))+1,p).

The rough part is at most `M^6`. For the largest prime 5, distinctness
improves the bound to `M^6/6!`: if the six 5-parts are ordered
`q_1>=...>=q_6`, their nested divisibility implies `i*q_i<=M`, hence
`product q_i<=M^6/6!`.

The strict real bound

    T_p(M) > M^8/(8!*p^7)

gives an explicit infinite tail. Exact integer checks below that real
threshold improve the common cutoff to `M>=9360`. The script
`g7_theory/analytic_cutoffs.py`, invoked by the master verifier, checks
these threshold calculations with integer arithmetic.

## Complete finite verification

The independent program `g7_theory/check_g6_independent.py` trial-factors
all integers below 9360, applies only the proved reductions above, and
enumerates every actual remaining six-source subset. It accepts direct
prime-union bounds, explicitly checked ordinary bin packings, or one of
277 independently validated cumulative-GCD slot witnesses in
`smooth_proof/frontier_slots6.json`.

The replay verifies 155 eligible maxima and 1,045,917 actual subsets,
with 74,220 distinct remaining demands. Of those, 67,918 close by prime
union, 5,940 by ordinary packing, and 362 by the validated slot witnesses.
The full replay returns PASS. No finite sampling of interval shifts is
used: every accepted certificate applies to every interval of length M.

Combining this finite verification with the analytic tail proves
`g(6)<=8`, subject only to the stated external `g(5)<=6` theorem.
