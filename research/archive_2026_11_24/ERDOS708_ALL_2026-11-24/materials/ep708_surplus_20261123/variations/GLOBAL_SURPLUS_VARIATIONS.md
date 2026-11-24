# Global surplus maxima: deletion stability and integrated price variations

## Status

All statements proved below hold on the full source class at an actual
global maximum of

\[
 J_c(w)=\sum_{a=2}^M(X_w(a)-c)_+
             -\sum_{b\in I}(X_w(b)-1)_+,
 \qquad c>2.
\]

They include a simultaneous full-tail/paired-optimal normalization,
deletion-cover constraints without a separate additive surplus error,
and a family of bounded test-function inequalities obtained by
integrating both directions of scalar price variation.

They do **not** bound the maximum by a constant depending only on c,
and do not establish the requested unrestricted asymptotic.

Throughout, I is a positive interval of M consecutive integers, weights
are supported on primes at most M, and X_w(n)=sum_p w_p v_p(n) uses the
full raw target valuations.

## 1. The cube maximum is a maximum over all nonnegative weights

If one coordinate v_p exceeds one, replace it by one, keeping all
others fixed. At every p-bearing target the reduced load is at least
one, so the target hinge decreases by exactly

\[
 (v_p-1)\sum_{b\in I}v_p(b).
\]

The source hinge decreases by at most

\[
 (v_p-1)\sum_{a\le M}v_p(a).
\]

The second sum is no larger than the first: every interval prime-power
count is at least its prefix count. Thus coordinate clipping cannot
decrease J_c. Primes greater than M can be deleted, since they have
no source contribution.

Consequently the maximum over 0<=w_p<=1 is also the maximum over all
nonnegative finite weight vectors. In particular both small positive
and negative variations of an active coordinate, and scalar increases
t w with t>1, are legitimate comparisons with the same global maximum.

## 2. Full tail and paired optimum on the same set

Choose a global maximizer w and put

\[
 J_*=J_c(w),\qquad
 A=\{a\in[2,M]:X_w(a)>c\},\qquad n=|A|.
\]

Then

\[
 F:=L_{\rm raw}(A,I)=\Phi_A(w)=cn+J_*.                  \tag{1}
\]

Indeed, for every source set B and every weight vector v,

\[
 \Phi_B(v)-c|B|\le J_c(v)\le J_*.
\]

Taking the dual maximum over v gives
L_raw(B,I)<=c|B|+J_*. For B=A the value at w attains equality,
proving (1). Thus a paired primal optimum z exists with

\[
 \begin{split}
 &z_b=1 &&\text{if }X_w(b)>1,\\
 &z_b=0 &&\text{if }X_w(b)<1,\\
 &\sum_{b\in I}z_bv_p(b)=D_p(A)&&\text{if }w_p>0.
 \end{split}                                             \tag{2}
\]

These are equations for this actual full-tail source set, not equations
borrowed from another example or another top-source choice.

## 3. All deletion subsets have a linear cost reduction

For every S subset A,

\[
 \boxed{\quad L_{\rm raw}(A\setminus S,I)
                    \le F-c|S|.\quad}                   \tag{3}
\]

This follows directly from the global source-set inequality above and
F=cn+J_*. In particular an optimal cover y of A without a has cost

\[
 C_a\le F-c.                                            \tag{4}
\]

No additional J_* term remains in (3) or (4).

Assume J_*>0, and put K=F-c+1. Let

\[
 U_a=\bigcup_{q\mid a,\ q\ \text{prime}}
             \{b\in I:a/q\mid b\}.
\]

Every deletion cover satisfying (4) obeys

\[
 \sum_{b\in U_a}(1-y_b)<1.                              \tag{5}
\]

To prove this, otherwise purchase residual mass one in U_a. At each
purchased target choose a witnessing deleted prime q. The added
valuation vector supplies v(a) except for a nonnegative missing vector
of total prime-unit mass at most one. Every remaining positive deficit
can be repaired at cost no more than that deficit: a target supplying
any positive integer valuation has cost per valuation at most one,
and the complete interval has sufficient total supply. Sequential
repairs cannot create new deficits. This would cover A at cost at most

\[
 F-c+2<F,
\]

contradicting its optimum.

The bank a/q has at least q positions. Hence (5) implies

\[
 q<K=F-c+1                                             \tag{6}
\]

for every prime factor q of every source, including zero-weight primes.
This is a price bound in terms of the actual objective F. Any already
available universal linear bound F<=C_0 n converts it to q<C_0 n and
therefore to o(n) prime-row rounding cost.

There is also an exact deletion gap identity. With the same full dual w,

\[
 \begin{split}
 C_a-F+X_w(a)={}&
 \sum_p w_p\left[\sum_b y_bv_p(b)-D_p(A)+v_p(a)\right]\\
 &+\sum_{X_w(b)>1}(1-y_b)(X_w(b)-1)\\
 &+\sum_{X_w(b)<1}y_b(1-X_w(b)).
 \end{split}                                             \tag{7}
\]

Every term on the right is nonnegative, and the total is at most
X_w(a)-c by (4). Writing w_max(a)=max_{q|a}w_q, every target in U_a
has load at least X_w(a)-w_max(a), so

\[
 \sum_{b\in U_a}(1-y_b)
 \le\frac{X_w(a)-c}{X_w(a)-1-w_{\max}(a)}<1.             \tag{8}
\]

