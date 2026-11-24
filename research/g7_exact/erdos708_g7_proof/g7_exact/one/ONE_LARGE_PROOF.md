# The one-large-prime branch of the nine-point theorem

## Statement and dependencies

This file closes the case of exactly one active prime P>=11 in the proof
that g(7)<=9. It is a proof about the least-M, maximal-sum counterexample
used by the surrounding argument. The global reductions are stated in
../root/LARGE_M_CUTOFF.md and the main proof; they imply that such a
counterexample, if it existed, would have all the following properties:

1. A consists of seven distinct integers >=2, with M=max(A)<=24696.
2. gcd(A)=1, and A is closed upward under integer multiples not exceeding M.
3. Every a in A satisfies 7a>M and is composite.
4. Exactly one prime factor P of product(A) is >=11. Every other prime
   factor belongs to {2,3,5,7}.
5. P occurs in at least three sources, P^2>M/9, and no source has more
   than two occurrences of primes >=11.
6. The case M>=1890 and 9P>M is already closed by the global large-prime
   argument. Thus it can be omitted from the finite enumeration below.

We use g(1)=1, g(2)<=2, g(3)<=4, g(4)<=5, g(5)<=6 and g(6)<=8. The
external small-n theorem and the separate proof of g(6)<=8 are identified
in the main proof. The computation below is independent of any claim
about g(7) itself. In particular, it does not use the stronger a/P filter
that was valid for the earlier ten-point upper bound.

The conclusion is that no set with properties 1--6 is a counterexample.
Together with the other prime-support branches and the global reductions,
this closes the one-large-prime part of g(7)<=9.

For clarity, the use of the threshold 1890 in property 6 follows from
the same explicit argument as the large-prime section of the global
cutoff proof. When P>M/9, the affected sources are P*c with distinct
c in {1,...,8}. After prescribing the largest cofactor, the remaining
cofactors for support sizes 3 or 4 have product at most 7*6*5=210.
For support sizes 5 or 6, divide the remaining at most five cofactors
into groups of at most three and two; their products are at most 210
and 42. The old-source/core counts are respectively 8 and 7. At
M>=1890 every required additional factor is at most M/9; the prescribed
cofactor, at most 8, can also be repaired with a fresh point if needed.
This proves the omitted case already at 1890, without assuming the
larger global cutoff 24697.

## Two general covering facts

Distinctness gives product(A)|M!, and the integer binomial coefficient
gives M!|product(I) for every interval I of M consecutive positive integers.
Thus every prime demand of A is supplied by the complete interval.

If at most t points have already been selected, an integer h satisfying
h<=floor(M/(t+1)) has a fresh multiple in I: there are at least t+1
multiples and at most t selected points. Consequently, a factorization
into factors bounded successively by floor(M/(t+1)), floor(M/(t+2)), ...
can be covered with that many additional points.

There is also a useful primewise bound. For any prime p, the k largest
p-valuations among interval points have sum at least

    S_p(M,k) = sum_{e>=1} min(k,floor(M/p^e)).

The sets of points with valuation at least e are nested; each has at least
floor(M/p^e) elements. Separate covers for distinct prime demands may be
united without losing any valuation, even when they intersect.

## A prescribed core cover for one large prime

Write each source containing P as P^e c, with e in {1,2} and c 7-smooth.
Let m be the number of these sources. The other z=7-m sources are P-free.
The structural assumptions give 3<=m<=6 and 1<=z<=4.

The P-parts of the m sources can be covered by at most m points of I,
while prescribing any particular point divisible by any chosen full
source P^e c. Here is a direct bank proof. For the sources with e=1,
choose the required number of distinct multiples of P; for the sources
with e=2, choose the required number of distinct multiples of P^2.
Include the prescribed point in its corresponding bank. Each bank has
enough points because its source members are distinct multiples of its
core and are at most M.

If the two banks intersect in t points, their union has m-t points and
can be short of the total P-demand by at most t units. The complete
interval supplies the demand. Whenever a unit is missing, an unused
point divisible by P therefore exists. At most t repairs give a cover
of at most m points. Every initially prescribed point remains present.

Let r be the available bound for the z P-free sources:

| m | z | r | Remaining point budget k=9-r-m |
|---|---|---|---|
| 3 | 4 | 5 | 1 |
| 4 | 3 | 4 | 1 |
| 5 | 2 | 2 | 2 |
| 6 | 1 | 1 | 2 |

Choose a cover B of these z sources, with |B|<=r. Among the P-containing
sources prescribe a source whose numerical cofactor c is largest; call
that cofactor c*. If its prescribed point is outside B, it supplies c*
in addition to the P-core demand. If it lies in B, the intersection saves
one point in the union of B with the core cover. Use that saving to select
a multiple of c* outside B. Such a point exists because c*<=M/P and P>=11.
It may coincide with another core point, which causes no problem.

