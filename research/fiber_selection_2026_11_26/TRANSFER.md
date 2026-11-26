# Transferring a set determined by prime divisibility

A valuation profile on S means the vector of exponents at the primes of a finite set S⊆[2,M]. Any subset of profiles is permitted, including intersections, unions, and complements of divisibility conditions. Write f for a [0,1]-valued function of the profile, J=[1,M], v=Σ_J f, and I any interval of M consecutive positive integers. For an interval E write F_E(d)=Σ_{b∈E,d|b}f(b). In applications to sets f is an indicator and we select every target satisfying it. The nonnegative error [F_J(p^j)−F_I(p^j)]_+ upper bounds the level deficit on that power for sources contained in the selected canonical set. Adding the highest remaining valuations costs at most the maximum level deficit at each prime. All estimates below are uniform in the shift, in the profile predicate, and in the actual primes of S under the stated bounds.

## Logarithmically sparse sources and many governing primes

Fix K>0 and 0<η<1. Suppose v≥M/(log M)^K and |S|≤exp((log M)^(1−η)). Then

    |F_I(1)−v|=o(v),
    Σ_{p^j≤M} [F_J(p^j)−F_I(p^j)]_+ = o(v).                       (1)

In particular every source set A contained in such a canonical profile set V has H(A,I)≤|V|+o(|V|). Thus half occupancy gives 2n+o(n) when n≥M/(log M)^K; full occupancy gives n+o(n). The conclusion extends to exceptions by adding Σ_{a∉V,a∈A}ω(a), once per missing atom rather than its exponent. This permits arbitrarily many progression generators on the given prime bases.

Put L=log M, h_0=exp(L^(1−η/2)), z=M/h_0. We use the project's [uniform valuation-profile comparison](../unrestricted_shifts_2026_11_26/SUBPOWER_PROFILES.md). On any quotient interval of length at least floor(h_0), the S-profile law differs in total variation from independent geometric exponents G_p (tails p^(−j)) by ε_M smaller than any fixed negative power of log M. Indeed the logarithm of the |S|-th prime is O(1+L^(1−η)), while the quotient log length is at least (1+o(1))L^(1−η/2). The estimate also applies to bounded functions v↦f(dv), since the valuations of d are fixed additions. Write θ=E f(G); in particular θ=v/M+O(ε_M).

For every d≤z, each quotient interval has floor(M/d) or ceil(M/d) points. Comparing its mean to the same model gives |F_I(d)−F_J(d)|≤2ε_M M/d+O(1). At d=1 this proves the first claim. Summation over prime powers d≤z gives o(v), using Σ_{p^j≤M}1/p^j=O(1+log log M) and z=o(v). For powers d>z of exponent at least two, the sum of the canonical counts, weighted or otherwise, is O(M log M/sqrt(z))=o(v). Indeed the count of such powers up to X is O(sqrt(X) log(2X)), and a dyadic reciprocal sum suffices.

For primes p>z it suffices to bound **the canonical f-mass** with such a factor, since z>sqrt(M). Primes p∈S cost ≤|S|h_0=o(v). Otherwise a=ph with h≤h_0 and f(a)=f(h); the prime-counting bound yields an upper bound O(M/log z)Σ_{h≤h_0}f(h)/h. The following relative estimate is essential:

    Σ_{h≤H}f(h)/h ≪ θ log(2H) whenever H≥max(2,|S|).             (2)

Write h=ur with u S-smooth and (r,∏S)=1, and V_S=∏_{p∈S}(1−1/p). Then Σ_{u S-smooth} f(u)/u=θ/V_S. Upper bound the reciprocal sum over coprime r≤H by ∏_{p≤H,p∉S}(1−1/p)^(−1). Dividing this product by V_S gives the full Mertens product through H times ∏_{p∈S,p>H}(1−1/p)^(−1), whose extra factor is O(1) because |S|≤H. This proves (2). Here h_0≥|S|, so the final contribution is O(M θ log(2h_0)/log z)=o(v). This proves (1), including the prime tail on quotient intervals too short for the profile comparison.

## Polynomially sparse sources, fewer governing primes

Let log v/log M→β for 1/2<β≤1 and s=|S|=o(log M/log log M). For Boolean f, every A contained in its canonical set of size v has

    H(A,I) ≤ [1+log(1/β)+o(1)]v.                                    (3)

For β=0.8 the coefficient is 1.22315 to five decimal places rounded upwards. This applies to a deterministic profile-defined family with no randomness assumption. Full occupancy and β→1 give v+o(v) even for densities below every fixed negative log power, under the smaller support condition.

Cap each S-valuation at e_p=floor(log_p M), extending f to targets with these clipped profiles. This preserves its canonical values. Finite differences on the product of the exponent chains express it as Σ c_d 1_{d|b}, including d=1, where W=Σ|c_d|≤∏_{p∈S}(1+2e_p)=M^o(1). Each coefficient has modulus ≤2 to the number of its positive coordinates; summing this bound gives the product. Every modulus and every intersection with an additional level differs in count between I and J by at most one, so |F_I(d)−F_J(d)|≤W at each d. Also |v−Mθ|≤W by comparison with independent geometric valuations.

Put z=v/[W(log M)^2] (use max(1,W) if necessary); eventually z>sqrt M and log z/log M→β. The total transfer error on p≤z and all their powers through M is O(W(z+sqrt M log M))=o(v). Select the clipped target predicate, costing at most v+W. It remains to bound the canonical count B of f-rows with a prime >z, costing at most one repair per such row. The primes from S contribute ≤sM/z=o(v), since β>1/2.

For the remaining primes write a=upb, with u its exact S-part, p>z outside S and b coprime to S. For fixed u let X=M/u. Uniformly in X≥z, the number of pairs (p,b) is at most

    V_S X [Σ_{z<p≤M}1/p + O((s+1)/log z)].

To see this, put T=4^(s+1). For p≤X/T, count coprime b≤X/p by inclusion-exclusion as V_S X/p+O(2^s). The count of such primes above z is O(X/(T log z)), or zero. Since V_S≥c/log(s+2) by Mertens applied to the first s primes, the errors total O(V_S X/log z). For p>X/T, sum first over b≤T coprime to S. For each eligible b with X/b≥z there are O(X/(b log z)) primes. The reciprocal sum of these b is O(V_S log(2T)) by the coprime product estimate in (2). This proves the pair bound, including X/T<z. Sum over u with weight f(u), use Σ f(u)/u=θ/V_S, and use the prime reciprocal sum Σ_{z<p≤M}1/p=log(log M/log z)+o(1). Thus B≤v[log(1/β)+o(1)], proving (3). This tail argument can also be used for fractional f.

The elementary prime-product and reciprocal-sum inputs are summarized in [Tao, Mertens' theorems](https://terrytao.wordpress.com/2013/12/11/mertens-theorems/).
