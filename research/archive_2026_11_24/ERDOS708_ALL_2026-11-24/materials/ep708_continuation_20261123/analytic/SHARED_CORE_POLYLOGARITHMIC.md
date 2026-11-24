# A shared polylogarithmic core and one outside prime per source

## Status and main conclusion

This note proves an integer coefficient-two asymptotic theorem for a shared core of at most c_0 (log M)^2/log log M primes, for some absolute c_0>0. It includes every fixed core bound (log M)^a with a<2. It permits arbitrarily many possible outside primes across the source set and arbitrary powers of each source's single outside prime. There is no separation between core and outside prime sizes. The fixed-exponent proof appears first; Sections 10--11 verify the stronger quantitative bounds.

The proof uses three explicit stages: cover all outside-prime demands, choose simultaneous carriers for the regular core cofactors, and repair the remaining bad core demands. The first two stages concern disjoint prime families, so their selected target sets may overlap safely. All shared core demands are counted with full multiplicity.

The complete argument has passed a separate independent internal mathematical audit. The unrestricted problem remains open; this is not an assertion of external peer review or novelty relative to all literature.

## 1. The theorem

Fix 0<a<2. For every epsilon>0 there is M_0(a,epsilon) such that the following holds for every M>=M_0.

Let A be a set of n distinct integers in [2,M]. Suppose there is a designated prime set E with

    |E| <= (log M)^a

such that each source has at most one distinct prime factor outside E. Thus every source is either E-smooth or has the form

    d r^e,   d E-smooth,   r prime outside E,   e>=1.

For every positive interval I of M consecutive integers,

    tau(A,I) <= (2+epsilon)n.

Consequently tau(A,I)<=(2+o(1))n uniformly over this source class and all shifts as n tends to infinity. The actual prime values are unrestricted, and E may vary with M and with the source set.

All logarithms are natural unless a base is displayed.

## 2. Covering all outside-prime parts

For each prime r outside E that occurs in the sources, list its source exponents e_1,...,e_s. Assign a target multiple of r^e_i to each demand, using distinct targets within this r-group.

Such an assignment exists. For every j>=1, distinctness of the sources gives

    #{i:e_i>=j}
       <= floor(M/r^j)
       <= #{b in I:r^j divides b}.                       (1)

The allowed target sets are nested. Equivalently, process the exponents in decreasing order: at a current exponent e_i, its target set has at least the number of demands with exponent at least e_i, so one target remains unused after the earlier assignments. This is precisely the nested Hall condition.

Let B_r be the selected targets for r. Then |B_r| equals the number of sources containing r, and their r-valuations cover the full source r-demand. Take

    B_out = union over outside r of B_r.

The sets may overlap. For every outside prime r, the union still contains all of B_r, so it covers that prime's entire demand. Different r-groups have disjoint demanded prime coordinates, and hence overlaps do not require any demand to be subtracted.

Let n_out be the number of ALL mixed sources, including those later called bad. Since each mixed source contains exactly one distinct outside prime,

    |B_out|<=n_out.                                      (2)

No source-exponent bound, minimal-counterexample argument, or prime-size restriction is used here.

### 2.1 A finite exact certificate

Let d(a) be the full E-smooth part of each source, and let m_d count sources with core part d. Choose any collection D of occupied core parts d>1. If every target interval has at least m_d positions with exact E-part d for every d in D, then

    tau(A,I)
       <=n_out+sum_{d in D}m_d
           +sum_{a:d(a)>1,d(a) not in D}Omega(d(a)).

Use the outside cover from Section 2, disjoint exact-part bins for the selected core fibres, and a global repair for the remaining core units. Core part one requires no carrier. If this explicit right side is at most 2n, it certifies the exact bound for every shift.

For T=M/d, a finite all-shift lower bound on the bin size is

    L_E(T)
      =sum_{S subset E, |S| even}floor(T/product S)
        -sum_{S subset E, |S| odd}ceil(T/product S),

with the empty product equal to one. The coarser bound
T product_{p in E}(1-1/p)-2^|E| is also valid. Either bound can be compared with m_d. These sufficient certificates are not asserted to be necessary.

## 3. Uniform Rankin estimates from core cardinality

