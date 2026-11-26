# Complete grids with pairwise disjoint, doubled source fibers

Let R be a hard source in the original ambient interval [1,M], after the terminal-row deletion when it is used. At fixed positive density the polynomial length cutoff is available directly for the original hard source, without deleting any rows. Put m=|R|, t=m/M, C_pq=|R∩pqℤ| and L_pq=⌊M/(pq)⌋. Fix 0<δ≤1. The only structural input is the oriented doubled-pair family from [the first-power inverse](TWO_BASELINES.md), after any stated product cutoff. An edge (p,q) goes from the left copy of its smaller prime to the right copy of its larger prime, both exceeding y. With the edge price 0<c_e=w_p v_q≤1,

    C_e > λ t L_e,   λ=2+δ/64,   A_*:=Σ_e c_e C_e ≥ δm/10.

Each edge is occupied. All densities use the residual population m at the original M. At y≥H₀=exp(log M/[D(log D)²]), D=log log M, the original peel guarantees L_e≥⌊H₀⌋. At fixed positive density, take y=M^α and retain the polynomial cutoff L_e≥⌊M^ρ⌋. Taking subgraphs preserves all originally established marginal and exclusion conditions.

## Private source rows on individual cells

Write k(u)=#{p>y:p divides u} and H=max(1,Σ_{y<p≤M}1/p). Choose Q≥1 so that packed input incidence on source rows with k(u)>Q is at most δ A_*/65536. The deterministic Q=log M/log y always works. Set

    κ=δ/[65536(Q+1)²],     λ₁=2+δ/128.

Retain every input edge independently with probability κc_e. For a retained edge e, let U_e consist of the rows u∈R divisible by e and by no other retained edge. These sets are pairwise disjoint. Write C°_e=|U_e|. At a source row u with k(u)≤Q, conditional on retaining one of its edges, the probability of retaining another is at most κQ² by independence and the union bound. On all other source rows use the bound one. Thus expected total sampled incidence is κA_*, and expected total sampled loss Σ_retained(C_e−C°_e) is at most

    κ(κQ²A_*+δ A_*/65536) ≤ δ κ A_*/32768.

Discard any retained edge with C°_e≤λ₁tL_e. At each discarded edge its loss is ≥(1−λ₁/λ)C_e>δC_e/260. Its entire raw count may therefore be charged at most (260/δ) times its loss. The expected sum of the private counts over surviving edges is ≥κA_*−(1+260/δ)δκA_*/32768≥(9/10)κA_*. Fix an outcome attaining at least this expectation bound. Its surviving graph G thus contains at least 9δκm/100 pairwise distinct private source rows, and each of its edges individually has C°_e>λ₁tL_e. Privacy here is with respect to every edge originally retained in the random sample, including edges later discarded.

## Packing complete growing prime rectangles

Use bipartite copies as above. Put mass 1/(Hp) at each real prime vertex p on each side, and add an isolated dummy to each side to bring its total mass to one. Each real vertex has mass ≤1/y. Set

    d₀=δκt/(1000H²),    r=⌊log y/[2 log(1/d₀)]⌋,    s=⌊√y/3⌋.

For the regimes below, r→∞ and r²/y=o(y^(−1/2)). In a remaining subgraph whose reciprocal sum Σ_e 1/(pq) is at least d₀H², the product probability of an edge is at least d₀. Sample r independent left vertices. The expected right measure of their common neighborhood is ≥d₀^r by Jensen's inequality. A tuple containing a dummy has zero common neighborhood; the probability that two positions coincide at a real vertex is at most binom(r,2)/y. Thus some tuple of distinct real vertices has common-neighbor measure at least d₀^r−binom(r,2)/y≥(1/2)y^(−1/2). The real atom bound yields at least s distinct common right primes. Each right label exceeds every chosen left label, by the original orientation.

Remove the edges of such a complete r-by-s rectangle and repeat until the remaining reciprocal sum is <d₀H². This finite procedure yields edge-disjoint complete rectangles. Unallocated edges lose private mass at most M d₀H²=δκm/1000 because C°_e≤M/(pq). Therefore their packed edges T satisfy

    S_T=Σ_{e∈T}|U_e| ≥ δκm/12.

