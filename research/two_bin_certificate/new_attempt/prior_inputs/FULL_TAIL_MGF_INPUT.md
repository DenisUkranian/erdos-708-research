# Uniform source-tail truncation and demand-band cleanup

Independent internal mathematical audit: PASS for Sections 0--3,
including the prime-power mean bound, exponential integrability, and
the cleanup quantifiers.

## Scope

This note derives consequences of the independently audited theorem in
the companion audit/FULL_TAIL_CONDITIONAL_FIRST_MOMENT.md note. It does
not prove the unrestricted surplus estimate.

The useful new point is the order of quantifiers: the bound on retained
source loads and the normalization error can be fixed independently of
the eventual significant-price cutoff. Consequently a later bound on
the number of significant occurrences per retained source need not be
used as a multiplier in this normalization step.

## 0. Positive surplus bounds the reciprocal weighted mean

For every fixed \(c>2\), there is a constant \(C(c)\) such that
\(J_c(w)>0\) implies

\[
 \mu=\sum_{p\le M}\frac{w_p}{p-1}\le C(c).              \tag{0.1}
\]

No optimality is needed for this assertion. Here is an elementary proof.
Let \(\mathbb E_M\) denote averaging over \(1,\ldots,M\). Prime-power
expansion gives

\[
 \mathbb E_M X=\mu-e,\qquad
 0\le e\le \frac{Q(M)}M+\frac4{\sqrt M}
             =O(1/\log M),                            \tag{0.2}
\]

where \(Q(M)\) counts pairs \((p,j)\) with \(p^j\le M\).
The floor errors contribute at most \(Q(M)/M\). For the remaining
geometric tails, primes \(p\le\sqrt M\) contribute at most \(2/M\)
each, and primes \(p>\sqrt M\) contribute at most
\(\sum_{k>\sqrt M}1/[k(k-1)]\le2/\sqrt M\).

The same nonnegative divisor expansion yields

\[
 \begin{split}
 \mathbb E_M X^2
 &\le \sum_p w_p^2\sum_{j\ge1}(2j-1)p^{-j}
      +2\sum_{p<q}\frac{w_pw_q}{(p-1)(q-1)}\\
 &=\mu^2+\sum_p w_p^2\frac{p}{(p-1)^2}
 \le\mu^2+2\mu.
 \end{split}                                          \tag{0.3}
\]

Consequently
\(\mathbb E_M(X-\mu)^2\le2\mu(1+e)\).

For \(A=\{a\le M:X(a)>c\}\), \(n=|A|\), positive surplus implies
\(cn<\Phi_A(w)\le M\). To see the second inequality directly, the full
interval has at least the prefix count at every prime-power level, so

\[
 \Phi_A(w)
 \le\sum_{b\in I}X(b)-\sum_{b\in I}(X(b)-1)_+
 =\sum_{b\in I}\min(X(b),1)\le M.
\]

Thus \(n/M<1/c<1/2\). For all sufficiently large \(M\), (0.2) gives
\(e\le1\). If \(\mu\ge\max(2c,33)\), Chebyshev's inequality then gives

