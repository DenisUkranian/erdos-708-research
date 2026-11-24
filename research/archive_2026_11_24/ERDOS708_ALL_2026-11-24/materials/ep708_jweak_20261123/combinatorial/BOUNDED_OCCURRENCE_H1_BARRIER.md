# A bounded-occurrence obstruction to universal quadratic H1 tail error

## Precise scope

Bounded substantial-weight occurrences per source do not justify a
universal aggregate-tail comparison with an additive \(O(k^2)\) error,
where \(k\) is the global number of substantial prime coordinates.

The construction below uses unit weights on \(k\) primes. **Every integer
in the prefix has at most four occurrences of these primes**, counted
with multiplicity. Nevertheless,

\[
 \sum_{n\le M}(X(n)-1)_+
 -
 \sum_{b\in I}(X(b)-1)_+
 \ge {k-1\choose4}-{k\choose2}-3k.                       \tag{1}
\]

The lower bound has order \(k^4\). The primes can tend to infinity while
their total reciprocal mass tends to zero. Thus neither a lower bound
on prime size, small harmonic mass, nor the bounded source occurrence
condition repairs this particular universal tail-error assertion.

This is **not** a counterexample to J_weak or to Erdős problem 708.
The construction does not impose the required lower source load
\(X(a)>2+\delta\), optimality, active-row balance, or the full minimality
conditions. In particular, replacing the desired joint argument by
this universal H1-tail estimate would discard essential information.

## 1. Parameters and exact interval

Choose \(k\ge9\) distinct odd primes

\[
 P=\{p_1<\cdots<p_k\}
\]

such that

\[
 p_k^4<2p_1^4,\qquad p_1^5-p_1>p_k^4.
                                                               \tag{2}
\]

Put

\[
 M=p_k^4,\qquad H=(M-1)/2.
\]

Since every listed prime is at least \(p_1\), condition (2) implies

\[
 \Omega_P(n)=\sum_{p\in P}v_p(n)\le4\quad(n\le M).         \tag{3}
\]

Define an integer \(C>H\) by the simultaneous CRT congruences

\[
 C\equiv\frac{p^5-p}{2}\pmod{p^5}\qquad(p\in P),           \tag{4}
\]

and let

\[
 I=\{C-H,\ldots,C+H\}.
\]

The moduli in (4) are pairwise coprime. Every listed prime divides
\(C\) exactly once. Moreover, the distance of \(C\) from either
neighboring multiple of \(p^5\) is greater than \(H\), by (2).
Consequently

\[
 v_p(b)\le4\quad\text{for every }b\in I,\ p\in P.          \tag{5}
\]

Thus the raw-power calculation below does not hide any omitted large
target exponents.

## 2. Capped coordinates: an exact inclusion-exclusion calculation

First set

\[
 Y(n)=\sum_{p\in P}1_{p\mid n}.
\]

For every nonnegative integer \(j\),

\[
 (j-1)_+=\sum_{\ell=2}^j(-1)^\ell {j\choose\ell}.         \tag{6}
\]

For a prime subset \(S\subseteq P\), write \(d_S=\prod_{p\in S}p\)
and

\[
 \varepsilon_S=\#\{b\in I:d_S\mid b\}-\lfloor M/d_S\rfloor
 \in\{0,1\}.
\]

If \(|S|=4\), then \(M/2<d_S\le M\). There is exactly one prefix
multiple of \(d_S\), and exactly one interval multiple, namely \(C\).
If \(|S|\ge5\), then \(d_S>M\), so there is no prefix multiple, whereas
the centered interval still contains exactly the single multiple \(C\).

Applying (6) and separating the two- and three-prime intersections gives
the exact identity

