# Independent full audit of the fixed-heavy-core extension

Date: 2026-11-23.

Audited file: `../analytic/FIXED_HEAVY_CORE.md`.

## Verdict

**PASS on the mathematics, constants, and quantifiers.** The theorem
is uniform in the actual values of the at most `k` exceptional primes,
including primes larger than the interval length, and in the growing
diffuse support. Its dependence on a fixed `k` remains essential.

The external standard sieve input was independently verified already
in `DIFFUSE_RAW_WEIGHTS_AUDIT.md` against the primary Lagarias handout.
This audit checks the additional exceptional-prime argument and the
complete passage to the raw hinge defect.

## 1. Uniformity with arbitrary exceptional primes

In the exact Möbius identity, each divisor `f` of the product of the
exceptional primes above `z` is coprime to the ordinary small-prime
sieving set. Thus dividing the interval by `f` preserves the ordinary
coprimality condition.

For `f<=T/z^(r/2)`, the divided interval has length at least `z^(r/2)`.
The sum of relative errors is bounded by

`e_0(r/2) product_{p in E_large}(1+1/p)/(1-1/p)`

`<=3^k e_0(r/2)`.

For larger `f`, the exact count and the absolute main term together
are at most `3z^(r/2)`. There are at most `2^k` divisors. The desired
main-term density is at least `T z^(-1)2^(-k)`, so the relative error
is at most

`3*4^k z^(1-r/2)<=3*4^k2^(1-r/2)`.

This also controls an exceptional prime much larger than `T`; no
unproved smallness restriction on the exceptional primes is present.
The resulting `e_k(r)` decreases for `r>=8` and tends to zero for
fixed `k`.

## 2. Conditional level comparison

The partial light-prime carrier is coprime to the exceptional-prime
product. Its positive target indicator therefore forces the target
itself to be coprime to that product, in addition to being the unique
first crossing of the light-weight level.

For every contributing low-power term, removal of `q^j` leaves at
least `r-j>=kappa` light-prime occurrences. Consequently the divided
cofactor interval has length at least `p^kappa`, even when its
original length is real rather than integer. The exceptional-prime
sieve estimate therefore applies exactly where used.

Dropping all coprimality conditions in the high-power tail costs a
factor at most `theta_E^(-1)<=2^k`. This gives the displayed
`eta 2^(k+1-J)`, with no missing factor of `p` or of a prime-power
exponent. The source and target estimates are compatible under (7).

## 3. The exact exceptional part

For a fixed exceptional-smooth `h`, both the prefix cofactor set and
the target cofactor interval have the same real length `M/h` and
are restricted by the same exact coprimality condition. This is
precisely what is needed to apply the conditional level comparison.
Conditioning merely on divisibility by `h` would not have been enough;
the written proof correctly uses the unique exact exceptional part.

If `s-Z(h)>=0`, the conditional level theorem directly gives no
positive defect. If `s-Z(h)<0`, every exceptional-coprime target is
counted. The source is bounded by the full exceptional-coprime
prefix count, so ordinary finite inclusion-exclusion bounds the
difference by `2^{|E|+1}`.

Targets with `h>M` have no prefix counterpart and contribute only
nonnegatively to the right side. Their deletion is legitimate.
Integrating the count of `h` with `Z(h)>s` over `s>=1` gives exactly

`2^{|E|+1} sum_{h<=M, E-smooth}(Z(h)-1)_+`.

The estimates `Z(h)<=Omega(h)<=log_2 M` and
`#{h<=M:E-smooth}<=(1+log_2 M)^{|E|}` then give the stated simpler
polylogarithmic bound.

## 4. High means and the parameter choice

After removing primes greater than `M`, the light first- and
second-moment estimates from the diffuse theorem apply. Adding the
exceptional raw coordinates only increases `min(X,2)`, so the
high-light-mean branch proves full `H_2`, with zero defect, for the
combined weights.

The low-mean condition has the limiting strict gap
`1+epsilon/2<1+epsilon` as `eta->0`, while `e_k(r),e_k(kappa)` and
the high-power error all vanish. Thus one positive
`eta_{epsilon,k}` works for all supports, lengths, shifts, and
exceptional-prime values. The cases `epsilon>1`, `k=0`, zero weights,
empty carrier families, and `M=1` are covered by the stated monotonicity
or trivial zero-prefix observations.

## 5. Clarifications recommended for the final transcription

1. Delete primes above `M` before the case split in Section 3, and
   define `mu_L` after that deletion. Section 5 currently says this is
   done "at the outset", which expresses the correct intention but
   appears after the case split in the written order. The original
   untruncated light mean must not be used for the high-mean branch.
   Restoring discarded primes increases only the target hinge; the
   sharper exceptional-part bound is unchanged or weakened safely.
2. Require `d>1` explicitly when defining eligible carriers.
3. Define `K_d(b)=0` when `d` does not divide `b`, before evaluating
   the coprimality condition on `b/d`.

No substantive proof correction is required. The growing-heavy-core
case remains outside the theorem; substituting a growing `k` into
either the threshold or the error bound does not produce a uniform
asymptotic solution.

## 6. Audit of the added quantitative extension

The subsequently added Section 6 also passes. It permits a controlled
growing `k`, and supersedes the unrestricted wording of the preceding
paragraph only in that specifically quantified range.

For `u>=16`,

`e_0(u/2)<=3C2^(-u/4)`,

because `(u/4)^(-u/8)<=2^(-u/4)`. Consequently

`e_k(u)<=3C3^k2^(-u/4)+6*4^k2^(-u/2)`.

Taking `u>=16k+R_epsilon` suppresses the two exponential factors in
`k`, as claimed. If `A=(1+epsilon)/c_epsilon` is at least both `32`
and `2R_epsilon+2`, then

`A(k+1)>=32k+2R_epsilon+2`.

Taking the floor therefore gives the required bound on `r`, and
hence on `kappa` and `J`.

For the low-mean condition, the tail is at most `eta`, the two sieve
errors are at most `epsilon/16`, and `eta<=epsilon^2/128<=epsilon/128`.
The difference between the lower right side and upper left side of
the sufficient condition is at least

`3epsilon/8-3epsilon^2/32-2eta+eta epsilon/16`

`>=46epsilon/128-191epsilon^2/2048>0`

for `0<epsilon<=1`. Thus `eta_{epsilon,k}=c_epsilon/(k+1)` is justified
uniformly in the exceptional-prime values and the support.

Finally, the logarithm of the defect bound is

`(k+1)[log 2+log(1+log_2 M)]`.

It is `o(log M)` when `k=o(log M/log log M)`, and at most
`(1-delta+o(1))log n` when `M<=16n^2` and
`k<=(1-delta)log n/log log n`. The stated `M^{o(1)}` and
`n^{1-delta+o(1)}` bounds follow. The resulting exclusion of raw dual
witnesses is correctly distinguished from a per-instance integer
rounding theorem.
