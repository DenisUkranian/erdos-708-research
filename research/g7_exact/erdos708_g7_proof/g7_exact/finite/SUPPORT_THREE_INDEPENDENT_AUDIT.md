# Independent audit of support-three elimination in the three-large-prime case

The revised `g7_exact/three/SUPPORT_THREE.md` is valid, subject to the previously established small-n bounds and the stated maximum-sum counterexample selection. This review includes the corrected C2 step and explicit exclusion of u=1 in D2.

## Four-atom lemma

The pair banks form K4 with only QR repeated. Two distinct positive-cycle points can only realize triangles PQR and QRS: every other pair of distinct cycles shares a single-use bank, forcing equality of the points. Their Q- and R-deficits are at most two each, so available squares save two picks from the provisional nine-point budget. A single rank-two point is K4 minus an edge; at least one of Q,R,S has degree three and total deficiency at most two, saving one pick. A rank-three point contains all six edge types; Q,R,S each have deficiency at most two, and their squares save three picks. The prescribed QR bank point is retained throughout.

For a composite atom S, the quantity max{k:S^k divides b} need only be superadditive under multiplication, which it is. Counting complete atom units therefore gives a sufficient divisibility certificate. Pairwise coprimality of the atoms makes the independent atom bookkeeping sound. At most ten points are ever provisionally needed, and at least eleven multiples of each atom exist, so every ordinary repair is available freshly. Squares already selected can only improve the baseline supply.

## Classification

The high support-three prime has distinct cofactors below sqrt(M), so each pair product used for compression is at most M. If all three compressions are blocked, the large-prime parts of its three cofactors must be (q,q,r) or (q,r,1). Both resulting source families follow from the support restrictions. In C1 the remaining smooth product is 8t^3; its use with a prescribed full source is valid because the chosen core contains only primes at least eleven.

In C2 the atom s is smooth, so a coefficient c at a prescribed point must not be credited independently of the atom demand. The revised proof correctly covers the entire coefficient a^3*b^3*c in a fresh point outside the atom cover when M>=9*a^3*b^3*c. The remaining family has M<4608 and is handled by explicit certificates, removing that double-counting issue.

For a low support-three prime, the square-gain lemma removes the all-simple case. The two-square-source case reduces to an unblocked compression of a high support-three prime or to the same square-gain lemma. In the one-square-source case, blocked products uqa and urb force two upward-closed banks. If u=1, the first bank already has at least p>=11 members, impossible; hence u>=2 and u does not divide p. The three p-sources lie outside both banks. The banks are disjoint because their common multiple would require at least eleven multiples of each modulus. The subsequent support count forces Nq=Nr=1 and exactly two qr-sources. Consequently p is 11 or 13 and M<2704, as stated.

## Finite coverage and certificates

The low-case enumerator uses a superset of the proved q,r<208 range, every coefficient in [1,8], all possible p in {11,13}, and all stated necessary inequalities. Ordering q<r and c<d loses no source set because the respective roles are interchangeable. Its upward-closure filter is a necessary property of the selected counterexample.

The high C2 enumerator covers q,r<=67, p<=418 (using a harmless superset through 419), 2<=s<=67 with s smooth, a,b in {1,2}, and c in [1,8]. The omitted a=b=1 case is already analytically covered because the extra coefficient is at most eight and M>=143. Every other discarded inequality is a necessary condition of the residual family.

A fresh independent execution of `verify_support3.py` returned PASS for all 162 low-case and 283 high-C2 nine-slot certificates, 445 in total. Each checks length at most nine, all slot bounds, every cumulative-GCD overlap, and exact divisibility of the source product. These certificates apply to every interval shift.