The denominator is positive because X_w(a)>c>2 and w_max(a)<=1.
Thus the full-tail maximizer retains the forced-bank structure rather
than losing it when global optimality is imposed.

## 4. Exact full-tail recovery under a coordinatewise decrease

Let 0<=u<=w, and write X_u for the new load. No old non-source can
become a source, since its load can only decrease. Consequently

\[
 J_c(u)=\Phi_A(u)-cn
              +\sum_{a\in A}(c-X_u(a))_+.               \tag{9}
\]

Paired active-row balance gives the usual exact coverage loss

\[
 F-\Phi_A(u)=\sum_{b\in I}z_b(1-X_u(b))_+.               \tag{10}
\]

Combining (9)--(10), the actual surplus loss is

\[
 \boxed{
 J_*-J_c(u)=
 \sum_{b\in I}z_b(1-X_u(b))_+
 -\sum_{a\in A}(c-X_u(a))_+\ge0.
 }                                                        \tag{11}
\]

The second term is the recovery obtained by dropping the sources that
cross below the source threshold. It must be retained when using a
weight deletion or a randomized coordinatewise decrease. Taking
expectations in (11) is valid for any distribution of such decreases;
independence is unnecessary.

## 5. Inverse moments of selected loads

Apply (11) to u=t w, 0<=t<=1. Every source in A has X_w(a)>c, and
every selected target has X_w(b)>=1. Thus for every t in this range,

\[
 \sum_{a\in A}(c-tX_w(a))_+
 \le\sum_{b\in I}z_b(1-tX_w(b))_+.                     \tag{12}
\]

For any s>0, multiply by t^{s-1} and integrate from zero to one.
The exact elementary integral is

\[
 \int_0^1 t^{s-1}(d-tx)_+\,dt
       =\frac{d^{s+1}}{s(s+1)x^s}
       \qquad(x\ge d>0).
\]

It follows that

\[
 \boxed{\quad
 c^{s+1}\sum_{a\in A}X_w(a)^{-s}
       \le\sum_{b:z_b>0}z_bX_w(b)^{-s}
       \qquad(s>0).
 \quad}                                                 \tag{13}
\]

This includes c^2 sum_A 1/X_w(a)<=sum_b z_b/X_w(b) at s=1.
Zero-load targets are omitted from the inverse expression; their
selection weights are zero by (2).

## 6. Positive moments of the complementary loads

Let

\[
 H=\{b:X_w(b)>1\},\quad T=\{b:X_w(b)=1\},\quad
 C=\{b:X_w(b)<1\},\quad U=\sum_{b\in T}(1-z_b).
\]

For t>=1 the original sources remain above c, while old non-sources
may enter the source set. Direct expansion and (2) give

\[
 \begin{split}
 J_c(tw)-J_*={}&-(t-1)U
 +\sum_{a\in[2,M]\setminus A}(tX_w(a)-c)_+\\
 &-\sum_{b\in C}(tX_w(b)-1)_+\le0.
 \end{split}                                             \tag{14}
\]

The comparison remains valid even when t w exceeds one in some
coordinates, by Section 1. Put r=1/t, divide by t, and integrate against
r^{s-1} on 0<r<=1. Old non-source loads are at most c, and cold target
loads are less than one. The same elementary integral yields

\[
 \boxed{\quad
 c^{-s}\sum_{a\notin A}X_w(a)^{s+1}
       \le \sum_{b\in C}X_w(b)^{s+1}+U
       \qquad(s>0).
 \quad}                                                 \tag{15}
\]

Source ties at load c are included in the left side. In particular, no
source-threshold crossing has been omitted from this increase argument.

## 7. A bounded whole-prefix test with no primal weights remaining

For s>0 define

\[
 f_s(t)=
 \begin{cases}
  t^{s+1},&0\le t\le1,\\
  t^{-s},&t\ge1.
 \end{cases}
\]

Then 0<=f_s<=1. Adding (13) and (15), the selected and unselected
parts of the target ties add to their full cardinality. Therefore

\[
 \boxed{\quad
 c\sum_{a=2}^M f_s\!\left(\frac{X_w(a)}c\right)
       \le\sum_{b\in I}f_s(X_w(b))
       \qquad(s>0).
 \quad}                                                 \tag{16}
\]

This is a necessary family of bounded test-function comparisons for a
true global maximum. It involves the entire prefix and target interval,
and no target mass is independently reused by different source patterns.
All paired primal weights have cancelled from (16).

The limit s down to zero yields the familiar necessary capped-load
comparison. Positive s tests concentration around the two thresholds
more sharply. Neither that limiting comparison nor the family (16) has
been shown here to be incompatible with c>2 and large positive surplus.

## 8. The unresolved arithmetic step

The identities and inequalities above are stronger bookkeeping than an
arbitrary top-source family: they hold at the same actual full-tail
optimum, retain every active-row equation, and keep the source recovery
under finite weight changes.

What is still missing is an arithmetic estimate that contradicts these
conditions when J_* exceeds a c-dependent constant. In particular,
integrating scalar price changes supplies (13)--(16), but does not bound
their interval side in the required direction. A coordinatewise deletion
without the recovery term in (11) would again discard relevant source
budget and would not solve that problem.

No bound J_*<=C_c is established in this note.
