# Independent audit: truncated carrier exclusions

Date: 2026-11-23 (Kyiv).

## Verdict and scope

The strengthened signed-certificate argument is **valid**. It gives a
newly derived sufficient condition within this working session, without
any priority claim and without solving unrestricted H2.

Let `P` be a finite prime set, `p>=y>=2`, and `0<=w_p<=1`. Define

`X(t)=sum_p w_p v_p(t)`,
`mu_0=sum_p 1/p`,
`mu_w=sum_p w_p/(p-1)`,
`rho_y=sup_{t>=y} (#{p in P:p<=t}+1)/t`.

Then raw valuation H2 holds for every interval length and every shift if

`3 mu_w + mu_0 + rho_y <= 1`.

For a finite support `p_1<...<p_k`, the supremum is exactly
`max(1/y, max_j (j+1)/p_j)`. If `y=p_1`, the term `1/y` is redundant.

## 1. Carrier choice and the prefix inequality

Fix the interval length `M`. Use the finite carrier family

`F={d: d is P-smooth, 1<X(d)<=2, d*Pmax(d)<=M}`,

and set `h_d=X(d)-1`, so `0<h_d<=1`.

Let `a<=M` be hot, meaning `X(a)>2`. Let `s` be the full `P`-smooth part
of `a`, and remove one occurrence of its largest prime `p`, obtaining
`u=s/p`. Then `X(u)>1` because `w_p<=1`.

If `X(u)>=4/3`, either use `d=u` when `X(u)<=2`, or apply the elementary
subset-sum lemma to the prime-factor weights of `u`. In both cases we get
`d|u` with `4/3<=X(d)<=2`. Since `Pmax(d)<=p` and `dp<=s<=a<=M`, this
carrier lies in `F`. Also

`X(a)-2 <= X(a/d) <= 3 h_d X(a/d)`.

If `1<X(u)<4/3`, set `d=u`. Put `h=X(d)-1`, so `0<h<1/3`, and `w=w_p`.
There are no other positive-weight factors outside `d`; factors of `a`
outside `P` have weight zero. Consequently

`X(a)-2=h+w-1 <= h*w = h X(a/d) <= 3h X(a/d)`,

because `(1-h)(1-w)>=0`. Again `d Pmax(d)<=dp<=M`.

Thus, pointwise on the prefix,

`(X(a)-2)_+ <= 3 sum_{d in F,d|a} h_d X(a/d)`.

After summation and the geometric-series bound for valuation sums,

`LHS <= 3 M mu_w sum_{d in F} h_d/d`.

**Necessary wording detail:** when `a` contains primes outside `P`, the
small-mass case uses the remaining `P`-smooth part `s/p`, not all of `a/p`.

## 2. At most one positive carrier summand

Define

`K(b)=sum_{d in F} h_d [1_{d|b}-sum_{p in P,p<=M/d}1_{dp|b}]`.

A positive bracket requires both `d|b` and the absence of any prime
`p in P`, `p<=M/d`, from `b/d`. The self-smoothness condition on `F`
ensures all primes dividing `d` are at most `M/d`. Hence a positive
carrier must be exactly the full `P_{<=M/d}`-smooth part of `b`.

Two such carriers cannot coexist. If `d<e` were positive, then `M/d>M/e`,
so the smooth part at threshold `M/d` would be at least the smooth part
at threshold `M/e`. This would give `d>=e`, a contradiction.

All other summands are nonpositive. The unique possible positive one is
`h_d=X(d)-1<=X(b)-1`; therefore

`K(b)<=(X(b)-1)_+`.

This argument remains valid for repeated prime powers and arbitrary real
weights in `[0,1]`.

## 3. Counting the truncated exclusions

For `d in F`, put `t=M/d`. We have `t>=Pmax(d)>=y`. Elementary interval
counts yield

`N_I(d)-sum_{p in P,p<=t}N_I(dp)`
`>=t-1-sum_{p<=t}(t/p+1)`
`>=t(1-mu_0-rho_y)`.

Let `beta=1-mu_0-rho_y`. The hypothesis gives `beta>=3mu_w>=0`.
Summing the signed certificate gives

`RHS>=beta M sum_F h_d/d>=3mu_w M sum_F h_d/d>=LHS`.

An empty `F` forces a zero prefix hinge by the carrier argument, so no
separate nonemptiness assumption is needed.

## 4. A stronger criterion when prefix sources have at most three active prime copies

For a fixed `M`, suppose every integer `a<=M` contains at most three
prime-factor occurrences from the positive-weight support, counting
multiplicity. In particular, it suffices that `M<y^4`.

Then the coefficient `3` can be replaced by `1`: H2 holds if

`mu_w + mu_0 + rho_y <= 1`.

Indeed, any hot `a` has exactly three positive-weight prime-factor
occurrences. Remove one occurrence of its largest active prime `p` from
its full active-prime smooth part `s`, and take `d=s/p`. The remaining
two weights have sum `1<X(d)<=2`, so `d` is an admissible carrier. Put
`h=X(d)-1` and `w=w_p`. Then

`X(a)-2=h+w-1 <= h*w = h X(a/d)`,

because `0<h<=1`, `0<=w<=1`, and `(1-h)(1-w)>=0`. Hence

`LHS <= M mu_w sum_F h_d/d`.

The same signed certificate and interval count from Sections 2--3 now
give the stated stronger criterion. Zero-weight primes may be removed
at the outset, so they do not affect the occurrence hypothesis.

This argument covers arbitrary real weights, including repeated prime
powers. It does not require unit weights.

## 5. An asymptotic rough-support consequence

Fix `alpha` with

`1/(2+exp(1/2)) < alpha < 1/3`.

The lower endpoint is approximately `0.274068619061197`.

For all sufficiently large `M`, H2 holds for every weight system whose
positive-weight primes are at least `y=M^alpha`.

To see this, primes exceeding `M/y^2` may be deleted without changing the
prefix hinge. Any hot source would need at least three positive-weight
prime-factor copies; one larger than `M/y^2` together with two copies at
least `y` would exceed `M`. Deletion only decreases the target hinge.

For the retained support, the standard reciprocal-prime asymptotic gives

`mu_0 <= log((1-2alpha)/alpha)+o(1)`.

Also `mu_w<=mu_0+o(1)` and `rho_y=o(1)`. Since the displayed range has
`alpha>1/4`, we have `M<y^4` for `M>1`, and Section 4 applies. Its
sufficient condition follows from

`2 log((1-2alpha)/alpha)<1`.

For `alpha>1/3` the prefix hinge is identically zero, so that range is
immediate (and `alpha=1/3` has a zero prefix hinge too). The lower
boundary is not claimed. This consequence concerns the
rough-support class only; arbitrary mixed-scale supports remain open.

