# Independent audit: a common core of fewer than a fixed power two of log M

## Status and precise scope

**PASS for the mathematical argument below, for the complete a<2
transcriptions in `analytic/SHARED_CORE_POLYLOGARITHMIC.md` and
`sections/shared_core_matching.tex`, and for both quantitative corollaries
in the latter file (`cor:sc-near-square`, `cor:sc-chebyshev-core`).** This is an
independent internal audit of the direct construction proposed by the root
agent and developed in that note. It is not formal verification or an
external referee report. The unrestricted exact and asymptotic versions of
Erdos Problem 708 are not proved here.

Fix **one constant** `0 < a < 2`. Let `A` consist of `n` distinct integers in
`[2,M]`, and suppose a designated finite prime set `E` has
`|E| <= (log M)^a`. Each source is either E-smooth or has the form
`d r^e`, where `d` is E-smooth, `r` is one prime outside E, and `e >= 1`.
The conclusion is `tau(A,I) <= (2+o(1)) n`, uniformly in this source class
and in every shift `I={x+1,...,x+M}`, `x>=0`.

There is no required separation between core and outside prime sizes. The
outside-prime exponent need not be one. The core may vary with `M` and `A`.
The proof below uses no minimal-counterexample reduction or forced-bank lemma.
Sections 6 and 7 audit stronger, separately quantified moving-parameter
extensions, culminating in a core of size `c_0 (log M)^2/log log M`.

## 1. Uniform estimates for exceptional sources

Choose a fixed

    max(0,1-1/a) < sigma < 1/2.

The interval is nonempty for every fixed `a<2`. Ordering the core primes gives
`p_i >= i+1`, so

    Z_E(sigma) = product_{p in E}(1-p^(-sigma))^(-1)
    log Z_E(sigma) <= C_sigma |E|^(1-sigma) = o(log M).

Thus, uniformly in the actual core primes,

    Psi_E(t) <= Z_E(sigma) t^sigma,
    Z_E(sigma) = M^{o(1)}.

Choose a fixed `theta>0` sufficiently small that

    beta = sigma + theta(1-sigma) < 1/2,
    Z = M^theta.

Call a source exceptional if it is E-smooth, or if it is mixed and its full
E-part `d` satisfies `T_d=M/d<Z`. In the latter case its outside prime-power
part `f=r^e` satisfies `2<=f<Z`. Distinctness of sources and unique
factorization justify the overcount

    #A_exceptional
      <= Psi_E(M) + sum_{integers 2<=f<Z} Psi_E(M/f)
      <= C_sigma Z_E(sigma) M^sigma Z^(1-sigma)
      = M^{beta+o(1)}.

The sum over all integers is a deliberate overcount of prime powers. It does
not require every `d` counted there to satisfy `d>M/Z`. Consequently

    sum_{a in A_exceptional} Omega(a)
      <= #A_exceptional log_2 M
      = M^{beta+o(1)} = o(sqrt M).

All estimates are uniform; `a,sigma,theta` are fixed before `M` grows.

## 2. Jointly covering every outside-prime demand

For each outside prime `r`, let `A_r` be all sources with outside prime `r`,
including exceptional mixed sources, and let `n_r=|A_r|`. For every `j>=1`,

    #{a in A_r : v_r(a)>=j}
      <= floor(M/r^j)
      <= #{b in I : v_r(b)>=j}.

The first inequality uses distinct source integers in `[2,M]`, not merely
the distinctness of their exponents. The second is the usual interval count.
The eligible target sets `{b:r^j|b}` are nested, so these inequalities are
exactly the Hall conditions for assigning to every source in `A_r` a distinct
target with at least its required r-adic exponent. This can equivalently be
proved by assigning the largest exponents first.

Let `B_r` be the resulting `n_r` targets. Their union `B_out` has size at most

    sum_r n_r = n_out,

