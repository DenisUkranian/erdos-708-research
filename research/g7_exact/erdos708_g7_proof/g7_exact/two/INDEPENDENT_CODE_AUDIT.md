# Independent audit of the two-large-prime finite implementation

24 November 2026. Code reviewed: `envelope.cpp`, `enumerate_nontrivial.cpp`, and `full_demands.py`.

## Envelope

The prime-pair range p<q, pq<=M<9p² is complete after elimination of actual source patterns with no pq core. In particular q<3sqrt(M)<472, so the code's q<=1500 range is a harmless superset. The source filter a>M/7 follows from the least-M gcd-one argument and maximum-sum upward closure.

The six core types and support counts are correct. Source supports seven are excluded by gcd one. The z<=3 restriction on zero-core sources is legitimate: z=4 would leave exactly three nontrivial sources, all with core pq, and the smaller prime p would be a low support-three prime with three simple occurrences, already eliminated by the square-gain lemma.

Every scalar coefficient product is an upper bound obtained by taking the largest eligible integer coefficients within each group. If a group supplies the prescribed coefficient, deleting its absolute largest eligible coefficient gives a valid upper bound for the product remaining after deleting the largest actually selected coefficient. Rough bounds use the same deletion before sorting rough parts, which is also valid.

The forced single-prime calculation considers every possible valuation at the prescribed point up to the full demand. It subtracts at most one point from each relevant prime-power count and credits that point's actual valuation. Larger valuations already satisfy the demand and require zero further points. The bank bound for two prime atoms is at most the number of nontrivial sources and can retain a prescribed full-source point.

The old zero-core sources are covered by B0 in at most g(z) points. If a prescribed point z0 overlaps B0, the one-point cardinality saving pays for a fresh copy of its coefficient outside B0. Consequently the remaining smooth-factor cover must avoid only B0 and the distinct coefficient-credit point, as implemented. Other core points may overlap the smooth-factor cover because their large-prime and small-prime allocations are coprime.

Descending 7-smooth packing uses exact integer thresholds. All called capacity lists admit every small prime in an empty bin. Products are safely within unsigned 128-bit range on the actual input bounds.

## Bad-pair graph and nontrivial-source enumeration

A pair is removed only after an explicit factor assignment into capacities floor(M/7), floor(M/8), floor(M/9) succeeds. Cover the other five sources in at most six points, then choose three fresh multiples of those factors. Thus every removed pair has a universal nine-point certificate.

The nontrivial source universe is complete. Repeated upward-closure pruning is valid: any required multiple of a nontrivial source remains nontrivial, and if it has been excluded then no closed counterexample can contain the original source. The grouped clique recursion selects distinct sources with exactly the required core counts and includes M when its core is nontrivial. Its bitsets have an asserted sufficient bound.

The `small_pack` routine's successes are sound: explicit factor placement, an exhaustive divisor test for two bins, or independent single-prime supply bounds after deleting at most f forbidden positions. The latter count is at least max(floor(M/p^e)-f,0) at every power level, and unions across prime coordinates are valid.

The positive cache depends on z and the entire nontrivial product, represented by its exponents at 2,3,5,7,p,q. This is valid even if the original successful proof used a source-specific anchor: the previous distinct nontrivial source factorization is a reusable auxiliary factorization of exactly the same demanded product and works with any permitted old zero-core source set. The small exponents fit their six-bit fields because every nontrivial cofactor is below 3sqrt(M)<472, giving an exponent sum at 2 of at most 56. Large-prime exponents are at most 14 and fit their four-bit fields.

## Expansion to full seven-source sets

The nontrivial residual output has only z=0 or z=1. With one zero-core source b, upward closure forces b>M/2, since 2b would otherwise be a second zero-core source. If M is not already nontrivial, b=M; otherwise all eligible 7-smooth b strictly below M are enumerated. The smooth list below 665 is sufficient because all z=1 residual maxima are at most 558; z=0 cases do not use that list.

Only common-factor sets and certified good pairs are removed. Assertions check seven distinct sources, the actual maximum, and full upward closure. The exponent vector is correctly ordered as (2,3,5,7,p,q).

The final coordinatewise dominance compression is complete. Sorting vectors by total exponent sum ensures a later vector cannot strictly dominate an earlier retained one; every discarded vector is dominated by a retained one. Covers depend on the full product demand, so retaining one source representative per equal vector is valid.

## Recorded verification results

The envelope examined 2,980,414 eligible core classes. It certified 2,784,139 directly and retained 196,275 classes in 50,660 distinct parameter configurations. The source-level enumeration found 112,998 nontrivial bad-pair cliques; 67,663 passed its further universal criteria, leaving 45,335 rows. Expanding those rows and checking the remaining good pairs produced 116,394 full source sets and 33,939 distinct product demands. Coordinatewise dominance reduced these to 24,511 frontier demands. All 24,511 have valid certificates with at most nine cumulative-GCD slots.

The separate independent checker `verify_demands_independent.py` rebuilt the full-demand expansion, checked coverage of all 33,939 demands, and verified all 24,511 slot certificates. Its recorded result is `verify_demands_independent.json`, with status `PASS`. The complete portable replay `verify_two.py` also returned `PASS`; its result is `verification_result.json`. These executions are additional checks alongside the source-code and mathematical audit above. The largest actual residual maximum is 665, within the proven finite range 24,696.

The source hashes recorded by the complete replay are:

| Source | SHA-256 |
|---|---|
| `envelope.cpp` | `a12d9a4312871a8afaf7ed9af4c8bca179403d30f4bd60963911f2f448fe5cc6` |
| `enumerate_nontrivial.cpp` | `a3e946007e475550b384cc63221f63745ee38920f313b25f191a6ff24a5b3c50` |
| `full_demands.py` | `f670ba47ed075c8923d55caba314ca210c52378f7af12a8993077ed0d4e67785` |

**Verdict:** no mathematical or implementation flaw was found in these three programs. Given the stated structural reductions, the two-large-prime finite branch is completely covered. All retained demand certificates and the demand-to-frontier coverage have passed the separate independent verification.
