# An exact price bound with disjoint sets of multiples

Write J=[1,M], I=(x,x+M] in positive integers, A a subset of J of size n. All primes below are at most M. Set X(b)=Σ w_p v_p(b), with 0≤w_p≤1, Q={p:w_p>0}, and Φ=Σ_A X−Σ_I(X−1)_+. The support Q can depend on M. Repeated prime factors are retained.

## An injection for overloaded rows (routes 3, 5 and 8)

Let a_Q be the full Q-part of a. For each row with X(a)>2 delete one occurrence of its largest active prime p and set h=a_Q/p, U=M/h. Let m_h count the rows giving h, and Q_U={q∈Q:q≤U}. Each prime of h is at most p≤U. Define a bank by

    K_h = { b∈I : h divides b and gcd(b/h, product of Q_U)=1 }.

The banks for the occupied h are disjoint. In fact b∈K_h means that its full part on Q_U is exactly h. As h increases, the cutoff U decreases, so those full parts cannot increase for a fixed b. Different rows giving h give different integers a/h≤U, each divisible by some p∈Q_U. Thus

    m_h ≤ Σ_{p∈Q_U} floor(U/p),
    |K_h| ≥ floor(U) − Σ_{p∈Q_U} ceil(U/p).

Here b/h runs over a real half-open interval of length U. In particular **the finite sufficient condition** at each occupied h is

    Σ_{p∈Q_U} [floor(U/p)+ceil(U/p)] ≤ floor(U).                 (1)

Whenever (1) holds, give every overloaded row a distinct b in its bank. Then X(b)≥X(a)−w_p≥X(a)−1. Consequently Σ_I(X−1)_+≥Σ_A(X−2)_+, so Φ≤2n **exactly**, for every shift and every n. The same argument works if |K_h|≥m_h is checked directly.

* If Σ_{p∈Q}1/p≤1/3, (1) holds even for bounded U. For t≥1, floor(t)+ceil(t)≤3t. The sum on the left is an integer.
* If Σ_{p∈Q}1/p≤1/2−ε for fixed ε>0 and the least active prime tends to infinity, then U tends to infinity uniformly at occupied h. The left side is ≤2U Σ_{p∈Q_U}1/p+π(U)≤(1−2ε)U+o(U). More generally only the cutoffs and reciprocal sums at the occupied h matter.
* On the entire band M^(1/4)<p≤M^(1/3), the reciprocal sum tends to log(4/3)<1/3 by Mertens. Thus **every** price vector supported there, including arbitrary placements of 1/3 and 3/4 on the proposed (M^.30,M^.32) band, satisfies Φ≤2n exactly for large M. The theorem also treats noncontiguous bands and has no relative-density loss. The complement of Q must have price zero in these statements.

There is a direct integral version. Test every row with a_Q>1 using the same h, even if its price is small. Under (1) on these banks, select its representative and charge the product of the h's to the distinct representatives. Each row leaves one prime occurrence. For any prime with a positive remaining exponent deficit, another multiple of the prime is available because the entire interval supplies all source valuations (count multiples at every power). Adding at most one point per missing occurrence covers the Q-projection in at most 2n positions. In particular this covers the full product if all source primes lie in Q. One can apply this separately to components of the source/prime incidence graph satisfying the support condition: their disjoint prime supports permit union without double counting. A common divisor g of all rows can first be stripped: among the multiples of g in I there is a quotient interval of length M/g. Pad its covering set to at least n positions if needed, then multiply the positions by g. The quotient 1 has no prime demand.

This use of the decreasing-cutoff exclusive kernels builds on [the marking construction](../uniform_three_2026_11_26/MARKED_PRIMES.md). Deleting one occurrence from the active projection and bounding multiplicity by all active-prime multiples in the canonical quotient are what make the exact price bound possible here.

## One common price on arbitrary support (route 3)

Independently of the reciprocal sum, take w_p=w on any chosen support and zero elsewhere. Write N for the total number of active prime occurrences, with multiplicity. For 0≤w≤1/2 the [two-spare inequality](../uniform_three_2026_11_26/TWO_SPARES.md) gives the cap comparison E_I min(wN,1)≤E_J min(wN,2)+o(1). For 1/2≤w≤1 put t=1/w. Because N is integer,

    min(N,t)=(2−t)min(N,1)+(t−1)min(N,2).
    min(N,2t)≥(2−t)min(N,2)+(t−1)min(N,4).

The second inequality is concavity in the threshold. Apply the [binary-price comparison](../cofactor_flow_2026_11_26/MIXED_BINARY_PRICES.md) and the two-spare comparison at w=1/2 to the two terms of the first identity, then multiply by w. This proves the same cap comparison, uniformly also for varying w. The entire interval has at least the canonical total at each prime, whence Φ≤2n+o(M). This suffices at fixed positive density for these price vectors. It does not extend by interpolating two independent prices across a kink of the target cap.

## A signed polynomial for two fractional prices (route 4)

Active labels carry costs c_i>0, and a canonical Boolean profile is feasible if its total cost is ≤1. Suppose every feasible profile has at most three labels. Prices are 1/3 or 3/4. Order labels by nondecreasing cost, breaking ties once. For a heavy (3/4) label q set B_q={earlier heavy p : 2c_p+c_q≤1}. At a Boolean target profile T put k_q=|B_q∩T|, let W be its total price and define

    P(T)=W−(1/4) Σ_{heavy q∈T} [k_q−binom(k_q,2)].