\[
 \begin{aligned}
 &\sum_{n\le M}(Y(n)-1)_+
 -\sum_{b\in I}(Y(b)-1)_+\\
 &\quad=
 -\sum_{\substack{S\subseteq P\\|S|=2}}\varepsilon_S
 +\sum_{\substack{S\subseteq P\\|S|=3}}\varepsilon_S
 -\sum_{j=5}^k(-1)^j{k\choose j}\\
 &\quad={k-1\choose4}
 -\sum_{|S|=2}\varepsilon_S
 +\sum_{|S|=3}\varepsilon_S .
                                                               \tag{7}
 \end{aligned}
\]

The last step is the finite binomial identity
\(\sum_{j=0}^{4}(-1)^j{k\choose j}={k-1\choose4}\).
The triple errors have the favorable sign. Therefore

\[
 \sum_{n\le M}(Y(n)-1)_+
 -\sum_{b\in I}(Y(b)-1)_+
 \ge {k-1\choose4}-{k\choose2}.                          \tag{8}
\]

No independence assumption about residues is used.

## 3. Restoring all raw prime powers

Now set \(X(n)=\Omega_P(n)\), so the weights of all listed primes are
one. The exact identity

\[
 (X(n)-1)_+-(Y(n)-1)_+=X(n)-Y(n)
       =\sum_{p\in P}\sum_{j\ge2}1_{p^j\mid n}           \tag{9}
\]

holds at every integer, including those divisible by none of the
listed primes. Equations (3) and (5) mean that only \(j=2,3,4\)
occur on either side.

For each of these \(3k\) powers, the interval count exceeds its prefix
count by either zero or one. Consequently the raw restoration changes
the deficit in (8) by at most \(3k\), proving (1).

This is a genuine obstruction to a constant times \(k^2\) error:
for fixed occurrence bound four, the quotient of the right side of
(1) by \(k^2\) tends to infinity.

## 4. Prime size and harmonic mass

For every \(k\), the primes may be chosen in a sufficiently large fixed
relative interval, for example \([P,1.1P]\), which satisfies the first
condition in (2). There are arbitrarily many primes in such intervals;
this standard fact follows, for example, from the prime number theorem.
Choose \(P\) sufficiently large in terms of \(k\), so that the second
condition in (2) holds and \(k/P\to0\).

Then

\[
 \min P\longrightarrow\infty,\qquad
 \sum_{p\in P}\frac1{p-1}\le\frac{k}{P-1}\longrightarrow0,
\]

while (1) continues to hold. The error therefore does not arise from
small anchor primes or from large weighted reciprocal mean.

The finite example below uses only trial-division verification and CRT,
so it does not depend on an asymptotic prime-distribution input.

## 5. Autonomous finite certificate

Take the following 20 primes:

\[
 \begin{split}
 1009,\ 1013,\ 1019,\ 1021,\ 1031,\ 1033,\ 1039,\ 1049,\ 1051,\ 1061,\\
 1063,\ 1069,\ 1087,\ 1091,\ 1093,\ 1097,\ 1103,\ 1109,\ 1117,\ 1123.
 \end{split}
\]

Then

\[
 M=1123^4=1590446354641.
\]

The adjacent certificate specifies all CRT residues, the exact center
and period in hexadecimal, and the relevant exact counts. The
standard-library verifier checks these data without enumerating the
length-\(M\) interval.

The checked values are:

\[
 \sum_{|S|=2}\varepsilon_S=89,\qquad
 \sum_{|S|=3}\varepsilon_S=573,
\]

and the total raw-power-tail count excess is \(39\). Thus

\[
 \begin{aligned}
 \text{capped H1 deficit}&={19\choose4}-89+573=4360,\\
 \text{raw H1 deficit}&=4360-39=\boxed{4321}.
 \end{aligned}
\]

The general lower bound (1) is \(3626\) for these parameters.

Files:

- bounded_occurrence_h1_certificate.json;
- verify_bounded_occurrence_h1.py;
- bounded_occurrence_h1_verification.json.

The missing joint gluing step must retain the source load threshold and
actual demand balance. This example only excludes replacing that step
by a universal quadratic H1-shift bound.
