# Independent audit of the diffuse raw-weight theorem

Date: 2026-11-23.

Audited file: `../analytic/DIFFUSE_RAW_WEIGHTS.md`.

## Verdict

**PASS on the mathematical argument and its quantifiers**, subject to
the standard fundamental lemma stated in Section 1. The exact version
of that external input was independently checked in the primary
Lagarias handout described below. The conclusion is a uniform theorem
for individually small raw prime weights, not a theorem for arbitrary
mixtures of small and substantial weights.

Two notation clarifications are recommended: require `d>1` explicitly
in the carrier family, and define `K_d(b)=0` for `d` not dividing `b`
before using `gcd(b/d,...)`.

## 1. External sieve input checked directly

J. C. Lagarias, *Math 675: Combinatorial Sieve: Fundamental Lemma*,
page 1 theorem and page 2 interval example:

https://websites.umich.edu/~lagarias/675notes/Estimate5-2015.pdf

The tilde URL redirected to the no-tilde URL in the candidate note.
The theorem explicitly gives a uniform relative error of order
`u^(-u/2)` and an additive remainder bounded by the sum of the
divisibility remainders for squarefree sieve divisors up to `z^u`.
The dimension-one upper product bound applies uniformly to every
subset of the primes, by comparison with the complete prime set.
For intervals the absolute remainder per divisor is at most one.

Thus the note's additive error `O(z^u)` is supported by the stated
theorem. Taking `u=k/2`, using `T>=z^k` and the elementary bound
`V_Q>=1/z`, gives relative additive error at most
`O(z^(1-k/2))<=O(2^(1-k/2))`. The displayed `E(k)` is decreasing for
`k>=4` after fixing one absolute constant, and tends to zero.

The second primary reference, Granville--Soundararajan's Theorem
1.4.2, was also opened; it states a uniform interval version with
an alternative additive error. The Lagarias statement directly
supports the exact error form used in the candidate proof.

## 2. Partial prime-power carrier checks

The first occurrence crossing a level `s` has weight at most `eta`,
so its accumulated weight is at most `s+eta`. A source above
`s+ell` leaves cofactor weight strictly greater than `ell-eta`.
With `r=floor(ell/eta)`, this requires at least `r` remaining prime
occurrences, including repetitions. Hence `T=M/d>=p^r`.

The exact target certificate is valid even when the crossing cuts
through a prime-power block. Coprimality excludes additional factors
at primes smaller than `p`; the crossing inequalities determine the
unique exponent at `p`, while further copies of `p` in the target
cofactor are correctly allowed. Two distinct positive carriers
would claim two first crossings of the same ordered occurrence list.

For a low prime-power level `j<=J`, a contributing heavy cofactor
still has at least `r-j>=kappa` occurrences after division by `q^j`.
Thus `T/q^j>=p^kappa` before the set is enlarged for the upper bound.
This justifies the second application of the sieve lemma. Terms
failing that inequality were zero already, so no short interval is
incorrectly passed to the sieve.

The high-power tail calculation is also valid:

`sum_{m>=p}1/[m^J(m-1)] <= p^(1-J)/(p-1)`

by telescoping `sum 1/[m(m-1)]`, and
`V_p>=1/(p-1)` converts it to the stated relative error
`eta 2^(1-J)`. No squarefree assumption is hidden here.

## 3. Mean and second-moment checks

After deleting primes above `M`, the total rounding error over
`p^j<=M` is at most `eta`, because distinct prime powers are distinct
integers. The geometric tails contribute at most `2eta`. Therefore
`mu-3eta<=E_0 X<=mu` is uniform in the support.

The mixed-prime moment and the one-prime second moment imply

`E_0 X^2 <= mu^2+2eta mu`.

Combining with the mean loss gives exactly

`E_0(X-mu)^2 <=8eta mu`.

For `1+delta<=mu<=4`, the Lipschitz estimate loses at most
`sqrt(32eta)<=delta`. For `mu>=4`, Chebyshev gives
`Pr(X<2)<=8eta`, and `eta<=1/32` is more than sufficient for the
needed lower bound on `E_0 min(X,2)`.

Finally, interval counts dominate prefix counts separately at every
prime-power level. The first-moment comparison used in (17) therefore
holds for arbitrarily large shifts.

## 4. Uniform choice of parameters and scope

With `ell=1+epsilon` and `delta=epsilon/2`, choosing
`eta<=epsilon^2/128` satisfies the high-mean requirement. As
`eta->0`, the low-mean sufficient condition tends to
`1+epsilon/2<1+epsilon`, so one `eta_epsilon>0` works uniformly for
all prime supports, lengths, shifts, and allowed weights.

Deleting primes above `M` preserves the prefix exactly, and restoring
them can only increase the target hinge. The case `M=1`, empty
carriers, zero weights, and equality at the mean threshold cause
no problem. For `epsilon>1`, the theorem with `epsilon=1` is enough.

No step in this audit yields a bounded number of substantial weights
or permits adjoining a diffuse block to an arbitrary weighted core.
Those remain genuine missing steps in an unrestricted proof.

## 5. Focused audit of the subsequently added one-prime extension

The new Section 5 passes independently. Section 3's elementary
high-mean proof was also reread and remains correct.

For a low light-prime mean, the level comparison is uniform at every
smaller integer length. Discarding light primes above that length
preserves the prefix and only decreases the mean; restoring them on
the target can only help. Since the exceptional prime is not a light
prime, dividing its powers leaves the light load unchanged.

The hinge increment formula (18) is an exact nonnegative integral
identity. For a bounded exceptional profile, the integration variable
lies in `[0,1]`, so the target threshold `s=1-v` remains nonnegative
and the source threshold is exactly `s+ell`. Rescaled target
multiples form an interval with at least the prefix count of
positions. The zero-length prefix case is trivial.

Finally, the exceptional raw tail has nonnegative successive
prime-power increments, so its prefix sum is dominated by its
interval sum. The target hinge identity is exact because a positive
tail forces the capped exceptional profile to equal one. Therefore
the extension is valid for an arbitrary nonnegative exceptional
weight, without an upper bound of one.

This gives zero defect for one exceptional prime. A violation of
`H_(2+epsilon)` must consequently have at least two weights strictly
larger than the diffuse threshold. It still does not extend
automatically to an arbitrary weighted core; the separately audited
fixed-heavy-core theorem handles a specified number with a controlled
error.
