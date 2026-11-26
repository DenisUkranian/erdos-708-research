# A sharp coefficient two for shifts close to a multiple of the source lcm

Let A consist of n distinct integers at least two, M=max A, L=lcm(A), and I={x+1,...,x+M} with x≥0. Write τ for the minimum number of distinct target positions needed for product divisibility. Write H for the stronger minimum requiring that the count of selected multiples of every prime power be at least its count in A. Always τ≤H. Logarithms are natural.

**Theorem 1.** Fix 0≤α<13/34. If there is an integer N divisible by L with |x−N|≤M(log M)^α, then H≤(2+o(1))n uniformly in all remaining parameters, as n→∞. The upper bound also allows any fixed multiplicative constant in the shift condition. With the displayed normalization (constant one), the worst-case τ is (2+o(1))n, with a matching lower construction for every large n.

**Theorem 2.** Fix an integer k≥2 and C>0. Suppose L divides N, gcd(k,N)=1 and |kx−N|≤CM. For all sufficiently large M (depending only on k and C) one has H≤2n−1. In particular A has no prime factor in common with k.

These restrictions are on residue classes. The size of the positive integer x itself is unrestricted. The general conjecture is still open. For example, if α=0 the first theorem applies to all shifts 0≤x≤CM, without a density restriction. The polynomial-shift result in the redlydi report *Density and shifts* assumes M≥n^{1+ε} for fixed ε. The two theorems have different hypotheses. No priority or formal verification claim is made.

## 1. Cofactors and the cost of a matching

Join a to b if b is a multiple of a/q for some prime power q=p^j dividing a. A matched row pays every full prime-power atom of a except possibly the one based at p. Having selected the distinct representatives, take for each prime p as many additional positions of largest available p-adic valuation as the largest positive deficit over its power levels. This count is at most the number of unpaid p-atoms. Each deficient level has enough remaining multiples, since the whole interval has at least floor(M/p^j) of them. The choices for the different primes can be united. A matched subset of s rows thus costs at most 2s positions for the level-count problem H. One can instead anchor a specified row a at a multiple of a, which leaves no unpaid atom for that row.

For completeness M≥(2n)^3 is easy for every shift. Split each a into two coprime blocks by putting its full prime powers in descending numerical order into the smaller current block. If h contains at least two atoms and q is its last addition, then h²≤Mq since the other block was at least h/q at that step. Also q²≤h. Hence h≤M^(2/3). Assign all such blocks distinct multiples (each bank has at least 2n positions). Each remaining singleton atom costs at most one by the level repair above. The number of blocks never exceeds 2n. We may consequently assume log M is comparable to log n when proving Theorem 1.

## 2. Source and target masses

Let Λ be the von Mangoldt function. A row a sends Λ(q)/log a to d=a/q for each prime power q dividing a. Its total mass is exactly one by the identity for log a. Write u=M/d. The column mass from all possible sources at most M is bounded by

    S_d ≤ sum_{q≤u} Λ(q)/log(dq) ≤ [ψ(u)+O(u/log M)]/log M,

with q≥2 understood. The terms dq<M^(1/4) together contribute at most M^(1/4)/d=u M^(−3/4). On the rest, 1/log(dq)≤[1+4log(u/q)/log M]/log M, and sum Λ(q)log(u/q)=∫_1^u ψ(t)dt/t=O(u).

For Theorem 1 set t_b=b−N and B=(2+C(log M)^α)M. At a target b with t_b nonzero allow column d to send mass Λ(|t_b|/d)/log B if d divides |t_b|. Only d arising from a source are needed, so d|N and hence d|b. The total capacity offered at b is at most log|t_b|/log B≤1. The zero offset can be ignored. If S'_d≤S_d is the actual source mass, route as much of it as possible within d, shrinking every input proportionally when needed. Since the paths end at valid neighbors, this projects to a fractional bipartite matching. Integral matching has at least the total routed mass by integrality of bipartite matching.

## 3. Prime estimates and the lost mass

Choose β with 17α/13<β<1/2 and set Y=(log M)^β. We use the quantitative short-interval PNT: for fixed η>0 and D>0,

    ψ(z+h)−ψ(z)=h+O_{η,D}(h/(log h)^D)   when z^(17/30+η) ≤ h ≤ z.

