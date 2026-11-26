# Lowering the coefficient-two density threshold in Erdős problem 708

**Theorem.** Let $A\subseteq\{2,\dots,M\}$, $M=\max A$, $n=|A|$, and let $I$ consist of $M$ consecutive integers. If $n/M\ge0.3930$, then for every sufficiently large $M$, there are at most $2n$ distinct positions of $I$ whose product is divisible by $\prod_{a\in A}a$. The sufficiency threshold is uniform in $A,I$. The unrestricted asymptotic is open.

The previous [density certificate](../density_2026_11_26/PROOF-3960.md) proves this for $n/M\ge0.3960$. This note supplies the adjacent range. It uses the preceding proof's small-prime profile transfer, variance estimate and nested target bounds from [PROOF.md](../density_2026_11_26/PROOF.md) and [SPLIT-TRIPLES.md](../density_2026_11_26/SPLIT-TRIPLES.md). Its new bounds combine a Bernoulli rounding on the source, the forced conditional mean of a putative counterexample and the integer pair envelope.

## Common inequalities and notation

Intervals containing zero are immediate and entirely negative intervals can be reflected. Use nonnegative prime weights (prices) $w_p\le1$ in the product-cover LP dual. Write $\Phi$ for its objective and $\rho=n/M$. On the canonical interval choose $m$ uniformly from $[1,M]$; ordinary expectations here are normalized by $M$, including those with $1_A$. Put $y=\exp\sqrt{\log M}$, $z=M^{1-(\log M)^{-1/4}}$, $W(m)=\sum_{y<p\le z}w_p1_{p\mid m}$, and $\mu=\sum_{y<p\le z}w_p/p$.

Use the published 24 upper bands inside exponents $1/3$ through $1/2$, with an $o(1)$ boundary shift; primes below these bands form the lower pool, and primes above $M^{1/2}$ form the high pool. Let $q_i$ be the weighted reciprocal mass in upper band $i$, $q=\sum q_i$, and $\nu$ the corresponding high mass. Let $b,B_Q,B_\nu$ be the sums of $w_p(1-w_p)/p$ over the lower, upper and high pools. The admissible upper-mass cap is $C=0.4055$. Define $D=2\sum_iq_i(\nu-h_i)_+$, the lower bound on the forbidden cross-pair mass supplied by the band endpoints. The constants $h_i$, upper-band capacities and lower-prefix losses in the verifier are exactly the outward rounded integers from the earlier certificate, in units of $1/32000$.

Write $x=(\mu-1)_+$, $m_0=(1-\mu)_+$, $G$ for the published lower bound on the target hinge, and $g=\max(x,G)$. Its split-triple estimate gives $G\ge G_1-B_Q/2$, where $G_1$ is the sum of the pure and the upper/lower mixed contributions computed in the verifier. Set
$$
 Y_0=W-\mu-\frac{1_A-\rho}{1-\rho},\qquad R=E Y_0^2.
$$
Replacing $EW$ by $\mu$ introduces only $o(1)$. The established profile transfer and variance bounds give
$$
 \frac{\Phi}{M}\le\rho+E[1_A(W-\mu)]-(1-\rho)g+o(1),\qquad
 \frac{\Phi}{M}\le\rho+\tfrac12-\tfrac12(1-\rho)\Gamma+o(1),
$$
$$
 \Gamma=m_0+x+\nu^2+D+b+B_Q+B_\nu+2(g-x)+R.
$$
Uniform LP vertex rounding costs at most $\pi(M)=o(M)$ positions. A counterexample sequence with ordinary covering number exceeding $2n$ therefore has optimal dual objectives $\Phi/M\ge2\rho-o(1)$. Passing to a subsequence lets all bounded parameters have limits; inequalities below can equivalently be read in that limit. The ordinary integral statement follows from a fixed strict gamma or dual margin at every terminal box.

## Bernoulli rounding of the high primes

Conditionally on the canonical row, replace each high summand $w_p1_{p\mid m}$ by $\xi_p1_{p\mid m}$, where $\xi_p$ are independent Bernoulli variables of mean $w_p$, independent of the row. Let $W'$ denote the resulting load and $Y=W'-\mu-(1_A-\rho)/(1-\rho)$. Then $E[Y\mid m]=Y_0$, and
$$
 E Y^2=R+E\sum_{p\mid m,\ p\text{ high}}w_p(1-w_p)=R+B_\nu+o(1).
$$
The last discrepancy is $O(\pi(z)/M)=o(1)$. Every retained high label certifies $W'\ge1$ at its row, irrespective of its original price.

Set
$$
 P(D)=q+\nu-q^2/2-q\nu+D/2-\rho,\qquad
 U_\tau=\min\{q(1-q/C),(1-\tau)(C-q)\}.
