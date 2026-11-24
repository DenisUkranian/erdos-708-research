# Geometric price grids and a small number of regular cofactors

## Scope

This note proves two unrestricted reductions for the surplus problem:

1. a genuine global surplus maximum on a geometric price grid has an
   approximately optimal boxed raw dual on its own full tail, with an
   error proportional to that new tail's size;
2. after a demand-controlled band deletion, the retained source set has
   exact same-price replacement closure, which bounds the number of
   distinct regular prime-deletion cofactors.

Neither assertion allocates the common target capacity among those
cofactors. The estimate J_(2+delta)<=C_delta is not proved.

Throughout, I is an interval of M consecutive positive integers,
X_w(a)=sum_p w_p v_p(a), and

\[
 \Phi_A(w)=\sum_{a\in A}X_w(a)-\sum_{b\in I}(X_w(b)-1)_+.
\]

L_raw(A,I) is the minimum sum of variables z_b in [0,1] covering every
raw prime-valuation demand of A. The entire interval supplies all rows,
so this LP is feasible. Its dual can be clipped to 0<=w_p<=1, with
prices supported on primes at most M.

## 1. Multiplicative downward rounding of an actual optimum

Let v be a continuous boxed raw dual optimum for a fixed source set A,
and let z be a paired primal optimum. If 0<=u<=v, active-row balance
and complementary slackness give the exact identity

\[
 \Phi_A(u)=\sum_{b\in I}z_b\min(X_u(b),1).                \tag{1}
\]

Indeed, sum_A X_u=sum_b z_b X_u because u is supported on the positive
coordinates of v. Whenever X_u(b)>1, also X_v(b)>1 and z_b=1.
Subtracting the hinge gives (1).

Fix 0<t<1. If tv<=u<=v coordinatewise, then every selected target has
X_v(b)>=1, hence X_u(b)>=t. Thus

\[
 \boxed{\Phi_A(u)\ge t L_{\rm raw}(A,I).}               \tag{2}
\]

This estimate does not lose a factor involving the target hinge, the
number of prime rows, or log(M/|A|).

### A finite grid

Fix eta>0 and put r=1+eta, t=1/r. Let

\[
 J_M=\left\lceil\frac{2\log M}{\log r}\right\rceil,
 \qquad
 \mathcal G_M=\{0,1,r^{-1},\ldots,r^{-J_M}\}.
\]

Round each coordinate of v down to its largest available positive grid
value, or to zero when v_p<r^(-J_M). The latter coordinates have
v_p<=M^(-2). Write v_small for their original prices. The rounded u
satisfies

\[
 u\ge t(v-v_{\rm small}).
\]

Using the 1-Lipschitz property of min(x,1) in (1),

\[
 \Phi_A(u)
 \ge t L_{\rm raw}(A,I)-t\sum_bz_bX_{v_{\rm small}}(b)
 =t L_{\rm raw}(A,I)-t\sum_{a\in A}X_{v_{\rm small}}(a).
\]

Since a<=M and Omega(a)<=log_2 M, this proves the convenient bound

\[
 \boxed{\Phi_A(u)\ge tL_{\rm raw}(A,I)-e_M(A),\qquad
 e_M(A)=|A|\frac{\log_2M}{M^2}.}                       \tag{3}
\]

The target raw powers are not truncated; the tiny-coordinate loss is
transferred to the source by the actual optimal row equations.

## 2. A global grid maximum is approximately paired optimal on its own tail

For c>2, maximize

\[
 J_c(w)=\sum_{a\le M}(X_w(a)-c)_+
           -\sum_{b\in I}(X_w(b)-1)_+
\]

over the finite product grid G_M. A maximizer exists. Let w be one,

\[
 A=\{a\le M:X_w(a)>c\},\quad n=|A|,\quad
 F_{\rm grid}=\Phi_A(w)=cn+J_c(w).
\]

For every grid vector u,

\[
 \Phi_A(u)-cn\le J_c(u)\le J_c(w),
\]

so w also maximizes the fixed-source dual objective Phi_A on the grid.
Apply (3) to a continuous optimum for this same A. It follows that

\[
 F_{\rm grid}\ge tL_{\rm raw}(A,I)-e_M(A).             \tag{4}
\]

Assume J_c(w)>0. The elementary mean bound and the full-tail conditional
first-moment theorem in the companion notes give constants C(c), B(c)
such that

\[
 \mu_w\le C(c),\qquad
 \sum_{a\in A}X_w(a)\le B(c)n.
\]

In particular F_grid<=B(c)n. Therefore the actual duality gap obeys

\[
 \boxed{
 0\le L_{\rm raw}(A,I)-F_{\rm grid}
 \le\eta B(c)n+(1+\eta)e_M(A).
 }                                                       \tag{5}
\]

No comparison between n and the cardinality of a previously chosen
continuous full tail is used.

Let z now be an actual continuous primal optimum for this new A, and
write Gap for the left side of (5). Exact LP algebra gives

\[
 \begin{split}
 \mathrm{Gap}={}&
 \sum_p w_p\left(\sum_bz_bv_p(b)-D_p(A)\right)\\
 &+\sum_{X_w(b)>1}(1-z_b)(X_w(b)-1)\\
 &+\sum_{X_w(b)<1}z_b(1-X_w(b)).
 \end{split}                                             \tag{6}
\]