Choose a fixed sigma satisfying

    max(0,1-1/a) < sigma < 1/2.                           (3)

Such a choice exists because a<2. Write

    Psi_E(x) = #{d<=x:d E-smooth},
    Z_E(sigma)=prod_{p in E}(1-p^(-sigma))^(-1).

For every x>0, elementary Rankin counting gives

    Psi_E(x)<=x^sigma Z_E(sigma).                        (4)

If E contains k primes in increasing order, then p_i>=i+1. Since
-log(1-p^(-sigma))<=p^(-sigma)/(1-2^(-sigma)), we obtain

    log Z_E(sigma)<=C_sigma k^(1-sigma).                 (5)

For E empty, Z_E=1. Thus k<=(log M)^a and (3) imply

    Z_E(sigma)
      <=exp(C_sigma (log M)^(a(1-sigma)))
       =M^{o(1)},                                       (6)

uniformly in all actual core-prime values. In particular, all estimates below hold uniformly even when E contains very large primes.

Choose

    theta=(1/2-sigma)/(2(1-sigma))>0,
    Z=M^theta,
    beta=sigma+theta(1-sigma)=1/4+sigma/2<1/2.             (7)

The parameters sigma,theta,beta are fixed once a is fixed.

## 4. Exact core-part bins at quotient length at least M^theta

We use the inherited uniform interval sieve: for Q a subset of primes at most Y and a real interval J of length T>=Y^u,

    #{t in J:gcd(t,product Q)=1}
      =T prod_{q in Q}(1-1/q)(1+O(e(u))),
    e(u)->0.

The error is uniform in Q and in the interval shift. The complete statement and its fundamental-lemma proof dependencies are provided in the preceding synthesis. We also use the classical estimate

    prod_{q<=Y prime}(1-1/q)>=c/log Y.

Set

    Y=(log M)^(2a+3),
    E_small={p in E:p<=Y},   E_large=E\E_small.

For every real interval J of length T in[M^theta,M], one has log T/log Y ->infinity uniformly. The sieve therefore supplies at least

    (c/2) T/log Y

integers coprime to E_small, for sufficiently large M.

Imposing coprimality to E_large discards at most

    sum_{q in E_large}(T/q+1)
      <=T|E|/Y+|E|
       =o(T/log Y),                                     (8)

because |E| log Y/Y ->0 and |E| log Y/T ->0 uniformly at T>=M^theta. Consequently, for some c_a>0,

    #{t in J:gcd(t,product E)=1}
       >=c_a T/log log M                                 (9)

for every such interval, all shifts, and every admitted E once M is large.

For an E-smooth d, the targets b with exact E-smooth part d are precisely b=d t with t in the scaled interval I/d and gcd(t,product E)=1. Different d define disjoint target bins.

## 5. Bad sources have negligible total core demand

Call every pure E-smooth source bad. For a mixed source, write its full E-smooth part as d and its outside prime-power part as f=r^e. Call it regular if

    T_d=M/d>=Z=M^theta,

and bad otherwise.

A bad mixed source has d>M/Z and d f<=M, so necessarily f<Z. Counting all integer f in this range, rather than only outside prime powers, gives

    #A_bad
      <=Psi_E(M)+sum_{2<=f<Z}Psi_E(M/f)
      <=Z_E(sigma) M^sigma
                        [1+sum_{2<=f<Z}f^(-sigma)]
      <=C_sigma Z_E(sigma) M^sigma Z^(1-sigma)
       =M^{beta+o(1)}.                                  (10)

The condition d>M/Z has only been dropped in an upper bound. The estimate is uniform over all admitted source sets.

Every remaining unmet core demand from these sources costs at most

    sum_{b in A_bad}Omega_E(b)
       <=sum_{b in A_bad}Omega(b)
       <=#A_bad log_2 M
       =M^{beta+o(1)}
       =o(sqrt M),                                      (11)

where Omega_E counts prime occurrences belonging to E. This bound is independent of n and of the interval shift.

## 6. Choose simultaneous carriers for the regular core cofactors

Group regular mixed sources by their exact E-part d. Let m_d be the fibre size, and put T_d=M/d. Each source in a fixed fibre has the form d f with a distinct prime power f<=T_d. Thus

    m_d<=P(T_d),