Use the von Mangoldt estimate in Guth and Maynard, Corollary 1.3 and its proof in §13.2. In their stated range up to z^0.99 the stronger exponential saving suffices. For z^0.99<h≤z, partition into equal pieces of lengths comparable to z^0.9 and apply the estimate at each starting point. The implied constants are uniform; we may always reduce η when needed. The earlier 7/12 exponent would give α<5/14. The ordinary PNT with its classical error applies if z≤h. We use D=4.

For u≥Y, in the case when the offsets have one sign, the column capacity numerator is a sum of Λ over a quotient interval of length u. Its lower endpoint z is at most O(u(log M)^α)=O(u^(1+α/β)). The chosen strict inequality for β permits 17/30+η<1/(1+α/β). Open or closed endpoint differences cost O(log(2+z+u)), absorbed by the error. If the offsets straddle zero, there are two prefix sums of total real length u, up to endpoints, and the ordinary PNT gives the same estimate. In either case the numerator is at least u[1−O(1/log^4(2u))]. Compare with S_d and use log B=log M+O(log log M). For u≥Y the relative source loss is at most

    O(1/log^4(2u) + (1+log log M)/log M).

For u<Y use the trivial loss of at most one. Every incoming q satisfies q≤u. Thus the mass lost at any row a is bounded by

    O((1+log log M)/log M) + [O(Y)+F(a)]/log a,
    F(a)=K sum_{q|a} Λ(q)/(log(2q))^4.

Here the discarded small powers cost at most ψ(Y)=O(Y) in the numerator, uniformly even for a very high prime power. Constants may depend on α,C. This use of all prime-power levels avoids a multiplicity loss.

For every fixed s>0 there is a finite C_s with M^(-1) sum_{a≤M} exp(sF(a))≤C_s. Indeed F(a)≤∑_{p|a}B_p, where B_p=K log p ∑_{j≥1}(log(2p^j))^(−4)=O((log p)^(−3)). Expand the squarefree divisor product and use floor(M/d)≤M/d. The resulting bound is ∏_p [1+(exp(sB_p)−1)/p]<∞. Put R=log(M/n). Jensen now gives

    average_A F ≤ (R+log C_s)/s.

This is bounded for bounded R, and is o(R) as R→∞ by letting s increase after the limsup. Fewer than √n source rows have a<√n. The number m left unmatched is therefore at most

    √n + O(n(1+log log M)/log M) + O(nY + sum_A F)/log n.

## 4. Repair at every density

For R≤√log M, keep the 2(n−m) cover of matched rows and use at most one new point per unpaid atom of the unmatched set E. For m>0 the identity 2^ω(a)=∑_{d|a} μ²(d) and Jensen imply

    sum_{a∈E} ω(a) ≤ m [log(M/m)+log(1+log M)]/log 2.

Write z=m/n. The loss estimate gives z→0 and z(R+log log M)→0: in particular YR/log M=o(1) since β<1/2, and the F contribution times R/log M is o(1) even if R grows up to √log M. Also z log(1/z)→0. Hence the repair costs o(n).

For R>√log M let V=M/(3n) and D=ceil(log M/log V). Then mD=o(n), since Y=o(√log M), the average of F is o(R), and log M=O(log n). Split an unmatched row using its *full prime-power atoms*. Defer every atom above V as a singleton. Greedily pack the remaining atoms into consecutive blocks of product ≤V. Each pair of adjacent finished blocks has product >V. Counting by logarithms, the number of blocks plus deferred atoms is O(D) per row. Each nonunit small block has at least 3n target multiples; choose one fresh multiple outside the matched cover and the earlier selections. The current size stays below 3n since mD=o(n). The deferred singleton atoms are supplied by the nested-level repair. Using full atoms ensures that level counts are preserved even if a prime has a large exponent. This proves Theorem 1's upper bound.

## 5. Strict gain for fixed denominators

For Theorem 2 use t_b=kb−N and B=(2+C+k)M. Each relevant d divides L, so it is coprime to k, and d|t_b implies d|b. On a positive or negative portion, |t_b|=dq' requires q' in the reduced residue class ∓N d^(−1) modulo k (minus for positive offsets). Each such q' corresponds to exactly one b on that portion. The total real length of the quotient intervals is ku. Both are contained in [0,(C+k)u], up to endpoints. By the PNT in arithmetic progressions for fixed k, their combined Λ mass is (k/φ(k)+o_{k,C}(1))u as u→∞, uniformly in endpoints. The target capacity at each b remains at most one. Compare to the source column bound. Because k/φ(k)>1, choose η>0 and a constant U_0 so that for all u≥U_0 and all large M the target column can receive more than (1+3η) times S_d.

