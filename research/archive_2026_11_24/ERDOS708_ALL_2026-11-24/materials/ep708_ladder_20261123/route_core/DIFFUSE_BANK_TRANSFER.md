# Diffuse prices: uniform arithmetic-bank concentration and a shared-budget transfer lemma

## Status

This note proves a new, general intermediate result for the asymptotic Erdős 708 programme. It does **not** prove the unrestricted asymptotic. The missing carrier-certificate construction is stated explicitly in Section 7.

The result does not assume a bounded number of diffuse primes, small reciprocal mass, a gap between the diffuse primes, or a bounded number of banks. It retains every inactive cofactor in a bank: a bank is an entire interval of multiples, not a list of active-prime patterns.

The only analytic input is the uniform rough-number estimate already used and proved from the fundamental lemma in `ep708_synthesis_20261123/analytic/DIFFUSE_RAW_WEIGHTS.md`, Section 1. We denote its relative error by `E(u)`, where `E(u) -> 0` as `u -> infinity`. In particular, for any subset `P` of the primes at most `z`, any real interval `J` of length `N >= z^u`, and sufficiently large fixed `u`,

\[
(1-E(u))N\prod_{p\in P}(1-1/p)
\le \#\{t\in J:(t,\prod_{p\in P}p)=1\}
\le (1+E(u))N\prod_{p\in P}(1-1/p).
\tag{S}
\]

All intervals below contain positive integers. Their real endpoints need not be integers.

## 1. The uniform concentration statement

Let

\[
V(t)=\sum_p v_p(t)\theta_p,\qquad 0\le\theta_p\le\eta,
\qquad
\mu_N=\sum_{p\le N}\frac{\theta_p}{p-1}.
\]

The support is any finite set of primes; primes greater than `N` are allowed. For fixed `B > 0`, assume only `mu_N <= B`.

There is a function `psi_B(eta) -> 0` as `eta -> 0`, independent of `N >= 1`, the support, the individual weights, and the shift, such that

\[
\sum_{1\le t\le N}|V(t)-\mu_N|
\le \sqrt{8\eta B}\,N,
\tag{1}
\]

and, for every real interval `J` of length `N`,

\[
\sum_{t\in J\cap\mathbb Z}(\mu_N-V(t))_+
\le \psi_B(\eta)N.
\tag{2}
\]

More explicitly, for any fixed `epsilon > 0`,

\[
\#\{t\in J\cap\mathbb Z:V(t)<\mu_N-\varepsilon\}
\le q_{B,\eta}(\varepsilon)N,
\qquad q_{B,\eta}(\varepsilon)\longrightarrow0.
\tag{3}
\]

One may take, for all sufficiently small `eta` depending on `B`,

\[
\psi_B(\eta)
=2\eta^{1/4}
 +2B\exp\left(-\tfrac12\eta^{-1/4}+\tfrac12B\right).
\tag{4}
\]

The precise rate is not important for the application. Uniformity at all bank lengths is important.

### 1.1 Source-side proof

Primes exceeding `N` do not divide a positive integer at most `N`. Put `N_0=floor(N)`. The elementary prime-power moment calculation from the diffuse-weight note gives

\[
\sum_{t=1}^{N_0}(V(t)-\mu_N)^2
\le8\eta\mu_N N_0.
\]

Its mean is the raw prime-power mean `sum theta_p/(p-1)`, not merely the strongly additive mean. Cauchy–Schwarz proves (1). The case `N_0=1` is included, since then `mu_N=0`.

### 1.2 A weighted sieve obtained by randomization

Fix `z >= 2`, `t > 0`, and let `P_z` be the supported primes at most `z`. Independently retain each `p in P_z` with probability

\[
g_p=1-e^{-t\theta_p}.
\]

For a fixed integer `m`, the probability that it avoids all retained primes is

\[
\prod_{p\mid m,\ p\in P_z}(1-g_p)
=\exp\left(-t\sum_{p\in P_z}\theta_p1_{p\mid m}\right).
\]

Average the upper bound in (S) over these random subsets. Every subset uses the **same relative error** `E(u)`. Thus, whenever `N >= z^u`,

\[
\sum_{m\in J\cap\mathbb Z}
\exp\left(-t\sum_{p\in P_z}\theta_p1_{p\mid m}\right)
\le (1+E(u))N\prod_{p\in P_z}(1-g_p/p).
\tag{5}
\]

