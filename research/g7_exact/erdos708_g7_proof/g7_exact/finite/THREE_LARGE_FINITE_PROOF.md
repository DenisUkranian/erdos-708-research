# Complete finite treatment of three large primes for the target g(7) <= 9

24 November 2026. This note proves that the finite three-large-prime residue is empty. It is one part of the complete seven-source argument, not by itself a proof for all prime-support classes.

## Dependencies and counterexample normalization

Use the established g(6)<=8, the two-source peeling and core-bank lemmas, the audited support-three elimination in `../three/SUPPORT_THREE.md`, and the independent large-M cutoff. Choose a hypothetical counterexample with least M, then with maximum source sum at that M and its fixed target interval.

Its gcd is one. If a prime divides all seven sources, divide both the sources and the M/p consecutive target p-multiples by p. If quotient 1 occurs, discard it and apply g(6)<=8; otherwise use minimality of M. Pad the resulting quotient cover to at least seven points before multiplying by p. There are at least seven available quotient positions, and padding remains within the nine-point budget. This supplies the required seven factors p and contradicts the counterexample.

Maximum source sum implies closure under every integer multiple at most M. Hence every source a satisfies a>M/7: otherwise its first seven multiples exhaust the seven-element set (or eight multiples are forced), giving gcd a>1.

Assume exactly three large primes p<q<r, all at least 11. Support-three elimination implies each occurs in at least four source integers. The earlier peeling reduction gives p²,q²,r²>M/9 and at most two large-prime occurrences per source. All remaining factors are 7-smooth.

Because two supports of size at least four in a seven-element set intersect, all three pair cores pq,pr,qr occur. Thus

    qr <= M < 9p²,

and q²<M. This bounds every prime triple for M<=24696 and also implies pqr>M. A large-prime core is one of

    1,p,q,r,p²,q²,r²,pq,pr,qr.

Enumerating seven-element multisets of these types with source support at least four at each prime yields exactly 46 patterns. They comprise 21 patterns with no zero or singleton core, 18 with one singleton, six with two singletons, and one with a zero core. The latter has each of pq,pr,qr twice.

## Complete finite source envelopes

The C++ checker `three_large_envelope.cpp` enumerates every prime triple satisfying qr<=24696 and qr<9p². There are 6294. For each triple it takes every possible M in [qr,min(24696,9p²-1)] that is a listed core times a 7-smooth integer. This covers every possible source maximum.

For core d, its eligible smooth coefficients are exactly

    C_d(M) = {c 7-smooth : M/7 < dc <= M}.

A pattern with m_d sources of core d is discarded only if fewer than m_d coefficients are available, or none of its present types can supply the maximum M. Different core groups cannot give equal source integers because their full large-prime parts differ. This is a complete relaxation of all actual normalized counterexamples, and may include extra patterns.

For a small prime ell in {2,3,5,7}, let R_ell(c) be the part of c supported on primes at least ell. For each core group the product of the m_d largest available values R_ell(c) is an upper bound for every actual selection of distinct coefficients. Multiplying these group bounds gives a universal upper envelope for the ell-rough part of the entire small-factor demand.

When a prescribed source is chosen with the largest *integer coefficient* within a selected nontrivial core group, its remaining m_d-1 coefficients all lie below that chosen coefficient. They therefore belong to C_d(M) with its absolute largest integer deleted. The product of the m_d-1 largest rough values in this reduced list bounds the residual group's rough demand. This argument is valid independently at every rough-prime threshold; it does not assume that the numerically largest total coefficient product is divisible by all smaller products.

## Core covers and the spare-bank improvement

For each large-core type d, select m_d distinct target multiples of d. Such a bank exists because m_d<=floor(M/d). The three-prime core-bank theorem supplies a core cover of at most m+1 points, where m is the number of nontrivial source cores, and it may retain a prescribed full-source multiple z from a nontrivial bank.

There is at most one target multiple T of pqr, because pqr>M. The only positive cycle in a three-prime core graph is the triangle formed by pq,pr,qr. Loops and singleton cores do not contribute a positive cycle cost in the bank deficit formula.

If an edge bank d in {pq,pr,qr} has floor(M/d)>m_d, choose all its representatives outside T. This destroys the triangle and improves the core bound to m. If a prescribed point z belongs to another bank, it is retained. Thus any spare edge bank suffices without a prescription, and any spare edge different from the prescribed bank suffices with a prescription. Two spare edges allow an arbitrary prescribed bank.

A separate bound uses the union of single-prime covers for the large-prime demand D=(D_p,D_q,D_r). The guaranteed supply in k points for prime p is

    min(k,floor(M/p)) + min(k,floor(M/p²)).

