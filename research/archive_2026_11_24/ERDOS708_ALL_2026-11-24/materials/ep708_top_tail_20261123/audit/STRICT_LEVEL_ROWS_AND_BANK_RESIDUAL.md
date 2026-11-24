# Strict source levels, exact active rows, and the bank residual

## Status and scope

This is a proof audit for the unrestricted top-tail problem. It proves an exact normalization and identifies the sign and meaning of the remaining bank term. It does **not** obtain a new quantitative bound for that term, prove J_weak, or prove the unrestricted asymptotic coefficient two. No values of g(n), finite optimizations, or numerical probes are computed here.

All intervals below are actual positive integer intervals

    I={x+1,...,x+M},  x>=0.

For a nonempty set A of distinct integers in [2,M], let F(A) be the boxed raw covering LP, with constraints

    sum_{b in I} z_b v_p(b) >= D_p(A),  0<=z_b<=1,

and write

    X(n)=sum_p w_p v_p(n),
    Phi_A(w)=sum_{a in A}X(a)-sum_{b in I}(X(b)-1)_+.

Target valuations are never truncated at the source exponent range. An optimal raw dual may be chosen with 0<=w_p<=1 and supported on source primes.

## 1. A maximum-ratio obstruction is a strict source superlevel set

Fix M and I and define

    R=max_{nonempty B subset [2,M]} F(B)/|B|.

The maximum exists because the ambient set is finite. Suppose R>1. Among all maximizers choose A with minimum cardinality m, and let w be any optimal clipped dual for A. Then

    A={a in [2,M]: X(a)>R}.                              (1)

First, m>=2: any single source a<=M is covered by one multiple of a in I, so F({a})<=1.

For a in A, deleting it gives

    F(A\{a}) >= Rm-X(a).

If X(a)<R, the smaller set would have ratio greater than R. If X(a)=R, its ratio would be exactly R, contradicting the choice of m. Hence every selected source has X(a)>R.

If a missing integer b has X(b)>R, adding b gives

    F(A union {b}) >= Rm+X(b)>R(m+1),

again a contradiction. This proves (1). In particular source ties at R disappear, and A is upward closed under divisibility.

The exact equality at the maximizing vector is

    sum_{a<=M}(X(a)-R)_+
       =sum_{b in I}(X(b)-1)_+.                         (2)

Indeed the left side is sum_A X-Rm, and optimality makes this the target hinge. Equation (2) is a normalization of a putative obstruction, not an upper bound for R.

### Relation to the forced-maximum top-tail expression

The normalization in (1) permits max A<M. This does not silently remove the forced-maximum condition in the user's expression. If M is absent, adding it costs one source and does not decrease F. Consequently an asymptotic coefficient-two upper bound for forced-maximum sets also bounds these unanchored sets, with an additive cost of two and the same asymptotic error.

For a hypothetical sequence R>=2+epsilon, the full interval is a feasible cover, so

    M>=F(A)>= (2+epsilon)m.

The ambient Wang quadratic gate also gives M<16m^2. Thus m tends to infinity with M; adding M preserves 2(m+1)<M<16(m+1)^2 for all sufficiently large members of the sequence. This is a justified reduction of the asymptotic problem, not a claim about a fixed finite n.

## 2. Exact threshold-row equations

Let z be an optimal primal paired with w. For every active prime p, complementary slackness gives

    D_p(A)=sum_{b in I}z_b v_p(b).                        (3)

The strict-level normalization expands the source side exactly as

    D_p(A)=sum_{j>=1}
      #{k<=floor(M/p^j): X(k)>R-jw_p}.                  (4)

This is a valuation-layer identity: each source divisible by p^j contributes once at layer j. It remains valid when k itself is divisible by p.

For the target side put

    J_j={floor(x/p^j)+1,...,floor((x+M)/p^j)}.

Writing z_b=1 for X(b)>1, z_b=0 for X(b)<1, and retaining the actual chosen z_b on X(b)=1, equation (3) becomes

    sum_{j>=1} #{k<=floor(M/p^j): X(k)>R-jw_p}
      = sum_{j>=1} [
          #{k in J_j: X(k)>1-jw_p}
          +sum_{k in J_j, X(k)=1-jw_p}z_{p^j k}
        ].                                               (5)

