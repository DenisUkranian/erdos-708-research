# Focused test of a weight-adapted sparse cutoff

Status: the proposed global sparse estimate is not proved here. No arithmetic counterexample satisfying the full-tail, genuine-optimality, and sparse hot-target hypotheses was established. The unrestricted conditional-tail first-moment theorem in the adjacent note is unaffected.

## Exact part of the proposed split

Fix \(\varepsilon>0\) and define

\[
 L=\left\{p:w_p>(1+\varepsilon)\frac{\log p}{\log M}\right\},
 \qquad R=\{p\le M\}\setminus L.
\]

For every source \(a\le M\), complete additivity gives the exact bound

\[
 X_R(a)\le(1+\varepsilon)
       \frac{\log a}{\log M}\le1+\varepsilon.             \tag{1}
\]

Consequently, if \(A=\{X>2+\delta\}\) and \(0<\varepsilon<\delta\), then

\[
 A\subseteq\{X_L>1+\delta-\varepsilon\}.                 \tag{2}
\]

Thus an estimate saying that the entire right side of (2) has weighted source demand \(o(|A|)\), under the actual sparse-optimum hypotheses, would already rule out that sparse optimum. It is a substantive missing arithmetic estimate, not a consequence of the deterministic split.

## Why the existing band-by-band Bonferroni estimate does not imply it

For a fixed weight band, the existing argument controls primes below its own degree-dependent cutoff and discards sources with too many occurrences from that small-prime part. Applying this independently to several bands does not produce one combined low-load budget: the retained band loads add with the same positive sign.

There are actual source monomials which evade every such individual small-prime cutoff. For example, set \(M=1500\),

\[
 w_{13}=w_{17}=0.9,\qquad w_5=0.3.
\]

The source \(a=5\cdot13\cdot17=1105\) has load \(2.1\). Both 13 and 17 exceed \(M^{1/3}\), the cutoff corresponding to \(s=2\) for the 0.9 band, while 5 exceeds \(M^{1/5}\), the cutoff corresponding to \(s=4\) for the 0.3 band. All three primes nevertheless belong to the joint set \(L\) when \(\varepsilon=0.05\). This checks only the classification obstruction; it is not a sparse-optimum counterexample.

## The product-size obstacle in a joint expansion

A minimal hot divisor \(d\), obtained by multiplying prime occurrences until its load first exceeds 1, obeys only

\[
 1<X_L(d)\le1+\max_{p\mid d}w_p.
\]

The definition of \(L\) therefore yields only

\[
 d\le M^{X_L(d)/(1+\varepsilon)}
 \le M^{(1+\max w_p)/(1+\varepsilon)}.                   \tag{3}
\]

For substantial weights, the exponent in (3) can exceed 1. Hence the first-crossing construction does not supply a uniform subcritical modulus for counting multiples in the length-\(M\) target interval. Restricting the expansion to actual divisors \(d\mid a\le M\) removes nonexistent source monomials, but does not solve the target overlap problem: intersections are governed by \(\operatorname{lcm}(d_1,d_2,\ldots)\), which can exceed \(M\), and each such target count can still be 1. Summing those unit rounding errors over a large family is not justified at the \(o(|A|)\) scale.

The newly proved conditional-tail bound permits deletion of sources with very large \(X(a)\), at uniformly small weighted cost. It bounds the number of substantial-price occurrences per retained source, but it neither bounds the number of distinct prime labels nor makes the above intersection errors small. No sign cancellation of those errors has been proved.

## Conclusion of this focused test

The high-part bound (1) is valid. The band-wise cleanup does not establish the required joint low-part estimate, and the direct weighted Bonferroni extension encounters the precise modulus and overlap obstruction above. No general sparse closure and no counterexample to the actual full-tail optimum were obtained in this test.
