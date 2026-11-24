ERDOS 708: GENERAL TWO-BIN CERTIFICATE
24 November 2026 -- revised after the user's counterexample and renewed attempt

STATUS
This bundle does NOT prove g(n) <= (2+o(1))n or g(n) <= 2n.
It contains a proved general source/target certificate and a correction:
the user supplied a valid counterexample to the unrestricted full-prefix
active-part transfer. Its deficit is Theta(M^(10/17)), so even an
O(sqrt(M)) error does not repair that assertion. All prime powers and
arbitrary weights in [0,1] remain allowed in the proved pointwise lemma.

START HERE
final_push/erdos708_common_factor_descent.pdf -- latest proved descent and gap.
final_push/erdos708_common_factor_descent.tex -- editable source.
new_attempt/erdos708_asymptotic_retry.pdf -- preceding continuation and exact gaps.
new_attempt/erdos708_asymptotic_retry.tex -- editable source for the continuation.
erdos708_two_bin_certificate.pdf -- revised report with the counterexample.
erdos708_two_bin_certificate.tex -- editable LaTeX source.

LATEST CONTINUATION: EXACT COMMON-FACTOR DESCENT
For the complete source and target divisibility class of g, let D_g be
its source hinge minus its target hinge, t=X(g), and N=floor(M/g).
If t<1, set s=1-t, w'_p=min(w_p,s)/s, and c'=(c-t)/(1-t). Then

  D_g <= s J_(c')(w';N,J_0)

for every N-term subinterval J_0 of I/g. If t>=1, then

  D_g <= -N min(t-1,c-1) <= 0.

This is exact for every shift, all weights, and all prime powers.
At a shortest violation J_c>B, every g>1 therefore satisfies
D_g <= (1-X(g))B if X(g)<1, and D_g<=0 otherwise. Its full tail has gcd 1.
The proof does not transport original row balances to normalized prices.

These individual class comparisons still do not give a simultaneous
allocation when target classes overlap. A proved ABSTRACT incidence
model has a unique positive global optimizer, exact rows, all these
class cuts, all binary Rosser cuts, divisor-count domination, and
globally nonpositive proper cold quotients. It is NOT an integer-interval
counterexample: actual interval counts differ from floor(M/d) by at most
one, whereas its triple count discrepancy is 510. That exact numerical
restriction is still needed jointly.

The retained full-tail energy bound uses K_(c-X(d)), but its coarse
consequence remains n^2/M+O(n^3/M); it does not close M=o(n^2).
The support-stable envelope transfer was audited, not proved. Its finite
directed search is not a uniform theorem or a computation of g(n).

Latest notes and exact checker:
  final_push/arithmetic/COLD_COMMON_FACTOR_DESCENT.md
  final_push/arithmetic/FULL_TAIL_DIVISOR_ENERGY_CONSTRAINT.md
  final_push/variation/ALL_DIVISIBILITY_CUTS_GLOBAL_OBSTRUCTION.md
  final_push/variation/verify_global_cluster_obstruction.py
  final_push/envelope/STABLE_ENVELOPE_TRANSFER_AUDIT.md

Run the exact checks from the unpacked archive root:
  python3 final_push/variation/verify_global_cluster_obstruction.py
  python3 final_push/dense/check_cold_bank_overlap.py
The optional envelope probe requires NumPy and SciPy; its previously
generated data and execution log are already included.

PRECEDING CONTINUATION: WHAT IS PROVED
For K hot target positions in an M-term interval,

  #{d<=y: X(d)>1} <= 8 (Ky/M)^2       (1<=y<=M/2).

The proof uses the positive differences of selected positions in one
short block. At a genuine positive global optimum it gives O(n^2/M)
distinct hot divisors up to any fixed multiple of sqrt(M); their total
load has the same bound. Repeated source uses are NOT counted by this.

For repeated carriers h<=sqrt(M), total demand sum m_h<=n, all +1 errors
in a single second-moment bank count sum to at most n^2/M. The unresolved
main term is M^(-1) sum_(h,k) m_h m_k gcd(h,k).

At a genuine positive global optimum with c=2+delta, the weighted source
demand carried by prices in (0,1/2] is at least F-2n>delta*n. This is a
necessary condition, not an upper bound proving the asymptotic.

