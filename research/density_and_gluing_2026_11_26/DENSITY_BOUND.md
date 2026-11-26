# An explicit unconditional bound throughout densities above one sixth

Suppose A⊂[1,M] has n points, and I is a length-M interval of positive integers. Write H(A,I) for the minimum size of a subset of I meeting every source prime-power-level count. The ordinary product covering number is at most H. For M/6≤n≤M/2,

    H(A,I) ≤ 3n/2 + M/4 + O(M/log M).

In particular limsup H/n≤9/4 at n/M→1/3 and ≤5/2 at n/M→1/4. At densities tending to 1/6, the earlier universal 3 upper bound agrees. The argument does not establish coefficient 2 at those example densities.

Let r be the number of powers h=p^j≤M, so r=O(M/log M). Use the fractional covering LP on ALL levels, with one common slack s_p for the levels of a prime, as in the all-scales note. Rounding at most r fractional sites, then adding highest available p-valuations to repair the remaining maximal deficit, shows that H≤r+Φ. Duality supplies nonnegative weights w_h with Σ_{h power of p}w_h≤1 and

    Φ=Σ_{a∈A}X(a)−Σ_{b∈I}(X(b)−1)_+,
    X_p(b)=Σ_{j:p^j|b} w_{p^j}, X=Σ_p X_p.

Each X_p is in [0,1]. Let μ=Σ_h w_h/h, u=E_A X, and v=M/n≥2. Consecutive interval counting gives Σ_I X≥Mμ−r. By convexity and nonnegativity, the subtracted penalty is ≥M(μ−1)_+−r. Thus H/n≤u−v(μ−1)_++2r/n.

Let B(x) be the convex polygon through (j,j(j−1)/2) at integers j≥0. At a fixed row, among [0,1] per-base weights with prescribed sum X, the distinct-base pair sum is minimized by packing unit weights and one fractional remainder: replacing two fractional entries by a pair with identical sum and one endpoint increases their sum of squares. So Σ_{p<q}X_p X_q≥B(X). On the canonical interval J all mixed prime-power levels at distinct bases are coprime, whence

    E_A B(X) ≤ (1/n)Σ_{J}Σ_{p<q}X_p X_q ≤ v μ²/2.

Jensen gives B(u)≤vμ²/2. Write g(y)=max{x:B(x)≤y}; g is piecewise linear on [0,∞), with g(0)=1 and slope 1/k when k≤g(y)≤k+1, k≥1. Therefore

    H/n ≤ g(vμ²/2)−v(μ−1)_++2r/n ≤ g(v/2)+2r/n.

For μ≤1 the second inequality is monotonicity. For μ≥1, B(ceil μ)≤μ(μ+1)/2≤μ²≤vμ²/2, so floor(g(vμ²/2))≥ceil μ. On each open affine piece of g the derivative of the penalized bound is vμ/k−v≤0. Continuity settles all breakpoints. Finally g(v/2)=(v/2+3)/2 when 2≤v≤6. This proves the displayed theorem, with absolute O-error and uniform shifts. More generally the inverse g bound holds at every n≤M/2, with explicit error 2r.

A still shorter proof avoiding all order calculus on M/6≤n≤M/2 is possible by using the same piecewise-binomial inequality and checking the one-variable piecewise quadratic maximum. The provided monotonicity calculation also certifies all lower densities, even though their prior global bound is stronger.
