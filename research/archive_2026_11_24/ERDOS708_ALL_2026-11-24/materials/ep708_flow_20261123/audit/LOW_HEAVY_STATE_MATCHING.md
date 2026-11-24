# Total-variation control and matching of low substantial-prime states

## Status and scope

This note proves a finite comparison of the entire empirical truncated-prime-state distributions of a prefix and an arbitrary equal-length interval. In an actual sparse obstruction, its error is o(m), and it gives an injective matching of all but a weighted o(m) set of sources to targets that cover their complete low substantial-prime parts.

Each matched source uses one target, and the target bins are disjoint. The argument does not construct a second cover for the remaining prime coordinates, and it does not prove J_weak. In particular, a collection of large-prime semiprime parts need not admit a one-target-per-source divisibility matching.

The finite-difference and matching assertions received an independent mathematical audit from another collaborating agent.

## 1. Finite empirical-state theorem

Let P be a finite set of k primes. Fix an integer s>=1 and define

    z_p(n)=min(v_p(n),s),
    z(n)=(z_p(n))_{p in P},
    nu(n)=#{p in P:p|n},
    mu_P=sum_{p in P}1/p.

For a length-M interval I={x+1,...,x+M}, x>=0, let

    N_0(sigma)=#{n<=M:z(n)=sigma},
    N_I(sigma)=#{b in I:z(b)=sigma},

where sigma ranges over {0,...,s}^P. Define the one-sided histogram deficit

    D(P,s;M,I)=sum_sigma (N_0(sigma)-N_I(sigma))_+.

Both histograms have total mass M, so D is also half their L1 distance.

**Theorem.** There is a constant C_s depending only on s such that

    D(P,s;M,I)
       <=C_s [k^s+M mu_P^{s+1}+k^{s+1}].                 (1)

For k=0 the deficit is zero. The bound is uniform in the primes, M, and the shift. No optimality, source set, or weight vector is needed for (1).

## 2. Arbitrary bounded functions and presence inversion

Fix any function f:{0,...,s}^P->[0,1]. For a prime subset S, let z^S be the vector that retains z_p for p in S and sets all other coordinates to zero. Define

    c_S(z)=sum_{R subset S}(-1)^{|S|-|R|}f(z^R).

In particular c_empty=f(0). Boolean inversion gives

    f(z)=sum_{S subset P}c_S(z).                          (2)

If a coordinate in S is zero, its two paired contributions cancel, so c_S(z)=0. Also

    |c_S(z)|<=2^{|S|}.                                   (3)

Put

    T_s(z)=f(0)+sum_{1<=|S|<=s}c_S(z).

Whenever nu(z)<=s, every nonzero term of (2) is included, so T_s(z)=f(z). For nu>=s+1,

    binom(nu,j)<=binom(s+1,j)binom(nu,s+1)  (j<=s).

Equations (3) and 0<=f<=1 therefore imply

    |f(z)-T_s(z)|<=B_s binom(nu(z),s+1),                  (4)

where, for example,

    B_s=2+sum_{j=1}^s 2^j binom(s+1,j)

works uniformly for every f. This estimate also holds when nu<=s, because both sides then vanish.

## 3. Finite prime-power differences

For a fixed S of size j, c_S depends on j exponent coordinates, each with values 0,...,s, and vanishes whenever one coordinate is zero. Applying the usual successive finite differences yields

    c_S(z(n))
      =sum_{1<=e_p<=s, p in S}
          beta_{S,e} 1_{prod_{p in S}p^{e_p}|n}.           (5)

There are s^j exponent tuples. Every coefficient in (5) is a sum of 2^j signed values bounded by 2^j in absolute value. Hence

    sum_e |beta_{S,e}|<=(4s)^j.                          (6)

The total coefficient absolute sum in T_s, excluding its constant term, is therefore at most

    sum_{j=1}^s (4s)^j binom(k,j)<=A_s k^s               (7)

for a constant A_s and k>=1. The constant term cancels between the equal-length intervals.

For every modulus d, the interval count minus floor(M/d) is zero or one. From (5)--(7),

    |sum_{n<=M}T_s(z(n))-sum_{b in I}T_s(z(b))|
       <=A_s k^s.                                       (8)

This remains valid for moduli greater than M. The profiles z_p record all target valuations at least s in the saturated state s; no target with a higher exponent is omitted.

## 4. Both tail distributions are controlled

On the prefix,

    sum_{n<=M}binom(nu(n),s+1)
       <=M e_{s+1}((1/p)_{p in P}).

On the actual target interval, the upper multiple-count bound gives

    sum_{b in I}binom(nu(b),s+1)
       <=M e_{s+1}((1/p)_{p in P})+binom(k,s+1).          (9)

Thus (4), (8), and (9) imply

    |sum_{n<=M}f(z(n))-sum_{b in I}f(z(b))|
       <=A_s k^s
          +B_s[2M e_{s+1}+binom(k,s+1)]
       <=C_s[k^s+M mu_P^{s+1}+k^{s+1}].                 (10)

All constants are uniform over f, despite the dimension k being unbounded. Take f to be the indicator of the state set on which N_0 exceeds N_I. The left side of (10) is then D, proving (1).

