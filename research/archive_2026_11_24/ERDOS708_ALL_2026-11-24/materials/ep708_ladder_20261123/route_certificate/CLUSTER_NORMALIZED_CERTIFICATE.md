# Cluster-normalized hot-root certificates and an all-occurrence closing ladder

Date: 2026-11-23. Status: the identities, norm bounds, small-bank deletion, and joint diffuse transfer below are proved. The terminal joint capture bound is not proved. The construction is unrestricted in prime occurrences and retains every inactive source cofactor.

This strengthens the constant-payment normalization in `NORMALIZED_COFACTOR_CERTIFICATE.md`: each cluster uses its whole hot-bank hinge, including the unit of spare capacity supplied by the hot-root lemma. In particular, the one-prime chain obstruction to the old constant bank payments disappears.

## 1. Genuine optimum and canonical first-crossing clusters

Fix `delta>0`, `c=2+delta`, and a genuine positive global maximizer `X` of `J_c` for the fixed interval `I` and length `M`. Let

\[
A=\{a\le M:X(a)>c\},\quad n=|A|,\quad
H(b)=(X(b)-1)_+,\quad S_2=\sum_{a\in A}(X(a)-2).
\]

The established full-tail bound gives `S_2<=C_delta n`. All row equalities below refer to this original optimum.

In the active part of a source, order all prime occurrences increasingly, with multiplicity. Let `g(a)` be the first partial product whose load exceeds `1+delta/2`. Then

\[
1+\delta/2<X(g(a))\le2+\delta/2<X(a).                       \tag{1}
\]

Thus an active prime occurrence remains after the root. If `q` is the largest active prime dividing `a`, it occurs in the remaining quotient and

\[
P^+(g(a))\le q\le M/g(a).
\tag{2}
\]

In fact **every active prime dividing `a` is at most the bank length `T_a=M/g(a)`**. Sources with different inactive cofactors remain different members of the same cluster when appropriate.

For each occupied root `g`, write

\[
A_g=\{a:g(a)=g\},\quad m_g=|A_g|,\quad
s_g=\sum_{a\in A_g}(X(a)-2),\quad
B_g=\sum_{\substack{b\in I\\g\mid b}}H(b),\quad
\alpha_g=s_g/B_g.
\tag{3}
\]

The denominators are positive by (1).

## 2. Exact hot-root cluster credit

The independently proved hot-root lemma has the following short direct proof. For any hot `g` and `N=floor(M/g)`, raw complete additivity gives

\[
B_g\ge (X(g)-1)N+\sum_{u\le N}X(u)
=\sum_{\substack{a\le M\\g\mid a}}(X(a)-1).                \tag{4}
\]

Indeed, the quotient target interval has length `M/g`. Its count of multiples of each `p^j` is at least `floor(M/(g p^j))`, exactly the count in `[1,N]`. Include all prime-power layers and use their nonnegative prices. The constant term has at least `N` copies.

Every cluster source is a distinct multiple of `g`, so (4) implies

\[
\boxed{\quad B_g\ge s_g+m_g.\quad}                         \tag{5}
\]

This inequality is also valid for fractional source assignments, with each source assigned total mass one: for a fixed root its fractional multiplicity is at most one per actual multiple. Consequently

\[
0<\alpha_g\le \frac{s_g}{s_g+m_g}<1.                      \tag{6}
\]

If all retained source loads are at most a fixed `L`, then

\[
\alpha_g\le\frac{L-2}{L-1}<1.                            \tag{7}
\]

The high-load sources can be removed at any prescribed small weighted cost using the already established full-tail exponential bound. Such a removal is not needed for (5)–(6).

## 3. Exact source mass and a uniform bank norm

Put

\[
F(b)=\sum_{g\mid b}\alpha_g,
\qquad \mathcal N_{\rm cl}=\sum_g\alpha_g M/g.
\]

Then

\[
\boxed{\quad\sum_{b\in I}H(b)F(b)=S_2.\quad}              \tag{8}
\]

Moreover `g` is a proper divisor of every source in its cluster, so `floor(M/g)>=2`. From (1),

\[
B_g\ge (\delta/2)\lfloor M/g\rfloor.
\]

It follows that

\[
\boxed{\quad
\mathcal N_{\rm cl}\le\frac3\delta S_2=O_\delta(n).
\quad}                                                      \tag{9}
\]

