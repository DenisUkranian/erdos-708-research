# Independent audit of HALF_HARMONIC_H2.md

Date: 2026-11-23 (Kyiv).

The proof in `../analytic/HALF_HARMONIC_H2.md` passes independent audit.

- In subset lemma (A), the induction gives
  `(k-2)F >= (k-1)S-k`; the claimed comparison with
  `(k-2)(S-1)` has the nonnegative difference `S-2`.
- The two cases of (B) are valid, including arbitrary zero coordinates.
- Selecting complete prime-power coordinates, rather than individual
  prime-factor occurrences, makes the carrier divisors distinct and
  preserves additivity between the divisor and its cofactor.
- The self-smoothness condition and the fixed-point monotonicity justify
  at most one positive signed summand. Repeated prime powers and an
  arbitrarily large interval shift do not change this.
- The interval-counting error is exactly controlled by `rho_y(P)`.
- The cap-and-tail identities, and interval dominance for every
  nondecreasing prime-power tail, are valid. They extend the bounded
  profile conclusion to arbitrary nonnegative completely additive
  prime weights.

This audit finds no missing case or unsupported step. The result is a
sufficient condition, not an unrestricted proof of H2 or problem 708.

An ordered-prefix variant in `ORDERED_CARRIER_H2.md` appears to replace
the weight-free hypothesis `2 mu_0+rho<=1` by `mu_0+rho<=1`. It is a
separate proof candidate sent to the parent for independent review.
