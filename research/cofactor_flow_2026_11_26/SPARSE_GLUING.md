# Shift-uniform clipping and gluing

Let a source set of distinct positive integers be bounded by L and consider any L consecutive positive target integers. Only primes p ≤ L can be required. Put e_p = floor(log_p L).

**Finite valuation model.** Every result uniform in the shift, for ordinary product covers or level-by-level covers, can be applied with the credit of each target position at prime p truncated to e_p+1. Write the interval x+1,...,x+L. For each p prescribe a surrogate shift equal to x modulo p^(e_p+1). At most one of the offsets is divisible by this modulus, which exceeds L. Choose a lift modulo p^(e_p+2) that avoids divisibility by p^(e_p+2) at this offset. CRT combines all lifts. At every offset the surrogate valuation is exactly min(v_p(x+i),e_p+1), proving the assertion.

**Loss on an arbitrary small set.** For a set E of positions with |E| ≤ L^(1/2+o(1)) as L tends to infinity,

    sum_{i in E} sum_{p≤L} min(v_p(x+i),e_p+1) = o(L)

uniformly in x and E. For p ≤ L^(1/4) the bound |E| L^(1/4)(1+log_2 L) suffices. Fix 0<eta<1/4. For L^(1/4)<p≤L^(1−eta) there are O(L^(1−eta)) capped levels. Denote by c_q the count of E at level q. Summing binom(c_q,2) counts pairs at a common level. All such p^j divide the nonzero difference of the two offsets, of size at most L. Each pair contributes at most four levels since p>L^(1/4). Thus for N levels the sum of c_q is O(N+|E|sqrt(N)), by Cauchy–Schwarz. It is o(L). For the remaining primes the whole interval has at most L/p+1 first-level hits and one possible second-level hit per prime. Their contribution is bounded by L log(1/(1−eta))+o(L), using the prime reciprocal estimate and pi(L)=o(L). Let eta decrease to zero.

This bounds a deficit in prime units after removing selected positions. Restoring a unit by another point is possible in the original interval when its valuation constraint is deficient. The lemma does not promise that a new cover can avoid E entirely.

**Gluing local product covers.** Partition A into a fixed number of groups A_i, all divisible by d_i within group i. Set L_i=floor(M/d_i), and assume L_i=O(n). Suppose that quotient inputs A_i/d_i have shift-uniform product covers of size 2 n_i+o(n) on L_i consecutive positive integers (a source 1 may be omitted). The following intersection hypothesis suffices for a global 2n+o(n) cover:

    (1 + M/lcm(d_i,d_j)) (log M)^2 = o(n)   for every i≠j,

where M is polynomially bounded in n. For each i use L_i consecutive d_i-multiples from I, divide by d_i, and apply the capped model to their quotients. Pad to n_i if necessary; this is possible because n_i≤L_i. Enlarge the chosen set back to the d_i-multiples. Its credited valuation per position b and prime p may be taken as

    w_i(b,p)=v_p(d_i) + 1_{p≤L_i} min(v_p(b/d_i),1+floor(log_p L_i)).

It is bounded by the actual valuation and summed over the group covers the full group demand. On union, summing these credits may duplicate valuations. At a selected b the duplicate credit for p is at most sum_{i<j} min(w_i(b,p),w_j(b,p)) over local groups that chose b: order their credits, and compare their sum to the largest. Bound this sum by counting all positions common to the two arithmetic banks. Write D=lcm(d_i,d_j), K=M/D, X=min(L_i,L_j). For p not dividing D, simultaneous positive credit requires p≤X. For level j the number of bank intersections divisible by p^j is ≤K/p^j+1. The resulting sum is O(K log log(3X) + pi(X) + sqrt(X) log(2X)) since for each p there are at most 1+floor(log_p X) levels. For primes dividing D a per-position bound O((log M)^2) suffices, as the core and capped quotient exponents are O(log M), and omega(D)=O(log M). There are ≤K+1 such positions. The total is o(n) per pair; the finitely many pairs preserve this. Add one target position per residual prime-valuation unit if needed. Whole-interval supply for each prime is at least source demand, so the repair succeeds. Summing the finite local budgets proves the result. The same argument with the explicit sum over all pairs remains valid for a growing number of groups if that sum and the aggregate local errors are o(n).

For example, for n^(1+c)≤M≤n^C and a bounded number of pairwise coprime d_i of order M/n, the overlap hypothesis is automatic. If n_i/L_i≥0.3960 and the local sizes grow, the project's written density theorem supplies the local covers: if max(A_i/d_i)<L_i, the same density inequality holds with its own maximum, so take a subinterval; the surrogate remains valid on L_i. This produces arbitrary-shift families of vanishing global density. It is a gluing criterion and does not prove that every sparse source can be decomposed in this way.
