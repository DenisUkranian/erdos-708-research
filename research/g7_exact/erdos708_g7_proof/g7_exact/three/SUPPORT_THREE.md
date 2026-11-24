# Eliminating support three in the three-large-prime case for g(7)<=9

24 November 2026. Research proof, requiring independent audit.

Assume the independently established bounds g(3)<=4, g(4)<=5, g(5)<=6, g(6)<=8. Suppose there is a counterexample to g(7)<=9, and choose one with a source set A of maximum sum among counterexamples at its fixed M=max A and fixed interval I. Thus A is closed upward under integer multiples within [1,M]: if a in A and ka<=M, then ka is in A. Otherwise replacing a by ka would increase the sum while preserving the counterexample.

Assume there are exactly three active primes >=11, denoted p,q,r. The previously proved reductions give:

* every such prime divides at least three sources;
* each has square greater than M/9;
* each source has at most two large-prime occurrences, including multiplicity;
* all other prime factors are among 2,3,5,7;
* a prime at most sqrt(M) occurring in exactly three sources to exponent one is impossible, by the square-gain lemma.

We prove that none of p,q,r can have source support exactly three.

## A. Compression of a prime group

Suppose p divides exactly d sources p^{e_i}c_i with p not dividing c_i. Choose one of them, a_*=p^{e_*}c_*, and set H=product(c_i for i != *). If H<=M and H is different from all p-free sources (or H=1), cover the p-free sources together with H in r<=g(8-d) points. For d=3 this means r<=g(5)<=6.

Choose z in I divisible by the full source a_*. The whole p-demand can be supplied by at most d points including z. Indeed, match the source p-powers to distinct target multiples by their nested divisibility counts. If the resulting set does not contain z, replace the representative assigned to e_* by z; if it already contains z, no change is needed. If z is outside the old r-cover, its cofactor c_* is supplied disjointly, and the union has at most r+d points. If z is inside the old cover, the p-bank adds at most d-1 points, and one fresh multiple of c_* finishes the job. This fresh multiple exists when p>=r+d, because c_*<=M/p.

Therefore d=3, p>=11, H<=M, H not a p-free source imply a nine-point cover. We call equality H in the p-free source set a blocked compression.

If H=1, use at most g(7-d) points for the old sources, and the same count remains valid.

## B. A four-atom covering lemma

Let P,Q,R,S be pairwise coprime integers >1. Suppose the seven required core factors are the six pair products from the complete graph on these four atoms, together with a second copy of QR. Assume each pair product is at most M, 2QR<=M, Q^2,R^2,S^2<=M, and I has at least eleven multiples of each atom. Then their product is covered by at most eight target points. The cover can be required to contain any specified target multiple of QR (in particular one divisible by a prescribed full source with core QR).

Choose one target representative for each pair bank except QR, which has two distinct representatives. Include the prescribed point in the QR bank. At a selected point, let k be the number of pair banks using it, e=k the number of edges, and v the number of atoms present. Relative to the assigned core factors, the atom-unit deficit is at most 2e-v, and union size plus unit repairs, compared with the seven assigned representatives, has excess at most 1+e-v. For a composite atom S, count the number of complete powers S^j dividing a point; coprimality of the four atoms makes this a valid sufficient accounting. Fresh ordinary atom multiples remain available throughout because there are at least eleven and the provisional bound never exceeds ten.

Distinct positive-cycle points are possible only for the triangles PQR and QRS: any other two cycles of K4 share an edge bank of cardinality one, forcing the points to coincide. If there are two such points, each Q- and R-demand has baseline deficiency two across them. A square multiple of each repairs those two units in one pick, or, if already selected, already improves the baseline by at least one unit. This saves two picks from the provisional bound 7+2=9.

If there is one positive-cycle point, cycle rank one gives at most eight immediately. Rank two means the five-edge graph K4 minus one edge. At least one of Q,R,S has degree three at that point and therefore has baseline total deficiency two; any remaining assigned occurrence is outside the point and adds one required and one supplied unit. Its square saves one pick from 7+2=9. Rank three means all six pair types meet at one point. Q,R have deficiency two (their extra QR representative supplies one additional unit), and S has deficiency two. The three squares save three picks from 7+3=10. Thus eight always suffice.

This proof also covers extra accidental atom divisibilities: they only reduce the deficits.

## C. A support-three prime above sqrt(M)

