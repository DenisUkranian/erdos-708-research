# Erdős 708: global surplus and the complete additive tail

Research checkpoint, 23 November 2026.

## Status

**The requested uniform bound `J_(2+delta) <= C_delta` is not proved.**
No proof of the unrestricted asymptotic `g(n) <= (2+o(1))n`, no exact
`2n` result, and no arithmetic counterexample to the requested surplus
bound is claimed. No new values of `g(n)` were computed.

The user's global surplus maximization is valid: the maximizing weight
vector is genuinely raw-dual optimal for its own full strict upper tail.
The present checkpoint uses that exact normalization.

## Main deliverable

`erdos708_surplus_tail.pdf` and its LaTeX source contain the consolidated
six-page argument. The main new unrestricted arithmetic result is

    sum_{a<=M, X(a)>t} X(a)
       <= [t+1+K(1+mu)] # {a<=M : X(a)>t},
    mu = sum_p w_p/(p-1),  0<=w_p<=1,

with an absolute constant K and every threshold t>=0. It uses exact
disjoint first-crossing cells, retains inactive factors and repeated
prime factors, and has no support-size or density restriction.

Positive surplus forces mu=O_c(1). Applying the tail theorem at every
threshold yields exponential integrability relative to the tail's own
size, hence a bounded-source-load and price-band normalization with
weighted error epsilon*n. Original paired rows are tracked explicitly;
they are not transferred to a different optimum without justification.

A separate genuine CRT modification of the shift, followed by
reoptimization, controls the raw linear prefix/interval discrepancy by
O(n/log n) at a normalized positive global extremum. It does not
compare the nonlinear hinges.

## Detailed notes

- `audit/FULL_TAIL_CONDITIONAL_FIRST_MOMENT.md`: full proof of the
  conditional first-moment theorem and its tail consequences.
- `variations/SOURCE_TAIL_AND_DEMAND_BAND_CLEANUP.md`: elementary mean
  bound, factorial moments, exponential integrability, and paired
  demand-band cleanup with the correct order of parameter choices.
- `audit/GLOBAL_MAXIMIZER_AND_SHIFT_REDUCTION.md`: exact global
  optimization, zero-demand-price normalization, rational optimum,
  genuine CRT shift reduction, and linear discrepancy estimate.
- `variations/GLOBAL_SURPLUS_VARIATIONS.md`: deletion stability,
  fractional cofactor-bank saturation, and integrated weight variations.
- `audit/ALL_COFACTOR_HALL_DEFICIENCY.md`: the exact weighted consequence
  of a hypothetical cofactor matching; its required matching bound is
  explicitly unproved.
- `analytic/POSITIVE_KERNEL_THRESHOLD_AND_LOG_CAP.md`: the sharp 13/6
  finite obstruction for nonnegative pointwise kernels, a log-cap
  restriction, and an abstract incidence countermodel. The countermodel
  is **not an actual prefix/interval counterexample**.
- `analytic/ROOTWISE_SIEVE_OBSTRUCTION.md`: an actual arithmetic
  obstruction to comparing each canonical root separately. It does not
  satisfy the paired-optimal hypotheses and does not refute the target.
- `audit/WEIGHT_ADAPTED_CUTOFF_TEST.md`: the precise unresolved step in
  a joint cutoff attempt; no sparse-branch closure is claimed.
- `analytic/GEOMETRIC_GRID_AND_FEW_COFACTORS.md`: finite geometric price
  grids with approximate raw optimality for their own new full tails,
  exact same-price replacement closure, and the resulting bound on
  distinct regular deletion cofactors. The missing Hall or common
  capacity estimate is explicitly not asserted.

Any additional note included in this archive states its own exact scope
and status. Method obstructions are distinguished from counterexamples
to the original arithmetic statement.

## Remaining mathematical gap

The source-demand and normalization bounds do not allocate the single
target hinge capacity among the different prime configurations. A bound
on occurrences in each source is not a bound on all configurations or
on their overlap at one target. Exact whole-row balances provide first
weighted moments, not the missing joint nonlinear estimate.

Without that estimate the proved tail bound leaves an error of order
n, rather than O_delta(1) or a coefficient-two asymptotic. The report
does not treat that error, or a restatement of the missing inequality,
as a solution.

## Verification and inputs

The main first-crossing and cleanup arguments received independent
internal mathematical checks. The consolidated PDF was checked for
mathematical scope and rendered page by page. These checks are not an
external referee report or a formal proof-assistant verification.

The rough-number input is from Kai Fan, Journal of Number Theory 260
(2024), 120–150, DOI 10.1016/j.jnt.2024.01.008: the uniform upper bound
in the introduction and the lower bound in Theorem 2.3. The published
primary source was inspected.

The absolute linear covering bound, ambient quadratic gate, and raw
fractional-to-integer transfer are retained as established inputs from
the Wang manuscript supplied by the user. The transfer is not reproved.
Links appear in the report. No external manuscript is copied into this
archive, and no changes have been published or sent to other people.
