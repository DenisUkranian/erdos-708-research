# An exact two-position cover on polynomially many private cells

Let J=[1,M], let I be any interval of M consecutive positive integers, and define H(A,I) to be the minimum number of distinct target positions whose counts at every prime-power level are at least those of A⊆J. Thus any H-cover also covers the source product. Fix α,ρ,ε>0. Let E consist of distinct squarefree products e=pq with p,q>M^α, and write L_e=⌊M/e⌋. Assume L_e≥⌊M^ρ⌋. Suppose there are pairwise disjoint sets U_e⊆R∩eℤ, for a source R⊆J, satisfying

    |U_e| ≥ (1/2+ε)L_e  for each e∈E.

There exists η=η(α,ρ,ε)>0 such that for every sufficiently large M, every F⊆E with |F|≤M^η, and every A satisfying

    ∪_{e∈F}U_e ⊆ A ⊆ R∩(∪_{e∈F}eℤ),

one has H(A,I)≤2|A| for every I. This includes the full actual source on the chosen cells and arbitrary common endpoints among the cells. The result applies in particular to the private grid theorem at fixed residual density t≥1/4, where |U_e|>(2+δ/128)tL_e≥(1/2+δ/512)L_e. It concerns the isolated source A; an arbitrary previous cover for the complementary source is a separate problem.

## Level credits on a full cell

Assign every row of U_e to e and each other row of A to any chosen cell dividing it. This is possible because the U_e are disjoint. The resulting partition A=⊔ A_e has |A_e|≥(1/2+ε)L_e. Take all positions I_e={b∈I:e divides b} for each e∈F. The quotient I_e/e is an interval of length L_e or L_e+1, while A_e/e consists of distinct integers in [1,L_e]. For a prime ℓ set h_e(ℓ)=v_ℓ(e)+⌊log L_e/log ℓ⌋. Credit a position b∈I_e at level ℓ^j precisely when 1≤j≤h_e(ℓ) and ℓ^j divides b. At any such level with j≤v_ℓ(e), all positions and all assigned rows have the level. When j>v_ℓ(e), divide by e; every quotient interval has at least ⌊L_e/ℓ^(j−v_ℓ(e))⌋ hits, sufficient for all assigned rows. Larger levels have zero assigned demand. These are valid H-level credits for each local group.

Form V=∪ I_e. A local credit can be duplicated only at a position in at least two selected banks. Define D_e as the number of local credits in I_e, summed over all its levels, at positions lying in at least one I_f with f≠e. Then the sum of the remaining global deficits over all prime-power levels is ≤Σ D_e: at each level the private local credits are counted once in V, and discarding all other local credits is conservative. Each deficient level can be repaired with one fresh target position per missing count, because J has ⌊M/ℓ^j⌋ sites at that level and I has at least that many. Each repair improves the chosen level and cannot hurt the others. Consequently

    H(A,I) ≤ |V|+Σ D_e ≤ Σ_{e∈F}(L_e+1+D_e).

## Uniform bound for duplicate credits

Fix e, put L=L_e, N=|F|, y=M^α. The estimate is trivial if N=1. For f≠e put g_f=f/gcd(e,f). Since the cells are distinct products of exactly two distinct primes, g_f>y, including when they share a root. Write b=e v, where v ranges over a quotient interval of length L or L+1. The condition f|b is equivalent to g_f|v.

For each f, separate the at most four exceptional primes dividing ef. They exceed y and have at most 1+log M/log y=O_α(1) relevant levels. There are at most (L+1)/g_f+1 positions of I_e∩I_f. The exceptional credits over all f are thus O_α(N((L+1)/y+1)). This overcounts any duplicates among exception lists and is an upper bound.

For the other primes in an (e,f) comparison, ℓ does not divide ef. At ℓ^j the joint condition on v is ℓ^j g_f|v. On summing over f for which ℓ does not divide ef, then bounding instead by the entire ℓ^j-level of the quotient interval, the credit count is at most

    N(L+1)/(y ℓ^j) + min(N,L/ℓ^j+2).