\[
 \frac{\#\{a\le M:X(a)\le c\}}M
 \le\frac{4\mu}{(\mu-c)^2}
 \le\frac{16}{\mu}<\frac12,
\]

contradicting \(n/M<1/2\). The finitely many smaller \(M\) have
\(\mu\le\sum_{p\le M_0}1/(p-1)\) for an absolute \(M_0\), proving
(0.1). In particular, the hypothesis \(\mu\le C\) in the next section
is automatic, with \(C=C(c)\), at every positive global surplus maximum.

## 1. Exponential integrability on a full upper tail

Let \(X(a)=\sum_p w_pv_p(a)\), \(0\le w_p\le1\), on \(1\le a\le M\),
and suppose \(\mu=\sum_p w_p/(p-1)\le C\). The audited conditional
first-moment theorem supplies an absolute constant \(K\). Put

\[
 B=1+K(1+C).
\]

For every \(t\ge0\), with

\[
 N(t)=\#\{a\le M:X(a)>t\},\qquad
 S(t)=\sum_{a\le M}(X(a)-t)_+,
\]

that theorem gives

\[
 S(t)\le B N(t).                                      \tag{1}
\]

Fix \(c\ge0\), \(A=\{a:X(a)>c\}\), and \(n=|A|\). The finite sum \(S\)
is absolutely continuous, and \(S'(t)=-N(t)\) almost everywhere.
Therefore

\[
 S'(t)\le-S(t)/B
\]

almost everywhere, and

\[
 \boxed{S(c+u)\le Bn\,e^{-u/B}\qquad(u\ge0).}           \tag{2}
\]

For every integer \(r\ge1\),

\[
 \boxed{\sum_{a\in A}(X(a)-c)^r\le r! B^r n.}          \tag{3}
\]

For \(r=1\), this is (1). For \(r\ge2\), use the exact layer-cake
identity

\[
 \sum_{a\in A}(X(a)-c)^r
 =r(r-1)\int_0^\infty u^{r-2}S(c+u)\,du
\]

and (2). Summing the nonnegative Taylor series then gives

\[
 \boxed{
 \sum_{a\in A}e^{\lambda(X(a)-c)}
 \le \frac{n}{1-\lambda B}
 \qquad(0\le\lambda<1/B).
 }                                                     \tag{4}
\]

The constants are independent of \(M\), the support, the number of
zero-price factors, and the source density \(n/M\).

For an explicit weighted-tail consequence, if \(u\ge B\), then

\[
 N(c+u)\le S(c+u-B)/B\le n e^{1-u/B}.
\]

Applying (1) at \(c+u\) yields

\[
 \boxed{
 \sum_{\substack{a\le M\\X(a)>c+u}}X(a)
 \le (c+u+B)n e^{1-u/B}\qquad(u\ge B).
 }                                                     \tag{5}
\]

Thus for every \(\varepsilon>0\) one may choose
\(L=L(c,C,\varepsilon)\ge c+B\), before making any price-band choices, such that

\[
 \sum_{\substack{a\in A\\X(a)>L}}X(a)\le\varepsilon n.  \tag{6}
\]

## 2. A cleanup lemma for a genuinely paired full-tail optimum

Assume now that \(w\) is paired with a boxed primal optimum \(z\) for
this same full-tail source set \(A\). In particular,

\[
 \sum_{b\in I}z_bv_p(b)=D_p(A)
 \quad\text{whenever }w_p>0,
\]

and \(z_b=1\) at every old hot target \(X_w(b)>1\).

Fix \(\gamma>0\) and \(\varepsilon>0\), and choose \(L\) as in (6).
Let \(E\) be any set of active coordinates with weighted source demand

\[
 D_E=\sum_{a\in A}\Delta_E(a),\qquad
 \Delta_E(a)=\sum_{p\in E}w_pv_p(a),
\]

satisfying

\[
 D_E\le \frac{\varepsilon\gamma}{L}\,n.                \tag{7}
\]

Delete these prices, setting \(w'_p=0\) on \(E\) and \(w'_p=w_p\)
otherwise. Retain

\[
 G=\{a\in A:X_w(a)\le L,\quad X_{w'}(a)>c-\gamma\}.
\]

Then

\[
 \boxed{\sum_{a\in A\setminus G}X_w(a)\le2\varepsilon n.}
                                                               \tag{8}
\]

Indeed, the sources with \(X_w(a)>L\) cost at most \(\varepsilon n\)
by (6). Every other discarded source satisfies
\(\Delta_E(a)>\gamma\), since \(X_w(a)>c\) but
\(X_{w'}(a)\le c-\gamma\). There are at most \(D_E/\gamma\) such
sources, each of original load at most \(L\). Their weighted cost is
at most \(LD_E/\gamma\le\varepsilon n\).

The same original paired optimum provides exact target control:

\[
 \boxed{\sum_{b\in I}z_b\Delta_E(b)=D_E.}               \tag{9}
\]

Every new hot target remains saturated, because
\(X_{w'}(b)>1\) implies \(X_w(b)>1\). For each retained active prime,
the original row balance becomes

\[
 \sum_{b\in I}z_bv_p(b)-D_p(G)=D_p(A\setminus G)\ge0.
\]

The total weighted row excess is therefore

\[
 \boxed{
 \sum_p w'_p
 \left(\sum_{b\in I}z_bv_p(b)-D_p(G)\right)
 =\sum_{a\in A\setminus G}X_{w'}(a)
 \le2\varepsilon n.
 }                                                     \tag{10}
\]

No row equation is borrowed from a different source set or an
unrelated optimum. Equation (10) states the precise remaining error
after the source set is reduced.

If \(F=\Phi_A(w)\), monotonicity of the target hinge also gives

\[
 \Phi_G(w')\ge F-D_E-2\varepsilon n.                   \tag{11}
\]

## 3. Choosing the band and preserving the quantifier order

The conditional first moment gives

\[
 \sum_{a\in A}X_w(a)\le(c+B)n.
\]

Partition the active coordinates into \(N\) disjoint bands. Some band
has

\[
 D_E\le(c+B)n/N.
\]

Thus (7) follows whenever

\[
 N\ge\frac{(c+B)L}{\varepsilon\gamma}.                  \tag{12}
\]

The choices can be made in the following order:

1. Fix \(c,C,\varepsilon,\gamma\).
2. Choose \(L=L(c,C,\varepsilon)\) using (5).
3. Choose \(N\) using (12).
4. Choose the \(N\) disjoint price bands, including recursively chosen
   gaps if a later argument requires them.

If, after deleting the chosen gap, every substantial retained price is
larger than \(b>0\), then every retained source has at most \(L/b\)
substantial prime occurrences. The error bounds (8)--(11) were already
fixed before \(b\) or this occurrence bound was introduced.

This removes a normalization loss caused by estimating the load of a
discarded source using a later cutoff-dependent occurrence bound.
It does not assert that a subsequent kernel estimate has constants
independent of \(b\). In particular, a later unproved bound with a
multiplier depending on \(L/b\) cannot automatically absorb (10).

## 4. What is not supplied

Equations (4)--(6) concern sources in the complete prefix tail.
Raw prime-row balance transfers their first weighted moment to
selected targets, but does not transfer exponential moments. A small
number of high-load targets can still carry a substantial share of
the weighted demand.

The lemma therefore provides a bounded-source-load, gapped-price
normalization with a controlled common row error. It supplies no
allocation of the capacities \((X_{w'}(b)-1)_+\) among the different
heavy-prime patterns. That joint allocation remains necessary for
the unrestricted surplus estimate.
