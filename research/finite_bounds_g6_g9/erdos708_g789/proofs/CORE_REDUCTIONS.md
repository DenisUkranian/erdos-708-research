# Small-n core reductions for the Erdős–Surányi covering problem

Research note, 24 November 2026. These statements are deductions made in the current investigation; they do not prove the requested exact values.

Let A be a set of n distinct integers at least 2, M=max A, and I an interval of M consecutive positive integers. Write P(A)=product(A), and let tau(A,I) be the smallest size of a subset of I whose product is divisible by P(A). Throughout, an already established bound g(k)<=b_k can be applied to a k-element subset using a suitable subinterval of I. The universal divisibility P(A) | M! | product(I) will be used repeatedly.

## 1. Prime units can be repaired individually

If a selected set B already covers P(A)/p for a prime p, either it covers P(A), or an unselected member of I divisible by p exists. Indeed, if all p-divisible members were already selected, the p-valuation of product(B) would be at least the p-valuation of P(A). Adding one such member repairs the deficiency.

More generally, if the missing prime-valuation total is at most E, successive additions repair it in at most E picks. This observation is valid because the complete interval covers all source prime valuations.

## 2. Two-source peeling

Suppose distinct a,b in A are divisible by primes p,q, respectively. Let r be a valid upper bound for covering A minus {a,b}. If

    p >= r+1,   q >= r+2,   pq <= M/(r+3),

then tau(A,I)<=r+3.

Proof: cover the remaining sources with at most r points. Since a/p<=M/p, the interval contains at least p>=r+1 multiples of a/p, so append a fresh one. Append a fresh multiple of b/q in the same way. The selected product now covers P(A)/(pq). Finally, pq has at least r+3 multiples in I, so a fresh multiple completes the cover. This also works for p=q and for source prime powers: only one occurrence of p and one occurrence of q are removed.

## 3. Elimination by the number of sources containing a prime

Suppose p divides exactly d sources, 1<=d<n. Let r be a valid bound for g(n-d), and put U=r+2d-1. If p>=U, then tau(A,I)<=U.

Write those d sources as a_i=p^{e_i}c_i with p not dividing c_i. Cover the p-free remaining sources with a set B of at most r points. Choose a source a_* having maximum e_i, and choose any multiple z of a_* in I.

There are at least d distinct interval points, one for each required prime-power occurrence, whose product covers p^{sum e_i}, and they can be chosen to include z. To see this, order the e_i decreasingly and match p^{e_i} to an interval multiple. For each exponent e, the number of source a_i divisible by p^e is at most floor(M/p^e), while I has at least that many multiples. Fixing z for one of the maximum exponents preserves each remaining counting inequality. Descending greedy matching therefore works.

Call this p-supply set C; |C|<=d. If z is not in B, B union C covers both the old source product and c_*, as well as the entire p-demand. Append fresh multiples of the other d-1 cofactors. If z is in B, C adds at most d-1 points; append all d cofactors. In either case the total is at most r+2d-1. Each required cofactor has at least p>=U multiples in I, so the fresh choices are available.

The use of a p-free old source product is essential: the p-demand of the removed sources can be supplied by C even when C intersects B.

## 4. An additional gain from one prime square

Suppose p divides exactly d sources, d>=3, and every such source has p-valuation exactly 1. Let r bound g(n-d), and put V=r+2d-2. If

    p >= V   and   p^2 <= M,

then tau(A,I)<=V.

Use B and z as above. The p-demand is now p^d. It can be supplied by a set C of d-1 points that includes z:

* If p^2 divides z, add d-2 other p-multiples.
* Otherwise, choose a p^2-multiple w (necessarily different from z) and add d-3 other p-multiples.

There are sufficiently many ordinary p-multiples because floor(M/p)>=p>=V>=d-1. The same two cases z outside/inside B now cost r+(d-1)+(d-1) or r+(d-2)+d, both V. Fresh cofactor multiples are available because p>=V.

This statement requires d>=3. The displayed construction is not a proof for d=2.

## 5. Concrete consequences for possible counterexamples

All conclusions in this section are conditional on the listed preceding bounds. A counterexample here means a particular (A,I) with tau exceeding the proposed target, not an assertion that such a counterexample exists.

### Target g(7)<=9

Assume g(6)<=8, g(5)<=6, g(4)<=5. Every prime p>=11 in a counterexample must divide at least 3 sources: support 1 or 2 is eliminated by Section 3. Applying Section 2 to two sources divisible by p shows p^2>M/9. Any three such prime occurrences, including repetitions, have product greater than 11*(M/9)>M: two of the primes have product greater than M/9 and the third is at least 11. Thus each source contains at most two of them, for every M, and there are at most floor(14/3)=4 distinct active primes >=11.