These bounds count all actual source copies. No prime-count estimate is substituted for the fibre multiplicity.

## 4. Small banks can be removed at o(n) weighted source cost

Fix `N_0`. If a canonical root has `M/g<=N_0`, (2) makes `g` an `N_0`-smooth integer. There are at most

\[
(1+\log_2M)^{\pi(N_0)}
\]

possible roots. Each cluster contains at most `floor(M/g)<=N_0` distinct sources, and `X(a)<=log_2M`. Thus the entire weighted demand of sources in these clusters is

\[
O_{N_0}\bigl((\log M)^{\pi(N_0)+1}\bigr)=o(n),             \tag{10}
\]

uniformly, using the previously proved gate `M<16n^2` for a positive optimum. By a diagonal choice, the retained minimum bank length may tend to infinity while the weighted deletion remains `o(n)`.

This observation is useful for analytic corrections whose error per bank is `epsilon(T)T`, with `epsilon(T)->0`: (9) then sums them to `o(n)`, including in the sparse regime. It does not justify corrections having unbounded order or uncontrolled least common multiples.

## 5. Hot-gcd mergers, and the correct order of operations

Two source clusters may be merged under `k=gcd(g,h)` whenever

\[
X(k)>1+\delta/4.
\]

Their union is still a set of distinct multiples of `k`, so (5) remains true for the combined source cost and multiplicity. Recompute `B_k` and `alpha_k`. The norm bound survives with `6S_2/delta` in place of `3S_2/delta`.

The merging process terminates, and the resulting roots satisfy

\[
X(\gcd(g,h))\le1+\delta/4\qquad(g\ne h).                  \tag{11}
\]

One safe order is to delete short **initial canonical** banks using (10) before merging. A gcd merger replaces a root by a divisor and therefore only increases its bank length. Thus the lower bound on bank length survives all mergers. In fact the precise self-smooth inequality also survives: if `k|g`, then `P^+(k)<=P^+(g)<=M/g<=M/k`. What may be lost is the canonical first-crossing description of the merged source cell, not this size inequality. Every active prime of every source in a merged cluster also remains at most its new bank length.

The following claims are **not** automatic:

* a merger need not preserve a previously obtained lower bound for the clipped target capture;
* (11) does not imply that all overlapping cluster payments fit one target;
* target row equalities cannot be transferred to a modified or averaged load.

The terminal estimate must apply to the recomputed clusters and their original raw row information.

## 6. Joint diffuse transfer for the cluster normalization

Write `X=W+V`, where every price in `V` is at most `eta`. Keep the original source payments and the coefficients `alpha_g`. Let

\[
\mu_g=\sum_{p\le M/g}\frac{w_p^V}{p-1},\qquad
\nu_g=V(g)+\mu_g,
\qquad
\bar\nu(b)=\frac{\sum_{g\mid b}\alpha_g\nu_g}{F(b)}
\quad(F(b)>0),
\]

and define `H_model=(W+bar nu-1)_+`. The quantity `V(g)` is retained; this is not replacement by one global constant.

For a fixed amplification `Lambda>=1`, use the one target accounting functional

\[
\mathcal Q_\Lambda(K)=
\sum_{b:F(b)>0}\min\{\Lambda F(b),1\}K(b)
+\sum_{b:F(b)=0}H(b).                                    \tag{12}
\]

For the actual hinge, `Q_Lambda(H)<=sum_I H`. Every target enters at most once.

Let `psi_B(eta)` be the proved one-sided diffuse-bank deficit function from the core route. Then

\[
\boxed{\quad
\mathcal Q_\Lambda(H)
\ge\mathcal Q_\Lambda(H_{\rm model})
-\Lambda\psi_B(\eta)\mathcal N_{\rm cl}.
\quad}                                                      \tag{13}
\]

**Proof.** At one target, the positive increase after replacing the hinge is at most

\[
\begin{aligned}
\min\{\Lambda F,1\}(\bar\nu-V(b))_+
&\le\Lambda F(b)(\bar\nu-V(b))_+\\
&\le\Lambda\sum_{g\mid b}\alpha_g(\nu_g-V(b))_+.
\end{aligned}
\]

Use complete additivity `V(b)=V(g)+V(b/g)`, apply the uniform lower-deficit estimate in each entire quotient interval, and sum using (9). This is one joint clipping operation, so no source pattern spends a separate copy of the target capacity. The argument remains valid after hot-gcd mergers, with the larger norm constant stated above.

