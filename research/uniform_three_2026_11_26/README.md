# An unconditional upper bound of (3+o(1))n for the Erdős–Surányi problem

Let A consist of n distinct integers in [2,M], with maximum M. For every interval I of M consecutive positive integers, write H(A,I) for the least size of a subset whose count of multiples of each prime power equals or exceeds its count in A. This condition implies the required product divisibility.

**Theorem.** Uniformly over all source sets, source densities and interval shifts,

    H(A,I) ≤ (3+o(1))n   as n → ∞.

In particular the at-most-cardinality version of Erdős Problem 708 satisfies limsup g(n)/n ≤ 3. This is a written research proof. The coefficient two remains open. A separate non-asymptotic conclusion in the supporting argument is H≤4n−3 for all sufficiently large M. The theorem on this page does not depend on the supplementary price or average-case results.

## 1. A matching with two or three specific atoms omitted

A full atom means p raised to its full exponent in one source. Fix 0<ε<1/4 for the proof. If n≥M/3 take the entire interval. If M≥(2n)^3, the [two-block bound](../cofactor_flow_2026_11_26/README.md) already gives 2n. Thus assume n<M/3 and M<(2n)^3.

Rows with at most three distinct primes need at most three individual atom repairs. For every other row write r<p<q for its three largest prime bases, and d₂ for the cofactor after removing the full p- and q-atoms. Call the row exceptional if M/d₂<r^(2+ε). From ordinary rows remove the two full atoms; from exceptional rows remove the three full atoms based at r,p,q. Denote the specified remaining cofactor by d₀. Temporarily discard rows with q≤Q(ε), a sufficiently large fixed constant chosen below. They number at most (1+log₂ M)^π(Q), each with at most π(Q) atoms; their combined repair costs o_ε(n).

The remaining d₀, counted once for each row, have distinct representatives among their respective multiples in I. The [prefix and rough-number argument](PREFIX_SIEVE.md) gives this assertion for the **specified** cofactors. Explicitly, for any subfamily S take the union T of its cofactor banks. Unless T=I, read each row's prime factors in ascending order, with repetitions, and stop at the first prefix d all of whose target multiples belong to T. It occurs no later than d₀. With t the last prime in d, the remaining quotient is composite and has no prime factor <t. For ordinary rows M/d≥t^(2+ε) and for exceptional rows M/d≥t³. In both cases M/d≥q>Q. Multiples of d in I with quotient free of primes <t have the same first trapped prefix; hence these target classes are disjoint. For H₀=M/d sufficiently large and H₀≥t^(2+ε), the lower linear sieve and the Buchstab estimate show that every H₀-window has at least as many such rough integers as there are composite rough integers ≤H₀. The proof, including uniformity for large log H₀/log t, is in the linked note. The resulting |T|≥|S| proves Hall's condition. Credit only the cofactor atoms to its row's representative, called an anchor. The extra freedom of the alternative-cofactor graph used elsewhere for an exact 4n−3 bound is unnecessary here.

## 2. A label for an exceptional row

In an exceptional row p and q occur to the first power: otherwise p²q or pq² exceeds r³, whereas the product of the removed atoms is ≤M/d₂<r^(2+ε). Also q<r^(1+ε) because p>r. Choose the two numerically smallest of the three removed **full atoms**. These are both first powers. Indeed if the exponent of r is greater than one then its atom is at least r²>q. Write their product v=st, with s and t distinct primes. The third removed atom is set aside for one ordinary repair.

There are three uniform bounds on these labels. All constants in their O(ε) bounds can be taken absolute by first fixing ε and then taking Q(ε) sufficiently large.

1. For a label containing s, the other base lies between s^(1/(1+ε)) and s^(1+ε). The reciprocal sum over all primes in this band is O(ε) by Mertens' theorem; all bases exceed Q^(1/(1+ε)).
2. The number m_v of exceptional rows giving label v is at most C ε M/v. Each such source is a multiple of v times a third, distinct prime in the same band relative to s. Sum the canonical floor counts of these multiples.
3. For each s dividing v, v²≤M s. In fact, if u₁≤u₂≤u₃ are the three full atoms in numerical order, (u₁u₂)²≤(u₁u₂u₃)u₁≤M u₁. Also v≤M^(2/3). Whenever two labels share a prime their lcm is ≤M by the preceding square bound.

## 3. Pairs already demanded by many source rows

