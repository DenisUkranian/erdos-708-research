# Audit of the proposed stable-envelope interval transfer

24 November 2026. **Status: the proposed interval transfer remains unproved. No arithmetic counterexample was found in the finite directed search below. This is not a proof of Erdős 708 or its asymptotic form.**

## 1. The assertion actually examined

For prices `0 <= w_p <= 1`, write

\[
X_w(t)=\sum_p w_p v_p(t),\qquad
h_w(t)=\prod_{w_p>0}p^{v_p(t)}.
\]

For a nonunit divisor supported on the active primes put

\[
r_w(d)=\max\left(0,\min\left\{
\min_{p\mid d}w_p,\frac{X_w(d)-1}{\Omega(d)}\right\}\right),
\]

\[
K_L^w(t)=\sum_p v_p(t)
 \max_{\substack{d\mid h_w(t),\ p\mid d\\d^2\le Lp}}r_w(d).
\]

The source envelope under examination is

\[
C_w(a)=\inf_{0\le v\le w}
\{K^v_{h_v(a)}(a)+X_w(a)-X_v(a)\}.
\]

The previous exact finite LP formula for this envelope is in
`ep708_new_attempt_20261124/envelope/EXACT_RESIDUAL_CAPACITY_FORMULA.md`.
The proposed new assertion is

\[
\boxed{\sum_{a\le M}C_w(a)
 \ \le\ \sum_{b\in I}K_M^w(b)}.\tag{E}
\]

Together with the proved pointwise inequalities

\[
(X_w(a)-2)_+\le C_w(a),\qquad
K_M^w(b)\le(X_w(b)-1)_+,
\]

(E) would imply the desired raw inequality with exact constant two. Neither pointwise inequality supplies (E).

## 2. Exact scope of the directed finite search

The reproducible script is `probe_stable_envelope_transfer.py`; its output is
`probe_stable_envelope_results.json`, with an execution log in `probe_console.txt`.

Run from the shared workspace root:

```bash
python3 ep708_finalpush_20261124/envelope/probe_stable_envelope_transfer.py
```

It imports the already checked support-enumerating LP implementation from
`ep708_new_attempt_20261124/envelope/check_residual_capacity.py`.

The catalogue contains 90 profiles: lengths `30, 60, 100, 200, 400`; the six supports
`{2,3}`, `{2,5}`, `{2,3,5}`, `{2,3,5,7}`, `{3,5,7}`, `{5,7,11}`; and, for each
length/support combination, unit prices plus two reproducible random price vectors
from `{.1,.2,.3,.4,.5,.6,.8,1}`. The fixed random seed is `7082411`.

For each source integer the computation retains all valuations, enumerates all
subsupports, and solves the exact-form envelope LP numerically using HiGHS.
The 22 profiles whose total source envelope is numerically zero are skipped.
The remaining 68 profiles have counts by length `12, 12, 12, 16, 16`.

For each nonzero profile the target search considers the prefix phase, 50 random
CRT phases, and 200 random one-coordinate improvements. It is **not** an exhaustive
phase minimization or a verified global optimization over weights. There is no
calculation of `g(n)` here.

Every retained numerical target sum exceeds the computed source-envelope sum.
The smallest observed margin is approximately `0.05`, in the profile
`M=30, w_2=.3, w_3=.5, w_5=.8`; this is only a report of the search, not an exact
certificate or evidence for arbitrary lengths. The search supplies no uniform
estimate and cannot distinguish (E) from a statement whose first failure occurs
at larger or more structured supports.

## 3. Why the searched target patterns are actual interval patterns

For each active prime `p`, let `P_p` be the smallest power of `p` greater than `M`.
The script chooses an independent residue `x_p mod P_p` for the interval start.
The valuation array records divisibility by all powers of `p` up through `P_p`.

There is at most one position in the length-`M` interval divisible by `P_p`.
If such a position exists, at most one lift of `x_p` modulo `p P_p` would give it
an additional factor `p`; choose any other lift. If no such position exists,
any lift works. Thus all recorded valuations are exact, including the top
valuation, after suitable independent lifts.

