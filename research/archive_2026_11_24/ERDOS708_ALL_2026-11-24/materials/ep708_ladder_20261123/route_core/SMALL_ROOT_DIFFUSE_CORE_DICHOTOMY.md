# A universal root dichotomy with a genuinely small remaining diffuse core

## Status

The carrier dichotomy suggested by the parent is valid. Choosing the light-prime crossing in **decreasing numerical order** gives a further arithmetic restriction: every light prime retained in a non-pure root is at most `M^(eta/(1+delta/4))`.

This is a proved structural reduction for every true positive joint optimum, not a deletion assumption about diffuse source demand. It does not itself establish the remaining amplified model-capacity inequality.

## 1. Setup

Let `c=2+delta`, and let `A={a<=M:X(a)>c}` be the full tail of a true positive joint optimizer with raw prices in `[0,1]`. Let

\[
K=\#\{b\in I:X(b)>1\},\qquad T=M/(K+1).
\]

The proved joint-optimum bounds give `K=O_delta(n)` and `M=O(n^2)`.

Fix `0<eta<=delta/8`. Call a coordinate light when `0<w_p<=eta`, and let

\[
V(a)=\sum_{0<w_p\le\eta}w_pv_p(a).
\]

All zero-price factors are inactive. Set

\[
t_0=1+\delta/4,\qquad \tau=1+\delta/2.
\]

For every source there is a proper divisor root `h|a`, with complement `u=a/h>=2`, such that `X(u)<=tau`, and one of the following two alternatives holds.

**Pure-heavy alternative:** `h` has no light or inactive prime factor, and

\[
X(h)>1+3\delta/4.
\tag{1}
\]

**Small-root alternative:**

\[
h\le K,\qquad X(h)>1+5\delta/8,
\tag{2}
\]

and every light prime dividing `h` satisfies

\[
\boxed{p\le M^{\eta/t_0}.}
\tag{3}
\]

All inactive factors may be put in the deleted complement, so `h` is supported on positive-price primes in both alternatives.

## 2. The pure-heavy case and its unit-complement edge case

Suppose `V(a)<=t_0`. Remove all light occurrences and all inactive factors. The complement has load at most `t_0<tau`, and the remaining root satisfies

\[
X(h)=X(a)-V(a)>2+\delta-t_0=1+3\delta/4.
\]

If this complement is at least two, the construction is complete.

If the complement equals one, the source already has only heavy active prime factors. Delete any one prime occurrence instead. Its price is at most one, and the root remains pure heavy with `X(h)>1+delta`. Thus the proper-complement requirement needed for `floor(M/h)>=2` is maintained in all cases.

## 3. The small-root case

Suppose `V(a)>t_0`. Order the light prime occurrences of `a` in **decreasing numerical order**, retaining multiplicity, and stop at the first time their accumulated price exceeds `t_0`. Let `u_0` be their product. Then

\[
t_0<V(u_0)\le t_0+\eta\le1+3\delta/8<\tau.
\tag{4}
\]

Include all inactive factors in the complement as well, obtaining `u`, and put `h=a/u`. The complement remains within the allowed load. Also

\[
X(h)>2+\delta-(1+3\delta/8)=1+5\delta/8.
\]

Since `X(u)>1`, every target multiple of `u` is hot. An interval of length `M` contains at least `floor(M/u)` such multiples, so

\[
K\ge\lfloor M/u\rfloor\ge a/u=h.
\]

This proves (2).

To prove (3), let `p` be the smallest light prime occurrence in `u_0`, and let `r=Omega(u_0)`. Every included occurrence has price at most `eta`, so

\[
r>t_0/\eta.
\]

All its prime factors are at least `p`; hence

\[
p^{t_0/\eta}<p^r\le u_0\le M.
\]

Every light prime left in `h` is at most the boundary prime `p`, by the decreasing order. This proves (3), including a boundary prime whose exponent is split between `u_0` and `h`.

## 4. A uniform small-prime cutoff relative to every small-root bank