The target bound in (9) is essential. A prefix exceptional-set estimate alone would not prove this total-variation statement.

## 5. The exact matching consequence

Partition prefix positions and target positions into their state bins. In every state sigma, pair min(N_0(sigma),N_I(sigma)) positions arbitrarily and injectively. Exactly D prefix positions remain unpaired.

For any source subset A of the prefix, one can instead pair its members directly in each bin. The number left unpaired is

    sum_sigma (N_A(sigma)-N_I(sigma))_+<=D,               (11)

because N_A(sigma)<=N_0(sigma). Thus every source subset has an injective state-preserving matching with at most D unmatched sources.

If a matched source a satisfies sum_{p in P}v_p(a)<=s, then every source exponent v_p(a) is at most s. A target b with z(b)=z(a) consequently satisfies

    v_p(b)>=v_p(a) for every p in P.                      (12)

When the common state is less than s, the exponents are equal. When it equals s, the target exponent is at least s, which still supplies the source exponent. Hence the matched target covers the source's full P-part, including powers.

This is one joint matching through disjoint bins. There is no separate reuse of a target for different source states.

## 6. Applying the theorem at the sparse-obstruction scale

Let A be an actual fixed-ambient raw-minimal obstruction, let m=|A|, and let rho=m/M->0. Fix eta>0, take s=floor(1/eta)+1, and set

    y=M^{1/(s+1)},
    P={p<=y:w_p>=eta}.

The independently checked absorption and shell bootstrap give

    mu_P=O_{c,eta}(rho^{1/s}),
    k<=y*mu_P.

Consequently

    k^{s+1}<=M mu_P^{s+1}=O_{c,eta}(m rho^{1/s}),
    k^s<=M^{s/(s+1)}mu_P^s
         =O_{c,eta}(m M^{-1/(s+1)}).

Equation (1) therefore becomes

    D<=C_{c,eta} m [rho^{1/s}+M^{-1/(s+1)}]=o(m).         (13)

The weighted monomial reduction already deletes an o(m) weighted-cost source set so that every retained source has at most s P-prime occurrences. Apply (11) to these retained sources. Every matched target then covers its source's complete low substantial-prime part by (12).

## 7. The unmatched sources have weighted cost o(m)

The number o(m) in (13) is not by itself enough to discard arbitrary sources of load up to log M. The previously proved exponential-moment bound supplies the needed stronger conclusion.

Let B be any unmatched source set of size d<=D. Put t=log(3/2), and let mu_w=sum_p w_p/(p-1)<=1+o(1) be the full original weighted mean. Jensen's estimate for any d distinct prefix integers gives

    sum_{a in B}X_w(a)
       <=(d/t)[log(M/d)+mu_w].                           (14)

There is nothing to prove if d=0. Otherwise put

    u=rho^{1/s}+M^{-1/(s+1)}.

Since d/m<=C*u and u->0, (14), using the eventual monotonicity of v*log(1/(rho*v)) on this small range, gives

    sum_B X_w / m
      <=O_{c,eta}(u[log(1/rho)+log(1/u)+1])=o(1).         (15)

The last limit follows from

    rho^{1/s} log(1/rho)->0,
    M^{-1/(s+1)}log(1/rho)
       <=M^{-1/(s+1)}log M->0,
    u log(1/u)->0.

Thus the unmatched sources may be removed at full original weighted cost o(m). The earlier objective and active-row-excess normalization survives this removal.

## 8. The missing joint step remains

The selected targets cover the low substantial-prime valuations of the matched sources. This does not reserve their remaining valuation capacities for other demands in any automatic way.

In particular, the high-prime part can contain more than one prime per source; a one-target-per-source divisibility matching for those high parts is false in general, as closely spaced semiprime families sharing a CRT target illustrate. Nor may a separately chosen diffuse cover be added at no cost or have its capacities counted independently.

The result removes pattern overcounting for the low substantial block and controls the cost of exceptional sources. A proof of J_weak still needs a single global budget for that block together with the high-prime and diffuse demands.

## 9. Filtering a high-prime cofactor bank into its correct low-state bin

One additional count avoids multiplying an error by the number of low states and high primes.

Let a be a retained source with at most s P-prime occurrences. Remove a prime occurrence q>y, and put d=a/q. The same argument works if an entire q-power component is removed. Write N=N_I(d). Since a<=M,

    N>=floor(M/d)>=q>y.

All target multiples of d have the form d*t, where t runs through N consecutive positive integers. To preserve the source's truncated low state, it suffices for t to avoid every prime p in P with v_p(a)<s. If v_p(a)=s, extra target powers are allowed. A union bound for the excluded primes shows that the number of suitable t is at least

    N(1-mu_P)-k.

Since k<=y*mu_P<N*mu_P, the original cofactor bank has at least

    N(1-2mu_P)                                           (16)

targets in the correct low-state bin. Thus each high-prime deletion bank retains a proportion 1-o(1) of its positions, uniformly over the source and the high prime.

This is a position-count estimate. It does not claim that the same fraction of weighted hinge mass survives: large target valuations could concentrate on the removed positions. Nor does (16) by itself prove Hall's condition for the many banks. Those are separate requirements of any proposed joint allocation.
