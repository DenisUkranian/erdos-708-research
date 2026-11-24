# Exact cuts for the hot-divisor flow

## Status

This note formulates a single target-capacity flow and identifies the exact
term obstructing a direct inheritance of proper-subset minimality.
It does not prove the necessary cut inequalities or J_weak.

Let \(A\subseteq[2,M]\) be an actual raw-minimal failing set at budget
\(c>2\), let \(I\) have length \(M\), and let \(w\) be an optimal clipped
dual. Write

\[
 X(n)=\sum_p w_pv_p(n),\qquad
 H=\{b\in I:X(b)>1\},\qquad h_b=X(b)-1\quad(b\in H).
\]

Thus every source has \(X(a)>c\). For \(2<t<c\), its proposed flow
demand is \(d_a=X(a)-t>0\).

## 1. The genuine single-capacity network

Join a source \(a\) to a hot target \(b\) if

\[
 X(\gcd(a,b))>1.                                         \tag{1}
\]

This is equivalent to the existence of a hot divisor \(d\mid a\) with
\(d\mid b\). The edge includes every hot-divisor bank, not only a selected
prime-deletion bank.

Each source has capacity/demand \(d_a\), and each target has capacity
\(h_b\), used once globally. A flow saturating all source demands exists
if and only if every \(S\subseteq A\) satisfies

\[
 D_t(S):=\sum_{a\in S}(X(a)-t)
          -\sum_{b\in N(S)}(X(b)-1)\le0.                 \tag{2}
\]

Here \(N(S)\) is the union of the neighborhoods in (1). This is the exact
capacitated Hall condition. A proof of (2), even only on the actual
minimal class, would give the requested hinge estimate.

For implementation, one may use intermediate nodes for the minimal hot
divisors \(d\le M\): those with \(X(d)>1\) but
\(X(d/p)\le1\) for every prime \(p\mid d\). Every hot common divisor
contains such a minimal hot divisor, so this compression changes no
edge or cut.

## 2. Exact comparison with proper-subset duality

For a nonempty \(S\subseteq A\), let

\[
 P(S)=\{p:w_p>0,\ p\mid a\text{ for some }a\in S\}
\]

and let \(w_P\) denote the restriction of \(w\) to these coordinates.
Write \(X_P=X_{w_P}\). Every source in \(S\) retains its full load.
Moreover,

\[
 N(S)\subseteq H_P:=\{b\in I:X_P(b)>1\}.
\]

Define the two nonnegative quantities

\[
 \begin{split}
 R(S)&=\sum_{b\in H_P\setminus N(S)}(X_P(b)-1),\\
 C(S)&=\sum_{b\in N(S)}(X(b)-X_P(b)).
 \end{split}
\]

The first is target hinge supported on the source prime set but not
accessible through a hot common divisor. The second is the contribution
of other prime coordinates to the accessible targets.

Direct subtraction gives the exact identity

\[
 \boxed{\quad
 D_t(S)=
 \Phi_S(w_P)-t|S|+R(S)-C(S).
 \quad}                                                 \tag{3}
\]

Consequently proper-subset minimality yields only

\[
 D_t(S)\le(c-t)|S|+R(S)-C(S)
 \qquad(S\subsetneq A).                                 \tag{4}
\]

Even at \(t=c\), a positive cut deficit does not by itself yield a
smaller raw failure: the term \(R(S)\) has not been removed or bounded.
Thus a proof that simply restricts the dual coordinates to \(P(S)\)
and asserts that the remaining hinge is supported on \(N(S)\) is
incomplete.

## 3. The inaccessible hinge is a real arithmetic phenomenon

Take \(S=\{30\}\), weights \(w_2=w_3=w_5=1\), and any interval containing
4. Then \(X_P(4)=2>1\), whereas
\[
 X(\gcd(30,4))=X(2)=1.
\]
Thus 4 contributes to \(R(S)\), not to the flow neighborhood.
This example uses additional target powers; no other source is needed.

There is also a mixing mechanism without repeated powers. With
\(S=\{30,1001\}\) and unit weights on their six distinct primes,
the target 14 has load two but shares only one weighted prime with
each source. It again lies outside the hot-divisor neighborhood.

These examples only disprove the proposed disappearance of \(R(S)\).
They are not deficient-cut examples and do not satisfy the full
minimal-counterexample hypotheses.

The original active-row equalities do not permit \(R(S)\) to be
discarded: primes in \(P(S)\) can also carry demands of sources outside
\(S\). Any successful control of (3) must use that joint accounting
explicitly.

## 4. What cut-minimality itself says

If \(S\) is inclusion-minimal with \(D_t(S)>0\), then every proper
subset satisfies its flow cut inequality. In particular, for each
\(a\in S\), let

\[
 N_{\rm priv}(a,S)=N(S)\setminus N(S\setminus\{a\}).
\]

Then
\[
 \begin{split}
 D_t(S)-D_t(S\setminus\{a\})
 &=X(a)-t-\sum_{b\in N_{\rm priv}(a,S)}h_b,\\
 \sum_{b\in N_{\rm priv}(a,S)}h_b
 &\le X(a)-t-D_t(S)<X(a)-t.
 \end{split}                                             \tag{5}
\]