Every source X(a)>2+delta has a three-block factorization whose pairwise
products all have load >1+delta/2. The required common interval-capacity
estimate remains unproved. Both sparse and dense remaining gaps are
explicitly stated. A local cleanup of divisor-hotness does not preserve
source excess.

Latest proofs and independently checked abstract limitations:
  new_attempt/variation/SHORT_WINDOW_HOT_DIVISORS.md
  new_attempt/arithmetic/BINARY_CUTS_AND_JOINT_OBSTRUCTION.md
  new_attempt/arithmetic/ALL_INTEGER_THRESHOLD_CUTS_OBSTRUCTION.md
  new_attempt/triangle/THREE_BLOCK_REDUCTION_AND_ARITHMETIC_GAP.md
  new_attempt/envelope/EXACT_RESIDUAL_CAPACITY_FORMULA.md
  new_attempt/envelope/GCD_CLUSTER_LOCAL_BARRIER.md

The last note proves the exact accumulated-lcm payment identity and gives
a six-prime arithmetic counterexample to the claim that pairwise cold
gcds suffice for all simultaneous payments. It is NOT a positive global
optimum and does not disprove the general asymptotic.

The envelope checker uses numerical LP evaluation plus stated exact
rational identities. It is NOT a full exact LP proof checker. The
abstract countermodels are NOT arithmetic counterexamples. The separate
arbitrary-upset counterexample does not apply to additive thresholds.
Prior inputs used by the continuation are included under
new_attempt/prior_inputs/.

MAIN PROVED RESULT
For r_w(d)=max(0,min(min_{p|d} w_p,(X(d)-1)/Omega(d))) and
K_L(t)=sum_p v_p(t) max_{d|h(t),p|d,d^2<=Lp} r_w(d),

  (X(a)-2)_+ <= K_{h(a)}(a) <= K_a(a) <= K_M(a)  (a<=M),
  K_M(b) <= (X(b)-1)_+                          (all b).

The proof uses a two-bin packing contradiction for residual prices.
Source constant 2 is sharp even for an actual prime power.

The unrestricted aggregate transfer of K_{h(a)} from the whole prefix is
FALSE. Its former equation (8) in chat is equation (9) in the report.
The own-full-tail, reserve-corrected estimate on genuine positive global
optimizers remains UNPROVED. Do not cite numerical searches as proof.

CORRECTION MATERIAL
  counterexample/audit/USER_COUNTEREXAMPLE_AUDIT.md
  counterexample/tail/CORRECTED_DEFICIT_AND_PRUNING.md
  counterexample/check_counterexample_constants.py

The construction is the user's. The audit verifies the exact CRT mean,
all prime powers, positive background prices, and the empty source tail.
The constant checker uses rational bounds, not floating-point positivity.

EXACT CHECKS
  python3 optimality/check_hyperbolic_certificate.py
  python3 floor/check_kernel_row_obstruction.py

The first program verifies rational instances of the proved lemma and an
actual M=18 counterexample to an excessively strong ambient-prefix
transfer. The second recomputes a fully explicit arithmetic counterexample
to independent row/price-level transfer. Neither computes g(n).

PROOF NOTES
  optimality/WATERFILLING_HYPERBOLIC_CERTIFICATE.md
  sieve/POSITIVE_SURPLUS_MEAN_RESTRICTION.md
  floor/KERNEL_ARITHMETIC_TRANSFER_AUDIT.md

EXPLORATORY SEARCHES
The probe sources and PROBE_SUMMARY.md are retained for reproducibility.
Their CRT phase patterns correspond to actual integer intervals, but their
searches are heuristic/local, not exhaustive global optimality certificates.
They missed the user's tiny-positive-weight support inflation mechanism.

ADDITIONAL AUDITS
The sieve and fresh directories also contain separate failed-route audits.
Abstract profile counterexamples there are NOT integer-interval
counterexamples to Erdos 708. These appendices do not strengthen the status
of the main theorem or establish the missing arithmetic transfer.

EXISTING RAW-TO-INTEGER TRANSFER
Wang's raw-transfer.tex is linked in the report. This bundle does not
reprove rounding. Even an exact raw bound 2n would imply the requested
integer asymptotic via that theorem, not automatically exact integer 2n.

Ordinary LaTeX installations can compile the source with pdflatex.
No public repository, email, or other external communication was modified.
