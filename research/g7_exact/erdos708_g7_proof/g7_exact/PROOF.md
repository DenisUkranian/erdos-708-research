# The seven-source Erdős–Surányi covering problem

Computer-assisted proof and exact verification record, 24 November 2026.

## Theorem and validation status

**Theorem. g(7)=9.** The explicit lower bound, normalization, structural reductions, infinite tail, and all four finite prime-support cases are complete and independently checked. The upper bound is computer-assisted: analytic reductions leave a finite collection of source configurations, and exact integer verifiers establish a universal cover for every remaining demand. All finite branches have been regenerated from the supplied source and their certificate checks have returned PASS.

The argument uses the earlier small-n bounds listed in Section 2. It does not prove the asymptotic Erdős Problem 708 or determine g(8) or g(9).

## 1. Definition and target

For a finite set A of distinct integers at least two, put M=max(A). For x>=0, let I={x+1,...,x+M}, and define

    tau(A,I)=min{|B| : B subset I and product(A) divides product(B)}.

The Erdős–Surányi function is

    g(n)=sup tau(A,I),

where the supremum ranges over all n-element source sets A and all nonnegative integer shifts x. Cardinality is interpreted as **at most**, not as an obligation to select exactly the same number from every interval.

To prove g(7)=9, two separate statements are needed: one explicit instance requiring nine points, and a universal nine-point upper bound for every source maximum and every shift. The finite verification below is about universal covering certificates, not a bounded sample of shifts.

## 2. Prior inputs and basic divisibility

The numerical inputs are

| k | Upper bound used |
|---|---:|
| 1 | 1 |
| 2 | 2 |
| 3 | 4 |
| 4 | 5 |
| 5 | 6 |
| 6 | 8 |

