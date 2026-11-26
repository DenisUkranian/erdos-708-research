# Twelve routes towards the coefficient two

This round addresses the at-most-cardinality Erdős–Surányi problem. In an M-point positive interval I, τ is the minimum number of distinct positions covering the product of n sources A⊆[2,M], M=max A. H is the stronger minimum for the separate counts of multiples of all prime powers. We obtain exact product costs, shift-uniform results on restricted families, and necessary conditions for an obstruction. The project's [uniform upper bound](../uniform_three_2026_11_26/README.md) remains (3+o(1))n. The coefficient-two upper bound for unrestricted A and I remains open.

| Route | Result of this round | Unresolved step |
|---|---|---|
| 1. Two blocks | Escaping-cycle lemma, exact rank-two characterization, and rank-three minimum 4 versus 5 with fixed full blocks | Bound the total cost of cycles whose alternate multiples are occupied |
| 2. Credit at occupied sites | One-cycle placement condition and an exact weighted matching for re-pairing atoms from arbitrary rows | Prove enough savings on all outstanding tokens |
| 3. Dual prices | Exact Φ≤2n on reciprocal-sparse support, including repeated powers; one common arbitrary price on any support gives 2n+o(M) | Two or more different prices on unrestricted supports, with relative error in sparse regimes |
| 4. Feasible signed polynomials | Explicit two-price rank-three polynomial and rational finite certificates with 6, 8 and 10 labels | Bound transferred coefficient error as support and feasible rank grow |
| 5. Prefix sieve | Disjoint quotient banks prove the entire requested (.30,.32) band, including all price choices and all source sizes, without additive error in Φ | Many interacting scales with large active reciprocal mass |
| 6. Rank-weighted Hall deficits | The original large fixed-deletion cut has a surplus of at least 17726307 on adaptive deletion; exact flows on twelve windows | Control all subfamilies simultaneously at successive ranks |
| 7. Density on progressions | Coefficient two for sources filling half a small union of divisibility progressions at every ambient density in M≤n², plus a forest criterion for general local covers | Extract a sufficiently complete inexpensive union from an arbitrary bad source |
| 8. Mixed marking | A mixture of deterministic marking pools repairs the full earlier normal-order obstruction for every shift | Handle many competing high-multiplicity supports at once |
| 9. Harmonic cuts | Polynomial lower bound on the number of complement runs of a bad cut; full-period maxima through M=12 | Scattered cuts depending on the shift |
| 10. Product valuation repair | Seven-row interval has τ=5 and H=7; two shifts with identical level data can have different orders of ordinary cost | Bound the product repair of arbitrary residuals in a worst shift |
| 11. Atypical sources | A fixed-gap violation in M≤n², n≤M/2 forces prime-power fibers with a fixed relative-density increase covering ≫_δ n/(1+log(M/n)) distinct rows | Cover enough rows with such fibers and control the remaining budget |
| 12. Counterfamilies | Exact centered complete-family formulas at every fixed rank; twin shifts for the very same A; exact small enumeration | No lower construction with asymptotic coefficient above two |

### Proofs and replay

* [Prices and the density increment](PRICE_AND_INVERSE.md).
* [Matching, marking, harmonic cuts and unions of progressions](MATCHING_AND_CUTS.md).
* [Exact products, centered twins and the small enumeration](EXACT_PRODUCTS.md).
* [Recorded output](REPLAY.txt). In this directory run the following with Python 3, NumPy and SciPy. The finite LP search uses HiGHS only for discovery and rechecks feasibility with rational arithmetic. The seven-row minimum uses exhaustive integer reasoning. The centered asymptotic conclusions follow from the proofs, independently of the numerical samples.

```sh
python exact_covers.py
python cuts.py
python profiles.py
python placements.py
```

In addition to the examples tabulated above, the replay tests all 602 genuinely mixed patterns with prices 0, 1/3, 3/4 on the first six primes, at five shifts for each M=30,120,504,1024. The canonical sum of the positive source excess is the maximum over all source subsets, including the empty set. None of the 12040 finite price/window tests violates the hinge comparison. The arithmetic tests include powers above the level-profile period.

### Remaining target

In the range n≤M/2 and M≤n², the density-increment result supplies, under a fixed-gap counterexample hypothesis, at least one prime-power fiber of growing size. Formula (3) in the matching note suggests a precise stronger obligation: either construct another direct cover, or find divisors d_i with s≤(1−ε)log_2(log n) for fixed ε>0 such that the size of their canonical union V plus the sum of ω(a) over exceptions is ≤2n+o(n). In the latter case the uniform bound follows immediately, intersections included. We have not proved this extraction. For example, disjoint prime rows in a sparse set can require many fibers while already admitting an elementary individual cover; alternative branches are essential.
