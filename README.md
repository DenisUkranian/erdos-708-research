# Erdős Problem 708 — Research Archive and Proof Certificates

**Status (24 November 2026): Open in general.** This repository is being populated with our recovered work on the Erdős–Surányi interval-product problem, with historical experiments, exact finite certificates, full research reports, counterexamples to intermediate claims, and reproducible scripts. An archived claim is not automatically an established theorem.

## Problem

Let `A` be a set of `n` distinct integers at least 2, and put `M = max(A)`. For any interval `I = {x+1, ..., x+M}` with integer `x >= 0`, let `tau(A,I)` be the minimum cardinality of `B subset I` such that `prod(A)` divides `prod(B)`. Define `g(n) = sup tau(A,I)` over these choices. The product uses each chosen interval position at most once.

Central goals include the asymptotic estimate `g(n) <= (2+o(1))n` and the stronger exact upper bound `g(n) <= 2n`. **Neither is proved by this repository.**

## What is included

- [`research/archive_2026_11_24/`](research/archive_2026_11_24/): preserved 292-file consolidation of reports, historical work, corrected arguments, scripts, and provenance. Start with `ERDOS708_ALL_2026-11-24/CURRENT_STATUS.txt` and `CORRECTIONS_LEDGER.csv`. This was collected before the later finite-case update.
- [`research/finite_bounds_g6_g9/`](research/finite_bounds_g6_g9/): a 24 November finite-case package, recording `g(6)=8`, `9 <= g(7) <= 10`, `11 <= g(8) <= 12`, and `12 <= g(9) <= 14`. **Its g(7) interval is superseded by the later g(7) proof package.**
- [`research/g7_exact/`](research/g7_exact/): later 24 November *computer-assisted claim* `g(7)=9` with exact integer certificates, C++/Python verifiers, and replay logs; external dependency on the stated `g(5)<=6` result. This compilation has not independently rerun the entire verifier and does not imply peer review or Lean formalization.
- [`research/two_bin_certificate/`](research/two_bin_certificate/): a subsequent working package of valuation/weight transfer attempts and counterexamples; distinguish proved component lemmas from unsuccessful global steps.

## Finite cases — provenance matters

| n | Status in supplied packages | Evidence |
|---|---|---|
| 6 | g(6)=8, subject to cited prior finite theorem | `finite_bounds_g6_g9`, `g7_exact` |
| 7 | g(7)=9, computer-assisted proof **claimed** in newest package | `g7_exact`; rerun `verify_all.py` |
| 8 | 11 <= g(8) <= 12; exact value not established here | `finite_bounds_g6_g9` |
| 9 | 12 <= g(9) <= 14; exact value not established here | `finite_bounds_g6_g9` |

The g(7) proof explicitly relies on John Tripodo's November 2026 manuscript for `g(4)` and `g(5)`. No independent verification of that external manuscript was performed for this repository assembly.

## Core weighted approach

For `0 <= w_p <= 1`, set `X_w(t)=sum_p w_p v_p(t)` and `H_w(b)=(X_w(b)-1)_+`. For fixed `M = max(A)` the top-tail objective is

```
Q_n(M,I,w) = X_w(M) + Top_{n-1}{X_w(a) : 2 <= a < M}
             - sum_{b in I} (X_w(b)-1)_+.
```

Its uniform upper bound by `2n+o(n)` is the remaining asymptotic target under the raw-transfer framework. The archived lemmas include quotient/cofactor banks, prime valuation repairs, diffuse prime weights, smooth-source and separated-band results, and exact bookkeeping. Uniform control over growing mixed prime cores is **still missing**. Refer to the status and corrections ledger before citing any lemma.

## Known failed shortcuts

Historical counterexamples and correction notes demonstrate that local witness inequalities cannot be summed and transported to arbitrary target intervals without controlling competing charges and positional budgets. In particular the previously proposed whole-sum transfer (8) is false: the archived `p,W,q` family has discrepancy larger than square-root scale. Counterexamples refute specific intermediate lemmas, not the original conjectures.

## Reproducibility

The complete `g(7)` package is nested under:

```sh
cd research/g7_exact/erdos708_g7_proof
python3 g7_exact/verify_all.py
```

It requires Python 3, a C++17 compiler, and enabled assertions. Other research packages contain independent scripts and instructions inside their own READMEs. Tests are *not* assumed to have been rerun in this assembly. See `MANIFEST_SHA256.txt` for payload hashes.

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