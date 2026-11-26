# Placement, matching, and cuts

An atom is a complete source power of one prime. H requires at least as many chosen multiples of every p^j as there are source multiples. In an H-cover one can inject source atoms of each given prime into eligible selected positions by sorting in decreasing exponent. Conversely, partial injective credits can be completed for at most one position per uncredited atom: for each p choose the highest valuations on the remaining positions, up to its maximum level-count deficit. The whole interval has enough multiples at every level. Take the union over primes.

## Fixed splits, escaping a cycle, and a joint move (route 1)

Split each source into at most two coprime blocks and assign each nonunit block to a multiple. At a site b the number of credited bases is v and the number of atom occurrences is e. Its price is 1+e−v including singleton repair. Summing gives a certified upper bound for H. Consequently H is a lower bound on the optimal price of this particular certificate model. If every row has at most two bases then the optimal price equals H: start from a minimum H-cover and use the per-prime injections above, splitting into singleton atoms. Every utilized site has zero duplicate charge.

For a block h on a cycle of the local bipartite graph (block occurrences versus prime bases), at least two of its bases are duplicated at that site. Moving h to an unused multiple decreases the total price by at least one. At a one-move local minimum, every multiple of each such h is occupied and every other such site already uses at least as many of its bases as are duplicated at the old site. Indeed leaving saves one charge per duplicated base; entering costs one if the site was empty and otherwise costs the number of common bases. In particular floor(M/h)≤2n. This works for unequal exponents at a common base, since distinct full powers can be repaired at one point per lost atom.

A plateau occurs for A={2,3,10}, I=[1,10], using full blocks at 4,9,10. No one relocation decreases price 3; simultaneously move 2 and 3 to 6 and the optimum is 2. A rank-three test with A={30,42,70,105}, x=157, gives minimum full-block price 5 and optimum joint split price 4. Actual sites are 168,175,180,210. In row order the blocks are (6,5), (7,6), (5,14), (7,15); see the replay for their assignments. At x=831 both optima are 4. The lower bound H≥4 in either window is also immediate: each of 2,3,5,7 occurs in three rows, so a three-point H-cover would require three multiples of 210 in a window of length 105.

## Pair labels with one cycle (route 2)

Suppose residual pairs are squarefree, and the graph of their distinct labels pq on prime bases consists of trees and unicyclic components. Assume each label occurs at most floor(M/(pq)) times, as when it comes from distinct source multiples. At each previously opened site assume that in each such component at most one base has a prior credit. Place occurrences of a given label at distinct multiples. At a new site receiving a forest with t edges there are at least t+1 different bases. At an old site a forest with t edges still has at least t previously uncredited bases, by applying the hypothesis on each of its tree components. Opening new sites and repairing all uncredited occurrences therefore costs at most one per edge whenever the placements are locally forests.

For a unicyclic component with cycle C the number of sites carrying that whole cycle is at most min_{e∈C}m_e, with m_e the multiplicity. Each such cycle can cost at most one further repair, since removing an edge restores the forest bound (equivalently use v=e in its cyclic component). One can remove the excess altogether if there is an edge e of C with

    |B_e| ≥ m_e + min_{f∈C, f≠e} m_f,

where B_e is its bank of multiples. Assign all other edges first and place e distinctly outside the sites carrying all of C minus e. There are at most the indicated minimum many prohibited sites. Do this independently for the unicyclic components. This proves a first-cycle case with explicit multiplicities and a finite test.

### Residual tokens can change partners

After arbitrary injective partial credits on F, list D uncredited full atoms as individual tokens, including the three from a single row if applicable. At b∈F allow one token of any previously uncredited base p dividing b to enough power. At a fresh b allow two tokens of different bases simultaneously, each dividing b to enough power. Let S be the maximum of the number of already-open slots filled plus the number of these fresh pairs. Then

    τ ≤ H ≤ |F|+D−S.

Each paid-slot hit saves one repair. Opening a fresh site for two tokens saves one net repair. The remaining singleton repair uses the nested levels argument above, including any accidental extra credits. No original pairing constraint is needed.

There is an exact ordinary weighted matching formulation of this restricted packing. Add an optional vertex per token and per available old slot, joining old slots to their eligible tokens at weight 2. At each fresh site add two mandatory ports with an internal edge. For each eligible base at that site add a mandatory pair u,v with its own internal edge, edges from both ports to u, and edges from v to eligible tokens at weight 1. All other edges have weight zero. Require every mandatory vertex to be matched, which is feasible with internal edges alone. A site either uses its port edge, or uses two distinct base gadgets and consequently two distinct tokens. Conversely any allowed packing fills all mandatory vertices. The maximum edge weight under mandatory saturation equals 2S. Ordinary weighted matching implements saturation by adding to each edge a bonus per mandatory endpoint greater than 2D. This certificate allows all residual rows in one optimization. Breaking a fresh high-capacity point into just two credits need not be optimal.

