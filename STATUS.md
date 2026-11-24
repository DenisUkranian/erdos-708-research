# Status and limitations — 2026-11-24

- **General asymptotic** `g(n) <= (2+o(1))n`: **OPEN** in this research.
- **Universal exact** `g(n) <= 2n`: **OPEN** in this research.
- **Finite g(7)**: newest separate archive reports a computer-assisted proof of `g(7)=9` with replay logs. External `g(5)<=6` theorem is a dependency. Independently rerun before publication as an externally confirmed fact.
- **Finite g(8), g(9)**: provided certified bounds only; not exact.
- **Weighted two-sided K construction**: pointwise source and target inequalities have proofs in the research record; an attempted summed transfer has a counterexample and is not a theorem.
- **Unresolved research gate**: uniform joint fractional valuation surplus control in the growing mixed-prime-core regime, or a new covering method.

This page summarizes *the included materials*, not the state of all worldwide research after 24 November 2026.


## Update — 24 November 2026: eight-source case

The subsequent archive `research/g8_exact` reports **g(8)=11**. Its lower bound is unconditional. Its universal upper bound is an exact-integer computer-assisted proof **conditional on** g(7)<=9, g(6)<=8, and the externally cited g(5)<=6. The full g(8) verifier was independently replayed in the preparation of this repository; all checks passed (57,487 universal certificates, 28 exhaustive CRT residual cases). This does not independently re-establish g(5), g(6), g(7) or provide formal Lean verification. The general n problem remains open.
