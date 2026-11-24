# Independent audit of the finite three-large-prime envelope

Auditor: parallel agent `g89_proof`, 24 November 2026.

Reviewed implementation: `g7_exact/finite/three_large_envelope.cpp`.
Recorded run: 6294 prime triples, 656193 eligible maxima, 850366 core classes; 850364 closed by envelope predicates and two passed to explicit-source certification.

## Verdict

PASS for the coverage and sufficiency arguments implemented in the envelope, conditional on the separately proved reductions to M<=24696, three large primes, source support at least four, and source large degree at most two. This review does not itself certify the two explicit residual classes.

## Coverage

The least-maximum counterexample has gcd one. Its maximum-sum representative is upward closed under multiples. If a<=M/7, all seven multiples a,...,7a lie in the seven-element set (and an eighth would be impossible), giving a common divisor a>1. Thus the strict filter a>M/7 is justified; upward closure without the gcd-one reduction alone would only imply a>M/8.

There are exactly 46 nonnegative ten-core count vectors of total seven with support at least four in each of three primes. Every pair core is present: two supports of size at least four intersect in a seven-element source set. At most one large prime can exceed sqrt(M), because two such primes cannot occur together and their two supports would require eight sources. Hence, for sorted p<q<r, q^2<=M and qr<=M. The square reduction gives M<9p^2. These justify all triple-loop limits and lo=qr, hi=min(24696,9p^2-1).

Every source maximum has form d*s with d among the ten cores and s 7-smooth. The enumerated set of maxima therefore contains every possible actual M. The available cofactor pools impose d*s<=M and d*s>M/7, and source distinctness is enforced by selecting different cofactors within a core group. The contains-M test is necessary but intentionally may overinclude classes; it cannot exclude a true source set.

## Cofactor upper envelopes

For a potential failing small prime t, remove all smaller prime factors from each available cofactor. The product of the largest k remaining numerical values bounds the t-and-higher part of any actual k-element cofactor subset. Different core groups can be bounded independently.

For a prescribed source, choose the largest actual cofactor in that core group. All other actual cofactors lie below the largest available cofactor, so the `minus` array, which excludes the largest available cofactor before taking the largest k-1 rough parts, is a valid upper bound. It does not assume that a packing of a numerically larger integer proves a packing for all smaller integers.

## Large-core covering costs

The independent per-prime cost uses the nested guaranteed counts floor(M/p) and floor(M/p^2). Their sum against min(k,count) bounds what the k richest available p-multiples supply. Higher target valuations can only improve the guarantee.

For a prescribed point z, the code removes it from the first two guaranteed count levels according to its valuation, credits that valuation, and maximizes over valuations 0,1,2 compatible with the prescribed core. Actual valuation >=3 is dominated by the valuation-2 branch: the removed first two counts are unchanged and the actual residual demand is smaller.

Covers for different large primes can be united because their required factors are coprime. The alternative bank bound m+1 is valid with a prescribed point. A spare pair bank can avoid the unique potential triangle point; without a prescription any spare pair bank suffices, and with a prescription a different spare pair bank suffices. Accidental membership of the prescribed point in another pair's divisibility class does not require that other bank to select it.

## Merging large and small covers

The large-prime product is coprime to the complete small-prime product, so independently obtained covers can be united even when their point sets intersect. If one selected point z is credited with a small cofactor, the remaining small cover needs to avoid only z. It may overlap every other large-core point. Thus the unrestricted small bin capacities M,M/2,... and the prescribed-point capacities M/2,M/3,... are correct.

The one-smooth-source predicate follows the separately proved two-credit-points argument in `ZERO_SOURCE_ENVELOPE.md`.

## Greedy threshold arithmetic

If descending prime insertion fails at t<=7 in a bin of integer capacity floor(M/k), its current product is at least both t and floor(M/(k*t))+1. Consequently the unplaced t times all current bin products gives the threshold used in the code. Passing requires every rough-product envelope to be strictly below this threshold. The direct one-bin tests use the actual numerical bound Q<=capacity and are also valid.

Every used bin capacity exceeds seven in this finite three-prime range. Empty-bin exceptions therefore do not undermine the `max(...,t)` lower bound at a failed insertion. All source/cofactor products and threshold products fit unsigned 128-bit arithmetic at the stated cutoff; intermediate integer core multiplications break their loops before any 32-bit overflow is possible.

## Residual work

The recorded two classes are p=11,q=13,r=23, M=1012 or 1035, with counts (0,0,0,2,0,0,0,3,1,1) in core order (1,p,q,r,p^2,q^2,r^2,pq,pr,qr). Their subsequent explicit source enumeration produced 17640 raw choices and 1096 eligible gcd-one, upward-closed sets. `verify_three_residual_independent.py` independently regenerated these sets and verified every one of the 1096 nine-slot certificates. Result: PASS.

The complete isolated replay `verify_all_three.py` subsequently regenerated both support-three finite families, checked all 445 certificates, rebuilt and reran the entire C++ envelope, checked the exact two residual classes, and ran the independent residual checker. Result: PASS. The audited C++ source SHA-256 is `f4491c8eb8455954251c0417f0203dcefc3c6cc74035be6139be3949cb11076f`.
