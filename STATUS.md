# Status and limitations

**26 November 2026, exact covers and residual obstructions.** The [new density certificate and structural results](research/density_and_gluing_2026_11_26/README.md) give exact two-per-row covers for all sufficiently large instances of density at least 39.30%, a reduction of every fixed-gap counterexample to rows with arbitrarily many distinct large prime factors, and simultaneous exact covers on polynomially many selected intersections. The unrestricted coefficient two remains open.

**26 November 2026, progression selection and inverse results.** [Routes 7 and 11](research/fiber_selection_2026_11_26/README.md) give a density increment on unions of prime-pair progressions for any putative fixed-gap violation, shift-uniform covers for source sets determined by prime valuations, and a counterfamily to unrestricted full-union selection with singleton repairs.

**26 November 2026, twelve proof routes.** [New proofs and exact replays](research/twelve_routes_2026_11_26/README.md) give a shift-uniform two-budget price bound on reciprocal-sparse supports, a two-budget cover for dense subsets of unions of progressions, a necessary density increment for a counterexample, and exact centered product costs. The general coefficient two remains open.

**26 November 2026, uniform upper bound.** The [full proof](research/uniform_three_2026_11_26/README.md) gives g(n) ≤ (3+o(1))n at every source density and every interval shift. The argument assigns a cofactor to each row and controls collisions of pairs of primes using a second moment. The coefficient-two asymptotic remains open.

**26 November 2026, full-period shifts.** [Simultaneous almost-all-shifts theorem and deterministic extensions](research/unrestricted_shifts_2026_11_26/README.md). Outside a vanishing proportion of shifts, one common bound gives (2+o(1))n for every family of size much larger than M(log log M)²/log M. The centered result now allows every fixed power of log M at all densities. A proof for the worst shift and unrestricted sources is still missing.

**26 November 2026, cofactor matching.** A [written proof](research/cofactor_flow_2026_11_26/README.md) gives the sharp coefficient two at every source density for intervals with start within M(log M)^α of a multiple of lcm(A), for fixed α<13/34, and a 2n−1 bound for fixed reduced rational centers under the stated hypotheses. Arbitrary shifts remain open.

**26 November 2026 update.** [Publication audit, external results and proof target](research/audit_2026_11_26/README.md). The [density package](research/density_2026_11_26/PROOF-3960.md) gives a written eventual exact 2n bound for n/M ≥ 0.3960 with replayed arithmetic certificates. The general asymptotic remains open.

- **Uniform upper bound:** the written full-shift theorem gives g(n) ≤ (3+o(1))n.
- **General asymptotic** g(n) ≤ (2+o(1))n: **OPEN** in this research.
- **Universal exact** g(n) ≤ 2n: **OPEN** in this research.
- **Finite g(6)**: claimed exact value 8 in prior packages, with stated smaller-case dependencies.
- **Finite g(7)**: computer-assisted claim g(7)=9 with prior dependencies; no new complete replay in this update.
- **Finite g(8)**: computer-assisted upper 11 and unconditional lower 11; the upper relies on g(7)≤9, g(6)≤8, g(5)≤6. Full g(8) verifier was independently replayed on 24 November (57,487 universal certificates, 28 exact CRT residual checks).
- **Finite g(9)**: 12 ≤ g(9) ≤ 13. Lower witness unconditional; upper conditional on g(8)≤11 and its upstream dependencies. The original upper-13 verifier was independently replayed on 25 November: 658,192 demands, 89,666 maximal vectors, 5,170 residual cases, PASS. Exact value not established. The earlier 12–14 interval is superseded, not erased from the historical archive.
- **Later g(9) reductions**: recovered packages claim conditional 11-smooth closure at budget 12, at most two large primes, and a smaller high-high frontier. These are not the global exact result; the latest packages have not all been independently replayed in this update.
- **Asymptotic components**: new weighted overlap, LCM loss, profile exclusivity and separated-support capped-valuation Hall reserve. More general conversational claims remain candidates or conditional deductions; see research/asymptotic_2026_11_25/CLAIM_LEDGER.md.
- **Unresolved gate**: uniform joint valuation surplus control for growing mixed-prime support, or an alternative covering construction with total leftover repair cost o(n).

This page summarizes the included materials, not worldwide research. No peer review or formal Lean verification is asserted. Original archive records and their limitations remain preserved. See the latest directories linked in README.md.
