# Relative diffuse concentration in arbitrarily large heavy-profile cells

## Status

This note proves a conditional extension of `DIFFUSE_BANK_TRANSFER.md`. It allows an arbitrary excluded heavy-prime set, with no bound on its cardinality or reciprocal mass. The price for that generality is an explicit scale gap: the quotient interval must have length at least `z^U`, where every conditioned prime and every diffuse prime is at most `z` and `U` is large.

The statement does not apply to short exact-profile banks merely because they arise in a full tail. Verifying this scale gap at every necessary conditioned atom remains part of the carrier-certificate problem.

## 1. Statement

Let `z>=2`, `U>=8`, and let `P` and `H` be disjoint finite sets of primes at most `z`. Put

\[
V(t)=\sum_{p\in P}\theta_pv_p(t),\quad
0\le\theta_p\le\eta,\quad
\mu=\sum_{p\in P}\frac{\theta_p}{p-1}\le B,
\]

\[
\mathfrak v_H=\prod_{q\in H}(1-1/q).
\]

For a real interval `J` of length `N>=z^U`, define the cell

\[
\mathcal C_H(J)=\{t\in J\cap\mathbb Z:(t,\prod_{q\in H}q)=1\}.
\]

Write `E(u)` for the relative sieve error in the preceding note. For sufficiently large `U`, it is at most one at `U/2` and `U`.

For every `epsilon>eta` and every `t>0`,

\[
\#\{m\in\mathcal C_H(J):V(m)<\mu-\varepsilon\}
\le q\,N\mathfrak v_H,
\tag{1}
\]

where

\[
q=(1+E(U))\exp\left[-t(\varepsilon-\eta)
+\tfrac12t^2\eta B\right].
\tag{2}
\]

In particular, define

\[
\phi=(1+E(U))\varepsilon+Bq.
\]

Then

\[
\sum_{m\in\mathcal C_H(J)}(\mu-V(m))_+
\le \phi N\mathfrak v_H.
\tag{3}
\]

For the source prefix cell, the corresponding two-sided estimate is

\[
\sum_{1\le m\le N,\ (m,H)=1}|V(m)-\mu|
\le\xi N\mathfrak v_H,
\tag{4}
\]

with

\[
\xi=B[E(U/2)+E(U)]
+2\eta\,2^{2-U/2}+2\phi.
\tag{5}
\]

Here `(m,H)=1` is shorthand for avoidance of all primes in `H`.

For example, take `epsilon=eta^{1/4}`, `t=eta^{-1/2}`, and first let `eta->0` while choosing `U=ceil(eta^{-1})`. Then `q,phi,xi -> 0`, uniformly in `P,H,z,N`, the shift, and all individual prices.

## 2. Conditional lower-tail proof

Retain each diffuse prime `p in P` independently with probability `1-exp(-t theta_p)`, and always exclude every prime in `H`. Since the two sets are disjoint, averaging the uniform sieve bound over the random retained subset gives

\[
\sum_{m\in\mathcal C_H(J)}
\exp\left(-t\sum_{p\in P}\theta_p1_{p\mid m}\right)
\le(1+E(U))N\mathfrak v_H
\prod_{p\in P}\left(1-\frac{1-e^{-t\theta_p}}p\right).
\tag{6}
\]

Put `mu_0=sum theta_p/p`. Then `0<=mu-mu_0<=eta`, since

\[
\sum_p\theta_p\left(\frac1{p-1}-\frac1p\right)
\le\eta\sum_{m\ge2}\frac1{m(m-1)}=\eta.
\]

As before, the product in (6) is at most

\[
\exp(-t\mu_0+\tfrac12t^2\eta\mu_0).
\]

Raw `V` dominates its strongly additive truncation. Exponential Markov proves (1)--(2). The total cell count is at most `(1+E(U))N mathfrak v_H`. Splitting its lower deficit at `epsilon` proves (3).

No factor depending exponentially on `|H|` is present. The factor `mathfrak v_H` remains in the estimate rather than being discarded.

## 3. Conditional source mean, with every raw prime power retained

Expand the raw source load by prime powers. For `p in P` and `p^j<=sqrt(N)`, multiplication or division by `p^j` preserves avoidance of `H`, because `P` and `H` are disjoint. The quotient interval has length

