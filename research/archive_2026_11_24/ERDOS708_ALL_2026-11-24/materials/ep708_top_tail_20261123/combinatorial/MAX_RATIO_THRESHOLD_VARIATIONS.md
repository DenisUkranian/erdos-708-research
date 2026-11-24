# Exact threshold variations at a maximum-ratio obstruction

## Status

This is a calculation of necessary optimality conditions, not a proof
that the maximum ratio is at most two. In particular, the logarithmic
cap direction has a nonpositive first derivative for a reason already
contained in complementary slackness; it does not provide an additional
contradiction.

Fix an ambient \(M\) and a positive length-\(M\) interval \(I\), and
let

\[
 R=\max_{\varnothing\ne A\subseteq[2,M]}
          \frac{L_{\rm raw}(A,I)}{|A|}.
\]

Assume \(R>2\). This is the unforced fixed-ambient maximum ratio; no
source set is required to contain \(M\) in this definition.

## 1. The exact strict-superlevel normalization

Choose a maximizing source set and an optimal clipped weight vector
\(w\). Write \(X=X_w\). Adding an excluded integer of load greater
than \(R\), or deleting a selected integer of load less than \(R\),
would increase the ratio. Hence all loads greater than \(R\) are
selected, no load less than \(R\) is selected, and loads exactly
\(R\) may be omitted.

Delete all selected threshold-equality sources. This preserves the
dual value divided by the remaining cardinality, and leaves

\[
 A=\{a\in[2,M]:X(a)>R\},\qquad n=|A|,
\]

with \(n>0\). To see the last assertion, if all originally selected
sources had load \(R\), equality of their ratio would require a zero
target hinge. But an interval multiple of any such source has load at
least \(R>1\), a contradiction.

The same weights remain optimal for the new set: its dual value is
\(Rn\), and the definition of \(R\) bounds its primal value by
\(Rn\). Thus a genuine paired optimum \(z\) exists, and

\[
 \sum_{a\le M}(X(a)-R)_+
     =\sum_{b\in I}(X(b)-1)_+.                           \tag{1}
\]

Moreover, for every nonnegative weight vector \(v\),

\[
 \Psi_R(v):=\sum_{a\le M}(X_v(a)-R)_+
                 -\sum_{b\in I}(X_v(b)-1)_+\le0.         \tag{2}
\]

Indeed, if its first hinge is nonzero, choose its strict source
superlevel set and apply the global ratio bound. If it is zero, (2)
is immediate. Equation (1) says \(\Psi_R(w)=0\).

## 2. Both source and target threshold terms

Let

\[
 T_0=\{a\le M:X(a)=R\},\quad
 H=\{b\in I:X(b)>1\},\quad
 T_1=\{b\in I:X(b)=1\}.
\]

Consider a signed direction \(q\) supported on active coordinates
\(\{p:w_p>0\}\), and define \(Q(n)=\sum_pq_pv_p(n)\).
For sufficiently small positive parameter values preserving
nonnegativity of the weights, the exact one-sided derivative is

\[
 \boxed{
 \Psi_R'(w;q)=
 \sum_{a\in T_0}(Q(a))_+
 -\sum_{b\in T_1}
       \bigl[(1-z_b)(Q(b))_++z_b(-Q(b))_+\bigr].
 }                                                        \tag{3}
\]

To prove this, differentiating the two hinges gives

\[
 \sum_{a\in A}Q(a)+\sum_{a\in T_0}(Q(a))_+
 -\sum_{b\in H}Q(b)-\sum_{b\in T_1}(Q(b))_+.
\]

Exact active-row balance replaces the first sum by
\(\sum_bz_bQ(b)\). Hot targets have \(z_b=1\), cold targets have
\(z_b=0\), and the remaining target-tie expression is exactly (3).
By (2), the derivative in (3) is nonpositive.

For completeness, if the source threshold also varies as
\(R+\varepsilon s\), the derivative becomes

\[
 -sn+\sum_{a\in T_0}(Q(a)-s)_+
 -\sum_{b\in T_1}
       \bigl[(1-z_b)(Q(b))_++z_b(-Q(b))_+\bigr].           \tag{4}
\]

This formula keeps all source threshold-crossing contributions. One
cannot drop the \(-sn\) term while varying the ratio, or treat a
decrease of the source threshold as a free improvement at the old ratio.

## 3. Scaling gives exact but insufficient count constraints

In the direction \(q=w\), source ties have \(Q(a)=R\) and target
ties have \(Q(b)=1\). Hence

\[
 R|T_0|\le\sum_{b\in T_1}(1-z_b).                       \tag{5}
\]

In the opposite direction,

\[
 \Psi_R'(w;-w)=-\sum_{b\in T_1}z_b\le0.                 \tag{6}
\]

These are equivalent to the appropriate one-sided count conditions at
the contact point of the two tail-integral functions under scaling.
They do not imply \(R\le2\).

If a direction preserves all target-tie loads and does not increase any
source-tie load, (3) is zero. On a sufficiently short segment without
new crossings, the objective is then exactly constant. Continuing such
an exchange requires an additional argument at the next source or
target threshold; first-order equality alone supplies no gain.

## 4. What happens in the logarithmic cap direction

Fix \(c_0<R\), for example \(c_0=2+\delta\), and let

\[
 u_p=\min\left\{w_p,\frac{c_0\log p}{\log M}\right\},
 \qquad q=u-w\le0.
\]

Then \(Q(a)\le0\) at every source threshold and (3) reduces to

\[
 \Psi_R'(w;u-w)
     =-\sum_{b\in T_1}z_b\bigl(X_w(b)-X_u(b)\bigr)\le0.
                                                               \tag{7}
\]

The sign is automatic. A negative derivative means that the capped
weights cease to attain the original maximum ratio; this is entirely
consistent with optimality of \(w\).

For the full finite cap, the exact coverage identity gives

\[
 E(u)=Rn-\Phi_A(u),\qquad
 S_{c_0}(u)=c_0n-\Phi_A(u),
\]

and therefore

\[
 E(u)-S_{c_0}(u)=(R-c_0)n.                               \tag{8}
\]

Thus the ratio normalization does not independently bound the joint
loss-minus-unused-budget expression. Proving that the left side of (8)
is smaller than its positive right side requires a new arithmetic
inequality. The derivative calculation, source threshold changes, and
active-row equations do not establish such an inequality.

No contradiction for \(R>2\), and no unrestricted asymptotic covering
bound, follows from this calculation alone.
