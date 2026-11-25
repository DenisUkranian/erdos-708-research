# Erdős–Surányi 708: at most two primes ≥13 in a nine-source obstruction

**Status:** a new structural reduction, conditional on the preceding bounds `g(4)≤5, g(5)≤6, g(6)≤8, g(7)≤9, g(8)≤11`. It is not a proof of `g(9)=12`. No smooth-source enumeration or large-M cutoff is assumed in this theorem.

Let A be nine distinct integers ≥2, M=max A, and I an interval of M consecutive positive integers. Write τ(A,I) for the minimum number of distinct interval elements whose product contains ∏A. Suppose τ(A,I)>12. Every upper bound for fewer distinct sources applies in I by choosing a subinterval of the required length.

## 1. Three elementary cover operations

* If k selected points cover D, and h≤M with (k+1)gcd(D,h)≤M, a fresh multiple of h can be used if available. Otherwise the existing product contains lcm(D,h), and a fresh multiple of gcd(D,h) supplies D h. A prime h can also be appended in one point without the gcd size condition: if the needed prime unit is missing, some multiple is still unused, since ∏A divides M! and hence the product of I.
* For a prime p dividing d sources, write those sources p^{e_i}u_i with p not dividing u_i. There are at least d distinct multiples of p in I. More generally the number of sources divisible by p^j is at most floor(M/p^j), so one can select d distinct p-carriers whose total p-valuation is at least sum e_i. One may prescribe a carrier w divisible by a designated full source: match the remaining exponent demands to distinct multiples, or choose the highest valuations among remaining positions. If the designated exponent is not maximal, the matching still works: for any level j, a prescribed w either serves one of the demands at that level or it is removed from the available pool at the cost of one; in the latter case w has valuation ≥ its own demand but below j, so no eligible point is lost. In particular, all applications below with exponents at most 2 are immediate from the counts of p and p² multiples.
* **Independent carrier lemma.** Cover the p-free sources in r positions B. Select k p-carriers C containing a full-source multiple w of an anchor p^{e_a}u_a, with total p-valuation ≥sum e_i. Suppose the other cofactors are partitioned into b products h_j (unit cofactors can be omitted) with (r+1+j)h_j≤M for j=1,...,b. Assume floor(M/u_a)≥r+1. If w is not in B, include it in the small-cofactor cover. If w is in B, choose a fresh multiple of u_a outside B instead. In either case the small-cofactor cover now uses ≤r+1 positions; then choose h_j multiples fresh relative only to this cover. Take the union with C. These new cofactor positions need not avoid C, because the p-demand is independent of all p-free demands. The union uses at most r+k+b positions: if w was new it is already counted in C; if w was in B its overlap pays for the extra cofactor point. This proves a uniform all-shift certificate with smaller bundle capacities than requiring freshness relative to all carriers.

## 2. Preliminary restrictions on primes p≥13

**Support at least three.** If p occurs in just one source a, cover the other eight by 11 points and append a by the gcd rule: gcd(a,D)≤M/p. If p occurs in exactly two sources, cover the other seven in nine points; select two p-carriers containing a full-source multiple of one of the two. The carriers can be matched to their source exponents by the preceding counting argument. The other cofactor is supplied in a fresh position relative to the p-free cover and the anchor, with the same intersection accounting as in the independent carrier lemma. Cost ≤9+2+1=12. Thus every active p≥13 has support d≥3.

**Pair deletion.** If 12p²≤M, cover seven sources after removing two p-sources a,b in nine points, then append fresh multiples of a/p,b/p,p² in positions 10,11,12. Since p≥13, all three capacity inequalities hold. Thus 12p²>M.

**At most two large factors per source.** For M<13³ this is immediate; for M≥13³, any three large prime occurrences have product >(M/12)^{3/2}>M. Each large part therefore has form 1,p,p²,pq, and no more than 18 large prime occurrences exist in total.

## 3. New saturation inequality

