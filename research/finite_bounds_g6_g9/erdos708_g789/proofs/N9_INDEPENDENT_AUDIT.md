# Independent audit of the proposed upper bound g(9) <= 14

Date: 2026-11-24.

## Scope and conclusion

The prime-deletion reduction, analytic tail, Pareto dynamic programming invariant, ordinary-bin criterion, prime-union criterion, and cumulative-GCD fallback criterion are mathematically sound under the prior bound `g(8)<=12`.

The implementation's 74 fallback certificates pass a separate exact integer checker. Every eligible source-demand vector for the entire small range `M<=240` was independently generated without Pareto pruning, and all 588,195 vectors are dominated by actual retained frontier vectors. The independent global checker maintained by the other reviewer has now returned PASS for every eligible maximum below 24,206. Its report is `results/g9_independent_result.json`: 701 eligible maxima, 500 covered by the whole-maximum rough envelope, and 201 processed further; 137,818,182,175 source subsets are represented through exact enumeration and certified branch pruning, with 3,611,037 distinct leaf demands checked individually. This global checker does not import the Pareto routine.

## Prime deletion

Assume `g(8)<=12`. Remove any `a` from a nine-element source set. A cover of the remaining eight inputs uses at most 12 interval points. If `p|a` and `a/p<=M/13`, there are at least 13 multiples of `a/p` in the target interval, so an unused one can be added. The resulting product covers `(product A)/p`.

If the remaining single p-unit is still missing, an unused point divisible by p exists: otherwise the selected set would contain all p-adic valuation in the interval, contradicting

`product A | M! | product_{b in I} b`.

Thus at most 14 points suffice. In particular, all active primes in a counterexample would be at most 12, hence among `2,3,5,7,11`. Every source element would satisfy `13*a>M*p_max(a)`. Also every source element must have at least three prime factors with multiplicity: deleting an element with at most two prime factors can always be repaired one missing prime unit at a time using at most two extra points.

## Infinite analytic tail

For fourteen bins with capacities `floor(M/j)`, process all demanded prime factors in descending order. If the next prime p cannot be placed and `p<=floor(M/14)`, each current bin product is at least

`max(floor(M/(j*p))+1,p)`.

The total p-rough demand is therefore at least

`T_p = p * product_{j=1}^{14} max(floor(M/(j*p))+1,p)`.

On the other hand, the total p-rough demand is at most `M^9`. At the largest allowed prime, 11, the sharper bound `11^D<=M^9/9!` follows by arranging the powers `11^{v_11(a)}` in descending order: the j-th one is at most `M/j` because the corresponding j distinct source integers are all multiples of that power.

Since `T_p>M^14/(14!*p^13)`, the following exact inequalities are sufficient:

`d_p*M^5 > 14!*p^13`, where `d_11=9!` and all other `d_p=1`.

All five inequalities hold at `M=24285`, and their left sides increase thereafter. Also `11<=floor(24285/14)`. Thus every larger M is covered. The finite scan with `M<24286` overlaps this tail, leaving no endpoint gap.

## Pareto invariant and code review

The dynamic program processes distinct eligible source integers in order, updating the number-selected index in descending order. Before processing a new integer, every retained vector represents a subset of the already processed integers. If vector u dominates vector v coordinate by coordinate, then adding any future set of source integers preserves that dominance. Thus retaining only coordinatewise maximal vectors is valid and does not conflict with distinctness.

The five-dimensional skyline code sorts vectors in descending lexicographic order. Every earlier vector has first coordinate at least the current first coordinate. Its three-dimensional Fenwick structure tests whether an earlier vector has coordinates 2,3,4 at least as large and coordinate 5 at least as large. The inverted indices implement exactly these three upper orthants. Skipped points are dominated by retained points, preserving transitivity. Duplicate vectors are removed before scanning. No exponent or coordinate reaches the signed-32-bit limit used at the Python/C++ interface.

The independent reference implementation uses direct coordinate comparisons, with no Fenwick tree. It agreed with the target implementation on 350 randomized and adversarially augmented test sets, including duplicates, zero vectors, and long dominance chains.

## Independent finite audit through M=240

`audit_frontier.py` trial-factors every integer in this range independently of the source generator. It constructs **all** exponent-demand vectors for exactly eight eligible smaller inputs plus M, without discarding dominated vectors at any DP stage. For every resulting demand it checks coordinatewise coverage by the proposed frontier, and checks that all frontier vectors are actual achievable demands and form an antichain.

Result: PASS for all 61 eligible maxima, covering 588,195 exact distinct demand vectors.

This is a complete check of this bounded range; it is not being presented as a universal result by itself.

## All 74 cumulative-GCD certificates

`audit_n9_certificates.py` independently checks that the fallback list matches every failed frontier demand exactly once. For each listed slot sequence `h_1,...,h_l`, it verifies

- `l<=14`;
- `1<=h_j<=M`;
- `gcd(h_1*...*h_{j-1},h_j)<=floor(M/j)`;
- `product h_j` is divisible by the stated complete prime demand.

These conditions guarantee a distinct target selection in every interval of length M. If an unused multiple of a slot exists, choose it. Otherwise the old target product is divisible by both the old source-slot product and the new slot, hence by their least common multiple. There are at least j multiples of their gcd, so a fresh one is available to restore the missing overlap.

Result: PASS for all 74 fallback demands at 15 maxima, all with `M<=240`.

## Additional implementation checks

The prime-union formula is valid because, for a fixed prime p, the sum of the k largest interval valuations equals the sum over prime-power levels of the minimum of k and that level's actual count. Each actual count is at least `floor(M/p^e)`. Covers for separate primes can then be united, with total cardinality at most the sum of their individual cardinalities.

A reported success from the ordinary packing heuristic is a valid certificate regardless of the floating-point comparisons used to choose a bin: factor placement and capacity inequalities themselves are checked using exact integers. The heuristic can miss a packing, but cannot certify an invalid one.

The rough-envelope shortcut uses the eight largest eligible p-rough values plus the p-rough part of M. This is an upper bound for every actual eight-element choice, even though the maximizing choices can differ with p. Hence strict comparison of this envelope with every `T_p` legitimately eliminates all source sets at that M.

## Artifacts

- `audit_frontier.py` and `frontier_audit.json`
- `audit_n9_certificates.py` and `n9_certificate_audit.json`

The separate lower-bound witness files prove `g(9)>=12`. This audit does not prove `g(9)=12`; the bounds 12 and 14 remain different.