If such a prime divides exactly 3 sources to exponent 1, Section 4 additionally forces p^2>M. Section 6A below eliminates the four-prime residue. Therefore a counterexample to g(7)<=9 has at most THREE distinct active primes >=11, for every M.

### Target g(8)<=11: at most three large primes

Assume g(7)<=10, g(6)<=8, g(5)<=6, g(4)<=5. Every prime p>=11 in a counterexample divides at least 4 sources: support d=1,2,3 gives respectively the bounds 10+1, 8+3, 6+5, all at most 11. Section 2 gives p^2>M/11.

Each source contains at most two prime occurrences from this large-prime set, for every M: a product of three is greater than (M/11)*11=M. There can be at most four large primes. If there were exactly four, all incidence inequalities would be equalities: every source would contain two different large primes, each large prime would occur in exactly four sources, and its valuation in those sources would be 1. Section 4, with d=4 and r=5, would eliminate every such prime with p^2<=M. Hence all four primes would exceed sqrt(M), making a product of two of them greater than M. This contradicts the forced form of every source.

Therefore, for every M, a counterexample to the target g(8)<=11 has at most THREE distinct active primes >=11. Each has source support at least 4 and exceeds sqrt(M/11). All remaining factors are composed of 2,3,5,7.

### Target g(9)<=13

Assume g(8)<=12, g(7)<=10, g(6)<=8, g(5)<=6. Every prime p>=13 in a counterexample divides at least 5 sources: support d=1,2,3,4 gives 12+1, 10+3, 8+5, 6+7, all at most 13. Section 2 gives p^2>M/13. Each source has at most two large-prime occurrences for every M, because a product of three is greater than (M/13)*13=M. Thus at most floor(18/5)=3 active primes >=13 remain. The other factors are 11-smooth.

## 6. A three-prime core can be covered with at most one extra pick

Let S consist of at most three primes. Assume every source's full S-part has degree at most two: it is 1, p, p^2, or pq for p,q in S. Let m be the number of sources with nontrivial S-part. If S={p,q,r}, additionally assume pqr>M. Then the entire S-demand can be covered by at most m+1 interval points. If |S|<=2, m points suffice. The selected set can be required to contain an arbitrary prescribed multiple z of any one full source with nontrivial S-part in I. A source with S-part 1 is excluded from this prescribed-point clause.

Proof. For every nontrivial core d, group the sources whose S-part equals d. If there are m_d sources in that group, distinctness of the sources implies m_d<=floor(M/d). Choose m_d distinct multiples of d in I. For a prescribed z, choose its core's group to include z. Call these chosen sets the core groups. Their cardinalities sum to m, but their union may be smaller because a point belongs to several groups.

At a point b in the union, let k_b be the number of groups using it. The assigned core types form a simple graph on the primes that occur there, together with loops p^2 and singleton types p. Let e_b be the number of ordinary edges pq and v_b the number of vertices present; let l_b and s_b be the numbers of loops and singleton types. Thus k_b=e_b+l_b+s_b. The total assigned prime valuation is 2e_b+2l_b+s_b. The actual point has at least one unit for every present vertex and an additional unit for each loop, so its assigned valuation deficit is at most

    delta_b <= 2e_b+l_b+s_b-v_b.

Consequently

    1 + delta_b - k_b <= 1 + e_b - v_b.

For a simple graph on at most three vertices, the right side is positive only if all three triangle edges pq,pr,qr are present, and then it is 1. Such a point must be a multiple of pqr, and there is at most one in I because pqr>M. The union's size plus the sum of all prime-unit deficits is therefore at most m+1 (or m when there are at most two vertices). Section 1 repairs the deficits within that budget.

The full-source cofactor at the prescribed point is coprime to S. It remains supplied after these repairs, so it may be removed from the subsequent small-prime product that still needs covering.

## 6A. Elimination of the four-large-prime case for g(7)<=9

Assume the preceding small-n bounds in Section 5. Suppose, towards a contradiction, that a seven-source counterexample to the bound 9 has four active primes at least 11. Call a prime low if p<=sqrt(M), and high otherwise. Every high prime has total source valuation at least 3. Every low prime has total source valuation at least 4: its source support is at least 3, and if its total valuation were exactly 3, all three occurrences would have exponent 1 and Section 4 would close the instance in 9 picks.