Let d be the support of p, s the number of sources with exponent two, D=d+s, and C=floor(M/p²). Choose two p-sources with the largest exponents e,f. Cover the other seven sources in nine points. If there is a fresh multiple of p², append it. If none exists, the old product already contains at least 2C p-units. Hence if 2C≥D-e-f+2, the old product (or its extension by the fresh square) covers the required product of the other seven sources times p². Then append fresh multiples of a/p and b/p, giving ≤12 positions. Consequently every obstruction satisfies

    2C < D-e-f+2,
    C ≤ floor((D-min(2,s)-1)/2).

Also C≥s by distinctness of the squared sources. All these inequalities are exact integers.

## 4. Every low large prime has support at least five

Call p low if p≥13 and p²≤M, and high if p²>M. For d=3 or 4, the saturation bound excludes s≥2. If s=0, choose d−1 p-carriers including a full-source anchor and at least one square multiple. This is possible: if the anchor is not square, choose a square separately; d−1≥2 and there are at least d p-multiples. These carriers supply d p-units. Supply the d−1 non-anchor cofactors individually. The independent carrier lemma gives cost g(9−d)+2d−2=12. The capacities hold since each cofactor ≤M/p and the small-cofactor cover never exceeds 12 points.

If s=1, the saturation bound forces C=1. The squared source is therefore exactly p², with cofactor 1. Choose a non-square source as anchor and d p-carriers, including the guaranteed square multiple, which supply d+1 p-units. Omit the unit cofactor and supply the d−2 other cofactors individually. Again cost g(9−d)+2d−2=12. Thus all low primes have d≥5.

## 5. Stronger bound at support five

If a low p has d=5,s=0 and C≥2, choose three p-carriers including a full-source anchor and two square multiples. These supply five p-units. The other four cofactors are supplied individually after covering the four p-free sources in five points. Cost 5+3+4=12. Thus C≤1.

If d=5,s=1 and C≥2, saturation forces C=2, so 2p²≤M<3p². Choose an anchor among the four non-square sources other than the one with smallest cofactor u. Four p-carriers including that anchor and two squares supply six p-units. The single square source has cofactor w≤2. Combine w with u into one bundle, and keep the other two non-anchor non-square cofactors as single bundles. The first bundle fits 7wu≤M. Indeed, for p≥17, 7wu≤14M/p≤M. If p=13, the four distinct non-square cofactors imply u≤floor(M/13)−3≤M/13−3. Hence 7wu≤14M/13−42≤M since M<507<546. The remaining singleton bundles satisfy 8h≤M and 9h≤M. Apply the independent carrier lemma with r=5,k=4,b=3. Cost 12. Thus for d=5 and s≤1 one always has C≤1 in an obstruction.

## 6. No five or more large primes

If v is the number of distinct active large primes and l the number of low ones, at least 3v+2l occurrences are required. In addition, high primes cannot share a source because their product exceeds M, so 3(v−l)≤9. Together with at most 18 occurrences these inequalities exclude v≥5: for v=5 they require l≤1 and l≥2; for v=6 they require l=0 and l≥3; v>6 already violates the occurrence bound.

## 7. Abstract type enumeration for v=3,4

Number low vertices first and high vertices last. Enumerate every multiset of nine large-part types from 1,p,p²,pq. A squared type requires a low vertex; a two-distinct-prime type requires at least one low vertex. For each type multiset obtain d_i,s_i,D_i and the upper bound C_i above, with C_i=0 for high vertices. Reject if supports are too small or if C_i<max(1,s_i) for low vertices. Apply the strengthened C_i≤1 when d_i=5,s_i≤1.

The number of distinct sources with large part p_i² is ≤C_i. The number with large part p_i p_j is ≤floor(M/(p_i p_j)). Since p_i²>M/(C_i+1) and p_j²>M/(C_j+1), this number is at most isqrt((C_i+1)(C_j+1)−1). These constraints are necessary even though the upper bounds C_i may overestimate the true counts. They therefore safely overenumerate all possible source types.

