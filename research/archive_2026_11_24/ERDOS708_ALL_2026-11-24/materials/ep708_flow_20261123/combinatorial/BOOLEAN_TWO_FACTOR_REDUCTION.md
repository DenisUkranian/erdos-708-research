# A two-factor Boolean reduction for the sparse branch

## Status

The reduction and the counterexample in Sections 1--3 are proved. The
uniform estimate in Section 4 is an **unproved sufficient statement**.
No proof of that estimate or of J_weak is claimed. The reduction keeps
the source-to-target load gap, which is lost by a condition involving
only one prime deletion.

Let \(I\) be a positive interval of \(M\) consecutive integers and let
\(H\subsetneq I\), with \(|H|=h\). Define

\[
 \begin{split}
 D(H)&=\{d\in[1,M]:\{b\in I:d\mid b\}\subseteq H\},\\
 C(H)&=([1,M]\setminus D(H))\cup\{p\le M:p\text{ is prime}\},\\
 R(H)&=\{a\in[1,M]:a\ne uv\text{ for all }u,v\in C(H)\}.
 \end{split}                                                   \tag{1}
\]

Products in the last definition are ordinary products of positive
integers. They need not be coprime, and the two factors may be equal.
Only products at most \(M\) matter.

## 1. Exact properties of the Boolean sets

The set \(D(H)\) is upward closed for divisibility inside \([1,M]\):
if \(d\mid e\le M\), every interval multiple of \(e\) is an interval
multiple of \(d\). Its complement is therefore divisor closed. Since
\(H\ne I\), the integer one lies in this complement. Adding all primes
preserves divisor closure, so \(C(H)\) is divisor closed and contains
one and every prime at most \(M\).

Every integer

\[
 d\le\frac{M}{h+1}
\]

lies in \(C(H)\). Its bank has at least
\(\lfloor M/d\rfloor\ge h+1\) positions and cannot be contained in
\(H\).

The sets are monotone under enlarging the target set:

\[
 H\subseteq H'\quad\Longrightarrow\quad
 D(H)\subseteq D(H'),\quad C(H')\subseteq C(H),\quad
 R(H)\subseteq R(H').                                  \tag{2}
\]

## 2. Why actual heavy sources lie in R(H)

Let

\[
 X(n)=\sum_p w_pv_p(n),\qquad 0\le w_p\le1,
\]

with finite prime support, and suppose \(H\) contains every target
\(b\in I\) with \(X(b)>1\). Then

\[
 X(d)\le1\qquad(d\in C(H)).                            \tag{3}
\]

For a prime this is the weight bound. For a nonprime
\(d\notin D(H)\), there is a multiple \(b\in I\setminus H\), and
nonnegativity gives \(X(d)\le X(b)\le1\).

Consequently complete additivity gives

\[
 \boxed{\quad
 X(a)>2\quad\Longrightarrow\quad a\in R(H).
 \quad}                                                 \tag{4}
\]

This handles repeated prime factors and inactive prime cofactors
without alteration. It also remains valid if \(H\) is enlarged by
adding some targets of load at most one.

Adding primes to \(C(H)\) is essential. Without that step, taking
\(I=[1,M]\) and \(H\) to be the multiples of a growing prime \(p\)
would make the complement of \(C(H)C(H)\) all multiples of \(p\),
of cardinality comparable to \(h\). Such a prime is nevertheless cold
for every clipped raw weight vector, and must be allowed as a factor.

## 3. Why the single-deletion condition is too weak

For comparison define

\[
 B(H)=\{a\in[2,M]:a/p\in D(H)\text{ for every prime }p\mid a\}.
                                                               \tag{5}
\]

Actual sources of load greater than two satisfy (5), since
\(X(a/p)=X(a)-w_p>1\). However, a bound \(|B(H)|=o(h)\) is false
even when \(h=o(M)\) and \(M=h^2\).

For an integer \(r\ge2\), take

\[
 M=2^{2r},\qquad I=[1,M],\qquad
 H=\{b\le M:2^r\mid b\},\qquad h=2^r.
\]

Here

\[
 D(H)=\{d\le M:2^r\mid d\}.
\]

Indeed, membership in \(H\) is necessary because \(d\) itself lies
in its interval bank, and it is also sufficient. It follows exactly
that

\[
 B(H)=\{a\le M:2^{r+1}\mid a\},\qquad |B(H)|=h/2.        \tag{6}
\]

Deleting the prime 2 tests necessity, and divisibility by \(2^{r+1}\)
makes every prime deletion sufficient.

The two-factor reduction removes this particular obstruction. Since
all primes already have 2-adic valuation less than \(r\),

\[
 C(H)=\{u\le M:v_2(u)<r\}.
\]

An integer \(a\le M\) is a product of two such factors if and only if
\(v_2(a)\le2r-2\). To prove sufficiency, split its power of 2 into
two exponents at most \(r-1\), and put its odd part in either factor.
Both resulting factors are at most \(a\le M\). Therefore

\[
 R(H)=\{a\le M:2^{2r-1}\mid a\},\qquad |R(H)|=2=o(h).    \tag{7}
\]

Thus (5) forgets a real part of the load gap; it cannot replace (4).
Equation (7) only disposes of this example and does not prove a general
estimate for \(R(H)\).

## 4. The precise unproved estimate

A sufficient uniform statement for the sparse branch would be:

> For every fixed \(C_0>0\), along every sequence of positive intervals
> \(I\) of lengths \(M\to\infty\) and sets \(H\subset I\) with
> \(h=|H|=o(M)\) and \(M\le C_0h^2\), one has
> \[
> |R(H)|=o(h).
> \tag{8}
> \]
> The little-o term must be uniform in the interval shift and the choice
> of \(H\).

No argument in this note establishes (8). In particular, the
single-deletion condition (5), the fact that \(C(H)\) is divisor
closed, and the elementary initial interval contained in \(C(H)\) do
not by themselves supply the missing uniform counting estimate.

## 5. Conditional consequence, including small hot sets

Suppose an actual raw-minimal obstruction sequence has \(m\) sources,
all of load greater than \(c>2\), and satisfies

\[
 m=o(M),\qquad M\le C_1m^2,\qquad
 |\{b\in I:X(b)>1\}|\le C_2m.                          \tag{9}
\]

The hot set need not itself have size comparable to \(m\), and (9)
does not imply \(M=O(h^2)\). To use (8), enlarge it to an arbitrary
set \(H'\subset I\) of size

\[
 h'=\max\{h,\lceil\sqrt M\rceil\}.
\]

For sufficiently large \(M\), this is possible with \(H'\ne I\).
Equations (9) give \(h'=O(m)=o(M)\) and \(M\le(h')^2\).
The source inclusion (4) survives this enlargement. Thus, **if** (8)
were proved, it would imply

\[
 m\le |R(H')|=o(h')=o(m),
\]

a contradiction. A cardinality estimate is enough here; a weighted
source-tail bound is not additionally required.

This conditional deduction addresses the sparse branch only. It does
not supply an estimate for the remaining dense regime, and the premise
(8) remains unproved.