where P(T) counts positive prime powers p^e with e>=1. Chebyshev's bound and the elementary estimate for higher powers give

    P(T)<=pi(T)+sum_{2<=e<=log_2 T}pi(T^(1/e))
         =O(T/log T).                                   (12)

Indeed the higher-power sum is at most sqrt(T) log_2 T, which is smaller than T/log T for large T.

Every occupied regular fibre has T_d>=M^theta. By (9), its exact-E-part target bin has at least

    N_d>=c_a T_d/log log M

positions. Since log T_d>=theta log M, equations (9)--(12) imply

    m_d/N_d=O_a(log log M/log M)->0.

Therefore N_d>=m_d simultaneously for all regular fibres once M is large.

Choose m_d distinct targets from each bin. The bins are disjoint, so the resulting set B_core has exactly n_reg positions, where n_reg is the number of regular sources. Its product covers the full product of their E-parts:

    product of d(a), a regular, divides product B_core.  (13)

All shared core-prime multiplicities are included in this single assignment.

## 7. Union the two stages and repair only bad core units

Take B_0=B_out union B_core. Then

    |B_0|<=n_out+n_reg.

For every outside prime, B_0 covers the entire source demand because it contains B_out. For every core prime, it covers the full regular-source demand because it contains B_core.

Hence the only possible remaining deficits belong to E, and their total number of prime units is at most the left side of (11). Whenever a core prime is deficient, the full interval supplies its entire demand, since

    product A divides M! divides product I.

Therefore an unused target divisible by that prime exists. Add one such target. Every addition reduces the total positive deficit by at least one and never increases another deficit. At most the number of units in (11) is required.

This gives the explicit covering estimate

    tau(A,I)
      <=n_out+n_reg+sum_{a in A_bad}Omega_E(a)
      <=2n+M^{beta+o(1)}.                                (14)

Overlaps between B_out and B_core are harmless: the demanded prime families of the two stages are disjoint, and the final repair is performed globally. No independently constructed covers of overlapping full demands are being combined.

## 8. Uniform coefficient-two asymptotics

If n<=sqrt M/4, the known ambient quadratic theorem gives the exact bound tau<=2n.

If n>sqrt M/4, then (11) gives

    M^{beta+o(1)}/n
       <=4M^{beta-1/2+o(1)}->0.

Thus (14) is tau<=(2+o(1))n uniformly for all admitted n,M,E,A and shifts. For every epsilon>0 this is a uniform large-M statement. Finally n->infinity implies M>=n+1->infinity, proving the theorem in the stated form.

The use of the quadratic gate occurs only in this last passage. There is no minimality argument and no fractional-cover rounding step in this proof.

## 9. Scope and the exponent barrier in this argument

The theorem includes every fixed power (log M)^a below exponent two, for example (log M)^1.99. It strictly expands the shared-core size permitted by the earlier controlled-weight transfer, while using a different integer construction.

The proof needs a fixed sigma with

    a(1-sigma)<1,    sigma<1/2.

The first makes the Euler factor subpolynomial uniformly from core cardinality; the second leaves a fixed positive margin below sqrt M for the bad-source cost. These inequalities are compatible for a<2. The fixed-parameter argument alone does not establish a=2 or an arbitrary instance-dependent exponent tending to two. Sections 10--11 separately verify two specified approaches to that endpoint.

The designated core must be common to the whole source set, and each source must have at most one distinct outside prime. General minimal-obstruction structure still permits a core of order sqrt(n/log n), vastly larger than a fixed power of log M in the subquadratic range. The unrestricted asymptotic and exact assertions therefore remain unproved. No optimality or literature-priority claim is made.

## 10. An explicit numerical bound close to a squared logarithm

For all sufficiently large M, the same integer conclusion holds under

    |E|<=10^(-6) (log M/log log M)^2.                     (15)

This is stronger than every fixed exponent a<2. The constant is sufficient, not optimal.

Put L=log M, l=log L, assume l>=4, and now let the parameters vary with M:

    delta=1/l,
    sigma=1/2-delta in[1/4,1/2),
    theta=delta/[2(1-sigma)]=1/(l+2),
    beta=1/2-1/(2l).

