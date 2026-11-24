# Exact top tails, legitimate optimality, and the joint residual

## Status

This note gives exact identities and records the remaining inequality.
It does not prove the uniform \(2n+o(n)\) estimate. In particular, an
optimality equation for one source set is never transferred to another
top set without re-establishing a paired optimum.

Fix \(M\), a positive interval \(I\) of length \(M\), and clipped
weights \(0\le w_p\le1\), supported on primes at most \(M\). Put

\[
 X_w(a)=\sum_p w_pv_p(a),\qquad
 H_I(w)=\sum_{b\in I}(X_w(b)-1)_+.
\]

## 1. Forcing M and selecting the top sources

For \(1\le n\le M-1\), the maximum of \(\Phi_A(w)\) over source
sets \(A\subseteq[2,M]\) of cardinality \(n\) containing \(M\) is
exactly

\[
 Q_n(w)=X_w(M)+\operatorname{Top}_{n-1}
                 (X_w(a):2\le a<M)-H_I(w).               \tag{1}
\]

Let \(U_n(w)\) be the analogous expression without requiring \(M\).
Replacing the least-load selected source by \(M\), if needed, gives

\[
 0\le U_n(w)-Q_n(w)\le\log_2 M.                         \tag{2}
\]

The last bound follows from \(X_w(a)\le\Omega(a)\le\log_2M\).
In the range \(M<16n^2\), this is \(o(n)\) uniformly. Thus forcing
the maximum can be kept exactly as in (1), or removed for an asymptotic
upper bound with the explicitly controlled difference (2).

### When row balance is legitimate

The finite maxima satisfy

\[
 \max_w Q_n(w)=
 \max_{\substack{A\subseteq[2,M],\ |A|=n\\M\in A}}
      L_{\rm raw}(A,I).                                 \tag{3}
\]

Indeed the source-set family is finite, and the optimal raw dual for
each source set may be clipped to the compact weight cube. Maxima can
therefore be interchanged.

If \(w\) maximizes the left side of (3), and \(A\) is any source set
attaining its top sum, then

\[
 \Phi_A(w)=\max_w Q_n(w)=L_{\rm raw}(A,I).
\]

Thus \(w\) is genuinely optimal for this \(A\), and a paired primal
\(z\) supplies the active-row equations

\[
 \sum_{b\in I}z_bv_p(b)=D_p(A)\qquad(w_p>0).             \tag{4}
\]

For a fixed nonoptimal weight vector, selecting its top source set
alone does not justify (4). If another tied top source set is chosen,
its own paired primal may differ; a previously chosen \(z\) is not
automatically feasible for its new demands.

Ties may be resolved by selecting the larger integers. The resulting
source set is upward closed under divisibility in \([2,M]\), including
the forced source \(M\). In particular every selected integer exceeds
\(M/(n+1)\). This source normalization does not supply a sign for the
joint residual below.

## 2. Exact tail-integral representations

Write

\[
 N_0(t)=\#\{a:2\le a<M,\ X_w(a)>t\},\qquad
 N_I(t)=\#\{b\in I:X_w(b)>t\}.
\]

The layer-cake identity gives

\[
 Q_n(w)=X_w(M)
       +\int_0^\infty\min\{n-1,N_0(t)\}\,dt
       -\int_1^\infty N_I(t)\,dt.                       \tag{5}
\]

Equivalently,

\[
 \begin{split}
 Q_n(w)-2n={}&X_w(M)-2
  +\int_2^\infty\min\{n-1,N_0(t)\}\,dt-H_I(w)\\
 &-\int_0^2\bigl(n-1-\min\{n-1,N_0(t)\}\bigr)\,dt.
 \end{split}                                             \tag{6}
\]

The last integral is nonnegative and is subtracted. Dropping it creates
a stronger sufficient estimate, not an equivalent statement. Likewise
replacing the truncated top tail in (6) by the full prefix hinge can
lose a relevant source-selection saving.

