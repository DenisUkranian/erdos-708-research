# A uniform first moment on a full additive upper tail

Status: proved below, using standard uniform estimates for rough numbers and the elementary Chebyshev bound for primes. This is an unrestricted prefix statement. It does not compare the prefix with an arbitrary shifted interval and does not by itself prove the Erdős 708 target.

## Theorem

Let \(M\ge 2\), let \(0\le w_p\le1\) for primes \(p\le M\), and put

\[
 X(a)=\sum_{p\le M}w_pv_p(a),\qquad
 \mu=\sum_{p\le M}\frac{w_p}{p-1}.
\]

For any real \(c\ge0\), define the full strict upper tail

\[
 A=\{1\le a\le M:X(a)>c\}.
\]

There is an absolute constant \(K\) such that

\[
 \boxed{\quad
 \sum_{a\in A}X(a)
 \le [c+1+K(1+\mu)]\,|A|.
 \quad}                                                   \tag{1}
\]

Consequently, if \(\mu\le C\), the conditional first moment is bounded solely in terms of \(c,C\). Equivalently,

\[
 \sum_{a\le M}(X(a)-c)_+
 \le [1+K(1+C)]\,|A|.                                    \tag{2}
\]

The assertion includes arbitrary zero-weight primes and arbitrary multiplicities of every prime. No optimality, minimal-obstruction, support-size, or separation hypothesis is used. If \(A\) is empty, both inequalities are immediate.

## 1. The rough-number input

For a prime \(p\), use the inclusive convention

\[
 R(T,p)=\#\{b\le T:P^-(b)\ge p\},\qquad P^-(1)=\infty.
\]

There are positive absolute constants \(a_0,b_0,b_1\) such that

\[
 R(T,p)\ge a_0\frac{T}{\log p}\quad(T\ge p^2),             \tag{3}
\]

\[
 R(t,p)\le b_0\frac{t}{\log p}\quad(t\ge p),               \tag{4}
\]

and

\[
 Q(T):=\#\{(q,j):q\text{ prime},\ j\ge1,\ q^j\le T\}
 \le b_1\frac{T}{\log T}\quad(T\ge2).                     \tag{5}
\]