The bound (3) can be tied to the actual hot-position scale. Fix a sieve parameter `U>=8`. On a sparse sequence `n/M->0`, the bound `K=O_delta(n)` implies `T->infinity`.

Choose the light cutoff to obey

\[
\eta\le\min\left\{\delta/8,
\frac{t_0\log T}{U\log M}\right\}.
\tag{5}
\]

The all-scale diffuse transfer lemmas are uniform in `eta`, so it is legitimate for this cutoff to depend on the obstruction. It may additionally be made to tend to zero, for example by imposing any slowly vanishing upper bound.

Put `z=T^(1/U)`. In every small-root alternative, every retained diffuse prime is at most `z`, while its quotient bank has length

\[
M/h\ge M/K>T=z^U.
\tag{6}
\]

Thus the diffuse part of every such root lies in one common prime range with a genuine power gap to **every** one of its target banks. The pure-heavy roots have no diffuse root mass and need no such assertion.

This is stronger than merely saying that the roots have size `O(n)`: it places their remaining diffuse prime support below the bank's sieve scale. It makes the conditional long-cell lemma applicable whenever the actual conditioned cell uses only primes up to this `z`.

The parameter caveat is essential. If `eta` depends on `M/T` and tends to zero, a source-load cutoff `L` only bounds the number of heavy occurrences by `L/eta`, which may grow. A theorem requiring a fixed carrier depth cannot be invoked with that bound without a new uniform estimate. The all-scale concentration and normalized clipping statements themselves do not require fixed depth, so (5) is valid for those statements.

## 5. A safe raw simplified load on all selected roots

Define one raw additive function `Y` by retaining every price greater than `eta` and retaining a light price only when its prime is at most `z`; set every other price to zero. For every carrier root selected by the preceding dichotomy,

\[
\boxed{Y(h)=X(h)>1+\delta/2.}
\tag{7}
\]

The pure-heavy alternative is immediate. The small-root alternative follows from (3)--(5). In addition,

\[
Y\le X,\qquad H_Y\le H_X,
\]

and every source payment in the tau construction satisfies

\[
s_a=X(a)-(1+\tau)
\le X(h)-1=Y(h)-1.
\tag{8}
\]

Consequently, for normalized fractional root demands,

\[
\beta_h\le Y(h)-1.
\tag{9}
\]

To verify (9), the fractional number of sources assigned to a fixed root is no greater than the number `floor(M/h)` of its prefix multiples, by distinctness. Each assigned payment is at most `Y(h)-1`, by (8).

Equations (7)--(9) are legitimate pointwise inputs to a target carrier-capacity argument. They do **not** say that `Y` is optimal, that the original set is its full tail, or that `J_c(Y)` is close to `J_c(X)`. A large amount of source diffuse load may have been removed in the complements. Whole-row equalities can only be used for retained original coordinates against the original set and original paired cover; no new full-tail optimization follows.

## 6. A small weighted mean for the entire retained numerical core

There is a quantitative consequence of the cold-divisor restriction that applies to **all** active primes below `z`, not only to the light coordinates.

Every integer `d<=T=M/(K+1)` satisfies `X(d)<=1`: otherwise its interval multiples would give at least `K+1` hot target positions. For `p<=z=T^(1/U)`, put `e=floor(log T/log p)`. Since `p^e<=T`,

\[
ew_p\le1.
\]

Consequently,

\[
\boxed{
w_p\le\frac1{\lfloor\log T/\log p\rfloor}
\le\frac{\log p}{\log T-\log p}
\le\frac U{U-1}\frac{\log p}{\log T}.
}
\tag{10}
\]

The elementary Chebyshev bound and partial summation imply

\[
\sum_{p\le z}\frac{\log p}{p-1}\le C_0\log z
\]

with an absolute constant `C_0`, for every `z>=2`. Hence

\[
\boxed{
\mu_{\rm core}:=\sum_{p\le z}\frac{w_p}{p-1}
\le\frac{C_0}{U-1}.
}
\tag{11}
\]