For k=|E|>=1, the Euler estimate is uniform:

    log Z_E(sigma)
      <=[2/(1-2^(-1/4))] k^(1-sigma)
      <13 k^(1-sigma).

This follows by summing (i+1)^(-sigma), using 1/(1-sigma)<=2. Since k<=L^2, k^(1/l)<=e^2, and (15) gives sqrt k<=10^(-3)L/l. Hence

    log Z_E(sigma)<13e^2 sqrt k<100 sqrt k<=L/(10l).       (16)

The empty core is immediate. With Z=M^theta, the sum in the bad-source bound is at most 3Z^(1-sigma), uniformly in this range. Thus

    #A_bad<=3sqrt M exp(-L/(2l)+L/(10l))
          =3sqrt M exp(-2L/(5l)).

Its total core demand is at most this expression times log_2 M, which is o(sqrt M).

The shrinking theta requires a fresh bin check. Set Y=L^7. Every regular fibre has

    T>=exp(L/(l+2)),
    log T/log Y>=L/[7l(l+2)]->infinity.

The small-prime sieve supplies a fixed positive multiple of T/log Y. Deleting the other core-prime multiples costs at most

    Tk/Y+k<=T/L^5+L^2=o(T/log Y).

Thus exact-core bins have size at least a constant times T/l. Their prime-power fibre size is O(T/log T), with ratio

    O(l/log T)=O(l(l+2)/L)->0.

The same outside matching and global repair therefore give the uniform constructive bound

    tau(A,I)<=2n+O(sqrt M L exp(-2L/(5l))).                (17)

If n<=sqrt M/4, use Wang's exact quadratic theorem. Otherwise divide the error by n>sqrt M/4. The relative error is
O(L exp(-2L/(5l)))=o(1). This verifies the asserted uniform coefficient-two conclusion, without applying a fixed-parameter theorem at a varying exponent.

## 11. A stronger order from Chebyshev's prime bound

There exists an absolute c_0>0 such that, under the same source factorization hypothesis of at most one distinct outside prime per source, the uniform conclusion and the error bound (17) hold whenever

    |E|<=c_0 (log M)^2/log log M.                         (18)

The existence of a positive absolute c_0 is asserted; no optimal value is claimed.

Chebyshev's estimate gives p_i>=c i log(i+1) for an absolute c>0. Uniformly for sigma in[1/4,1/2],

    log Z_E(sigma)
       <=C k^(1-sigma)/(log(k+1))^sigma.                 (19)

To verify uniformity, split the sum of p_i^(-sigma) at i=sqrt k. The first portion is O(k^((1-sigma)/2)). The second is O(k^(1-sigma)/(log(k+1))^sigma). The first is absorbed uniformly: its ratio to the second bound is at most a constant times sqrt(log(k+1))/k^(1/4). The Euler-logarithm factor 1/(1-2^(-sigma)) is uniformly bounded. Enlarge C to handle small k.

Retain sigma=1/2-1/l and put K=floor(c_0 L^2/l). The function in (19) is increasing in k, since

    k d/dk log[k^(1-sigma)/(log(k+1))^sigma]
      =(1-sigma)-sigma k/[(k+1)log(k+1)]
      >=1-2sigma>=0.

For every fixed c_0>0,

    K^(1-sigma)/(log(K+1))^sigma
      =sqrt(K/log(K+1))
          exp[(log K+log log(K+1))/l]
      =(e^2 sqrt(c_0/2)+o(1)) L/l.                       (20)

Choose c_0<=1 so small that C e^2 sqrt(c_0/2)<1/20. Equations (19)--(20) imply log Z_E(sigma)<=L/(10l) for every k<=K once M is large. Thus the Euler bound (16) still holds. Also k<=L^2, so all the Y=L^7 sieve estimates, deletion costs, fibre counts and bad-source bounds in Section 10 apply unchanged. They prove (17) and the coefficient-two asymptotic theorem under (18).

This is the strongest shared-core bound established in this note. It still leaves a log log M denominator and an unspecified sufficient absolute constant. It does not establish a core of size (log M)^2 or an optimal endpoint. The unrestricted minimal-obstruction core can be much larger, so the general problem remains open.
