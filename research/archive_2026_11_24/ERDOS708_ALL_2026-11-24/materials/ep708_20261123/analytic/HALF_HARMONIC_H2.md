# A fixed-point divisor certificate and the half-harmonic sparse regime

## Status

This is a proof candidate for a substantial special case of H2, not a solution of the unrestricted Erdős 708 problem. The truncated certificate and fixed-point observation were supplied by the parent research agent; the subset-sum strengthening below removes the earlier factor three after prime-power tails are separated. No priority claim is made.

## Definitions

Let `P` be a finite set of primes, all at least `y>=2`. For each `p in P`, let `u_p(e)` be a nondecreasing function of the nonnegative integer `e`, with `u_p(0)=0` and `0<=u_p(e)<=1`. Define

`U(a)=sum_{p in P}u_p(v_p(a))`,

`mu_u=sum_{p in P}sum_{j>=1}(u_p(j)-u_p(j-1))/p^j`,

`mu_0=sum_{p in P}1/p`,

`rho_y(P)=sup_{T>=y} (#{p in P:p<=T}+1)/T`.

The nonnegative increments sum to at most one, so `mu_u<=mu_0`.

## Theorem

If

`mu_u + mu_0 + rho_y(P) <= 1`,                                    (H)

then every positive interval `I` of `M` consecutive integers satisfies

`sum_{a<=M}(U(a)-2)_+ <= sum_{b in I}(U(b)-1)_+`.

In particular, the weight-free condition `2mu_0+rho_y(P)<=1` suffices for all such bounded nondecreasing prime-power profiles.

## 1. A finite subset lemma

For a finite list `z_1,...,z_k in [0,1]`, write `S=sum z_i`, `s_J=sum_{j in J}z_j`, and

`F(z)=sum_{J subset {1,...,k}, 1<s_J<=2}(s_J-1)`.

Then

`F(z)>=(S-1)_+`.                                                  (A)

For `S<=2`, the full set itself proves the inequality whenever `S>1`, and the other cases are trivial. For `S>2`, necessarily `k>=3`. Induct on `k`. Deleting coordinate `i` leaves total `S-z_i>1`. Every carrier subset has size at least two, so

`sum_i F(z with i deleted) = sum_{J:1<s_J<=2}(k-|J|)(s_J-1) <= (k-2)F(z)`.

The induction hypothesis therefore gives

`(k-2)F(z) >= sum_i(S-z_i-1) = (k-1)S-k >= (k-2)(S-1)`.

This proves (A).

Now start with a list of total `S>2` and remove one distinguished entry `v<=1`. Let the remaining list have total `T=S-v>1`. Then

`sum_{J in remaining coordinates, 1<s_J<=2}(s_J-1)(S-s_J) >= S-2`. (B)

If `T<=2`, the full remaining set contributes `(T-1)v>=T+v-2=S-2`, since the difference is `(2-T)(1-v)>=0`. If `T>2`, every carrier has `S-s_J>=S-2`, while (A) gives total carrier coefficient at least `T-1>1`. This proves (B).

## 2. A carrier family controlled by the source interval

Fix `M`. Let `F_M` consist of all `P`-smooth integers `d>1` such that

`1<U(d)<=2` and `Pmax(d)<=M/d`.

Put `h_d=U(d)-1>0`. The family is finite since every member satisfies `d<=M/y`.

For a prefix integer `a` with `U(a)>2`, consider its nonzero prime-power coordinates, and distinguish the coordinate belonging to its largest active prime `p_*`. Apply (B). For every carrier subset `J` of the remaining coordinates use the divisor

`d_J=product_{p in J} p^(v_p(a))`.

The selected factors are complete prime-power components. Consequently `U(d_J)=s_J` and `U(a/d_J)=U(a)-s_J`. Moreover, the entire prime-power component of `p_*` remains outside `d_J`, so

`Pmax(d_J)<=p_*<=a/d_J<=M/d_J`.

Thus `d_J in F_M`. Distinct subsets give distinct divisors. Adding other nonnegative terms yields the pointwise bound

