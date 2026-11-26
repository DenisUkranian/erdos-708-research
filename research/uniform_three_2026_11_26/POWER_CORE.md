# Two atoms outside a polynomial-sized prime cutoff, at every shift

Write H(A,I) for the minimum number of distinct positions in an M-term interval I of positive integers sufficient to dominate all prime-power level counts of n distinct sources A in [2,M] with maximum M. For each row a suppose one can choose a divisor h with X=M/h such that all prime factors of h are at most z=X^c and a/h is supported on at most two prime bases, both strictly above z. Empty supports are allowed. Here c>0 is a sufficiently small absolute fixed constant. Then, uniformly at every source density and every shift,

    H(A,I) ≤ (2+o(1))n.

In particular, for h≤sqrt(M), the core may contain arbitrary primes up to M^(c/2) and arbitrary multiplicities, with up to two additional prime bases above M^c. The cutoff also applies when h>sqrt(M), with X=M/h. The assertion allows distinct h and distinct cutoffs in different rows.

**Distinguishing the cores.** Assign b to a prefix by processing its prime factors with multiplicity in ascending order. Starting at t=1, append the next prime p while p≤(M/(tp))^c, and stop at the first failure. If b=h v with h supported on primes through z and v free of primes through z, the prefix is precisely h. Indeed all primes of h come first and pass the test even at t p=h. The first prime of v fails it. Thus the target positions described for different cores h are disjoint.

**Capacity within one core.** From the quotient a/h, omit the larger full prime-power atom if two are present, the unique atom if one is present, and nothing if it equals one. Write q for the remaining factor. Thus q=1 or a power of a prime greater than z, and q≤sqrt(X). At each q there are at most 1 plus the number of prime powers through X/q possible rows, and therefore at most C X/(q log X) for an absolute C when X is large. Its available quotient targets have the form q v in the length-X quotient interval I/h with v free of primes through z. All quotient target positions must be integers; intervals here are cut out by half-open real intervals, so each unweighted divisibility count differs from length divided by modulus by at most one.

We use two standard consequences of the one-dimensional fundamental lemma. For c sufficiently small, an interval of length T≥sqrt(X) contains at least c₀ T/log z integers free of primes through z, with c₀>0 absolute, uniformly for sufficiently large X (the starting threshold may depend on fixed c). For any T≥1 the count is at most

    C₀ T [1/log z + 1/log(2T)]

for an absolute C₀ when z≥2. For completeness, use sieve level T^(1/2) with divisor remainders bounded by one. There is an absolute fixed K for which sieving to any 2≤w≤T^(1/K) gives between fixed positive constant multiples of T/log w, uniformly for large T. This follows from the fundamental lemma and Mertens' product with the total remainder O(T^(1/2+o(1))). For the lower bound take c≤1/(2K) and w=z. For the upper bound take w=min(z,T^(1/K)); bounded T is covered by increasing the constant. See [Ford, Sieve Methods Lecture Notes](https://ford126.web.illinois.edu/sieve2023.pdf).

Fix a nonempty collection S of q-labels at this core and put λ=Σ_{q∈S}1/q. Let D(b) be the number of their available quotient banks containing b. The lower sieve gives ΣD≥c₀ Xλ/(c log X). We claim

    Σ D² ≤ C₁ X λ(1+λ)/(c log X)

with an absolute C₁ for c≤1/(2K) and all sufficiently large X depending on c. For each pair q,r, the intersection requires a multiple of lcm(q,r) with quotient free of primes through z. All labels are already coprime to the product of these primes. In particular it is bounded by the upper sieve applied at T=X/lcm(q,r)≥1.

Diagonal terms have T≥sqrt(X). For distinct powers of one prime p the lcm is the larger one and again T≥sqrt(X); for each smaller q their total reciprocal lcm is at most Σ_{j≥1}1/(qp^j)≤1/q. All these terms cost O(Xλ/(c log X)). For coprime pairs the 1/log z part costs O(Xλ²/(c log X)). Consider the remaining term with 1/log(2X/(qr)), ordered q≤r. If q≤X^(1/4) then X/(qr)≥X^(1/4) and the cost is O(Xλ²/log X). For q>X^(1/4) we have

    Σ_{q≤r≤sqrt(X), r prime power} 1/r
      ≪ [1+log(sqrt(X)/q)]/log X.

Indeed, dyadic subdivision and the prime counting upper bound prove this for primes. The reciprocal sum of all nonprime prime powers above X^(1/4) is O(X^(−1/8)log(2X)), by partial summation from their O(sqrt(t)log(2t)) counting bound. The series converges and this contribution is o(1/log X). Since log(2X/(qr))≥log(2sqrt(X)/q), summing first in r bounds the remaining ordered-pair contribution by O(Xλ/log X). This proves the claim even at the upper square-root boundary.

Cauchy–Schwarz now gives a union of at least c₂ Xλ/[c(1+λ)log X] target positions for an absolute c₂>0. Also λ≤log(1/c)+O(1) by Mertens' estimate for the primes from X^c to sqrt(X) and the convergent higher-power reciprocal sum. Choose a fixed c>0 so small that this lower bound exceeds C Xλ/log X, where C was the absolute row-count constant. Hall's theorem gives distinct representatives for all rows at this core. Distinct cores have disjoint representatives, and each covered cofactor lacks at most one source atom.

**Bounded quotient lengths and repair.** The argument applies simultaneously for X≥X₀(c). At smaller X, h is supported on the fixed finite primes at most X₀^c, so there are at most (1+log₂ M)^{π(X₀^c)} possibilities for h and O_c(1) rows for each. Their individual atom counts sum to at most a fixed power of log M. If M≥(2n)^3 use the previously proved unconditional two-block bound H≤2n. In the complementary range this exceptional cost is o(n). Covering each remaining omitted atom costs at most one new point: use the greatest unselected valuations of each prime to satisfy its nested levels, whose full interval counts always suffice. This completes the proof.
