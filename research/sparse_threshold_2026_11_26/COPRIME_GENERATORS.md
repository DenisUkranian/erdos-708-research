# Full divisibility upsets with pairwise coprime generators

Let D be any set of pairwise coprime integers g in [2,M]. Put J=[1,M], A=J∩⋃_{g∈D}gℤ and n=|A|. In every interval I of M positive consecutive integers the simultaneous prime-power-level covering number satisfies

    H(A,I) ≤ (2+o(1))n,

uniformly as n tends to infinity. The g may be composite, include powers, grow with M, or lie near M. This extends the corresponding theorem with only prime generators. It gives an all-density terminal subclass for the common-root/full-union route. If the quotient source is a union of these progressions after removing a common factor, multiply the representatives back and pad to n distinct multiples of the common factor.

Write L_g=⌊M/g⌋, m=ΣL_g, μ=Σ1/g. Pairwise coprimality implies |D∩[1,u]|≤π(u) by assigning one distinct prime to each member. Also

    m(1−μ/2)≤n≤m,       n≥M(μ−μ²/2)−π(M).

The second terms in Bonferroni use ⌊M/(eg)⌋≤L_g/e. If μ≥c for some fixed 0<c≤1, thin the generators independently with probabilities u_g such that Σu_g/g=c. The same two-term estimate in expectation gives n/M≥c−c²/2−o(1). Thus μ tends to zero on any sequence with n/M→0, and there m=(1+o(1))n. It suffices by passage to subsequences to consider n/M bounded below or tending to zero.

## Positive density

When μ≥1, the whole interval costs at most 2n+o(M) by thinning at c=1. Take μ<1. Include F=I∩⋃gℤ in full, and give every other position weight λ=min(1,μ+O(1/log D₀)), where D₀→∞ and D₀=o(log M), say D₀=√log M. The constant in the O term can be chosen absolute and positive. Since |F|≤Mμ+π(M) the weight is at most (2μ−μ²)M+o(M)≤2n+o(M).

For each level d=q^j≤M put N=⌊M/d⌋. If q divides no generator, source demand ≤μN. Otherwise let g be the unique generator divisible by q, and put G=g/gcd(g,d). In the prefix d-quotient the g-progression contributes ⌊N/G⌋ and its complement from all other generators contributes at most

    Σ_{e≠g,e≤N} (⌊N/e⌋−⌊N/(eG)⌋) ≤ (1−1/G)Nμ+π(N).

Indeed coprimality with d and G gives the indicated counts, and each summand exceeds its real counterpart by at most one. The target F contains at least ⌊N/G⌋ points at this level. When G=1 they already suffice. When G≥2 and N≥D₀, the available extra fractional coverage above the canonical g-count is at least λ(N−⌊N/G⌋). For λ<1 this exceeds the displayed bound after fixing the absolute constant, since 1−1/G≥1/2 and π(N)≪N/log N; for λ=1 the whole interval works. Rows with N<D₀ have demand <D₀, and there are O(M/log M) prime-power levels in total. Upward LP vertex rounding for levels with N≥D₀ costs O(M/log M) because at most this many non-fixed position variables can be fractional. Repair each remaining unit of deficit on short levels by an available multiple, at cost O(D₀ M/log M)=o(M).

## Density tending to zero

For each g choose exactly L_g consecutive multiples of g in I. Their union F has size ≤m, and the g-selection alone meets the source count of g-multiples at every prime-power level, since its quotient has L_g consecutive positions. In particular at level d (with unique g carrying q) it supplies ≥⌊N/G⌋, regardless of overlaps of chosen positions with the other generators. Demand at d outside that principal source progression is at most m/d by summing ⌊L_e/d⌋ over e≠g. Whenever it is nonzero, d≤max L_e≤n. The same two estimates apply with principal count zero when q divides no g.

Choose K→∞ so slowly that K²(n+1)/M→0 and set λ=m/[(M−n)(1−1/K)]=o(1). Give F weight one and every other point weight λ. For d≤n and G≥K, since N≥(M−n)/d, λ(N−⌊N/G⌋)≥m/d. The same estimate works with zero principal count. Levels with G=1 or d>n already suffice. Round up an optimum vertex retaining F at one and enforcing just the nonexceptional required levels d≤n. This adds O(n/log n) to the cost; d>n remain covered through F. The cost so far is ≤m+λ M+O(n/log n)=(2+o(1))n.

It remains to repair levels with 2≤G<K and nonzero outside demand. There are at most 2K distinct primes q involved. There are ≤K possibilities q≤K. For q>K, the integer G<K is coprime to q, and G≥2 supplies a prime <K dividing g. No other generator can use that small prime. For any one g there cannot be two exceptional primes q,q'>K, since then q' would divide G at every q-level. Thus there are ≤K further q. For each such q let d₀ be its least exceptional level of nonzero outside demand. Then

    d₀≥g/K>M/[K(n+1)],

because L_g≤n. At every outstanding level of q its total remaining deficit above F is ≤m/d₀. Selecting the largest remaining q-valuations repairs all nested levels with at most the greatest outstanding deficit in positions: at a level with deficit D there are at least D eligible unselected points since I suffices globally. Hence the whole final cost is at most 2K²m(n+1)/M=o(n). This covers sparse generators having both a high power of a small prime and a small additional factor, for which a naive common uniform reserve can lose a fixed factor.

## Effect on threshold counterexamples at fixed positive density

The ordinary boxed LP and rounding give, from τ(A,I)>(2+δ)n at n/M≥t>0, a witness with X(u)=Σ w_p v_p(u), 0≤w_p≤1, and Σ_A(X−2)−Σ_I(X−1)_+>δn/2 for large M. Taking the entire strict tail T={u≤M:X(u)>2} increases this gap and makes T a divisibility upset. For every pairwise coprime choice of generators from T, the corresponding full union B is contained in T. The terminal theorem gives

    Σ_{a∈T\B}(X(a)−2)≥δn/2−o(M).

Indeed every level cover of B is a product cover, hence Σ_B X−Σ_I(X−1)_+≤H(B,I). The bound H(B,I)≤2|B|+o(M) also holds for bounded |B|, e.g. using ≤|B|log₂M single prime-unit repairs. The positive-gap exponential moment established in [the residual gap proof](../density_and_gluing_2026_11_26/RESIDUAL_GAP.md) (using the original A of size ≤M/2) gives Σ_{a∈S}X(a)≪|S| log(eM/|S|) for every S⊆J. Therefore every coprime packing leaves at least c(δ,t)M of T uncovered, with c>0. In particular the generators may be any tail members and need not be minimal. This quantifies the obstruction that remains for route 11; it does not show that arbitrary threshold tails admit such a packing.