Let p>sqrt(M) divide exactly three sources p*c1,p*c2,p*c3. The c_i are distinct and less than sqrt(M), so every pair product c_i*c_j is at most M. If any compression is unblocked, Section A closes the instance. Otherwise all three distinct pair products belong to the four p-free sources. Write the seventh source as b.

Both q and r must divide some c_i: otherwise the missing large prime would occur only in b. Each c_i contains at most one large-prime occurrence. Therefore the large parts of (c1,c2,c3) are, after relabeling, either (q,q,r) or (q,r,1).

### C1. Pattern (q,q,r)

Since pq,pr>M/3, their source cofactors are at most two. The two distinct q-cofactors are exactly 1 and 2. Thus the six forced sources are

    pq, 2pq, prt, 2q^2, qrt, 2qrt,   t in {1,2}.

The seventh source b must contain r: otherwise r occurs exactly three times to exponent one and r<sqrt(M), so the square-gain lemma closes the case. Its large core is r, r^2, or qr. Use the three-prime core-bank theorem to cover all large-prime demand in at most eight points, prescribing a multiple of b. The remaining small factor is exactly 8t^3, at most 64.

If M>=576, it has at least nine interval multiples. If M<576, t=2 is impossible: 2pq<=M<p^2 gives p>2q, so distinct primes q,r>=11 imply 2pr>=598. Hence t=1, the remaining factor is 8, and M>=2pq>=506>72. A fresh multiple finishes in nine points in either case.

### C2. Pattern (q,r,1)

Write c1=qa, c2=rb, c3=s, with a,b in {1,2} and s composed only of 2,3,5,7. Both q,r are below sqrt(M). The seventh source must contain both q and r, since otherwise one remains a support-three exponent-one low prime. The full source set is

    pqa, prb, ps, qr ab, qa s, rb s, qr c,

where c<=8 and c!=ab. We have s<sqrt(M). Also s>1: if s=1, the source p has at least q>=11 target multiples, so it can be appended freshly to an eight-point cover of the other six sources.

The four atoms p,q,r,s are pairwise coprime. Their required cores are K4 plus a repeated qr, with q^2,r^2,s^2<=M. Each atom has at least eleven target multiples because its product with one of p,q,r>=11 is at most M. Apply Section B. The remaining multiplier is the ENTIRE factor K=a^3*b^3*c, at most 512. We do not credit c from a prescribed point: c may share prime factors with the composite atom s, so doing so could double-count its valuation.

If M>=9K, choose a fresh multiple of K outside the at-most-eight-point atom cover. This completes the original source product in nine points. The remaining case has M<9K<=4608. If a=b=1, K=c<=8 while M>=pq>=143, so this case already closes. Otherwise enumerate the finite family with M<=4607, primes q,r<68, prime p<420, 7-smooth s in [2,67], a,b in {1,2}, c in [1,8] different from ab, and the source set displayed above. The bounds follow from q,r,s<sqrt(M) and p*q<=M. After imposing the counterexample inequalities and upward closure, 283 sets remain, all with exact nine-slot certificates; see Section E.

This eliminates all high support-three primes in the three-large-prime case.

## D. A support-three prime at most sqrt(M)

If all three occurrences of p have exponent one, the square-gain lemma applies. Hence at least one source has p-exponent two. Any cofactor of a p^2-source is at most eight.

### D1. At least two squared sources

Write two sources as p^2*u,p^2*v, with u,v<=8, and let the third be p^e*w. Compression omitting the third source has H=uv<=64<M. If unblocked, Section A applies. If blocked, uv is a source containing none of p,q,r. The other three p-free sources must then supply all occurrences of q,r not in p^e*w.

If w contains neither q nor r, all three remaining sources must have core qr. At least one of q,r is low and occurs exactly three times to exponent one, so the square-gain lemma applies.

If w contains q (the r case is symmetric), write the third source pqa, with a<=8. Every remaining source must contain r, and at least two must also contain q. If all three have core qr, then r is support three to exponent one: if low use the square-gain lemma; if high, compress r using the product of two q-cofactors. That product contains q^2 and cannot equal any of p^2*u,p^2*v,pqa,uv, and is at most M.

If exactly two remaining sources have core qr, q is support three to exponent one. If low use the square-gain lemma. If high, its cofactors include pa and rc; the pair product p*r*a*c is at most M and cannot equal a q-free source, since those contain only p, only r, or no large prime. Again Section A applies.

