# A doubled source-density inverse at every nontrivial scale

Let J=[1,M], I any length-M interval of positive integers, A⊂J, n=|A|→∞, t=n/M≤1/2. Let H be the shift's minimum level cover. Fix 0<δ≤1 and assume H>(2+δ)n. By the existing universal two-block cover at M≥(2n)^3, necessarily M<(2n)^3. For any preassigned S0 of o(log M/log log M) prime bases and y=floor(sqrt(log M)), there are prime powers d=p^j, e=q^k with distinct bases p,q>y outside S0, each individually enriched above (1+δ/64)t, whose intersection satisfies

    C_de > (2+δ/64)t floor(M/(de)).

A union of such progressions has actual density >(2+δ/128)t and contains ≫δ n [log(2+D)/D]^2 source rows, D=1+log(M/n). A union having a *single common prime-power level* d also reaches the latter density and contains ≫δ t floor(M/d) log(2+D)/D rows. The claim is uniform over all eligible n,M at every fixed δ; the hidden constants depend only on δ. No new lower bound for the cover in a quotient is implied. At positive and logarithmically sparse densities the stronger established choices of large excluded sets and absolutely populated marginal labels remain available under the separately established small-profile transfer.

## 1. Exact LP grouped by base and small occupied terminal reciprocal mass

Take γ=δ/1024, z=n^(1−γ). The retained LP contains every level h=p^j≤M with p≤z or p∈S0. Let r count these levels. Since log M=O(log n),

    r ≤ (z+|S0|)log_2 M = n^(1−γ+o(1)) = o(n).

Write Q for the occupied bases q>z outside S0. For large n, M<z^4, hence |Q|≤3n: there are at most three distinct terminal primes in any source. Unconditionally,

    ℓ=Σ_Q 1/q ≤ Σ_{z<q≤n log n, q prime}1/q + 3/log n
      = −log(1−γ)+o(1) ≤ δ/256.

For each q∈Q reserve C_q target sites of highest q-valuation. These meet all q-level demands, regardless of repeated prime factors or several terminal primes per source. Their union costs at most B=Σ_Q C_q.

For the retained LP minimize Σ_b x_b+Σ_p s_p over 0≤x_b≤1, s_p≥0, subject to Σ_{b, h|b}x_b+s_p≥C_h at every level h=p^j. A vertex has at most r fractional site variables. Round them up, then add at most floor(s_p) highest remaining sites for each base, since every deficit at that base is an integer ≤s_p and the whole interval has capacity. Taking the union with the terminal sites is valid. By duality some weights w_h≥0 with Σ_j w_{p^j}≤1 for EACH base p satisfy

    H ≤ B+r+Φ,    Φ=Σ_A X−Σ_I(X−1)_+ ≥0,    X(b)=Σ_{h|b}w_h.

The dual includes zero and its maximum is nonnegative even when B>2n.

For completeness, μ_all=Σ_h w_h/h<8 for large M. On J the mean of X lies in [μ_all−r/M, μ_all]. Each per-base load X_p is in [0,1]. Since distinct-base levels are coprime, E_J X² ≤ μ_all+μ_all² by X_p²≤X_p and canonical floor upper bounds. Thus E_J(X−μ_all)²≤2μ_all for large M. On the other hand, 0≤Φ≤M−Σ_{J outside A}X because every single-level count on I dominates the corresponding one on J. Cauchy gives s−sqrt(2s)≤1 for s=(1−t)μ_all, whence μ_all≤2(2+sqrt(3))<8. This is valid for the optimized common-slack LP.

## 2. Fitted profiles and two baselines at every level

Set S=S0∪{p≤y} and let f on each capped S-profile be the source fraction of its canonical class (zero on empty classes). Caps are floor(log_p M). The established finite-difference identity f(b)=Σ_e c_e 1_{e|b} has norm W=Σ_e|c_e|≤∏_{p∈S}(1+2 floor(log_p M))=M^o(1). Its moduli have bases only in S. Since M≤(2n)^3, rW=o(n) uniformly along the chosen sequence.

Write F_I(h)=Σ_{b∈I,h|b}f(b). Then Σ_I f=n+O(W), and F_I(h)=C_h+O(W) for all powers on S, because all intersections have discrepancies at most one. For any retained h based outside S, each expansion modulus is coprime to h, giving F_I(h)=(M/h)Σ_e c_e/e+O(W)=tM/h+O(2W). These estimates hold without a length condition on h.

