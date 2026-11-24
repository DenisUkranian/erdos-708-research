# Deleting a weight band at an actual optimal dual

## Status

This note proves an exact joint loss inequality and derives a genuine
gap between light and substantial weights. It removes the numerical
circularity caused by applying a condition of the form
\(\eta K\ll\delta\) with \(K=O(1/\eta)\).

It does not prove the remaining gluing estimate. In particular, a bound
on heavy occurrences in each source still does not bound the global
number of heavy primes, and the target hinge cannot be used separately
for every source pattern.

The main loss identity and its summation have been independently
audited by both other research agents.

## 1. Exact optimal setup

Let \(A\subseteq[2,M]\) be a set of \(m\) distinct integers, and let
\(I=\{x+1,\ldots,x+M\}\). The boxed raw covering LP has demand

\[
 D_p(A)=\sum_{a\in A}v_p(a).
\]

Let \(z=(z_b)_{b\in I}\) be an optimal primal solution and let
\(w=(w_p)\), \(0\le w_p\le1\), be a paired optimal dual solution.
Write

\[
 \begin{split}
 X(n)&=\sum_p w_pv_p(n),\\
 H&=\{b\in I:X(b)>1\},\\
 T&=\{b\in I:X(b)=1\},\\
 \Phi_A(v)&=\sum_{a\in A}X_v(a)
       -\sum_{b\in I}(X_v(b)-1)_+,\\
 F&=\Phi_A(w)=\sum_{b\in I}z_b.
 \end{split}
\]

Complementary slackness gives

\[
 z_b=1\ (b\in H),\qquad z_b=0\ (X(b)<1),
\]

\[
 \sum_bz_bv_p(b)=D_p(A)\quad\text{whenever }w_p>0,
\]

and therefore

\[
 F=|H|+\sum_{b\in T}z_b.                                  \tag{1}
\]

No bound on the total weighted source load is assumed.

## 2. The joint block-deletion inequality

Let \(B_1,\ldots,B_N\) be pairwise disjoint sets of prime coordinates.
They need not partition the entire support. Let \(w^{(j)}\) be obtained
from \(w\) by setting the coordinates of \(B_j\) to zero, and put

\[
 \Delta_j(n)=\sum_{p\in B_j}w_pv_p(n),\qquad
 \ell_j=F-\Phi_A(w^{(j)}).
\]

**Lemma.** For every \(j\),

\[
 \ell_j=
 \sum_{b\in H}\bigl(\Delta_j(b)-(X(b)-1)\bigr)_+
 +\sum_{b\in T}z_b\Delta_j(b).                             \tag{2}
\]

Consequently

\[
 \boxed{\qquad 0\le\sum_{j=1}^N\ell_j\le F. \qquad}        \tag{3}
\]

In particular, some block can be deleted at a loss at most \(F/N\).

**Proof.** Active-row equality implies

\[
 \sum_{a\in A}\Delta_j(a)=\sum_{b\in I}z_b\Delta_j(b).
\]

Zero-price rows cause no difficulty: their contribution to
\(\Delta_j\) is zero. Substitute this equality into the difference
of the two dual objectives. For a hot target, its contribution is

\[
 \begin{split}
 &\Delta_j(b)
 -\bigl[(X(b)-1)-(X(b)-\Delta_j(b)-1)_+\bigr]\\
 &\qquad=\bigl(\Delta_j(b)-(X(b)-1)\bigr)_+.
 \end{split}
\]

At a threshold-one target both hinges vanish after the decrease,
leaving \(z_b\Delta_j(b)\). At a cold target \(z_b=0\), and lowering
weights cannot make it hot. This proves (2), including nonnegativity.

For a fixed hot target, put \(t=X(b)-1>0\). Disjointness gives
\(\sum_j\Delta_j(b)\le X(b)\). The elementary inequality
\(\sum_j(y_j-t)_+\le(\sum_jy_j-t)_+\), for \(y_j\ge0,t\ge0\),
therefore yields

\[
 \sum_j(\Delta_j(b)-(X(b)-1))_+\le1.
\]

