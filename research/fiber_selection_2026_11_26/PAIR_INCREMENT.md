# A calibrated density increment on intersections of two prime progressions

Write t=n/M, J=[1,M], C_d=|A∩dℤ| and L_d=floor(M/d). H(A,I) is the minimum number of positions meeting each source prime-power level count. Fix 0<δ<1 and suppose H(A,I)>(2+δ)n. This is necessary for a violation of the same bound for the ordinary product. Assume t≤1/2 (otherwise the whole interval suffices). The following bounds are uniform in the shift.

**Theorem.** Set z=M^(3/4). Use either of the following choices, with M sufficiently large for the fixed parameters.

* If t≥1/(log M)^K for fixed K>0, take y=exp((log M)^a) for any fixed 0<a<1.
* If t≥t_0>0, one can take y=M^α for a fixed α=α(t_0,δ)>0.

Preassign **any** set S_0 of at most y prime bases to exclude. There is a set of primes P outside S_0 with

    y<p≤z,    C_p>(1+δ/64)t L_p,    C_p≥δ n log M/(256 z).           (1)

There is a family of products d=pq≤M of distinct primes. One prime lies in P and the other lies either in P or above z outside S_0. Each product in the family satisfies

    C_d > (33/32)t L_d.                                                (2)

Some union V⊆J of progressions from this family satisfies, with D=1+log(M/n),

    |A∩V| > (65/64)t |V|,
    |A∩V| ≫_δ n [log(2+D)/D]².                                        (3)

At fixed positive density these are a positive fraction of the original distinct source rows. Moreover the products in (2) and (3) can all be restricted to d≤M^(1−ρ) for some ρ=ρ(t_0,δ)>0, so **every selected fiber has polynomially many rows**. More generally if t log y→∞, the products can be restricted to d≤M exp(−t log y/256). At t of order 1/log M the stated row count is for the union. We do not assert growing occupancy of each individual pair at that density.

## An inverse inequality after fitting the source on a chosen prime set

At p>z each row contains at most one such prime, to exponent one. Let B count these rows. Independently for each such prime select C_p distinct multiples in I, costing at most B in total. For the small primes minimize Σ_b y_b+Σ_d s_d subject to Σ_{b:d|b} y_b+s_d≥C_d, with 0≤y_b≤1 and s_d≥0, for all levels d=p^j≤M, p≤z. The number r of constraints is O(z+sqrt M log M)=o(n). At a vertex, round at most r fractional positions up; the remaining integer shortages cost at most Σ_d s_d in fresh sites (use nested repair separately at each base). Union with the large-prime positions. LP duality gives a vector 0≤w_d≤1 such that

    H ≤ B+r+Φ,   X(b)=Σ_{d|b} w_d,   Φ=Σ_A X−Σ_I(X−1)_+.

Thus Φ>(2+δ)n−B−o(n) and is positive. The absolute mass estimates Σ_{p≤z}w_p/p<10 and Σ_{p^j≤M}w_{p^j}/p^j≤11 follow from the [earlier variance argument](../twelve_routes_2026_11_26/PRICE_AND_INVERSE.md), which works for these level weights. Explicitly Φ≤M−Σ_{J outside A}X since every level count in I dominates its J count. For Y=Σ w_p 1_{p|b}≤X and μ_0=Σ w_p/p, canonical floor counts give E_J(Y−μ_0)²≤3μ_0. Hence s−sqrt(3s)≤1 for s=(1−t)μ_0, so μ_0<10. The extra reciprocal sum at j≥2 is at most Σ_{m≥2}1/[m(m−1)]=1.

Put S=S_0∪{p≤y}. Define f at every S-profile occurring in J to be the proportion of its canonical rows belonging to A, and zero on absent profiles. Then Σ_J f=n and Σ_{J:d|u} f(u)=C_d for every power of a prime in S. Pointwise (X−1)_+≥f(X−1), so

    Φ ≤ Σ_I f + Σ_d w_d (C_d−F_I(d)),      F_I(d)=Σ_{b∈I,d|b} f(b).

