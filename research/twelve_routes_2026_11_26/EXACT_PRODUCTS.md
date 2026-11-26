# Exact product costs on centered families and the seven-row interval

## A centered cluster theorem (routes 2, 10 and 12)

Fix r≥2. Choose primes P≤p_1<...<p_k≤cP with c^r<2. Let A be a nonempty subfamily of products of r **distinct** primes from this list. Write n=|A|, M=max A, and D_i for the number of rows divisible by p_i. Take N=∏ p_i^r and the M-point interval starting at N−floor(M/2), inclusive. Assume floor(P/c^(r−1))≥2+ceil(rn/(r−1)). For fixed r and k such primes exist by the prime number theorem for sufficiently large P. Then the exact ordinary product cost is

    τ = min{ ceil(rn/(r−1)), 1+ceil( Σ_i (D_i−r)_+ /(r−1) ) }.          (1)

Every noncentral b has fewer than r prime units from the chosen primes, including multiplicity. Otherwise some product d of r of these units divides both N and b (the exponents in d are at most r). But d≥P^r and 0<|b−N|≤M/2<P^r. If the center is omitted, this gives the first lower bound; if included, it pays min(r,D_i) at each base and gives the second. A solution must pay at least the lesser of these two costs.

Conversely, in either case list the remaining units with repetitions, and pack into batches of r−1 with a possible final shorter batch. For each batch take one new multiple of its product. Even with repeated bases the batch product is at most (cP)^(r−1). Its bank contains at least floor(M/(cP)^(r−1))≥floor(P/c^(r−1)) positions. This exceeds the number of earlier sites plus the center, so choose all sites distinctly and avoid N. Adding N in the second case proves both upper bounds. The re-pairing across rows is legitimate because the target is product divisibility.

For the complete r-subset family, n=binom(k,r) and D=binom(k−1,r−1). For D≥r, formula (1) simplifies to

    τ = 1+ceil((rn−rk)/(r−1)).
    H = 1+ceil((rn−k)/(r−1)).                                       (2)

For H each base pays only one occurrence at the center. Away from N even r different bases cannot be present. To achieve the bound, repeat the list (p_1,...,p_k) exactly D−1 times and cut the resulting sequence into batches of length at most r−1. No batch repeats a base. Choose distinct multiples as before. Omitting the center costs at least ceil(rn/(r−1)), which is no smaller. In fact the same H formula holds for a center containing each prime only to the **first** power (e.g. N=∏p_i, with a positive interval): the proof about r distinct bases still applies. The valuation lower bound for ordinary τ at such a center need not hold.

For fixed r and k→∞ the complete-family ratio tends to r/(r−1) under (1)'s separation hypothesis. At rank two this approaches 2, at rank three 3/2, at rank four 4/3. Further, (1) bounds every subfamily of a fixed rank under the same separation condition by ceil(rn/(r−1)). Thus increasing the uniform rank in this particular centered construction does not give a counterfamily above two. The classical pair lower construction also allows squares; we use only squarefree sources and prescribe the center valuations here. No assertion about unrestricted shifts or mixed ranks follows from this exact computation.

For the previously troublesome family {2p_i p_j p_l}, take a centered quotient window as above and multiply its selected positions by 2 inside the double-length window of multiples (select the length-2M window with these M even sites). Pad the quotient cover to n positions if needed. This yields the same 3n/2+O(k+1) upper estimate for the doubled family on these windows. The old cost near 3n for repairing after a single full-row center is an algorithmic loss.

The replay constructs actual integer positions for r=2,k=6 (τ=19,H=25), r=3,k=7 (τ=43,H=50), and r=4,k=8 (τ=84,H=92). For the last numerical sample p_1=1009,p_k=1049, so c^r<2 and the size conditions hold. It checks the integer products and level demands as well as the formula.

## Identical level data, two different asymptotic product costs

Keep the complete family, fix r and let k grow, with P sufficiently large as above. Take the primes odd. There are two sequences of centers with **identical residues modulo lcm(A)** and v_{p_i}(N)=1 for every i, with the following ordinary costs:

    cheap shift:       τ = ceil(k/(r−1)),
    expensive shift:   τ = (r/(r−1)) n + O_r(k^(r−1)).

