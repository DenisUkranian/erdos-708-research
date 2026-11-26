# A full prime-pair cell can cost three new positions per row, even after reoptimizing the complement

Write τ(B,I) for the minimum number of distinct positions in an interval I whose product is divisible by the product of the distinct source integers B. There are sources R,U⊆[2,M] with M∈R, R∩U empty, and positive translates I of length M, for which U is a disjoint union of complete prime-pair cells, |U|/M→0.02059249… and

    τ(R∪V,I) = τ(R,I) + Σ_{v∈V} (2+v₂(v))           for every V⊆U.

In particular τ(R∪U,I)−τ(R,I)=(3−o(1))|U|. Also τ(R∪U,I)=|R∪U| in this construction. It refutes the unconditional marginal estimate with coefficient two, even allowing a global o(|R∪U|) error, with independent optimization of both minima, and taking cells at 100% source density. The global 2n conjecture is consistent with the example.

## Choosing full cells and singleton reserves

Let M=2^m tend to infinity. Fix a=2/5, b=49/100 and let P be the primes in (M^a,M^b]. Set λ=log(b/a)=log(49/40), u=λ²/2. Define the integer load

    X(i)=v₂(i)+Σ_{p∈P}v_p(i),        H={1≤i≤M:X(i)≥2}.

For each distinct pair p,q∈P put the **entire** cell U_pq={pqh:1≤h≤⌊M/(pq)⌋} into U. Since 3a>1, every cell is disjoint from every other and no member is divisible by p² for p∈P. Every cell has length at least ⌊M^(1−2b)⌋, tending to infinity. The reciprocal prime sum over P tends to λ by Mertens' theorem. Counting each pair with error at most one and using |P|² log M=o(M) gives

    |U|/M→u,        T:=Σ_{v∈U}v₂(v)=|U|+o(M).

For the latter identity, Σ_{h≤L}v₂(h)=L−s₂(L), where s₂ counts set bits, so the error per cell is at most 1+log₂M. Uniformly each individual complete cell has mean load 3−o(1).

For each p∈P write c_p=|{v∈U:p|v}|≤(M/p)(λ+o(1)). Choose a disjoint reserve B_p of c_p odd integers with p-valuation exactly one and with no other factor from P. To see availability, write the integers as p j for odd j≤M/p and discard all j divisible by any member of P, including p. At least (M/(2p))(1−λ−o(1)) remain, uniformly in p, since the total endpoint error O(|P|+1) is o(M/p) by 2b<1. This exceeds c_p because λ<1/3. Banks for different roots are disjoint by construction. Choose also T integers B₂ with v₂ exactly one and divisible by no member of P. From the integers 2 mod 4, removing at most (M/4)(λ+o(1)) leaves enough since (1−λ)/4>u. These banks all lie outside H. Put

    R=(H\U)∪B₂∪⋃_{p∈P}B_p,        A=R∪U.

Thus every priced valuation has the same total on R as on H, exactly. This follows prime by prime since the removed U supplied precisely c_p units of p and T units of 2. Also M∈H\U and 1∉R. The cardinalities are |R|=|H|+|U|+T and |A|=|H|+2|U|+T.

## The translate and both matching certificates

Fix i*=4∈H. For every priced prime s∈{2}∪P require x≡0 mod s^(1+⌊log_s M⌋), so v_s(x+i)=v_s(i) at every position 1≤i≤M. For every other prime ℓ dividing the product of A, prescribe x≡−i* mod ℓ^(Σ_{a∈A}v_ℓ(a)). All these moduli are pairwise coprime, and CRT gives positive x. The target is I=x+[1,M]. Its single position x+i* supplies every unpriced prime demand of every subset of A.

For S⊆I the priced load satisfies

    Σ_{s∈S}X(s) ≤ |S|+Σ_{i∈H}(X(i)−1).

Any product cover for R∪V must have priced load at least Σ_H X+Σ_V X. Consequently τ(R∪V,I)≥|H|+Σ_V X. Conversely take all positions x+H. For each priced root p∈P supplement those by exactly |V∩pℤ| positions from x+B_p. Supplement x+B₂ positions in number Σ_V v₂(v). Every bank is large enough and the selected sites have exactly the designated single priced unit. All unpriced demands are available from x+i*. These positions prove equality. Because X(v)=2+v₂(v) on U, the formula in the introduction follows. The same lower bound holds for the stronger distinct-prime-power-level cover; the CRT hub argument for upper equality uses ordinary product covers only.

## Densities

Counting numbers in the classes 2 mod 4 and 1 mod 2 by single and pair divisibility gives

    |H|/M→1/4+(λ+u)/4,
    |R|/M→1/4+λ/4+9u/4,
    |A|/M→1/4+λ/4+13u/4.

Indeed the mass with v₂=1 and at least one marked odd prime is (λ−u)/4; the mass of odd numbers with two distinct marked primes is u/2. The squares of marked primes have density o(1). The inclusion-exclusion stops at pairs since 3a>1. Thus A has density about 0.36766 and U about 5.6% of A. This example already lies between the previously derived 0.196 local-cell regime and the global 0.392 guarantee, and every cell alone admits its full-density one-position-per-row cover. The inherited global dual has negative signed gap on A; a conditional descent retaining a positive global gap is still a possible route.

## No finite universal marginal coefficient

The same construction gives arbitrarily large *fixed* marginal coefficients on full cells if the global source density can vary. Replace the pivot 2 by any nonempty finite set S of fixed primes, give each unit price, and put d₀=∏_{s∈S}(1−1/s)>0. Let M run through powers of one member of S, retain a>1/3 and b<1/2, and take the fixed positive λ=log(b/a) sufficiently small in terms of S. In place of B₂ take one disjoint singleton bank B_s for each s, marked by exactly one valuation at precisely s. The required count is

    c_s(U)=Σ_{v∈U}v_s(v)=(u/(s−1)+o(1))M,

since Σ_{h≤L}v_s(h)=L/(s−1)+O_s(log(2L)) and all cell quotients tend to infinity. Candidates with exactly one s-unit and no other S-mark have density d₀/s by fixed periodic counting. Removing those carrying a P prime costs at most (d₀/s)(λ+o(1))M, by the same fixed periodic counting after division by each large prime. For each p∈P the candidates p j with j free of all S and all P have count at least (d₀(1−λ)−o(1))M/p, uniformly, by the union bound after division and |P|=o(M/p). For small λ all these supply bounds strictly exceed demand. The candidates for different priced roots are disjoint. Choose i*=s²∈H for some s∈S and perform the identical CRT construction. The two certificates yield, for every V⊆U simultaneously,

    τ(R∪V,I)−τ(R,I)=Σ_{v∈V}(2+Σ_{s∈S}v_s(v)).

In particular each whole cell and the macroscopic union have asymptotic marginal coefficient 2+Σ_{s∈S}1/(s−1). This is unbounded over finite S by divergence of the prime reciprocal sum. The constant positive density |U|/M=u depends on S. The sub-0.392 density calculation above specifically uses S={2}.

## A small exact example

Take M=24, I=[101,124], R={2,4,5,6,8,12,14,15,16,24} and the full 2·5 cell U={10,20}. Price X=v₂+v₅. The seven positions F={104,108,110,112,116,120,124} are exactly those with X>1 in I. Their product covers R, with the same totals of v₂ and v₅ as R, namely 17 and 2. Hence τ(R,I)=7 by the same priced lower bound. The full cell adds five priced units and the five extra positions {102,106,114,105,115} meet them. Thus τ(R∪U,I)=12, exceeding τ(R,I)+2|U|=11.
