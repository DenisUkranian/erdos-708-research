# An upper bound for arbitrary prices after removing a diffuse part

Let `J=[1,M]`, let I be any positive interval of M consecutive integers, let A be a subset of J, and write n=|A|. Let w_p (0≤w_p≤1) be the dual prices in the product-cover relaxation, with load X(v)=Σ_{p≤M} w_p v_p(v) and objective

    Φ = Σ_{a∈A} X(a) − Σ_{b∈I} (X(b)−1)_+.

Set Y=floor(sqrt(log M)). All prices for p≤Y are unrestricted. Partition primes Y<p≤M arbitrarily into D and Q. On D suppose w_p≤ε_M with ε_M→0; on Q allow arbitrary prices. Put

    e(a) = [ Σ_{p∈Q, p|a} w_p − max_{p∈Q, p|a} w_p − 1 ]_+,

where the empty maximum is zero. Then, uniformly over shifts, sets and prices with this diffuseness condition,

    Φ ≤ 2n + Σ_{a∈A} e(a) + o(M).

For example all prices above M^(1/3) are allowed, and e vanishes if Q consists only of such primes. The bound concerns values of the dual at specified prices. It gives a bound on the covering optimum when the hypotheses cover an optimal dual, with the usual additional π(M) positions for vertex rounding. The error o(M) is useful at positive density; it is not a uniform relative sparse estimate.

## Reduction to bounded loads

Truncate prime exponents at K_p=floor(log_p M) everywhere and denote the resulting load by X'. This does not alter any source load, and only decreases the target hinge, so that upper bounding the truncated objective suffices. Moreover Σ_I X'≥Σ_J X' by counting each level of each prime. Consequently the objective is at most

    Σ_{b∈I} min(X'(b),1) − Σ_{j∈J outside A} X'(j).

On primes above Y, retaining just distinct divisibility indicators instead of all capped levels changes X' by o(M) in total, on both intervals: the normalized loss is bounded by Σ_{p>Y} 1/[p(p−1)] + O(sqrt(M) log M/M), since the number of powers p^j≤M with j≥2 is O(sqrt(M) log M).

At p≤Y, truncate further at floor(log_p Y), obtaining a small load s_0 with period P=lcm(1,...,Y)≤Y^Y=M^o(1). The total omitted load, normalized by M, is o(1). Indeed the sum of reciprocal higher powers is at most 2Σ_{p≤Y} p^{−1−floor(log_p Y)}=O(Y^(−1/2)), by splitting above and below sqrt(Y). The normalized floor errors are O(Y log M/M).

## Diffuse primes

Write μ=Σ_{p∈D}w_p/p. If μ is bounded, the distinct diffuse load Z has mean absolute deviation from μ of size o(1) on either interval. The contribution of p>M^(1/5) to its mean in either interval and to μ is O(ε_M), by the reciprocal-prime estimate and π(M)/M≤1. For p≤M^(1/5), the first and pair divisibility counts differ from the independent Bernoulli moments (parameters 1/p) by at most 1/M per moment. The aggregated errors are O(M^(−3/5)) in the raw second moment and O(M^(−4/5)) in the first. Thus the expected squared deviation of this part from its reciprocal mean is O(ε_M μ)+o(1). Cauchy–Schwarz proves the assertion. All these comparisons are unconditional, so replacing Z by μ inside a Lipschitz cap is valid even if the other prices correlate with Z.

If μ≥3, select a diffuse subset with reciprocal mean in [2,2+ε_M] by accumulating terms until it reaches 2. The preceding bounded-mean proof applied to this subset shows Σ_J (2−X')_+=o(M). The target cap is ≤1, while the canonical mean of min(X',2) is ≥2−o(1), so the target cap sum is at most Σ_J min(X',2)+o(M). Subtracting Σ_{J outside A} X' yields Φ≤2n+o(M). We can therefore use the bounded-mean case μ<3 below.

## Transfer of the cap

Write s=s_0+μ, h=(1−s)_+ and U=Σ_{p∈Q, p|v} w_p. The preceding estimates compare X' to s+U with total absolute error o(M) on both intervals. Pointwise subadditivity of a cap gives the envelope

    min(s+U,1) ≤ F(v) := min(s,1) + Σ_{p∈Q, p|v} min(w_p,h(v)) ≤ s+U.

Its sums over I and J differ by o(M). The base term is bounded and P-periodic. For each p∈Q the coefficient is also bounded and P-periodic, coprime to p in the sense that p does not divide P. On the multiples of p it has full-period mean equal to its ordinary period mean. For p≤M^(1−η) with fixed η>0 the total discrepancy is O((P+1) M^(1−η))=o(M). For larger primes the normalized sums on both intervals are bounded by Σ_{M^(1−η)<p≤M} (1/p+1/M) ≤ −log(1−η)+o(1). Let η decrease to zero.

If s≥1 then F=1. Otherwise list the Q-prices present at v in descending order, with largest w_*. The term min(w_*,h) is at most h and the others sum to at most U−w_*. Thus F≤1+U−w_* and F≤2+e(v), also for an empty list. We conclude

    Φ ≤ Σ_J F − Σ_{J outside A} X' + o(M) ≤ Σ_A F + o(M)
      ≤ 2n + Σ_A e(a) + o(M).

A source has at most two distinct prime divisors above M^(1/3), so if Q is supported there, its total price after its largest price is removed is at most one.

The diffuse reduction also extends the previously proved binary comparison. If the Q-prices are all binary, add the common constant μ to the core load s in the small-core proof of MIXED_BINARY_PRICES.md. The proof there uses only nonnegativity and periodicity of the core, boundedness of its capped functions and their period. The same normalized o(M) estimate for the dual follows, with no restriction on the number of Q-primes in a source.
