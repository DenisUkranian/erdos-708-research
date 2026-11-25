# Erdős–Surányi problem 708: stronger nine-source reduction

**Status:** conditional on the previously obtained bounds for 5, 6, 7 and 8 sources. This note establishes a new tail bound and necessary structure for a counterexample. It does **not** establish the global equality g(9)=12. The lower witness has exact optimum 12.

Let A be nine distinct integers in [2,M], with max A=M, and I any interval of M consecutive positive integers. Write P=prod(A). We use g(5)<=6, g(6)<=8, g(7)<=9, g(8)<=11, and the supplied prior upper bound g(9)<=13. The first four bounds are inputs from earlier work, not re-proved here. A bound on a subset applies in the same interval by taking a subinterval of the required length. The full interval product is divisible by M!, hence by P. A missing single prime unit can always be supplied by one new point (or is already supplied). A factor h can be supplied by a new point in slot j whenever j*h<=M. Call a pair (A,I) an obstruction if tau(A,I)>12.

## 1. Structural lemmas

A prime p>=13 is called large. A low large prime satisfies p^2<=M, a high one satisfies p^2>M. Let D_p be its total demand and d_p its number of distinct source incidences.

**1a.** Every large prime has d_p>=3. If d_p=1, cover the other eight sources in 11 points. To append the remaining source a, take a multiple of a if new, otherwise the old product already covers lcm(P/a,a). A fresh multiple of gcd(P/a,a)<=M/p supplies the missing gcd. If d_p=2, write the sources as p^e u and p^f v (p-free cofactors), e>=f. Cover the other seven in nine points. Pick a multiple z of the first source and another distinct multiple of p^f; the latter exists because there are two distinct sources divisible by p^f. These two carriers supply all the p-demand. If z is new, it also supplies u, and one fresh multiple of v completes the old p-free demand. If z was already chosen, at most one carrier is new, and append fresh multiples of u and v. Either way there are at most three new points. Freshness follows from at least p>=13 multiples of each cofactor.

**1b.** Cover seven sources, excluding two divisible by p, in nine points. Add fresh multiples of their quotients by p, leaving only two p-units possibly missing. If 12*p^2<=M there is a fresh square multiple in the last slot. More strongly, if all multiples of p^2 are already chosen, their product supplies at least 2*floor(M/p^2) units. If this is at least D_p-1, at most one unit is missing, so the last slot suffices anyway. Consequently in an obstruction,

    12*p^2 > M,
    2*floor(M/p^2) <= D_p-2.

Each source has at most two large-prime occurrences: a product of any two large primes is >M/12, and a third factor >=13 would exceed M. Thus sum D_p<=18. Put F_p=floor(M/p^2). In particular p^2>M/floor(D_p/2)>=M/9.

**1c.** Every low large prime has support d_p>=5. If d=3 or 4 and all exponents are one, cover the p-free sources in r=8 or 6 points, respectively. Choose a full-source anchor z. One square multiple together with ordinary p-multiples supplies p^d in d-1 carriers including z (if z is square use it; otherwise take a square and ordinary multiples). There are enough multiples since the sources are distinct. If z was new, append d-1 other cofactors; if z was old, save one carrier but append all d cofactors. Either way r+2d-2=12.

Otherwise let t>=1 count square sources. All exponents are 1 or 2, so D=d+t, and t<=F<=floor((d+t-2)/2). For d=3 or 4 these inequalities force F=t (t=1 for d=3, t=1 or 2 for d=4). Therefore the square source group consists of p^2*j for j=1,...,t, including p^2 itself. Choose a full-source anchor z of a different source, and choose d p-carriers including z, of which at least t are square multiples: if z is square take t-1 additional squares, otherwise take t squares, then fill with ordinary multiples. Their product supplies p^(d+t). If z is new append only d-2 remaining non-unit cofactors; if z was already chosen append at most d-1, saving one carrier. The pure source p^2 has no cofactor cost. Again r+2d-2=12. Every fresh cofactor has >=p>=13 multiples.

**1d.** If there is a square source p^2*s, there is also a unit source p*u: otherwise t=d and F>=d contradicts 1b. Remove those two sources, cover seven in nine points, then append a fresh multiple of u. Need p^3*s in two slots. If a fresh square multiple exists, add it and a fresh multiple of p*s. If not, all square multiples are already chosen, supplying at least 2F units. Add a fresh multiple of p*s (there are >=p multiples since p^2*s<=M). If D<=2F+2, at most one p-unit is missing and can be supplied in the last slot. Hence a square source in an obstruction requires D>=2F+3.

**1e.** If t>=2 and F=t, the sources include p^2 and 2p^2. Remove these two and cover seven in nine points. If no square multiple was used, add two distinct new squares and a new even point. If a square was used but some square is still free, add one fresh square and a fresh multiple of 2p, then repair at most one prime unit. If all F squares were used, append a fresh multiple of 2p and repair at most two p-units whenever D<=2F+3. A fresh multiple of 2p is guaranteed (M>=2p^2). All cases use <=12 points and restore the additional factor 2. Therefore the saturated case t>=2, F=t, D<=2F+3 is excluded.