\[
N/p^j\ge\sqrt N\ge z^{U/2}.
\]

Apply the upper sieve bound there. Summing all these low prime-power levels gives at most

\[
(1+E(U/2))N\mathfrak v_H\mu.
\]

For the remaining levels, discard the avoidance condition but retain ordinary divisibility counts. If `j_p` is the first exponent with `p^{j_p}>sqrt(N)`, then

\[
\sum_{j\ge j_p}p^{-j}
\le2p^{-j_p}\le2N^{-1/2}.
\]

There are at most `z` primes in `P`. Therefore the contribution of all high levels is at most

\[
2\eta z\sqrt N.
\]

The elementary telescoping product gives

\[
\mathfrak v_H
\ge\prod_{m=2}^{\lfloor z\rfloor}(1-1/m)
=1/\lfloor z\rfloor\ge1/z.
\]

Thus the relative high-power contribution is at most

\[
2\eta z^2/\sqrt N
\le2\eta z^{2-U/2}
\le2\eta 2^{2-U/2}.
\]

We have proved

\[
\sum_{m\le N,\ (m,H)=1}V(m)
\le N\mathfrak v_H
\left[(1+E(U/2))\mu+2\eta2^{2-U/2}\right].
\tag{7}
\]

The prefix cell contains at least `(1-E(U))N mathfrak v_H` integers. Subtracting its mean baseline from (7), and then using

\[
|V-\mu|=(V-\mu)+2(\mu-V)_+,
\]

with (3) for the prefix interval, proves (4)--(5).

## 4. Exact-profile banks, arbitrary roots, and conditional transfer

Let `d` be any positive integer. Its cell in the original target interval is

\[
\{b\in I:d\mid b,\ (b/d,H)=1\}.
\]

No coprimality of `d` and `P` is needed: raw additivity gives

\[
V(b)=V(d)+V(b/d).
\]

The correct baseline is `V(d)+mu`, with real quotient length `N=M/d`. Conditions on exact heavy exponents are encoded by their forced heavy part in `d` and the excluded set `H` in the quotient. Inactive primes are unrestricted unless deliberately placed in `H`.

For a nonnegative nondecreasing 1-Lipschitz function `f` with `f(0)=0`, the source/target cell comparison follows from (3)--(5) and the two relative cell counts:

\[
\sum_{m\le N,\ (m,H)=1}f(V(m))
\le\sum_{m\in\mathcal C_H(J)}f(V(m))
+[\xi+\phi+2BE(U)]N\mathfrak v_H.
\tag{8}
\]

The term `2BE(U)` pays for the possible difference of the two cell counts, since `f(mu)<=mu<=B`. For general nonnegative 1-Lipschitz `f`, replace that term by `2f(mu)E(U)`.

## 5. A conditional shared-budget normalization

Allow an arbitrary family of roots `d_j`, excluded sets `H_j`, and nonnegative coefficients `alpha_j`. Assume every prime in every `H_j` and in the diffuse support is at most the same `z`, the two supports are disjoint, and `N_j=M/d_j>=z^U`.

Put

\[
\mathcal N_H=\sum_j\alpha_jN_j\mathfrak v_{H_j}.
\]

Suppose nonnegative payments `P_j(b)` satisfy both

\[
P_j(b)\ge a\alpha_j
\]

on every point of the `j`th exact-profile cell where `V(b)-V(d_j)>=mu-epsilon`, and the single joint target bound

\[
\sum_jP_j(b)\le C(X(b)-1)_+.
\]

The lower sieve count and (1) show that the good part of each cell has size at least

\[
[1-E(U)-q]N_j\mathfrak v_{H_j}.
\]

Consequently,

\[
\boxed{
a[1-E(U)-q]\mathcal N_H\le C\sum_{b\in I}(X(b)-1)_+.
}
\tag{9}
\]

All source/target errors in (3)--(8), summed with their corresponding Lipschitz coefficients, are therefore bounded by the same one target budget. At a true optimum they have size `o_{eta,U}(n)` once the other certificate parameters are fixed.

The missing step is not an assumption that there are few heavy states. It is to construct the actual jointly payable cells at sufficiently long quotient lengths, and to control those cells that do not have the required scale gap.
