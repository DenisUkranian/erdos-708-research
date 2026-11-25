# Audited component lemmas

Let \(I=(x,x+M]\cap\mathbb Z\) be a positive interval of integer length \(M\). Let \(B_d=I\cap d\mathbb Z\) for \(1\le d\le M\); \(N_d=\lfloor M/d\rfloor\). A bank is a set of available positions, not a supply of independently reusable prime units.

## 1. Demand-weighted overlap and shared capacity

Assign nonnegative demands \(s_d\) to distinct carriers and put \(\beta_d=s_d/N_d\), \(S=\sum s_d\), \(W=\sum\beta_d\). Since \(N_d\ge M/(2d)\),
\[
 \sum_{d<e,\ (d,e)\le G}\beta_d\beta_e|B_d\cap B_e|
 \le {2GS^2\over M}+{W^2\over2}.
\]
Indeed \(|B_d\cap B_e|\le M(d,e)/(de)+1\), and \(\beta_d/d\le2s_d/M\). The inequality does not require a bound on the number of carriers. If \(S=O(n)\), \(d\le Bn\), \(G=o(M/n)\), its right hand side is \(o(n)+O_B(n^4/M^2)\), hence \(o(n)\) for \(M/n^{3/2}\to\infty\). This controls only the specified overlap, not the entire matching.

For any \(H\ge\gamma>0\) and \(0\le x_i\le H\),
\[
 (\sum_i x_i-H)_+\le {2\over\gamma}\sum_{i<j}x_i x_j.
\]
For \(V=\sum_i x_i>H\), use \(2\sum_{i<j}x_ix_j=V^2-\sum_i x_i^2\ge V(V-H)\).
For \(\beta_i\in[0,1]\), the unit-capacity version is \((\sum\beta_i-1)_+\le\sum_{i<j}\beta_i\beta_j\), by the two-term Bonferroni bound.

If two carriers have different exact parts supported on primes \(>y\), at least one of \(d/(d,e),e/(d,e)\) exceeds \(y\). Orient each pair so that the other carrier, say \(d\), is used for the denominator of \(M/(yd)\). Summation gives
\[
 E_{\rm cross}\le 2SW/y+W^2/2.
\]
This is again an overlap bound, not an automatic global cover.

## 2. Conditional long-bank union transfer

Assume the following uniform relative counting input: for a divisor-downward-closed set of \(y\)-smooth parts and intervals of equal real length \(U\) with \(\log U/\log y\ge u\), the shifted count is at least \(1-\varepsilon(u)\) times the prefix count; \(\varepsilon(u)\to0\). This input is the subject of the earlier smooth-profile sieve argument and must retain its real-interval and uniformity hypotheses.

Let all carriers be at most \(D\), and let \(s\) distinct sources in \([1,M]\) lie in their prefix union. Order carriers increasingly. For each \(d_i\) exclude only multiples of previous \(d_j\) for which \(\max(d_i,d_j)/(d_i,d_j)\le y\). The resulting quotient restriction is downward closed and all excluded quotient moduli are at most \(y\). Assign each source to its earliest carrier. In the prefix cell with \(c_i\) points let \(s_i\) be assigned sources and \(\beta_i=s_i/c_i\), omitting zero-demand cells. Standard lower sieve bounds give \(c_i\gg M/(d_i\log y)\) when \(u=\log(M/D)/\log y\) is sufficiently large (divisibility by none of the primes up to \(y\) is sufficient; identical carriers have been removed).

Then \(\sum\beta_i M/d_i\ll s\log y\), \(\sum\beta_i\ll Ds\log y/M\). Close cells are disjoint for each such pair. For other pairs the intersection is bounded by \(M/(yd_i)+1\) in increasing order. Clipping the sum of payments at one and applying the counting input yields
\[
 |\bigcup B_{d_i}|\ge(1-\varepsilon(u))s
 -O((\log y)^2s^2[D/(My)+D^2/M^2]).
\]
Taking \(D=M/n^{1-\theta}\), \(y=n^\theta(\log M)^3\), \(0<\theta<1/2\), \(n\le M\le16n^2\), the additive error is \(o(n)\). Taking \(\theta\) small controls the relative error. This is a Hall-deficiency estimate for long carriers, conditional on the stated sieve input; it does not treat all short carriers. In particular it is not a proof of the unrestricted hinge inequality.

## 3. Exact random profiles: a pointwise identity