## Gluing at a shared position (route 7)

Partition the source rows into groups with local H-covers F_i in the original interval and choose injective atom credits within each group. Where quotient fibers are used, multiply their positions back first and pad to the number of rows to pay for the common divisor. At a shared site b form the incidence graph between its g local groups and the bases credited there by each group. Let e be the number of incidences, v the number of used bases. Keep the largest credited exponent at each base. There are e−v lost atoms, while taking the union saves g−1 site openings. Hence

    H ≤ Σ_i |F_i| + Σ_{b shared} [e_b−v_b−g_b+1].

This follows by singleton level repair on the original interval, even when the lost exponents are unequal. A forest costs no excess: with c connected components the bracket is 1−c. Thus arbitrarily many shared positions are allowed if their credit graphs are all forests. In particular two groups sharing at most one credited base at any common position glue within their combined budgets. For example, take groups {6,10} and {21,35} in [1,35]. Assign the first group to {6,30} and the second to {21,30,35}, with the 5-credit of 35 at 30 and its 7-credit at 35. The only common credited base at 30 is 5. The formula gives 5 as a bound despite the shared credit. With two or more shared bases per position the cycle terms require a separate argument. This lemma glues H-certificates; unrestricted product certificates may combine several exponent units inside a single position.

### Dense subsets of unions of progressions, even at zero ambient density

Let d_1,...,d_s≤M be positive integers, s≥1. Let V be their union of multiples in J=[1,M], F the same union in I, K=floor(M/min d_i), R=A outside V, and P the set of prime divisors of rows in A∩V. Then

    H(A,I) ≤ |V| + 2^(s−1) + (2^(s−1)−1) |P| + Σ_{a∈R} ω(a),
    |P| ≤ π(K) + Σ_i ω(d_i).                                         (3)

For each nonempty set of indices take the lcm l of its moduli. The I-count of l-multiples exceeds the canonical count by either zero or one. Inclusion-exclusion has 2^(s−1) positive and 2^(s−1)−1 negative terms, even when some lcm values coincide. Therefore |F|≤|V|+2^(s−1). After imposing p^j divisibility replace l by lcm(l,p^j); the same one-sided errors show that the count in F is at worst 2^(s−1)−1 below that in V, uniformly in j. This bounds the maximum level deficit per core prime. Exceptional rows increase its total over bases by at most Σ_R ω(a). Apply nested repair. Every prime in a row a divisible by d_i either divides d_i or is ≤a/d_i≤K. This proves (3). No restriction is imposed on pairwise gcds or on the number of shared target positions.

In particular if M≤n², all rows lie in such a union with |V|≤2n+o(n), and s is fixed, then **H≤2n+o(n) for every shift**, without a lower bound on n/M. Indeed K≤|V|, π(K)=O(n/log n) and Σ_i ω(d_i)=O(s log n). For a fixed ε>0 the proof still works with s≤(1−ε)log_2(log n). More generally the same conclusion holds when |V|+Σ_R ω(a)≤2n+o(n). This closes the two-overlapping-progressions test for sources occupying at least half their canonical union. For instance V formed from 6 and 10 has overlap on every multiple of 30; a common scaling factor can make ambient density tend to zero while preserving relative occupancy. Formula (3) treats these intersections all at once. The density increment proved in [the inverse lemma](PRICE_AND_INVERSE.md) does not guarantee such a union.

## Weighted Hall tests and the Preil example (route 6)

For each j≥3 use rows of rank at least j. The replay computes maximum flow through one layer of cofactor labels into actual positions, with unit capacities on row and target endpoints. A row can delete any entire atom or, in the comparison rule, its numerically largest entire atom. All tested levels had zero deficiency for M=210,840,2310,10010 on the zero, centered and specified seeded shifts, with A=[2,M]. At M=10010 the level sizes were 4627,929,34. These finite tests cannot certify the asymptotic weighted sum of deficiencies. The fixed comparison rule in these tests uses the numerical atom; the following external obstruction uses the largest **prime base**.

