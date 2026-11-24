ERDOS PROBLEM 708 — REPRODUCIBLE PARTIAL-RESULTS BUNDLE
Research note dated 23 November 2026

STATUS — READ FIRST

The unrestricted exact conjecture g(n) <= 2n and the unrestricted asymptotic
conjecture g(n) <= (2+o(1))n remain open. Neither is proved or disproved by
this bundle. The general weighted inequality H2 is also not proved here.

These are AI-assisted working proofs with independent internal audits
within the research session. They have not received external referee
approval and are not formally verified. No novelty or literature-priority
claim is made. The exact finite checks supplement the mathematical proofs;
finite searches and floating-point solver bounds do not replace them.

START HERE

  erdos708_partial_results.pdf  — consolidated, readable research note
  erdos708_partial_results.tex  — corresponding source and bibliography
  STATUS.json                  — machine-readable scope and verification status

The consolidated note controls the stated scope. Earlier working notes may
retain weaker constants, exploratory language, or results later superseded.

WHAT THE NOTE ESTABLISHES WITHIN ITS STATED HYPOTHESES

* An exact 2n cover under a finite condition on the prime support of the
  quotients a/P^+(a). A sharper source-specific floor/ceiling certificate
  uses the actual number of sources with each quotient. Both conditions
  are sufficient for EVERY shift x>=0, not just one tested interval.

* An exact 2n cover for all sufficiently large M when every source prime
  factor is at least M^alpha, for fixed alpha > 1/(2e). No explicit numerical
  threshold M_alpha is asserted. A simple separate corollary covers all
  source sets supported on k primes whose minimum is at least 3k+1.

* A uniform 2n+o_delta(n) cover when the cofactor prime support has reciprocal
  sum at most 1-delta, with fixed delta>0. Fixed small-prime anchors are
  allowed under the additional hypotheses in Section 4. This asymptotic
  deduction uses the cited long-interval theorem; neither delta nor the
  finite anchor set may silently vary in the uniform assertion.

* Ordered-support level and hinge inequalities for bounded prime-power
  profiles, with raw H2 obtained by separating tails, including the condition
  sum_{p in P}1/p + rho_y(P) <= 1, where
  rho_y(P)=sup_{T>=y}(pi_P(T)+1)/T and y=min(P). The note also proves precise
  extensions for one arbitrary extra prime and for at most two smaller
  anchor primes. Adding one prime does not permit unlimited iteration.
  Weighted-support statements and statements about the full prime support
  of the source integers are different and must not be conflated.

* For every fixed nonempty finite prime support P, with k=|P|, eventual H2
  yields the integer upper bound tau(A,I)<=2n+k-1 when M>=M0(P).
  Consequently, (2+o(1))n is an upper bound on every fixed support,
  uniformly for every shift x>=0, without any reciprocal-prime-mass
  restriction. The constants depend on P and are not uniform over
  unrestricted growing supports.

* A complete finite CRT optimization model for fixed M and fixed support.
  The unrestricted uniform defect bound identified in Section 9 remains
  unproved.

EXACT FINITE VERIFICATION

Run commands from this directory. Python 3.10 or newer is recommended.
The following command uses only the Python standard library; -S makes
verification without site packages explicit:

  python3 -S computation/exact2n_certificate.py --verify computation/exact2n_demo_results.json

It recomputes both sufficient source criteria with integer arithmetic and
fractions.Fraction. It also verifies every saved matching, distinct interval
position, repair step, and final prime valuation, without calling SciPy.
A failed sufficient criterion is explicitly NOT reported as a counterexample.

The two main demonstrations are different:

1. All 1330 products of three DISTINCT primes from 101 through 199 have
   M=7,566,179. Both finite criteria pass; the minimum integer surplus is
   158. This is a source certificate, giving a 2660-position bound for every
   shift through the proved theorem. No full interval matching was built.

2. On {11,13,17,19,23}, all 35 cubic monomials (repetitions included), the
   five squares, and the five primes give 45 distinct sources, M=12167.
   For the interval centered at their least common multiple, the saved
   witness has 45 initial matched positions and 36 repairs: an explicit
   81-position cover, within the 90-position bound. Its full valuation
   certificate and repair trace are in the JSON file.

To rebuild the illustrative matching, install NumPy and SciPy, then run:

  python3 computation/exact2n_certificate.py --demo --output exact2n_regenerated.json
  python3 -S computation/exact2n_certificate.py --verify exact2n_regenerated.json

The recorded construction used Python 3.12.14, NumPy 2.3.5, and SciPy 1.17.0.
SciPy/NumPy are needed for matching construction and optimization searches,
not for verification of the saved exact certificates. Rebuilding the PDF
requires a LaTeX installation with the packages declared in the source;
run pdflatex twice to resolve references and the table of contents.

RECOMMENDED SUPPORTING NOTES

  combinatorial/SPARSE_MATCHING_EXACT2N_AUDIT.md — Hall matching and exact covers
  analytic/SMALL_PRIME_EXCEPTIONS.md            — uniform asymptotic source class
  combinatorial/ARBITRARY_ANCHOR_MATCHING.md    — fixed small-prime source anchors
  combinatorial/ORDERED_CARRIER_H2.md          — ordered weighted carriers
  combinatorial/TWO_ANCHOR_H2.md               — two small-prime hinge anchors
  analytic/AMPLIFICATION.md                   — fixed-support uniformity
  computation/FINITE_CRT_MODEL.md             — finite phase model and search limits

SUPERSEDED INTERMEDIATE NOTES

The following are retained as a research trail, not as the final statement
of the strongest constants: analytic/SPARSE_SUPPORT_H2.md,
analytic/HALF_HARMONIC_H2.md, analytic/LEVEL_AND_ANCHORS.md, and their audits
combinatorial/SPARSE_SUPPORT_AUDIT.md, combinatorial/TRUNCATED_CARRIER_AUDIT.md,
and combinatorial/HALF_HARMONIC_AUDIT.md. Superseded does not mean disproved:
the ordered and anchor arguments strengthen their earlier sufficient conditions.
The adaptive-certificate script/JSON also tests an intermediate argument.

SEARCH LIMITS AND EXTERNAL INPUTS

The h2_* scripts and result files record exploratory finite optimization.
No H2 violation was found in the completed searches. They do not exhaust
all lengths, supports, weights, or phases. Timed-out global MILP runs are
not completed verifications, and numerical solver bounds are not formal
proof certificates. They establish no unrestricted upper bound.

The exact finite cover theorem is independent of LP solvers, the searches,
and the external raw fractional transfer. The asymptotic source-class
argument uses a cited long-interval result; the asymptotic characterization
uses the cited raw fractional transfer. Standard prime-counting and Mertens
estimates enter the rough-source exponent. Precise references and the
remaining obstruction are given in the consolidated note.