Every term on the right is nonnegative. Thus (5) controls, on the actual
new full tail, the weighted row excess, the unsaturated hot-target
hinge, and the cost of selecting cold targets. It does not assert exact
row balance or saturation of every target with load merely above one.

## 3. Transferring an unrestricted surplus into a grid problem

This section explains the role of changing the source threshold; it
does not assume that full-tail cardinality remains bounded under that
change.

Let w* be an unrestricted global maximum at threshold c and let
A*={X_w*>c}, n*=|A*|. It is a paired continuous raw optimum for A*.
Round w* down as in Section 1. For any c'<tc,

\[
 \begin{split}
 J_{c'}(u)
 &\ge\Phi_{A*}(u)-c'n*\\
 &\ge tJ_c(w*)+(tc-c')n*-e_M(A*).                       \tag{7}
 \end{split}
\]

A global grid maximum at c' is at least this large. Its own full tail
may be much larger than A*. Section 2 supplies its approximation error
relative to its own cardinality, so approximate rows need not be
borrowed from the old instance.

A uniform constant bound for these grid problems at a slightly smaller
threshold would imply a uniform constant bound for the original
problem. By contrast, an estimate with an uncontrolled error proportional
to the new full-tail size cannot simply be charged to n* in (7).

## 4. Demand cleanup preserves exact same-price replacement closure

Use a positive grid maximum w and its full tail A from Section 2.
Delete a union E of entire price levels, obtaining w'. Choose L and
gamma>0, and retain

\[
 G=\{a\in A:X_w(a)\le L,\quad X_{w'}(a)>c-\gamma\}.
\]

The exponential full-tail estimate permits the high-load deletion to
have arbitrarily small weighted demand. Choosing a band with small
source demand controls the other deletion, as proved in the companion
SOURCE_TAIL_AND_DEMAND_BAND_CLEANUP note.

Here the approximate rows from (6) cause only their already quantified
additional gap. For any deleted-price set E,

\[
 \sum_bz_bX_E(b)
 =\sum_{a\in A}X_E(a)
   +\sum_{p\in E}w_p\left(\sum_bz_bv_p(b)-D_p(A)\right)
 \le\sum_{a\in A}X_E(a)+\mathrm{Gap}.                    \tag{8}
\]

For a retained-price row, passing from A to G adds precisely the demand
of A minus G. Hence its total weighted row excess is at most
Gap+sum_(A minus G) X_w. All of these estimates concern the same actual
primal solution z.

Crucially, G is closed under the following replacements. If p divides
a in G and q<=p is a prime at the same retained price level as p, then

\[
 a'=a q/p\le a\le M,
 \qquad X_w(a')=X_w(a),\qquad X_{w'}(a')=X_{w'}(a).
\]

Thus a' also belongs to G. No source margin is lost in such a
replacement: both prices are exactly equal, not merely close.

## 5. A counting lemma for regular deletion cofactors

Fix 0<b<=1 and an integer R>=2. There are at most

\[
 J_b=1+\left\lfloor\frac{\log(1/b)}{\log(1+\eta)}\right\rfloor
\]

nonzero grid levels at least b. At each retained level, call its first
R-1 primes exceptional. The exceptional set has size at most
(R-1)J_b. Every other prime at that level has at least R primes q<=p
at the same price.

Let D be any set of distinct integers d, each witnessed by a source
a in G and a nonexceptional retained prime p with w_p>=b such that
d=a/p. Then

\[
 \boxed{
 |D|\le\frac1{bR}\sum_{a\in G}X_w(a)
      \le\frac{L|G|}{bR}.
 }                                                       \tag{9}
\]

For each d fix one witnessing p. Its R same-price predecessors produce
R distinct integers dq in G by Section 4. An integer a' in G can occur
in these incidences only through a distinct prime divisor q of a' with
w_q>=b; the associated d is uniquely a'/q. Thus the number of incoming
incidences is at most the number of such prime divisors, at most
X_w(a')/b. Summing proves (9).

This argument includes repeated prime powers in the sources and
arbitrary inactive or diffuse cofactor factors. It is a statement about
the actual distinct integers d=a/p, not only about their weighted prime
parts.

For fixed eta,b,L, taking R large makes the number of regular cofactors
an arbitrarily small fraction of |G|. The exceptional prime set remains
finite, with its size explicitly depending on those fixed parameters.
Its prime values may still depend on M; only its cardinality is bounded.

## 6. The unsolved capacity step

The count (9) is not a matching or covering theorem. Many sources can
have the same cofactor d; their valuation demand retains that
multiplicity. Furthermore, the target banks {b in I:d divides b} for
different d can overlap. Selecting a representative target once per
distinct d does not pay the repeated source demands.

In particular, no implication of the form

\[
 \text{Hall deficiency}\le O(|D|)
\]

has been established here for these arithmetic fibres. Such an
implication must not be inserted into (9) without a new proof.

The grid step repairs the genuine-optimality/cardinality difficulty in
price quantization. The cofactor count gives a small set of regular
cofactor types. The common target-capacity allocation across those
types is still required to derive coefficient 2+delta.
