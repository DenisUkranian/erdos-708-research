# Level-count certificates, small-prime anchors, and rough weights

## Status

These are special-case consequences of the fixed-point divisor certificate. They do not settle unrestricted Erdős 708. The exact integer-cover theorem developed separately by the parent agent has a different hypothesis: its source integers are smooth over the specified prime set. A hinge theorem for weights supported on a prime set also permits arbitrary unweighted cofactors in the prefix integers, so these statements must not be conflated.

## 1. Sparse level-count dominance

Let `P` be a finite prime set with `min P>=y`, `mu=sum_{p in P}1/p`, and

`rho=sup_{T>=y}(#{p in P:p<=T}+1)/T`.

If `2mu+rho<=1`, then for every `s>=0`, every `M`, every positive interval `I` of length `M`, and every additive weight `X=sum_p w_p v_p` with `0<=w_p<=1`,

`#{a<=M:X(a)>s+1} <= #{b in I:X(b)>s}`.                           (L)

**Proof.** Use the carrier family

`F_s={d P-smooth: s<X(d)<=s+1, Pmax(d)<=M/d}`.

A heavy prefix integer has, after one occurrence of its largest active prime is removed, residual weight greater than `s`. Choose prime-factor occurrences until their weight first exceeds `s`; the carrier weight is at most `s+1`. The removed largest prime remains outside the carrier, establishing the cutoff condition. Therefore

`1_{X(a)>s+1} <= sum_{d in F_s,d|a} omega_P(a/d)`.

The prefix count is at most `mu M sum_{d in F_s}1/d`. The fixed-point certificate with coefficient one,

`K(b)=sum_{d in F_s}[1_{d|b}-sum_{p in P,p<=M/d}1_{dp|b}]`,

has at most one positive term, and a positive term forces `X(b)>s`. Its interval sum is at least `(1-mu-rho)M sum 1/d`, proving (L).

The same result holds for arbitrary bounded nondecreasing prime-power profiles `U=sum u_p(v_p)`, `u_p(0)=0`, `0<=u_p<=1`. Remove the entire largest-prime component and choose whole remaining components for the carrier. The prefix argument again uses `omega_P` of the quotient.

Integrating (L) over `s>=1` gives H2. The level statement is stronger than that integrated inequality.

## 2. Adding one arbitrary prime

Suppose a class of functions `V`, invariant under multiplication by powers of a prime `q`, satisfies (L) at every length and shift. Then the H2 inequality holds for

`V(n)+u_q(v_q(n))`,

where `u_q` is any bounded nondecreasing profile with values in `[0,1]` and `u_q(0)=0`.

Indeed, (L) integrated over `s>=1` gives H2 for `V` itself. Expand the difference between the hinges of `V+u_q` and `V` one prime-power increment at a time. For exponent `r`, the threshold-one increment integrates the level counts of `V` over

`1-u_q(r) <= s <= 1-u_q(r-1)`,

an interval contained in `[0,1]`. The corresponding threshold-two increment uses `s+1`. Multiples of `q^r` in the shifted interval rescale to a consecutive interval of `floor(M/q^r)` or one more integers. Invariance under `q` and (L) compare these increments; any extra position is harmless. Sum the increments and add the base H2 inequality.

For a sparse support `P`, this proves bounded-profile H2 on `P union {q}` for an arbitrary additional prime. Standard separation of individual prime-power tails then gives raw H2 for all nonnegative weights on that support.

## 3. One anchor inside the level theorem, and a second arbitrary prime

Let `p0` be a fixed prime and let `R` consist of primes at least `y>p0`. Put

`mu_R=sum_{r in R}1/r`,

`rho_R=sup_{T>=y}(#{r in R:r<=T}+1)/T`.

For arbitrary bounded nondecreasing profiles on `{p0} union R`, level dominance (L) holds if

`(2-1/p0)mu_R+2rho_R <= 1-1/p0`.                                 (A)

**Prefix proof.** A prefix integer with `U(a)>s+1`, `s>=0`, must have a nonzero `R` coordinate, because the single anchor contributes at most one. Remove the entire component of its largest active `R` prime. Select whole remaining components until their weight first exceeds `s`. The carrier belongs to

`F_s={d smooth over {p0} union R: s<U(d)<=s+1, d<=M/y, Pmax(d)<=M/d}`.

The quotient retains an `R` prime. Hence the prefix count is at most

`mu_R M sum_{d in F_s}1/d`.

**Interval certificate.** For `T=M/d`, use the factorized certificate

`K_d(b)=1_{d|b}(1-1_{p0|b/d})(1-sum_{r in R,r<=T}1_{r|b/d})`,

with value zero if `d` does not divide `b`. Its expanded form is

`1_{d|b}-1_{p0d|b}-sum_{r<=T}1_{rd|b}+sum_{r<=T}1_{p0rd|b}`.

A positive contribution forces `d` to be the full smooth part of `b` over primes at most `M/d`; hence at most one `d` is positive. It also forces `U(b)>s`. Every other summand is nonpositive. Thus `sum_d K_d(b)<=1_{U(b)>s}`.

The mean term of the expanded interval count is

`T(1-1/p0)(1-sum_{r in R,r<=T}1/r)`.

There are `2+2#{r<=T}` signed terms, each with rounding error at most one. Therefore the interval count is at least

`[(1-1/p0)(1-mu_R)-2rho_R] M sum_{d in F_s}1/d`.

Condition (A) makes this no smaller than the prefix upper bound, proving the level theorem.

Apply section 2 to add a second arbitrary prime `q`, then separate the individual prime-power tails. Consequently H2 holds for all nonnegative raw weights on `{p0,q} union R` whenever (A) holds.

For example, with `p0=3`, `q=2`, every fixed `delta>0` admits a sufficiently large `y_delta` such that H2 holds on

`{2,3} union R`, `min R>=y_delta`, `sum_{r in R}1/r<=2/5-delta`,

for all interval lengths, shifts, and weights. No restriction to one prime-size range is made.

## 4. Rough-weight corollary

Fix

`alpha > 1/(2+sqrt(e)) = approximately 0.2740686`.

For all sufficiently large `M`, H2 holds for every weight vector supported on primes at least `M^alpha`, uniformly in the interval shift.

First separate prime-power tails, leaving bounded profiles. Any prefix integer with bounded weight greater than two contains at least three distinct active primes. Therefore no such integer can contain an active prime greater than `M/y^2`, where `y=M^alpha`. Removing primes above that cutoff leaves the prefix threshold-two hinge unchanged and can only decrease the interval threshold-one hinge. It is therefore enough to handle

`M^alpha <= p <= M^(1-2alpha)`.

If `alpha>1/3`, this support is empty and the statement is immediate. Otherwise the standard prime-harmonic asymptotic (Mertens' theorem), applied at the two endpoints, gives

`sum_{M^alpha<=p<=M^(1-2alpha)}1/p = log((1-2alpha)/alpha)+o(1)`.

The right side is strictly below `1/2` exactly when `alpha>1/(2+sqrt(e))`. The sparse theorem now applies because `rho_y<=sup_{T>=y}(pi(T)+1)/T=o(1)`.

This corollary is a hinge statement. A claim about an exact integer cover does not follow from it merely by rounding. Any asymptotic integer-cover corollary requires checking the transfer argument and closure of the specified source class under passage to retained source subsets.