Take T=M^(3/4). For d≤T the quotient intervals have length at least floor(M^(1/4)). By the [profile estimate](../unrestricted_shifts_2026_11_26/SUBPOWER_PROFILES.md) their S-profile laws, including that of J itself, are within ε of the same geometric model. In the first regime |S|≤2y gives ε smaller than every fixed inverse power of log M. In the second, log of the |S|-th prime is at most (α+o(1))log M, and the ratio of quotient log length to this log is ≥1/(5α) for large M. Choose α small enough that ε<t_0 δ/10000. These estimates apply to f(dv) as a function of the quotient v. For d based in S, |C_d−F_I(d)|≤2ε M/d+O(1). For d based outside S, f(dv)=f(v), and F_I(d)=t L_d+O(2ε M/d+1). Also Σ_I f=n+O(2ε M). All comparison errors together are ≤δn/32 for large M after using the mass bound 11 and r=o(n) (or further decreasing α). Terms at d>T are all higher powers, with aggregate positive contribution O(M log M/sqrt T)=o(n). Outside S, all higher powers cost at most M Σ_{p>y}1/[p(p−1)]=O(M/y)=o(n).

We have thus reduced to first powers outside S. Primes with C_p<δ n log M/(256 z) contribute at most δn/64 for large M by the prime-counting upper bound. Primes with C_p≤(1+δ/64)t L_p contribute at most (10δ/64)n in positive weighted excess. Keep the remaining primes P, and put μ=Σ_{p∈P}w_p/p<10. Writing v_i=w_i for primes in P and v_i=1 for primes i>z outside S_0, set Z(b)=Σ_i v_i 1_{i|b}. The large primes above z excluded by S_0 cover at most |S_0|M/z=o(n) canonical rows, taking α<1/8 in the second regime. Since t Σ_{p∈P}w_p L_p=nμ+o(n), the preceding estimates give

    u=(1/n)Σ_A Z ≥ 1+μ+δ/2.                                         (4)

The fitted predicate is essential here: its canonical levels on the excluded prime set are accounted for simultaneously before looking for a further density increase.

## From marginal excess to overpopulated products

Let c_{ij}=v_i v_j for i<j. On J there is at most one prime >z per integer. Since all v_i≤1, the weighted number of unordered distinct pairs present in b is at least (Z(b)²−Z(b))/2. Cauchy–Schwarz on A and (4) therefore bound Σ c_{ij} C_{ij}/n below by (u²−u)/2. On the canonical background use L_{ij}≤M/(ij), and omit the impossible pairs with both primes >z. The background bound is

    t Σ c_{ij} L_{ij}/n ≤ μ²/2+μℓ,    ℓ=Σ_{z<q≤M}1/q≤0.30

for large M, by Mertens since ℓ→log(4/3). Subtraction gives a weighted excess at least n[(1/2−ℓ)μ+δ/4]. Pairs failing (2) can contribute at most n(μ²/2+μℓ)/32≤(5.30/32)μn. Hence the pairs satisfying (2) retain a surplus of at least

    Σ_{hot pairs} c_{ij}(C_{ij}−tL_{ij}) ≥ n(δ/4+0.03μ).             (5)

Here and below “hot” means exactly (2) within the specified pair family.

If t log y→∞, put H_0=exp(t log y/256). Discard pairs with ij>M/H_0. Every pair has a first prime in P and a second prime ≥y. After fixing the first, the sum of reciprocals of allowed second primes is at most log(H_0)/log y+O(1/log y)≤t/128 eventually. This follows from Σ_{p≤v}1/p=log log v+c+O(1/log v), clipping both endpoints to primes ≥y. Bounding C_{ij}≤M/(ij), the positive contribution discarded is at most Mμt/128=μn/128. Thus a surplus of at least δn/4 remains. For t≥t_0 and y=M^α this gives ρ=t_0 α/256. The same conclusions hold with no cutoff when t log y fails to grow.

## Producing a single union with its actual source density

On the retained pairs let R(b)=Σ c_{ij}1_{ij|b}. Write A_*=Σ_A R and J_*=Σ_J R. Then A_*≥δ n/4 and A_*≥(1+κ)tJ_* with κ=1/32. Let X_P(b)=Σ_{p∈P}w_p 1_{p|b}. On J we have R≤(1+X_P)²/2. For any s≥0, expansion into squarefree divisibility indicators gives

    E_J exp(sX_P) ≤ ∏_{p∈P}[1+(exp(sw_p)−1)/p] ≤ exp(10(exp(s)−1)).

