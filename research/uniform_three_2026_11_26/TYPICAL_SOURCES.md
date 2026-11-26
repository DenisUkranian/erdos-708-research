# Almost every source family works for every shift

For integers 1≤n≤M−1 choose uniformly among the n-element subsets of [2,M] that have maximum M. Write τ(A,I) for the minimum number of positions needed for ordinary product divisibility on an interval I of M positive consecutive integers. For every sequence n→∞, with arbitrary M=M(n), with probability 1−o(1) one has

    τ(A,I) ≤ (2+o(1))n simultaneously for every shift I.

When log M / log n is bounded by a fixed constant, there is the stronger simultaneous bound

    τ(A,I) ≤ [1+min(1,log(log M/log n))+o(1)]n.

In particular all positive densities, and more generally n=M^(1−o(1)), have upper bound (1+o(1))n for a typical source family, even at its worst shift. For n≥M^(1/2−o(1)) the coefficient is at most 1+log 2+o(1). This probability is on source families. It does not bound the maximum over all A.

## A deterministic bound for a given sample

In the polynomial regime handle the forced row M at an extra cost of at most Ω(M)≤log₂ M=o(n) prime units, in the simultaneous final repair. Put A'=A without M, t=(n−1)/(M−2) for M≥3, and U=[2,M−1]. For each p≤n put S_p=Σ_{a∈A'}v_p(a), and define

    D = Σ_{p≤n} [S_p−t Σ_{u∈U}v_p(u)]_+ .
    B = #{a∈A' : a has a prime factor >n}.
    V = Σ_{p>n} Σ_{unordered pairs {a,a'}⊆A'} min(v_p(a),v_p(a')).

Then for every shift,

    τ(A,I) ≤ n+1+B+D+V+π(n)+Ω(M).

For every row counted by B choose one multiple in I, and give its position weight one. These anchors collectively pay at every p>n at least the maximum single-row valuation of A' at that p. The sum of the other valuations is at most the sum over row pairs of their pairwise minima. This leaves at most V unpaid outside units across all such primes. The number of anchors is at most B, including after any collisions.

On all other positions assign temporary weight t. For every p≤n this gives at least t times the total p-valuation available in I, which is at least t times its total in U by counting multiples at each level. Fix every anchor's weight to one and minimize the sum of all weights in [0,1], requiring the small-prime cover to achieve the smaller of S_p and t Σ_{u∈U}v_p(u) at each p≤n. The temporary weights are feasible and cost at most tM+B≤n+1+B. At an optimal vertex at most π(n) coordinates are fractional: a larger collection would admit a nonzero two-sided perturbation fixing all small-prime linear totals and the fixed anchor coordinates. Rounding them upward adds at most π(n) to the cost. At this point the deficiency on the small primes sums to at most D. For any remaining prime-unit deficit, a fresh position divisible by that prime exists because the full interval covers the source product. The final repair costs at most D+V+Ω(M). This accounts for collisions between the small-prime cover and the anchors.

## Probability estimates independent of the shift

A' is a simple random sample without replacement of size n−1 from U. Its p-valuation sum has mean tΣ_U v_p and variance O(n/p), uniformly in p. Indeed the population mean square is O(1/p) by the identity v²=Σ_{j≤v}(2j−1) and the floor bounds for p^j multiples in U. Sampling without replacement only reduces the variance relative to independent draws. Thus E D ≪ Σ_{p≤n} sqrt(n/p) ≪ n/log n by partial summation from π(x)≪x/log x.

For a random distinct pair of rows in U, the probability they are both divisible by p^j is at most the square of the fraction of such multiples, which is at most O(1/p^(2j)). Consequently E V ≪ n² Σ_{p>n} 1/(p²−1) ≪ n/log n. Markov gives D+V=o(n) with probability tending to one, uniformly in M. Finally B≤n and E B/(n−1) ≤ (1+O(1/M))Σ_{n<p≤M} 1/p ≤ log(log M/log n)+o(1) when log M/log n is bounded, by Mertens' estimate. B counts marked members of the sample, so its hypergeometric variance is at most n; Chebyshev gives the same upper bound up to o(1) with probability 1−o(1). This proves the polynomial statement, including its forced-row term.

For arbitrary sequences use this argument uniformly when M<(2n)^3. For M≥(2n)^3 the shift-uniform elementary [two-block argument](../cofactor_flow_2026_11_26/README.md) gives τ≤2n for every source family. The two cases cover every growth regime.
