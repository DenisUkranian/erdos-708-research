# Erdős Problem 708 — Research Archive and Proof Certificates

**26 November 2026, three comparable primes.** An [exact-bank transfer](research/sparse_threshold_2026_11_26/TRIPLE_TRANSFER.md) covers the identified triple family in at most $2m-1$ positions on its own. In a mixed source the replacement uses two positions per exceptional row and preserves the other main labels by splitting their credited factors. This proves $H(A,I)\le 2n+O(n^{1-c})$ for arbitrary sources when $M\ge n^{10000/8201}$. The full asymptotic remains open.

**26 November 2026, sparse sources and the cost of adding full cells.** A [level-cover proof](research/sparse_threshold_2026_11_26/README.md) gives a bound of $2n+O_\varepsilon(n^{1-c_\varepsilon})$ on every interval when $M\ge n^{11/9+\varepsilon}$. A separate exact construction shows that adding complete prime-pair cells to an optimal residual cover can cost asymptotically three positions per added source. The unrestricted coefficient two remains open.

**26 November 2026, exact covers and residual obstructions.** The [new density certificate and structural results](research/density_and_gluing_2026_11_26/README.md) give exact two-per-row covers for all sufficiently large instances of density at least 39.20%, a reduction of every fixed-gap counterexample to rows with arbitrarily many distinct large prime factors, and simultaneous exact covers on polynomially many selected intersections. The unrestricted coefficient two remains open.

**26 November 2026, progression selection and inverse results.** [Routes 7 and 11](research/fiber_selection_2026_11_26/README.md) give a density increment on unions of prime-pair progressions for any putative fixed-gap violation, shift-uniform covers for source sets determined by prime valuations, and a counterfamily to unrestricted full-union selection with singleton repairs.

**26 November 2026, twelve proof routes.** [New proofs and exact replays](research/twelve_routes_2026_11_26/README.md) give a shift-uniform two-budget price bound on reciprocal-sparse supports, a two-budget cover for dense subsets of unions of progressions, a necessary density increment for a counterexample, and exact centered product costs. The general coefficient two remains open.

**26 November 2026, uniform upper bound.** The [full proof](research/uniform_three_2026_11_26/README.md) gives g(n) ≤ (3+o(1))n at every source density and every interval shift. The argument assigns a cofactor to each row and controls collisions of pairs of primes using a second moment. The coefficient-two asymptotic remains open.

**26 November 2026, full-period shifts.** [Simultaneous almost-all-shifts theorem and deterministic extensions](research/unrestricted_shifts_2026_11_26/README.md). Outside a vanishing proportion of shifts, one common bound gives (2+o(1))n for every family of size much larger than M(log log M)²/log M. The centered result now allows every fixed power of log M at all densities. A proof for the worst shift and unrestricted sources is still missing.

**26 November 2026, cofactor matching.** A [written proof](research/cofactor_flow_2026_11_26/README.md) gives the sharp coefficient two at every source density for intervals with start within M(log M)^α of a multiple of lcm(A), for fixed α<13/34, and a 2n−1 bound for fixed reduced rational centers under the stated hypotheses. Arbitrary shifts remain open.

**26 November 2026 update.** [Publication audit, external results and proof target](research/audit_2026_11_26/README.md). The [density package](research/density_2026_11_26/PROOF-3960.md) gives a written eventual exact 2n bound for n/M ≥ 0.3960 with replayed arithmetic certificates. The general asymptotic remains open.

**Status (25 November 2026): Open in general.** This repository collects our recovered work on the Erdős–Surányi interval-product problem, with historical experiments, exact finite certificates, full research reports, counterexamples to intermediate claims, and reproducible scripts. An archived claim is not automatically an established theorem.

## Problem

Let `A` be a set of `n` distinct integers at least 2, and put `M = max(A)`. For any interval `I = {x+1, ..., x+M}` with integer `x >= 0`, let `tau(A,I)` be the minimum cardinality of `B subset I` such that `prod(A)` divides `prod(B)`. Define `g(n) = sup tau(A,I)` over these choices. The product uses each chosen interval position at most once.

Central goals include the asymptotic estimate `g(n) <= (2+o(1))n` and the stronger exact upper bound `g(n) <= 2n`. **Neither is proved by this repository.**

## What is included

