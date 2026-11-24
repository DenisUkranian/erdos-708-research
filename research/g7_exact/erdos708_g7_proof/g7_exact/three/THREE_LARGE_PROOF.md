# Complete closure of the three-large-prime case for g(7)<=9

24 November 2026. This is a component of the exact-g(7) proof, not a stand-alone claim that the zero-, one-, and two-large-prime cases have been completed here.

## Statement

Assume g(3)<=4, g(4)<=5, g(5)<=6, and the independently certified bound g(6)<=8. Choose a counterexample to g(7)<=9 with least possible maximum M, then a maximum-sum source set at that M and interval. Such a counterexample cannot have exactly three active primes at least 11.

## Reduction chain

1. Minimal M gives gcd(A)=1; maximum sum gives upward closure under integer multiples within [1,M]. Together these imply every source exceeds M/7. If a<=M/7, seven multiples force the whole set to have gcd at least a>1, while eight multiples would exceed its cardinality.

2. The prime-support and two-source-peeling lemmas in `g89_theory/core_reductions.md` give source support at least three, p^2>M/9, and at most two large-prime occurrences per source. The product of any three large-prime occurrences exceeds M for every M.

3. `SUPPORT_THREE.md` eliminates support exactly three when exactly three large primes are active. Its analytic cases use prime-group compression, the square gain, and the four-atom K4-plus-repeated-edge lemma. Two residual finite families have 162 and 283 eligible source sets, respectively. Every one has an exact universal-shift nine-slot certificate. The proof and all 445 certificates have independent audit and verification.

4. The global analytic cutoff `g7_exact/root/LARGE_M_CUTOFF.md` excludes M>=24697. Its proof was independently audited, including the source/core packing step, spare pair-bank avoidance, and saturated triangle cofactor bound. Thus only M<=24696 remains.

5. Each of the three active large primes now has source support at least four. On seven sources every two supports intersect, so all three pair cores occur. At most one large prime exceeds sqrt(M), since two high-prime supports would be disjoint and require eight sources. For sorted primes p<q<r, therefore q^2<=M, qr<=M, and M<9p^2.

6. There are 46 possible multiplicity vectors for the ten cores 1,p,q,r,p^2,q^2,r^2,pq,pr,qr: total seven sources, each prime's source support at least four. The finite envelope enumerates all such patterns, all eligible prime triples, and every possible actual maximum M, which must equal a core times a 7-smooth integer.

## Finite envelope and its predicates

`g7_exact/finite/three_large_envelope.cpp` checks 6294 prime triples, 656193 eligible maxima, and 850366 core classes. For every class it uses only sufficient universal-shift covering criteria:

* independent nested prime-power count covers for the large-prime demand;
* the at-most-m+1 core-bank bound, improved to m by avoiding the unique possible triangle point through a spare pair bank;
* a prescribed full-source point, with the remaining small-prime cover required to avoid only that point;
* independent small-prime covers united with a large-prime cover, valid because their required products are coprime;
* exact descending-factor-packing thresholds, bounded against the worst possible prime-prefix product over all distinct allowed cofactors;
* the separate one-smooth-source criterion in `ZERO_SOURCE_ENVELOPE.md`.

The numerical envelopes are upper bounds on the relevant prime-prefix products, not merely products of a few guessed source sets. The mathematical justification and source coverage were independently reviewed in `THREE_ENVELOPE_INDEPENDENT_AUDIT.md`.

The envelope closes 850364 classes. Its only two remaining classes have p=11,q=13,r=23, M=1012 or 1035, and multiplicities (0,0,0,2,0,0,0,3,1,1) in the ten-core order above.

## Exact certification of the last two classes

`g7_exact/finite/close_three_residual.py` enumerates their actual source sets: two numbers with core 23, three with core 143, one with core 253, and one with core 299. After imposing actual maximum, gcd one, and upward closure, 17640 raw choices reduce to 1096 eligible sets. There are 347 distinct (M,valuation-demand) combinations.

Every eligible set has a certificate of at most nine integers h_1,...,h_k satisfying

    1<=h_j<=M,
    gcd(h_1*...*h_{j-1}, h_j)<=floor(M/j),
    product(A) divides h_1*...*h_k.

The cumulative-GCD slot theorem turns each certificate into a cover for EVERY interval of M consecutive positive integers. No bound on the interval shift, numerical optimization, or unverified solver assertion is needed to check the certificates.

An independent program, `verify_three_residual_independent.py`, regenerates the source sets from pools of actual integers rather than importing the search routines. It reproduced all 17640 raw choices and all 1096 eligible sets, checked exact equality with the certificate set, and verified every slot inequality and final divisibility by integer arithmetic. Result: PASS.

## Reproduction

Run `python3 g7_exact/three/verify_all_three.py` from any directory. It regenerates both support-three finite families in a temporary directory, verifies all 445 support-three certificates, recompiles and reruns the complete finite envelope in an isolated temporary directory, checks that its unresolved output is exactly the two stated classes, and independently regenerates and verifies all 1096 final certificates.

Requirements are Python 3's standard library and a C++17 compiler. The code performing proof checks uses integer arithmetic. The search routines used to find the slot lists are not needed for verification.

Together, these steps exclude every three-large-prime counterexample under the stated preceding bounds and analytic lemmas.
