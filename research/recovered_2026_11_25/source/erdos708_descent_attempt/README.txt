ERDOS 708 -- EXECUTION OF THE COLD-QUOTIENT DESCENT ROUTE
24 November 2026

Status: the required uniform descent inequality (D) remains unproved.
Neither the general asymptotic nor exact 2n has been established here.

Main report: erdos708_descent_attempt.pdf
Editable mathematical source: erdos708_descent_attempt.tex

The report contains:
1. An actual arithmetic obstruction to source-only cold-quotient localization,
   and the exact joint target payment that excludes it from true optimality.
2. An actual hot-root union whose interval-transfer discrepancy exceeds every
   fixed multiple of sqrt(M).
3. A nonarithmetic, uniquely globally optimized model defeating localization
   from row balances, full tails and orthant domination alone.
4. The additional phase-averaging inequality and its actual direction.

These are obstructions to intermediate proof steps. None refutes the genuine
arithmetic inequality (D). They are not new factorization classes presented as
a solution, and no values of g(n) were computed.

Exact checks, using only Python's standard library:
    python3 variation/check_abstract_globality.py
    python3 hyperbola/check_hot_union.py

The first verifier consumes the accompanying rational certificates and does
not invoke an optimizer. The 204 certificates cover all graphical degree
sequences relevant to the six-coordinate example. The second verifies an
exact CRT-average existence certificate for a real shifted interval.

Detailed working proofs are in the variation/, hyperbola/ and obstruction/
directories.
