# An arithmetic obstruction to a root-count Hall error

## Scope

This note does **not** disprove the Erdős 708 asymptotic or the proposed estimate at a genuine global surplus maximizer. It disproves a tempting intermediate shortcut: replacing the inclusion–exclusion loss for a fixed family of carrier banks by an absolute constant times the number of carrier roots. The obstruction uses an actual integer interval, so it respects every exact count of multiples, including all composite intersections.

There is also a lift to a genuine complete source tail, with hot carriers and cold complementary factors. In that lift, however, the weights are not globally optimal and the full adaptive carrier graph has an obvious repair. Thus optimality and adaptive carrier selection cannot be omitted from any remaining general lemma.

## 1. More than a root-count loss for a union of prime banks

Let an integer parameter \(y\to\infty\), put \(N=y^2\), and let

\[
\mathcal P=\{p:p\text{ prime},\ p\le y\},\qquad Q=\prod_{p\le y}p.
\]

For an integer shift \(C\), write

\[
R(C)=\#\{1\le j\le N:\gcd(C+j,Q)=1\}.
\]

Every integer at most \(y^2\) with no prime divisor at most \(y\) is either 1 or a prime exceeding \(y\). Therefore the prime number theorem gives

\[
R(0)=1+\pi(y^2)-\pi(y)
=\left(\frac12+o(1)\right)\frac{N}{\log y}.
\tag{1}
\]

Average \(R(C)\) over the \(Q\) residue classes of \(C\). Each fixed \(j\) is coprime to \(Q\) for exactly \(\varphi(Q)\) classes, so

\[
\frac1Q\sum_{C=0}^{Q-1}R(C)
=N\frac{\varphi(Q)}Q
=\left(e^{-\gamma}+o(1)\right)\frac{N}{\log y}
\tag{2}
\]

by Mertens' product theorem. Select a class attaining at least this average; adding a multiple of \(Q\) makes the shift positive without changing any counts. Since \(e^{-\gamma}>1/2\), (1) and (2) show that some actual interval \(J=\{C+1,\ldots,C+N\}\) satisfies

\[
\begin{aligned}
&\#\{b\le N:\exists p\in\mathcal P,\ p\mid b\}
-\#\{b\in J:\exists p\in\mathcal P,\ p\mid b\}\\
&\hspace{2cm}\ge
\left(e^{-\gamma}-\frac12+o(1)\right)\frac{N}{\log y}.
\end{aligned}
\tag{3}
\]

But the number of roots is

\[
k=|\mathcal P|=\left(1+o(1)\right)\frac y{\log y}.
\]

Consequently the loss divided by \(k\) tends to infinity, at least linearly in \(y\). There is no universal estimate of this union discrepancy by \(O(k)\).

This is not a formal family of inconsistent residue data. For every positive integer \(d\), its bank in \(J\) has either \(\lfloor N/d\rfloor\) or \(\lfloor N/d\rfloor+1\) points. Intersections are exactly the banks of least common multiples.

## 2. Lift to a full tail with hot carriers and cold complements

Fix any \(c>2\). Retain \(N=y^2\), and choose

\[
R=\left\lceil3\log_2\log N\right\rceil,\qquad
k_0=\lfloor cR\rfloor+1,\qquad h=2^{k_0},\qquad M=hN.
\]

Set \(w_2=1/R\) and every other prime weight equal to zero. Then

\[
X(a)=\frac{v_2(a)}R,
\qquad A=\{a\le M:X(a)>c\}=\{h,2h,\ldots,Nh\}.
\]

Thus \(A\) is exactly the complete strict upper tail and \(n=|A|=N\). Notice that \(h=(\log N)^{3c+o(1)}\), so \(M=o(n^2)\).

Take the shift \(C\) furnished above and the actual ambient interval

\[
I=\{hC+1,\ldots,h(C+N)\},\qquad |I|=M.
\]

Let \(S\subseteq A\) consist of \(a=hb\) for which \(b\le N\) has a prime divisor \(p\le y\) and \(v_2(b)\le R\). For each such source choose one such \(p\) and assign the carrier \(d(a)=hp\). Every carrier is hot because

\[
X(hp)\ge X(h)>c>1,
\]

and every assigned complementary factor is cold:

\[
X\bigl(a/d(a)\bigr)=\frac{v_2(b/p)}R\le1.
\]

For each fixed \(B'>0\), all these carrier roots are at most \(B'n\) once \(N\) is sufficiently large, since \(hy=o(N)\).

The sources of \(S\) have cardinality

\[
|S|\ge N-R(0)-\frac{N}{2^{R+1}}.
\tag{4}
\]

The union of their assigned banks is contained in the union of all banks \(hp\), \(p\le y\), in \(I\). The multiples of \(h\) in \(I\) correspond exactly to \(C+1,\ldots,C+N\). Hence

\[
|\Gamma(S)|\le N-R(C).
\tag{5}
\]

Combining (1), (2), (4), and (5), and using \(2^R\ge(\log N)^3\), gives the Hall deficit

\[
|S|-|\Gamma(S)|
\ge\left(e^{-\gamma}-\frac12+o(1)\right)\frac{N}{\log y}.
\tag{6}
\]

This is much larger even than the number of **all** hot integers below \(B'n\). Indeed,

\[
H=\#\{d\le B'n:X(d)>1\}
=\left\lfloor\frac{B'N}{2^{R+1}}\right\rfloor
=O_{B'}\left(\frac{N}{(\log N)^3}\right).
\tag{7}
\]

Thus an \(O(H)\) deficiency estimate for arbitrary fixed cold-complement carrier selections is false, even when the source set is a full tail.

## 3. Exactly which additional hypotheses this does not test

The example fails genuine optimality in two explicit ways relevant to the intended proof.

First, the number of hot target positions is

\[
K=\#\{b\in I:X(b)>1\}
=\frac{M}{2^{R+1}}+O(1)
=N\frac{h}{2^{R+1}}+O(1),
\]

so \(K/n\to\infty\). It violates the \(K=O_c(n)\) consequence of a positive global surplus maximizer.

Second, in the full adaptive graph the common divisor \(h\) is also an admissible hot carrier for every source in \(S\): its complement is \(b\), which is cold by definition. Its bank contains exactly \(N\) positions in \(I\). Accordingly the adaptive graph matches all of \(S\), and the fixed-carrier deficit disappears completely.

The obstruction therefore establishes a precise boundary, not a counterexample to the desired theorem. A successful replacement for the first-group inclusion–exclusion argument must use the ability to reassign carriers, and must use the restrictions from actual optimality. Full-tail membership and cold complements alone do not justify a root-count error.

## Source for the two classical asymptotics

Terence Tao, *Mertens' theorems* (11 December 2013), states both the Mertens product asymptotic and the prime number theorem used in (1)–(2):

<https://terrytao.wordpress.com/2013/12/11/mertens-theorems/>

All remaining calculations above are explicit deductions. The shift is obtained by finite averaging over residue classes; no unproved equidistribution assertion about long prime-free intervals is used.
