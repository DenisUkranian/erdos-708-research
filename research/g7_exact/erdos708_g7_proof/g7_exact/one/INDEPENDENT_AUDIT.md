# Independent audit of the one-large-prime branch

Date: 24 November 2026. Result: **PASS**, subject to the global reductions and the earlier small-n bounds stated in `ONE_LARGE_PROOF.md`.

This audit reviewed `close_one.cpp`, `skyline.cpp`, `verify_one.py`, and the mathematical statements behind every successful pruning condition. It also reran the portable verifier from source. Recompiling the enumeration is a reproducibility check; the justification of its coverage and of the pruning conditions is the separate mathematical and code review below.

## Complete configuration range

For a normalized counterexample, the source primes are 2,3,5,7 and exactly one prime P>=11. Every source has P-exponent at most two, and P has support between three and six. The lower support bound comes from the support lemma, and the upper one comes from gcd(A)=1. The inequalities P^2>M/9 and M<=24696 imply M<=min(24696,9P^2-1). Three distinct multiples of P require M>=3P. If M>=1890, the separate high-prime argument already closes M<9P, so retained P is at most 2744. If M<1890, M>=3P gives the stronger P<630. Generating all primes through 2744 is therefore complete.

The source list consists of every integer c, Pc, P^2c in the permitted range with c 7-smooth, without duplication. It also contains every possible maximum. The nonmaximum pool imposes only conditions already proved for a normalized counterexample: a>M/7 and compositeness. A prime source would be removed from the source set, the other six covered in eight points, and its one missing prime unit repaired in one point using the full interval's sufficient valuation.

## Cofactor envelope

The cofactor pool is a multiset: equal cofactors from distinct sources remain separate candidates. Remove one fixed occurrence of its largest numerical cofactor. In an actual selected group, prescribe a largest selected cofactor, choosing that fixed occurrence if it is present. Every unprescribed cofactor then belongs to the reduced multiset, whether or not the removed occurrence was selected. Taking the largest rough parts independently for each prime threshold gives a valid upper bound; it does not assume that numerical order of integers implies divisibility or packing monotonicity.

The one-bin bound compares the total cofactor product with its capacity. For two bins, if descending prime-factor placement first fails at q, both existing bin products exceed their capacities divided by q. They are nonempty, because all primes being placed are at most seven and both capacities are at least seven in the two-bin cases. Their integer lower bounds are exactly the `max(M/(j*q)+1,q)` expressions in the program. Including the failed q gives the stated strict threshold. Thus every support size omitted from the bitmask is universally covered. Reapplying the bound after candidate removal remains valid.

## Pair and closure enumeration

The pair test only returns success after constructing a full factorization of the pair product within M/7, M/8, M/9. Combining this with a six-point cover of the other five sources proves a nine-point cover. A false negative in its three packing orders merely retains additional candidates.

Upward closure forces every multiple of a selected source through M. The descending elimination is sound because every proper multiple is numerically larger and has already been processed. Missing or eliminated multiples invalidate the candidate. A successful pair among its forced sources also invalidates it.

The recursive enumeration keeps selected and available masks. Selecting the least available candidate adds all its forced multiples. A branch is rejected if a required new multiple has already been excluded, if more than seven sources would be selected, if too few compatible candidates remain, or if no permitted prime support can be attained. Intersecting all selected bad-pair neighborhoods enforces pair compatibility. Selected bits disappear from future availability because the adjacency relation has no self-loops. The loop also explores the branch excluding each candidate. Every normalized closed seven-clique therefore has its own sequence of least selected candidates and is reached. The final gcd check rejects only nonprimitive source sets, already excluded by normalization.

## Successful leaf tests

The first core test covers the P-free sources, uses a P-bank retaining a point for the largest selected cofactor, and covers the remaining cofactors while avoiding only the earlier small-factor cover and that credited point. This is legitimate because the other core points are allocated solely to P. If the prescribed point was already in the old cover, the saved union cardinality pays for a fresh cofactor point.

The second test covers the pure P-demand separately. Small-prime factors may overlap that cover and need avoid only the old small-factor cover. The guaranteed supply `sum_e min(k,floor(M/P^e))` follows from nested valuation level sets.

The third test divides all P-containing sources by P and applies the earlier g(d) bound in the consecutive interval of target P-multiples. Padding to at least d selected quotient points supplies the d removed P-units; there are at least d available quotient positions. It then covers the P-free source product with fresh points. This test uses no g(7) conclusion.

Separate prime covers can be united because their demands are coprime. Ordinary full-product packing is valid by the fresh-multiple bound. Every test returns success only under a sufficient theorem; their possible failure does not remove a case.

## Demand keys and exact domination

Each coordinate of a seven-source demand is less than 128; the largest possible one is at most 7*floor(log_2(24696))=98. Adding the seven-bit encodings therefore cannot carry into another coordinate. A cached successful demand applies to every source set with that same product and maximum.

The skyline procedure sorts vectors in descending lexicographic order. A previously processed vector has first coordinate at least that of the current vector. Reverse coordinates convert coordinatewise inequalities in the next three coordinates into three prefix inequalities. The Fenwick tree stores the largest fifth coordinate in the corresponding prefixes. A vector is discarded only if an earlier retained vector dominates all its coordinates. Discarding a dominated vector does not require inserting it: its retained dominator dominates every later vector it could dominate. This proves that the emitted antichain dominates all generated demands.

The verifier rebuilds both the unknown and independently covered maximal-demand files. It checks all slot lists with unbounded integers and independently reruns the successful leaf conditions in Python for all 120,285 other maximal demands.

## The hand-proved demand at M=55

The remaining target is 2^4*3^9*5^2*11^4. Two consecutive multiples of 27 contribute 3^6 and at least one factor 2. Of those two points at most one is a multiple of 18, so among at least three multiples of 18 there is a fresh one. A fresh multiple of 6 is also available. These four distinct points supply 2^3*3^9. A multiple of 50 supplies 5^2 and a further factor 2; if that point is already among the four, its 5^2 is available and a fresh even point supplies the extra factor 2. This gives five points for the small-prime demand. Four distinct multiples of 11 cover the remaining coprime demand, and their union with the five-point set has at most nine members. The proof does not require a CRT search.

## Replayed result

An independent invocation of `python g7_exact/one/verify_one.py` completed successfully in 20.528 seconds, compiling the enumerator from the supplied source. It reported:

| Item | Count |
|---|---:|
| Initial (M,P) configurations | 59,982 |
| Configurations containing surviving normalized source sets | 623 |
| Actual source sets enumerated | 7,006,656 |
| Distinct generated product demands | 658,925 |
| Maximal demands independently covered by the other tests | 120,285 |
| Explicit cumulative-GCD certificates | 252,175 |
| Remaining hand-proved maximal demand | 1 |

All 252,175 slot keys matched exactly the regenerated non-hand maximal demands. Every cumulative-GCD inequality and final product divisibility passed. No uncovered demand, missing certificate, or failed program assertion remained.