Every nonlinear monomial used is feasible: any two members of B_q have total cost ≤1−c_q. For arbitrary T the bracket is ≤1 for every integer k_q≥0, and zero for the first heavy label. If there are H≥2 heavy labels, P≥3H/4−(H−1)/4≥1. With at most one heavy label P=W. Thus P≥min(W,1) everywhere. On a feasible source all k_q≤2 so the correction subtracts nonnegative amounts. The only overloaded profile has three heavy labels. For its largest q at least the cheaper of the two predecessors is in B_q, hence its bracket is 1. Thus P≤min(W,2) on every feasible source. This gives a signed divisor polynomial even when some pairs or triples are infeasible. It concerns Boolean profiles; the preceding bank proof covers actual prime powers on its stated supports.

For general mixed costs the replay tests 6, 8 and 10 labels without a rank-three restriction. It finds rational coefficients on feasible monomials and checks the two pointwise inequalities on every Boolean profile in rational arithmetic. The sums of absolute coefficients obtained are 47/12, 110/21 and 23/3. These are feasible norms; optimality of the floating-point discovery objective is unnecessary and is not asserted. No uniform control over growing supports follows.

## A density increment necessary for a bad source (routes 7 and 11)

Assume n≤M/2 and M≤n². Write t=n/M, C_d=#{a∈A:d|a}, L_d=floor(M/d), and B=#{a∈A:some p>n divides a}. For every fixed δ>0 and large n, if

    τ(A,I)>2n+π(n)+δ n,

then some d=p^j≤M with p≤n satisfies

    C_d≥sqrt(log n),        C_d/L_d > (1+δ/22)t.                (2)

First, each row counted by B contains just one prime above n, to exponent one. For every such prime independently choose C_p distinct multiples in I, which exist since C_p≤L_p. The union costs at most B, even when different primes share a position.

For the small primes minimize Σ y_b+Σ z_p subject to Σ_b v_p(b)y_b+z_p≥Σ_A v_p, 0≤y_b≤1, z_p≥0. Its LP dual maximizes Φ over prices supported on p≤n in [0,1]. At a vertex at most π(n) position variables are fractional (otherwise perturb them in both directions fixing prime totals). Round them upwards and repair the remaining integer deficits at one position per unit. Those deficits are bounded by the original z_p, and every remaining unit can be found as in the integral argument above. Together with the large primes this proves τ≤B+π(n)+max Φ. In particular the hypothesis supplies a nonnegative dual objective with Φ>2n−B+δ n.

Here is an absolute bound on its price mass. Let μ=Σ w_p/p, Y(u)=Σ w_p 1_{p|u} and let E average over J. The floor counts give E Y≥μ−π(M)/M and E Y²≤μ²+μ, so E(Y−μ)²≤3μ. Total valuation dominance gives Φ≤M−Σ_{J outside A} X. If Φ≥0 then the latter sum of loads is at most M. By Cauchy–Schwarz, s−sqrt(3s)≤1 with s=(1−t)μ. Hence s<5 and μ<10. Also Σ w_p/(p−1)≤μ+Σ_{m≥2}1/[m(m−1)]≤11.

Using (X−1)_+≥t(X−1) pointwise and total valuation dominance gives

    Φ ≤ n + Σ_{p≤n} w_p Σ_{j:p^j≤M} (C_{p^j}−t L_{p^j}).

There are O(n/log n) tested powers: at j=1,2 there are at most 2π(n) by M≤n², and higher j contribute O(M^(1/3) log M). Powers with C_d<sqrt(log n) contribute o(n) to the positive excess. Those with C_d≤(1+δ/22)t L_d contribute in aggregate at most (δ/22)n Σ w_p/(p−1)≤δ n/2. The other powers must therefore carry weighted excess exceeding n−B+δ n/2−o(n), which proves (2). Each resulting fiber has quotient density at least C_d/L_d. This proves a fixed multiplicative gain with a growing number of rows. It provides neither a disjoint covering of almost all rows by such fibers nor a bound on the total cost of lifting their covers.

### How many rows lie on the improved fibers?

Let W be the union inside A of all fibers satisfying (2), and m=|W|. Under the same fixed-gap hypothesis, for large n,

    m log(exp(11/2) M/m) ≥ log(4/3) [n−B+δ n/2−o(n)].
    In particular m ≫_δ n / (1+log(M/n)).                             (3)

Indeed the total weighted excess on the lifted fibers was at least the quantity in brackets. Dropping the negative canonical terms bounds this excess above by Σ_{a∈W}X(a): for each p all counted powers on row a number at most v_p(a).

For u uniform on J, the exponential moment of X is bounded above by that of independent geometric prime valuations with tails p^(−j). To check this directly, expand each exp(s w_p v_p) as 1 plus the sum of its nonnegative increments times 1_{p^j|u}. Products of these divisibility indicators have canonical mean at most the reciprocal of their modulus. Take s=log(4/3). The independent product is

    ∏_p [1−(exp(s w_p)−1)/(p−1)]^(−1) ≤ exp(11/2).

Convexity gives exp(s w_p)−1≤w_p/3. Also −log(1−u)≤3u/2 for 0≤u≤1/3, and the price-mass bound above is 11. Jensen on W now gives Σ_W X≤(m/s) log(exp(11/2) M/m), proving the first inequality. For the second put z=m/n and L=11/2+log(M/n). If z≤c/L, then z(L+log(1/z))≤c[1+log(L/c)/L] by monotonicity; choosing c small in terms of δ contradicts the first inequality.

Thus a fixed fraction of source rows lies on increased-density progressions at any fixed positive density. At n asymptotic to M/log M the guarantee is ≫_δ n/log log M. These are sizes of unions, with each row counted once. No bound on the number of generators of this union, or the cost of covering its complement, is implied.