With D=1+log(M/n), choose K_*=C_δ D/log(2+D), with C_δ a sufficiently large fixed constant. The total R on rows of J with X_P>K_* is at most κδ n/256. In detail, take s=log(2+D)/2: (1+X_P)²≤C exp(sX_P/2) for this uniformly positive s. The normalized tail is then at most C exp(10 sqrt(2+D)−sK_*/2), which is ≤κδ t/256 by the choice of C_δ.

Independently select each retained generator ij with probability θc_{ij}, where θ=κ/[16(K_*+1)²]. Let V be their union of divisibility progressions in J. At b the inclusion probability is at most θR(b), and at least θR(b)−(θR(b))²/2 by the first two inclusion-exclusion inequalities. On the source rows with X_P≤K_*, the latter is at least (1−κ/32)θR(b). Deduct the discarded tail and obtain E|A∩V|≥(1−κ/8)θ A_*. Also E|V|≤θ J_*. Hence

    E[|A∩V|−(1+κ/2)t|V|] ≥ κ θ A_*/4.

Some particular union attains this gain. It has both properties (3), with no duplicate source credits. The choices can be made deterministically by conditional expectations, testing each generator in any fixed order.

This argument proves an increase of density inside an actual union and, in the stated range, inside long individual quotient fibers. It does not transfer a covering lower bound for A to any of those quotient source sets. At positive density every single pair here covers at most M/y² canonical slots, so a union capturing a fixed share may require polynomially many generators. The target-side joint cost for a union on that many unrestricted prime bases remains open.

## A polynomial-density version, including n of order M^0.8

Assume log n/log M→β with 3/4<β<1, keep z=M^(3/4), and allow any excluded set |S_0|=o(log M/log log M). Put y=sqrt(log M). Under the same fixed-gap hypothesis, (3) and its constant 65/64 continue to hold for a union of intersections of **two distinct prime-power level conditions**. Each intersection has density greater than (33/32)t. One condition is an overpopulated level p^j of a prime y<p≤z outside S_0; it satisfies the bounds (1) with C_{p^j}, L_{p^j} in place of C_p,L_p. The other condition is either another such level or a prime >z outside S_0. At one base two different levels have lcm equal to the larger power. For squarefree sources all overpopulated levels are first powers, and the two bases in every pair are distinct. No macroscopic size bound for each separate intersection is claimed here.

To prove this, fit f on the **capped** profiles of S=S_0∪{p≤y}, with caps floor(log_p M). In J these are the full profiles. The finite-difference expansion in [the transfer proof](TRANSFER.md) has norm W=M^o(1). For levels in S the discrepancy is at most W. For any level d based outside S all expansion moduli are coprime to d; expanding their joint counts gives F_I(d)=(M/d)E f(G)+O(W)=tL_d+O(W+1), even at d>M^(3/4). Summing over the O(z+sqrt M log M) levels with p≤z costs o(n), since β>3/4. Also |S_0|M/z=o(n). Retain all eligible levels outside S, including higher powers. The number of levels is at most 4z/log M for large M, so rejecting lightly populated levels with threshold δ n log M/(256z) costs at most δ n/64. Rejecting levels without the relative marginal gain costs at most 11δ n/64. We obtain (4) with μ now the sum of w_d/d over **retained** small-prime levels, bounded by 11. Replacing floor(M/d) by M/d in the weighted baseline costs o(n).

For pairs of levels with different bases the canonical background calculation is unchanged. For pairs on the same base it gains at most nΣ_{p>y}Σ_{j≥2}(j−1)/p^j=O(n/y), since lcm determines their intersection. The canonical bound is now n(μ²/2+μℓ+o(1)). With μ≤11 and ℓ≤0.30 we have 1/2−ℓ−(μ/2+ℓ)/32≥0.018, leaving a surplus at least δ n/5 on the retained (33/32)-uplifted intersections for large M. The inequality involving Z²−Z is still valid for distinct label occurrences even when two labels have the same base.