- [`research/archive_2026_11_24/`](research/archive_2026_11_24/): preserved historical consolidation (with four third-party source files omitted in the public release) of reports, historical work, corrected arguments, scripts, and provenance. Start with `ERDOS708_ALL_2026-11-24/CURRENT_STATUS.txt` and `CORRECTIONS_LEDGER.csv`. This was collected before the later finite-case update.
- [`research/finite_bounds_g6_g9/`](research/finite_bounds_g6_g9/): a 24 November finite-case package, recording `g(6)=8`, `9 <= g(7) <= 10`, `11 <= g(8) <= 12`, and `12 <= g(9) <= 14`. **Its g(7) interval is superseded by the later g(7) proof package.**
- [`research/g7_exact/`](research/g7_exact/): later 24 November *computer-assisted claim* `g(7)=9` with exact integer certificates, C++/Python verifiers, and replay logs; external dependency on the stated `g(5)<=6` result. This compilation has not independently rerun the entire verifier and does not imply peer review or Lean formalization.
- [`research/g8_exact/`](research/g8_exact/): the later computer-assisted exact-case result **g(8)=11**, conditional on prior g(5), g(6), and g(7) upper bounds; proof in English, C++/Python verifiers, 57,487 universal certificates, and 28 exact CRT residual checks. Independently replayed on 24 November 2026.
- [`research/asymptotic_2026_11_25/`](research/asymptotic_2026_11_25/): new audited conversation consolidation, component lemmas, external-research comparison, corrections, and precise remaining gates.
- [`research/g9_12_or_13/`](research/g9_12_or_13/): recovered narrow nine-source bounds **12 ≤ g(9) ≤ 13**, with unconditional lower witness and upper bound conditional on the prior g(8) proof. The original verifier was independently replayed on 25 November 2026.
- [`research/recovered_2026_11_25/`](research/recovered_2026_11_25/): all eight recovered original ZIP packages, with complete code, data and logs preserved byte-for-byte in a verified split archive; restore using the included Python script.
- [`research/g9_followup/`](research/g9_followup/): inventory and scope audit of the subsequent partial upper-12 reductions (not a proof of exact g(9)).
- [`research/two_bin_certificate/`](research/two_bin_certificate/): a subsequent working package of valuation/weight transfer attempts and counterexamples; distinguish proved component lemmas from unsuccessful global steps.

## Finite cases — provenance matters

| n | Status in supplied packages | Evidence |
|---|---|---|
| 6 | g(6)=8, subject to cited prior finite theorem | `finite_bounds_g6_g9`, `g7_exact` |
| 7 | g(7)=9, computer-assisted proof **claimed** in newest package | `g7_exact`; rerun `verify_all.py` |
| 8 | g(8)=11 in the later computer-assisted package, conditional on g(7)<=9, g(6)<=8, g(5)<=6; the older 11<=g(8)<=12 interval is superseded | `g8_exact`; `finite_bounds_g6_g9` |
| 9 | 12 <= g(9) <= 13; conditional upper bound, exact value not established | `g9_12_or_13`; later partial reductions in `g9_followup` |

The g(8) upper proof additionally depends on the g(7) and g(6) bounds and an external g(5) result. The g(8) verifier passed independently on 24 November 2026.

The g(7) proof explicitly relies on John Tripodo's November 2026 manuscript for `g(4)` and `g(5)`. No independent verification of that external manuscript was performed for this repository assembly.

## Core weighted approach

For `0 <= w_p <= 1`, set `X_w(t)=sum_p w_p v_p(t)` and `H_w(b)=(X_w(b)-1)_+`. For fixed `M = max(A)` the top-tail objective is

```
Q_n(M,I,w) = X_w(M) + Top_{n-1}{X_w(a) : 2 <= a < M}
             - sum_{b in I} (X_w(b)-1)_+.
```

Its uniform upper bound by `2n+o(n)` is the remaining asymptotic target under the raw-transfer framework. The archived lemmas include quotient/cofactor banks, prime valuation repairs, diffuse prime weights, smooth-source and separated-band results, and exact bookkeeping. Uniform control over growing mixed prime cores is **still missing**. Refer to the status and corrections ledger before citing any lemma.

## Latest research checkpoint (25 November)

The new capped-valuation certificate handles an explicit separated-support class with growing Hall reserve. Weighted bank overlap and local LCM loss give common-budget components. The broader conjectured mixed-weight and arbitrary-support extensions remain open; consult the [claim ledger](research/asymptotic_2026_11_25/CLAIM_LEDGER.md) before using them. No unrestricted asymptotic proof is claimed.

## Known failed shortcuts

Historical counterexamples and correction notes demonstrate that local witness inequalities cannot be summed and transported to arbitrary target intervals without controlling competing charges and positional budgets. In particular the previously proposed whole-sum transfer (8) is false: the archived `p,W,q` family has discrepancy larger than square-root scale. Counterexamples refute specific intermediate lemmas, not the original conjectures.

## Reproducibility

The complete `g(7)` package is available under:

```sh
cd research/g7_exact/erdos708_g7_proof
python3 g7_exact/verify_all.py
```

It requires Python 3, a C++17 compiler, and enabled assertions. Run the exact g(8) verification using `cd research/g8_exact && python3 verify_all.py`. Other research packages contain independent scripts and instructions inside their own READMEs. The `g(8)` verifier was independently replayed on 24 November 2026; not all older historical programs have been rerun. See `MANIFEST_SHA256.txt` for the historical payload hashes and the newer packet's provenance and replay notes for added materials. The historical archive is preserved; its inventory is not a complete manifest of later additions.

## Editorial policy

1. Always label theorem status as proved *within a specified argument*, computer-checked, conditional, empirical, counterexample, or open.
2. Never cite an older snapshot as superseding a newer correction.
3. Preserve original sources, logs, and certificates. Claims of external peer review are not made.
4. Communicate project text in English. Original archival language is preserved for provenance.

## Source links

- [Erdős Problem 708](https://www.erdosproblems.com/708)
- [Z. Wang, interval divisor covers](https://github.com/science-prince/erdos-708-interval-divisor-covers)
- [External finite-case manuscript](https://hexagonmath.org/pdf/2611.00694v1)

## Suggested repository name

`DenisUkranian/erdos-708-research`


**Public-source provenance:** Four files reproducing complete manuscripts of other authors were excluded; see [`EXCLUDED_THIRD_PARTY.md`](EXCLUDED_THIRD_PARTY.md).
