# Unrestricted ordinary-product gap inheritance after removal of all bounded rough-rank rows

Fix an integer R≥1 and 0<δ<1. Let n→∞, let A⊆[1,M] have n distinct elements, and let I be any positive interval of M consecutive integers. Suppose that its actual product-cover number satisfies τ(A,I)>(2+δ)n. Put L=log M and U=log L. Take some sufficiently small fixed γ=γ(R,δ)>0 (in particular γ<1), and put

    y=(log M)^γ.

Let E contain exactly the rows with no prime >4n and with at least R+1 distinct prime bases >y. Then for all sufficiently large n,

    τ(E,I)>2|E|+(δ/2)n.

Here E is cut from original distinct integers, with no multiplicities or quotient projections. The theorem does not claim a gap for any particular divisibility progression. If an ambient max convention is needed a subinterval of I of length max E retains its lower bound. All constants are independent of the interval shift.

## 1. Remove very large primes and obtain an ordinary price witness

At n>M/2 the whole interval is a feasible cover. The existing two-block bound handles M≥(2n)^3, so all work is in M<(2n)^3, in particular n>(1/2)M^(1/3). Remove all rows divisible by a prime p>4n, obtaining A_0. In reverse order restore each removed row by a fresh multiple of h=a/p (remove just one factor, even for a repeated p). There are at least floor(M/h)≥p>4n choices. This fresh position supplies the entire cofactor, leaving at most one remaining ordinary p-unit; if one is required then some unused position supplies it because the whole interval meets every original prime demand. Thus each restored row costs at most two when the pre-existing budget remains below 4n. Contrapositively τ(A_0,I)>2|A_0|+δ n: a cover violating this strict lower bound would return a cover of all A with ≤(2+δ)n≤3n positions.

Use one nonnegative unit-cost slack s_p in each ordinary prime-demand inequality, with genuine uncapped target coefficients v_p(b), position variables 0≤x_b≤1, and total source demand E_p=Σ_{a∈A_0}v_p(a). Only primes ≤min(M,4n) occur, so there are O(n/log n) such constraints. A basic optimum has at most this many fractional positions. Rounding these up leaves at most floor(s_p) units to repair for each p; whole-window dominance supplies each unit if still deficient. Therefore a dual optimum supplies prices 0≤w_p≤1, X(u)=Σ w_p v_p(u), with

    Φ(A_0)=Σ_{A_0}X−T>2|A_0|+(7δ/8)n,       T=Σ_{b∈I}(X(b)−1)_+.

We record bounds on T for choosing the reserved fraction. The canonical exponential-moment proof in [the residual price proof](RESIDUAL_GAP.md) gives T≤C n[1+log(M/n)] and E_[1,M] exp(sX)=O(1) at every nonnegative witness. At an ordinary optimum one can also impose the price caps from [the trimmed-list proof](PRUNED_RESERVE.md): writing D=1+log(M/n), if D>10 log L then w_p≤4 log p/D for every p, and hence T≤4nL/D. Indeed for log p<D/4 take k=floor(D/(2log p))≥D/(4log p); at least floor(M/p^k) targets with valuation ≥k have total supply ≥k floor(M/p^k)≥nL/log p≥E_p. Lowering w_p to 1/k while it exceeds that value lowers the hinge by at least E_p times the reduction and cannot lower the objective. These caps use one coordinate at a time and hold simultaneously. Therefore T≤C n sqrt L in general and T≤C_* n if n≤M^(19/20), with C_* absolute (enlarged for a finite initial range). These estimates still use the same witness. Every actual ordinary cover F of any residual E' costs at least Φ(E') by Σ_{E'}X≤Σ_F X≤|F|+T.

## 2. Fixed global core construction and baseline blue competitors

Write h for the full y-smooth part of a and X_h=M/h; below, X_h always denotes this length, independent of the price load X(u). There are at most (1+log_2 M)^π(y)=M^o(1) possible h, since y=L^γ, with γ<1. For every h>M^(3/4) at most M^(1/4) quotients occur. All these exceptional rows together, even charged their full ordinary price log_2 M each, cost o(n).

We apply the fixed-global red/blue construction of [the two-color proof](BOUNDED_RANK.md) to the remaining G={a∈A_0: at most R primes >y} with h≤M^(3/4). Split the full outside powers greedily by size into balanced v≤w, with v≤sqrt(X_h) and w²≤X_h q for each atom q of w. Take a red candidate b divisible by h v, with b/(hv) free of primes ≤y and coprime to v. Different h have disjoint red banks. For every composite label w (at least two bases) the uncolored blue bank C_w consists of multiples b of w with gcd(w,b/w)=1. Now also assign some repeated singleton labels w=p^j (j≥2) in blue, as specified below; an exponent-one singleton costs one unit of source price directly.

Here c=(log y)/L, L_c=1+log(1/c). The previous uncolored proof gives two uniform bounds, since X_h≥M^(1/4). After deleting at most half of each red bank, its uniform task requests have total load at every surviving site ≤ρ_r, where

    ρ_r ≪_R c L_c^(2R)(1+c log log(3M)).

This is exactly the fixed-label dyadic trimming bound in [the trimmed-list proof](PRUNED_RESERVE.md) (before deleting the half, use full-bank denominators; constants change by at most two on switching to trimmed denominators). All trimmed red banks have polynomial size.

On the full uncolored blue banks, the competitor load at a site b for a task with label w is Σ_{w': gcd(w,w')>1} m_w' 1[b∈C_w']/|C_w'|. Restrict this sum first to COMPOSITE w'. The average over C_w is ≤ρ_b≪_R c L_c^(2R) for every w whose bank has cardinality ≫M/w and whose shared full atoms satisfy w²≤M q. This follows from the earlier global blue estimate: a compatible shared gcd g consists of full atoms; if they share q then lcm(w,w')≤M since w²,(w')²≤M q. Therefore |C_w∩C_w'|≤2M/lcm, and the summand averaged on C_w is ≤C m_w'g/M. At any h bound m_{h,w'}≤C_R L_c^R X_h/(w' log X_h), sum g/w' by selecting a unitary divisor of w in ≤2^R ways followed by a reciprocal sum ≤C_R L_c^R, and then sum 1/(h log X_h)≪(log y)/L over all h. The same proof includes repeated singleton tasks among the queried w because w²≤M w and the shared atom must equal w. Composite w'≤M^(2/3) always.

