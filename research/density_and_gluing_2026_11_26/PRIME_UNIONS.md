# Unrestricted unions of prime progressions and a partial-occupancy test

Let J=[1,M], let I be any interval of M consecutive positive integers, and let H be the minimum cardinality dominating the source counts at every prime-power level. All covers here dominate levels, hence also cover the ordinary product. Write L_d=floor(M/d), C_d=|A∩dℤ|, n=|A|. A finite number of source values equal to one may be discarded from demand.

## Every fully occupied union, all densities and all supports

Take any set P of primes ≤M and let A be all numbers in J divisible by at least one member of P. (The proof works with ambient length M whether or not the last point is used.) Uniformly in M,P,I as n tends to infinity,

    H(A,I) ≤ (2+o(1)) n.

In particular this applies after dividing out a common root p when the quotient source fills the union of the chosen partner-prime progressions. Lift back by multiplying selected quotient positions by p and pad to n distinct multiples to cover the root power contributed by every row. For arbitrary multiples in I the quotient interval has L_p or L_p+1 positions; use any L_p consecutive ones.

Write μ=Σ_{p∈P}1/p, m=Σ L_p. If the source density is bounded below and μ≤1, give every point in F=I∩(union of P-multiples) weight one and all other points weight μ. At a level d=q^j with q in P, F alone has ≥L_d≥C_d hits. At any other level, C_d≤Σ_{p∈P}floor(L_d/p)≤μL_d. Thus all demands are met. The cost is at most (2μ−μ²)M+π(M), since |F|≤μM+π(M). Two-term inclusion-exclusion on J gives n≥M(μ−μ²/2)−π(M). An LP vertex with the same required lower level totals and F fixed to one has at most O(π(M)+sqrt(M)log M) fractional coordinates; upward rounding costs o(n). If μ≥1 choose 0≤u_p≤1 with Σu_p/p=1 and randomly keep each p independently with probability u_p. The union is always contained in A. The first two inclusion-exclusion terms in expectation give n≥M/2−π(M). Use the whole interval.

For density tending to zero, μ must tend to zero: if μ≥c for some fixed c∈(0,1], the same thinning to mass c would give n/M≥c−c²/2−o(1). Furthermore

    m(1−μ/2) ≤ n ≤ m,

because 2 Σ_{p<q} floor(M/(pq))≤Σ_p L_p Σ_{q≠p}1/q≤μm. Hence m=(1+o(1))n even when n is comparable to or smaller than π(M). For each p∈P anchor L_p multiples in I with largest p-adic valuations, breaking ties arbitrarily, and take their union F, of size ≤m. This pays every level at every generating prime: the number of its selected multiples at p^j is min(L_p,|I∩p^jℤ|)≥L_{p^j}. For any other level d with C_d>0 we have d≤K=max_{p∈P}L_p≤n, since each source hit is divisible by pd for at least one generating p. Also C_d≤Σ_p floor(L_p/d)≤m/d. Assign other sites weight λ=m/(M−K), which is <1 eventually. Then λ floor(M/d)≥m/d for d≤K, since floor(M/d)≥(M−K)/d. The cost is at most m+λM=(2+o(1))n. With F fixed one needs constraints only for nonroot prime powers through K. There are O(K/log(2K))=o(n) such powers, so vertex rounding closes. These density arguments imply the uniform sequence statement by passing to a density-convergent subsequence of any alleged counterexample.

## Arbitrary or partially filled stars and a source-only certificate

For any A, fix 0<λ<1 and let

    s_p = max_{d=p^j≤M} ceil( max(C_d−λL_d,0)/(1−λ) ).
    R(L) = number of distinct prime powers in [2,L].

At each p take the s_p multiples in I of greatest p-valuation, then form their union F. There are enough: C_d≤L_d makes s_p≤max_j C_d≤L_p. At d=p^j this supplies min(s_p,|I∩dℤ|) units from these p-anchors alone. Give all sites in F weight 1 and every other site weight λ. At d, if the p-anchors do not take all multiples, the fractional supply is at least λL_d+(1−λ)s_p≥C_d. Otherwise all multiples are already included. If d>λM and C_d>0, λL_d<1 implies (C_d−λL_d)/(1−λ)>C_d−1, and hence s_p≥C_d. All these levels have already been paid integrally. Fix F and round a minimum-cost LP vertex for the remaining levels d≤λM. This gives the finite bound

    H ≤ λM+(1−λ)|F|+R(λM)
      ≤ λM+(1−λ)Σ_p s_p+R(λM).

For λM tending to infinity, R(λM)=O(λM/log(λM)) by counting first powers with the prime-counting upper bound and higher powers separately. For each p the displayed s_p is exactly the smallest integer guaranteeing its levels in the separate p-bank model with canonical-minimum supplies L_d. The statement does not claim that the union bound Σ s_p is always sharp; F can be much smaller.

For example, at λ=(1+o(1))n/M<1, if every level outside an arbitrary root set P has C_d≤λL_d and (1−λ)Σ_{p∈P}C_p≤n+o(n), the coefficient two follows without any support-size bound or any requirement that A fill the star. More generally replace C_p by the smaller s_p and retain the full displayed tradeoff. This can absorb incomplete fibers; no statement for arbitrary half-occupied unions on unboundedly many primes follows. As an illustration of why the sum bound alone cannot prove everything, sufficiently sparse sources consisting entirely of multiples of several fixed primes can have s_p of order n for each such prime; the actual anchors may be shared.

The rounding assertion throughout follows by fixing the chosen coordinates, minimizing the sum of all other weights in [0,1], and observing that more fractional coordinates than level constraints admit a nonzero two-sided perturbation preserving every level total. The selected upward-rounded positions form an actual subset, so an integral certificate obtained this way automatically manages collisions.

### A bounded cofactor-demand corollary for arbitrary holes

Assign to each source row a prime divisor p and remove a positive power of p, leaving a cofactor h. The removed power can depend on the row. Source value one contributes no demand and can be ignored. Let r_p be the number assigned to p, and let D_d count the cofactors divisible by d with multiplicity. If D_d ≤ k/d for every prime power d, then uniformly for k=O(n) and k tending to infinity,

    H ≤ n+k+O(k/log(2k)).

Indeed C_d≤D_d+r_p at d=p^j. When M≤n+k the whole target works. Otherwise use λ=k/M<1. If d≤k, then λL_d≥k/d−λ, hence (C_d−λL_d)/(1−λ)≤(r_p+λ)/(1−λ). If d>k, D_d=0, and since C_d≤L_d we have s_p's candidate for that level at most C_d≤r_p. For each p≤k, upward integer rounding of the former bound costs at most one, giving (1−λ)s_p≤r_p+1. For p>k, s_p≤r_p. Summing gives (1−λ)Σs_p≤n+π(k). Use the source-only certificate and R(k)=O(k/log(2k)). For k bounded the same proof gives the finite error O(1+k/log(2k)).

For example, if the projected cofactors assigned to p form a subset of [1,K_p] without repetitions in each fiber and ΣK_p≤n+o(n), then D_d≤Σ floor(K_p/d)≤(n+o(n))/d and H≤2n+o(n). This criterion allows arbitrary holes and overlaps across different root fibers. It also allows high individual occupancies with arbitrarily many irrelevant large roots. Its input is a bound on cumulative residual counts rather than a uniform density requirement.