The level-cover optimum is exactly the second formula in (2) on both shifts. In particular for triples the same A and the same level profiles permit either exactly ceil(k/2) positions or (3/2+o(1))n. The source sets and M used on the two sides are identical for each k.

For the cheap shift, divide the k bases into G=ceil(k/(r−1)) disjoint batches of at most r−1 bases. Let t be the product of the primes in a batch. Impose N≡−t modulo p^D for every p in that batch, independently across primes, and take a large positive CRT representative. Assume D≥2. Then v_p(N)=1. The G offsets t are distinct, positive and less than the right radius for sufficiently large P. The point N+t covers the entire exponent requirement of every prime in its batch. Conversely an off-center point contains at most r−1 different bases, since every product of r distinct bases divides N and exceeds the radius. The center can supply only one unit at each base, while D≥2, so every base still needs an off-center point. At least G such points are necessary even if the center is included.

For the expensive shift, for each chosen p impose

    N ≡ p(p^r−1)/2 (mod p^(r+1)).

This residue has valuation exactly one and lies within p/2 of the middle of its modulus. For large P (at fixed r), the entire centered window therefore avoids multiples of p^(r+1), simultaneously at all chosen primes by CRT. Every off-center position has at most r−1 distinct active bases and at most r(r−1) active units in total. If it has at least r units, it is divisible by some multiset product of r chosen primes with a repetition. There are O_r(k^(r−1)) such products, since each uses at most r−1 distinct bases. Each product is ≥P^r and has at most two multiples in a window of length M<2P^r. Hence the total number of units in excess of r−1 per off-center position, summed over the entire window, is O_r(k^(r−1)). The center contributes k. Every covering set of size L must supply rn units, so rn≤(r−1)L+k+O_r(k^(r−1)). The level-cover construction in (2) gives the matching leading upper bound. Both centers are 0 modulo every source prime; for squarefree A the level profiles relevant to A coincide offset by offset. These examples separate actual product costs even after the center multiplicities themselves are specified.

## A seven-row product needs exactly five positions (route 10)

Let x=920168185 and A={4370,6555,15295,24035,28405,37145,60090}, I=(x,x+60090]. The five offsets

    11790, 27315, 28396, 56939, 60090

give distinct numbers whose product is divisible by ∏A. To certify minimality, cap each target valuation at its required total. In the coordinate order (2,3,5,7,11,13,17,19,23,2003) the demand is (2,2,7,1,1,1,1,6,6,1). Enumerate all 60090 positions, discard dominated signatures, and allow **unlimited reuse** of every remaining signature. This relaxation can only decrease the minimum; it has 163 maximal signatures. The exact recursion chooses a positive residual coordinate, subtracts each maximal signature that touches it, clipping residuals below at zero, and decreases the remaining budget by one. Any successful multiset can be reordered to begin with such a signature. With budget 4 the recursion returns false. Its pruning compares each residual with the remaining budget times its largest single-position supply. Thus τ=5. The supplied checker needs no integer-programming solver for this certificate.

All seven sources are multiples of 5, so H≥7. Offsets 865,3050,9605,35825,11790,24900,50075 in source order are distinct multiples of the corresponding full rows after adding x, so H=7.

The gap can even grow at a fixed density for specially chosen shifts. For A={2,4,...,2n}, choose I with its first element divisible by ∏A. Then τ=1 and H≥n by the level p=2. This does not lower the worst-shift maximum. It shows why an obstruction only to level covering is insufficient evidence against ordinary product covering.

## Exhaustive small comparison

For every 2≤M≤8 and every subset of [2,M] containing M, the replay enumerates all target subsets by cardinality with exact integer valuation and level constraints. It checks a complete lcm(1,...,M) shift period for H. For ordinary τ, a period divisible by ∏A suffices because every target valuation can be capped at the total demand. The replay takes a full M! period for M≤6, and only the lcm period for M=7,8. In total there are 79790 tested (A,x) pairs for τ, including 68702 (A,x) pairs over one full lcm period at each M for H. The greatest observed H−τ is 3. These are counts of tested pairs and finite comparisons; the τ tests at M=7,8 do not certify their maxima at all shifts.
