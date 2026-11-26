# A shift-uniform matching bound and a test for the remaining cases

Use positive intervals; reflection and the zero case handle other intervals. An atom of a source is the full power of one prime in its factorization. Write $r(a)=\omega(a)$ for the number of these atoms. For $a\in A,b\in I$ let $s(a,b)$ count the atoms of $a$ dividing $b$. Give the edge $(a,b)$ weight $(s(a,b)-1)_+$. Write $W$ for the maximum weight of a bipartite matching. Then
$$\tau(A,I)\le H(A,I)\le \sum_{a\in A}r(a)-W.$$
Here $H$ is the stronger cover satisfying every prime-power count. To prove the bound, keep only positive edges of an optimal matching and select their target positions. Attribute the full shared atoms of each matched source to its position. At any level $p^j$ the resulting shortfall is at most the number of unattributed source atoms based at $p$, since attributed positions are distinct. For each $p$, add as many of the largest remaining $p$-valuations as the maximum positive shortfall over its levels. The level sets are nested and the full interval supplies each required count. The union costs at most one point per unattributed atom. The matching costs one point per positive edge, giving the inequality. This uses the nested-level repair argument in redlydi's report. The bound gives credit for any number of shared atoms without preassigning a split. Maximizing the weight is an ordinary integer assignment problem.

## A sufficient class with a small set of exceptional primes

Let $P$ be any set of $k\ge1$ primes at most $M$, with $e_p=\lfloor\log_p M\rfloor$. Record the vector $t_p(u)=\min(v_p(u),e_p)$ for $p\in P$. Put
$$D_P=\prod_{p\in P}(2e_p+1),\qquad R_P=\sum_{a\in A}\#\{p\mid a:p\notin P\}.$$
Then $H\le n+R_P+(k-1)\min(n,D_P)$ for every shift.

**Proof.** Within each exact profile, inject as many sources as possible into distinct target positions of the same profile. Compare the counts in $[1,M]$ and in $I$. For a profile $t$, inclusion-exclusion tests exactness in the coordinates $t_p<e_p$ using at most $2^{\#\{p:t_p<e_p\}}$ divisor counts. Each count changes by at most one between the two intervals, even for divisors exceeding $M$. Summing this discrepancy bound over all profiles gives $D_P$. Since $A\subseteq[1,M]$, at most $u\le\min(n,D_P)$ sources are unmatched. The $n-u$ selected points meet every core atom of their matched sources. The nested-level repair above consequently costs at most $ku+R_P$. This proves the bound, including $k=1$. A sharper instance bound uses the actual positive profile deficits against the shift.

For polynomial $M$ in $n$, $k=o(\log n/\log\log n)$ gives $kD_P=n^{o(1)}$ for nonempty $P$. Thus $R_P\le n+o(n)$ suffices for coefficient two. Multiplicities within or outside the core can be arbitrarily large. This is a sufficient class and a direct integer argument. No priority claim is made.

## Experiment and proof target

For a putative bad instance compute $W$ and the full-interval cover as competing upper bounds. A proof that $W\ge\sum_a(r(a)-2)-o(n)$ uniformly in the still-open region would suffice. Equivalently, by weighted bipartite matching duality, every feasible nonnegative system $u_a+v_b\ge(s(a,b)-1)_+$ must have total price at least that right-hand side. A low-price cover certifies failure of this matching method on an instance. It does not lower-bound $\tau$. Test adversarial shifts formed by CRT and examine which atom sets share the scarce positions. If a subset of the positions carries disjoint atoms from different sources, allowing joint payment there can outperform the matching. A uniform proof must handle $n/M\to0$ as well as each fixed density. An error $o(M)$ is insufficient along sparse sequences.

## A nested Hall target with an exact deficit formula

For each source with at least three atoms allow all choices of one atom to omit. Its neighborhood is the union of the multiples, in the target interval, of the remaining cofactors. For each integer j ≥ 3 let A_j be the sources with at least j atoms. Put d_j = max over S ⊆ A_j of (|S| − |N(S)|), including the empty set. Then for every instance

    H(A,I) ≤ 2n − #{a : r(a) = 1} + sum_{j≥3} d_j.

Indeed a matched source costs at most two positions in the accounting above, saving r(a)−2 relative to the completely separate atom budget. Matchable source subsets form a transversal matroid. Process sources in descending r order, retaining a row exactly when it can be added while preserving matchability (augmenting paths may reassign previously matched rows). At the end of each rank prefix the retained rows form a maximal independent subset of that prefix, hence a maximum-cardinality matchable subset. The number retained from A_j is |A_j|−d_j by the deficiency form of Hall's theorem. Summing prefix sizes counts each retained source r(a)−2 times and gives the displayed bound. Distinct positions are used once across all prefixes. In particular the formula measures the cost of unmatched rows with many atoms.

**Finite test.** The accompanying program computes one matching simultaneously for *every* source up to the indicated M with three or more distinct prime factors. At M = 512, 2,048, 8,192 and 32,768, all 122, 728, 3,688 and 17,073 rows respectively matched for each of three shifts: x=M, x=10^24+271, and a window centered near the product of the primes below 150. The script checks each edge by integer division and all selected offsets for distinctness. Each of those 12 windows therefore admits at most 2|A| positions for every source subset with that maximum, because rank-one and rank-two sources can be repaired separately. These are finite checks at fixed shifts. The missing estimate is uniform over every shift and over input sizes, including n/M tending to zero. A macroscopic deficiency would refute this particular sufficient condition; the weighted matching and shared-position constructions could still succeed.

## Compressing the obstruction to one price function

For a target set T write C_j(T) for the number of rows a in A_j whose **entire** cofactor neighborhood is contained in T. Hall deficiency is equivalently max_T (C_j(T)−|T|): take T=N(S) in one direction and all rows trapped in T in the other. There are maximizing sets nested as T_3 ⊇ T_4 ⊇ ... . Indeed the indicator of N(a) ⊆ T is supermodular in T, and contributions from extra rows at the lower rank are increasing. Hence for i<j the sum of the objectives at T,S is at most the sum at T∪S,T∩S respectively. Taking T to be the largest maximizing set at level i forces S ⊆ T for any maximizer at level j. Largest maximizers exist by the same union argument at a single level.

Equivalently let h(a)=(r(a)−2)_+. The total deficit has the single exact expression

    max_z  [ sum_{a : h(a)>0} min(h(a), min_{b in N(a)} z(b)) − sum_{b in I} z(b) ],

where z is nonnegative integer-valued and bounded by max h. Expand into superlevel sets to get the upper bound, and use the nested optimizing sets to attain it. Thus a sufficient analytic target is to bound this expression by o(n) uniformly. The target prices here count Hall obstructions and differ from the prime prices in the valuation relaxation.

**Arithmetic test for trapped rows.** In any complete period of length a, the union of the multiples of a/q, over the full prime-power atoms q of a, has exactly 1+sum(q−1) positions. Each pair of distinct cofactors has lcm a. Therefore if N(a) is trapped in a set of size t, then

    floor(M/a) [1 + sum_{q atom of a}(q−1)] ≤ t.

Separately each cofactor bank must be trapped in full. This gives a shift-independent screen on every superlevel of z, including repeated prime powers; a proof must still control the union of the surviving banks. A single paid position is shared across ranks exactly as specified by z.