Use only source powers q≥U_0. Every surviving column has u≥U_0. A row a loses at most ψ(U_0)/log a. Choose a fixed a_0 large enough that the retained row mass times (1+3η) is ≥1+η whenever a≥a_0. Route this enlarged mass. This is a fractional flow certifying |N(S)|≥(1+η)|S| for every set S of such large rows. The graph can include all original one-omission edges, not only the edges used by the flow.

There are at most a_0 other rows. For any nonempty mixed set with at least (a_0+1)/η large rows, the surplus pays for every small row and one extra position. If a set contains a small row and fewer large rows, its size is bounded, whereas the small row alone has at least floor(M/a_0) neighbors. A nonempty set of only large rows has integral neighborhood size strictly greater than its size. Thus every nonempty set has at least one more neighbor than rows. Anchor one source at any actual multiple, remove that row and position, and apply Hall to the rest. Repair gives H≤1+2(n−1).

## 6. Sharpness and the remaining shifts

Choose ℓ distinct primes in [P,1.1P], P large, and all t=ℓ(ℓ+1)/2 products p_i p_j, including squares. Put N=∏p_i² and center an M-term integer interval at N, M=(max p_i)². Every noncentral point carries at most one unit from these primes: a product of two, including a square, divides N and is greater than every nonzero offset in absolute value. The center carries exactly 2ℓ units, while the sources need 2t. Thus τ≥2t−2ℓ+1. For t≤n<t+ℓ+1, add n−t of the individual primes to the source set. They divide N and leave M unchanged, so the lower bound is 2n−O(√n) for every n. This is the classical Erdős–Surányi construction with padding. It gives no larger-than-two obstruction.

The map through prime-power quotients cannot simply be used with N=0 for all shifts. Assign two distinct primes >M to each of the M offsets, all 2M primes different. The Chinese remainder theorem places the corresponding pair in each target number. Dividing any target by any divisor d≤M leaves both primes, hence never a prime power. Every target edge of that particular flow vanishes. This construction concerns the auxiliary flow; the original divisibility graph can still have many edges. It also explains why the size condition on the effective offsets was needed.

## Sources

- [Guth and Maynard, New large value estimates for Dirichlet polynomials, Corollary 1.3 and §13.2](https://arxiv.org/pdf/2405.20552).
- [Vaughan, prime estimates in short intervals, Theorem 28.5](https://personal.science.psu.edu/rcv4/597-5f25/Class597-28.pdf).
- [Koukoulopoulos, The Distribution of Prime Numbers, chapter on primes in arithmetic progressions](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf).
- [Erdős problem 708 and the classical lower bound](https://www.erdosproblems.com/708).
- [Project's earlier nested Hall reduction](../audit_2026_11_26/MATCHING.md).
- [redlydi's density and shifts report](https://github.com/redlydi/Erdos708-Research/blob/32f397f8f/reports/erdos708-density-and-shifts%282%29.md).

## Additional partial results and checks

- [An exact harmonic reduction for general shifts](HARMONIC_REDUCTION.md) and [bounds for trapped divisor families](TRAPPED_DIVISORS.md).
- [Sharp exponent for matching the polylogarithmic smooth part at arbitrary shifts](SMOOTH_PROFILES.md).
- [Mixed small-prime prices and binary prices outside the core](MIXED_BINARY_PRICES.md), and [a smooth reciprocal comparison for general weights](RECIPROCAL_TRANSFER.md). The smooth comparison controls a different function from the full covering dual.
- [Gluing product covers while bounding losses at overlapping positions](SPARSE_GLUING.md).
- [Exact moment countermodel](verify_moment_obstruction.py). With four labels of cost 30, two of cost 60 and budget 100, all 25 feasible inclusion moments agree and factor into the prescribed marginals. Yet the one-deletion matching has deficit 1/64. Adding an independent cost-one label with probability 99/100 leaves a rank-at-least-three deficit of at least 7/800. The marginals in the example need not be reciprocals of actual primes.

[Arithmetic example checks](verify_examples.py) cover the lower construction, the empty auxiliary graph and the signs of both rational congruences. A [second exact tail countermodel](verify_conditional_tail.py) accompanies the reciprocal comparison.
