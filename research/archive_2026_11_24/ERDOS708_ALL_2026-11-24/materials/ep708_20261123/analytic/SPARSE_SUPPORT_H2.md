# A sufficient sparse-support condition for H2

## Statement

Let `P` be a finite set of primes, all at least `y>=2`, and let `0<=w_p<=1` be arbitrary real weights, supported on `P`. Put

`k=|P|`, `mu_0=sum_{p in P} 1/p`, `mu_w=sum_{p in P} w_p/(p-1)`.

If

`3 mu_w + mu_0 + (k+1)/y <= 1`,                                      (S)

then, for every integer `M>=1` and every positive interval `I` of `M` consecutive integers,

`sum_{a=1}^M (X_w(a)-2)_+ <= sum_{b in I}(X_w(b)-1)_+`,

where `X_w(n)=sum_p w_p v_p(n)`.

No upper bound on the interval shift, no bound on prime-power exponents, and no common-value restriction on the weights is used.

## A subset-sum observation

Any finite list of numbers in `[0,1]` with total greater than two has a sublist whose total lies in `[4/3,2]`.

If two entries are at least `2/3`, those two form such a sublist. Otherwise there is at most one such entry. Put it first if it exists, then add the remaining entries until the sum first reaches `4/3`. This is possible because the total exceeds two. Every entry after the first is less than `2/3`, and the first entry alone is at most one, so the sum at this first crossing is less than two. This proves the observation, including endpoint cases.

## Carrier family and prefix estimate

Let `F` consist of all `P`-smooth positive integers `d` satisfying

`d<=M/y` and `4/3<=X_w(d)<=2`.

It is finite. For `d in F`, put `h_d=X_w(d)-1`, so `1/3<=h_d<=1`.

If `X_w(a)>2`, apply the observation to the list of prime-factor weights of `a`, including multiplicity. The chosen sublist gives a divisor `d` with `4/3<=X_w(d)<=2`. Because `X_w(a)>2`, at least one positive-weight prime factor remains outside `d`; it is at least `y`. Hence `d<=a/y<=M/y`, so `d in F`. Furthermore,

`X_w(a)-2 <= X_w(a)-X_w(d) = X_w(a/d)`.

Since every term below is nonnegative, this proves the pointwise upper bound

`(X_w(a)-2)_+ <= sum_{d in F, d|a} X_w(a/d)`.

Consequently

`sum_{a<=M}(X_w(a)-2)_+ <= sum_{d in F} sum_{u<=M/d} X_w(u)`

`<= M mu_w sum_{d in F} 1/d`,                                      (1)

because `sum_{u<=L} X_w(u)=sum_{p,j>=1}w_p floor(L/p^j)<=L mu_w`.

## A signed divisor certificate

Define, for every positive integer `b`,

`K(b)=sum_{d in F} h_d [1_{d|b}-sum_{p in P}1_{dp|b}]`.

This certificate satisfies

`K(b) <= (X_w(b)-1)_+`                                              (2)

pointwise. To see this, let `s` be the full `P`-smooth part of `b`. A contributing divisor `d` divides `s`. If `d` is a proper divisor of `s`, some prime `p in P` divides `s/d`; thus the bracket for this `d` is nonpositive. The only possible positive bracket comes from `d=s`, and then its contribution is exactly `h_s=X_w(b)-1`. If `s` is not in `F`, all contributions are nonpositive. This proves (2). The argument permits repeated prime powers and arbitrary weights.

Let `N_I(t)` be the number of multiples of `t` in `I`. The elementary interval bounds give

`N_I(d)-sum_{p in P}N_I(dp)`

`>= M/d-1-sum_{p in P}(M/(dp)+1)`

`= (M/d)(1-mu_0)-(k+1)`

`>= (M/d)[1-mu_0-(k+1)/y]`,

where the last step uses `d<=M/y`. Write `beta=1-mu_0-(k+1)/y`. Condition (S) says `beta>=3mu_w>=0`. Summing (2), and then using `h_d>=1/3`, yields

`sum_{b in I}(X_w(b)-1)_+ >= sum_{b in I}K(b)`

`>= beta M sum_{d in F} h_d/d`

`>= (beta/3) M sum_{d in F}1/d`

`>= mu_w M sum_{d in F}1/d`.

Combine this with (1) to obtain H2. If `F` is empty, (1) already shows that the prefix hinge vanishes. **QED.**

## Uniform weight-free sufficient condition

Since `mu_w<=k/(y-1)` and `mu_0<=k/y`, condition (S) follows from

`3k/(y-1) + (2k+1)/y <= 1`.                                        (S0)

For example, the simpler condition `5k+1<=y-1` is sufficient, because

`3k/(y-1)+(2k+1)/y <= (5k+1)/(y-1)`.

This explicit criterion is intentionally conservative.

## Comparable prime ranges

Fix `C>1`. For every sufficiently large `y` (depending on `C`), every set of primes `P subset [y,Cy]` satisfies (S0), since the elementary prime-counting bound gives `|P|/y=O_C(1/log y)`. Therefore H2 holds for every real weight vector supported in that range, every interval length `M`, and every shift.

This establishes the entire comparable-range regime, not only lengths of order `y^3`. It does not settle arbitrary supports: a set spread over many scales can have `(k+1)/y` arbitrarily large even when its reciprocal-prime sum is small. The term `(k+1)/y` comes from the sum of the one-integer rounding errors for the extension moduli `dp`; controlling that loss across widely separated prime sizes is a remaining obstruction.

## Status and attribution

This is an independently derived sufficient condition and a proof candidate submitted for independent checking. No novelty or priority claim is made. It does not prove the general H2 inequality or the general Erdős 708 conjecture.