Let `V_core` denote the light part supported on primes at most `z`. Ordinary prefix prime-power counts now give

\[
\sum_{h\le K}V_{\rm core}(h)
\le K\sum_{p\le z}\frac{w_p}{p-1}
\le\frac{C_0K}{U-1}.
\tag{12}
\]

In every selected small-root alternative, `V(h)=V_core(h)`; in the pure-heavy alternative, `V(h)=0`. Thus the **distinct selected roots** satisfy

\[
\sum_{h\ {m distinct}}V(h)\le\frac{C_0K}{U-1},
\qquad
\#\{h\ {m distinct}:V(h)>\varepsilon\}
\le\frac{C_0K}{(U-1)\varepsilon}.
\tag{13}
\]

This is a proved aggregate core restriction, rather than an assumption that the core is small. However, the sums in (12)--(13) count a root once. They do not contain its source multiplicity or source payment. Replacing them by `sum_a V(h(a))` or `sum_h s_h V(h)` would be invalid without a new estimate for repeated-root demands.

## 7. Uniform dilution of the high-light source fibres

There is also a genuine multiplicity estimate for the high-light part of the construction. Assume `0<delta<=1` and choose `eta` sufficiently small that

\[
\eta\le\frac{(\delta/8)^2}{32}.
\]

The previously proved large-mean diffuse theorem says that `mu_V>=1+delta/8` would give `J_2(X)<=0`, even after adjoining all other nonnegative coordinates. Therefore a positive joint optimizer must satisfy

\[
\mu_V=\sum_{0<w_p\le\eta}\frac{w_p}{p-1}<1+\delta/8.
\tag{14}
\]

For a fixed root `h`, retain only sources assigned to it by the **high-light** construction. Each quotient `u=a/h` lies in the prefix of length `N_h=floor(M/h)` and satisfies

\[
V(u)>t_0=1+\delta/4.
\]

It includes every inactive factor of the source; no restriction to a prime quotient is made. Distinct sources give distinct quotients. Since the truncated diffuse mean at `N_h` is no larger than (14), the elementary prefix variance estimate gives

\[
\boxed{
\frac{m_h^{\rm high}}{N_h}
\le q_\eta:=\frac{512\eta(1+\delta/8)}{\delta^2}.
}
\tag{15}
\]

The same statement holds for fractional fibre counts. In fact every high-light source has `V(u)<=t_0+eta<tau`, so its tau-payment obeys

\[
s_a=X(a)-(1+\tau)\le X(h)-1.
\]

Thus the corresponding normalized high-light coefficient satisfies

\[
\boxed{
\beta_h^{\rm high}\le q_\eta\,[X(h)-1],
\qquad q_\eta\longrightarrow0.
}
\tag{16}
\]

This dilution is uniform in the shift, root, numerical scale, inactive factors, and prime support. It is stronger than merely having few possible roots. It does not itself control simultaneous congestion from many roots at one target. If low-light and high-light sources share a root, (15)--(16) apply only to the labelled high-light contribution, not to their combined coefficient.

## 8. What is still not justified

Equations (3)--(6) do not show that `V(h)` is small. Many tiny prices may accumulate in a small integer, and the root can retain substantial diffuse load. The normalized model must continue to include that load.

Nor does the power gap automatically turn arbitrary root banks into disjoint exact-state cells. If the deleted block and the root share a boundary prime, source and target state descriptions must retain all exponents correctly. Conditions on heavy primes larger than `z` also fall outside the conditional small-prime sieve lemma unless separately controlled.

Only the small-root alternative has all its bank lengths greater than `T`. Pure-heavy roots may have banks of length two or another bounded number; the small value of `eta` does not make those banks long. They must stay in the argument as a separate part of the same target budget.

The concrete remaining task is to use this shared small-prime core and the actual fractional root assignments to prove the **joint amplified model-capacity lower bound** from the tau version of `JOINT_CLIPPED_DIFFUSE_TRANSFER.md`. Source-state reassignment, repeated roots, and target overlap still require a common arithmetic argument.
