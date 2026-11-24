# Erdős 708: exact top tails and verified intermediate gaps

Research checkpoint, 23 November 2026.

## Status

The requested unrestricted bound g(n) <= (2+o(1))n, and the corresponding uniform raw top-tail inequality, have **not been proved** in this checkpoint. No counterexample to either the asymptotic bound or the exact 2n bound was found. The exact identities recorded here are not claimed as a solution.

The new proved results are a linear counterexample to a same-threshold prefix/interval comparison, and a full-top-tail refinement of a prime-deletion-bank counterexample. The latter is explicitly proved not to satisfy optimal active-row balance. Two other attempted intermediate arguments are audited in the supplementary notes.

## Main report

- erdos708_top_tail_gap.pdf — self-contained five-page report, including the exact residual and both counterexamples.
- erdos708_top_tail_gap.tex — report source.

The exact target remains

    X_w(M) + Top_{n-1}{X_w(a):2<=a<M}
      - sum_{b in I}(X_w(b)-1)_+ <= 2n+o(n),

uniformly over M, the positive M-term interval I, and 0<=w_p<=1. Wang's raw transfer suffices once this bound is proved. No new rounding argument is needed.

## Proof and audit notes

- combinatorial/DENSE_H1_LINEAR_DISCREPANCY.md: a finite CRT averaging construction with discrepancy kappa*M+o(M), kappa>0; the forced-maximum top set is retained.
- analytic/TOP_TAIL_BANK_COUNTERLEMMA.md: a complete strict top superlevel with a one-unit prime-row deficit in its bank union, plus the exact row oversupply that excludes optimality.
- audit/STRICT_LEVEL_ROWS_AND_BANK_RESIDUAL.md: strict-source normalization, all-power row formulas, and the nonnegative residual identity. These are identities, not the missing bound.
- combinatorial/EXACT_TOP_TAIL_AND_JOINT_RESIDUAL.md and combinatorial/MAX_RATIO_THRESHOLD_VARIATIONS.md: precise joint-accounting and variation audits; neither closes the estimate.
- analytic/WANG_PRIMARY_AND_EXACT_TOP_TAIL.md: primary-source verification of raw transfer, the quadratic gate, and the forced-maximum dual objective.
- analytic/REJECTED_SELBERG_BRIDGE.md: a linear counterexample to one proposed sufficient Selberg-denominator comparison. It does not refute the underlying two-level interval inequality.
- audit/OFFSET_TRANSPORT_AUDIT.md: a valid local injection and a small counterexample to a half-radius truncation. Full interval transport and the fractional route remain undecided.

## Exact numerical certificate and reproduction

The inherited exact CRT certificate is in certificate/bank_product_certificate.json. It specifies every congruence, the full center in hexadecimal, and all 1,411 rough offsets. These are our earlier working certificate and verifier, included so the present refinement is independently reproducible. The original source count in that certificate is 10,353; the new full top set has 56,063,090 members, as explained in the report.

Run the standard-library-only certificate verification:

    python3 certificate/verify_bank_product_counterexample.py

It checks all CRT congruences, all rough offsets, every relevant quotient, the lifted interval, and the exact bank p-valuation. The checked output is certificate/bank_product_verification.json.

To reproduce only the cardinality and row-demand parameters of the new top set:

    python3 audit/count_top_counterexample.py

This uses NumPy and approximately 0.4 GiB of memory. It is a deterministic prime-power sieve for a specified set; it does not optimize a cover or compute any g(n). Its checked output is audit/count_top_counterexample.json.

## Primary materials

Wang's source files were retrieved and inspected through the GitHub connector on 23 November 2026:

- [raw-transfer.tex](https://github.com/science-prince/erdos-708-interval-divisor-covers/blob/main/papers/main-paper/raw-transfer.tex), blob 652a6c28dc52abd22116084746aff569021207a7;
- [main.tex](https://github.com/science-prince/erdos-708-interval-divisor-covers/blob/main/papers/main-paper/main.tex), blob 17f471ea0073e00e8b0245505a62529c643cbf60.

This archive includes links and source identifiers, but does not redistribute those external files. Additional primary references are given in the corresponding mathematical notes.

## Scope of the conclusion

Both the sparse regime n/M -> 0 and the nontrivial positive-density regime remain unresolved for the full balanced optimum. Exact 2n remains separate. The false shortcuts and the exact remaining quantity are identified; the quantitative estimate sufficient for the desired contradiction is still missing.