## 3. Additional repeated singleton requests at n≤M^(19/20)

Put H_0=Q=L^(1/4). For a repeated singleton w=p^j at core h defer it without a blue assignment only when h≤H_0 AND X_h/w≤Q. In this case a=h r p^j with r≤Q, p≤4n. The total ordinary price charged on all such singletons is at most

    H_0 Q Σ_{p≤4n} Σ_{j≥2: p^j≤M} j = O(L^(1/2) n/log n)=o(n).

Indeed p<M^(1/7) contributes at most O(M^(1/7)L²)=o(n/log n), even at n=M^(1/3)/2. For larger p there are at most seven admissible j and π(4n)=O(n/log n). Distinct triples h,r,p^j determine individual source rows, so the displayed overcount is valid.

Every added singleton bank has M/w≥min(H_0,Q)=L^(1/4), and uncolored size ≥M/w−1−(M/(wp)+1)≥M/(2w), uniformly since p>y→∞. Let m_w be its added task count. We claim uniformly in w=p^j

    m_w w/M ≪_R exp(−1/(4γ)) + γ(1+log(1/γ))^R + o(1) =: η.

For h>H_0 count DISTINCT source rows as a=w k, k≤Z=M/w. Since w has no prime ≤y, H_y(k), the full y-smooth part of k, equals h. For uniform k in [1,floor Z], E H_y(k)^(1/log y)≤∏_{p≤y}(1−1/p)/(1−p^(−1+1/log y))≤C with absolute C, uniformly in Z. This follows by nonnegative prime-power divisor increments and Σ_{p≤y}log p/p=O(log y), as in [the residual price proof](RESIDUAL_GAP.md). Thus their count divided by Z is ≤C H_0^(−1/log y)=C exp(−1/(4γ)). Using this normalized smooth-part moment is essential; summing the unnormalized harmonic tail would lose a factor log y.

For h≤H_0 we only add tasks for T=X_h/w>Q. The residual r=a/(hw) is y-rough and has at most R distinct bases. For s=log T/log y≥1/(4γ), the number of such r, divided by T, is

    ≪_R T^(−1/2) + (1+log s)^R / log T.

Indeed ignore r≤sqrt T. From the remaining r choose a full atom ≥T^(1/(2R)), fix its complementary divisor k', then use prime-power counting O_R(T/(k' log T)) for the atom. The k'-reciprocal sum is ≪_R(1+log s)^R by expanding the sums of 1/(p−1) over y<p≤T. For γ small in terms of R the maximum of (1+log s)^R/s on the indicated range is ≤C_R γ(1+log(1/γ))^R. Multiply the T-reciprocal estimates by 1/h and sum over h; the smooth harmonic sum is O(log y). The sqrt error costs O(log y/sqrt Q)=o(1), and the other term gives the stated γ-dependent bound. This proves the claim uniformly in w.


