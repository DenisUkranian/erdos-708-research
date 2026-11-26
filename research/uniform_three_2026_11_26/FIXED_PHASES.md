# A simultaneous mean bound conditional on adversarial prime phases

Let P=lcm(1,...,M), and prescribe the starting residue of the target window modulo the full p-part of P, independently and arbitrarily for each p in a specified set S. Choose the remaining prime phases uniformly and independently. Write e(M,I) for the harmonic cut excess from the [harmonic reduction](../cofactor_flow_2026_11_26/HARMONIC_REDUCTION.md).

**Theorem.** If Σ_{p∈S} (log p)/p = o(log M), then E[e(M,I) | prescribed phases]=o(1), uniformly in their values. In particular the adversary may prescribe all phases at all primes p≤y for *any* y=M^{o(1)}. Outside a vanishing proportion of the remaining phase choices, every source A of size at least δM, for any fixed δ>0, has a product cover of size at most (2+o(1))|A|. The family may depend on the shift. The average is conditional and makes no assertion for a single worst setting of the remaining phases.

## Sampling one divisor bank

Use the [full-period harmonic transport kernel](../unrestricted_shifts_2026_11_26/README.md). Its weights K_d(b) sum to one at b, depend only on gcd(b,P), are zero unless d|b, and have unconditional mean μ_d=1/(d H_M), H_M=Σ_{j≤M}1/j. For empirical bank masses w_d=M^(-1)Σ_{b∈I} K_d(b), e≤Σ_d(μ_d−w_d)_+. This inequality is pointwise, including for adaptive cuts.

First prescribe phases only at primes in S⊆[2,y], where log y=o(log M); y≥3. Fix 0<δ<1/2 and omit d>M^{1−δ} at cost at most δ+O(1/log M) in total harmonic mass. For each remaining d additionally condition on x mod d. This extra conditioning can be chosen separately in each bank and is averaged away after bounding its positive deficit. Put Q=P/d. The multiples of d give a consecutive quotient window t+1,...,t+H, with |H−M/d|≤1. The residues of t at the S-prime powers of Q are prescribed. Modulo the complementary prime powers of Q, t is uniform by CRT. Fix arbitrary lifts of the prescribed residues to sufficiently high powers when necessary. Divisibility at levels beyond Q may then be used in deterministic sieve masks without changing any kernel values. More explicitly one may fix true integer lifts for each pinned coordinate (or compatible p-adic lifts), and impose each finite collection of masks by CRT on the offset index.

The summand f(j)=K_d(dj) in this bank has unconditional mean m=1/H_M over a uniform j modulo Q. It is invariant under multiplication of j by units. If the exact S-supported part of j is h, then f(j) is a function F_h of only the complementary coordinates. Its values lie in [0,1], and on those coordinates it remains invariant under multiplication by units. Exact S-valuations can be taken uncapped and only then capped in evaluating f. Write bar F_h for its uniform complementary-coordinate mean.

## A lower approximation that can be sampled uniformly

Take Z=H^(1/10). There is a lower sieve polynomial Σ_{e|v} λ_e for the condition that v has no S-prime factor. Its e are squarefree S-supported integers ≤Z, its coefficients have absolute value O(log log(3M)), and its independent-model mean is at least (1−ε_M)V, where V=∏_{p∈S}(1−1/p), and ε_M→0 uniformly for the fixed δ.

For completeness, partition S into bands y^(2^(−i−1))<p≤y^(2^(−i)) for i≥0, stopping below 2. Each band has bounded reciprocal prime mass by Mertens' estimate, and its product V_i is bounded below absolutely. In each band use upper and lower Bonferroni polynomials U_i,L_i through consecutive even and odd orders r_i, r_i+1, with r_i the even integer immediately above (log H)/(100 log y)+i. Replace the joint sifted indicator by the lower polynomial

    ∏ U_i − Σ_i (U_i−L_i) ∏_{j≠i} U_j.

Pointwise each U_i dominates its true indicator and is nonnegative, so the lower bound follows by telescoping. Band partitioning gives coefficient magnitude at most one plus the number of bands. Total log modulus is at most (log y)Σ_i 2^(−i)(r_i+1) < (log H)/10 for large M. The mean of U_i−L_i is at most C^(r_i+1)/(r_i+1)! by the band mass bound. Relative to V_i these errors are summable with sum o(1), uniformly as log H/log y→∞. Independence across bands gives the asserted lower mean.

Use this polynomial for each h≤Z supported on S, multiplying by 1_{h|j}F_h and applying the sieve to j/h. Each term is a product of F_h and the indicator of a single congruence of the offset index mod he, where he≤H^(1/5) and has only S-primes. Their signed sum is a pointwise lower bound on f. All F_h are nonnegative and every exact profile appears only in its own indicator. Terms at other h have nonpositive total at that point. This argument also covers p-adic lifts for which an offset has infinite valuation: it contributes no valid finite exact profile below Z.