Indeed the two direct upper bounds are N(L+1)/(yℓ^j)+N and L/ℓ^j+2, and min(a+N,b)≤a+min(N,b). Only ℓ^j≤L need be included. The first term sums to O((N/y)(L+1) log log(3L)) by the prime reciprocal estimate. The terms for j≥2 are O(N√L log(2L)), by the trivial count of prime powers with such exponents.

For 1≤N≤√L the remaining first-level terms satisfy

    Σ_{ℓ≤L prime} min(N,L/ℓ+2) ≪ L(1+log(2N))/log(2L).

Indeed, primes ℓ≤L/N cost at most Nπ(L/N)≪L/log(2L). For L/N<ℓ≤L, split into intervals shrinking by factors of two. There are O(1+log(2N)) bands and each contains primes of reciprocal sum O(1/log(2L)), since ℓ≥√L across the range and the prime-counting upper bound applies at each band. The +2 floor terms summed over all these primes cost O(L/log(2L)). All estimates use only shift-independent divisibility counts.

Together these inequalities give an absolute constant C in the leading term:

    D_e/L ≤ C(1+log(2N))/log(2L)
              + O_α((N/y) log log(3M) + N log(2M)/√L + N/L).

If η<min(α/2,ρ/4), the O-term tends to zero uniformly for N≤M^η and L≥⌊M^ρ⌋, and N≤√L. Choose η smaller as necessary so that Cη/ρ<ε/2. For sufficiently large M, (D_e+1)/L_e≤ε uniformly. Therefore H(A,I)≤(1+ε)Σ L_e≤2Σ|A_e|=2|A|. No integrality rounding or asymptotic budget overspend remains.

For a complete private grid of Ω(log M) left primes and Ω(M^(α/2)) right primes, reduce η if necessary below α/2. Taking Ω(log M) left primes and ⌊M^(η/2)⌋ right primes gives a complete, physically covered subrectangle, for sufficiently large M. Each of its cells contains at least (1/2+ε)⌊M^ρ⌋ disjoint private source rows.

## Dense quotients below half: the level-cover calculation

The same polynomial-size conclusion holds already if |U_e|≥0.3960 L_e for each e. In particular it applies to a hard residual of density t≥0.198 by the private grid theorem. This extension uses the repository's certified density estimates in density_2026_11_26/PROOF.md and PROOF-3960.md. Their stated covering theorem concerns ordinary products. The following argument transfers their relaxation proof to H itself, before rounding.

**Dense level lemma.** For an absolute σ>0 and all sufficiently large L, every B⊆[1,L] of density d=|B|/L≥0.3960 has a level cover on any L consecutive positive integers of cardinality at most 2|B|−σL.

To see this, give the separate level constraint at p^j≤L its own price w_{p,j}, obtaining the dual objective Σ_B X−Σ_I(X−1)_+ with X=Σ_{p,j}w_{p,j}1_{p^j|b}. Full target supply at each such level is at least ⌊L/p^j⌋, which dominates source demand. Every individual w_{p,j} can be clipped to one: on the positions hit by that level the hinge stays linear down to price one, so the decrease of the target penalty is at least the decrease of the source term. All prices therefore lie in [0,1].

Use the choices of y,z in PROOF.md and put s=Σ_{p≤y,j}w_{p,j}1_{p^j|b}, W=Σ_{y<p≤z}w_{p,1}1_{p|b}. Omitting p>z and higher levels of p>y increases the upper bound on the dual by at most o(L), uniformly. For the source, first levels above z cost ≤LΣ_{z<p≤L}1/p=o(L), higher levels cost ≤LΣ_{p>y}1/[p(p−1)]=o(L); omitting them in the target hinge only lowers the penalty. The narrow discarded band around exponent 1/2 in PROOF.md also has reciprocal mass o(1). The small load s is nonnegative and determined by the complete small-prime profile. Its untruncated linear total obeys Σ_I s≥Σ_[1,L]s termwise at each p^j. No comparison of unbounded profile functions in total variation is needed.