where `n_out` is the number of **all** mixed sources. It supplies all outside
prime demands simultaneously: different `B_r` may overlap, but their demands
concern different prime coordinates. No multiplicity is lost by this union.

## 3. Distinct carriers for all regular core cofactors

For a regular mixed source the quotient length `T_d=M/d` is at least
`M^theta`. For each fixed `d`, different sources have different outside
prime-power parts. Therefore its fibre size satisfies

    m_d <= #{prime powers f<=T_d} = O(T_d/log T_d).

The last estimate follows from `pi(T)=O(T/log T)` and the elementary bound
`sum_{e>=2} pi(T^(1/e))=O(sqrt(T) log T)`.

The bin of targets having **exact** full E-part `d` is

    B_d = {b in I : d|b and gcd(b/d, product E)=1}.

These bins are pairwise disjoint. To count one, use the scaled real interval
of length `T=T_d`, and split `E` at `Y=(log M)^(2a+3)`. The inherited uniform
interval sieve applies to the primes at most `Y`, since
`log T/log Y -> infinity` uniformly for `T>=M^theta`. Together with the
Mertens lower product bound it supplies at least `c T/log Y` candidates.
Removing divisibility by the larger core primes costs at most

    sum_{q in E,q>Y}(T/q+1) <= T|E|/Y+|E| = o(T/log Y).

This estimate also includes primes larger than `T` and arbitrary shifts.
Thus `|B_d| >= c_a T/log log M`, which exceeds `m_d` for all occupied regular
fibres once `M` is large. Select `m_d` targets in each bin. The resulting
`n_reg` distinct targets jointly cover the product of **all** regular core
cofactors, with their full shared-prime multiplicities.

## 4. Union and one global repair

Take the union of `B_out` and the regular core carriers. This union has at
most `n_out+n_reg` targets. It covers all outside prime demands and all
regular E-prime demands. Overlap is harmless: the two certified collections
cover disjoint sets of prime-coordinate demands, and the union contains each
collection in full.

Only core demand from exceptional sources can remain. Its total deficiency
is at most `sum_exceptional Omega(a)`. The full interval supplies every
source demand because `product A | M! | product I`. Whenever a prime is
still deficient, some unused target is divisible by it; adding such a target
decreases the total deficiency by at least one. Hence one global repair uses
at most the preceding exceptional Omega bound.

The resulting cover therefore has size at most

    n_out+n_reg+sum_exceptional Omega(a)
       <= 2n+M^{beta+o(1)}.

For `n<=sqrt(M)/4`, the external ambient quadratic theorem already gives an
exact cover of size at most `2n`. For larger `n`, dividing the displayed error
by `n` gives `M^{beta-1/2+o(1)}=o(1)`. This proves the asserted uniform
coefficient-two asymptotic. Since `M>=n+1`, the conclusion is also uniform as
`n` tends to infinity.

## 5. Dependencies and limitations of the fixed-exponent argument

The proof uses the established uniform interval sieve, the classical Mertens
product lower bound and Chebyshev prime upper bound, and the external
ambient `M>=16n^2` exact-cover theorem. On its own, the fixed-exponent argument
makes no numerical claim about the threshold `M_0(a,epsilon)`, no endpoint
claim at `a=2`, and no claim allowing `a` to approach two with `M`. The later
sections prove specific moving-parameter extensions. Sources with two
distinct outside primes remain outside the scope. The core's cardinality
bound is essential to the uniform
exceptional-source estimate and the bin count as presently proved.

## 6. Quantitative moving-parameter upgrade: an explicit constant

**PASS independently**, including all moving-parameter uniformity. Put
`L=log M`, `l=log L`, and suppose

    k=|E| <= 10^(-6) (L/l)^2.

For `l>=4`, choose

    delta=1/l, sigma=1/2-delta in [1/4,1/2),
    theta=1/(l+2), beta=1/2-1/(2l).

