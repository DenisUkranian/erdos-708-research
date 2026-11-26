# The coefficient two for all fixed logarithmic shift exponents

Let A consist of n different integers in [2,M] with maximum M, L=lcm(A), and I={x+1,...,x+M} an interval of positive integers. H is the minimum size of a subset of I whose counts at every prime-power level dominate those of A.

**Theorem.** Fix C>0 and α≥0. If L divides N and |x−N|≤CM(log M)^α, then H(A,I)≤(2+o(1))n, uniformly for all remaining choices as n→∞. Every fixed logarithmic exponent is allowed. For the normalization C=1, the coefficient two is sharp by the classical centered construction.

The extension beyond the previous restriction α<13/34 uses a source-dependent cutoff chosen by averaging and a different normalization at both ends of the matching.

## Shifts and the sparsest ranges

Write ℓ=log M. For |x−N|≤2M the earlier centered theorem applies, so assume all the offsets b−N have the same strict sign. The positive integers |b−N| form an interval of length M with maximum O_C(M(1+ℓ^α)). A demanded prime power q divides N, hence q divides b exactly when it divides b−N. The reflected or translated interval therefore has the same level-cover problem. In particular the [bounded polynomial shift theorem of redlydi](https://github.com/redlydi/Erdos708-Research/blob/32f397f8f/reports/erdos708-density-and-shifts%282%29.md) applies for every fixed ε>0 when M≥n^(1+ε); its polynomial upper bound on the positive interval endpoint holds here, for example with K=2 for large M. We will use this for one specific small ε depending only on α.

## Selecting the cutoff and excluding rare rows

Fix a constant B>4(α+1) and set T=ℓ^(2B), λ=1/(16B). For y≥2 let s_y(m) denote the full y-smooth part of m. For U uniform on [1,M],

    E s_T(U)^λ ≤ ∏_{p≤T} (1−1/p)/(1−p^(λ−1)) ≤ exp(O_B(ℓ^(1/8))).

Expand nonnegative divisor coefficients p^(jλ)−p^((j−1)λ) and use floor(M/d)≤M/d. The logarithm is bounded by O_B(Σ_{m≤T}m^(λ−1)). Put R=log(M/n). Applying Jensen conditionally on A gives

    E_A log s_T(a) = O_B(R+ℓ^(1/8)).

Choose log Y uniformly on [B log ℓ,2B log ℓ]. For each prime p the event Y<p≤2Y has probability O_B(1/log ℓ). Every such p is ≤2T, and the same moment bound holds with 2T in place of T. Averaging selects a cutoff Y satisfying

    E_A Σ_{Y<p≤2Y, p|a} log p = O_B((R+ℓ^(1/8))/log ℓ).

Choose δ=λ/16. We may assume n≥M^(1−δ), since the remaining range satisfies M≥n^(1+ε) with fixed ε=δ/(1−δ). Discard rows a<sqrt(M) or s_Y(a)>M^(1/4). There are at most

    sqrt(M) + M^(1−λ/4) exp(O_B(ℓ^(1/8))) = o(n/ℓ^2)

such rows, by the square-root cutoff and Markov's inequality using the preceding moment. In each remaining row f(a)=log(a/s_Y(a))≥ℓ/4.

## A flow with the smooth part removed from its normalization

A retained row sends Λ(q)/f(a) to d=a/q for every prime power q=p^j dividing a with p>Y. Its total mass is one. In the target put t=|b−N| and f(t)=log(t/s_Y(t)). At columns d|t allow Λ(t/d)/f(t) when t/d is a power of a prime >Y; take zero otherwise, including f(t)=0. This charges at most one at each target, by the identity for f(t). Every source column divides N, so d|t implies d|b. A matching along these paths covers all but at most one full prime-power atom per matched row.

For a contributing column set d_0=d/s_Y(d), W=M/s_Y(d), and u=M/d=W/d_0. We have log W≥3ℓ/4. For every allowed source q, f(dq)=log(d_0 q). The total column demand is bounded by

    [ψ(u)−θ(Y)+O(u/log W)]/log W,   when u≥2Y.

Indeed the admissible von Mangoldt mass below u is at most ψ(u)−θ(Y). Replacing 1/log(d_0 q) by 1/log W incurs O(u/log² W): the part d_0 q<W^(1/4) contributes O(W^(1/4)/d_0) using Λ(q)≤log(d_0 q), and on the rest the positive correction is bounded using Σ_{q≤u}Λ(q)log(u/q)=O(u).

On every admissible target with t=dq', its denominator f(t)=log(t/s_Y(d)) is at most log W+O_{C,α}(1+log ℓ). Before normalizing, its column supply sums Λ(q') over the quotient interval of absolute offsets, with prime bases ≤Y removed. The quotient interval has length u (up to endpoint conventions) and maximum O(u(1+ℓ^α)). For u≥2Y we have ℓ^α≤u^(α/B). The prime number theorem in short intervals gives total mass u+O_{α,B}(u/log^4(2u)): the interval length exceeds the lower endpoint to a fixed exponent greater than 17/30, or the ordinary prime number theorem handles endpoints smaller than the length. The [Guth–Maynard estimate](https://arxiv.org/abs/2405.20552) and the long-interval subdivision in the earlier centered proof suffice. From this total remove at most θ(Y) first powers; the combined mass of all higher powers up to Z=O(u(1+ℓ^α)) is O(sqrt(Z) log²(2Z))=O_B(u/log^4(2u)). Thus target supply is at least

    [u−θ(Y)−O_B(u/log^4(2u))]/[log W+O(1+log ℓ)].

For u≥2Y, u−θ(Y)≥u/3 for large M. Using ψ(u)=u+O(u/log^4(2u)), the relative source loss of the column is bounded by O(1/log^4(2u)+(1+log ℓ)/ℓ). Shrink each input proportionally to fit the column supply, then use integrality of bipartite matching. For u<2Y every surviving source q≤u must be a first power Y<p<2Y. Charge the whole mass of these inputs as lost.

## Repairing the unmatched rows

Put F(a)=Σ_{p^j|a} Λ(p^j)/log^4(2p^j). The number m left unmatched, including previously discarded rows, is bounded by

    m/n ≤ o(ℓ^(−2)) + O((1+log ℓ)/ℓ)
          + O_B((R+ℓ^(1/8))/(ℓ log ℓ)) + O_B(E_A F/ℓ).

Indeed q≤u in every source input, every retained row has f(a)≥ℓ/4, and the boundary band in this estimate is exactly the averaged sum above. For every fixed η>0 the mean of exp(ηF(U)) is bounded by a constant depending on η, via F(a)≤Σ_{p|a}O((log p)^−3) and its convergent Euler product. Hence E_A F=O(1) for bounded R and E_A F=o(R) if R→∞ by Jensen with η arbitrarily large.

For R≤sqrt(ℓ), writing z=m/n, the last bound gives z(R+log ℓ)=o(1), uniformly by the sequence criterion. The 2^ω divisor bound on [1,M] therefore gives Σ_{a unmatched}ω(a)≤m(log(M/m)+log(1+ℓ))/log 2=o(n); the term z log(1/z) tends to zero. Cover those rows by singleton atoms. For R>sqrt(ℓ), we have zℓ/R=o(1). In each unmatched row defer full prime-power atoms exceeding V=M/(3n) as singletons, and greedily pack the rest into blocks of product ≤V. Each adjacent pair of finished blocks has product >V, so all deferred atoms and blocks together number O(m(1+ℓ/log V))=o(n). Fresh multiples for small blocks exist since floor(M/V)≥3n. Nested level repair supplies the deferred atoms and the at most one missing atom per matched row. This proves H≤2n+o(n) for the remaining ranges.

See the [previous cofactor proof](../cofactor_flow_2026_11_26/README.md) for the level-repair argument, the short-interval prime estimate, and the sharp lower construction.

## Longer displacements at fixed positive density

**Corollary for product divisibility.** Suppose n/M≥δ>0 and |x−N|≤M S for some N divisible by L and S=M^o(1), S≥1. Then τ(A,I)≤2n+o(n), where τ is the ordinary product-divisibility optimum. This includes superpolylogarithmic multipliers S. The stability step below is for τ.

Use the original weights Λ(q)/log a and Λ(|b−N|/d)/log((S+2)M) and set Y=max(ℓ^(1/4),(S+2)^2). For u≥Y the quotient interval has length u, lower endpoint at most O(u^(3/2)), so the short-interval prime estimate applies with a fixed margin in its exponent. If the interval straddles zero the ordinary prefix estimates suffice. These columns lose proportion o(1), uniformly, since log(S+2)=o(ℓ) and Y tends to infinity. The remaining columns have only incoming q≤Y. After temporarily omitting a<sqrt(M), the average of the lost mass on all rows is at most O_δ(ℓ^(−1) Σ_{q≤Y}Λ(q)/q)=O_δ(log(2Y)/ℓ)=o(1), by summing floor(M/q) and using partial summation of the Chebyshev estimate. Consequently a matching leaves m=o(M) rows and the matched subfamily has H≤2(n−m).

For n>M/2 take the full interval. For n≤M/2 use [redlydi's source-removal inequality, §2](https://github.com/redlydi/Erdos708-Research/blob/32f397f8f/reports/erdos708-residue-certificates.md): the ordinary covering LP cost for A exceeds the cost of the matched subfamily by at most O(m log(eM/m))=o(M). Rounding costs at most π(M)=o(M) additional positions. Since M=O_δ(n), this proves the corollary.
