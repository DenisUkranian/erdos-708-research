# Conditional and absolute density gain on the same pair

Use the twofold calibration ([the first-power inverse](TWO_BASELINES.md)), with z=M^(1−δ/1024). Also delete terminal primes q>z with C_q≤(1+δ/64)tL_q. This deletes ≤(1+δ/64)ℓn source incidences, where ℓ=Σ_{z<q≤M}1/q≤δ/256. Let i enumerate the surviving labels, with v_i in (0,1], m=Σ_i v_i/i<10+ℓ, u=Σ_i v_i C_i/n. Then every marginal ρ_i=C_i/L_i exceeds (1+δ/64)t and the twofold calibration gives

    u≥1+m+δ/3,       u≥2m+δ/3.

Indeed its bound is 1+μ+δ/2+[(1−t)/t](μ−1)_+, with t≤1/2, and m−µ≤ℓ. In particular m>0.

The following two thresholds can be imposed simultaneously on an oriented edge i→j, where ρ_i≤ρ_j. Write λ=(1+u/m)/2. Up to an absolute constant c>0 they are

    ρ_ij > (1+cδ) max(λt,ρ_i),     ρ_i > (1+δ/64)t.               (1)

Hence λ≥3/2. In the regime u≥3m this gives BOTH more than 2t and a genuine conditional gain on the SAME fibers. A sufficient parameter condition is m≤(1+δ/3)/2, since u≥1+m+δ/3. The conditional gain and the twofold gain cannot in general be intersected from their separate positive masses.

Proof. For independent R,S of the same distribution supported on [1,∞) and mean a, put b=(1+a)/2, h=P(R>b) and H(x)=P(R>x). Then

    E R − E max(b,min(R,S))
       = −∫_1^b (1−H(x)) dx + ∫_b^∞ H(x)(1−H(x)) dx
       ≥ −(b−1)(1−h)+(1−h)(a−b) = 0.

Here ∫_b^∞ H ≥a−b. Under the label distribution with mass v_i/(mi), set R_i=max(1,C_i i/n) and let ũ=m E R. Then u≤ũ≤u+ℓ: small primes i≤z have L_i i/M≥1−M^(−δ/1024), and are marginally hot; increases are charged only to the terminal reciprocal mass. If L_ij≥1, i,j≤M/y, so ρ_i/t ≤(1+O(1/y))R_i and likewise for j. Since L_ij≤M/(ij), nonnegative terms and the iid inequality show that the total ordered potential background of max(λt,min(ρ_i,ρ_j)) against v_i v_j L_ij is at most (1+O(1/y))n mũ. Indeed λ≤(1+ũ/m)/2, and the iid bound includes also infeasible pairs and diagonal terms.

Weighted actual ordered pair mass ≥nu(u−1), by E_A Z²≥u² and sum of squared individual label weights ≤Z. Since u≥1+m+δ/3, m≤u, and ũ≤u+δ/256, the difference exceeds δnu/4 for large M. Inflating the combined threshold by (1+δ/256) still leaves at least δnu/6, since m≤10.01 for large M. On the positively contributing edges (1) therefore holds with c=1/256. In particular their weighted source mass is ≫δnu. If desired the prior product boundary strip can be deleted before extraction at total cost ≪δnu with modified absolute constants. At positive density this retains polynomially many slots in every quotient.

Orient each remaining unordered edge toward the endpoint with higher marginal density, with ties broken in any fixed way. Write T_i=Σ_{i→j} v_j C_ij. Summation gives Σ_i v_i T_i ≫δnu, while Σ_i v_i C_i=nu. Some i consequently has T_i ≫δ C_i. In this quotient every edge obeys (1) with its common lower endpoint i. Thinning using the previous quotient exponential moment E exp(s Σ v_j 1_{j|b})≤exp(m(e^s−1)) yields an actual union V_i with

    |A_i ∩ V_i| > (1+c'δ) max(λt,ρ_i) |V_i|,
    |A_i ∩ V_i| ≫_δ C_i log(2+D_i)/D_i,   D_i=1+log(1/ρ_i).

In detail truncate above K=C_δ D_i/log(2+D_i), to cost o_δ(C_i)≤(δ/2048)T_i after choosing C_δ large. Sample j with probability θv_j, θ=δ/[2048(K+1)]. On the untruncated rows the first two Bonferroni terms give inclusion probability ≥(1−δ/2048)θY. The expected canonical union size is at most θ Σv_j L_ij≤θ T_i/[(1+δ/256)max(λt,ρ_i)]. Choosing c'=1/1024 leaves positive expected surplus ≫δθ T_i. The constants in the population estimate may depend on δ. This conclusion quantifies actual populations and does not assert that the quotient inherits a price gap.

## Rational stress test against the unconditional combination at factor 2

Two exchangeable classes of K≥10000 unit labels each have total canonical reciprocal masses m_L=1/5, m_H=4/5. Use the independent Bernoulli canonical law with marginal m_g/K on each label in class g. Under the source, choose the following class counts (L,H), then choose uniform subsets of the indicated sizes independently between classes.

| Source counts | Number of rows per 10000 |
| --- | ---: |
| (0,1) | 125 |
| (0,2) | 6565 |
| (1,1) | 3193 |
| (3,0) | 101 |
| (4,0) | 16 |

The marginal multipliers are exactly r_L=1.78, r_H=2.056, giving u=2.0008 while m=1. In particular a positive fixed surplus u−2 can coexist with this profile. The normalized total actual factorial pair masses are 0.0798 (LL ordered), 0.3193 (LH, one orientation), 1.313 (HH ordered). The joint maximum thresholds for the blocks LL,LH,HH in infinite-label normalization are 0.08, 0.32, 1.31584, respectively. Exact finite-K capacities are multiplied by (1−1/K) for the two diagonal blocks, leaving strict slack for K≥10000. Thus every individual pair satisfies r_ij < max(2,min(r_i,r_j)), although separate rich pairs of each requisite kind do occur. The canonical law assigns positive probability to every profile. The source is realizable as conditioning on an event after adding one independent uniform variable and choosing a sufficiently small positive density t. The PDF ratio is bounded on the finite canonical space. This is an abstract probability model for the moment argument, not a divisibility counterexample or a feasible supercritical dual of problem 708. It falsifies an inference based solely on these moment, slope, and canonical pair constraints. A universal simultaneous factor-2 theorem would require more arithmetic, dual, or higher-profile information.

## Extension to every admissible sparsity scale

The common-slack, occupied-terminal calibration ([the all-scale inverse](ALL_SCALES.md)) gives the same two inequalities for u and m for all |A|→∞, using prime-power labels d=p^j on distinct bases and base load ≤1. Include the independent iid sample from all labels with mass v_d/(dm). The correction ũ−u from any common-slack label is bounded by v_d/M, since C_d≥tL_d implies (1−C_d d/n)_+≤d/M. There are r=o(n) common-slack levels; for occupied terminal labels the total correction remains ≤ℓ. Every feasible distinct-base pair de≤M has d,e≤M/y. On the background, including same-base iid label pairs only enlarges the bound, and on the source the per-base total load ≤1 gives exactly the needed u(u−1) bound for ordered distinct-base pairs. The quotient star moment estimate also follows from that common-slack proof, since every partner base differs from the root and has total level price ≤1. Thus (1) and its common-lower-endpoint union hold at every eligible sparsity scale, with the exclusions admitted by the corresponding calibration. The criterion u≥3m and the abstract obstruction are unchanged.