The elementary Euler-product estimate has a uniform constant:

    log Z_E(sigma)
      <= [1/((1-2^(-sigma))(1-sigma))] k^(1-sigma)
      <= [2/(1-2^(-1/4))] k^(1-sigma)
      < 13 k^(1-sigma).

For `k>=1`, `k<=L^2` implies `k^(1/l)<=e^2`; the empty support is
immediate. Since `13e^2<100`, the assumed bound on k gives

    log Z_E(sigma) < 100 sqrt(k) <= 0.1 L/l.

Furthermore `1+sum_{2<=f<Z}f^(-sigma)<=2 Z^(1-sigma)` uniformly in
this sigma range. The exceptional-source estimate is therefore explicitly

    #A_exceptional <= 2 sqrt(M) exp(-0.4 L/l).

Its total Omega cost is at most this quantity times `L/log 2`, still
`o(sqrt M)`.

The earlier **fixed-theta** bin lemma cannot simply be cited when theta
tends to zero. The required fresh calculation does hold. Take `Y=L^7` and
`T>=exp(L/(l+2))`. The sieve parameter satisfies

    log T/log Y >= L/[7l(l+2)] -> infinity.

Using `k<=L^2`, the two discarded-prime terms, normalized by `T/log Y`,
are bounded by

    7l/L^5 + 7L^2 l exp(-L/(l+2)) -> 0.

Thus exact-core bins have size at least a constant times `T/l`, while the
prime-power fibre has size `O(T/log T)`. Their ratio is
`O(l(l+2)/L)=o(1)`. Outside matching, union, global repair, and the final
quadratic gate are unchanged. The explicit constant `10^(-6)` is safely
within the numerical margin of the proof.

## 7. Strongest audited order: c_0 (log M)^2 / log log M

**PASS independently.** There exists an absolute `c_0>0` such that the
same uniform integer asymptotic holds for

    |E| <= c_0 L^2/l.

Here no numerical value of `c_0` is asserted. The preceding explicit
weaker hypothesis remains available separately.

The Chebyshev prime upper bound implies `p_i >= c i log(i+1)` with an
absolute positive c. Uniformly for `1/4<=sigma<=1/2`, this yields

    log Z_E(sigma)
      <= C k^(1-sigma)/(log(k+1))^sigma.                  (*)

To check uniformity, split the associated sum over i at `sqrt(k)`. The
first part is `O(k^((1-sigma)/2))`; the second is
`O(k^(1-sigma)/(log k)^sigma)`. The first is absorbed in the second
uniformly, since its ratio is at most a constant times
`sqrt(log k)/k^(1/4)`. Bounded positive k can be absorbed by one larger
absolute C. The empty support has Euler product one.

Set `K=floor(c_0 L^2/l)` and keep `sigma=1/2-1/l`. For every actual
support with at most K primes, its Euler product is at most the Euler
product on the first K primes, so applying (*) at K covers even tiny
supports without a separate asymptotic assumption on k. Equivalently,
the function `t^(1-sigma)/(log(t+1))^sigma` is increasing for t>0:

    t (log f)' = (1-sigma)
                 - sigma t/[(t+1)log(t+1)] >= 1-2sigma >= 0.

For fixed `c_0>0`, as M grows,

    K^(1-sigma)/(log(K+1))^sigma
      = [e^2 sqrt(c_0/2)+o(1)] L/l.

Indeed `log K=2l-log l+log c_0+o(1)` and
`log log(K+1)=log l+log 2+o(1)`. Choose c_0 so small that
`C e^2 sqrt(c_0/2)<1/20`. The Euler logarithm is then at most
`0.1 L/l` for all sufficiently large M, uniformly in every admitted
core. The rest of Section 6 applies verbatim: its bin argument only
requires `k<=L^2`, which holds eventually here.

This is an actual stronger cardinality order than every fixed power
`(log M)^a`, `a<2`, and than the explicit condition in Section 6. It
still requires one common core and at most one distinct outside prime
per source; it does not establish unrestricted Problem 708.
