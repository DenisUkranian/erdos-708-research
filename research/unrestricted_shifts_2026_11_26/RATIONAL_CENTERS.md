# Fixed rational centers with arbitrary common prime factors

Let A be a set of n distinct integers in [2,M] with maximum M. Let I consist of x+1,...,x+M, all positive. Write H(A,I) for the minimum number of distinct target positions whose multiple counts at every prime-power level dominate those of A.

**Theorem.** Fix an integer k ≥ 1 and C > 0. Suppose N is divisible by lcm(A) and |kx−N| ≤ CM. Then H(A,I) ≤ (2+o(1))n uniformly in A,x,N as n grows. N and k may have any common divisor.

For example, the case of even source lcm L and N=L puts the interval start near L/2. The written exact 2n−1 result for coprime centers uses a strict surplus; the theorem here requires no surplus.

## Separating the primes in k

Let P be the primes dividing k, let r be their product (r=1 for k=1), and set ρ=φ(r)/r. Write h(a) for the full P-part of a. Within a bank h write a=h s; target positions in this bank have the form b=h z with (z,r)=1. Thus different banks have disjoint targets. Write X=M/h and B=(C+k+2)X. Ignore temporarily s < sqrt(n). For every prime power q dividing s, send source mass Λ(q)/log s to d=s/q. Its total is one. For this bank (d,r)=1, hd divides N, and u=X/d. The total input of a column d is at most

    [ψ(u)+O(u/log X)]/log X.

This follows by summing Λ(q)/log(dq) over all q ≤ u with dq≥2, as in the original cofactor proof (split dq<X^(1/4), then integrate the Chebyshev bound). For every column used here X≥sqrt(n).

For a target b=h z in the bank, form t by removing all P-factors from |k z−N/h|. Ignore k z=N/h. A column with d|z may send Λ(t/d)/log B to b; it is zero unless d|t. In fact d|z implies d|t, because hd|N and d is coprime to every p in P. Since t≤B, the identity Σ_{d|t}Λ(t/d)=log t bounds total capacity at this target by one. These edges match a row h s to a multiple of h d, hence pay all full prime-power atoms of a except possibly the one based at the prime underlying q.

## Estimating column capacity

Set m=N/(hd), and enumerate z=d w with (w,r)=1 and x/(hd)<w≤(x+M)/(hd). This real interval has length u and all its points satisfy |kw−m|≤(C+k)u. Apart from a possible zero, uniquely write |kw−m|=v y where v is P-smooth and (y,r)=1. Then t/d=y. We claim that

    Σ_w Λ(y) = u + O_{k,C,D}(u/log^D(2u))   for u≥2

for every fixed D>0, where the sum includes only the above integer units w, away from the zero. Here and below bounded u is covered by increasing the implied constant.

First restrict to v≤sqrt(u). For a given v and sign ε=±1, y ranges over a positive interval with endpoints at most (C+k)u/v and belongs to a union of reduced classes modulo K=k r. Precisely, (y,r)=1 and v ε y+m ≡ k j mod K for some unit j mod r. These conditions recover integer w=(v ε y+m)/k with (w,r)=1. The allowed interval on y imposes exactly the original bounds on w. For each reduced class the fixed-modulus prime number theorem, subtracted at the two endpoints, replaces Σ Λ(y) by ρ^(-1) times the number of integers y in this class, with absolute error

    O_{k,C,E}((u/v)/log^E(2u/v)).

This follows by applying the PNT up to (C+k)u/v with its classical log-power remainder (for endpoints below its square root the trivial bound suffices). The conversion between length and integer counts costs O(1). There are O_k(1) classes and signs for each v, and Σ_{v P-smooth}1/v=1/ρ. Since u/v≥sqrt(u), the combined error is O_{k,C,E}(u/log^E(2u)).

To bound the discarded terms when P is nonempty, if v>sqrt(u), then p^j | kw−m for some p∈P and j=ceil(log u/(2|P| log p)). The congruence has at most gcd(k,p^j)(u/p^j+1) solutions in the w interval, which is O_k(u^(1−1/(2|P|))+1). Each contributes O_{k,C}(log(2u)) even with the Λ weight. For P empty there is no tail. The count of all unit w is ρu+O_k(1); this proves the claim.

## Counting unmatched rows

When M≥(2n)^3 the shift-uniform two-block argument of the original proof already gives H≤2n. Otherwise log M and log n are comparable. The temporary exclusion s<sqrt(n) omits at most sqrt(n)(1+log_2 M)^|P| rows, by counting h, which is o(n/log^2 M).

For the other rows, choose Y=(log M)^(1/4). By the column estimates, if u≥Y a proportion at most

    O_{k,C}(1/log^4(2u)+1/log n)

of the column input is lost. For u<Y use the bound one. Shrink the input of a column in equal proportion across its source rows, then route it into the available target capacities. The result is a fractional bipartite matching. Integrality gives an ordinary matching at least as large as the total mass routed. For each included row a=h s, incoming q≤u and log s≥(log n)/2. With an absolute constant adjusted for k,C, define

    F(a)=K_0 Σ_{p^j|a} (log p)/log^4(2p^j).

The discarded powers q≤Y contribute at most ψ(Y)=O(Y) in the numerator of the lost mass. Thus, writing m_0 for the total number of unmatched rows, we have

    m_0 ≤ o(n/log² M)+ O(n/log n) + O((nY+Σ_{a∈A}F(a))/log n).

For every fixed λ>0 the average of exp(λF(a)) over [1,M] is bounded uniformly in M, by the convergent Euler product obtained from F(a) ≤ Σ_{p|a} O((log p)^−3). Put R=log(M/n). Applying Jensen gives E_A F=O(1) for bounded R and E_A F=o(R) if R tends to infinity (first hold λ fixed and then let it increase).

For completeness, if R≤sqrt(log M), the displayed estimate implies (m_0/n)(R+log log M)=o(1). For the unmatched set E, the mean of 2^ω on [1,M] is ≤1+log M. Jensen therefore bounds Σ_{a∈E}ω(a) by (m_0/log 2)(log(M/m_0)+log(1+log M))=o(n), with the empty set immediate. Cover these atoms individually. If R>sqrt(log M), put V=M/(3n). Then m_0 log M/log V=o(n). In each unmatched row set aside singleton full prime-power atoms above V and greedily pack the others into consecutive blocks of product ≤V. Each pair of successive small blocks has product >V, so the number of blocks plus singletons per row is O(1+log M/log V). Every small block has at least 3n multiples in I and can use a fresh one. Supply the remaining singletons by nested prime-power level repair. The repair of a matched row costs at most one extra position beyond its representative; the nested-level repair is valid because the full interval supplies at least the source count at every level. The total cost is 2(n−m_0)+o(n) in either range, proving the theorem.

The analytic input is the prime number theorem in arithmetic progressions for a fixed modulus, with its classical log-power remainder. See also the [original cofactor argument](../cofactor_flow_2026_11_26/README.md) for the two-block bound and nested repair.
