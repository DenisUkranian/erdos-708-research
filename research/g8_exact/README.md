# Erdős Problem 708 — Exact eight-source case

**Claim:** g(8) = 11, a reproducible computer-assisted result, 24 November 2026.

**Dependency:** the universal upper bound g(8) <= 11 assumes g(7) <= 9, g(6) <= 8, and an external theorem g(5) <= 6. The lower-bound witness is unconditional. This package is **not independently peer reviewed** and is not a formal Lean proof.

## Proof assets

- `g8_exact_proof.pdf` / `g8_exact_proof.tex`: complete English proof.
- `REPRODUCIBILITY.md`: independent verification architecture.
- `src/`: four C++17 proof components, including CRT multicover and exact lower-bound dynamic programming.
- `certificates/`: 57,515 demands, 57,487 universal slot witnesses, 28 CRT exceptional demands.
- `logs/`: original replay output.
- `verify_all.py`: deterministic regeneration and cross-check.
- `README_RU.md`: original accompanying Russian-language note (retained for provenance).

The preceding g(7) proof is already in `../g7_exact/`. A redundant nested ZIP copy that appeared in the stand-alone g(8) package has been omitted from this repository import.

## Reproduce

From this directory:

```sh
python3 verify_all.py
```

Requires Python 3.9+ and g++ with C++17 support. The archive was independently replayed during this repository import and concluded:

```
ALL CHECKS PASS: upper g(8)<=11 conditional on g(7)<=9,g(6)<=8,g(5)<=6; lower g(8)>=11 unconditional
```

Read the mathematical paper, especially the analytic gate, sound finite-source reductions, cumulative-GCD lemma and exhaustive CRT stage. A successful replay is not the same as external verification of every underlying theoretical dependency.