For explicit verification of the only step which involves s, put μ=Σ w_{p,1}/p over retained large primes, c=(s+μ−1)_+, and let G be the verified lower bound for the conditional target mean of (W−1)_+. The original conditional first moments on each small-profile event and the cap calculation give

    Σ_I min(1,s+W) ≤ Σ_J [min(1,s+μ)−(G−c)_+] + o(L),  J=[1,L].

In the region c≥G use the tangent min(1,s+μ)+1_{s+μ<1}(W−μ). In the complementary region use min(1,s+W)≤s+W−(W−1)_+. Subtract the proposed comparator there: the pointwise difference is at most (W−μ)−((W−1)_+−G). Thus the error estimates use only conditional large-prime first moments and the hinge bound. The comparator is a bounded profile function up to the same uniform bounds on G as in the density proof (even G≤O(log log L) is absorbed by its profile error). All profile tests remain valid for these independent level prices.

Use Σ_I W≥Σ_J W, Σ_J W=Lμ+o(L), Σ_I s≥Σ_J s, and min(1,s+μ)=s+μ−c. On B bound the comparator min(1,s+μ)−(G−c)_+ by one; on J outside B subtract c+(G−c)_+≥max((μ−1)_+,G). This gives precisely the repository's key bound

    Φ/L ≤ d+ E_J[1_B(W−E_J W)] −(1−d)max((μ−1)_+,G)+o(1).

The variance, pair/triple, and source/target coupling estimates following it concern only W, its first-level weights in [0,1], and the indicator of B. Hence all the same rational certificates give the same bound Φ/L≤d+1/2−(1−d)Γ₀/2+o(1). They have fixed strict margins below 2d on the finite parameter intervals from 0.3960 up to one half, as explicitly recorded in PROOF.md and PROOF-3960.md. For 1/2≤d≤0.51 the variance-only certificate verify-variance.js gives Γ₀=0.3168 independently of d, since it uses no source bonus R and all other charges in Γ are independent of d. This leaves a fixed margin there too. For d≥0.51 the entire L-point interval costs ≤2|B|−0.02L. Finally the level LP has at most π(L)+O(√L log L)=o(L) constraints, so rounding a primal vertex upward preserves fixed slack. Choosing σ smaller than the finitely many resulting margins proves the lemma. The arithmetic calculation uses the ambient J throughout, allows the row 1, and never requires max B=L.

**Application to the selected cells.** Keep the source partition used above. In the quotient e use any L_e consecutive target positions and apply the dense level lemma to B=A_e/e. Pad the resulting selected quotient positions to at least |A_e|, which preserves an upper bound 2|A_e|−σ' L_e after replacing σ by min(σ,0.1). On multiplication by e these positions meet every local level demand: the first v_ℓ(e) root levels are paid by their count, and levels above the root use the shifted quotient level demands. Credit only the levels j≤h_e(ℓ) defined above. All duplicate credits are bounded by exactly the same D_e calculated for the full banks, since only subsets of those banks were selected. Choose η smaller than necessary for (D_e/L_e)≤σ'/2. Then the union and the fresh-level repairs use at most Σ_e[2|A_e|−σ' L_e+D_e]≤2|A|. This establishes the stronger polynomial gluing statement for H, with no surrogate valuation model.

## Applying the improved density threshold

The same level-price proof also admits the [improved density certificate](DENSITY_THRESHOLD.md). After the profile inequality the new Bernoulli variance identity, conditional means and pair bounds involve only the first-level middle and high weights and the canonical source indicator. All are unchanged in the level formulation. The finite proof excludes an entire sequence with dual cost at least twice the source size minus $o(L)$ on each of its compact subintervals. It therefore supplies uniform positive slack below twice the size there, by compactness, as required for polynomially many cells. With this certificate the physical gluing conclusion holds for $t\ge0.3930/2=0.1965$. It applies to the density of the actual input to the rectangular selection.