At a threshold-one target,
\(\sum_jz_b\Delta_j(b)\le z_bX(b)=z_b\).
Summation over targets and (1) prove (3). \(\square\)

The target hinge has been counted once in (3). There is no factor
depending on the number of sources, prime coordinates, or heavy
patterns.

## 3. Selecting an actual gap in the weights

Fix \(R>1\) and a positive integer \(N\). Use the disjoint bands

\[
 B_j=\{p:R^{-j-1}<w_p\le R^{-j}\},
 \qquad j=0,\ldots,N-1.
\]

Choose a band supplied by (3), and write

\[
 b=R^{-j},\qquad a=R^{-j-1}=b/R,\qquad w'=w^{(j)}.
\]

Then

\[
 \Phi_A(w')\ge F-F/N,                                    \tag{4}
\]

and every remaining nonzero weight is either at most \(a\) or
strictly greater than \(b\). Thus (4) creates a genuine weight gap
of ratio \(R\); it does not assume one in the original source class.

There are only \(N\) possible values of \(b\), all fixed once \(R,N\)
are fixed. Asymptotic statements established uniformly for each fixed
substantial threshold can therefore be applied to the selected
threshold. Equivalently, take the union of the finitely many exceptional
source sets first; their total weighted cost remains \(o(m)\).

In the sparse actual-obstruction reduction, the currently proved
occurrence bound at threshold \(b\) is

\[
 K(b)\le4(\lfloor1/b\rfloor+1).
\]

The smaller threshold \(a=b/R\) therefore satisfies

\[
 aK(b)\le\frac{4(1+b)}R\le\frac8R.                       \tag{5}
\]

Also \(a(K(b)+1)\le9/R\). Any improved occurrence constant only
strengthens these estimates. Thus a conditional diffuse requirement
of the form \(a\le c_\delta/(K+1)\) can be met by choosing
\(R\ge9/c_\delta\), independently of the selected band and of \(N\).
This is the precise removal of the previous numerical circularity.

For each fixed choice of \(R,N\), the selected heavy threshold is
positive and fixed. Its primes tend to infinity in the sparse
obstruction regime by the already established cold-prefix bound.

### Arbitrarily strong prescribed gaps

Geometric bands are not essential. Fix a finite \(N\), start with
\(b_0=1\), and recursively choose positive numbers
\[
 1=b_0>b_1>\cdots>b_N>0.
\]
At stage \(j\), the heavy-occurrence bound
\(K_j=4(\lfloor1/b_j\rfloor+1)\) is already fixed. The next threshold
\(b_{j+1}\) may therefore be chosen to satisfy any specified positive
upper bound depending on \(b_j,K_j\) and fixed accuracy parameters.
For example, one may require
\[
 b_{j+1}\le
 \min\left\{\frac{b_j}{2},
 \frac{\varepsilon}{K_j+1},
 \exp[-C K_j\log(K_j+2)]\right\}.
 \]
Apply (3) to \(B_j=\{p:b_{j+1}<w_p\le b_j\}\).
Some such band still costs at most \(F/N\) to delete. For that band the
light maximum is at most \(b_{j+1}\), the remaining heavy weights exceed
\(b_j\), and the intended gap constraints hold with its own \(K_j\).

This recursive choice is noncircular: \(K_j\) depends on the already
chosen upper threshold, not on the next lower threshold. All thresholds
remain fixed positive constants in a finite construction. It does not,
however, address a later multiplicative amplification of the
objective-loss budget; the caution in Section 6 still applies.

## 4. Source normalization after the deletion

Now assume that \(A\) is a fixed-ambient inclusion-minimal raw failure
at budget \(c>2\):

\[
 F=cm+e,\quad e>0,\qquad
 L_{\rm raw}(S,I)\le c|S|\quad(S\subsetneq A).
\]

For every nonnegative test vector \(v\), proper-subset minimality
implies the exact global shortfall inequality

\[
 \sum_{a\in A}(c-X_v(a))_+
 \le (cm-\Phi_A(v))_+.                                  \tag{6}
\]

To verify it, take \(S=\{a:X_v(a)>c\}\). If \(S=A\), the
left side is zero. Otherwise weak duality on that proper subset
gives \(\Phi_S(v)\le c|S|\); subtracting its objective from
\(\Phi_A(v)\) yields (6). The same target hinge is used throughout.

Apply (6) to \(w'\). If the chosen deletion has loss \(\ell\le F/N\),
then

\[
 \sum_{a\in A}(c-X_{w'}(a))_+
 \le(\ell-e)_+\le\ell.                                  \tag{7}
\]

Fix \(0<\gamma<c\), and let
\(B_{\rm low}=\{a:X_{w'}(a)\le c-\gamma\}\).
Writing \(W_{\rm low}=\sum_{a\in B_{\rm low}}X_{w'}(a)\), we obtain

\[
 |B_{\rm low}|\le\ell/\gamma,\qquad
 W_{\rm low}\le(c-\gamma)\ell/\gamma.                    \tag{8}
\]

Let \(B_{\rm occ}\) be the exceptional set from the substantial-
occurrence reduction at the selected threshold. Its original weighted
cost is \(o(m)\), and its cost under \(w'\le w\) is no greater.
Set

\[
 G=A\setminus(B_{\rm low}\cup B_{\rm occ}),\qquad g=|G|.
\]

Then every retained source has load greater than \(c-\gamma\),
it has at most \(K(b)\) retained heavy occurrences, and

\[
 g\ge m-\frac{F}{N\gamma}-o(m).                           \tag{9}
\]

There is a useful sharper comparison with the retained cardinality:

\[
 \Phi_G(w')\ge cg-\ell-o(m)
             \ge cg-F/N-o(m).                           \tag{10}
\]

Indeed, removing the low-load sources changes
\(\Phi_A(w')-cm\) by adding their nonnegative shortfalls
\(c-X_{w'}(a)\). Removing the additional occurrence-exception sources
costs only \(o(m)\) in weighted demand.

Since \(F=cm+O(\log M)=cm+o(m)\), fixed \(N\) can make the
loss in (10) as small a fixed fraction of \(m\) as desired.
The weighted removal cost in (8) is
\(O_c(m/(N\gamma))\), and must be charged only once.

## 5. What survives in the target and demand constraints

The new vector \(w'\) is not asserted to be optimal. Nevertheless,

\[
 H'=\{b:X_{w'}(b)>1\}\subseteq H,
\]

so the original optimal primal \(z\) still selects every member of
\(H'\) fully. Every active coordinate of \(w'\) was active for \(w\),
and its original demand row remains exactly tight in \(z\).

Consequently, for any union \(U'\) of \(w'\)-hot divisor banks,

\[
 V_p(U')\le D_p(A)\quad(w'_p>0).
\]

Relative to the retained demands,

\[
 \sum_p w'_p\bigl(V_p(U')-D_p(G)\bigr)_+
 \le W_{\rm low}+o(m)
 \le \frac{(c-\gamma)F}{N\gamma}+o(m).                   \tag{11}
\]

Equations (9)--(11) give the exact normalization costs. They do not
silently restore source minimality or optimality at the new vector.

## 6. Remaining logical limitation

The argument has produced a weight gap satisfying (5), with a
controlled joint loss in the dual objective. It has not justified
summing a separate conditional-diffuse inequality over all heavy
source patterns. Those patterns can share the same target positions,
and there may be unboundedly many heavy coordinates globally.

There is also a quantitative caution. If a proposed subsequent gluing
lemma multiplies the row-excess error in (11) by a constant that grows
with \(K(b)\), its cost must be checked explicitly. Increasing \(N\)
also changes the possible heavy threshold and hence \(K(b)\); one
cannot assume that a larger \(N\) automatically defeats every such
constant. A direct joint argument that charges the objective loss
once, or a uniform treatment of the remaining errors, is still needed.

Thus the band-deletion lemma supplies a valid global reduction and
removes one specific circularity. It does not by itself prove
J_weak or the unrestricted asymptotic covering bound.