Thus no source has enough private target capacity. Equation (5) does
not identify \(S\) as a raw-minimal failing set: its target functional
is the restricted neighborhood sum, and (3) records the difference
from a raw dual functional.

### Every prime-deletion-bank target must be shared

There is a stronger pointwise consequence of (5). For every \(a\in S\)
and every prime \(q\mid a\),
\[
 \{b\in I:a/q\mid b\}\subseteq N(S\setminus\{a\}).          \tag{6}
\]
Indeed, such a target is adjacent to \(a\) and has
\[
 h_b\ge X(a)-w_q-1
       \ge X(a)-t+(t-2)>d_a.
\]
If it were private to \(a\), its individual capacity would contradict
(5). Thus all positions in every such bank, not only most of their
total capacity, must be shared with other sources of the cut.
This uses \(t>2\) and \(w_q\le1\); it remains valid for a zero-weight
source prime.

### A common hot divisor excludes a cut completely

Suppose a nonempty source set \(S\) has a common divisor \(d_0\) with
\(z=X(d_0)>1\). Then \(S\) satisfies its flow cut inequality strictly
for every \(t>1\).

To prove this, the quotients \(u_a=a/d_0\), \(a\in S\), are distinct
positive integers at most \(N=\lfloor M/d_0\rfloor\). The target
\(d_0\)-bank has \(N'\ge N\) elements, and its quotients form an
interval of \(N'\) consecutive positive integers. Prime-power
multiple counts imply
\[
 \sum_{\substack{b\in I\\d_0\mid b}}X(b/d_0)
 \ge\sum_{n\le N'}X(n)
 \ge\sum_{a\in S}X(u_a).
\]
Every target in this bank is adjacent to every source of \(S\).
Its total capacity exceeds the total requested source mass by at least
\[
 \begin{split}
 N'(z-1)-|S|(z-t)
 &=(N'-|S|)(z-1)+(t-1)|S|\\
 &>0.                                                     \tag{7}
 \end{split}
\]
Here \(N'\ge N\ge|S|\). The argument explicitly retains multiplicities
of active parts arising from different inactive cofactors: the actual
integer quotients \(u_a\), rather than their active parts, are distinct.

In particular, every deficient cut must satisfy
\[
 X\!\left(\gcd_{a\in S}a\right)\le1.                       \tag{8}
\]
Equations (6) and (8) are additional necessary conditions on a deficient
cut. They do not prove that all such cuts are impossible.

### A deficient cut has at least three sources

Every set of at most two positive-demand sources satisfies (2) strictly
for \(t>1\). A singleton has a full interval multiple whose capacity is
at least \(X(a)-1>X(a)-t\).

For two sources \(a_1,a_2\), a hot gcd is handled by (7). Otherwise
\(X(g)\le1\), where \(g=\gcd(a_1,a_2)\). Choose one interval multiple
\(b_i\) of each complete source \(a_i\). If the chosen targets differ,
their combined capacity is at least \(X(a_1)+X(a_2)-2\). If they
coincide, that one target is divisible by the lcm and has capacity at
least
\[
 X(\operatorname{lcm}(a_1,a_2))-1
 =X(a_1)+X(a_2)-X(g)-1
 \ge X(a_1)+X(a_2)-2.
\]
Both bounds exceed \(X(a_1)+X(a_2)-2t\). The chosen targets belong to
the relevant hot-divisor neighborhoods because each source load is
greater than \(t>1\).

The exact spill identity and the private-bank/common-hot-divisor
arguments above were independently audited within the research team.
Their scope is limited to these necessary cut conditions.

## 5. Relation to the prime-conserving flow

The separately proved prime-conserving network has edges
\(a\to p\to b\), with capacities \(w_pv_p(a)\) and \(w_pv_p(b)\).
Its cuts naturally involve
\[
 \sum_{b\in H}\min\{h_b,X_P(b)\}
 \ge \sum_{b\in I}(X_P(b)-1)_+.
 \]
Thus those cuts do inherit proper-subset dual bounds. A path in that
network only requires a shared prime; it need not satisfy (1).

This distinction is essential. The proven prime-conserving normal form
fills the existing hot hinge at source quotas based on the failing
coefficient \(c\). It does not prove that the larger quotas
\(X(a)-t\), \(t<c\), can be filled. Conversely, imposing (1) can remove
the mixing and repeated-power capacity that made its cut proof valid.

## 6. Finite probes and their limited meaning

The adjacent script hot_divisor_flow.py performs exact integral
maximum-closure tests for rational weights, using minimal hot divisors
to represent (1). All target phases are lifted by CRT to a genuine
integer interval. A selected cut is rechecked against the actual gcd
criterion.

Sixty-four cases were tested: \(M=100,250,500,1000\), eight weight
profiles per size, and two interval-phase constructions. No positive
cut deficit was found. The results are in hot_divisor_flow_probes.json.
These finite tests neither establish (2) nor establish optimality or
minimality for the tested weight vectors. No broader scan was used as
a substitute for the missing general proof.

The unresolved arithmetic obligation is precisely a bound on the cuts
in (2), or a joint control of the spill term in (3) strong enough to
produce it. No such bound is proved here.