The first two are elementary. The three-source bound is the classical Erdős–Surányi result of 1959. The external four- and five-source input is Theorem 1.6 of John Tripodo, *Sharp finite cases of the Erdős–Surányi interval-product problem: g(4)=5 and g(5)=6*, 19 November 2026, manuscript version 1.8, [primary manuscript](https://hexagonmath.org/pdf/2611.00694v1). That manuscript also states the classical three-source result. It reports a Lean registration, PALOMAR-2026-11-19-000019; the external formalization was not rebuilt in this verification.

The six-source bound has a separate analytic and exact computational proof in [`dependencies/G6_UPPER_BOUND.md`](dependencies/G6_UPPER_BOUND.md), using only the stated g(5)<=6 input. Its independent verifier is `../g7_theory/check_g6_independent.py`, with slot data in `../smooth_proof/frontier_slots6.json`. The replay checks all 1,045,917 remaining six-source subsets and returns PASS. Thus g(6)<=8 is established independently of the present seven-source argument. In particular, this proof does not rely on the faulty large-M passage of the previously discussed Bergström preprint.

If a subset has maximum smaller than M, any suitable shorter subinterval of I allows the corresponding g(k) bound to be used inside I.

Distinctness gives

    product(A) divides M!.

Also product(I)/M! is the integer binomial coefficient binomial(x+M,M). Therefore

    product(A) divides M! divides product(I).

In particular, the complete interval always has sufficient valuation at every source prime. If a selected product is missing only one unit of a prime p, an unselected p-divisible point exists and repairs that deficiency. More generally, missing prime units can be repaired one at a time within their total number.

## 3. An explicit lower bound of nine

Take

    A={289,323,361,391,437,493,551}
     ={17^2,17*19,19^2,17*23,19*23,17*29,19*29}.

Its prime demands at (17,19,23,29) are (5,5,2,2), and M=551. Set

    N=17^2*19^2*23*29=69,587,443,
    I={N-275,...,N+275}.

The center has valuations (2,2,1,1). Every off-center point is divisible by at most one active prime: otherwise the product of two active primes would divide a nonzero offset of absolute value at most 275, while the smallest such product is 323. Off-center 17- and 19-valuations are at most one, because 17^2=289 and 19^2=361 also exceed 275.

If the center is chosen, the remaining demands (3,3,1,1) require eight separate off-center points. If the center is omitted, the first two primes require five points each and the other two require at least one each, totaling at least twelve. Thus tau(A,I)>=9.

The nine offsets

    0,17,34,51,19,38,57,23,29

give a matching cover, so this instance has tau(A,I)=9 exactly. Consequently g(7)>=9. `LOWER9_SIMPLE.md` gives the full argument, and `verify_lower9_simple.py` checks every interval point's stated restrictions and the exact product divisibility of the displayed cover.

## 4. Normalize a hypothetical counterexample

Suppose the upper bound g(7)<=9 fails. Choose a counterexample with least M, and then a source set of largest sum among counterexamples at that M and its target interval. Cases M<=9 are already covered by the complete interval, so M>=10.

### 4.1. The source gcd is one

If a prime p divides all seven sources, then p divides M. The target p-multiples, after division by p, form an interval of exactly M/p consecutive positive integers. The seven divided sources are distinct and have maximum M/p. If none equals one, minimality of M supplies a nine-point cover. If one equals one, cover the other six in at most eight points using g(6)<=8.

Pad the quotient cover to at least seven points when necessary, then multiply the selected points by p. There are at least seven quotient positions, since seven distinct positive quotient sources exist. Padding stays within nine points, and supplies the required additional p^7. This contradicts the counterexample. Hence gcd(A)=1.

### 4.2. Upward closure and a minimum source bound

If a is a source, ka<=M, and ka is not a source, replace a by ka. The new set still has seven distinct members and maximum M, its product is a multiple of the original product, and its sum is larger. It would remain a counterexample, contradicting maximality. Therefore A is closed under all integer multiples at most M.

Every source consequently exceeds M/7. Otherwise its first seven multiples exhaust the seven-element source set, giving a nontrivial common divisor, or an eighth multiple would require too many sources. This sharper M/7 bound uses both upward closure and gcd one.

## 5. Elementary covering tools

### 5.1. Cumulative-GCD slots

Let h1,...,hL be positive integers at most M, with L<=M, such that

    gcd(h1*...*h_{j-1},hj) <= floor(M/j)

for every j>=2. Then L distinct interval points have product divisible by h1*...*hL.

Inductively suppose earlier selected points cover H=h1*...*h_{j-1}. If a fresh multiple of hj exists, append it. Otherwise hj divides the product of the selected points, as does H, so lcm(H,hj) divides that product. There are at least j multiples of gcd(H,hj) in the interval and only j-1 selected points. Appending a fresh such multiple supplies H*hj. The first step uses any multiple of h1.

This lemma makes a finite list of small integers a universal-shift certificate. Verification requires only integer ranges, cumulative gcds, and final divisibility.

### 5.2. Removing two sources

Cover five sources in at most six points. If the product ab of the two removed sources factors into three integers bounded respectively by

    floor(M/7), floor(M/8), floor(M/9),

fresh multiples of these factors finish the cover in nine points.

A useful special case removes one occurrence of a prime p from a and one occurrence of a prime q from b. If p>=7, q>=8, and pq<=M/9, append fresh multiples of a/p, b/q, and pq. This also works for p=q and for sources containing higher prime powers.

### 5.3. A prime appearing in d sources

Suppose a prime p divides exactly d sources, with 1<=d<7, and g(7-d)<=r. Write the affected sources p^{e_i}c_i, with p not dividing c_i. If

    p >= r+2d-1,

then r+2d-1 points suffice.

Cover the p-free sources in r points. Select a target multiple z of one full p-source, and at most d p-divisible points, including z, that supply the total p-demand. Such a set exists by the nested counts of multiples of p^e: the number of sources divisible by p^e is at most floor(M/p^e). A matching can include any prescribed z by replacing the representative assigned to that source if z is not already selected.

If z is new, its cofactor is supplied separately from the old cover, and append the other d-1 cofactors. If z is old, the p-bank adds at most d-1 points, and append all d cofactors. Each cofactor is at most M/p, so enough fresh multiples exist. Both cases use r+2d-1 points.

If d>=3, all affected source valuations are one, p^2<=M, and p>=r+2d-2, the bound improves to r+2d-2. The p-demand p^d can then be supplied in d-1 points including z, using a square multiple and ordinary p-multiples.

### 5.4. Compression of a prime group

For the same p-sources, choose one source p^{e_*}c_* and put H=product of the other d-1 cofactors. If H<=M and H is different from every p-free source, cover those p-free sources together with H in r<=g(8-d) points. If H=1, omit it. A p-bank of d points including a multiple of the chosen full source, with the same overlap accounting, completes the cover in r+d points when p>=r+d.

For d=3, r<=6, so an unblocked cofactor compression gives nine points. A substantial part of the three-prime proof analyzes the cases where all available H coincide with old sources.

## 6. Large-prime structure

Call primes at least 11 large. All other source factors are 7-smooth.

The support lemma with d=1 and d=2 gives respectively 8+1=9 and 6+3=9. Thus each active large prime divides at least three sources. Applying the two-source peeling lemma to two sources divisible by p gives

    p^2 > M/9.

Any three large-prime occurrences, including repetitions, would have product greater than (M/9)*11>M. Hence each source contains at most two large-prime occurrences. There are at most four distinct large primes, since their total source incidence is at most fourteen.

### 6.1. Core-bank counting

For a chosen large-prime set, the full large part of a source is 1, p, p^2, or pq. Group sources by their nontrivial core d. If the group has m_d members, choose m_d distinct target multiples of d; these exist because m_d<=floor(M/d). A group can be required to contain a specified multiple of one full source from that group.

At a target point shared by several groups, draw their ordinary pair cores as edges, their squares as loops, and their singleton cores as singleton types. If e is the number of ordinary edges, v the number of present vertices, l the number of loops, and s the number of singleton types, then k=e+l+s groups use the point. Their assigned valuation is 2e+2l+s, while the point supplies at least v+l. The valuation deficit is at most 2e+l+s-v. Relative to the k assigned representatives, union size plus unit repair has excess at most

    1+e-v.

With one or two primes this is never positive. With three primes it is positive only for a triangle, and equals one there. Since pqr>M, at most one target point can carry that triangle. Therefore m nontrivial sources have their large demand covered in at most m points for at most two primes, or m+1 for three primes. A prescribed full-source point is retained.

A pair group with spare capacity can avoid the unique potential triangle point, improving m+1 to m. If a full-source point is prescribed in another group, it is still retained.

### 6.2. Four large primes are impossible

Call a large prime low if it is at most sqrt(M), and high otherwise. Each high prime has demand at least three. Each low prime has demand at least four: demand three would mean three simple source occurrences, which the square-gain lemma closes in nine points.

Four primes with l low ones require at least 12+l valuation units, but at most fourteen exist, so l<=2. Three high primes would require nine distinct sources, because no source can contain two high primes. Thus exactly two are low, p1,p2, and two high, q1,q2. All inequalities are equalities: demands are (4,4,3,3), and all seven sources have large degree two.

Six sources have cross cores p_i*q_j. The seventh has core p1*p2, p1^2, or p2^2. Since p_i>sqrt(M)/3 and q_j>sqrt(M), every cross core exceeds M/3, so its cofactor is 1 or 2 and its multiplicity is at most two. The cross multiplicity matrix is, up to labels,

    [[1,2],[2,1]]   or   [[1,1],[2,2]].

Core-bank counting covers the large demand in at most eight points. In the loop case only the four-cycle can have positive excess, and it occurs at at most one point. In the edge case all positive cycles coalesce, because distinct cycles would share a single-member group. Excess at most one gives eight points. Excess two means all five core types meet at one point, leaving at most three selected points and deficiencies at most (2,2,1,1). The two low-prime squares repair their two-unit deficits in one point each, giving at most seven overall.

Require a selected point to cover one full cross source with cofactor 2; such a source exists in a multiplicity-two group. The six cross cofactors have product at most 16. If the seventh source is d0*s0, the uncredited small product is at most

    8*s0 <= 8M/d0 <= 8M/121 < M/9.

One fresh multiple finishes the cover. Therefore a counterexample has at most three large primes, for every M. Full details and an independent audit are recorded in `g89_theory/core_reductions.md`.

### 6.3. Coprime merging of large and small covers

Large-prime and small-prime demands are coprime. Independent covers can therefore be united even if their target sets intersect. If one prescribed point z is credited with a small cofactor c_*, a cover of the remaining small product need avoid only z, not every point of the large-core cover.

This distinction is essential. It applies to a genuine large-prime core, whose primes are all at least 11. It cannot automatically be used when a composite 7-smooth factor has been introduced as an auxiliary atom; the four-atom proof handles its remaining multiplier separately.

## 7. The infinite tail: M>=24697

The complete proof is `root/LARGE_M_CUTOFF.md`; the argument is summarized here to show why only a finite range remains.

### 7.1. Greedy packing bounds

After covering five sources in six points, put any already assigned large factors into bins M/7,M/8,M/9, and insert all remaining prime factors, at most seven, in descending order. Failure at a prime t<=7 would give

    ab > M^3/(504*t^2) >= M^3/24696.

Since ab<=M^2, this is impossible when M>=24697.

A 7-smooth product Q<=6^7 also packs into two bins M/8,M/9 in this range. Failure would give Q>M^2/(72t)>=M^2/504, while 504*6^7<24697^2.

### 7.2. A large prime above M/9

Such a prime p has source support d in {3,4,5,6}; gcd one excludes d=7. Because p>=11 and M<9p<p^2, its sources are p*c_i with distinct c_i in {1,...,8}. Cover the other sources and a p-bank, retaining a full source with largest cofactor. The budgets are

| d | old-source bound r | r+d |
|---|---:|---:|
| 3 | 5 | 8 |
| 4 | 4 | 8 |
| 5 | 2 | 7 |
| 6 | 1 | 7 |

For d=3,4, the remaining cofactors have product at most 210 and take one fresh point. For d=5,6, split them into two products bounded by 210 and 42 and take two fresh points. All these products are below M/9 in the stated range. The total is at most nine.

### 7.3. All large primes at most M/9

If a source has large degree at most one, pair it with another source. At most three large occurrences need placement, one in each of the three bins; the remaining small factors pack by 7.1. Thus every source in a counterexample has degree two.

If any core is at most M/7, put that core in the first bin and the two individual large occurrences of another source in the other bins. Again the small factors finish the pair. Hence every core exceeds M/7 and every small cofactor is at most six.

If the core graph has no triangle, or a triangle edge group has spare capacity, the core cover uses at most seven points. Two small-factor bins cover the full small product, at most 6^7.

Otherwise all three edge groups are present and saturated: their source multiplicities equal floor(M/d), so distinctness forces their cofactors to be exactly 1,...,m_d. Prescribe a full source having the largest small cofactor. The core cover uses at most eight points. If t is the number of edge-core sources, the remaining small product is bounded by

| t | Remaining product bound |
|---|---:|
| 3 | 216 |
| 4 | 72 |
| 5 | 36 |
| 6 | 24 |
| 7 | 24 |

Each is below M/9, so one fresh point completes the cover. This excludes every counterexample with M>=24697.

## 8. Finite case with no large prime — complete

Every source is 7-smooth. `smooth/SMOOTH9_PROOF.md` proves this case independently of common-factor normalization or upward closure.

Its analytic tail starts at M=12555. Below that cutoff, a graph joins source pairs for which no valid three-bin certificate has been found. Every possible counterexample is among the resulting seven-source cliques. The independent enumeration covers 3,413,772 source sets at 94 maxima, with 135,961 distinct demand vectors; the largest surviving source maximum is 567.

Separate-prime covers, ordinary bins, cumulative-GCD certificates, and exact CRT profile enumeration close every demand. There are 36,247 explicit slot lists. The final CRT method checks 318 targets over all relevant prime-power residue classes, not sampled shifts, using 99,864 branch nodes and 6,049 exact multicover calls. Capping valuations at the source-relevant prime-power level gives lower supply profiles for every actual shift, so successful covers of all capped profiles prove the universal result.

The independent replay is `smooth/verify_smooth9.py`; its recorded result is `smooth/verification_result.json`. The CRT implementation and finite-state bounds were independently audited.

## 9. Finite case with one large prime — complete

The one-large-prime computation covers 59,982 initial configurations. Universal cofactor envelopes, pair tests, and forced-multiple closure leave 623 configurations, all with M<=735. Exact enumeration covers 7,006,656 normalized source sets and 658,925 distinct demand vectors. Their maximal-demand antichain consists of 120,285 demands closed by independent core, prime-union, or ordinary-bin tests, 252,175 demands with explicit nine-slot certificates, and one hand-proved demand:

    M=55, demand at (2,3,5,7,11) = (4,9,2,0,4).

For the hand demand, choose two consecutive multiples of 27, a fresh multiple of 18, and a fresh multiple of 6. The first pair contains an even number, so these four points supply 2^3*3^9. A multiple of 50 adds 5^2 and a further factor 2; if that multiple was already chosen, append a fresh even point instead. Thus five points cover 2^4*3^9*5^2. Unite them with four distinct multiples of 11. The demands are coprime, so their intersection is harmless and at most nine points suffice.

`one/ONE_LARGE_PROOF.md` gives the detailed argument. The independent source review in `one/INDEPENDENT_AUDIT.md` checks the configuration bounds, cofactor envelopes, complete forced-closure recursion, core-cover conditions, demand encoding, and exact domination algorithm. The portable `one/verify_one.py` regenerates all source configurations, checks every slot certificate using unbounded integers, and rechecks all 120,285 other maximal demands in Python. Its independent replay returned PASS. The hand proof removes any dependency on a CRT computation for the last demand.

## 10. Finite case with two large primes — complete

If no source contains both p and q, their supports are disjoint and one has size three. If that prime is high, all three pair products of its cofactors are at most M. If it is low and all its source valuations are one, the square-gain lemma applies. Otherwise at least two distinct cofactor-pair products involving a squared-source cofactor are less than M. Every such product is q-free, while at least three of the four old sources contain q. Hence at most one old source can block these two choices, and an unblocked prime-group compression gives nine points. Thus an actual pq core must occur in a counterexample.

The two-prime finite envelope covers 2,980,414 eligible core classes: 2,784,139 close directly and 196,275 pass to further enumeration. Pair-graph and closure enumeration on 50,660 configurations gives 112,998 nontrivial-source cliques. Of these, 67,663 close by core/small-factor criteria; the other 45,335 rows expand to 116,394 actual full source sets, at maxima at most 665.

These sets have 33,939 distinct valuation demands. Componentwise domination reduces them to 24,511 maximal demands at fixed (p,q,M). Every maximal demand has a nine-slot certificate. The envelope and source-enumeration code have independent review. A separate exact program rebuilt all 116,394 full source sets from the nontrivial rows, checked normalized source closure, verified equality with all 33,939 stored demand keys, checked that every demand is dominated by a stored maximal demand, and validated all 24,511 cumulative-GCD certificates.

Primary files are under `two/`. The independent expansion and domination check is `two/verify_demands_independent.py`; it returned PASS. The complete portable two-prime replay also returned PASS after rebuilding the finite envelope and enumerator from source.

## 11. Finite case with three large primes — complete

`three/SUPPORT_THREE.md` eliminates support exactly three for each large prime in this case. It uses prime-group compression, the square gain, and a four-atom K4-plus-repeated-edge lemma. Two bounded residual families contain 162 and 283 source sets. All 445 have exact nine-slot certificates. The argument explicitly avoids double-counting coefficients that share primes with an auxiliary composite atom.

Every large prime therefore has source support at least four. Every two supports intersect, so all three pair cores occur. For p<q<r, at most one prime can exceed sqrt(M), and

    qr<=M<9p^2,

with q^2<=M. There are 46 possible multiplicity vectors for the ten cores 1,p,q,r,p^2,q^2,r^2,pq,pr,qr. The finite envelope covers 6,294 prime triples, 656,193 eligible maxima, and 850,366 classes.

The envelope uses only proved sufficient criteria: independent prime-power covers, core banks, spare-bank triangle avoidance, coprime merging, and exact upper bounds for each rough-prime part of all possible coefficient choices. It closes 850,364 classes.

The two remaining classes have p=11,q=13,r=23, M=1012 or 1035, and core pattern

    r,r,pq,pq,pq,pr,qr.

Their full source enumeration has 17,640 raw choices and 1,096 normalized sets, with 347 distinct demands. All 1,096 have universal nine-slot certificates. An independent program regenerated the actual sets from integer pools, verified exact equality with the certificate set, and checked every certificate.

The consolidated proof is `three/THREE_LARGE_PROOF.md`. Running `three/verify_all_three.py` regenerates both support-three finite families, verifies their 445 certificates, recompiles and reruns all 850,366 envelope classes in an isolated directory, checks the exact residual classes, and independently regenerates and checks all 1,096 final certificates. The complete replay returned PASS. It needs only Python's standard library and a C++17 compiler.

## 12. Conclusion and limits

The case split is exhaustive. A normalized counterexample can have only zero, one, two, or three large primes; four have been excluded analytically. The global analytic argument removes every M>=24697. Each finite branch below that threshold has now been closed, regenerated, and independently checked. Therefore no counterexample exists, and g(7)<=9. The explicit example in Section 3 proves g(7)>=9. Together these establish

    g(7)=9.

This is a computer-assisted mathematical proof, with the stated prior small-n inputs. Its finite source ranges and finite CRT classes become universal only through the explicit reductions above. The cumulative-GCD certificates prove covers for every interval shift; the CRT certificates exhaust all relevant capped prime-power profiles. No conclusion is based on testing a finite list of numerical shifts.

This proof establishes no new exact value for g(8) or g(9), and it does not settle either global coefficient-two conjecture in Erdős Problem 708.