For any fixed queried blue task, at most R added singleton labels have a compatible shared base, precisely its full atoms p^j. At every site their competitor load is at most Σ 2m_{p^j}p^j/M≤2Rη. This includes the queried task's own label and all of its equal-label competitors, even with the shortest allowed bank. Incompatible exponents have disjoint exact banks. On the full blue banks the mean competitor load for any task is now ≤ρ_b+2Rη. Discard sites of competitor load >2(ρ_b+2Rη) to retain at least half of every bank.

Reserve red/blue/unused sites independently with probabilities α/2,α/2,1−α, where α=δ/(128C_*) or smaller, a fixed constant. Choose γ=γ(R,δ) sufficiently small that the displayed η is less than α divided by a sufficiently large constant depending on R for all large M. The probability that a trimmed bank retains <α/4 of its trimmed sites in its color is exp(−Ω(αM/w)) on blue, with the analogous estimate on red. All polynomial-sized red and composite blue banks succeed simultaneously with probability 1−o(1). Individual singleton lists fail with probability ≤exp(−c_1 α L^(1/4)), where c_1>0 is absolute. The expected number of singleton TASKS with failed lists, with multiplicities, is at most n exp(−c_1α L^(1/4))=o(n/L²); no independence among failure events is needed. Markov gives with probability 1−o(1) that their aggregate price is o(n), since each such task has price ≤log_2 M. Simultaneously the hinge of all reserved sites is ≤4αT with probability ≥3/4. Fix such a coloring; drop these failed singleton tasks, leaving their red assignments in place.

The uniform fractional red placement has total load ≤Cρ_r/α<1 on each site. Integral Hall therefore gives distinct red representatives. For each retained blue task place it independently uniformly on its retained list. Conditioned on its own site, the aggregate probability of collisions with tasks sharing a base is ≤C(ρ_b+2Rη)/α<1/8 for large M. Apply the asymmetric local lemma to pair collision events, taking x_event=2Pr(event). Independence holds for events with disjoint task variables and the sum of neighboring x is ≤1/2. This also covers repeated copies of one short singleton label: their collision probability is the reciprocal retained bank size, and pointwise their total is included in the same bound. Nonconflicting blue tasks at the same site have disjoint bases.

## 4. Dense upper range and passing to the residual

For n>M^(19/20) discard h>sqrt M at an o(n) ordinary price cost by the same count of smooth cores. Use the same red and blue construction with α=δ/(128 C sqrt L). Here assign ALL repeated singleton labels w≤M^(1/6) as ordinary blue tasks; since X_h≥sqrt M, X_h/w≥X_h^(2/3), their bounded-rank multiplicities per h satisfy exactly the composite bound, hence ρ_b≪_R c L_c^(2R) including all such tasks. All lists have polynomial size. Larger repeated singleton powers have total price O(M^(11/12)L³)=o(n), by the upper bound O(T^(1/2)log M) for the count of p^j≤T with j≥2 and dyadic reciprocal summation beyond M^(1/6). Thus ρ_b/α,ρ_r/α→0, since c=(log y)/L and L_c=O(U). All red/blue lists succeed simultaneously; the same Markov, Hall, and local-lemma argument applies.

In either range G consists of all low-rank rows removed from A_0. Among their paid positions, red sites are distinct, blue duplicates use disjoint bases, red and blue are disjoint colors. Each assigned red site pays all prime valuations of its h and v; a blue site pays each of its credited labels simultaneously since they are pairwise coprime. Source price beyond these credits costs at most one per deferred exponent-one singleton plus o(n) for the exceptional and failed cases enumerated above. Thus Σ_G X≤2|G|+4αT+o(n). Subtract from the unchanged original witness: Φ(E)=Φ(A_0)−Σ_G X>2|E|+(δ/2)n. Weak duality for the actual product now proves the claim.

The statement is compatible with typical integer statistics: it forces every row of a genuinely bad residual to retain many distinct growing primes but gives no contradiction for such residuals. At fixed positive density and polylog density, the earlier fixed-global results in [the residual price proof](RESIDUAL_GAP.md) and [the trimmed-list proof](PRUNED_RESERVE.md) yield much larger prime cutoffs.

For the bounded-rank count used in the singleton estimate one may split the residual quotient at its square root. Above that boundary one of its at most $R$ full prime-power factors has size at least $T^{1/(2R)}$. After fixing the product $k$ of the other full factors, the prime-power counting upper bound gives $O_R(T/(k\log T))$ options. The reciprocal sum over the available $k$ is $O_R((1+\log(\log T/\log y))^R)$ by expanding the reciprocal prime-power sum for bases between $y$ and $T$. Below the boundary there are at most $\sqrt T$ choices. In the application $T>(\log M)^{1/4}$ and $\gamma<1/4$.
