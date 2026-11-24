# Erdős 708: joint-estimate research addendum

Date: 23 November 2026.

**Status: J_weak remains unproved. Neither the general asymptotic
g(n) <= (2+o(1))n nor the exact 2n bound is established by this work.**

Start with erdos708_joint_estimate_addendum.pdf (six pages). Its source is
erdos708_joint_estimate_addendum.tex. It contains complete proofs of the
global optimal-coverage identity, the exact prime-conserving flow theorem,
the canonical signed root certificate, and the finite empirical-state
comparison. It states the remaining sufficient logarithmic-cap estimate
explicitly as **unproved**, and derives the desired contradiction only
conditionally on that estimate.

## Proved results and their scope

- analytic/OPTIMAL_COVERAGE_AND_LOG_CAP.md: exact identities for every
  coordinatewise reduction of a paired optimal raw dual; logarithmic row
  conservation; finite bounds for all coordinates cut by a logarithmic cap.
  The small total cap-loss estimate is not proved.
- audit/PRIME_CONSERVING_EXCESS_FLOW.md: an exact maximum-flow formula,
  including its source-quota disintegration. Its global deficiency is exactly
  the unresolved LP excess; it does not supply an additional covering gain.
- analytic/WEIGHTED_ROOTED_STAR_CERTIFICATE.md: a global signed target
  certificate with at most one positive root per target; exact source fibres,
  repeated prime occurrences, and a counterexample to separate-root exact
  sieve comparison. This certificate is not proved sufficient on the full
  minimal-obstruction class.
- audit/LOW_HEAVY_STATE_MATCHING.md: a finite bound for the total variation
  of **all** truncated-prime state bins simultaneously, its actual injective
  matching consequence, weighted exceptional-source control in the sparse
  application, and a position-count estimate for filtered cofactor banks.
  No second simultaneous cover is supplied.
- audit/LOW_HEAVY_HINGE_COMPARISON.md: the low-prime hinge comparison and
  its aggregate one-coordinate cap. It does not transfer raw dual
  minimality to a nonlinear capped coordinate.
- audit/BONFERRONI_ABSORPTION_AUDIT.md: error absorption and a shell
  bootstrap at the improved substantial-prime cutoff.
- combinatorial/HOT_DIVISOR_FLOW_CUTS.md: exact cut spill identity,
  restrictions on inclusion-minimal deficient cuts, and their limits.
- combinatorial/GLOBAL_MINIMAL_COMPRESSION.md: global minimum-cardinality
  source normalization, upper-set structure, and merge rules that retain
  the essential lcm-collision condition.

## Explicitly unresolved or rejected steps

1. The uniform logarithmic-cap loss bound (U) in the PDF is unproved.
   It is sufficient on the actual integer-minimal class, but false without
   minimality even for a genuinely paired optimum.
2. Independent exact-sieve comparison for each canonical root is false.
   verify_root_counterexample.py and root_counterexample_verified.json
   record the exact rational example. It is **not** a counterexample
   to J_weak.
3. The Boolean two-factor counting statement, if present in
   combinatorial/BOOLEAN_TWO_FACTOR_REDUCTION.md, is a conjectural
   sufficient sparse reduction, not a completed theorem.
4. A proof for a single substantial-weight level is not the requested
   arbitrary-weight result. Any ancillary note about that calculation
   retains this distinction and the mixed-weight obstruction.
5. Position counts in a cofactor bank are not automatically retained
   weighted hinge capacity. Separately chosen covers cannot be added while
   reusing the same target budget.

## Verification

The counterexample is checked with exact Python rational arithmetic:

    python3 verify_root_counterexample.py

The PDF was compiled and visually inspected. Several proofs received
independent internal mathematical checks. These are not external referee
reports or formal proof-assistant verification. Finite exploratory flow
probes, if included, establish only their individual computed cases and
are not computations of new values of g(n).

The earlier minimal-obstruction normalization and its integer-rounding
preliminaries are explicitly identified as prior inputs in the addendum.
No new uniform bound is inferred merely from those inputs.
