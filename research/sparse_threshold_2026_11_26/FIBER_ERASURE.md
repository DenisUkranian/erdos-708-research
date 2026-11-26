# Actual ordinary gap inheritance on deletion of unit-priced prime fibers

Let J=[1,M], I any positive interval of M consecutive integers, h(x)=(x-1)_+. Write
$$
\Phi(A,w)=\sum_{a\in A}X_w(a)-\sum_{b\in I}h(X_w(b)),\qquad
X_w(j)=\sum_{q\le M}w_qv_q(j),\quad 0\le w_q\le1 .
$$
Suppose the initial reciprocal mass $\sum_q w_q/(q-1)$ is bounded by a fixed constant B. Let P be any ordered list of distinct primes exceeding $y=y(M)\to\infty$, of prices $w_p=1-o(1)$ uniformly. Just before deleting a prime p, write $u_q$ for the then-current prices on the other primes (all previously deleted prices are zero). Assume that
$$
 \mu_p=\sum_{q\ne p,\;q\le M/p}u_q/(q-1)\le 1+o(1)
$$
uniformly in the list. Remove all rows hit by a prime in P, producing R, and set all prices on P to zero, producing v. Uniformly in every such choice and all shifts,
$$
  \Phi(R,v)-2|R|\ \ge\ \Phi(A,w)-2|A|-o(M).
$$
Thus a true ordinary gap at positive density passes to the complementary source whenever an optimal ordinary price witness has these properties. The reduction incurs neither an assumption on the occupied target sites nor any pairwise disjointness of target fibers.

**One step.** Ignore repeat occurrences of the removed root in its assigned source rows. Their total over the entire sequence is $O(M\sum_{p>y}1/[p(p-1)])=o(M)$. With $X_0$ the load on remaining primes, removal of the source part costs at most $\sum_{a\le M,\;p|a}(X_0(a)-1)_+$ above the budget two per removed row. This extends the sum to all p-multiples, irrespective of earlier source removals. On the target, changing the root price from 1 to 0 on p-multiples yields a rebate at least $h(X_0+1)-h(X_0)=\min(X_0,1)$; higher powers only increase the rebate. Starting instead from $w_p=1-\xi_p$ reduces this lower bound by at most $\xi_p$ per target p-multiple because h is 1-Lipschitz (one uses only one root incidence on the target). The total losses here are o(M) since $\sum_{p\in P}1/p\le 2B$ and $\pi(M)=o(M)$. The exact sequence of target rebates telescopes even when all the underlying target fibers overlap.

**Cofactor comparison.** Put $L=M/p$. In the cofactor quotient split eligible other primes q at $\sqrt L$ into cheap and expensive, omitting all $q>L$. These omitted primes have zero canonical contribution and may be ignored on the target. For an independent geometric variable $G_q$ with $\Pr(G_q\ge j)=q^{-j}$, put
$$
 \mu_q=u_q/(q-1),\quad m_q=E\min(u_q G_q,1),\quad D_q=\mu_q-m_q .
$$
Write $m=\sum m_q,\ D=\sum D_q,\ b=\sum_{q\text{ cheap}}m_q$. For an actual cofactor t write $c_q=\min(u_q v_q(t),1)$. The source positive part is at most the sum of individual excesses $(u_q v_q(t)-1)_+$ plus $\sum_{q<r}c_qc_r$. This follows by independent Bernoulli marking of event probabilities $c_q$, Jensen, and $(k-1)_+\le {k\choose2}$ for integers. Two expensive distinct primes cannot co-occur in the canonical quotient. Divisibility expansion with nonnegative coefficients, followed by canonical floor upper bounds, gives a normalized canonical upper bound
$$
 D+\tfrac12[b^2-\sum_{\rm cheap}m_q^2]+b(m-b).
$$
The target truncated cap dominates $\sum_{\rm cheap}c_q-\sum_{q<r\ {\rm cheap}}c_qc_r$, by the Bernoulli union bound and first Bonferroni correction. The corresponding normalized lower bound after aggregate remainder has main term $b-\tfrac12[b^2-\sum_{\rm cheap}m_q^2]$. Consequently the net normalized bound is
$$
 D+b(m-1)-\sum_{\rm cheap}m_q^2 .
