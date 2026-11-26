# Distinct prime factors up to the normal-order threshold

Let A consist of n distinct integers at least two, M=max A, and let I be any M consecutive positive integers. Write H for the minimum number of positions whose counts of prime-power multiples dominate those of A. A full atom of a source is the full power of one of its prime divisors.

**Theorem.** Fix 0<c<1. For all sufficiently large M, independently of the shift and density, H≤2n−1 if each a∈A satisfies ω(a)≤c log log M. All exponents are unrestricted. More generally discard all rows with at most two distinct prime factors from the test. In each tested row remove a numerically largest full atom q, put h=a/q and U=M/h, and require only ω(h)≤c log log U for every resulting h.

The reference point is [redlydi's growing-rank theorem](https://github.com/redlydi/Erdos708-Research/blob/32f397f8fdc00d0e9c73242d8510c541267a30db/reports/growing-prime-factors.md), which uses a constant below approximately 0.481545 and counts prime factors with multiplicity. The exclusive marked-profile kernel itself was recorded in the project's [component lemmas, Section 3](../asymptotic_2026_11_25/COMPONENT_LEMMAS.md). We supply the missing uniform bank lower bound for the exact exponents. No approximation of the shift is needed.

## Disjoint profiles

Choose each prime through M independently with fixed probability θ in (0,1). For a target b and real t>0 let D_t(b) be its full divisor supported on the marked primes ≤t. Write K_h(b)=Pr(D_{M/h}(b)=h). For fixed b the events for different h are disjoint: as h increases the threshold M/h decreases and D_{M/h}(b) cannot increase. Thus Σ_h K_h(b)≤1.

All primes of h are ≤q≤U. With z=1−θ and r=ω(h), the capacity of h sums exactly to

    Σ_{b∈I} K_h(b) = θ^r Σ_{b=hv∈I} 1_{gcd(v,h)=1} z^{ω_{≤U}(v)}.

Here only distinct prime factors ≤U are counted. Exact coprimality is needed even for prime powers in h. The v lie in a half-open real interval of length U with nonnegative endpoints.

## A uniform weighted sieve on the quotient interval

Uniformly in the shift, when r=O(log log U), as U→∞ we have

    Σ_v 1_{gcd(v,h)=1} z^{ω_{≤U}(v)}
        ≥ U (log U)^(−θ) (r+2)^(−C_θ).

To prove the estimate, choose a sufficiently large absolute K. The dimension-one fundamental lemma gives, for every subset S of primes ≤y≤H^(1/K), the quantity of integers in any real interval of length H avoiding S between constant multiples of H∏_{p∈S}(1−1/p) for H large. Use level H^(1/2), bounded interval remainders and the dimension bound obtained from all primes. The remainder costs O(sqrt H), whereas H∏(1−1/p) ≫ H/log H. See [Ford, Sieve Methods, Theorem 3.6](https://ford126.web.illinois.edu/sieve2023.pdf).

Set y=U^(1/K). Weight each quotient v by W(v)=1_{gcd(v,h)=1} z^{ω_{≤y}(v)} and let D=Σ_v W(v). First impose only the factors of h through y. Weighting agrees with the probability of avoiding a set S of primes through y in which all primes dividing h are included and the others are included independently with probability θ. The sieve lower bound gives

    D ≥ c₀ U ∏_{p≤y, p∤h}(1−θ/p) ∏_{p≤y, p|h}(1−1/p) − r(U/y+1)
      ≫_θ U (log U)^(−θ)/log(r+2).

The subtraction imposes the remaining primes of h. Use Mertens' theorem and ∏_{p|h}(1−1/p)≫1/log(r+2), since replacing its r primes by the first r primes can only decrease the product. The subtraction is negligible since r=O(log log U).

For p∈(y,U], put T=U/p. On these p-multiples drop the coprimality weights and retain only the random sieve through T^(1/K). The upper fundamental lemma, averaged over the marked primes, bounds the sum of W on the p-multiples by O_θ(T/(log(2T))^θ), with bounded T handled trivially. Split T dyadically. Within each dyadic band the sum of 1/p is O_K(1/log U), by the elementary upper bound for the number of primes and p≥U^(1/K). Therefore

    Σ_v W(v) ω_{y<p≤U}(v) ≪_θ (U/log U) Σ_{j≤log₂ U} (j+1)^(−θ)
                         ≪_θ U/(log U)^θ.

Under the probability weights W(v)/D, the mean number of these additional prime divisors is O_θ(log(r+2)). Jensen for z^t thus bounds the normalized expectation of z raised to this count below by (r+2)^(−O_θ(1)). This proves the uniform weighted estimate.

## Matching and coverage

With θ=c the bank mass is at least U/(log U)^{c+c log(1/c)+o(1)}. The exponent is strictly less than one for 0<c<1. Rows with the same h have distinct deleted full atoms q≤U, hence at most π(U)+O(sqrt(U) log(2U)) possibilities. The bank mass exceeds that number plus one for large U, uniformly under the rank hypothesis. All occupied U tend to infinity uniformly with M: U≤B implies every atom is ≤B, hence a divides lcm(1,...,floor B), and M=Uh≤Ba is bounded. Also log M≤(r+1)log U because h is the product of r atoms each at most U. Thus ω(a)≤c log log M implies r≤c' log log U for any fixed c<c'<1 and all large M.

Anchor a tested row at a full multiple of itself, remove the row and that position. Each occupied cofactor bank loses at most one unit. Split its remaining mass across its rows so each receives one unit, scaling any excess down. The per-position sum of all K_h is at most one. Bipartite matching integrality gives distinct representatives for all remaining tested rows, each divisible by h. They leave at most one full atom per row to repair. Untested rows need at most two singleton atoms each. For each prime, add as many largest remaining valuations as the maximum positive count deficit over its powers. Each deficit is at most the number of missing atoms at that prime, and all levels are sufficiently supplied in the full interval. Taking the union covers all rows with at most 2n−1 points. If there are no tested rows, anchor any row and repair all other atoms directly.

## Arbitrary reciprocal support

For a common pool P containing the primes of the tested cofactors one may mark only P. The removed atom can use any prime. Put L_P(U)=Σ_{p∈P,p≤U}1/p. Uniformly for r=O(log log U), the same calculation gives the cofactor capacity lower bound

    c_θ U exp(−θ L_P(U)) θ^r (r+2)^(−C_θ).

Indeed let V(t)=∏_{p∈P,p≤t}(1−θ/p). The initial lower bound is ≫U V(y)/log(r+2). The sum of the conditional large-prime counts has the upper bound Σ_{y<p≤U} O(T V(T^(1/K))), T=U/p. By Mertens over all primes, V(T^(1/K))/V(y)≪_{θ,K}(log U/log(2T))^θ. The same dyadic summation bounds this total by O(U V(y)). Jensen then yields the claimed lower bound since V(y)≥V(U)≫_θ exp(−θ L_P(U)). Thus it suffices that θ L_P(U)+r log(1/θ)≤(1−δ)log log U for some fixed θ∈(0,1) and δ>0. In particular, if L_P(U)≤(1−η)log log U uniformly at occupied U, any fixed upper rank multiple r≤C log log U is permitted: take θ sufficiently close to one. The pool can depend on M. Disjoint pools can also reuse a target whenever their cofactor credits involve disjoint primes, by the [local blocker argument](../unrestricted_shifts_2026_11_26/LOCAL_BLOCKERS.md).

## An unrestricted exceptional prime set

Fix 0<β<1 and 0<c<1, and allow any exceptional set S of at most (log M)^β primes of arbitrary sizes. If the number of distinct nonexceptional primes in each tested row is at most c(1−β)log log M, the same all-shifts exact 2n−1 bound holds. The size and multiplicity of the exceptional part of each source are unrestricted.

Mark every prime in S and mark the others independently with probability θ. For cofactor h let r count its distinct nonexceptional primes. Since each full atom in h is at most U,
log M≤(|S|+r+1)log U. Hence log U≥(log M)^(1−β+o(1)), and r≤c' log log U for any c<c'<1 at large M. The capacity formula uses θ^r, compulsory exclusions on the quotient for primes in E={p≤U:p∈S or p|h}, and factor z for each other occurring prime through U. Write N=|S|+r+2, so |E|≤N and log N=O(log log M).

Use y=U^(1/K) as before and define V_E(t) by taking a local factor 1−1/l at each prime l∈E through t, and 1−θ/l at all other primes through t. The total small-prime weight, now also forbidding E-primes above y, is ≫U V_E(y): before those additional exclusions the sieve yields this bound, and removing their multiples costs O(N(U/y+1)). This is negligible since V_E(y)≫_θ (log U)^(−θ)/log N, and y exceeds every fixed power of log M.

For a noncompulsory large p>y the upper sieve on p-multiples, with T=U/p, costs O_θ(T V_E(T^(1/K))). Its ratio to T V_E(y) is bounded by a constant times (log U/log(2T))^θ if T≥N^(2K), since the missing compulsory primes above T^(1/K) have total reciprocal sum at most N/T^(1/K)≤1. The same ratio bound with an extra O(log N) factor holds for all T≥1, by the reciprocal product of the first |E| primes. Relative to U V_E(y), the aggregate conditional count of these large primes is bounded by a constant on T≥N^(2K), by the preceding dyadic estimate. For T<N^(2K), the bound is

    O_θ((log N) (log U)^(θ−1) (1+log N)^(1−θ)) = o(1).

Thus Jensen for the remaining noncompulsory primes incurs only a constant factor. The capacity is ≫_θ U θ^r (log U)^(−θ)/log N; the factor log N is (log U)^o(1). Taking θ=c' leaves strict exponent slack. The exclusivity, matching and anchor arguments apply without change.

The proof also allows an individual multiplicity test. Write m_h for the number of tested rows with a given h. With r≤C log log U, no exceptional set, and any fixed θ∈(0,1), it suffices that

    m_h+1 ≤ θ^r U (log U)^(−θ) (r+2)^(−C_θ)

up to the fixed positive constant in the bank estimate. For instance, for any fixed C and δ>0, if r≤C log log U and m_h≤U/(log U)^(1+δ) throughout, then H≤2n−1 for large M. Choose θ close enough to one that θ+C log(1/θ)<1+δ. This only tests the local fiber sizes; the overall density n/M may be arbitrary.

## Why optimizing one common marking probability stops at the threshold

There are canonical intervals in which the available mass K_h is insufficient by an unbounded factor for one cofactor of rank r=ceil(log log U), for every common θ, even when the marking pool is restricted to the primes actually needed by the tested cofactors. This bounds the uniform-probability certificate with all tested cofactors in the same pool; it does not obstruct covering.

Take U prime tending to infinity. Let d be the product of the first r−1 odd primes and choose a power of two so that h=2^j d belongs to [4U,8U). Such a choice exists for large U since log d=O(r log r)=o(log U). Put M=hU, I=[1,M]. Include all hp with p prime between the largest numerical atom of h and U, inclusive at U and strict at the lower endpoint. This supplies (1+o(1))U/log U rows with cofactor h: its largest atom is o(U) since 2^j≤8U/d and its odd prime factors are O(r log r). Also include 2lU for every odd prime l<U, and 2UP for one prime U<P<2U. All fit below M and have three different prime factors. Their largest-atom cofactors 2l and 2U ensure that every prime through U is active, and all these cofactors share 2 with h.

For z=1−θ the capacity of h in I is at most θ^r Σ_{v≤U} z^{ω(v)}. The uniform [Hardy–Ramanujan inequality, Ford's Corollary 1.14](https://ford126.web.illinois.edu/lectnotes_2025.pdf) gives

    Σ_{v≤U} z^{ω(v)} ≤ 1 + O(z U/log U · exp(z(log log U + O(1)))).

In fact sum the upper bound O((U/log U)(log log U+C)^{k−1}/(k−1)!) for ω(v)=k over k≥1 with weight z^k. Using log(1−z)≤−z−z²/2 and r≥log log U, the total bank mass divided by U/log U is O((log U)/U + z exp(−r z²/2))=O(1/sqrt(log log U)), uniformly including the endpoints by continuity. The same holds for mixtures over a single global marking probability. The direct assignment a↦a in this very interval covers all sources.

## Sparse cofactor fibers without a rank hypothesis

Fix ε>0. There is C_ε such that H≤2n−1 for all large M at every shift if every tested cofactor h has U=M/h≥M^ε and multiplicity

    m_h ≤ U/[log U (log log M)^(C_ε)].

There is no restriction on the number of prime factors or their exponents. For example, the hypothesis holds for distinct tested cofactors with uniformly polynomial U.

Use the same absolute sieve constant K as above. For each global prime choose a uniform random number independently. At threshold U mark every prime ≤y=U^(1/K), and mark each prime in (y,U] if its chosen number is at most θ_M=1/log log M. As U increases, the marked prime set can only grow, so the bin events remain disjoint. A given h has at most K/ε primes >y because their product is bounded by M. Consequently the probability charge for requiring these primes to be marked is at least (log log M)^(−K/ε).

The quotient v must avoid all primes ≤y. The lower interval sieve gives ≫_K U/log U such candidates. Also exclude primes of h above y, losing at most (K/ε)(U/y+1). On the surviving v the mean number of primes in (y,U] dividing v is O_K(log log U). In fact sum the upper quotient sieve O_K(T/log(2T)) for p>y, T=U/p, retaining the sieve through T^(1/K) on each p-multiple. The dyadic sum is O_K(U log log U/log U). Dividing by the lower count gives the assertion. Jensen now lower bounds the average of (1−θ_M) to this number of primes by a positive absolute-in-M constant, since θ_M log log U≤1. Thus h receives ≫_{K,ε} U/[log U (log log M)^(K/ε)]. Choose C_ε>K/ε and use the same anchor, Hall and repair argument. Again, source rows with at most two distinct primes may bypass the test.

## One free shared prime per ordered cofactor

There is a separate exact relaxation of the [local blocker criterion](../unrestricted_shifts_2026_11_26/LOCAL_BLOCKERS.md). For each distinct tested cofactor d let p_d be any one prime (or none). Among cofactor labels e>d, demand a blocker from the primes of e/gcd(e,d) only when gcd(e,d) has some prime divisor different from p_d. Keep the same bank size requirement m_d+1 and anchor. When a target is shared by k distinct labels from different banks, process its labels in decreasing order. Every new label shares at most one distinct prime with the union of the preceding labels, since any other overlap was blocked. Thus the sum of support sizes of the k labels minus the size of their support union is at most k−1. At this target attribute its highest claimed full atom to a single row for each prime, leaving at most k−1 cofactor atoms unpaid even for unequal exponents. Exactly k−1 positions were saved by sharing. Different occurrences of one cofactor value remain injective, and the reserved anchor position is separate. Over all targets the saved positions pay for every duplicate cofactor atom by the nested repair. The result is H≤2n−1 with the relaxed criterion. In particular arbitrarily large pairwise cliques whose shared cofactor supports consist of a single common prime require no blockers for these intersections.