The source sum stops once p^j>M. The target sum must continue through all powers present in I, potentially far beyond that point. Replacing its range by the source range is unjustified.

The system (5) is stronger data than a cardinality-only bank count. The audit did not derive a new uniform inequality from it. Treating it as a proof that R<=2 would merely assume the missing arithmetic comparison between its two threshold systems.

## 3. The residual has an exact nonnegative meaning

Let H={b in I:X(b)>1}. Take any U subset H; in particular, U may be the union of all proper-prime-deletion banks

    U=union_{a in A, q prime dividing a}
          {b in I: a/q divides b}.

When (1) holds and R>2, every such bank lies in H because

    X(a/q)=X(a)-w_q>R-1>1.

In fact there is the stronger containment

    U subset {b in I:X(b)>R-1}.                         (6)

For an active p, write V_p(U)=sum_{b in U}v_p(b). Since z_b=1 on U, equation (3) gives

    D_p(A)-V_p(U)=sum_{b in I\U}z_bv_p(b)>=0.           (7)

Consequently the signed-looking remainder in the bank decomposition is exactly

    sum_p w_p(D_p(A)-V_p(U))
       -sum_{b in I\U}(X(b)-1)_+
      =sum_{b in I\U}z_b.                              (8)

To verify (8), use (7) and observe that for every target outside U,

    z_b X(b)-(X(b)-1)_+ = z_b.

This holds separately for hot targets (z_b=1), threshold-one targets, and cold targets (z_b=0). Hence

    Phi_A(w)=|U|+sum_{b in I\U}z_b=F(A).                (9)

Thus active-row balance does not make the residual negative or negligible. It identifies the residual as the remaining selected primal mass. At the maximum-ratio normalization this mass is precisely Rm-|U|.

Containment (6) explains one obstruction to a shortcut: selected targets of load between one and R-1 necessarily lie outside this particular bank union. Neither strict top-source selection nor equation (5) has yet bounded their mass, or the mass of other selected targets outside U, by the required residual budget.

For the full optimal source set, the active-row positive-oversupply metric

    sum_p w_p(V_p(U)-D_p(A))_+

is exactly zero by (7). A construction with a strict oversupply in any positive-price row therefore cannot be an example satisfying these optimality equations. Conversely a one-row deficit or coordinatewise failure of bank-product domination is not by itself an obstruction to the desired weighted estimate.

## 4. A sanity check for isolated log-cap loss

This section records a limitation already recognized in the task; it is not the proposed solution route.

Let M=3^k, n=M/3, I=[1,M], w_3=1, all other prices zero, and

    A={3,6,...,M},   z=1_A.

A realizes the forced-M top-n source sum at w. It is a paired optimum with F=n. Moreover this is a global optimum over all n-element source sets and all dual vectors: every source set in the prefix covers itself at cost n.

For fixed delta>0 and k>2+delta, set

    gamma=(2+delta)/k,   u_3=gamma.

This is exactly the logarithmic cap u_p=min(w_p,(2+delta)log p/log M). Its value is

    Phi_A(u)=sum_{j=1}^{k-1}2*3^{k-j-1}min(gamma*j,1)
               +min(gamma*k,1)
             <=gamma*(M-1)/2=O_delta(n/k).

Consequently

    E=F-Phi_A(u)=n-O_delta(n/k),
    S=(2+delta)n-Phi_A(u)=(1+delta)n+E,
    E-S=-(1+delta)n.

The source set is top-selected, the active rows are exact, M is forced, and 2n<M<16n^2. The example therefore rules out an isolated o(n) loss assertion even with these conditions. It does not challenge any valid joint estimate involving S, and its source loads do not satisfy a high-load minimal-obstruction hypothesis.

## 5. Audit conclusion

The strict-superlevel normalization is valid and removes source-tie bookkeeping. The full target-power threshold equations are exact. The bank residual has the explicit nonnegative form (8). These statements clarify the remaining obligation but do not close it: a quantitative estimate for the joint target mass is still required.

No counterexample to the requested asymptotic bound or J_weak was found or claimed. No evidence from finite probes is used as a general theorem.
