ERDOS 708: PROOF LADDERS FOR THE UNRESTRICTED ASYMPTOTIC
Research checkpoint, 23 November 2026

STATUS
The general asymptotic g(n) <= (2+o(1))n has NOT been proved.
The exact 2n conjecture has NOT been proved.
No new values of g(n) are computed. Scripts test intermediate structural claims.

START HERE
1. erdos708_proof_ladders.pdf: integrated report, detailed proof ladders, executed lemmas, counterexamples, and exact missing endpoint.
2. COMMON_COMPLETION_CRITERION.md: fixed-error contradiction and the relaxed complement threshold.

ROUTE A: ADAPTIVE TRANSPORT
route_adaptive/ADAPTIVE_HALL_LADDER.md
route_adaptive/TWO_CARRIER_REDUCTION.md
route_adaptive/SMALL_ROOT_UNION_COUNTEREXAMPLE.md
route_adaptive/test_adaptive_hall.py

ROUTE B: JOINT DIFFUSE TRANSFER
route_core/DIFFUSE_BANK_TRANSFER.md
route_core/CONDITIONAL_DIFFUSE_CELLS.md
route_core/JOINT_CLIPPED_DIFFUSE_TRANSFER.md
route_core/SMALL_ROOT_DIFFUSE_CORE_DICHOTOMY.md

ROUTE C: NORMALIZED AND CLUSTER CERTIFICATES
route_certificate/NORMALIZED_COFACTOR_CERTIFICATE.md
route_certificate/CLUSTER_NORMALIZED_CERTIFICATE.md
route_certificate/verify_counterexamples.py

INHERITED INPUTS
inherited/ contains the previously established global optimizer, complete-tail moment, near-quadratic exclusion, and diffuse-weight inputs. These are carried forward, not claimed as newly proved in this session. Some working-note references preserve the original workspace paths; copies of the essential inputs are included here under inherited/.

NEW PROVED CONTENT
- Uniform one-sided diffuse concentration at every arithmetic-bank length.
- Positive-density diffuse-demand bound for all genuine global optimizers.
- Relative concentration in arbitrary conditioned heavy-prime cells under an explicit power gap.
- Joint clipped capacity transfer with O_delta(psi(eta) n) error, including sparse tails and all inactive source cofactors.
- Relaxed-complement carrier dichotomy, decreasing-order residual light-prime cutoff, small-core weighted mean and labelled high-light fibre dilution.
- Adaptive Hall upset cuts and the common-hot-root cluster credit.
- Cluster-normalized bank norm, short-bank deletion, and exact scale-row identity (with the explicit deletion caveat).

UNPROVED TERMINAL STEPS
The relaxed adaptive Hall/capacity cut and the single amplified model-capture inequality remain open. The model is not declared additive or optimal. Exact original row balances are not transferred to replacement source sets or auxiliary loads. Distinct-root estimates are not promoted to multiplicity-weighted estimates.

COUNTEREXAMPLE SCOPE
The fixed-union and uniform-routing examples refute stronger intermediate shortcuts. They are NOT counterexamples to the actual positive-optimizer class or to Erdos 708. The small-root union example has an explicit active-row imbalance excluding it from that class.

VERIFICATION
Independent internal derivations checked arithmetic counts, raw prime powers, real quotient intervals, shared budgets, and parameter order. Exact rational examples are reproducible with the included script. No external mathematical validation or priority claim is made.

EXTERNAL INPUTS
Wang raw-transfer and main manuscripts, and Granville--Soundararajan's fundamental sieve lemma, are linked in the PDF and PROVENANCE.json. Third-party manuscript source files are not bundled.
