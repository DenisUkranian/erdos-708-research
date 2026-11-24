Erdos 708 — global asymptotic attempt, 23 November 2026
====================================================

STATUS: THE UNRESTRICTED ASYMPTOTIC BOUND IS NOT PROVED.

This package addresses g(n) <= (2+o(1)) n on the full minimal-obstruction
class. It does not calculate another g(n), present a new restricted source
class, or claim an unrestricted exact 2n result.

Start with erdos708_global_gap.pdf (10 pages). Its LaTeX source is included.

Proved general reductions
------------------------
For a fixed-ambient least-cardinality integer failure with budget
c m = (2+3 delta)m and an optimal clipped raw dual:

1. The sum of all source load shortfalls below c is less than the SINGLE
   rounding loss r=|P|=O_delta(m/log m).
2. Discarding sources of load at most 2+2 delta removes o(m) sources and
   o(m) weighted demand.
3. The union of the retained sources' prime-deletion banks is saturated
   in one full primal optimum.
4. Its positive weighted row excess over retained demands is o(m).
5. Every active bank has the factorial valuation lower bound.
6. The number of actual input core prime-power levels J_E satisfies
   J_E^2+|R|=O_delta(m/log m).

The all-weight estimate (91) is neither proved nor refuted. Equation (23)
of the PDF is the remaining balanced-optimal joint estimate. Even its
weaker version with an added delta*|G| would close the general asymptotic
target; neither version has been proved.

Exact negative result
---------------------
The product of all sources need not divide the product over the union
of their prime-deletion banks. A fully specified CRT example has
10353 source p-units and 10352 bank-union p-units.

This counterexample is OUTSIDE the required minimal class. It does not
refute (91), the joint weighted estimate, or Erdos 708. Its other active
prime rows have substantial oversupply; at high source loads its joint
weighted bank surplus is strictly positive.

Run the independent exact verifier from any directory:

python3 combinatorial/verify_bank_product_counterexample.py

The script locates its adjacent certificate itself and uses only the
Python standard library. The exact certificate, residue table, center,
period, saved verification output, and explanatory proof are included.
No full enumeration of the lifted interval is required.

Contents
--------
erdos708_global_gap.pdf / .tex
    The main report: proofs, precise gap, weaker sufficient target,
    conditional contradiction, exact counterexample, raw-minimal appendix.

analytic/GLOBAL_DUAL_NORMALIZATION.md
    Detailed original proof note with actual-level and boundary warnings.

audit/RAW_MINIMALITY_AND_DELETION_IDENTITIES.md
    Independently checked fractional-minimality and deletion identities.

audit/AUDIT_REPORT.md
    Scope of the independent mathematical and exact arithmetic audits.

combinatorial/BANK_PRODUCT_COUNTEREXAMPLE.md
combinatorial/bank_product_certificate.json
combinatorial/verify_bank_product_counterexample.py
combinatorial/bank_product_verification.json
    The autonomous counterexample package.

Other analytic/audit scripts and probe JSON files
    Exploratory directed tests of intermediate global-bank statements.
    Negative finite searches are not used as evidence of a universal
    theorem and are not computations of a new value of g(n).

STATUS.json / MANIFEST.json
    Machine-readable scope and integrity records.

Uniformity and scope
--------------------
M and I stay fixed under every deletion. All target prime powers are
retained, with no upper bound on the interval shift. Core cardinality,
substantial weight count, and prime gaps are not restricted.

The inherited exact quadratic gate M>=16m^2 is cited in the report.
The preceding report is erdos708_continuation.pdf, Section 8, equation
(91). No claim of priority or externally accepted solution is made.