There is no multiplication of the sieve remainder by `exp(tB)`: the remainder is relative before taking the average.

### 1.3 Truncating the prime support without a restriction on reciprocal mass

Take `u=ceil(eta^{-1})`, and suppose first that `z=N^{1/u} >= 2`. The elementary prime reciprocal-sum bound

\[
\sum_{z<p\le N}\frac1{p-1}\le C_0(1+\log u)
\]

is uniform here. It follows, for example, from the usual Chebyshev upper bound and partial summation; no assumption on the chosen prime support is required. Also

\[
\sum_{p\le z}\theta_p\left(\frac1{p-1}-\frac1p\right)
\le\eta\sum_{m\ge2}\frac1{m(m-1)}\le\eta.
\]

Consequently, with

\[
\mu_0=\sum_{p\le z}\frac{\theta_p}{p},
\qquad d_\eta=C_1\eta(1+\log u),
\]

we have

\[
0\le\mu_N-\mu_0\le d_\eta=o(1).
\tag{6}
\]

If `z < 2`, then `N < 2^u` and the same reciprocal-sum estimate gives `mu_N <= d_eta`, after increasing the absolute constant `C_1`. This is the small-bank case; it will be treated without a sieve estimate.

### 1.4 Lower-tail estimate in an arbitrary shifted bank

The raw load `V(m)` is at least the truncated strongly additive load in (5). Using `1-e^{-x} >= x-x^2/2` for `x >= 0`,

\[
\begin{aligned}
\prod_{p\le z}(1-g_p/p)
&\le\exp\left(-\sum_{p\le z}g_p/p\right)\\
&\le\exp\left(-t\mu_0+\tfrac12t^2\eta\mu_0\right).
\end{aligned}
\]

Therefore, for `z >= 2`, exponential Markov gives

\[
\frac1N\#\{m\in J:V(m)<\mu_N-\varepsilon\}
\le (1+E(u))
\exp\left[-t\varepsilon+td_\eta+\tfrac12t^2\eta B\right].
\tag{7}
\]

Taking `t=eta^{-1/2}` proves (3) for every fixed `epsilon > 0`. If `z < 2`, the left side is zero as soon as `d_eta < epsilon`.

For the explicit integrated estimate, put `epsilon_eta=eta^{1/4}`. For small enough `eta`, `d_eta <= epsilon_eta/2` and `E(u) <= 1`. Hence the right side of (7) is at most

\[
2\exp\left[-\tfrac12\eta^{-1/4}+\tfrac12B\right].
\]

On the complementary positions the deficit is at most `epsilon_eta`; on the bad positions it is at most `mu_N <= B`. A real interval of length `N >= 1` has at most `N+1 <= 2N` integers. This proves (2) with (4). The small-bank case has `mu_N <= epsilon_eta/2`, so it satisfies the same bound directly.

## 2. Same-threshold transfer for every monotone Lipschitz core function

Let `f:[0,infinity)->[0,infinity)` be nondecreasing and 1-Lipschitz. From (1),

\[
\sum_{a\le N}f(V(a))
\le\lfloor N\rfloor f(\mu_N)+\sqrt{8\eta B}\,N.
\]

From (2),

\[
\sum_{b\in J}f(V(b))
\ge\#(J\cap\mathbb Z) f(\mu_N)-\psi_B(\eta)N.
\]

Since every interval of real length `N` contains at least `floor(N)` integers,

\[
\sum_{a\le N}f(V(a))
\le\sum_{b\in J}f(V(b))
+\bigl[\sqrt{8\eta B}+\psi_B(\eta)\bigr]N.
\tag{8}
\]

The inequality is uniform in `f`; in particular, `f(v)=(v+h-1)_+` is allowed for every `h >= 0`. This is a **same-threshold** comparison, rather than a comparison with a fixed additive shift between source and target thresholds.

For every positive integer `d`, raw complete additivity gives `V(dt)=V(d)+V(t)`, with no coprimality assumption. Multiples of `d` in `[1,M]` and `I` rescale to intervals of the same real length `N=M/d`. Thus (1)--(8) apply inside that arithmetic bank to the cofactor load `V(b)-V(d)`, with its mean `mu_N`; equivalently, the full-load baseline is `V(d)+mu_N`. All cofactor integers are counted, including factors with zero weight. This exact identity would not hold for an already capped prime profile, so the statement here is expressly about raw `V`.

## 3. A consequence for a true joint optimizer: dense diffuse demand vanishes