## 2. Finite type enumeration (not source enumeration)

Let v be the number of distinct large primes and l the number of low ones. High primes cannot coexist in a source, and each low prime occurs in >=5 distinct sources. Thus 3(v-l)<=9 and 3v+2l<=18, giving v<=4. Write a=h*s with h its full large-prime part and s 11-smooth. Each h has type 1, p, p^2 or pq. Squares only at low vertices; an edge cannot join two high vertices.

Enumerate all multisets of nine such types for each v=1,2,3,4 and each l satisfying the two inequalities. For each low vertex, with t loops and total demand D, retain F in the integer range max(1,t)<=F<=floor((D-2)/2). If t>0 require D>=2F+3; if t>=2 exclude F=t and D<=2F+3. These are exactly the necessary conditions proved above (possibly overapproximating the real arithmetic). Set c=1+max allowed F for a low vertex and c=1 for a high vertex. For a degree-two type ij (including i=j), the core satisfies p_i*p_j>M/sqrt(c_i*c_j), so its distinct cofactors are bounded above by floor(sqrt(c_i*c_j-1)). Its multiplicity cannot exceed this number. The integer square root here is exact, because the bound on the cofactor is strict.

The standard-library verifier `verify.py` enumerates these multisets directly. No interval shifts or candidate source magnitudes are sampled. The surviving counts are:

- v=1: 7 types with l=0, 20 with l=1;
- v=2: 10 with l=0, 25 with l=1, 16 with l=2;
- v=3: one with l=0 and two with l=1;
- v=4: none.

The three v=3 patterns are (p is low, q,r high in the last two):

1. Three singleton occurrences of each of three high primes.
2. pq, pr, three p-singletons, two q-singletons and two r-singletons.
3. p^2, pq, pr, two p-singletons, two q-singletons and two r-singletons.

In patterns 2 and 3, all degree-two cofactors are 1. In particular there is no ordinary triangle in any remaining core, including v<=2. Also in every obstruction all degree-two cofactors are <9, because p_i^2>M/9 and p_j^2>M/9.

## 3. Three spare slots for small cofactors

For each nontrivial large core h with multiplicity m_h, choose m_h distinct multiples of h in I. This is possible by distinctness of the original sources. We may force one chosen bank to contain any prescribed multiple of a full source with this core. Let m=sum m_h. At each union point of the banks, suppose e ordinary edges, l' loops, s' singletons and v' vertices are assigned, k=e+l'+s'. The point supplies at least v'+l' units, versus 2e+2l'+s' assigned units. The excess of the count of the point plus its possible local prime-unit deficits over k is at most 1+e-v'. Because the entire edge graph is a forest, e<=v'-1. Summing gives a cover of the entire large-prime demand with at most m points after individual prime-unit repairs. Any marked full-source multiple is retained. The full interval supply justifies the repairs; they do not use the small-prime budget.

Choose an anchor source whose small part is maximal. If its core is nontrivial, mark a full multiple in the above construction. Otherwise choose a full multiple separately, costing one point out of the at least one source with trivial core. In either case at most nine points cover the large demand and the anchor's small factor. If the other eight small cofactors are <=10, split them into groups of sizes 3,3,2, with products <=1000,1000,100. When M>=9450 there are enough multiples to choose three distinct points, distinct also from the anchor. They may overlap other core points, since small and large prime demands are disjoint. Thus twelve points suffice.

## 4. Tail reduction M>=9450: at least two large small cofactors

Assume an obstruction in this range. Every source a satisfies 12a>M, since otherwise it can be appended to an eight-source cover in the last slot. If two small cofactors s_a,s_b>=11, choose any of their divisibility-minimal divisors u,v>=11. Each divides an 11-smooth source, so u,v<=110 (take a factor out of a minimal divisor). The complete list is computed in the verifier. Let C(u,v) be the minimum of k*d*e over permutations (i,j,k) of (10,11,12) and divisors d|u, e|v with d>=i,e>=j. For M>=C(u,v), cover seven sources in nine points, then append fresh multiples of a/d,b/e,de in that permutation. Their product is ab. Therefore every pair of such divisors in different sources must have C(u,v)>M.

The only unordered pairs with C>9450 are:

| u,v | C |
|---|---:|
|21,49|10290|
|25,49|12250|
|27,49|13230|
|35,35|12250|
|35,49|17150|
|49,49|24010|

Consequently if M>=24010, at most one small cofactor is >=11 and Section 3 closes the case. For 9450<=M<24010 there are three cases:

* If all large small cofactors have only minimal divisor 49, each is a pure power of 7. Indeed any other prime factor 2,3,5,11 gives minimal divisor 14,21,35,11 respectively. Remove the two largest 7-valuations; both divisible by 49.
* If there is a source with minimal divisor 21,25,27, every other large small cofactor has only minimal divisor 49 by the table. Otherwise if exactly one source has minimal divisor 35, the same holds. Remove this special source and the pure-7 source with largest valuation. Use d=21,25,27,35 from the special source and 49 from the second.
* Otherwise at least two sources have minimal divisor 35, and every large small cofactor has all minimal divisors in {35,49}. Those with divisor 35 are exactly of the form 5*7^e (e>=1): factor 2,3 or 11 is excluded by an additional minimal divisor, and 5^2 would give minimal divisor 25. The other large small cofactors are pure powers of 7. Remove the two largest 7-valuations among the 35 sources; use 35 from each.

In every case cover the seven sources left in at most nine points. Want to append h=de, then a/d,b/e; the latter have plenty of fresh multiples since d,e>=21. If h has a fresh multiple, the result follows immediately. Otherwise all multiples of h have been selected. For every prime w dividing h, their product contains at least

    floor(M/h)*v_w(h) + v_w(floor(M/h)!)

units. This uses the fact that their quotients are a consecutive interval with length at least floor(M/h). It is enough to bound the old seven sources' demands at these primes.

## 5. Exact supply bounds

For a small cofactor s>=11, a source is s or s*p with one large prime: degree-two cores have s<9. Pure s is eligible only if 12s>M. The singleton possibility requires 12sp>M, sp<=M, p>=13, 9p^2>M; at most three distinct p are active. Thus for a fixed s there are at most min(3,number of primes in that exact band) singleton sources and at most one pure source. These bounds may be summed independently for different s, which only overestimates the demand.

Use these counts for s=7^e,e>=2 and for s=5*7^e,e>=1 to create lists of 7-valuations, with padding ones for small sources. Removing the largest two or one from the appropriate list gives an upper bound on the order statistics of all actual survivors: the j-th largest actual value after deletion cannot exceed the (j+number deleted)-th largest value in its containing multiset. For the 35,35 case take the seven largest of the pure list and the mixed list after removing the largest two from the latter. The verifier computes the bounds at every integer M in [9450,24009].

For a mixed d,49 pair, all other large small cofactors are pure powers of 7. Their 3- and 5-demands vanish. Among s<=10, the only s with v_3>=2 is 9; it is impossible for a pure source or degree-two core and occurs at most once per large singleton type. Therefore the old 3-demand is at most 3*2+4=10.

The old 5-demand is at most 5. Indeed only s=5,10 contribute. Pure such sources are excluded. If v<=2, there are at most 2v singleton sources of this kind. No degree-two ordinary edge can have cofactor 5, since floor(D_p/2)*floor(D_q/2)<=20 for distinct p,q from sum D<=18. A square core with cofactor 5 requires F>=5 and D>=12, so at most one such large prime exists; there is at most one source with that cofactor and square core. Cofactor 10 is impossible for a degree-two core. If v=3, all degree-two cofactors are 1. Each high vertex has support three in the three patterns. It cannot have both 5 and 10 as singleton cofactors: cover the other six sources in eight points, choose the third full-source multiple as anchor and three p-carriers including it, then append a fresh multiple of 50. If the anchor was old, the saved carrier pays for one fresh anchor cofactor. This takes at most four new positions because 12*50<=M and p>=13. Hence each high vertex has at most one such source, and the sole possible low vertex at most two. This proves the bound 5 in all cases. For 35,35, the old 5-demand is at most seven by the pure/mixed classification.

For each case the verifier checks supply minus the upper bound on old demand minus the demand of h. All margins are nonnegative except the pure (49,49) case, where the minimum is -1. In this exceptional case h=7^4 is a pure prime power and one missing 7-unit, if needed, is repaired in the same single slot by the full interval divisibility property. Thus P_old*h is covered in at most ten points; append the two fresh quotients to finish. This contradicts every obstruction with two big small cofactors and M>=9450.

Together Sections 3–5 establish **tau(A,I)<=12 for every M>=9450**, conditional on the input bounds stated at the start. The numerical part is exact and reproducible.

## 6. Remaining work

The verifier also independently confirms an explicit nine-source interval with optimum 12. The global range remains 12<=g(9)<=13. The new proof excludes every counterexample with M>=9450 and every counterexample containing four or more large primes (at every M). With exactly three large primes only the three listed patterns are possible. The proof does not exhaust the remaining M<9450 cases with zero, one, two or three large primes. The attached report's previous 7-smooth and local M<=120 checks may be used once their complete supporting dependencies are independently reproduced. Its supplied source files are not a complete proof of the remaining middle interval; in particular one must not infer a 12-bound from a finite domain pruned only for the 13-bound. No claim of a globally solved nine-source case is made here.

Run `python3 verify.py` from this folder. The program verifies precisely the finite structural and tail computations and the lower witness; it does not test the upstream g(k) proofs or all remaining nine-source instances. A PASS is not a certificate of global equality.