No source has a large-prime cube, and ignoring additional target valuation is safe. Summing the least sufficient k over the three primes gives an independent core cover bound.

If z is prescribed, its valuation at a prime is at least the source-core exponent e in {0,1,2}. For each possible capped actual valuation v=e,...,2, remove z from the interval counts and require fresh supply D_p-v. This uses lower counts

    max(0,floor(M/p)-[v>=1]),
    max(0,floor(M/p²)-[v>=2]).

Take the worst required fresh cardinality over v=e,...,2 and sum it over the primes, adding one for z. Actual valuations greater than two only improve this bound. The checker takes the better of this construction and the bank construction.

## Combining core and small-prime covers

The large-prime demand and the full small-prime demand are coprime. Therefore independent covers of sizes c and t can be united into at most c+t points even when their target sets overlap.

When a full-source point z has already supplied a credited smooth coefficient c*, only that point must be avoided by the cover of the remaining small product Q/c*. All other core points were allocated solely to large primes. Consequently t small bins may have capacities

    floor(M/2), floor(M/3), ..., floor(M/(t+1)).

Choose their target representatives successively outside z and previously chosen small representatives. They may coincide with other core points without double-counting any allocated small valuation. Without a credited coefficient, the ordinary capacities are floor(M),...,floor(M/t).

For any of these capacity lists floor(M/j), descending placement of 7-smooth factors fails at a prime ell only if the remaining ell-rough product is at least

    ell * product_j max(floor(M/(j*ell))+1, ell).

Every ell fits every empty bin in the finite range, since M>=qr>=221. Thus strict comparison of every rough upper envelope with this threshold proves the packing for every actual coefficient choice. One-bin cases additionally use the immediate bound that the whole required product is at most the single-bin capacity.

## The one-zero-core pattern

This pattern has a smooth source a0 and two sources of each pair core. Put L_d=floor(M/d). The remaining nontrivial smooth product after crediting its largest coefficient is at most

    W = product_{d=pq,pr,qr} L_d(L_d-1) / max_d L_d.

Cover a0 at a point b0 and cover the core while retaining a full-source point z supplying that largest coefficient. If z=b0, the overlap saves one point, which can be spent on a fresh coefficient multiple. Thus a0 and the credited coefficient are supplied at two distinct allocated small-prime points, within the sum of the old-source and core budgets.

The pattern is covered if 3W<=M: the core uses at most seven points, the union accounting uses at most eight, and one new multiple of the remaining product can avoid the two allocated points.

If at least two pair banks are spare, the core uses at most six points while retaining z. There are then two remaining small slots with capacities floor(M/3),floor(M/4), avoiding only the two allocated points. Descending 7-smooth packing succeeds whenever M²>=84W, because failure at ell<=7 would force a product strictly greater than M²/(12ell)>=M²/84.

Both tests are implemented with exact integer arithmetic.

## Complete run and final two classes

The full envelope scan returned:

- 6294 prime triples;
- 656193 eligible maxima across those triples;
- 850366 admissible core-pattern classes;
- 850364 classes proved directly by the preceding universal criteria;
- exactly two unresolved classes.

Both residual classes have p=11,q=13,r=23 and core pattern

    r,r,pq,pq,pq,pr,qr.

Their maxima are M=1012 and M=1035. Thus every residual source set has form

    {23u,23v,143a,143b,143c,253d,299e},

where u,v are distinct eligible 7-smooth coefficients, a,b,c are distinct eligible coefficients for 143, and d,e are eligible coefficients for 253,299. The program `close_three_residual.py` enumerates all choices, requires the actual maximum to equal M, and then applies only necessary gcd-one and upward-closure filters.

There are 17640 choices with the correct maximum and 1096 normalized source sets. Their demands form 347 distinct (M,demand) pairs. Every one of the 1096 source sets has a verified sequence of at most nine cumulative-GCD slots. The certificate checker verifies

    1<=h_j<=M,
    gcd(product_{i<j}h_i,h_j)<=floor(M/j),
    product(A) divides product(h_j).

These are universal interval certificates, not sampled-shift calculations. The failure list is empty.

## Conclusion and artifacts

Under the audited support-three reduction and counterexample normalization, no three-large-prime counterexample exists with M<=24696. Combined with the independently audited large-M theorem, the three-large-prime case is eliminated completely.

Reproduction files:

- `three_large_envelope.cpp`, `three_large_result.json`, `three_large_unresolved.tsv`
- `close_three_residual.py`
- `three_residual_candidates.json`, `three_residual_slots.json`, `three_residual_failed.json`

The finite envelope implementation was independently reviewed by another agent before the two residual classes were certified.
