# Erdős 708: attempt at J_weak (23 November 2026)

## Status

**J_weak is NOT proved.** The unrestricted g(n) <= (2+o(1))n asymptotic and the exact 2n assertion are not claimed. No new finite g(n) value is computed. No restricted source class is presented as completion.

## Main deliverable

- `erdos708_jweak_attempt.pdf`: ten-page synthesis with full proofs of the main new inequalities and an explicit remaining obligation.
- `erdos708_jweak_attempt.tex`: editable mathematical source.
- `prior/erdos708_global_gap.pdf` and `.tex`: preceding normalization report, including the definition of J_weak and the conditional contradiction.

## Proved statements and their scope

1. `combinatorial/OPTIMAL_BAND_DELETION.md`: exact joint objective loss, sum_j loss_j <= L_raw, for arbitrary disjoint coordinate blocks at an actual optimum. Includes threshold-one primal mass, derived weight gaps, normalization costs, and the remaining error-multiplier warning.
2. `audit/GLOBAL_SPARSE_MEAN_AND_HOTSET.md`: cold initial segment, exponential moment, weighted mean <=1+o(1) along sparse optimal-obstruction sequences, and exact capped-core moment estimates.
3. `analytic/SPARSE_HOT_BONFERRONI.md`: finite aggregate substantial-prime reciprocal bound, with the actual arithmetic rounding error.
4. `analytic/SPARSE_BOUNDED_HEAVY_OCCURRENCES.md`: weighted exceptional-source deletion and bounded substantial occurrences per retained source. The synthesis uses the sharper t=s+1 consequence, giving at most 3s+1 occurrences; the original note records the valid coarser 4s version. Neither bounds global prime support.
5. `combinatorial/HOT_DIVISOR_PARTITIONS.md`: prescribed-prime divisor and demand bounds.
6. `audit/ATOM_LP_MINIMALITY_AND_COMPONENT_BANKS.md`: a separate stronger prime-power-count LP, its own minimal class and cubic ambient gate, and exact component-bank union bounds. These conditions are NOT silently transferred to a raw-minimal instance.
7. `analytic/DENSE_LIGHT_CORE_CONCENTRATION.md`: replacement of the diffuse core by a constant in the dense branch, with the remaining shifted heavy-profile inequality unproved.

## Excluded shortcuts, not counterexamples to J_weak

- `combinatorial/BOUNDED_OCCURRENCE_H1_BARRIER.md`: actual integer intervals refuting a universal O(k^2) same-threshold H1 discrepancy estimate, even with four occurrences per prefix integer. The exact finite raw deficit is 4321.
- `audit/FOURIER_SAME_THRESHOLD_BARRIER.md`: a different same-threshold Fourier obstruction and its scale limitation.
- `analytic/JOINT_GLUING_DIAGNOSIS.md`: actual arithmetic examples showing why active-part fibre counts and active-only carrier multiplicity bounds do not follow from bounded active occurrences. These examples fail full optimal row balance and do not refute the requested lemma.

## Reproduce the finite certificate

From this directory run:

```sh
python3 combinatorial/verify_bounded_occurrence_h1.py
```

The verifier uses only the Python standard library. It checks primality, CRT conditions, exact divisibility counts, and all relevant raw power tails without enumerating the very long interval. Its expected status is PASS. This is a verification of the auxiliary counterexample only, not a computational proof of Problem 708.

The main analytical inequalities were independently cross-checked by collaborating agents. This is not external refereeing or formal verification. The ten-page PDF was compiled without missing references or overfull boxes and visually inspected.

## Remaining obligation

A single uniform arithmetic estimate must control the retained source demand jointly with overlapping hot banks and the original tight demand rows. The positive residual demand in the exact identity in Section 9 of the synthesis is still not bounded by (2+2delta)|G|+o(m). The sparse and dense branches both retain an unresolved joint hinge estimate.

All final files are listed in MANIFEST.json with SHA-256 hashes. Intermediate renderings and LaTeX build files are excluded.
