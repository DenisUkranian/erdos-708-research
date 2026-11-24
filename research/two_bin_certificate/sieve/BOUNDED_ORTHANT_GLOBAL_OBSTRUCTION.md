# Bounded mixed-orthant discrepancies still do not supply numerical floor laws

24 November 2026. This is an exact abstract obstruction to a proposed proof shortcut. It is not an arithmetic counterexample to Erdős 708 or to the coherent hyperbolic kernel.

## 1. The certified six-coordinate block

Use the 90-source/90-target integer-profile block from
`ep708_descent_20261124/variation/VARIATION_DESCENT_OBSTRUCTION.md`.
At threshold c=21/10 it has the uniquely globally maximizing price vector
(1/2,...,1/2), full tail of size 18, surplus 6/5, and exact raw source/selected-target demand 23 in each coordinate. Every nonzero formal cold quotient has surplus -23/10.

The existing rational certificate checker proves those statements. The following additional observation is elementary and exact.

For a threshold vector e in {0,1,2}^6, let s be the number of its positive coordinates. Let D(e) be the target orthant count minus its source count. Then:

* s=0,1,2: D(e)=0;
* s=3: D(e)=0 if every positive threshold is one, and D(e)=3 otherwise;
* s=4: D(e)=2 if every positive threshold is one, and D(e)=5 otherwise;
* s=5,6: D(e)=3 if every positive threshold is one, and D(e)=6 otherwise.

If a coordinate threshold exceeds two, both counts are zero. Thus every orthant discrepancy belongs to [0,6], and every discrepancy supported on at most two coordinates vanishes exactly.

For example, a pair of threshold-one coordinates has source count 3+6=9 and target count 6+3=9. If either pair threshold is two, both counts are six. A single threshold-one coordinate has count 25 on each side; a threshold-two coordinate has count ten on each side.

## 2. Pack many blocks into comparatively few coordinates

For each integer r>=6, greedily choose 6-subsets of an r-element coordinate set, subject to pairwise intersection at most two. Any chosen block forbids at most

    C(6,3) C(r-3,3)=20 C(r-3,3)

possible 6-subsets, since any forbidden set contains some triple in the chosen block. Consequently a maximal greedy family has cardinality L satisfying

    L >= C(r,6)/(20 C(r-3,3)) = r(r-1)(r-2)/2400.      (1)

Put one copy of the certified six-coordinate block on each chosen 6-subset. Extend each profile by zero outside its block, and concatenate the lists of source and target profiles. They are integer multisets of equal size

    M=90L.

Repeated profiles are allowed in this formal model, just as in the original obstruction. They are not asserted to be distinct actual integers in a prefix.

## 3. Globality and every exact row survive

For an arbitrary r-coordinate price vector w, the surplus of the concatenated system is the sum of the individual block surpluses:

    J_c(w)=sum_B J_c^B(w restricted to B).

Each summand is at most 6/5. Taking every used coordinate price equal to 1/2 attains all of these maxima simultaneously. The maximizer is unique on the used coordinates, because each block's maximum is unique.

At this genuine global maximum,

    n=18L,       J_c=6L/5,       F=39L.              (2)

The blockwise selected-target solutions concatenate to a primal optimum with all exact whole-coordinate row balances. A coordinate belonging to d blocks has source demand 23d and selected-target supply 23d.

All nontrivial cold exponent vectors are singleton coordinates. Conditioning on such a coordinate simply collects the corresponding quotient from each block containing it. The quotient surplus is therefore

    Q_p=-(23/10)*d<0.                               (3)

No new-tail, endpoint or clipping reserve appears in these formal quotient models.

## 4. Every mixed orthant discrepancy is still at most six

An orthant supported on one or two coordinates receives contributions only from blocks containing that support; every such block contributes zero discrepancy. If the support has size at least three, at most one block contains it, by the packing property. Any other block has a zero coordinate at some positive threshold and contributes zero on both sides. The preceding table therefore gives

    0 <= target_count(e)-source_count(e) <= 6         (4)

for every exponent threshold vector, independently of r, L and M.

Combining (1)--(2), J_c is Omega(r^3), while M=90L and J_c/sqrt(M) tends to infinity as r grows. It follows that genuine full-tail globality, complete row balances, negative formal cold quotients, and uniformly bounded mixed-orthant discrepancies do not imply either an O(r^2) bound or a square-root-in-M bound for surplus.

If one permits fractional profile masses, dividing all masses by six makes every orthant discrepancy at most one without changing the conclusion. The unscaled construction already uses integer multisets with an absolute rounding-error bound of six.

## 5. Precisely what remains missing

Actual arithmetic orthants have the main term floor(M/d), where d is the numerical product of the specified prime powers, and every target count is that integer or one more. The construction retains a uniformly bounded difference between the two counts but does not retain these common numerical main terms, the numerical ordering of distinct primes, or actual consecutive target positions.

Thus an argument based only on bounded orthant error after discarding the floor(M/d) main terms remains insufficient, even with unique globality. This does not refute a method that uses those numerical main terms, nor the size-coherent divisor kernel developed in this same research turn.