[Preil's explicit set](https://github.com/dpreil-ydlp/open-problems/blob/4077a6093abfd8e84f5a95421628cd3d9a50a5cb/math/erdos708/SOL-UPPER-ATTEMPT.md) consists of all even a≤M with at least two distinct odd prime divisors. At M=300000000 and x=2000000000000001416 its size is 132347966. Fixed deletion of the power of the largest prime base has a neighborhood at least 233721 short on the whole set.

For adaptive deletion, take the first twelve primes through 37. Every product of two of them is a cofactor of a squarefree source of rank three: add 2 for an odd pair, and another odd prime for a pair containing 2. Hence every target divisible by at least two of them is a neighbor. Its full-period density is

    1−∏(1−1/p)(1+Σ 1/(p−1)) = 123740190883/247357937827 > 1/2.

The inclusion-exclusion coefficient of a j-subset is (−1)^j(j−1) for j≥2, giving absolute endpoint error at most 20481. Thus on **every** such window of length 300000000 there are at least 150053771 neighbors; the exact subcount at the published shift is 150074273, a surplus of 17726307 over the number of rows. This excludes the displayed full-set cut for adaptive deletion. Hall still ranges over all subfamilies. For each fixed rank threshold j≥3 the analogous whole-level obstruction disappears asymptotically: use targets divisible by at least j−1 out of a sufficiently large fixed set of small primes including 2. Such a subset is a cofactor of a rank-j source after adjoining 2 or another odd prime. The full-period probability can be made larger than 1/2 since the independent Bernoulli count has mean Σ1/p→∞ and variance at most its mean. The interval discrepancy for this fixed period tends to zero, and every level has at most M/2 sources.

The actual product on Preil's finite instance has the independent upper bound 150000000: select all even positions. Their quotients by 2 are an interval of M/2 consecutive integers whose product is divisible by (M/2)! and hence by the product of the distinct source quotients. This survives the common-power scaling in the external construction.

## Mixed marking at the normal-order example (route 8)

For a deterministic pool S equal to the distinct bases of h, its decreasing-cutoff bin has size at least

    c_h = U ∏_{p|h}(1−1/p) − 2^ω(h),    U=M/h,

when all bases of h are ≤U. This follows by inclusion-exclusion on the quotient interval. Mix deterministic pools with masses λ_S, using any remaining mass for a common random marking. Each h with support S receives at least λ_S c_h; kernels at different h are disjoint for each outcome, so total mass per site is at most one. In particular Σ_S max_{h:supp(h)=S}(m_h+1)/c_h ≤1 is sufficient for those families (positive c_h only). Other groups can be served from the unallocated fraction if they meet their own capacity test.

This repairs the **entire growing example** from [the normal-order obstruction](../uniform_three_2026_11_26/MARKED_PRIMES.md), simultaneously at every shift. In its notation U is prime, h in [4U,8U) has r=ceil(log log U) distinct bases, M=hU, the h-bank has O(U/log U) requests, and the other banks are 2l and 2U with bounded multiplicity and quotient lengths at least 2U. Use half the mass on the deterministic support of h. Divide the other half equally between all the light supports {2,l}, including l=U; there are at most π(U) such supports. The first half gives the heavy bank ≫U/log(r+2)−2^r, enough with slack: the product over r primes is minimized by the first r, giving the stated bound by Mertens. Each light support has c_h'≥U'/3−4, since l≥3. Its allocated capacity is therefore at least (2U/3−4)/(2π(U)), which tends to infinity uniformly. This uses only inclusion-exclusion on two primes for the light banks and leaves at least one spare unit everywhere. The finite replay also verifies the uniform capacity inequalities at U=5003, h=30720. Anchor one complete row, remove its position, allocate one unit to every other row, and apply integral bipartite matching. Each matched row has at most one full atom left, so H≤2n−1. The previous negative result optimized mixtures of a *single common marking probability*. The deterministic support-specific part makes this a different certificate. An arbitrary growing collection of thick, incompatible banks still need not pass this mixture test.

## Harmonic cuts (route 9)

For T⊂I take the normalized harmonic mass of all d≤M whose every multiple in I is in T, minus |T|/M. If the excess is at least δ>0, put t=|T|/M. The complement is nonempty, and its longest consecutive run G is shorter than every trapped d. If it has k runs, G≥(1−t)M/k, while

    (t+δ)H_M ≤ Σ_{d>G}1/d ≤ log(M/G).

It follows that k≥(1−t) exp((t+δ)H_M)≥δ M^(t+δ). This explicitly excludes every cut with subpolynomially many complement runs at fixed excess. It gives no upper bound on cuts made of many scattered sites.

The replay computes the exact maximum over every T and one complete lcm period of shifts for 4≤M≤12, using a subset sum transform with integer weights. For M=12 the maximum is 131263/1032252 at x=27713 with T consisting only of offset 7. A single centered or near-centered site attains the maximum at every tested M. This empirical pattern cannot be taken to arbitrary M. The earlier [harmonic-to-Hall reduction](../cofactor_flow_2026_11_26/HARMONIC_REDUCTION.md) has an additional O(M/log M) error relevant at sparse densities.