Remove from the retained bases outside S all levels with C_h≤(1+δ/64)t floor(M/h), and optionally remove levels with C_h<δ n/(64r). The total loss in weighted positive discrepancy is at most δn μ_all/64+δn/64. Call the surviving labels P, put Y(b)=Σ_{h∈P:h|b}w_h and μ=Σ_{h∈P}w_h/h. Remove from Q also any q failing C_q>(1+δ/64)t floor(M/q); this loses at most (1+δ/64)nℓ≤δn/128 of B. Call the remainder Q'. Let Z=Y+Σ_{q∈Q'}1_{q|b}.

The nonnegative slack R=Σ_I[(X−1)_+−f(X−1)] satisfies

    R ≥ Σ_I(1−f)(X−1) ≥ Σ_I(1−f)(Y−1)
      = (1−t)M(μ−1)+O(rW).
    Hence R ≥ (1−t)M(μ−1)_+−o(n).

Here Σ_I Y=Mμ+O(r), Σ_I fY=tMμ+O(rW). Substitution in the exact identity Φ=Σ_I f+Σ_h w_h(C_h−F_I(h))−R and the LP cover bound yields, uniformly for large n,

    u=E_A Z ≥ 1+μ+δ/2 + [(1−t)/t](μ−1)_+.

The discarded terms consume at most δn(8/64+1/64+1/128)+o(n); retaining just δ/2 leaves substantial slack.

## 3. Distinct-base pairs, actual unions and a common root

The source pair score counts *only distinct bases*. For each base p let Z_p be its total retained load, so 0≤Z_p≤1, including terminal labels. Pointwise,

    Σ_{p<q} Z_p Z_q = (Z²−Σ_p Z_p²)/2 ≥ (Z²−Z)/2.

On J every two levels at distinct bases are coprime, so t times the total weighted canonical pair count is ≤ n(μ+ℓ)^2/2. Equality is unnecessary; the bound includes terminal-terminal pairs. Let b=1+μ for μ≤1 and b=2μ otherwise. We have u≥b+δ/2 and b(b−1)≥2μ². For λ=2+δ/64 the normalized surplus is at least

    δ(2b−1)/4 −δ μ²/128 − λ μℓ − λℓ²/2.

This exceeds (δ/8)max(1,μ) uniformly: for μ≤1 the lower bound divided by δ is at least 1/4−1/128−3/256−3/(2·256²)>1/8. For μ≥1 use 2b−1≥3μ, μ≤8, and λ<3, giving ≥μ(3/4−8/128−3/256−3/(2·256²))>μ/8. Remove pairs with C_de≤λ t L_de, which only increases the surplus. Thus some pair satisfies the claimed doubled density; all its labels pass the stated individual marginal test. The total weighted source mass A* on hot pairs is ≥δn/8 and A*≥λ t J* with J* their weighted canonical mass.

For a uniform elementary tail bound note E_J exp(sZ)≤exp[(μ+ℓ)(exp(s)−1)] for s≥0. Indeed each per-base exponential is a nondecreasing function of its valuation, hence is a sum of nonnegative nested divisibility increments. Expansion into levels on distinct bases and the canonical floor bound compare its expectation to the independent geometric model. There the expected increment at p is ≤(exp(s)−1)E Z_p by 0≤Z_p≤1. The hot pair weight at a row is at most Z²/2. With D=1+log(1/t), T=Cδ D/log(2+D), choose s=log(2+D)/2 and take Cδ large enough to leave at most δ A*/4096 weight on Z>T over J. Independent thinning with inclusion probabilities θ v_d v_e, θ=δ/[2048(T+1)^2], gives a union: source occupancy expectation ≥(1−δ/1024)θ A*, canonical expectation ≤θ J*. Because 1−(2+δ/128)/(2+δ/64)=δ/[128(2+δ/64)]>δ/260, the density gain has expectation ≥δ θ A*/512, proving the quoted row count.

Orient edges by any fixed order of bases. Since Σ_i v_i L_i≤M(μ+ℓ)<9M, some root level d=p^j of positive weight has outgoing source weight Σ_{e outgoing}v_e C_de≥δ t L_d/72. In the canonical quotient [1,L_d] the other bases differ from p, hence the same exponential bound applies to their combined load, with total reciprocal ≤μ+ℓ. Repeat the tail removal and thinning with θ=δ/[2048(T+1)] and Cδ sufficiently large relative to the root bound; every outgoing edge is hot. This yields the stated actual star and its population. The argument counts distinct source positions even with repeated prime-power indices on partner bases.

The proof is based on [the preceding inverse theorem](../fiber_selection_2026_11_26/PAIR_INCREMENT.md) and [the profile expansion](../fiber_selection_2026_11_26/TRANSFER.md); the additional ingredients are the common LP slack, calibration's second baseline and the cardinality bound for occupied terminal bases.