In either case at most r+m points cover the old P-free sources, all core
demand, and one copy of c*. To cover the remaining product Q of the other
m-1 cofactors, avoid only B and the one point accounting for c*. It is
unnecessary to avoid the other core points: Q uses only primes 2,3,5,7,
whereas the core cover is used only for P.

It is therefore sufficient to factor Q into k factors with capacities

    floor(M/(r+2)), ..., floor(M/(r+k+1)).             (1)

This proves the first test in core_cover in close_one.cpp.

## Two additional core tests

### Separate P cover

Let D_P be the total P-demand, and choose k_P such that
S_P(M,k_P)>=D_P. Cover the old P-free sources in at most r points and the
P-demand in at most k_P points. The product of all m small cofactors can
overlap the P-cover and need only avoid the old cover. Hence it suffices
to pack that product into 9-r-k_P factors with capacities

    floor(M/(r+1)), ..., floor(M/(9-k_P)).            (2)

### Divide the whole P-containing group by P

The m divided sources a/P are distinct positive integers. The multiples
of P in I, after division by P, contain a consecutive interval of length
at least max(a/P). Apply the known g(m) bound to the divided sources.
If the number 1 occurs, omit it and use the corresponding smaller-n bound.
Pad the chosen quotient set to at least m points; there are at least m
quotients available, and g(m)>=m. Multiplication back by P covers the
original m sources, including the m removed P-factors.

This takes at most g(m) points. The product of the z P-free sources can
then be packed into the remaining 9-g(m) fresh factors, with capacities

    floor(M/(g(m)+1)), ..., floor(M/9).              (3)

Tests (1)--(3) are only sufficient tests. A failed packing attempt causes
the enumeration to retain the case; it never removes an unproved case.

## Configuration envelopes before source-set enumeration

Fix M and P and a current pool of possible sources, including M. For a
proposed support size m, list the cofactors of all P-containing candidates,
with multiplicity if two distinct sources have the same cofactor. Remove
one fixed candidate with the largest numerical cofactor.

For any actual selection of m sources, prescribe its largest cofactor,
using the fixed candidate if it is selected. The other m-1 cofactors
belong to the candidate pool with that fixed largest candidate removed.
This remains valid if the fixed candidate was not selected and if there
are ties. Thus for each q in {2,3,5,7}, the q-rough part of Q is bounded
by U_q, the product of the m-1 largest q-rough parts in the reduced pool.
The q-rough part means the factor supported on primes >=q.

For one bin, U_2 no greater than its capacity proves (1). For two bins,
place prime factors in descending order, into any bin in which they fit.
If q is the first failed factor and the capacity denominators are j_1,j_2,
the q-rough part must be at least

    T_q = q * product_{j in {j_1,j_2}} max(floor(M/(jq))+1,q).

Both bins are nonempty at failure: in these cases m>=5 distinct multiples
of P imply M>=5P>=55, and both capacities in (1) are at least 7. Hence
U_q<T_q for all four q proves successful packing for every possible set
with that support size. All products and comparisons are exact integers.

The allowed-support bitmask records only support sizes not closed by this
envelope. A support size with too few available P-containing or P-free
sources is also omitted. This envelope is applied to the original pool,
after the initial pair filter, and after forced-multiple elimination.

## Complete finite enumeration

Because M<9P^2, the bound on the maximum for a fixed P is

    M <= min(24696,9P^2-1).

If M>=1890, the retained cases have 9P<=M, so P<=2744. If M<1890, three
distinct multiples of P imply P<=M/3<630. Therefore trial-generating
every prime 11<=P<=2744 is complete.

For each such P, the program generates every possible source as c, Pc,
or P^2c with c 7-smooth, and every possible maximum M from that same list.
It keeps M>=3P and omits only the already closed M>=1890, M<9P case.
There are exactly 59,982 resulting (M,P) configurations.

For each configuration the possible nonmaximum sources are precisely
the composite generated integers a<M with 7a>M. The mandatory source is M.

### Pair filter

If the product ab of two source candidates packs into three factors with
capacities floor(M/7), floor(M/8), floor(M/9), cover the other five sources
in six points and append those three fresh factors. Therefore every pair
in a counterexample must fail this sufficient test.

First remove every a whose pair with M succeeds. Then construct the graph
whose edges are the remaining pairs for which the test has not found a
packing. A possible counterexample is a seven-clique including M.

### Forced-multiple closure

Every selected a forces all ka<=M. Inspect candidates in descending
numerical order. Remove a if one of its forced multiples has been removed,
is missing from the pool, or if two forced sources form a successful pair.
All forced multiples are larger than a, so one descending pass suffices.
The envelope is then applied to the surviving pool.

The recursion selects the smallest available next source and immediately
adds all its not-yet-selected forced multiples. It discards a branch if
a forced source was already excluded, if there would be more than seven
sources, if too few compatible candidates remain, or if no allowed P
support can be reached. Available candidates are intersected with every
newly selected source's bad-pair neighborhood. Thus every generated set
is a closed seven-clique and every closed seven-clique is generated by
its sequence of least not-yet-forced sources. Finally gcd(A)=1 is required.

