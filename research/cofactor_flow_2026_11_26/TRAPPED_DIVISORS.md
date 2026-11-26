# Harmonic density of trapped divisors and a coprime-generator Hall bound

Let I be a positive interval of M integers, T a subset of I and D the set of d ≤ M for which every multiple of d in I is in T. It is an upward ideal in [1,M] under divisibility. Extend it to a periodic set U by taking all positive multiples of its minimal generators. Thus U ∩ [1,M] = D and U ∩ I ⊆ T. Write H_M = Σ_{d≤M} 1/d.

## Exact harmonic comparison with the full-period density

Let G_p, p ≤ M, be independent with P(G_p≥j)=p^(-j), and Z=∏p^{G_p}. On {Z≤M} the law of Z is exactly d ↦ 1/(dH_M), since the unconditioned mass has the form c_M/d throughout [1,M]. Membership Z∈U is increasing in the coordinates while Z≤M is decreasing. Harris's product inequality yields

    (1/H_M) Σ_{d∈D} 1/d ≤ P(Z∈U) = δ_per(U).

The last equality follows by the Chinese remainder theorem, since membership is determined by the bounded prime-power requirements appearing in the generators.

If 1_U = Σ_l c_l 1_{l|·} is its finite inclusion-exclusion expansion on the lcm lattice, counting multiples in I gives, for every shift,

    (1/H_M) Σ_{d∈D} 1/d ≤ |T|/M + M^(-1) Σ_{l>1} |c_l|.

In particular k minimal generators give error at most (2^k−1)/M regardless of their sizes. A common period L gives the alternative error L/M. For unrestricted ideals the coefficient sum and period can each be much larger than M.

## Concentration for a fixed ideal over CRT shifts

Fix an ideal of moduli E before choosing the shift, and let U be its periodic extension. Choose the shift uniformly modulo lcm(1,...,M), with independent prime-power phases. Write f=|I ∩ U|/M. Changing one prime phase p affects at most 2(M/p+1) positions. Set y=(log M)^(1/2). Conditional on phases p≤y, bounded differences at p>y have squared sum O(1/y+1/M). Consequently
P(|f−E[f | small phases]|>u | small phases) ≤ 2 exp(−c u² y).

Uniformly in the small phases and in the fixed ideal, the conditional mean differs from δ_per(U) by o(1). To see this, for p≤y take e_p maximal with p^{e_p}≤(log M)^2. Ignore positions divisible by p^{e_p}, whose total proportion is at most O(y²/(log M)^2+y/M) uniformly, and the same in the independent model. Else the small-coordinate profile is determined modulo L=∏p^{e_p}, with log L=O(y log log M)=o(log M). The uniform interval and a complete period differ by O(L/M) in averages of bounded functions of that profile. The expected contribution of the other primes at an individual position, conditional on the small profile, is the same bounded function there as in the independent model. This proves the assertion.

Harmonic mass is therefore bounded by the interval density plus o(1)+u outside the indicated exceptional shifts, for each predetermined ideal or a finite list by union bound. It does not treat an arbitrary shift-adaptive ideal.

## Actual one-omission Hall traps can be easier than harmonic mass

Suppose every minimal generator of D is ≥2 and the generators are pairwise coprime. Put L={g≤√M}, μ=Σ_{g∈L}1/g and η=Σ_{g>√M}1/g over generators. A row a with at least three prime-power atoms is trapped when every cofactor obtained by omitting one entire atom is in D. Such a row is divisible by at least two distinct generators: with only one generator g|a, omitting an atom based at any prime of g leaves a cofactor divisible by no generator. At least one of the two generators is ≤√M by coprimality.

Hence the number of trapped canonical rows (in any rank prefix or source subset) is at most

    M(μ²/2 + μη).

On the other hand T contains the union of all banks of the small generators. Two-term inclusion-exclusion gives

    |T| ≥ M(μ−μ²/2) − |L| − binom(|L|,2).

Let m=|L|. Pairwise coprimality gives m≤π(√M)≪√M/log M, and m≤μ√M because every small generator contributes at least 1/√M. Thus m+binom(m,2)=O(Mμ/log M), including m=0. If μ+η≤1, the union lower estimate gives |T|≥(1/2−O(1/log M))Mμ. Consequently the excess of the trapped rank-prefix row count over |T| is at most O(|T|/log M). At a positive Hall deficiency |T|<n, so the level costs at most O(n/log M), uniformly even when n/M→0. There are O(log M/log log M) nonempty levels because r!≤M for r distinct prime factors. If a maximizing trap at every positive-deficit level satisfies the stated conditions, summation gives an unrestricted-density bound O(n/log log M) on the total Hall deficit.

If μ+η≤1−ε for fixed ε>0, the negative main term −ε Mμ absorbs the entire error, so no such trap has positive deficiency for large M. Large composite generators each consume a distinct prime ≤√M; their reciprocal sum is O(1/log M). Mertens' estimate for the remaining primes gives η≤log 2+o(1); thus μ≤1−log 2−ε suffices for this exact exclusion.

In particular an ideal generated only by primes >√M traps no source row, even though the unrestricted harmonic criterion for these same ideals asks for a nontrivial lower bound on the union of arbitrary prime progressions. The harmonic estimate is a sufficient strengthening and need not be the weakest productive target.