Suppose `X` is a true joint maximum of `J_c`, `c>2`, with its full tail `A`, `n=|A|`, paired primal cover `z`, and cost `F=sum z_b >= cn`. Let `V` consist of any subset of its positive coordinates whose weights are at most `eta`. Exact row balance gives

\[
D_V:=\sum_{a\in A}V(a)=\sum_{b\in I}z_bV(b).
\tag{9}
\]

Let `mu=sum theta_p/(p-1) <= B_c`, where the independently proved global-optimum mean bound supplies `B_c`. Write `rho=n/M`.

Cauchy–Schwarz on the source set, using the full-prefix second moment, yields

\[
D_V\le\mu n+\sqrt{8\eta B_c nM}.
\tag{10}
\]

Because `0<=z_b<=1`, the target lower-deficit estimate yields

\[
D_V\ge\mu F-\psi_{B_c}(\eta)M.
\tag{11}
\]

Consequently,

\[
\boxed{
\frac{D_V}{n}
\le \frac{c}{c-1}\sqrt{\frac{8\eta B_c}{\rho}}
+\frac{\psi_{B_c}(\eta)}{(c-1)\rho}.
}
\tag{12}
\]

Thus, for every fixed positive density lower bound, the weighted source demand carried by prices at most `eta` tends to zero uniformly as `eta -> 0`. This conclusion uses genuine whole-row balances and the simultaneous full-tail optimum. It is a structural reduction for the required dense branch; it is not a general deletion result for `rho -> 0`.

The factors `rho^{-1/2}` and `rho^{-1}` expose precisely why using a full-prefix `o(M)` bound would not solve the sparse branch.

## 4. Normalizing all bank errors with one target budget

The following abstract lemma is useful because it **derives** a demand-scale bank norm from a shared target certificate. It never assigns an independent target budget to each bank.

Assume the diffuse load `V` is supported on primes at most `y`, and put

\[
\mu=\sum_p\frac{\theta_p}{p-1}\le B.
\]

Let `d_j` be any finite family of positive roots, possibly with repeated roots. Put

\[
N_j=M/d_j\ge y,\qquad \alpha_j\ge0,
\qquad \mathcal N=\sum_j\alpha_j N_j.
\]

The number of roots, their overlap, and the inactive cofactors are unrestricted. Let `X` be the actual target load and `H=sum_I(X-1)_+`.

Fix `epsilon>0`, `a>0`, and `C>0`. Suppose there are nonnegative target payments `P_j(b)` such that

\[
P_j(b)\ge a\alpha_j
\quad\text{whenever}\quad d_j\mid b,\ V(b)-V(d_j)\ge\mu-\varepsilon,
\tag{13}
\]

and, pointwise on every target,

\[
\sum_jP_j(b)\le C(X(b)-1)_+.
\tag{14}
\]

Let `q=q_{B,eta}(epsilon)` from (3). Then

\[
\boxed{
a(1-q-y^{-1})\mathcal N\le C H.
}
\tag{15}
\]

In particular, if `q+y^{-1}<1`,

\[
\mathcal N\le\frac{C H}{a(1-q-y^{-1})}.
\tag{16}
\]

### Proof

For every bank, `N_j >= y`, so its cofactor mean `mu_{N_j}` is the same number `mu`. Raw additivity makes the number of its target positions with `V(b)-V(d_j) >= mu-epsilon` at least

\[
\lfloor N_j\rfloor-qN_j
\ge(1-q-y^{-1})N_j.
\]

Sum (13) over these positions and all indices `j`. Then sum the **single pointwise bound** (14) over `I`. This gives (15). Overlap causes no separate payment because it is already controlled in (14). Repeated roots are also included: their simultaneous fees must satisfy (14), or the hypothesis is false.

### Source and target approximation errors

For any family of core functions whose individual Lipschitz constants are at most `alpha_j`, the total source error when replacing the cofactor load `V(b)-V(d_j)` by `mu` in those banks is at most

\[
\sqrt{8\eta B}\,\mathcal N.
\]

The corresponding one-sided target-deficit error is at most

\[
\psi_B(\eta)\,\mathcal N.
\]

By (16), their sum is at most

\[
\boxed{
\frac{C[\sqrt{8\eta B}+\psi_B(\eta)]}
 {a(1-q-y^{-1})}\,H.
}
\tag{17}
\]

