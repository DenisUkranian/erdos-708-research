# Linear same-threshold discrepancy in a dense top-tail instance

## Status

This note disproves the proposed intermediate statement

\[
 \sum_{a\le M}(X(a)-1)_+
       -\sum_{b\in I}(X(b)-1)_+=o(M)
\]

uniformly over clipped raw prime weights and shifted intervals of
length \(M\). It also disproves the stronger dense covering guess
\(L_{\rm raw}\le n+o(n)\).

It does **not** contradict the requested \(2n+o(n)\) bound, J_weak,
or any asserted optimal/minimal-obstruction condition. No finite search
is used. The construction uses a finite family of actual CRT shifts
with an exact expectation formula.

## 1. The prime band and the exact prefix formula

Fix constants

\[
 \frac13<\alpha<\beta<\frac12,
\]

and let

\[
 P_M=\{p\text{ prime}:M^\alpha<p\le M^\beta\},\qquad
 X(n)=\sum_{p\in P_M}v_p(n).
\]

All active weights are one. Write

\[
 k=|P_M|,\qquad \mu_j=\sum_{p\in P_M}p^{-j},\qquad
 \theta=\prod_{p\in P_M}(1-1/p).
\]

Because \(3\alpha>1\), every integer \(a\le M\) has
\(X(a)\le2\), counting repeated occurrences. Let

\[
 N_2=\#\{a\le M:X(a)=2\}.
\]

Every such integer has one unique unordered pair of active prime
occurrences. Conversely, any multiple at most \(M\) of such a pair
has exactly two active occurrences. Therefore the exact identity is

\[
 N_2=
 \sum_{\substack{p,q\in P_M\\p<q}}
       \left\lfloor\frac{M}{pq}\right\rfloor
 +\sum_{p\in P_M}\left\lfloor\frac{M}{p^2}\right\rfloor.
                                                               \tag{1}
\]

In particular,

\[
 \sum_{a\le M}(X(a)-1)_+=N_2,
 \qquad
 \left|\frac{N_2}{M}-\frac{\mu_1^2+\mu_2}{2}\right|
 \le\frac{k(k+1)}{2M}.                                  \tag{2}
\]

The floor error tends to zero: the elementary bound
\(k\le M^\beta\) gives \(k^2/M\le M^{2\beta-1}=o(1)\).
Also \(\mu_j=o(1)\) for each fixed \(j\ge2\).

Mertens' prime-product theorem gives

\[
 \theta\longrightarrow\frac\alpha\beta,
 \qquad
 \mu_1\longrightarrow\mu:=\log(\beta/\alpha)>0.
                                                               \tag{3}
\]

The second conclusion follows from the first because
\(\log\theta=-\mu_1+O(\mu_2)\). Thus

\[
 N_2=\left(\frac{\mu^2}{2}+o(1)\right)M.                 \tag{4}
\]

## 2. A finite family of actual raw-valuation intervals

For every \(p\in P_M\), independently choose a residue

\[
 r_p\in\{0,1,\ldots,p^3-1\}
\]

uniformly. By CRT choose the least nonnegative \(x\) satisfying

\[
 x\equiv r_p\pmod{p^4}\qquad(p\in P_M),                 \tag{5}
\]

and put \(I_x=\{x+1,\ldots,x+M\}\). These are ordinary positive
integer intervals, not formal p-adic windows.

Since \(p^3>M\), for every position \(1\le j\le M\),

\[
 1\le r_p+j<2p^3\le p^4.
\]

If \(p^3\mid r_p+j\), then \(r_p+j=p^3\), so its valuation is
exactly three. Congruence (5) consequently gives the exact raw identity

\[
 v_p(x+j)=\min\{v_p(r_p+j),3\}\in\{0,1,2,3\}.           \tag{6}
\]

Here the minimum is redundant, but emphasizes that no unaccounted
higher target powers remain. For each fixed \(j\), uniformity modulo
\(p^3\) gives

\[
 \mathbb P(p^a\mid x+j)=p^{-a}\quad(a=1,2,3),
 \qquad
 \mathbb P(p\nmid x+j)=1-1/p.
\]

Different prime coordinates are independent at that fixed position.
Independence between different positions is neither asserted nor
needed.

Because \(X\) is integer valued,
\((X-1)_+=X-\mathbf1_{X>0}\). The exact finite expectation over the
\(\prod_{p\in P_M}p^3\) residue choices is therefore

\[
 \boxed{\quad
 \mathbb E\sum_{b\in I_x}(X(b)-1)_+
 =M\bigl(\mu_1+\mu_2+\mu_3-1+\theta\bigr).
 \quad}                                                 \tag{7}
\]

At least one actual shift in this finite family has hinge no larger
than (7). Choose one such shift for each \(M\).

## 3. A positive linear discrepancy

Equations (2)--(3) and (7) give

\[
 \sum_{a\le M}(X(a)-1)_+
 -\sum_{b\in I_x}(X(b)-1)_+
 \ge\bigl(\kappa(\mu)+o(1)\bigr)M,                      \tag{8}
\]

where

\[
 \kappa(\mu)=\frac{\mu^2}{2}-\mu+1-e^{-\mu}>0.
                                                               \tag{9}
\]

For example, \(\kappa(0)=0\) and
\(\kappa'(\mu)=\mu-1+e^{-\mu}>0\) for every \(\mu>0\), proving
strict positivity without a numerical test.

A concrete rational choice is

\[
 \alpha=\frac7{20},\qquad\beta=\frac9{20},\qquad
 \mu=\log(9/7).
\]

For reference,

\[
 \frac{\mu^2}{2}\approx0.03157947093,
 \qquad \kappa(\mu)\approx0.002487264872.
\]

Thus the deficit is a fixed positive proportion of \(M\), not
merely a large but sublinear discrepancy.

## 4. Exact top-tail structure with M forced into the source set

Let \(M\) tend to infinity through primes. Then \(M\notin P_M\)
and \(X(M)=0\). Set

\[
 A_M=\{a<M:X(a)=2\}\cup\{M\},\qquad n=N_2+1.
\]

This is a valid set of distinct source integers with maximum exactly
\(M\). Since every prefix load is at most two, it realizes the exact
top-tail expression at these weights:

\[
 Q_n(w)=X(M)+\operatorname{Top}_{n-1}(X(a):2\le a<M)
             -\sum_{b\in I_x}(X(b)-1)_+
        =2N_2-\sum_{b\in I_x}(X(b)-1)_+.
\]

Hence

\[
 Q_n(w)\ge
 \left(1+\frac{2\kappa(\mu)}{\mu^2}+o(1)\right)n.       \tag{10}
\]

For the displayed rational band, the constant is approximately
\(1.07876208179\). By weak duality, the raw covering optimum and the
integer covering number are at least this large. This does not claim
that the chosen weight vector is optimal.

We have \(n/M\to\mu^2/2>0\), while \(2n<M<16n^2\) for all
sufficiently large \(M\). Thus (10) is a dense instance in the exact
ambient range of the requested top-tail estimate.

However \(Q_n(w)\le2N_2<2n\), simply because the target hinge is
nonnegative. The construction therefore supplies **no violation** of
the desired coefficient two. Its purpose is to rule out an invalid
same-threshold or coefficient-one shortcut in the dense branch.

## Source for the asymptotic prime input

The only prime asymptotic used is the prime-product form of Mertens'
theorem. See T. Tao, [Mertens' theorems](https://terrytao.wordpress.com/2013/12/11/mertens-theorems/),
11 December 2013. The CRT construction, finite expectation, prefix
counting, and top-tail consequences above are proved directly here.
