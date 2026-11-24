# Proof audit and reproducibility: Erdős--Surányi g(8)=11

## Scope and dependencies

This bundle establishes the new finite step g(8)<=11 as a computer-assisted theorem **conditional on** the previously established g(7)<=9, g(6)<=8, and g(5)<=6. The g(7),g(6) proofs are included as a nested zip. The original g(5) theorem is external and cited in the PDF. The lower g(8)>=11 is unconditional and demonstrated by an explicit example.

## Finite source enumeration: no sampled shifts

For each 7-smooth M<11538 with Omega(M)>=3, every surviving counterexample must use seven distinct 7-smooth numbers a<M with Omega(a)>=3 and 11a>M. If the product of a and M packs in bins floor(M/j), j=9,10,11, the other six sources are covered by g(6)<=8, and these three bins produce three distinct free interval points. Accordingly a may be omitted. Similarly, a surviving pair (a,b) cannot pack in those bins; a surviving triple (a,b,c) cannot pack in five bins with j=7,...,11, because g(5)<=6 takes care of the remaining five sources. The C++ enumerator applies these only as one-sided tests: a successful packing returns an explicitly legal factorization; an unsuccessful packing is *not* assumed to prove impossibility.

The candidate sets have at most 54 vertices, permitting a 64-bit adjacency mask. The DFS visits all ordered increasing combinations of seven surviving vertices. Pairs are filtered by graph edges and triples by masks indexed by the previously selected pair. Every seven-vertex set appears once if it survives, and contributes one vector of prime exponents with the maximum M held fixed. Counting yields 50 maxima, max M=252, 1,691,461 surviving eight-source sets, and 57,515 distinct valuation vectors.

## Universal slot certificates

For a sequence of h_j<=M, let H_{j-1}=product_{i<j} h_i. If gcd(H_{j-1},h_j)<=floor(M/j), one can choose one new interval point at the j-th step and have product of chosen points divisible by product_{i<=j}h_i. Proof: if a fresh multiple of h_j exists, choose it; otherwise some chosen point was a multiple of h_j, so lcm(H,h_j) divides the current product. There are at least j multiples of gcd(H,h_j) and at most j-1 points used. A fresh such multiple supplies the missing gcd and hence H*h_j. Factors h_j=1 are harmless idle steps.

`make_gcd_certificates.cpp` performs exact finite-state reachability on the four prime-exponent coordinates, preserving predecessor pointers. Every emitted certificate is independently checked by `verify_all.py`, which recomputes all p-adic valuations and every cumulative gcd inequality with unbounded Python integers; no trust in a floating-point solver or pre-computed hash is needed. The checker validates set equality between all enumerated demands, the verified slot demands, and the 28 residual CRT demands.

## Complete CRT residual check

For each of the 28 remaining (M,D2,D3,D5,D7) with M<=54, for each active prime p let h=min(Dp,floor(log_p M)) and q=p^h. For each x mod q, record the length-M valuation row of min(v_p(x+j),h). Distinct primes have coprime q; CRT shows every combination of these rows can occur (or is harmlessly overcounted). The recursive checker considers all such combinations, using a rigorously upper-bounded independent-prime suffix cost for safe pruning. If it cannot prune, it runs exact integer multicover over the positions, grouping equal valuation profiles while preserving their capacities. Each successful branch is a legitimate <=11 cover. It reports `ALL_PASS rows=28` after 2,800 branch nodes and 92 exact multicover calls.

The suffix cost is safe even if selected positions for different primes intersect: each prime's entire required valuation is covered by its own selected positions, so taking a *union* cannot reduce its supply. When several prime-power requests p^Dp<=M are combined into one cofactor bin, the bin is the product of powers of **distinct** primes and its value is <=M. One multiple always exists in the interval; if multiples chosen for different bins coincide, their coprime requests are simultaneously satisfied by that one position, so no demand is lost.

## Lower witness

A={37^2,37*41,37*43,37*47,37*53,41*53,43*53,47*53}, M=2491, x=246043396342067361. Its demands are (6,2,2,2,4) at primes (37,41,43,47,53). The central interval point b0=x+1246 has active valuations (2,1,1,1,1). Every other point carries at most one active prime because each pair of these primes has product >=37*41=1517 and all offsets from b0 have absolute value <=1245. Further, no other point is divisible by 37^2 (difference >=1369), and no interval point is divisible by 53^2: b0 mod 53^2 is 1378, and the nearest such multiples are at displacements -1378 and +1431, both outside the interval.

If b0 is chosen, remaining needs (4,1,1,1,3) require at least ten further points because every other point supports only one active prime and 37/53 with exponent<=1. Total >=11. If b0 is omitted, at least six pure 37-points, four pure 53-points, and at least one for each 41,43,47 are required: >=13. Finally, offsets 25,27,62,80,99,133,136,1199,1203,1205,1246 attain the demand with exactly eleven points. The lower bound is thus elementary, and `src/lower8.cpp` additionally computes the exact optimum 11 via 0/1 dynamic programming.

## Limitations

This is a computer-assisted mathematical argument, not a Lean formalization of g(8). Independent journal peer review has not been undertaken. Its global upper conclusion inherits the validity of the previously supplied g(7)=9, g(6)=8 proofs and the published g(5)=6 result. It does not establish the unrestricted asymptotic Erdős 708 conjecture.
