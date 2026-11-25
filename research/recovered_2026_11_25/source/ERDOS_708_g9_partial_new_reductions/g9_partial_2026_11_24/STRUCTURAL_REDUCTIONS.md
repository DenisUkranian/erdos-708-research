# Erdős–Surányi Problem 708: structural reduction for the nine-source case

**Date:** 24 November 2026. **Status:** partial result, **not** a proof of `g(9)=12`.

## Statement and dependencies

For nine *distinct* integers `A⊂{2,…,M}`, `M=max(A)`, and any interval `I` of `M` consecutive positive integers, denote by `τ(A,I)` the smallest number of **distinct** interval elements whose product is divisible by `P(A)=∏_{a∈A}a`.

The following statements assume the earlier upper bounds `g(6)≤8`, `g(7)≤9`, and `g(8)≤11`. These bounds are computational/research dependencies and are not reproved here. For every subset `A'` with `max(A')≤M`, the bound for `A'` applies to `I` as well: choose an `max(A')`-term subinterval of `I`.

We study a hypothetical obstruction satisfying `τ(A,I)≥13`.

## Lemma 1. A large prime of source support one is impossible

Suppose prime `p≥13` divides exactly one source `a`, and let `P0=∏_{b∈A\{a}}b`. Then `p∤P0`, so `d=gcd(P0,a)≤a/p≤M/13<M/12`. Cover `P0` with ≤11 interval positions. If some multiple of `a` is still unused, add it. Otherwise an already selected position is a multiple of `a`, so the current product is divisible by `lcm(P0,a)`. There are at least `⌊M/d⌋≥12` multiples of `d` in `I`, versus ≤11 previously selected positions. Adding a fresh multiple of `d` supplies `P0 a=d⋅lcm(P0,a)`. Thus 12 positions suffice.

## Lemma 2. A large prime of source support two is impossible

Suppose `p≥13` divides exactly two sources `a=p^e u`, `b=p^f v`, where `p∤uv`. Let `P0` be the product of the other seven sources; `p∤P0`. Choose `B0⊆I`, `|B0|≤9`, whose product is divisible by `P0`. For each of `a,b` choose *one* multiple in `I`, called `s,t`; each exists because `a,b≤M`.

* If `s≠t`, retain both of them (adding whichever are not in `B0`). Their combined `p`-valuation is at least `e+f`. For any carrier already in `B0`, its cofactor contribution cannot be counted separately from `P0`; add a **fresh** multiple of `u` or `v`, respectively. At most two extra positions are necessary in total: one per carrier, either its own new position or a fresh cofactor multiple.
* If `s=t=w` and `w∉B0`, add `w` (one position). Its `p`-valuation is at least `max(e,f)`, and its p-free factor is divisible by `lcm(u,v)`. There exists a second distinct multiple of `p^{min(e,f)}` in `I`, because the two distinct source integers `a,b≤M` imply `⌊M/p^{min(e,f)}⌋≥2`. Add that multiple if it is not already selected (at most one position). Finally, add a fresh multiple of `gcd(u,v)` if necessary (at most one position). All additional demands are now supplied: `p^{e+f}uv = p^{max(e,f)}p^{min(e,f)}lcm(u,v)gcd(u,v)`.
* If `s=t=w∈B0`, its `p`-valuation is already at least `max(e,f)`. Add a different multiple of `p^{min(e,f)}` if necessary (at most one position), then fresh multiples of both `u` and `v` (at most two positions). The `p`-free `P0` is still fully covered by the old positions.

Every fresh multiple of a cofactor (or its gcd) exists: `u,v,gcd(u,v)≤M/p`, so each has at least `p≥13` multiples in `I`. At the point it is requested no more than 11 positions have been selected. Thus at most `9+3=12` positions are needed.

**Conclusion:** in any obstruction, every prime `p≥13` divides **at least three distinct** sources.

## Lemma 3. Pair deletion forces `12p²>M`

Suppose `p≥13` divides at least two sources `a,b`. Cover the seven others in ≤9 positions. If `12p²≤M`, the following three factors can be placed in three *fresh* positions, successively:

```
position 10: a/p  (10a/p ≤ M because p≥13)
position 11: b/p  (11b/p ≤ M because p≥13)
position 12: p²   (12p² ≤ M by assumption)
```

At step `j`, `⌊M/h_j⌋≥j`, so an unused multiple of `h_j` exists. The product of the three factors is `ab`. This gives 12 positions, a contradiction. Hence each prime `p≥13` in a hypothetical obstruction satisfies **`12p²>M`**.

## Lemma 4. Every source contains at most two large-prime occurrences

Count repetitions of primes `p≥13`. If a source had three of them, then it would be at least `13³=2197`; hence this cannot occur for `M<2197`. For `M≥2197`, Lemma 3 gives each such prime `p>sqrt(M/12)`. Their product would exceed `(M/12)^{3/2}>M` (because `M≥2197>12³=1728`). Either way this is impossible.

Therefore every source has **large part** of one of the forms `1`, `p`, `p²`, `pq`, with `p,q≥13` prime. If `v` is the number of distinct large primes, Lemma 2 and the 18 available occurrence slots yield `3v≤18`, so `v≤6`.