The complete configuration counts are:

| Outcome | Configurations |
|---|---:|
| Closed by the original cofactor envelope | 24,796 |
| Closed after the pair-with-M filter | 34,408 |
| Closed after forced-multiple elimination | 8 |
| No primitive closed seven-clique remains | 147 |
| At least one primitive closed seven-clique remains | 623 |
| Total | 59,982 |

The remaining 623 configurations have M<=735 and P<=59. They contain
7,006,656 actual source sets and 658,925 distinct product-demand vectors.
These counts include every retained set, not a random or bounded-shift
sample.

## Demand compression and universal witnesses

For each configuration the program records the five-coordinate demand

    (D_2,D_3,D_5,D_7,D_P).

Whether an interval admits a product cover depends only on this demand
and M. A successful cover for a coordinatewise larger demand also covers
a smaller demand. It is therefore enough to retain all coordinatewise
maximal demand vectors. The supplied skyline.cpp performs this exact
operation: descending lexicographic order handles the first coordinate;
a three-dimensional prefix-maximum Fenwick tree queries dominance in the
next three coordinates and stores the last coordinate. A discarded point
is dominated by a previously retained point.

All source exponents fit in seven bits per coordinate. For example,
7 floor(log_2 24696)<=98<128; the other coordinates have smaller bounds.
The product-memo keys therefore have no carries or collisions. Reusing a
successful product test for a different source set with the same product
is legitimate.

There are 120,285 maximal vectors covered by the core tests above, by
separate prime covers, or by ordinary nine-bin packing. The portable
verifier rechecks each of these vectors in Python, including its actual
seven-source witness and the appropriate sufficient covering test.

There are 252,176 other maximal vectors. Of these, 252,175 have an explicit
cumulative-GCD certificate in slots9.txt or slots9_extra.txt. The remaining
vector is covered by the hand lemma in the next section.

### Cumulative-GCD certificates

A list h_1,...,h_l with l<=9 proves a cover if its product covers the demand,
each h_j<=M, and

    gcd(h_1 ... h_{j-1},h_j) <= floor(M/j).

Inductively suppose the selected points cover H=h_1 ... h_{j-1}. If a
fresh multiple of h_j exists, append it. Otherwise all interval multiples
of h_j are selected, so the selected product is divisible by h_j and H,
and hence by lcm(H,h_j). A fresh multiple of gcd(H,h_j) exists by the
displayed bound. Appending it supplies Hh_j. This proves the certificate.

The verifier checks every slot integer, every cumulative GCD, and final
divisibility using unbounded Python integers. The slot-search procedure
and its node limits are not trusted or rerun by the verifier. The files
contain 252,105 and 70 certificates respectively, all with distinct keys.

## Final hand lemma: M=55

The only remaining demand is

    2^4 * 3^9 * 5^2 * 11^4.

One representative source set is {22,27,33,44,45,54,55}. We prove directly
that every interval of 55 consecutive positive integers has a nine-point
cover of this product.

Choose two consecutive multiples u,v of 27 in the interval. At least two
exist, and they differ by 27, so exactly one is even. They supply 3^6 and
at least one factor 2.

Choose a fresh multiple w of 18. At least three multiples of 18 exist;
at most one of u,v is divisible by 18. Then choose a fresh multiple t of 6;
at least nine exist, and only three points have been selected. The four
distinct points u,v,w,t together supply 2^3*3^9.

Choose a multiple s of 50, which exists because 50<=55. If s is new,
append it; it supplies the remaining factor 2 and 5^2. If s is already
one of the four selected points, the factor 5^2 is already present; append
an unused even point to supply the remaining factor 2. Such a point exists
because there are at least 27 even interval points. Thus at most five
points cover 2^4*3^9*5^2.

Finally choose four distinct multiples of 11, of which there are at least
five. Unite them with the preceding five-point cover. The two demands
involve disjoint prime sets, so intersections are harmless. The union
has at most nine points and covers the full demand.

An optional independent prime-power residue checker also verified this
case, but the finite certificate does not depend on that checker.

## Portable replay

Run in this directory, or from any other working directory:

    python /path/to/one/verify_one.py

Required files are verify_one.py, close_one.cpp, skyline.cpp, slots9.txt,
and slots9_extra.txt. Python 3 and a C++17 compiler are required. No
external Python packages, network access, existing executable, generated
frontier file, or slot-search code is required.

The replay regenerates every configuration and every retained source set,
recomputes demand maxima, checks all 252,175 GCD lists independently,
rechecks all 120,285 other maximal vectors in Python, and verifies that
the only uncovered-by-slots vector is precisely the hand-proved M=55
demand. It writes verification_result.json and reports PASS only when
all these checks succeed.

This completes the one-large-prime branch, subject to the explicitly
listed global reductions and small-n bounds.
