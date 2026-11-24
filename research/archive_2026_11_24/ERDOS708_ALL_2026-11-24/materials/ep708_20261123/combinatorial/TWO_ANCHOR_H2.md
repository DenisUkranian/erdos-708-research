# Two small-prime anchors can be absorbed into the ordered certificate

Date: 2026-11-23 (Kyiv). Working theorem for independent audit. No
priority claim; the unrestricted problem remains open in this work.

## Statement

Let `Q` contain at most two primes, and let `R` be a disjoint finite
prime set with every `r in R` at least `y>max Q`. Empty `Q` is allowed.
For every prime in `P=Q union R`, let `u_p(e)` be a nondecreasing
profile with `u_p(0)=0` and values in `[0,1]`. Define

`U(a)=sum_{p in P}u_p(v_p(a))`,

`mu_R=sum_{r in R}1/r`,

`rho_y(R)=sup_{T>=y}(#{r in R:r<=T}+1)/T`,

`delta_Q=product_{q in Q}(1-1/q)`, `C_Q=2^|Q|`.

If

`mu_R + (C_Q/delta_Q) rho_y(R) <= 1`,                            (H)

then H2 holds for every positive interval `I` of `M` consecutive
integers:

`sum_{a<=M}(U(a)-2)_+ <= sum_{b in I}(U(b)-1)_+`.

For two anchors, `C_Q/delta_Q<=12`, uniformly in the identities of the
two primes. In particular, for any fixed `epsilon>0`, sufficiently
large `y` and `mu_R<=1-epsilon` imply H2, with no charge for the
reciprocal mass of the two smaller primes.

The cap-and-tail argument then gives raw H2 for completely additive
nonnegative prime weights on the same support.

## 1. A coprimality count

Put `L_Q=product_{q in Q}q`. For any real interval `J` of length `T`,
Möbius inversion and the elementary count of multiples give

`#{m in J: gcd(m,L_Q)=1} = delta_Q T + error`,

with `|error|<=C_Q`. The same bound holds for a prefix `[1,T]`.
Since any `r in R` is coprime to `L_Q`, the count of numbers that are
both `r`-divisible and coprime to `L_Q` has main term `delta_Q T/r`
and the same error bound.

## 2. Carriers and the source bound

For a `P`-smooth integer `d>1`, let `p=p(d)=Pmax(d)`, `e=v_p(d)` and

`h_d=(U(d)-1)_+-(U(d/p^e)-1)_+`.

Use only carriers with `h_d>0` and

`M/d >= max(p,y)`.

Such a positive carrier contains at least two distinct active prime
coordinates. Since there are at most two anchors below every prime
of `R`, its largest prime is at least every prime of `Q`.

For a source `a` with `U(a)>2`, apply the numerical prefix lemma from
`ORDERED_CARRIER_H2.md` to its full prime-power prefixes `d_i`. Every
nonzero summand `h_{d_i}(U(a)-U(d_i))` has a larger active prime
outside `d_i`. Since `p(d_i)>=max Q`, this larger prime belongs to
`R`, and is at least `y`. Thus `M/d_i>=max(p(d_i),y)`, as required.
The full prefix also contains every `Q`-prime power occurring in `a`,
so its cofactor is coprime to `L_Q`.

Consequently, pointwise,

`(U(a)-2)_+ <= sum_{d|a, d in F_M}`
`                 h_d 1[gcd(a/d,L_Q)=1] U_{R,>p(d)}(a/d)`.

For `T=M/d`, define

`m_r=sum_{j>=1}(u_r(j)-u_r(j-1))/r^j`.

The coprimality count and nonnegative profile increments give

`sum_{m<=T,gcd(m,L_Q)=1} U_{R,>p}(m)`

`<= delta_Q T sum_{r in R,r>p}m_r`
`   + C_Q [pi_R(T)-pi_R(p)]`.                                   (1)

For the error, only prime powers `r^j<=T` contribute, and the sum of
increments for any fixed prime is at most one. Also `p<=T` for every
carrier. Summing (1) after multiplication by `h_d` bounds the entire
prefix hinge.

## 3. The signed certificate

Define

`K(b)=sum_{d in F_M} h_d 1[d|b] 1[gcd(b/d,L_Q)=1]`
`                       *[1-sum_{r in R,r<=p(d)}1[r|b/d]]`.

Then `K(b)<=(U(b)-1)_+`. Indeed, any positive summand requires `d` to
contain the full `Q`-smooth part of `b`, together with the full
`R intersect [2,p(d)]`-smooth part. Since `p(d)>=max Q`, this means
that `d` is an actual full prime-power prefix of the `P`-smooth part
of `b`. Its coefficient is the corresponding hinge increment. The
sum of all such positive increments is at most `(U(b)-1)_+` by
telescoping; every other summand is zero or negative.

For each carrier `d`, the sum of its bracketed expression over `I`
is at least

`delta_Q T [1-sum_{r in R,r<=p}1/r]`
` - C_Q [pi_R(p)+1]`.                                           (2)

The source and target errors in (1)--(2) combine to just

`C_Q [pi_R(T)+1]`,

because the source counts only the primes above `p` and the target
only those at most `p`.

Using `m_r<=1/r`, target contribution minus the source upper bound is
therefore at least

`delta_Q T [1-mu_R] - C_Q [pi_R(T)+1]`

`>= delta_Q T [1-mu_R-(C_Q/delta_Q)rho_y(R)] >= 0`

under (H). Multiplying by `h_d>=0` and summing proves H2.

## 4. Edge cases and limits

If the source hinge is positive, it involves at least three active
prime coordinates, so with at most two anchors there is an `R` prime.
Thus the argument does not silently discard an anchor-only hot source.

Zero profile coordinates, repeated prime powers, and prime factors
outside `P` cause no change to the proof. If `R` is empty, the source
hinge is identically zero and H2 is immediate, independently of (H).

This proof does not immediately absorb a third arbitrary anchor: a
positive carrier may then lie below the largest anchor, and its
remaining source cofactor can contain another anchor rather than an
`R` prime. Both the cutoff `T>=y` and the full-anchor coprimality
condition would need a new argument.
