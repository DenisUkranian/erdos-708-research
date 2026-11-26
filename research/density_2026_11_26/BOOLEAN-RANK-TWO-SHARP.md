# Exact sharp cutoff for the rank-two Boolean transfer in #708

One approach to #708 uses a Boolean moment inequality with source cutoff 2 and target cutoff 1. In the rank-two case there is an exact sharp finite-dimensional answer. For \(N\ge2\) coordinates with weights in \([0,1]\), a universal source cutoff is \(2-2/N\), and it cannot be lowered. This applies whenever the source profile has size at most two and the first and relevant pair moments agree. The optimal cutoff approaches 2 as the number of coordinates increases.

Write \(X(S)=\sum_{i\in S}w_i\). For every target profile \(S\) of size \(m\ge2\),
\[
\sum_{\{i,j\}\subseteq S}(w_i+w_j-1)_+\le\frac{m}{2}(X(S)-1)_+.
\]
Fix the total weight \(X(S)=k+\theta\), with \(k\) an integer and \(0\le\theta<1\). The convex function on the left has a maximum at a vertex of the cube slice with this total. The vertex has \(k\) unit weights, at most one fractional weight \(\theta\), and zeros. If \(k=0\) both sides vanish. Otherwise the maximum is \(\binom{k}{2}+k\theta\). At \(\theta=0\) the desired inequality holds since \(k\le m\). At \(\theta=1\) it holds since \(k+1\le m\); between endpoints it follows by linearity. If \(k=m\) use only \(\theta=0\). The cases \(m=0,1\) are immediate.

Let \(c=2-2/N\). For a source pair with total weight \(x\le2\), \((x-c)_+\le(2-c)(x-1)_+\). Therefore
\[
\mathbb E(X(U)-c)_+
\le \frac2N\sum_{\{i,j\}\text{ admissible}}(w_i+w_j-1)_+\Pr(\{i,j\}\subseteq U)
\le \mathbb E(X(V)-1)_+.
\]
The second inequality transfers the admissible pair moments, enlarges to all target pairs, and uses the preceding target bound. With identical first moments, this is the clipped-weight transfer.

For sharpness, give all coordinates cost \(1/2\) and weight 1. Let \(U\) be empty with probability \(1/2\) and otherwise a uniform pair. Let \(V\) be empty with probability \(1/N\), the complete set with probability \(1/[N(N-1)]\), and each singleton with probability \((N-2)/[N(N-1)]\). Their single inclusion probabilities are \(1/N\), and their pair inclusion probabilities are \(1/[N(N-1)]\), so every admissible moment agrees exactly. However \(\mathbb E\min(X(V),1)=1-1/N\) and \(\mathbb E\min(X(U),c)=c/2\) for \(c\le2\). Thus \(c\ge2-2/N\) is necessary.

This is an obstruction for schemes using only admissible abstract Boolean moments. It does not assert that these extremal distributions can occur in positive-density arithmetic instances.