Put a label v in V if at least (4/5)M/v rows of the **entire** A are multiples of v. Write λ=Σ_{v∈V}1/v. For U uniform in the canonical interval [1,M], let N(U) count the distinct labels of V dividing U. Then

    E[N 1_A] ≥ (4/5)λ,
    E[N²] ≤ λ + λ² + C ε λ.

The diagonal costs at most λ and distinct coprime pairs cost at most λ² by the canonical floor counts. For v fixed, the sum over distinct labels w sharing a prime s with v of 1/lcm(v,w) is bounded by (1/v) times the reciprocal sum over the possible other primes of w. Sum the O(ε) bound of Step 2 over the two choices of s and over v. This includes ordered pairs as required.

Cauchy–Schwarz now gives (16/25)λ²≤(n/M)[λ²+(1+Cε)λ]. Since n/M<1/3, this implies λ≪n/M, including λ=0. It follows that Σ_{v∈V}m_v≪ε n. Discard the pair assignment for those rows and pay their three omitted atoms individually, one position above the three-per-row budget including the anchor.

## 4. Assigning the remaining pairs

For v outside V, use the multiples of v in I except those anchors *credited* with both its primes. Each excluded point belongs to a distinct source divisible by v. Thus at least floor(M/v)−(4/5)M/v ≥ M/(6v) positions remain for large M, since M/v≥M^(1/3). For each exceptional row still under consideration, choose a position uniformly in its allowed set, independently across rows.

Mark a conflict between rows if they choose the same position and their labels have a prime in common. For labels v,w of such a potential pair, independence, the bound on the allowed sets and lcm(v,w)≤M give

    Pr(same position) ≤ 72 gcd(v,w)/M.

This includes identical labels. For a fixed row of label v, summing probabilities over rows of that same label costs O(m_v v/M)=O(ε). For distinct labels with common prime s, sum over w=sℓ: the bound is O((s/M) Σ_ℓ m_{sℓ})=O(ε Σ_ℓ 1/ℓ)=O(ε²). There are only two choices for s. Some joint assignment therefore has O(ε n) conflicting pairs. Discard both ends of every conflict at a cost of at most one extra repair position per discarded row above the three-per-row budget.

## 5. Counting distinct positions and repairing levels

The surviving pairs at each position are mutually coprime. At a new position, one selected integer pays every assigned pair there, at cost at most one per pair. At a position already selected as an anchor, the anchor is credited with at most one prime of each assigned pair by construction. Give credit there to the pair's other prime or to both if possible. For each such pair at most one additional singleton atom needs repair, and no new position was used by the pair itself. This accounting works with multiple pairs at one anchor. It charges at most one position per surviving pair in addition to the original anchors. Every exceptional row also pays for the third omitted atom.

For clarity, at any prime-power level the credited positions are distinct for the source atoms credited at that prime. Hence the positive count shortfall is at most the number of remaining unpaid source atoms of its base prime. For each prime, add as many positions of greatest remaining valuation as needed for its worst shortfall over all levels. The level sets are nested and the entire interval has at least the required count at every level. Union these choices over the primes. This justifies all individual repairs together without duplicating credit.

The resulting bound is 3n+Cε n+o_ε(n) with an absolute C. First take n→∞ at fixed ε, then send ε→0. No assumption on the shift survives in the bound.

The [finite replay](verify_pair_accounting.py) checks the local accounting and the constructed level covers in four concrete windows, including an interval centered near a common multiple. The asymptotic conclusion uses the argument above.

## The remaining coefficient and supporting notes

The ordinary rows in Step 1 still use one anchor and as many as two separate repairs. Their two largest prime bases may lie on widely separated scales. Step 2's narrow-band estimates and Step 4's pair assignment do not give one repair per ordinary row. This leaves the gap from three to two.

* [Rough-prefix comparison and the exact four-per-row bound](PREFIX_SIEVE.md)
* [Marked primes and an exact two-per-row theorem below the normal number of distinct prime factors](MARKED_PRIMES.md)
* [Further worst-shift source classes](POWER_CORE.md), [ascending prefixes](ASCENDING_PREFIX.md) and [bounded rough rank](BOUNDED_ROUGH_RANK.md)
* [Two-spare price comparison](TWO_SPARES.md), [multiple spare primes](MULTIPLE_SPARES.md) and [fractional-price reserve](SMOOTH_RESERVE.md)
* [Prescribed prime phases](FIXED_PHASES.md), [quantitative exceptional shifts](EXCEPTIONAL_SHIFTS.md), and [a counterexample for an auxiliary kernel](KERNEL_OBSTRUCTION.md)
* [Typical source sets at every shift](TYPICAL_SOURCES.md)
