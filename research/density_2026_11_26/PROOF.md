# Erdős problem 708: the density-2/5 theorem

**Claim.** Let \(A\subseteq\{2,\ldots,M\}\), with \(M=\max A\) and \(n=|A|\). If \(n/M\ge2/5\), then for all sufficiently large \(M\), every interval \(I\) of \(M\) consecutive integers contains at most \(2n\) distinct positions whose product is divisible by \(\prod_{a\in A}a\). The bound on \(M\) is uniform in \(A\) and the shift. This does not settle smaller densities or the unrestricted asymptotic. See [Erdős's formulation](https://hrj.episciences.org/125/pdf), section 1.

## 1. Linear programming and profile transfer

Intervals containing zero are immediate; reflect negative intervals. For positive intervals, put \(d_p=\sum_{a\in A}v_p(a)\) for each prime \(p\le M\). The covering relaxation has one variable in \([0,1]\) per target position and one constraint \(\sum_{b\in I}v_p(b)t_b\ge d_p\) per prime. It is feasible: the target product is a multiple of \(M!\), because it contains at least \(\lfloor M/p^j\rfloor\) multiples of each \(p^j\). Its dual objective is \(\Phi=\sum_A X-\sum_I(X-1)_+\), where \(X(b)=\sum_p w_pv_p(b)\) and \(w_p\ge0\). A price above one can be reduced to one, because for every affected position the hinge is already linear and target capacity is at least demand. Round an optimal primal vertex upward; at most \(\pi(M)=o(M)\) coordinates can be fractional, by the rank bound for the active prime constraints.

Choose \(\eta=(\log M)^{-1/4}\), \(y=\exp(\sqrt{\log M})\), and \(z=M^{1-\eta}\). Write \(s=\sum_{p\le y}w_pv_p\), \(W=\sum_{y<p\le z}w_p1_{p\mid b}\), and \(\mu=\sum_{y<p\le z}w_p/p\). Source terms omitted by truncating primes above \(z\) or dropping repeated occurrences above \(y\) are \(o(M)\), by Mertens' reciprocal-prime estimate and \(\sum_{p>y}1/(p(p-1))=o(1)\). Dropping them in the target hinge is safe. The linear target total of \(s+W\) still dominates the source total term by term.

The exact small-prime profile \(h=(v_p)_{p\le y}\) is asymptotically distributed, in total variation, as independent geometric valuations in every interval of length \(X\) with \(\log X/\log y\to\infty\). For the uses here the error decreases exponentially in a fixed positive multiple of \(\log X/\log y\). One proof uses the fundamental lemma of the dimension-one sieve for the exact \(y\)-part \(d\le\sqrt X\), on the quotient interval of length \(X/d+O(1)\). The exceptional \(y\)-parts \(d>\sqrt X\) are bounded by taking their first increasing-prime prefix \(p m>\sqrt X\); then \(\sqrt X/p<m\le\sqrt X\), \(m\) is \(p\)-smooth, and the remaining quotient avoids primes below \(p\). The upper sieve gives \(O(X/(pm\log(2p)))\) possibilities for each prefix. In a band \(\sqrt u<p\le u\), the sum of reciprocal \(p\)'s is \(O(1)\), and
\[
\sum_{\substack{m>\sqrt X/u\\m\ u\text{-smooth}}}m^{-1}
\ll\log(2u)\exp[-c\log(\sqrt X/u)/\log(2u)].
\]
This follows by Rankin's trick with exponent \(1/\log(2u)\) and the Euler product, using \(\sum_{p\le u}\log p/p=O(\log(2u))\). Summing over \(u=y,y^{1/2},y^{1/4},\ldots\) gives the stated exponential tail uniformly in the shift. The same Rankin bound controls the independent-profile tail. For the main strata the sieve is uniform in translated quotient intervals: divisibility by each sieve modulus has the length-over-modulus count with error at most one; a fixed power of the quotient length as sieve level makes the accumulated remainder negligible.

Dividing by a product \(d\) of primes above \(y\) preserves the profile. Thus for any profile event \(H\) or bounded profile function, the corresponding weighted divisor moment over a shifted interval is its profile mass times the reciprocal weighted sum, up to \(o(M)\). For first moments the moduli are at most \(z\), with total reciprocal mass \(O(\log\log M)\), which the exponentially small profile error absorbs. For the pair and triple moments below, moduli are at most \(M^{1-3\eta}\), total reciprocal weighted mass is bounded, and the sum of rounding errors is \(o(M)\). Coefficients are bounded and the multiplicity of each modulus in any one moment is bounded.

## 2. Source variance and the target cap

Set \(\rho=n/M\). Use 24 upper prime bands with exponent endpoints \(a_i=(48+i)/144\), \(0\le i\le24\), all diminished by \(\eta\). Lower primes lie between \(y\) and the first endpoint, and high primes have exponent above \(1/2\), up to \(z\). The gap of width \(\eta\) just below \(1/2\) costs \(o(1)\) reciprocal mass. Let \(q_i,q=\sum_iq_i,\nu\) be the upper bin, total upper, and high weighted reciprocal masses. Let \(B_L,B_Q,B_\nu\) be the lower, upper and high sums of \(w_p(1-w_p)/p\). The code constants \(c_i,h_i,\mathrm{cap}_i\) are outward upper roundings, in units \(1/32000\), of
\[
 \log\frac{2}{3(1-a_i)},\quad \log(2(1-a_{i-1})),\quad \log\frac{a_i}{a_{i-1}},
 \qquad 1\le i\le24.
\]
Their strict enclosures can be checked with six terms of the series for \(2\operatorname{atanh}((u-1)/(u+1))=\log u\), with a geometric bound for the remaining terms. The full upper reciprocal mass is at most \(C=.4055>\log(3/2)\) eventually. Put \(D=2\sum_i q_i(\nu-h_i)_+\). Two high primes cannot divide a source number together. For each upper bin, also exclude all its pairs with high primes of exponent \(>1-a_{i-1}+\eta\); their high weighted mass is at least \((\nu-h_i)_+\). Thus \(v=\operatorname{Var}_{[1,M]}W\le\mu-B_L-B_Q-B_\nu-\nu^2-D+o(1)\), using \(\lfloor M/(pq)\rfloor\le M/(pq)\) for the remaining second-moment terms.

Let \(G\ge0\) be a uniform lower bound on the conditional target mean of \((W-1)_+\), in the sense of an additive \(o(M)\) error on every profile event. Put \(x=(\mu-1)_+\), \(m=(1-\mu)_+\) and \(c=(s+\mu-1)_+\). Conditional first moments bound the target cap \(\min(s+W,1)\) by its baseline \(\min(s+\mu,1)\), via a tangent. On profiles where \(c<G\), use \(\min(s+W,1)\le s+W-(W-1)_+\) instead, gaining \(G-c\) per position. Transfer the capped baseline and \((G-c)_+\) to the source, and use linear target capacity. Each source position outside \(A\) pays \(c+(G-c)_+\ge\max(x,G)\). Consequently
\[
 \Phi/M\le\rho+\mathbb E[1_A(W-\mathbb EW)]-(1-\rho)\max(x,G)+o(1).
\]
With \(R=\mathbb E[(W-\mathbb EW)-(1_A-\rho)/(1-\rho)]^2\), the covariance is exactly \(\rho/2+(1-\rho)(v-R)/2\). Therefore it suffices to prove
\[
 \Gamma=m+\nu^2+D+B_L+B_Q+B_\nu+x+2(G-x)_++R\ \ge\ \Gamma_0,
 \quad\text{giving }\Phi/M\le\rho+\tfrac12-\tfrac12(1-\rho)\Gamma_0+o(1).
\]

## 3. Nested target estimate

Choose a lower pool of weighted reciprocal mass \(\ell=\min(3/2,(\mu-\nu-q)_+)\), and its nested lowest-prime prefixes \(R_i\) of masses \(r_i=\min(1,(\ell-c_i)_+)\), up to \(o(1)\). These prefixes lie below exponent \((1-a_i)/2-\eta\): the reciprocal mass lost to larger lower primes is no more than the bound \(c_i\). The only rounding needed is the largest individual reciprocal, \(o(1)\).

For any present lower labels, retain each independently with probability \(w_p\), and write \(h_{ij}=(w_i+w_j-1)_+\) for a pair hinge. The hinge of the retained sum is at least the sum of pair hinges minus the sum, over triples, of the least of their three hinges. To see this, append weights in decreasing order. Triangles using the largest new incident hinge pay for all the other incident hinges; the remainder is at most the newly appended weight. If the previous sum is less than one, at most one incident hinge can be positive, and the new total hinge covers it. Replace the least triangle hinge by the mean of its three edges. Averaging and transferring costs at most \(\ell/3\) times the transferred pair sum. This explains the common factor \(1-\ell/3\) on the pure pair term.

For an upper label \(j\), take the maximum pair hinge with its retained lower neighbors in \(R_i\). This is at least their sum minus the sum of the smaller of each pair of those hinges: pair each other hinge with the largest one. Replace each minimum by its two-term average, and multiply by the upper price \(w_j\). On transferring, the correction costs at most \(r_i/2\) of the mixed pair sum. For actual lower load \(L\), the upper-label maximum is at most \((w_j+\min(L,1)-1)_+\). Summing these terms over the upper labels and adding \((L-1)_+\) does not overcount the total hinge: apply superadditivity of \((u-(1-L)_+)_+\) to the upper load. Thus the pure and all mixed band lower bounds can be added even after taking their individual positive parts.

Let \(b=B_L\), fix bin \(j=16\), put \(r=r_j\), \(t=\ell-r\), \(e=B_{R_j}\). Nesting gives \(B_{R_i}\le\min(b,e+(r_i-r)_+)\). Jensen or the lower inequality \(h_{ij}\ge w_i+w_j-1\), then nonnegativity for each separate pair class, gives the two pure lower estimates
\[
 P_{\rm old}=(\ell-\ell^2/3)(\ell/2-b)_+,\quad
 P_{\rm split}=(1-\ell/3)[r(r/2-e)_++t(t/2-b+e)_++(rt-te-r(b-e))_+].
\]
The mixed bin bound is \(q_i(1-r_i/2)(r_i-B_{R_i})-f(r_i)B_{Q_i}\), with \(f(r)=r-r^2/2\) and \(B_{Q_i}\) the bin's variance charge. Taking positive parts separately and using \(f(r_i)\le1/2\) yields \(G\ge G_1-B_Q/2\), where
\[
 G_1=\max(P_{\rm old},P_{\rm split})+\sum_i q_i(1-r_i/2)(r_i-\min(b,e+(r_i-r)_+))_+.
\]
Since \(B_Q+2(G-x)_+\ge2(G_1-x)_+\), the upper charge cancels.

## 4. Source remainder and verification

Put \(P_0=q+\nu-q^2/2-q\nu+D/2-\rho\). At a source threshold \(a=1-\tau\), count upper and high labels of price at least \(a\), independently retained with probability \(w_p\). A nonempty retained set proves \(W\ge a\). The single-label term loses at most \(B_\nu/\tau\) from high prices and \(U_\tau/\tau\) from upper prices, where
\(U_\tau=\min(q(1-q/C),a(C-q))\).
The first upper bound follows from weighted Cauchy and \(w\le w(1-w)/\tau\) on skipped labels; the second from \(w\le a(1-w)/\tau\). The two-label Bonferroni subtraction is at most \(q^2/2+q\nu-D/2\). Removing \(A\) costs at most \(\rho\). The probability outside \(A\) at threshold \(a\) is therefore at least \((P_0-(U_\tau+B_\nu)/\tau)_+-o(1)\).

For increasing \(a_i=1-\tau_i\), put \(c_i'=(a_i-\mu+\rho/(1-\rho))_+^2\), \(c_0'=0\). The pointwise squared remainder on the source complement dominates the sum of \((c_i'-c_{i-1}')1_{W\ge a_i}\); this telescopes. The resulting source bonus \(S\) is the minimum over \(u\ge0\) of
\[
 u+\sum_i(c_i'-c_{i-1}')(\tau_i P_0-U_{\tau_i}-u)_+/\tau_i .
\]
It lower-bounds \(B_\nu+R\), up to \(o(1)\). The minimization is exact by checking zero and the positive breakpoints of a convex piecewise linear function.

The main exact-arithmetic check proves
\[
 m+\nu^2+D+x+b+2(G_1-x)_++S\ge.3334
\]
on \(.4\le\rho\le.4035\). It uses the upper density for \(P_0\) and the rounded lower odds \(21333/32000\) in \(c_i'\). Each parameter box is bounded by its appropriate endpoints. The positive-part cross expression in \(P_{\rm split}\) is nondecreasing in both \(r,t\) for \(0\le e\le b\): a negative slope forces the expression itself to be nonpositive. Use lower \(r,t\), upper \(b\), and the worse endpoint for \(e\), since the inner expression is affine in \(e\). Use upper \(\ell\) for \(1-\ell/3\). For each mixed bin the bound uses lower \(r_i\) and upper charge \(\min(B,E+(c_j-c_i)_+)\), with \(B,E\) the upper endpoints of \(b,e\). Minimize the sum of nonnegative bin coefficients under the mass caps by filling cheapest bins first, with lower \(q\). Combine with the independent bound for \(D\). The checked ranges are \(0\le\nu\le.6\), \(0\le m\) or \(x\le.4\), and \(0\le b,e\le.4\); outside them the baseline already suffices. See the JavaScript for the precise integer bounds.

The overlap from .4035 upward follows by the same separate-band formula with \(\ell\) capped at one and \(G_1\) replaced by the old pure bound plus \(\sum_i q_i(1-r_i/2)(r_i-b)_+\), using the overlap check. The earlier overlap checks use unseparated prices: use any fraction \(\alpha\) of the nonnegative pure piece, \(g_\alpha=\alpha(\ell^2/2-\ell^3/6)+\sum_i q_i f(r_i)\), and \(\kappa_\alpha=\max(\alpha(\ell-\ell^2/3)+q-R_*/2,f(r_1))\), where \(R_*=\min\sum_i q_i r_i\) fills the highest bins first. Minimizing \(B+2(g_\alpha-x-\kappa_\alpha B)_+\) gives \(\min(2,1/\kappa_\alpha)(g_\alpha-x)_+\). When \(\mu\le1\), restrict to \(\alpha\ge1/2\); then \(\kappa_\alpha\) is nondecreasing in \(\ell\) because \(q+\ell\le1\), and \(g_\alpha'\le\kappa_\alpha\). Therefore lowering \(\mu\) from 1 cannot lower the total bound after adding \(m\). The source bonus also cannot decrease. Of the earlier overlap checks, one uses the multilevel bonus, an alternative uses a single-level bonus with the weaker upper mass cap \(\sum_i\mathrm{cap}_i\), and the variance-only check for the highest densities uses no bonus.

In every range the first bound in Section 2 leaves fixed strict slack below \(2\rho\). Uniform error and rounding fit inside the slack. At density at least \(1/2\), choose the entire interval instead.

## References

- P. Erdős, [Some of my forgotten problems in number theory](https://hrj.episciences.org/125/pdf), Hardy–Ramanujan Journal 15 (1992), section 1.
- H. Iwaniec, [A new form of the error term in the linear sieve](https://matwbn.icm.edu.pl/ksiazki/aa/aa37/aa37127.pdf), Acta Arithmetica 37 (1980), 307–320. The standard dimension-one fundamental lemma is the analytic input used in Section 1.

## Appendix: extension to density 39.75%

The statement at the start of this proof holds in fact for \(n/M\ge0.3975\) with all other hypotheses unchanged. Sections 1–4 are unmodified. Rerun the five-variable certificate with the two additional overlapping density ranges below. Each range uses its upper endpoint to lower-bound \(P_0\), and the stated odds bound to lower-bound the coefficients in \(S\). The table gives exact values implemented by verify-below-4000.js.

| Density interval | Lower odds | Upper density | Certified \(\Gamma\) | High-mean boxes | Low-mean boxes |
|---|---:|---:|---:|---:|---:|
| [0.3985, 0.4000] | 21200/32000 | 12800/32000 | 0.3376 | 3,732,245 | 241,113 |
| [0.3975, 0.3985] | 21112/32000 | 12752/32000 | 0.3403 | 7,098,589 | 324,561 |

In a fixed interval it suffices that \(\Gamma>(1-2\rho)/(1-\rho)\) at the lower density endpoint, since the required value decreases with density. The two required values are \(0.203/0.6015<0.3376\) and \(0.205/0.6025<0.3403\), respectively. Their strict margins uniformly absorb both the analytic errors and the LP rounding cost. The theorem at density at least 40% supplies the upper overlap.

A separately proved refinement for charging triple overlaps is in SPLIT-TRIPLES.md. It is not used in the sub-40% certificate and does not, by itself, certify a stronger threshold.