## 3. The exact relation to same-threshold discrepancy

For any selected set \(A\), not only a top set, define

\[
 \begin{split}
 H_0(w)&=\sum_{a=2}^M(X_w(a)-1)_+,\\
 \Delta_1(w)&=H_0(w)-H_I(w),\\
 S_A(w)&=\sum_{a\in A}(1-X_w(a))_+
          +\sum_{a\in[2,M]\setminus A}(X_w(a)-1)_+.
 \end{split}
\]

Then \(S_A(w)\ge0\), and exact subtraction gives

\[
 \boxed{\quad\Phi_A(w)=n+\Delta_1(w)-S_A(w).\quad}       \tag{7}
\]

Consequently the desired upper bound is equivalent, for this set and
weight vector, to

\[
 \Delta_1(w)\le n+S_A(w)+o(n).                          \tag{8}
\]

The shorter bound \(\Delta_1(w)\le n+o(n)\) would be sufficient,
but has not been proved on the full jointly optimal top-source class.
The still stronger assertion \(\Delta_1=o(M)\) is false, as shown by
the independently audited construction in
`DENSE_H1_LINEAR_DISCREPANCY.md`.

That construction has \(\Delta_1/n\) bounded below by about 0.078762.
It also has \(\Delta_1\le N_2<n\), because its prefix hinge is
\(N_2=n-1\) and its target hinge is nonnegative. It refutes neither
(8) nor the shorter sufficient bound, nor the desired coefficient two.

## 4. A logarithmic cap must be combined with unused source budget

Now assume \(w,z\) are a genuine paired optimum for \(A\), and write
\(F=\Phi_A(w)\). Fix \(\delta>0\), let

\[
 c_0=2+\delta,\qquad
 u_p=\min\left\{w_p,\frac{c_0\log p}{\log M}\right\}.
\]

Every source satisfies \(X_u(a)\le c_0\). Active-row balance and
hot-target saturation yield the exact loss identity

\[
 E(u):=F-\Phi_A(u)=\sum_{b\in I}z_b(1-X_u(b))_+.
                                                               \tag{9}
\]

The unused source budget is

\[
 \begin{split}
 S(u)&=c_0n-\Phi_A(u)\\
 &=\sum_{a\in A}(c_0-X_u(a))
     +\sum_{b\in I}(X_u(b)-1)_+\ge0.
 \end{split}                                             \tag{10}
\]

Therefore the correct joint quantity is

\[
 \boxed{\quad F-c_0n=E(u)-S(u).\quad}                   \tag{11}
\]

A sufficient remaining estimate, at a prescribed fixed slack, is

\[
 E(u)-S(u)\le\delta n+o_\delta(n).                      \tag{12}
\]

Bounding \(E(u)\) alone by \(\delta n+o(n)\) is stronger than (12)
and may throw away a linear amount of useful source budget. For example,
in the earlier optimal single-prime example with sources all multiples
of a fixed prime, \(E(u)=n-o(n)\), but
\(S(u)=c_0n-o(n)\). Their difference is negative, as it should be.

The active-row equations prove (9)--(11), not an upper bound for their
difference. Indeed, substituting those equations back into the
difference recovers \(F-c_0n\) exactly. A proof of (12) must introduce
an additional arithmetic allocation or estimate; rearranging the same
equalities cannot supply it.

## 5. Remaining gap

The proved bank and state constraints still do not show (8) or (12)
uniformly. Top-load ordering and upward closure do not establish
primewise bank-product dominance: the separate top-tail CRT
counterexample rules out that stronger intermediate claim. Its lack
of paired optimality is explicitly retained.

Actual paired optimality supplies exact active-row conservation,
mandatory selection of every hot target, and the bounded per-target
loss in (9). It does not yet provide a joint way to charge all low capped
targets against (10), or to control the inaccessible/mixing capacity in
a hot-divisor flow cut.

Thus neither the dense branch nor the unrestricted asymptotic bound is
closed by the identities in this note.