Let \(h=a/P^+(a)\), \(T_h=M/h\), and \(P\) be the union of prime supports of the carriers. Each prime factor of \(h\) is at most \(T_h\). Independently select primes of \(P\) with probability \(\theta\in(0,1)\) (or any fixed per-prime probabilities). Write
\[
 D_T(b)=\prod_{p\in P,\ p\le T,\ p\ {\rm selected}}p^{v_p(b)},\qquad K_h(b)=\Pr[D_{T_h}(b)=h].
\]
For \(h_1<h_2\) we have \(T_{h_1}>T_{h_2}\) and \(D_{T_{h_1}}(b)\ge D_{T_{h_2}}(b)\) in every realization. Thus the two equalities cannot both hold, and
\[
 0\le K_h(b)\le {\bf1}_{h\mid b},\qquad \sum_h K_h(b)\le1.
\]
Exactly,
\[
 K_h(b)={\bf1}_{h\mid b}\theta^{\omega(h)}
 (1-\theta)^{\#\{p\in P:p\le T_h,\ p\mid b/h\}}
\]
except that if a prime dividing \(h\) also divides \(b/h\), the event is impossible and the value is zero. (Such a prime is required selected and its exponent must be exact.) The monotonicity proof does not require an averaged lower bound. The earlier proposed lower bound and its \(\omega(h)\le\rho\log\log T_h\) consequence require an independent analytic proof with this exact-exponent restriction.

## 4. A capped-valuation certificate for separated, bounded reciprocal mass

Here is a rigorous form of the latest separated-support argument. Fix \(\alpha>0, A_*>1, B,C>0\). Put \(L=\log M\), \(\ell=\log\log M\), \(Y=\exp(L/\ell^{A_*})\). Suppose every carrier \(h=a/P^+(a)\) has \(T_h\ge M^\alpha\), its prime factors greater than \(Y\) belong to a fixed set \(R\) with \(\sum_{q\in R}1/q\le B\), and \(\omega_R(h)\le k=C\log\ell\). Define \(J_q=\lfloor L/\log q\rfloor\) for \(q\le M\) and take an integer \(D\) larger than a constant depending on \(B,\alpha\). On \(h\mid b\) let
\[
 C_h(b)={\bf1}_{P^-(b/h)>Y}
 \left(1-D^{-1}\sum_{q\in R,\ q\le T_h}\min(v_q(b/h),J_q)\right);
\]
otherwise \(C_h(b)=0\). We use \(P^-(1)=+\infty\). The full small part of each positive carrier is fixed by \(b\).

**Pointwise proof.** Choose the numerically least carrier \(h_0\) with positive \(C_{h_0}(b)\); every other positive carrier has \(T_h\le T_{h_0}\). Among \(q\in R\) with \(q\le T_{h_0}\) dividing \(b\), at most \(k+D-1\) exist: at most \(k\) in \(h_0\) and at most \(D-1\) extra in \(b/h_0\), since \(J_q\ge1\). For any positive carrier, the primes at most \(T_h\) form a prefix of this ordered set. On that prefix, \(v_q(h)\le\min(v_q(b),J_q)\), and the sum of the deficits from these capped exponents is at most \(D-1\), since each deficit is bounded by \(\min(v_q(b/h),J_q)\). The small part, prefix and deficit vector determine \(h\). There are at most
\[
 C_*(k,D)=(k+D)\binom{k+2D-2}{D-1}
\]
positive carriers (stars and bars), irrespective of their actual exponents. Thus \(\sum_h C_h(b)\le C_*(k,D)\), with negative terms harmless for this upper bound.

**Average estimate.** Use the standard fundamental lemma and uniform upper-bound sieve for primes \(\le Y\). For a real interval of length \(T=T_h\), the rough count is \(\gg T/\log Y\), since \(\log T/\log Y\to\infty\). For a quotient of length \(U\ge1\), the rough count is \(O(U/\log(2\min(U,Y)))\), uniformly in the shift (with a fixed absolute constant). For the first powers \(q\le T/Y^v\), with fixed \(v>1\), use \(O(T/(q\log Y))\) and sum over \(R\). For \(T/Y^v<q\le T\), dyadic subdivision and Chebyshev's prime bound (these primes exceed \(\sqrt T\) for large \(M\)) give \(O(T\log\log Y/\log T)\). For \(j\ge2\), even dropping roughness, the terms with \(q^j\le T\) contribute at most \(O(T/Y)+O(\sum_{q\le T}J_q)\), while terms with \(q^j>T\) each cost at most one. The bound \(\sum_{Y<q\le T}J_q\ll_\alpha T/\log T\) follows by splitting at \(\sqrt T\). In consequence the subtracted sum is
\[
 O_B(T/\log Y)+O_\alpha(T\log\log Y/\log T)+O(T/Y).
\]
Its last two terms are \(o(T/\log Y)\) because \(A_*>1\). Choose \(D\) sufficiently large, after the fixed constants. Then \(\sum_{b\in I}C_h(b)\gg T_h/\log Y\).

**Hall.** The number of sources with a fixed carrier is at most \(\pi(T_h)\ll T_h/\log T_h\). Summing the average bound for the distinct carriers of any source subfamily and using the pointwise bound gives a neighborhood-to-demand ratio
\[
 G(M)\gg_{\alpha,B,C,A_*}\ell^{A_*}/(1+\log\ell)^D\longrightarrow\infty.
\]
Hence Hall matching is possible, even after one reserved position, for large \(M\). Reserve a multiple of one full source; assign distinct multiples of all remaining carriers, and repair one deleted largest-prime unit per remaining source using unused positions and full-interval supply. This proves \(\tau\le 2n-1\) in this explicit class. For \(n=1\) reserve alone suffices. The reciprocal mass hypothesis is substantive: all primes in \((Y,M]\) have reciprocal mass of order \(A_*\log\ell\), not necessarily bounded. This lemma alone cannot be applied to the entire critical class.

The rare-continuation variant in the conversation (sources \(hqu\), with \(u\) rough and a small reciprocal mass of eligible \(q\)'s) has the same numerator count bound by the preceding first-power sieve argument. To infer a cover one must ensure that the removed quotient \(qu\) has repair cost at most one, or separately account for all its demand. A Hall match of \(h\) alone does not prove a two-position cover for general \(qu\).

## 5. Reserve matching and repair

If every nonempty source subfamily \(S\) of a matching graph has \(|N(S)|\ge G|S|\), forbidding \(r\) already selected positions leaves Hall deficiency at most \(r/G\): \(|S|-|N(S)\setminus B_0|\le\min(|S|,r-(G-1)|S|)\le r/G\). There is a matching missing at most \(\lfloor r/G\rfloor\) sources. Exact integer Hall deficiency is the maximum over subsets. For prime-deletion cofactors of matched sources, repair the missing prime unit at most once per matched source. A previously covered source group is not double counted if carrier assignments avoid its reserved points.

For unmatched sources, the established global bound \(g(t)\le10t\) from the cited Wang framework is useful only with a joint disjointness/payment argument; simply adjoining a cover that overlaps an existing cover does not automatically supply the product of both groups. One unconditional alternative is to repair each prime occurrence, or to pack cofactor factors into blocks of size \(\le M/(K+1)\) when at most \(K\) positions have already been used. The cost of this correction must be shown \(o(n)\); it is not implied solely by \(t=o(n)\) in a construction that must preserve all existing product demands.

## 6. LCM loss for local core matchings

For \(a_i=d_i p_i r_i\), \(p_i\le r_i\), with \(p_i\) a smallest prime of \(a_i\), suppose each source has a representative divisible by \(d_i p_i\); matches are distinct within each core group. At a common position \(b\) define \(E_b=\Omega(\prod_i d_i/\operatorname{lcm}_i d_i)\). Since \(p_i\le P^-(d_i)\), choose a source with the smallest \(p_i\) among that bucket and, among those, with maximal \(v_{p_i}(d_i)\). If some other core contains a larger exponent of that prime, its smallest prime is at most \(p_i\) and hence equals \(p_i\), contradicting maximality. Therefore \(\operatorname{lcm}_i(d_i)p_i\mid b\). In total the bucket can supply its core LCM and one of its outside prime occurrences. Repair the remaining demand using at most \(2t-1+E_b\) prime units for \(t\) assigned sources. The total cover size is bounded by \(2n+\sum_b E_b\) for the represented sources (and by \(2n-1+\sum E_b\) with a successfully reserved full source). This argument uses actual total prime units, not merely distinct primes. It applies to any constructed local matchings with the smallest-prime condition; no bound \(\sum E_b=o(n)\) has been proved in general.