Therefore

\[
\boxed{\quad
J_{2+\delta}(X)
\le S_2-\delta n-\mathcal Q_\Lambda(H_{\rm model})
+O_\delta(\Lambda\psi_B(\eta)n).
\quad}                                                      \tag{14}
\]

Unlike the old active-prime constant payments, this construction has no one-prime chain congestion. With only one active prime, all sources have the same first-crossing root, `F=alpha<=1` on its bank, and (8) already gives `Q_1(H)>=S_2`.

## 7. The exact remaining arithmetic assertion

A sufficient all-occurrence assertion is:

> For every `delta>0`, there is a fixed `Lambda_delta` such that, on every sufficiently large positive global optimum, one can choose and, where useful, merge the above clusters so that
> \[
> \mathcal Q_{\Lambda_\delta}(H_{\rm model})
> \ge S_2-\tfrac12\delta n,                               \tag{15}
> \]
> uniformly for all sufficiently small diffuse cutoffs `eta`.

Choose `Lambda_delta` first. Then choose `eta` so small that the error in (14), together with explicitly charged source deletions, is below `delta n/4`. Equation (14) contradicts a positive maximum. This would give the uniform raw asymptotic and hence, by the already proved Wang transfer, the desired integer asymptotic. **No proof of (15) is claimed here.**

One must not infer (15) merely from the individual credits (5), the pairwise gcd restriction (11), or exact prime row balances. Multiway intersections and source clusters with repeated cofactors are still part of the same target expression.

## 8. A useful but possibly overstrong second-moment subtarget

For the actual hinge let

\[
\mathcal V=\sum_{b\in I}H(b)F(b)^2.
\]

Since `min(2t,1)>=2t-t^2` for `t>=0`, (8) gives

\[
\mathcal Q_2(H)\ge2S_2-\mathcal V
+\sum_{F=0}H.                                             \tag{16}
\]

The diagonal in `V` has a built-in margin:

\[
\begin{aligned}
\sum_g\alpha_g^2B_g
&=\sum_g\frac{s_g^2}{B_g}\\
&\le S_2-\sum_g\frac{s_gm_g}{s_g+m_g}\\
&\le S_2-\frac{\delta}{1+\delta}n,
\end{aligned}                                               \tag{17}
\]

because `s_g>delta m_g`. The off-diagonal is exactly

\[
2\sum_{g<h}\alpha_g\alpha_h B_{\operatorname{lcm}(g,h)}.   \tag{18}
\]

Thus an appropriate bound for this one *joint weighted lcm energy* would prove a capture inequality without enumerating prime profiles. It is not available from the row equalities alone. A naive untruncated second moment can overcharge one target incident with many roots; any attempt along (18) should retain a truncation or demonstrate why that rare-point overcharge is negligible on the true optimizer. Merely bounding each intersection separately by a floor plus one reintroduces the unresolved accumulation of errors.

## 9. A scale-triangular row identity worth retaining in the stopping-tree attempt

For the initial canonical clusters, and also after the described gcd mergers, every active prime in a source `a` is at most its cluster bank length `T_a`. Therefore, for every real `t`, the original exact row balances imply

\[
\boxed{\quad
\sum_{b\in I}z_b X_{>t}(b)
=\sum_{a\in A:T_a>t}X_{>t}(a).
\quad}                                                      \tag{19}
\]

All prime powers are included inside `v_p`; the cutoff here is on the prime value, not on an exponent layer. Formula (19) follows because sources with `T_a<=t` contain no active prime exceeding `t`.

In particular, high-prime load occurring in a short-root bank must be supplied by source clusters with strictly larger bank scale. Each prime unit may be transported to a source unit of that same prime using the exact row equality, so this cross-scale transport can be chosen without double use. This offers a genuine arithmetic direction for a stopping-tree argument.

The missing step is a summation of these scale transfers with bounded total loss. Raw exponent layers cannot silently be treated as independent balanced rows, and repeatedly charging the same prime supply at every lower scale is invalid. No such complete telescoping estimate is established in this note.


## Balance convention after source deletion

Identity (19) is exact for the full original source set, with every source retaining its assigned bank scale. If short-bank or high-load sources are omitted from a later capture construction, their original row demand must remain as a separate term in (19). Its weighted cost is bounded by the explicitly proved deletion estimate; it is not literally zero. No original exact row balance is asserted for a truncated source set.