$$
For each threshold $a=1-\tau$, retain an upper label independently with probability $w_p$ only when its price is at least $a$. A retained upper label certifies $W'\ge a$; it only aids the event bound and does not replace the upper summand in $W'$. Their skipped single-label mass is at most $U_\tau/\tau$. Indeed $w\le w(1-w)/\tau$ and $w\le (1-\tau)(1-w)/\tau$ on skipped labels, with $B_Q\le q(1-q/C)$ by Cauchy. The two-term union bound loses at most $q^2/2+q\nu-D/2$: high-high intersections are impossible, and each other canonical coprime pair has frequency at most $1/(pq)$. Removing all $A$-rows yields
$$
 \Pr(m\notin A,\ W'\ge1-\tau)\ge[P(D)-U_\tau/\tau]_+-o(1).
$$

For $\delta\ge0$, let $c_i(\delta)=(1-\tau_i-\mu+\rho/(1-\rho)+\delta)_+^2$, in ascending threshold order, and take $c_0=0$. Threshold telescoping on the complement gives
$$
 E[1_{A^c}(Y+\delta)^2]\ge
 S_\delta(D):=\sum_i\frac{c_i(\delta)-c_{i-1}(\delta)}{\tau_i}
 [\tau_iP(D)-U_{\tau_i}]_+-o(1).
$$
In particular $R+B_\nu\ge S_0(D)-o(1)$. There is no unit cap on the sum of the threshold coefficients. The randomization has already used the high-price variance, and the union estimate charges no skipped high prices. For an affine support, choose at $D_0\le D$ the positive brackets and use the slope $s=\sum_{i\,\mathrm{chosen}}(c_i(0)-c_{i-1}(0))/2$. The same slope is admissible for $S_\delta$, since every squared positive-part increment is nondecreasing in the shift.

## Conditional mean, target charge and the integer envelope

For a counterexample sequence, profile transfer gives
$$
 E[1_A Y]=E[1_A(W-\mu)]-\rho\ge(1-\rho)g-o(1).
$$
Consequently $E[1_{A^c}Y]\le-(1-\rho)g+o(1)$, since $EY=o(1)$. Cauchy on $A$, followed by expansion of $(Y+\delta)^2$ on its complement, gives the new inequality
$$
 R+B_\nu\ge
 S_\delta(D)+\frac{(1-\rho)^2g^2}{\rho}
 +2\delta(1-\rho)g-\delta^2(1-\rho)-o(1).
$$
It is valid for any certified lower bound on the nonnegative $g$ on the right. The verifier tries shifts $0,.03,.07,.12,.18,.25$.

There is a useful bound on the upper-price variance in boxes where gamma still fails. If $L_0\le m_0+x+\nu^2+D+b$, and $S\le S_0(D)$, then $\Gamma\ge L_0+S+B_Q-o(1)$. Thus it suffices to check
$$
 B_Q\le \min\{q(1-q/C),\ \Gamma_* -L_0-S\},
$$
where $\Gamma_*$ is the strict target value for the box. Substituting this in $G\ge G_1-B_Q/2$ gives a certified $g$ for the conditional inequality and the Schur test. Independently, $B_Q+2(g-x)\ge2(G_1-x)$; this allows the existing coupled source/target bound to use the affine support in $D$ with no upper-price charge.

Finally, for distinct-base pair weight at a canonical row,
$$
 \sum_{p<q} w_p w_q1_{pq\mid m}\ge kW-k(k+1)/2\quad(k=1,2,\ldots).
$$
One proof independently Bernoulli-rounds all summands; each realized integer load $N$ satisfies $\binom N2\ge kN-k(k+1)/2$. On averaging, its pair expectation is the left side. The canonical pair expectation on all rows is at most $(\mu^2-\nu^2-D)/2+o(1)$, and pair weights are nonnegative on $A^c$. Therefore the first profile-transfer inequality also implies
$$
 \frac{\Phi}{M}-2\rho\le
 \rho\big((k-1)/2-\mu\big)+\frac{\mu^2-\nu^2-D}{2k}
 -(1-\rho)g+o(1).
$$
We use $k=1,2,3,4$, with the original unrounded $W$.

## Exact finite verification

Use the accompanying C++17 source. For a band $[a,b]$, the gamma goal is $(1-2a)/(1-a)$, rounded up on the integer grid, plus $16/32000000$. The Schur alternative requires an upper bound at most $-16/32000000$. The initial box coordinates are $\nu,q,|\mu-1|,b,e$, where $e$ is the variance charge on the 16th nested lower-prime prefix. A coordinate above the selected cutoffs for $\nu, |\mu-1|$, or $b$ already attains the gamma goal. The nested target formulas and the greedy minimization over band caps are the earlier split-triple bounds; the new branches follow the formulas above. Each undecided box is split into two closed children covering it. An unresolved minimum-width box returns failure.

Every operation used in a bound rounds outward with integer products or division. Both products in the squared-threshold increments are kept in unscaled squared grid units before subtracting. Only then do we round the incremental weight down; this avoids the error of subtracting two independent lower bounds. For the input domain accepted by the verifier, the lower odds are below .656, offsets below .401, and thresholds at least .05. Every factor passed to scaled product routines has absolute value below 20 grid units, and every raw squared threshold is at most one square grid unit. Products plus rounding offsets are thus bounded by $400(32000000)^2+32000000<2^{63}-1$. Squared-threshold differences are never multiplied before division by the scaled threshold. Costs and sums remain well inside the same bound.

| Density band | High-mean boxes | Low-mean boxes | High-mean Schur leaves | Low-mean Schur leaves |
|---|---:|---:|---:|---:|
| [.3950,.3960] | 5,339,905 | 453,047 | 28,095 | 5,046 |
| [.3930,.3950] | 51,990,865 | 1,010,339 | 52,506 | 9,170 |

Compile with `c++ -std=c++17 -O3 verify_density.cpp -o verify_density`. For each band run `./verify_density lo hi 0` and `./verify_density lo hi 1`, writing the endpoints in units of $1/10000$. The proof only uses wholly accepted bands together with the earlier theorem from .3960 upward.

The low-mean subproblem alone also passed on [.3900,.3930] in 8,085,999 boxes. The high-mean test on [.3900,.3930] stopped on an unresolved box after 215,949,546 nodes. The integer endpoint pairs for that box, in the displayed coordinate order and units of 1/32000000, are (4807926,4808000), (12569609,12569708), (1008620,1008709), (7573692,7573781), (4897915,4898003). The box describes the limits of these inequalities and supplies no counterexample to the covering conjecture.
