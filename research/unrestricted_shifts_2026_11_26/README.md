# One set of shifts that works for every dense source family

For each integer M let P=lcm(1,...,M), x be uniform modulo P and I consist of x+1,...,x+M, using a nonnegative representative. For A⊆[2,M], let H(A,I) be the minimum number of target positions whose counts of multiples dominate those of A at every prime-power level. This suffices for divisibility of the two products. The o(1) exceptional proportion below refers to a complete period of shifts.

**Theorem.** Write B(M)=M(log log M)²/log M for M sufficiently large. There is a nonnegative random variable W_M(x) with E W_M ≪ B(M) such that, simultaneously for every A⊆[2,M],

    H(A,I) ≤ 2|A| + W_M(x).

In particular for every sequence n₀(M)/B(M)→∞, outside a proportion o(1) of shifts every A of size n≥n₀(M) has H(A,I)≤(2+o(1))n, with a common relative error tending to zero. Any fixed positive density is covered, as are the densities tending to zero in this range. This conclusion allows the source set to be chosen *after* the shift is observed.

## A harmonic divisor of the full-period model

Put h=Σ_{d≤M}1/d and μ_d=1/(dh). For a uniform residue b modulo P record Z=gcd(b,P). There is a stochastic kernel K_d(b) which depends only on Z, is supported on d|b, satisfies Σ_d K_d(b)=1 and has full-period mean μ_d for 1≤d≤M.

Indeed, introduce independent geometric prime exponents with tail Pr(G_p≥j)=p^(−j) for p≤M, and let V=∏p^(G_p). The conditional law of V given V≤M is μ. The coordinatewise capped product gcd(V,P) has the law of Z by the Chinese remainder theorem. For any set S of possible d, the event that some d in S divides V is increasing, while V≤M is decreasing. Harris's inequality for independent coordinates gives μ(S)≤Pr(some d in S divides V). This last probability is unchanged on capping, because each d divides P. These are exactly the finite weighted Hall inequalities for a coupling supported on d|Z (equivalently, apply the max-flow min-cut theorem). Condition its joint law on Z to get the kernel. Neither S nor the later shift enters the choice of kernel.

## Uniform-interval variance for a function of the gcd

Suppose f on residues mod Q is invariant under multiplication by units, t is uniform mod Q and J≥1 is an integer. Then

    Var[(1/J) Σ_{i=1}^J f(t+i)] ≤ (Q/φ(Q)) Var(f)/J.

For Q=1 this is immediate. Otherwise take the normalized discrete Fourier transform and use Parseval. Invariance makes its coefficients constant on the primitive frequencies of each conductor s|Q. For s>1, average the squared multiplier |Σ_{i=1}^J exp(2πiai/s)|²/J² over reduced a modulo s. Complete periods sum to zero. The sum of the unnormalized squared residual multiplier over *all* a modulo s equals s(J mod s) by orthogonality. Dividing by φ(s)J² gives at most s/(φ(s)J)≤Q/(φ(Q)J). Sum the nonconstant Fourier shells to get the assertion. Standard background on these gcd-invariant Fourier expansions is provided by [Tóth and Haukkanen](https://www.kurims.kyoto-u.ac.jp/EMIS/journals/AUSM/C3-1/math31-1.pdf).

## One bound for all adaptive cuts

Let w_d=M^(−1)Σ_{b∈I} K_d(b) and Δ=Σ_{d≤M}(μ_d−w_d)_+. For every T⊆I the empirical w-mass of those d for which all their multiples in I belong to T is at most |T|/M. This follows by summing the kernel at the points of T. Consequently the harmonic cut excess e(M,I) of the [one-deletion reduction](../cofactor_flow_2026_11_26/HARMONIC_REDUCTION.md) is bounded by Δ, even when T depends on x.

Fix d. Conditional on x mod d the quotient positions b/d for multiples of d in I form J consecutive integers with uniform starting residue modulo Q=P/d, and |J−M/d|≤1. The function f(j)=K_d(dj) is gcd-invariant modulo Q since gcd(dj,P)=d gcd(j,Q). Its mean is dμ_d=1/h and its variance is at most 1/h. The variance lemma, Q/φ(Q)≤P/φ(P)≪log M by Mertens' theorem, and J≤2M/d give

    E|w_d−μ_d| ≤ 1/(Mh) + O(1/sqrt(Md)).

For d≤M/(log M)^4 sum this bound. For the other d use (μ_d−w_d)_+≤μ_d. This proves

    E Δ ≪ log log M / log M.

The [deletion law and Hall bound](../cofactor_flow_2026_11_26/HARMONIC_REDUCTION.md) yield a maximum deficiency m for the entire canonical family [2,M] with m≤MΔ+O(M/log M). A matching of the whole family restricted to A leaves at most m of its rows unmatched. Each matched row costs at most two positions, by crediting the shared prime powers and repairing the omitted atom. The extra cost of the unmatched rows is at most their total number of distinct prime factors, using the same nested repair across all rows. For any set of at most m rows Jensen's inequality and Σ_{a≤M}2^ω(a)≤M(1+log M) bound that extra cost by

    F(m)=m log(M(1+log M)/m)/log 2,

with F(0)=0. This function is increasing on [0,M] for large M and concave, so E F(m)≤F(E m)≪B(M). Take W_M=F(m). For the simultaneous relative conclusion use Markov at sqrt(n₀ B(M)); both the exceptional proportion and the relative error are O(sqrt(B(M)/n₀)). A full-period mean gives no bound on the single worst shift. Closing this last quantifier is still necessary for the original g(n).

The [exact small-period replay](verify_period.py) constructs the rational kernel by integer max-flow and checks the cut inequality for every subset and every shift for 2≤M≤8.

## Deterministic results and auxiliary estimates

* [All fixed logarithmic shift exponents](ALL_LOG_POWERS.md) gives the sharp coefficient two at every source density when the distance from x to a multiple of lcm(A) is at most M times any fixed power of log M. At fixed positive density the distance can be M^(1+o(1)).
* [Rational centers](RATIONAL_CENTERS.md) removes the coprimality requirement for fixed denominator and error O(M).
* [Local blocking primes](LOCAL_BLOCKERS.md) gives an exact 2n−1 bound for specific source families at **every** shift. An [arithmetic replay](verify_blockers.py) checks the construction on finite instances.
* [Square-root cofactors](SQUARE_ROOT_COFACTORS.md) treats other arbitrary-shift families, including an unrestricted small-prime part and at most two additional distinct prime factors per row.
* [Subpower smooth profiles](SUBPOWER_PROFILES.md), [fractional prices](FRACTIONAL_PRICES.md), [active support](ACTIVE_SUPPORT.md) and [macroscopic prices](MACROSCOPIC_PRICES.md) give auxiliary transfer estimates and explicit hypotheses for their application. A restriction on a dual price vector is not by itself an unconditional covering theorem.

These are written arguments. The general asymptotic and the exact conjecture remain open in this work.