Thus at least two squared p-sources are impossible.

### D2. Exactly one squared source

Write the p-sources as p^2*u,p*v,p*w, with u<=8 and v!=w. The products uv,uw are less than M because v,w<=M/p and u<p. If either is unblocked, Section A applies. Suppose both are sources.

The case u=1 is already impossible: the blocked source v and the source pv<=M would force, by upward closure, at least p>=11 multiples of v into the seven-element set. Hence 2<=u<=8, and u does not divide p.

Both q and r must appear in v,w: otherwise a missing large prime would occur in only the two remaining p-free sources. Thus, after relabeling, v=qa,w=rb with a,b<=8. The seven sources include

    p^2*u, pqa, prb, uqa, urb.

Put Nq=floor(M/(uqa)), Nr=floor(M/(urb)). Upward closure places all Nq multiples of uqa and all Nr multiples of urb in A. The first three displayed sources belong to neither set: u does not divide the prime p, and their other large-prime supports differ. The two multiple sets cannot intersect within [1,M], because their least common multiple is at least eleven times each modulus; an intersection would require at least eleven multiples in each set, already more than seven sources. Therefore Nq+Nr<=4.

If q has support exactly three, it can be eliminated as follows. If q is high, the cofactor product (pa)*(ua)=p*u*a^2 is at most M. It cannot equal a q-free source: it contains p but no r, and the only q-free source containing p and no r is p^2*u; equality would require a^2=p. If q is low and has three simple occurrences, use the square-gain lemma. Otherwise its third source is q^2*e with e<=8. Compress by H=u*a*e, a smooth integer. It is less than M, since a<=M/(pq) and ue<=64<pq. All q-free sources contain p or r: an additional smooth source would leave r with fewer than three supports. Thus H is unblocked. The same reasoning applies to r.

Consequently, unless the instance is already closed, both q and r have support at least four. The existing multiple sets contribute Nq+1 and Nr+1 supports, and the remaining 4-Nq-Nr sources contribute at most twice that many q/r incidences. The inequality

    8 <= (Nq+Nr+2) + 2(4-Nq-Nr)

forces Nq+Nr<=2. Hence Nq=Nr=1, and the two remaining sources both have core qr. The only residual family is

    A={p^2*u, pqa, prb, uqa, urb, qrc, qrd},

with c<d<=8. Since uqa>M/2 and pqa<=M, p<2u<=16, so p is 11 or 13. The unique p^2-source must exceed M/2 by upward closure, hence

    p^2*u <= M < 2p^2*u <=2704.

All q,r>=11 are distinct from each other and p. Their coefficients a,b,c,d lie in [1,8]. The conditions pqa<=M<2p^2*u give q*a<2pu<=208 and similarly r*b<208; hence q,r<208. This is a finite, explicitly bounded family.

## E. Exhaustive certificates for the residual family

`enumerate_low_support3.py` enumerates the family in D2: p in {11,13}, u in [1,8] with p<2u, primes q,r in [11,249] (a harmless superset of the proved q,r<208), and a,b,c,d in [1,8], c<d. It forms the displayed seven-source set, computes its actual M, and imposes M<2p^2*u, Nq=Nr=1, uniqueness of the p^2-source's upward multiples, the three large-prime square inequalities, and upward closure.

There are 312 candidates before the final upward-closure filter and 162 afterward. Every one has a nine-slot cumulative-GCD certificate, stored in `low_support3_slots.json`.

`enumerate_high_c2.py` enumerates the residual C2 family with the exact condition M<9K, using the finite bounds just proved, the large-prime square inequalities, actual source maximum, high/low prime conditions, and upward closure. It gives 1527 sets before the final upward-closure filter and 283 afterward. All 283 certificates are stored in `high_c2_slots.json`.

Each certificate consists only of positive integers h_j<=M satisfying

    gcd(product_{i<j} h_i, h_j) <= floor(M/(j+1)),

and product(A) divides product(h_j). The cumulative-GCD theorem proves the bound for every shift; no shift enumeration or floating-point optimization is used. `verify_support3.py` checks all 445 certificates using exact integer arithmetic and returns PASS.

## Conclusion

Subject to independent audit of this proof and the finite enumeration, a maximum-sum counterexample to g(7)<=9 with exactly three active primes >=11 must have every such prime in at least FOUR sources. Thus the remaining three-prime analysis has total large-prime source incidence at least twelve.