On the indicated congruence the number of offsets is J=H/(he)+O(1). Along them the free inputs of F_h run along an arithmetic progression of step he, coprime to the complementary modulus. Its initial residue is uniform there. Multiplying by the inverse step preserves F_h, so the [gcd-invariant Fourier variance bound](../unrestricted_shifts_2026_11_26/README.md) applies on this subprogression. The expected absolute difference between the contribution divided by H and (bar F_h)/(he) is at most

    O(H^(−1) + sqrt(log M / H)).

Here the complementary modulus over its totient is O(log M) and J≤2H. This is uniform in the selected congruence and all prescribed phases. There are at most Z²=H^(1/5) pairs (h,e). After summing coefficient magnitudes, the total expected absolute error is O(H^(−3/10) sqrt(log M) log log(3M)), which is smaller than every fixed negative power of log M since H≥M^δ−1.

The unconditional reference value of the lower polynomial is at least (1−ε_M) Σ_{h≤Z} V (bar F_h)/h, over S-supported h. Indeed the uncapped model takes independent geometric prime exponents and gives exact S-part h with probability V/h. Consequently the positive deficit of this d-bank, in expectation and in units of M/d, is bounded by ε_M m, the reference tail E[f(j)1_{s_S(j)>Z}], and the preceding polynomially small error, plus the harmless floor correction. Here s_S is the full product supported on S.

## Summing the tails without a factor of log M

Couple all reference tails using one product B of independent uncapped geometric prime powers through M. The gcd of B with P has the full-period law. Conditional on d|B, the remaining prime exponents in B/d are again independent geometric variables. Therefore the sum of all the reference tail bounds with weights 1/d, for d≤M^{1−δ}, is at most

    E Σ_{d|B, d≤M} K_d(B) 1_{s_S(B)> (M^δ−1)^(1/10)}
        ≤ Pr(s_S(B)> (M^δ−1)^(1/10)) = o(1).

For the last step, E log s_S(B)=Σ_{p∈S} (log p)/(p−1) = O(log y) by the elementary weighted prime estimate. The sieve relative losses sum to o(1) since Σ μ_d=1. All other absolute normalized bank errors sum to o(1), even after multiplication by Σ_{d≤M}1/d. The empirical normalizations H/M and 1/d differ by at most 1/M, with total over these d at most M^(−δ). Hence limsup E e≤δ. Send δ down to zero.

For general S in the theorem choose y=M^{o(1)} tending to infinity slowly enough on the logarithmic exponent scale that Σ_{p∈S,p>y}1/p=o(1); for example take log y/log M to be the square root of (1+Σ_{p∈S}(log p)/p)/log M. First condition only on the small prescribed phases. Couple the desired experiment to this one by replacing the phases at p∈S, p>y by their prescribed values. In each realization this changes the profiles at most on the union of the multiples of these primes in the two windows (positions identified by their offsets). The fraction is ≤2Σ_{p∈S,p>y}(1/p+1/M)=o(1), since π(M)=o(M). At each changed position the total variation between its two kernels is at most one; normalized bank mass and therefore the harmonic deficit bound change by o(1). This proves the full conditional claim.

The harmonic Hall reduction now gives o(M) unmatched rows with probability tending to one, simultaneously for every dense source. For product covers use the source-removal stability and vertex rounding in [redlydi, residue certificates, §2](https://github.com/redlydi/Erdos708-Research/blob/32f397f8fdc00d0e9c73242d8510c541267a30db/reports/erdos708-residue-certificates.md), charging O(m log(eM/m)) for m missing sources plus π(M) positions. The full interval covers |A|≥M/2 directly. Quantities with conditional mean o(1) give a common error o(1) outside a common o(1) exceptional proportion by Markov's inequality.

## A rate when all prescribed primes are at most y

Put L=log M, R=L/log(2y) and η=log(2R)/R + log(2L)/L. For R→∞ the proof gives E e≪η uniformly in the phases. Choose δ=Cη with a sufficiently large absolute C, so H≥exp(δL)/2. The first Bonferroni order is at least c C log(2R). The sum of the relative band errors is O(R^(−2)) by the factorial bound. The total sampling error, after multiplying by H_M, is O(L^(−2)) for large C. For the profile tails use E[s_S(B)^(1/(2 log(2y)))]≪1: the log Euler product is bounded by a constant times Σ_{p≤y}(p^t−1)/p=O(1) at t=1/(2 log(2y)), since p^t−1≪t log p. Thus the common tail is O(exp(−cδR))=O(R^(−2)). The discarded harmonic mass is O(δ+1/L). This proves the rate. By the same Hall reduction, source-removal stability and Jensen, for simultaneous product covers the mean additive excess over 2n is O(Mη log(e/η)+M/log M). Consequently almost every conditional shift works simultaneously for all source sizes much larger than this additive scale, even when their density tends to zero.