## Lemma 5. Squarefree three- or four-source support with `p²≤M` is impossible

Suppose `p≥13` divides exactly three sources `p u_i`, with `p∤u_i`, and `p²≤M`. The other six sources are p-free and admit a cover `B0` of ≤8 positions. Choose a multiple `w` of the full source `p u_1`. If `p²∤w`, choose a distinct multiple `z` of `p²` in the interval. If `p²|w`, choose a distinct multiple `z` of `p` instead; one exists because at least three source numbers ≤M are divisible by `p`. Together `w,z` contribute at least three copies of `p`, regardless of whether they were in `B0`. If `w` is new, add fresh multiples of `u_2,u_3` (two): at most two carriers plus two cofactors, hence four additions. If `w` belongs to `B0`, add fresh multiples of all three `u_i`; at most one further carrier plus three cofactors, again four additions. Each cofactor has ≥13 multiples in the interval, so freshness holds. Thus 12 suffice.

The four-source case is analogous and uses `g(5)≤6`. Choose a full-source multiple `w` of one `p u_i`. We need four p-units. If `w` has exactly one p-unit, use one p²-multiple and a third distinct p-multiple; if `w` has at least two p-units, use two other distinct p-multiples. All chosen auxiliary p-multiples can be distinct: the four distinct source numbers divisible by p imply the interval has at least four p-multiples. Thus at most three carrier positions supply four p-units. If `w` is new, at most three fresh cofactors remain, costing at most `3+3=6` new positions. If `w` was already selected, add four fresh cofactors but only at most two auxiliary carriers, costing at most `2+4=6`. The five-source old cover uses at most six positions; hence the total is at most twelve. The freshness argument uses `⌊M/u_i⌋≥p≥13` as before.

## Lemma 6. At most five distinct large primes

Suppose, instead, that there are six. Each must occur in at least three sources (Lemma 2). Since nine sources contain at most 18 large-prime occurrences in total (Lemma 4), every source has **exactly two** and every large prime occurs in **exactly three different sources**, always to exponent one. There must be a source `pq≤M` with `p≠q`, and at least one endpoint has square ≤M. Lemma 5 excludes this. Therefore **`v≤5`**.

## Lemma 7. Exact shape of the five-large-prime incidence multigraph

Suppose `v=5`, and let `l` be the number of large primes with `p²≤M`. By Lemma 5, each of these must have at least four *occurrences with multiplicity*: with exactly three they would have squarefree support three, which is impossible. The other `5−l` primes have ≥3 occurrences. Consequently `15+l≤18`, or `l≤3`.

Distinct primes `q>sqrt(M)` cannot occur in one source together. Each requires at least three **distinct** source indices. If `l≤1`, at least four such primes require at least twelve source indices, impossible. If `l=2`, three such primes require all nine sources, each containing one of these primes. No source could then contain a square of either of the two smaller large primes (that would be three large occurrences). Without a square, each of these two smaller primes must occur in at least five sources, by Lemma 5 (which excludes squarefree supports three and four). But there are only nine available second-large-prime slots altogether, whereas they need ten. Thus `l≥3` and hence **`l=3`**.

Total high-prime occurrence count is therefore exactly 18. There are three primes `p_1,p_2,p_3` with `p_i²≤M` and two primes `q_1,q_2>sqrt(M)`. Each `p_i` has exactly four occurrences, including precisely one source with large part `p_i²` (two p-units) and two sources with large part `p_i q_j`. Each `q_j` appears in exactly three sources. All nine sources have two large-prime occurrences.

The six edges between `{p_1,p_2,p_3}` and `{q_1,q_2}` form a **bipartite multigraph** with row degrees `(2,2,2)` and column degrees `(3,3)`. Up to permuting the vertices, there are **two** possibilities:

1. Simple `K_{3,2}`: one edge `p_i q_j` for every pair.
2. Double-edge pattern: two copies of `p_1 q_1`, two copies of `p_2 q_2`, and one copy each of `p_3 q_1`, `p_3 q_2`.

In the double-edge case, the actual source integers remain distinct because equal large parts have **different p-free cofactors**. Treating the graph as necessarily simple would be erroneous.

For example, the nine distinct integers

```
169, 289, 361, 559, 1118, 799, 1598, 817, 893
```

have `M=1598` and the second high-part pattern with `p_i=13,17,19` and `q_j=43,47`. They also satisfy `12p²>M` for all their large primes, confirming that the double-edge pattern is not excluded by the earlier gate. This illustrates the possibility of repeated edge types; it is **not** a counterexample to `g(9)≤12`.

## What is NOT proved

The lemmas exclude no six-or-more-large-prime cases and classify the five-large-prime case, but **do not exclude all instances with three, four, or five large primes**. We did not complete the mixed-source interval analysis for `121≤M<20000` or establish the global `g(9)≤12`. Under the supplied report's asserted `M≥20000` theorem, and under the previously proven values `g(7)=9`, `g(8)=11`, current status is `12≤g(9)≤13`. A claim that `g(9)=12` would presently be unsupported.

The file `verify_lower_examples.py` independently reproduces the explicit lower-bound interval with `τ=12` claimed in the attached report (it checks the required valuation geometry and an attaining cover). The source file's earlier name was `common_window.py`.