`(U(a)-2)_+ <= sum_{d in F_M,d|a} h_d U(a/d)`.

Summing and expanding the nonnegative prime-power increments gives

`sum_{a<=M}(U(a)-2)_+ <= sum_{d in F_M}h_d sum_{r<=M/d}U(r)`

`<= mu_u M sum_{d in F_M}h_d/d`.                                 (C)

## 3. The truncated signed certificate

For every positive integer `b`, define

`K(b)=sum_{d in F_M} h_d [1_{d|b}-sum_{p in P,p<=M/d}1_{dp|b}]`.

Then

`K(b)<=(U(b)-1)_+`.                                               (D)

Indeed, a positive summand requires `d|b` and no extra factor `p<=M/d` in `b/d`. Since every prime divisor of `d` is itself at most `M/d`, positivity forces

`d = smooth_{P intersect [2,M/d]}(b)`.

There is at most one such `d`: the right side is nonincreasing as `d` increases, so two distinct fixed points are impossible. Every other summand is nonpositive. For the possible positive summand, monotonicity of the profiles gives `h_d=U(d)-1<=U(b)-1`. This proves (D).

Set `T=M/d>=y`. Using the lower and upper counts of multiples in an interval,

`N_I(d)-sum_{p in P,p<=T}N_I(dp)`

`>= T-1-sum_{p in P,p<=T}(T/p+1)`

`>= T [1-mu_0-rho_y(P)]`.

Put `beta=1-mu_0-rho_y(P)`. By (H), `beta>=mu_u>=0`. Summing (D) gives

`sum_{b in I}(U(b)-1)_+ >= beta M sum_{d in F_M}h_d/d`.

Combine this with (C) to prove the theorem. If `F_M` is empty, (C) already shows that the prefix hinge is zero.

## 4. Completely additive weights and tails

For arbitrary nonnegative weights `w_p`, set

`u_p(e)=min(w_p e,1)`, `h_p(e)=(w_p e-1)_+`,

`X_w(n)=sum_p w_p v_p(n)`, `H(n)=sum_p h_p(v_p(n))`.

Then

`(X_w(n)-1)_+=H(n)+(U(n)-1)_+`,

`(X_w(n)-2)_+<=H(n)+(U(n)-2)_+`.

The first identity follows because `H(n)>0` forces at least one capped coordinate to equal one. Every `h_p` is nondecreasing with `h_p(0)=0`, so its prefix sum is no greater than its sum over any interval of the same length, by counting multiples of each prime power. Therefore the bounded-profile theorem implies the raw H2 inequality for `X_w` whenever (H) holds for its capped profiles. In particular, `2mu_0+rho_y(P)<=1` is sufficient uniformly in all nonnegative prime weights, and hence in the usual weights in `[0,1]`.

For these capped profiles, if `L_p=floor(1/w_p)` and `w_p>0`,

`sum_j (u_p(j)-u_p(j-1))/p^j = w_p sum_{j=1}^{L_p}p^(-j) + (1-w_p L_p)p^(-L_p-1)`.

A zero weight contributes zero. The general inequality `mu_u<=mu_0` is enough for the uniform corollary.

## 5. Consequences and remaining limitations

For every fixed `delta>0`, there is `y_delta` such that H2 holds for every finite support `P` with

`min P>=y_delta` and `sum_{p in P}1/p <= 1/2-delta`,

uniformly in the weights, interval length, and interval shift. This follows from the elementary prime-counting estimate `sup_{T>=y}(pi(T)+1)/T -> 0`.

The primes need not lie in one comparable range. They may span arbitrarily many scales, provided their total reciprocal-prime mass is below the stated threshold. The theorem also covers supports of larger reciprocal mass when `mu_u+mu_0+rho_y(P)<=1` still holds.

It does not settle supports with large reciprocal-prime mass and diffuse small weights, or interactions involving a fixed collection of small primes for which the rounding term is not small. These are still part of the unrestricted problem.