The total valuation at the four primes is at most 14, because each source has at most two occurrences. If there are l low primes, this gives 12+l<=14 and hence l<=2. There cannot be three or four high primes: each high prime occurs in at least three sources, whereas each source contains at most one high prime. Thus l=2. All bounds are equalities: the two low primes p1,p2 have demand 4 each, the two high primes q1,q2 have demand 3 each, and every source has exactly two large-prime occurrences.

Six sources contain a high prime, so they have cross cores p_i*q_j. The seventh core is either p1*p2, p1^2, or p2^2. Because p_i>sqrt(M)/3 and q_j>sqrt(M), every cross core exceeds M/3. Its source cofactor is therefore either 1 or 2, and a particular cross core occurs at most twice (the source integers are distinct).

If the seventh core is the edge p1*p2, cross degrees are 3 at each of the four vertices. Thus, after relabeling, the cross multiplicity matrix is

    [[1,2], [2,1]].

If the seventh core is a loop, cross degrees at the two low vertices are 2 and 4, and the high degrees are 3 and 3. The only possible matrix, up to relabeling, is

    [[1,1], [2,2]].

In both cases the product of the six cross cofactors is at most 16. At least one cross core occurs twice, so its two source cofactors are exactly 1 and 2.

### Covering the large core in at most 8 picks

Use the core-group selection and the pointwise deficit calculation from Section 6. Force one selected point to be a multiple of a full source with cross cofactor 2.

In the loop case, the ordinary graph is K(2,2). Its only positive value of 1+e_b-v_b is 1, arising when all four cross types meet at the point. There is at most one such point in I, since it is divisible by p1*p2*q1*q2>M. Thus the large-prime demand is covered in at most 7+1=8 picks.

In the edge case, the ordinary graph is K(2,2) plus the low edge p1*p2. Positive cycle contributions can arise from a triangle, the four-cycle, or the full five-edge graph. Two distinct triangle points would both have to belong to the low-edge group, which has only one selected member. A triangle point and a distinct four-cycle point are also impossible: the relevant high vertex has a cross group of multiplicity 1, which both points would need. Thus all positive cycle contributions occur at at most one point. A contribution of at most 1 again gives 8 picks.

The only remaining case is a contribution of 2, so all five core types meet at one point z. The two cross groups of multiplicity 2 contribute at most two other selected points, hence the union has at most three points. Each prime has at least two supplied valuation units: one at z and one at the extra point of its incident multiplicity-2 group, which is distinct from z. Its baseline valuation deficiencies are therefore at most 2,2,1,1 at p1,p2,q1,q2, respectively. Each low prime p_i satisfies p_i^2<=M. If a multiple of p_i^2 is already in the union, it supplies at least one unit beyond this two-unit baseline and the actual deficiency is at most 1. Otherwise, append a square multiple to cover its at-most-two-unit deficiency in one pick. Thus each low prime requires at most one additional pick; each high prime also requires at most one, with a fresh multiple guaranteed by divisibility of the full interval product. The total is at most 3+4=7. This proves the required at-most-eight core bound in every case, including the prescribed full-source point.

### Covering the remaining small factors

Write the seventh source as d0*s0, where d0 is its low-edge or loop core. Then d0>=11^2=121. The product Q of all small cofactors is at most 16*s0. The forced selected point already supplies one factor 2, so only Q/2 remains to be supplied. It satisfies

    Q/2 <= 8*s0 <= 8M/d0 <= 8M/121 < M/9.

There are therefore at least 9 interval multiples of Q/2. After the at-most-eight-point core cover, one fresh multiple completes the full source product in at most 9 picks. If Q/2=1, no additional factor is required. This contradiction eliminates the four-large-prime case for every M.

## 7. What these reductions do not establish

The three-prime core theorem covers only the selected large-prime valuations. It does not cover all the remaining small-prime factors for free, and reusing a selected point for their demands can double-count its valuation. A final proof must supply a rigorous allocation or disjoint repair for those factors, uniformly in M and the shift. The reductions above therefore do not prove g(7)=9, g(8)=11, or g(9)=12/13.

## 8. Audit of a previously cited small-n paper

The Bergström preprint at DOI 10.5281/zenodo.24366897 claims g(6)=8 and supplies valid lower witnesses for 7 and 8. Its printed proof is not a safe independent justification of the upper bound: page 7, Subcase 3a, asserts that P1*P2>M implies no interval member is divisible by P1*P2. A shifted interval can contain such a multiple. In Subcase 3b it also asserts that repeat demand for a prime can occur only below sqrt(M), which fails when a prime above sqrt(M) divides several distinct sources. The elementary cumulative-GCD slot theorem stated earlier in that paper is valid. None of the present deductions relies on the faulty large-M passage; the bounds used in Section 5 must be verified separately.