For clarity, these are uniform finite bounds, not asymptotics with a fixed roughness parameter. One primary reference for (3)--(4) is Kai Fan, *Numerically explicit estimates for the distribution of rough numbers*, Journal of Number Theory 260 (2024), 120--150, DOI [10.1016/j.jnt.2024.01.008](https://doi.org/10.1016/j.jnt.2024.01.008). The author's [published PDF](https://stvfan.github.io/files/papers/Numerically%20explicit%20estimates%20for%20the%20distribution%20of%20rough%20numbers.pdf) uses \(\Phi(x,y)=\#\{b\le x:P^-(b)>y\}\). Its introduction records \(\Phi(x,y)<x/\log y\) for \(x\ge y>1\), and Theorem 2.3 proves \(\Phi(x,y)>0.4x/\log y\) for \(7\le y\le x^{2/3}\). Taking \(y=p-1\) gives (3)--(4) for large primes; the finitely many small primes are handled by counting residue classes. Constants are not optimized here.

For (5), Chebyshev's estimate controls the term \(j=1\). The terms \(j\ge2\) contribute at most \(\sqrt T\log_2T\), which is \(O(T/\log T)\) uniformly for \(T\ge2\).

## 2. A weighted mean over rough integers

For every \(T\ge1\) and every prime \(p\),

\[
 \sum_{\substack{b\le T\\P^-(b)\ge p}}X(b)
 \le K(1+\mu)R(T,p).                                    \tag{6}
\]

If \(T<p^2\), each counted integer is either 1 or a prime. Hence \(X(b)\le1\), proving (6) directly.

Now suppose \(T\ge p^2\). Expanding all prime-power valuation layers gives the exact identity

\[
 \sum_{\substack{b\le T\\P^-(b)\ge p}}X(b)
 =\sum_{\substack{q\ge p\\q\le M}}w_q
   \sum_{\substack{j\ge1\\q^j\le T}}R(T/q^j,p).          \tag{7}
\]

Split the pairs \((q,j)\) according to whether \(T/q^j\ge p\). By (4), the first part is at most

\[
 \frac{b_0T}{\log p}\sum_{q\ge p}w_q\sum_{j\ge1}q^{-j}
 \le \frac{b_0\mu T}{\log p}.                            \tag{8}
\]

In the second part, \(1\le T/q^j<p\), so the only rough integer is 1. Since \(w_q\le1\), this entire part is at most \(Q(T)\). Applying (5), then \(\log T\ge2\log p\), gives

\[
 Q(T)\le\frac{b_1T}{\log T}
       \le\frac{b_1T}{2\log p}.                         \tag{9}
\]

Finally divide (8)+(9) by the lower bound (3). Thus (6) holds with any

\[
 K\ge\max\{1,b_0/a_0,b_1/(2a_0)\}.
\]

All prime-power layers are included in (7); the small-quotient terms in (9) are essential.

## 3. An exact disjoint first-crossing decomposition

For \(a\in A\), list every prime factor of \(a\), including repetitions, in nondecreasing order. Starting from 1, multiply these factors one at a time. Let \(d=d(a)\) be the first partial product at which \(X\) exceeds \(c\), and let \(p=P^+(d)\) be the final prime factor at that crossing. Then

\[
 X(d/p)\le c<X(d)\le c+w_p\le c+1.                       \tag{10}
\]

The remaining quotient \(b=a/d\) has \(P^-(b)\ge p\).

Conversely, if \(d\le M\), \(p=P^+(d)\), and
\(X(d/p)\le c<X(d)\), then every

\[
 a=db\le M,\qquad P^-(b)\ge p,
\]

has first crossing exactly at \(d\). Indeed, all smaller prime factors of \(a\) are already in \(d\), the required initial occurrences of \(p\) are exactly those in \(d\), and all earlier partial products have load at most \(X(d/p)\le c\).

Thus these cells are pairwise disjoint and partition \(A\). In particular,

\[
 |A|=\sum_d R(M/d,P^+(d)).                               \tag{11}
\]

Zero-weight factors cause no problem: they are retained in the ordered factorization. The final crossing prime necessarily has positive weight. Repeated copies of that prime are retained in the rough quotient, which is why the inclusive condition \(P^-(b)\ge p\) is used.

By complete additivity, the contribution from the cell indexed by \(d\) is

\[
 X(d)R(M/d,p)
 +\sum_{\substack{b\le M/d\\P^-(b)\ge p}}X(b).
\]

Using (10) and (6), this is at most

\[
 [c+1+K(1+\mu)]R(M/d,p).
\]

Summing over the disjoint cells and applying (11) proves (1). Subtracting \(c|A|\) proves (2).

## 4. Uniform integrability relative to the full tail

The excess bound (2) is uniform in the level. Put

\[
 L=1+K(1+C),\qquad N(t)=\#\{a\le M:X(a)>t\}.
\]

For every \(t\ge0\),

\[
 2L\,N(t+2L)
 \le\sum_{X(a)>t}(X(a)-t)
 \le L N(t).
\]

Iteration therefore gives

\[
 N(c+2Lk)\le2^{-k}N(c)\qquad(k=0,1,2,\ldots).
\]

Applying (2) again at the higher level yields

\[
 \boxed{\quad
 \sum_{X(a)>c+2Lk}X(a)
 \le(c+2Lk+L)2^{-k}|A|.
 \quad}                                                  \tag{12}
\]

Thus, for any \(\varepsilon>0\), one can discard the sources with \(X(a)>T\), losing at most \(\varepsilon|A|\) of their entire weighted demand, with \(T\) depending only on \(c,C,\varepsilon\). This conclusion has no factor involving \(\log(M/|A|)\). The same geometric-tail estimate also bounds every fixed conditional moment in terms of \(c,C\) and the moment order.

## 5. A direct price-band consequence, and the remaining scope

Let the active primes be partitioned into any \(N\) disjoint bands \(P_1,\ldots,P_N\). Define the source demand of band \(i\) by

\[
 L_i=\sum_{a\in A}\sum_{p\in P_i}w_pv_p(a).
\]

By (1),

\[
 \sum_iL_i\le[c+1+K(1+C)]|A|,
\]

so some band has \(L_i\le[c+1+K(1+C)]|A|/N\). Removing its prices from \(w\) reduces the fixed-source dual objective by at most \(L_i\): the source linear term loses exactly \(L_i\), while the target hinge can only decrease.

This supplies a small selected-source-demand band without an unbounded \(\log(M/|A|)\) factor. It does not prove that the remaining diffuse and substantial-price pieces can be combined against a single target capacity budget. In particular, (1) is not a shifted-interval hinge comparison, and neither (1) nor the band consequence proves \(J_c\le C_c\).
