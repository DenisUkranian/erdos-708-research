# Ordered prime-prefix carriers: a harmonic-mass-one sufficient condition

Date: 2026-11-23 (Kyiv). Working proof for independent audit. No priority
claim; this is a special case of H2, not a solution of unrestricted
Erdős problem 708.

## Statement

Let `P` be a finite set of primes, all at least `y>=2`. For each `p in P`,
let `u_p(e)` be nondecreasing for nonnegative integers `e`, with
`u_p(0)=0` and `0<=u_p(e)<=1`. Put

`U(a)=sum_{p in P}u_p(v_p(a))`,

`m_p=sum_{j>=1}(u_p(j)-u_p(j-1))/p^j`,

`mu_0(Q)=sum_{q in Q}1/q`, `mu_u(Q)=sum_{q in Q}m_q`,

`rho_y(P)=sup_{T>=y}(#{p in P:p<=T}+1)/T`.

The following sufficient condition implies H2 for every `M` and every
positive interval `I` of `M` consecutive integers:

`mu_0(P intersect [2,p])+mu_u(P intersect (p,infinity))+rho_y(P)<=1`
for every `p in P`.

In particular, since `m_q<=1/q`, the simpler condition

`mu_0(P)+rho_y(P)<=1`                                             (H)

suffices uniformly in all bounded monotone profiles. Here H2 means

`sum_{a<=M}(U(a)-2)_+ <= sum_{b in I}(U(b)-1)_+`.

## 1. A numerical prefix lemma

Let `z_1,...,z_k in [0,1]` have total `S>2`, and write

`S_i=z_1+...+z_i`, `S_0=0`,

`h_i=(S_i-1)_+-(S_{i-1}-1)_+`.

Then `0<=h_i<=1`, `sum h_i=S-1`, and

`sum_i h_i(S-S_i)=sum_{i<j}h_i h_j >= S-2`.                      (1)

For the equality, if `h_i>0`, then all later increments satisfy
`h_j=z_j`; hence `S-S_i=sum_{j>i}h_j`.

For the inequality, the elementary multiaffine inequality

`sum_i t_i-sum_{i<j}t_i t_j<=1` for all `t_i in [0,1]`

is enough. Its maximum occurs at a vertex of the unit cube; at a vertex
with `r` ones the left side is `r-binomial(r,2)<=1` for every
nonnegative integer `r`. Apply it with `t_i=h_i`.

Equivalently, one may take independent Bernoulli variables with success
probabilities `h_i` and use `binomial(N,2)>=N-1` pointwise.

## 2. Carriers and the source estimate

For each `P`-smooth `d>1`, put `p(d)=Pmax(d)`, `e(d)=v_{p(d)}(d)` and

`h_d=(U(d)-1)_+-(U(d/p(d)^e(d))-1)_+`.

Thus `0<=h_d<=u_{p(d)}(e(d))<=1`. For the given `M`, use the finite
family

`F_M={d>1: d is P-smooth and d*p(d)<=M}`.

There is no upper bound on `U(d)` in the definition of this family.

Consider a hot source `a<=M`, with its `P`-prime factors in increasing
order `p_1<...<p_k`, and write

`z_i=u_{p_i}(v_{p_i}(a))`,

`d_i=product_{j<=i}p_j^(v_{p_j}(a))`.

These are the full prime-power prefixes of the `P`-smooth part of `a`.
Their `h_{d_i}` are exactly the increments in (1). Also

`U_{>p_i}(a/d_i)=S-S_i`,

where `U_{>p}(r)=sum_{q in P,q>p}u_q(v_q(r))`.

Whenever the summand in (1) is nonzero, some active prime `q>p_i`
divides `a/d_i`. Thus

`d_i p_i <= d_i q <= a <= M`,

so `d_i in F_M`. The final prefix has zero residual and need not belong
to `F_M`. Inactive coordinates cause no difficulty.

Therefore (1), followed by the addition of other nonnegative terms,
gives the pointwise source inequality

