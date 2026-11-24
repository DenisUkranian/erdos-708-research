# Independent audit of the subexponential-support theorem and covering consequence

Date: 2026-11-23.

Audited file: `../analytic/SUBEXPONENTIAL_DENSE_SUPPORT.md`.

## Verdict

**PASS on the full mathematical proof**, including the uniform hinge
statement, the explicit admissible `gamma_epsilon`, and the restricted
integer-cover consequence. The proof uses the already audited diffuse
theorem, the standard uniform fundamental lemma, and the previously
checked quadratic long-interval theorem.

The only noted editorial correction is the final reference's author
initial: the verified manuscript is by Ziming (Z.) Wang, not B. Wang.

## 1. Reference model and positive gap

The distribution assigning mass `theta_P/h` to every `P`-smooth `h`
is normalized by the convergent finite-prime Euler product. Its mean
raw load is exactly `sum w_p/(p-1)`, bounded by `1+log Y` through the
ordinary harmonic sum.

If `w_p>=eta_epsilon`, the integer `j=ceil(2/w_p)` is at most
`J_epsilon=ceil(2/eta_epsilon)`. The geometric probability of
`p^j|h` is `p^(-j)>=Y^(-J_epsilon)`. On this event the difference of
the two reference hinges is exactly one. This establishes the stated
gap independently of the number of primes or their spacing.

## 2. Uniform Rankin tail

With `sigma=1/(4log Y)`, one has `0<sigma<1` for `Y>=2`, so every
Euler product and its logarithmic derivative in the proof converge.
For `p<=Y`,

`z_p=p^(-1+sigma)<=exp(1/4)/p<4/(3p)`.

Consequently `z_p/(1-z_p)<=4/p`, including `p=2`. The inequalities

`log F<=sum z_p/(1-z_p)<=4sum_{p<=Y}1/p<=4log Y`

and

`sum_{h P-smooth}log(h)/h^(1-sigma)`
`=F sum_p(log p)z_p/(1-z_p)<=4Y^4(log Y)^2`

are correct. The raw-load estimate `X(h)<=log h/log 2` and Rankin's
factor `H^(-sigma)=exp(-u/8)` give exactly the displayed tail bound.
No squarefree or bounded-exponent assumption is used.

## 3. Exact smooth-part sieve comparison

For `h<=sqrt M`, both exact smooth-part counts are coprimality counts
on intervals of real length `M/h>=sqrt M=Y^(u/2)`. The fundamental
lemma therefore applies with the same relative error `e(u/2)` on
the prefix and on an arbitrary shifted target interval.

The actual prefix tail is at most `M R`, since the exact-part count
is at most the unrestricted multiple count `M/h`. The loss in the
reference gap on removing `h>sqrt M` is at most `theta_P R<=R`.
The two small-part approximation errors are at most
`2e(u/2)E X`. Thus the final normalized defect bound is precisely

`Delta_2/M<=-Y^(-J)+2R+2e(u/2)(1+log Y)`.

This keeps every normalization factor in the correct direction.
Dropping large exact parts from the target is also valid, including
parts larger than `M` when the shift is large.

## 4. Uniform decay over the full allowed Y range

Write `L=log M`, `y=log Y`, and
`gamma=[16(J+5)]^(-1/2)`. The tail-to-gap ratio is bounded by a
constant times

`y^2 exp((J+4)y-L/(8y))`.

It increases with `y>0`, so the largest value is at
`y=gamma sqrt L`. The exponent there is exactly

`-gamma(J+6)sqrt L`.

For `u>=16`, the sieve error satisfies `e(u/2)<=3C2^(-u/4)`, giving
the second ratio in the note. Its exponent is likewise increasing
with `y` and is uniformly negative at the upper endpoint because

`J gamma^2<1/16<(log 2)/4`.

The polynomial factors are dominated by these negative multiples of
`sqrt L`. Hence both error-to-gap ratios tend to zero uniformly for
every `2<=Y<=exp(gamma sqrt(log M))`. The required lower bounds on
`u` hold for all sufficiently large `M`, uniformly in this range.

If all weights are at most `eta_epsilon`, the diffuse theorem gives
the required approximate hinge directly. Otherwise the comparison
above gives the stronger exact threshold-two hinge. This covers all
weights in `[0,1]` without a gap at equality.

## 5. Raw LP and legitimate integer rounding

For the source-prime boxed covering LP, clipping a dual coordinate
from a value above one down to one cannot reduce the dual objective:
every target divisible by that prime remains on the linear branch
of the target hinge, and the full interval has at least the demanded
total valuation. Thus the compact dual domain `[0,1]^P` is valid.

The uniform hinge inequality bounds every such dual objective by
`(2+epsilon)n`; strong LP duality gives the same bound for the
fractional cover.

An optimal vertex of this boxed covering polytope has at most the
number of source-prime rows strictly fractional. Otherwise a nonzero
linear dependence among those columns permits a two-sided feasible
perturbation, contradicting extremality. Rounding upward preserves
all valuation constraints and costs at most `pi(Y)` additional
positions. This is a specific row-count argument, not an assumed
universal per-instance rounding result.

For a given cutoff function with `log Y(M)=o(sqrt(log M))`, one has
`pi(Y)<=Y=M^{o(1)}=o(sqrt M)`. In the range `M<16n^2`, this is `o(n)`.
The complementary range is covered by the known exact `2n` theorem.
Because distinct source sets have `M>=n+1`, the large-`M` hinge
threshold is eventually met as `n` tends to infinity.

The asymptotic statement is correctly uniform in the interval shift.
Its convergence threshold may depend on the given cutoff function
and on epsilon; no uniform convergence rate over all functions
described only by a little-o condition is claimed.

## Scope

The conclusion is a genuine restricted source-family theorem with
an integer-cover consequence. Polynomial-scale prime factors and
their interaction with the dense smaller-prime component remain
outside this proof. No unrestricted conclusion follows from this
audit.
