# Partial g(9) research checkpoint — Erdős Problem 708

This package **does not close** `g(9)`.

* `STRUCTURAL_REDUCTIONS.md`: six unconditional-on-M structural reductions, conditional on previously obtained `g(6)≤8,g(7)≤9,g(8)≤11`, and correct five-prime multigraph classification.
* `verify_lower_examples.py`: independently check the exact explicit lower construction for `n=7,8,9`, including an attaining 12-position cover for nine inputs.

Run `python3 verify_lower_examples.py` with Python 3 (no third-party dependencies). The reported `g(9)≥12` is verified. The missing task is the universal `g(9)≤12` for mixed sources in the finite intermediate range. Do not describe this as a completed proof.