`(U(a)-2)_+ <= sum_{d in F_M,d|a}h_d U_{>p(d)}(a/d)`.

Summing over `a<=M` and expanding the nonnegative prime-power increments
yields

`LHS <= M sum_{d in F_M} (h_d/d) mu_u(P intersect (p(d),infinity))`. (2)

Primes outside `P` in `a` have weight zero and do not enter the prefixes.

## 3. The ordered signed certificate

For a positive integer `b`, define

`K(b)=sum_{d in F_M}h_d[1_{d|b}-sum_{q in P,q<=p(d)}1_{dq|b}]`.

Then

`K(b)<=(U(b)-1)_+`.                                               (3)

To prove this, a positive bracket must have `d|b` and no prime
`q in P`, `q<=p(d)`, dividing `b/d`. Hence `d` is exactly the full
`P intersect [2,p(d)]`-smooth part of `b`. Such positive carriers, if
present, are among the full prime-power prefixes of the `P`-smooth part
of `b`. Along the complete list of those prefixes, their coefficients
`h_d` telescope to `(U(b)-1)_+`. A subcollection has no larger sum,
because every coefficient is nonnegative. Every non-prefix carrier has
a nonpositive bracket. This proves (3).

Unlike the fixed-point certificate, this one permits several positive
summands. Their exact telescoping, rather than uniqueness, is the key.

## 4. Counting the exclusions

Fix `d in F_M`, and put `p=p(d)` and `T=M/d`. We have `T>=p>=y`.
Let `N_I(c)` count the multiples of `c` in `I`. Elementary interval
counts give

`N_I(d)-sum_{q in P,q<=p}N_I(dq)`

`>= T-1-sum_{q in P,q<=p}(T/q+1)`

`>= T[1-mu_0(P intersect [2,p])-rho_y(P)]`,

since `(#{q in P:q<=p}+1)/T <= (#{q in P:q<=T}+1)/T <= rho_y(P)`.

Consequently, summing (3),

`RHS >= M sum_{d in F_M}(h_d/d)`
`                 *[1-mu_0(P intersect [2,p(d)])-rho_y(P)]`.

The stated sufficient condition makes each bracket at least
`mu_u(P intersect (p(d),infinity))`. Comparing with (2) proves H2.

## 5. Completely additive weights

For arbitrary nonnegative prime weights `w_p`, use

`u_p(e)=min(w_p e,1)`, `t_p(e)=(w_p e-1)_+`.

Writing `X(a)=sum_p w_p v_p(a)` and `T(a)=sum_p t_p(v_p(a))`, one has

`(X(a)-1)_+=T(a)+(U(a)-1)_+`,

`(X(a)-2)_+<=T(a)+(U(a)-2)_+`.

Every nondecreasing tail `t_p` has its sum over `[1,M]` no greater than
its sum over any positive interval of length `M`, by expansion into
nonnegative prime-power divisibility indicators. Thus the bounded
profile H2 theorem implies raw valuation H2 under the same condition.

## 6. Asymptotic sparse-support consequence

For every fixed `delta>0`, sufficiently large `min P` and

`sum_{p in P}1/p <= 1-delta`

imply H2 uniformly in `M`, the shift, and all nonnegative prime weights.
This follows from `rho_y(P)<=sup_{T>=y}(pi(T)+1)/T -> 0`.

The primes may occupy many scales. Supports with reciprocal-prime mass
above one, and arbitrary interactions with small primes, remain beyond
this criterion.

For a fixed `alpha>1/(2+e)`, H2 also holds for all sufficiently large
`M` for weights supported on primes at least `M^alpha`. For the bounded
profiles, primes exceeding `M/M^(2alpha)` can be deleted without
changing the prefix hinge: a hot source requires at least three
distinct active prime factors. After deletion the reciprocal-prime
mass is at most

`log((1-2alpha)/alpha)+o(1)<1`

when `alpha<1/3`. The case `alpha>=1/3` has a zero bounded-profile
prefix hinge. The tail transfer then gives the raw statement as well.