For completeness the tail truncation used in the union step also survives repeated powers. The load of retained small-prime levels is bounded by Σ_{p>y}[w_p 1_{p|b}+(v_p(b)−1)_+], taking w_p=0 for omitted first powers. Nonnegative divisibility increments bound its canonical exponential moment by the independent geometric model. When e^s≤y/2, the factor at p is at most 1+(e^s−1)w_p/p+O(e^(2s)/p²), by summing the geometric tail from exponent two. Its log moment is therefore ≤10(e^s−1)+O(e^(2s)/y). Use s=log(2+D)/4, for which e^(2s)/y=O(1), and enlarge C_δ in the cutoff K_*. The same two-term inclusion-exclusion and expectation argument proves (3). Duplicate generator moduli from different pairs may be independently sampled as labels; their union still counts each underlying row once.

The same proof works at every fixed β>exp(−1/2), with constants changed if necessary. Choose exp(−1/2)<γ<β and z=M^γ. Then ℓ→log(1/γ)<1/2 and the rounding and expansion errors are still o(n). Choose any κ>0 with 1/2−log(1/γ)>κ[11/2+log(1/γ)]. The pair and union density multipliers are 1+κ and 1+κ/2 respectively; retaining a fixed positive margin in this strict inequality pays for the o(n) terms. In particular **γ=5/8, κ=1/256** works for every β>5/8, including β=2/3. At β>3/4 the preceding 33/32 and 65/64 bounds are stronger.

## What the overlap looks like in the distinct-prime theorem

In the positive-density and logarithmically sparse regimes, form the graph of all distinct-prime pairs permitted by (1),(2), including the size cutoff when available. It is defined from A before any exclusions, using the smaller endpoint for the marginal condition. A fixed-gap violation has the following additional consequences.

* This graph contains at least floor(y/2)+1 vertex-disjoint edges. The endpoints of a maximal matching hit every edge; if there were at most y such endpoints, take them as S_0 and apply the theorem.
* Even the union of **all** pairs of any matching has canonical size O(M/(y log y)). Indeed 1/(pq)≤(1/p²+1/q²)/2, the endpoints are distinct, and Σ_{p>y}1/p²≪1/(y log y) by partial summation. This is o(n) in both regimes. The large source mass in (3) must reuse prime bases. More quantitatively orient each chosen pair from its smaller endpoint p, which necessarily lies in P. If the maximum outgoing degree is Δ, then |V|≤MΔ Σ_{p>y}1/p². Consequently the graph outside any excluded S_0 has a marginally lifted prime with at least c_δ t y log y [log(2+D)/D]² distinct larger partners.

There is also a local density statement inside one prime fiber. After the exclusions, there exists p satisfying (1) and a union V_p of pairs pq with this **same** p, for which

    |A∩V_p| > (65/64)t |V_p|,
    |A∩V_p| ≫_δ t L_p log(2+D)/D.                                    (6)

To prove it use the weighted hot pairs remaining in (5) after any permitted cutoff, oriented by their smaller prime. Their total source weight is at least δ n/4 and Σ_{p∈P} w_p L_p≤10 M. Hence some p with w_p>0 has Σ_{q outgoing}v_q C_{pq}≥(δ/40)t L_p. Every term also satisfies (2). In the canonical quotient [1,L_p] the corresponding weighted incidence is Y=Σ_{q outgoing}v_q 1_{q|u}. Its exponential moment there is at most exp(11(exp(s)−1)), because the sum of v_q/q is ≤10.30. Put K_*=C_δ D/log(2+D) as above, enlarging C_δ as needed. The weight ΣY over quotient rows with Y>K_* is ≤κδ t L_p/2048, by the same tail inequality. Select each q independently with probability θ v_q, now taking θ=κ/[16(K_*+1)]. First and second inclusion-exclusion give the same relative loss bounds on Y≤K_* and loss at most κ/32 of the source weight from the truncated tail. The conditional-expectation argument for (3) gives (6), with one factor of K_* instead of two. Multiplying the quotient rows back by p preserves all these counts because L_{pq}=floor(L_p/q).

Thus either the p-fiber itself has density greater than (129/128)t, or the selected union in its quotient has density greater than (130/129) times the density of that p-fiber. This is an increase in the source population density. The theorem does not assert that the quotient is a further covering counterexample.