Chinese remaindering the lifts modulo the pairwise coprime numbers `p P_p`
produces a genuine common integer interval start. A further common-period shift
makes the interval positive if necessary. Therefore the search is over a subset
of realizable arithmetic intervals, not arbitrary incidence matrices or
independent unconstrained prime rows. It may miss good phases, but it does not
create spurious phases.

## 4. Two exact structural checks

### The envelope is still stronger than the raw source hinge

For `a=30=2*3*5` with all three prices `3/5`,

\[
X_w(30)=9/5<2,\qquad C_w(30)=1/5>0.\tag{1}
\]

Here is an exact calculation, independent of numerical optimization. Write the
reduced positive prices at `2,3,5` as `u,v,z`, respectively. The only pair roots
are `6` in the rows `2,3`, and `10` in the row `5`. There are no eligible triples.
The minimum-price cap in each pair is inactive because all prices are at most
one. Consequently

\[
F(u,v,z)=(u+v-1)_++\tfrac12(u+z-1)_+.
\]

For the full support the residual capacity
`u+v+z-F(u,v,z)` is nondecreasing in `v,z`, so it is maximized with
`v=z=3/5`. It then becomes

\[
u+6/5-\tfrac32(u-2/5)_+,
\]

whose maximum is `8/5`, attained at `u=2/5`. Any proper support has residual
capacity at most its retained load, which is at most `6/5`. Therefore the
envelope is `9/5-8/5=1/5`.

Thus (E), if valid, is a stronger sufficient statement. Its truth is not a
formal consequence of replacing the source hinge with an equivalent function.

### The envelope does not make all divisor coefficients nonnegative

At unit prices and a squarefree active integer `a`, retaining any two active
primes gives

\[
C_w(a)=(\Omega(a)-2)_+.
\]

Hence on the divisors of `210=2*3*5*7`, the coefficient of the divisor `210`
in the unique divisor expansion of `C_w` is

\[
\sum_{d\mid210}\mu(210/d)C_w(d)=2-4=-2.\tag{2}
\]

It is therefore invalid to infer interval transfer merely by claiming that
support stabilization has turned the source envelope into a nonnegative
linear combination of divisibility indicators. Equation (2) is a local
obstruction to that proof shortcut; it is not a counterexample to (E).

## 5. Correction to the one-prime observation

When only one prime `p` is active at price `w`, the target kernel is generally
**not** a fixed constant times `v_p(t)` at all valuations.
Let

\[
q_M=\max\{j\ge1:p^{2j-1}\le M\},\qquad
f_M(e)=e\left(w-\frac1{\min(e,q_M)}\right)_+
\]

for `e>=1`, with `f_M(0)=0`. Then the correct formula is
`K_M^w(t)=f_M(v_p(t))`. The coefficient is constant only after `e>=q_M`.

The function `f_M` is nondecreasing in `e`, and so has nonnegative successive
increments. Counting each prime-power divisibility indicator in any interval
of length `M` gives at least `floor(M/p^j)` occurrences. This proves

\[
\sum_{a\le M} f_M(v_p(a))\le\sum_{b\in I}f_M(v_p(b)).
\]

At a source valuation `e`, the source envelope is

\[
C_w(p^e)=e\left(w-\frac1{\lceil e/2\rceil}\right)_+
\le f_M(e),\qquad p^e\le M.
\]

This verifies the one-prime sanity check with all powers. It is not a substitute
for the arbitrary-support estimate required by the task.

## 6. The exact remaining gap

The per-source LP formula chooses different reduced price vectors and different
active supports for different integers `a`. Its feasibility gives only a
pointwise residual capacity. No common arithmetic certificate has been
constructed that places all the resulting source charges into the target row
maxima without reusing their capacities.

The failed original full-kernel transfer cannot be restored by silently taking
these minima after summation: the minima are source-specific, while each target
row pays only its largest eligible root price. The original empty-tail
support-inflation counterexample is removed by the envelope, but that removal
does not prove the joint transfer.

The new directed search neither disproves nor establishes (E). There is no new
uniform bound on `J_{2+delta}`, and no contradiction with positive global
optimality has been obtained in this branch.