`verify_structures.py` enumerates all these multisets (not sampled interval shifts). Exactly nine patterns with v=3 survive, and zero with v=4.

## 8. Three-source compression rule for high primes

Let a high p with p²>M divide exactly three sources p u_1,p u_2,p u_3. The u_i are distinct and ≤M/p<sqrt(M), and each pair product u_i u_j≤M. All source primes themselves can be excluded from an obstruction by g(8) and one prime repair, so u_i≥2.

Let A_0 be the six p-free sources. If some pair product h=u_i u_j is not in A_0, cover the seven distinct sources A_0∪{h} in nine positions via g(7). Select three p-carriers including a full multiple of the remaining source p u_k. If the anchor already belongs to the nine-position cover, its overlap pays for appending a fresh multiple of u_k outside the old cover, possible since floor(M/u_k)≥p. This is the carrier lemma without other bundles. The two requirements (p-units and p-free demand) are both covered in ≤12 positions. Thus in an obstruction all three distinct pair products must belong to A_0.

At the type level, subtract p from each of the three large types and take the three products of the remaining types. The original p-free source pool must contain at least those type multiplicities. This is `product_rule` in the verifier. It rejects all nine v=3 patterns, proving the theorem.

A further necessary condition: for any pair i,j, if neither u_i² nor u_j² belongs to A_0, replace the source h=u_i u_j in A_0 and its extra required copy by the two distinct sources u_i²,u_j². This yields seven distinct p-free sources ≤M with precisely the needed product. The same carrier proof closes the case. Therefore at least two of the three squares u_i² must belong to A_0. Of the squares and pair products the only possible equality is u_middle²=u_min u_max. `square_rule` overenumerates all orders and allows this equality only when the high-part types agree.

This additional condition removes six more abstract two-large-prime patterns. In particular, if both large primes have square >M, the only remaining abstract multiplicities are (4,4) plus one 11-smooth source, or (4,5) with no 11-smooth source.

## 9. Exact status and limitations

**New theorem:** Conditional on the smaller g-bounds above, any nine-source obstruction to a 12-point cover uses at most two distinct primes ≥13. The proof is global in M, has no interval-shift sampling, and does not depend on the supplied report's large-M theorem or any smooth enumeration.

For a minimal-M obstruction a common prime divisor can also be excluded: divide by it, cover the distinct quotient sources in the shorter interval (possibly omitting quotient 1 and using g(8)), and pad to at least nine positions before multiplying them back by the common prime. A minimal counterexample thus has no prime of support nine. With this filter, the verifier gives 24 one-large-prime patterns and 82 labelled two-large-prime patterns after the rules above. These are abstract incidence types, not a count of numerical source sets or shifts. No claim that all remaining types fail is made.

**Audit correction:** The earlier 44,193-vector 11-smooth computation used `enumerate9.cpp`, whose exclusion rules are for budget 13 (e.g. slots 10..13 for a pair). A successful subsequent 12-slot cover on those vectors does not establish the 12-slot theorem for all 11-smooth sets. A second earlier program `enumerate12.cpp` still pruned using `pack(a.e,M,12,13)` and excluded Ω(a)<3, neither justified for a 12-slot obstruction in general. The 11-smooth branch must be established with a correctly regenerated domain. This defect does not invalidate the separate verified 13-upper-bound package, or the present structural reduction. The supplied report's claimed 7-smooth result is a separate result, not independently replayed here. The exact global value remains either 12 or 13 under the earlier smaller-g dependencies.

## Reproduction

Run `python3 verify_structures.py`. It needs only Python's standard library. The included `replay.log` records the actual output. No external mathematics package, random search, or prior certificate is needed for the finite type enumeration. The preceding proof supplies the mathematical justification for every pruning rule. The smaller-g results remain explicit external dependencies of this reduction.