For every F⊆T the assigned source sets U_e, e∈F, are genuinely disjoint and individually |U_e|>λ₁tL_e. Put V_W(F)=union of the multiples of these edges in an M-point interval W. In particular with J=[1,M], for every nonempty F,

    S_F:=Σ_{e∈F}|U_e| > λ₁t Σ_{e∈F} L_e ≥ λ₁t |V_J(F)|.

Hence each individual rectangle as well as every union of its cells retains doubled density with mutually disjoint source assignments. As every L_e→∞ uniformly, |W∩eℤ|≤L_e+1 gives, uniformly in the shift W and all F, with λ₂=2+δ/256,

    S_F − λ₂t Σ_{e∈F}|W∩eℤ| ≥ (δ/1100) S_F

for sufficiently large M. Indeed the ratio of the subtracted term to S_F is at most (λ₂/λ₁)(1+1/min L_e), and 1−λ₂/λ₁>δ/516. This is a count comparison with target lengths, even when overlaps on the target are counted several times. It does not construct a simultaneous target cover or transfer a price gap to one cell. The lower bound S_T concerns the combined disjoint mass; an individual rectangle need not carry that full mass.

## Quantitative regimes

At fixed t≥t₀ use y=M^α, Q=1/α. Then H=O_α(1) by the prime reciprocal sum estimate, κ≫_{δ,α}1 and log(1/d₀)=O_{δ,α,t₀}(1). The union has Ω_{δ,α}(m) distinct assigned rows. Each rectangle has Ω_{δ,α,t₀}(log M) left primes and Ω(M^(α/2)) right primes; every pair quotient has length at least ⌊M^ρ⌋ when the polynomial cutoff is used.

For t≥(log M)^(−K), K fixed, retain the original peel but increase the later hot-pair cutoff to

    y=exp(a log M log D/D)

for a sufficiently small fixed positive a=a(δ,K). To verify the audit under this choice, its comparison quotient lengths are at least ⌊M^γ⌋, γ=δ/1024. There are at most 2y profile primes and the logarithm of the prime of rank ⌊2y⌋ is (1+o(1))log y. The estimate in unrestricted_shifts_2026_11_26/SUBPOWER_PROFILES.md is O(exp(−c min(log(length),u log(2u)))) with u the ratio of the logarithms of length and rank prime. Since u≥(γ/(2a))D/log D eventually, taking a small gives error O((log M)^(−K−2)). All other losses are as in the audit: M/y=o(m), |S₀|M/z=o(m) for allowed exclusions of size at most y, and the large-power and rounding errors do not grow. Both endpoints exceed the original peel cutoff H₀, ensuring L_e≥⌊H₀⌋.

Here Q=B=log M/log y=D/(a log D) deterministically, H=O(1+log B), and log(1/d₀)=O_{δ,K}(D). The packed union has Ω_{δ,K}(m(log D/D)²) distinct assigned rows. Every complete rectangle has Ω_{δ,K}(log M log D/D²) distinct left primes and Ω(√y)=exp(Ω_{δ,K}(log M log D/D)) distinct right primes. All cells retain private density above (2+δ/128)t. The same order of aggregate distinct-row mass holds for the original y=H₀ using Q=C_K D/log D: the nonnegative divisor expansion gives M^(−1)Σ exp(h k(u))≤exp((exp(h)−1)H), H≪log D. With h=(log D)/2, C_K=8(K+2), the total k(u)² over k(u)>Q is ≤M exp(O(√D log D)−C_K D/4)=o(m). This also bounds all weighted lost incidence on the exceptional rows. The deterministic larger-cutoff version has the stronger grid dimensions above.

The common-neighborhood extraction needs only the doubled hot-pair incidence input, its arithmetic spacing, and the elementary divisibility bounds in J. The price and target-interval information used to infer this input from hardness is in the [first-power inverse](TWO_BASELINES.md).

For a simultaneous integral cover on polynomially many of the private cells, see [the level-by-level gluing proof](PHYSICAL_GRIDS.md).