At a true positive joint optimum, `H=O_c(n)`. Thus, with `a,C,epsilon` fixed before `eta`, this is `o_eta(n)` uniformly in `M`, the source set, the shift, the support, and the number of banks.

This is a conditional joint transfer theorem, not a general core-replacement theorem. In particular, a signed divisor certificate cannot be substituted for (13)--(14) without first producing actual nonnegative target payments satisfying them.

## 5. The exact threshold-compensated deletion identity

There is a different possible route that does not require a carrier certificate. It has an exact necessary target, rather than the unnecessarily stronger assertion that all low-price source demand vanishes.

At a true joint optimum of `J_c`, let `X=W+V`, where `V` is any set of deleted coordinates, and retain the original full tail `A` and original paired primal cover `z`. Put

\[
B_V=\sum_{b\in I}z_b(1-W(b))_+.
\]

The audited finite-variation identity gives

\[
J_c(X)-J_c(W)
=B_V-\sum_{a\in A}(c-W(a))_+\ge0.
\tag{18}
\]

For every `0<tau<c`, one obtains the following **exact** stronger formula:

\[
\boxed{
\begin{aligned}
J_c(X)-J_{c-\tau}(W)
={}&B_V-\sum_{a\in A}\max\{\tau,c-W(a)\}\\
&-\sum_{a\notin A}(W(a)-c+\tau)_+.
\end{aligned}}
\tag{19}
\]

The final sum is over the same prefix `[2,M]`. It must not be dropped in an asserted equality; dropping it gives a valid upper bound.

To check (19), note that `W<=X`, so the strict `c`-tail of `W` is contained in `A`. For `a in A`,

\[
(c-W(a))_+
+(W(a)-c+\tau)_+-(W(a)-c)_+
=\max\{\tau,c-W(a)\}.
\]

For `a notin A`, `(W(a)-c)_+=0`. Substitution in (18) proves the identity.

Thus a sufficient diffuse-deletion theorem would bound `B_V` by the two source terms on the right side of (19), with a suitable demand-scale error. The source recovery term is part of the desired inequality, not a dispensable remainder. The current proofs do not establish this bound uniformly in the sparse branch.

## 6. A legitimate parameter order

For a fixed final budget slack `delta>0`:

1. Use the full-tail exponential moment to select a source-load cutoff `L=L(delta)`; the discarded weighted source demand is a prescribed small fraction of `delta n`.
2. Choose a substantial-weight cutoff `b>0` and any necessary finite carrier depth. If a middle price band is removed, its allowable demand error must be fixed before choosing the band by pigeonhole.
3. Fix the smallest retained target payment `a>0` and the allowed pointwise target factor `C`. These must come from the actual certificate. If payments below `a` are discarded, their total source loss requires a separate proof, for example a bounded source incidence count; it cannot be assumed.
4. Fix `epsilon>0` small relative to the retained payment margin.
5. Only now choose the diffuse cutoff `eta>0` small enough that (17) is below the available slack. One must not choose `eta` first and later allow `a` to tend to zero without revisiting the estimate.
6. Let `n` tend to infinity, so any genuine minimum bank length `y` tends to infinity and source rounding/active-support errors become negligible.

The ordering permits a gap between `eta` and `b`; a small-demand intermediate price band may provide that gap. It does not prove that such a gap or such a certificate suffices on its own.

## 7. What remains to make this a full proof

The new lemma resolves the diffuse **analytic transfer** once a shared positive carrier certificate with (13)--(14) exists. It does not construct that certificate.

For a complete argument one still has to show, after permissible demand-scale cleanup, that every remaining source surplus can be represented by banks satisfying all of the following simultaneously:

* each bank uses its correct raw baseline `V(d_j)+mu`, including the diffuse load already present in the root; any exact-state exclusions require the corresponding conditional concentration statement;
* bank lengths are at least a common cutoff containing the diffuse support, so their mean is the same `mu`;
* the source representation retains every inactive cofactor and all prime powers;
* each retained atom has a uniform positive target fee relative to its core Lipschitz coefficient;
* all the nonnegative atom payments fit into one target hinge as in (14), including simultaneous different source arities;
* discarded small-fee atoms cost `o_delta(n)` in **weighted source surplus**, not merely `o(M)` in prefix count.

These requirements isolate the actual joint arithmetic step. They cannot be inferred from separate matching results, separate core histograms, or a signed formula for a target residual. In particular, neither the dense corollary (12) nor the conditional transfer theorem (17) proves the unrestricted asymptotic by itself.