$$
Since $\min(1,ku_q)\ge1-(1-u_q)^k$, the geometric generating function gives $m_q\ge\mu_q/(1+\mu_q)$ and $D_q\le m_q^2/(1-m_q)$. The expensive-prime sum of $D_q$ tends uniformly to zero for $L\to\infty$, as $D_q\le 1/[q(q-1)]$. Since $m+D\le 1+o(1)$, $b\le1+o(1)$, and $b$ is bounded, the last bound is at most $(1-b)D-\sum_{\rm cheap}m_q^2+o(1)\le o(1)$; if $b\ge1$ the last sign is immediate, otherwise use $m_q\le b$ for cheap q.

**Arithmetic errors.** Fix $u>0$ and restrict first to $p\le M^{1-u}$, so $L\ge M^u$. For larger p the source positive part is bounded by full cofactor load with total at most $\sum_p (M/p)B=O(BuM)+o(M)$ by the reciprocal prime estimate; no target lower bound is then needed. Fix $T,K$. In the target Bonferroni expression retain the first level only for $q>T$, and cap valuation at K for the finite set of primes $q\le T$. Each cap is a sum of nested divisibility indicators with nonnegative coefficients, each coefficient at most the corresponding price. The sum of removed geometric first-moment contributions is $O(1/T+\sum_{q\le T}q^{-K}/(q-1))$; the Bonferroni polynomial in the means changes by this error times $O_B(1)$. For large M all retained powers on the fixed small bases are below $\sqrt L$. All counting moduli $d=pq^i$ or $p q^i r^j$ in the target lower bound are now at most M. They involve at most three distinct primes, and each occurs a bounded number of times across the sequence, with bounded coefficients (even though current prices, order, cutoffs, and coefficients can depend on p). The total count error is $O_{T,K,B}(M/\log M+M^{9/10})=o(M)$ for all such terms with at least one macroscopic prime $\ge M^{1/40}$, by fixing all other factors and counting primes $\ll M/(e\log M)$, summed with their weights; the aggregate reciprocal weight over those fixed factors is $O_{B,T,K}(1)$. Here the removed label p has weight one in the summation, with $\sum_{p\in P}1/p\le2B$; other factor weights are bounded by their initial prices, whose reciprocal sum is bounded. If there is no macroscopic prime the factor from the finitely many small higher powers is $O_{T,K}(1)$ and all counting moduli are $O_{T,K}(M^{3/40})$. Ties in assigning the distinguished macro prime give multiplicity at most three. These arguments use the uniform interval count error at most one for each term. Send M to infinity, next $T,K$ to infinity, then $u\to0$; multiply the per-fiber geometric tail by $\sum_{p\in P}1/p\le2B$. The proof is complete.

## Fractional root deletion with a source-density rebate

There is a more general quantitative version. The prescribed roots in P can have arbitrary prices $w_p\in[0,1]$. Assume directly $\sum_{p\in P}1/p=O(1)$, keep the same bounded initial priced mass B, and still take $\min P\to\infty$. In the order of removal write $N_p$ for the number of current source rows hit by p, and $d_p=pN_p/M$. Use $b_p=b$ and $\mu_p=m+D$ from the preceding proof, always using the other, still-active prices. Without any upper threshold on $\mu_p$, the total loss of excess above two is at most
$$
 \big[\Phi(A,w)-2|A|\big]-\big[\Phi(R,v)-2|R|\big]
 \ \le\ M\sum_{p\in P}{(1-w_p)(1-d_p)+b_p(\mu_p-1)\over p}+o(M).
$$
In particular any ordering with a nonpositive aggregate right-hand score gives actual gap inheritance at positive density, for an optimum witness as above. The source fractions are those at their removal step; they partition the discarded rows without repeating their memberships. No hypothesis about target overlaps is needed.

Indeed, up to the already bounded repeated root powers, the net source contribution is at most $\sum_{p|a,a\le M}(X_0(a)-1)_+-(1-w_p)N_p$. The exact target rebate is at least $\min(1,X_0(b))-(1-w_p)$ per multiple. This leaves the stated $(1-w_p)(1-d_p)$ term and total $O(\pi(M))$ endpoint error. In the other part the algebraic remainder after subtracting $b(\mu_p-1)$ is $(1-b)D-\sum_{\rm cheap}m_q^2$, which is nonpositive up to the vanishing expensive-prime tail by the geometric inequality, for any b. For p very close to M the main score in absolute value is bounded in terms of B, and dropping this final prime range still costs $O_B(uM)+o(M)$ as before. The previous aggregate arithmetic argument applies since unweighted reciprocal mass of the removed primes is now an explicit hypothesis.
