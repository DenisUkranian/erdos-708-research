# A dense-regime hinge comparison for arbitrary binary prime prices outside a small core

Let I be any interval of M positive integers and J=[1,M]. Put X(v)=sum w_p v_p(v) over primes through M, with 0≤w_p≤1. Uniformly in the interval and these prices, if all prices beyond Y=floor(sqrt(log M)) are binary, then

    E_I min(X,1) ≤ E_J min(X,2) + o(1).

Here E is the average over all M positions. Consequently the source hinge above 2 minus the target hinge above 1 is o(M) from above, since the total target valuation at every prime dominates the source total. For any set A of n sources the boxed covering dual objective at these prices is ≤2n+o(M). For n/M bounded below this is 2n+o(n). This statement leaves unrestricted fractional dual prices open. All estimates below are uniform. No priority claim is intended.

Let Q be the active primes beyond Y, N(v) count the distinct Q-primes dividing v, h_p=1/p, and μ=sum_Q h_p. Repetitions can only increase the source cap; on the target a single such occurrence already saturates the cap of one.

**Large mass.** Put u=3−sqrt(3). If μ≥u choose a subset with total mass μ' in [u,u+1/Y]. Write K for the distinct-label count on that subset. E_J K≥μ'−π(M)/M; E_J binom(K,2)≤(μ')²/2 because source counts are floors. The integer inequality min(k,2)≥k−binom(k,2)/3 holds for every k≥0. Hence E_J min(X,2)≥μ'−(μ')²/6−o(1)≥1−o(1), sufficient for every shift.

**The small core.** Henceforth μ<u. Let s be the contribution from p≤Y. We may truncate each such valuation at floor(log_p Y) when evaluating bounded caps. Indeed the exceptional proportion in either interval is ≤sum_{p≤Y} p^(−1−floor(log_p Y)) + π(Y)/M = o(1): split at sqrt(Y), bounding the two sums by sqrt(Y)/Y and sum_{m>sqrt(Y)} m^(-2). After truncation s is periodic with period D=lcm(1,...,Y)≤Y^Y=M^o(1). Put h=(1−s)_+ and m the period mean of h. By periodicity E_I min(s,1)=E_J min(s,1)+o(1). On integer loads N,

    min(s+N,1)=min(s,1)+h min(N,1),
    min(s+N,2)≥min(s,1)+h min(N,2).

For s≤1 the latter follows by checking N=0,1,≥2; for s≥1 it is immediate. It suffices to prove E_I h min(N,1)≤E_J h min(N,2)+o(1).

**Counting moments with h.** In sums of counts of divisibility by d≤M that are products of at most three distinct Q-primes, with each d counted O(1) times and bounded coefficients, replace E_I[h 1_{d|v}] or E_J[h 1_{d|v}] by m/d with total absolute error o(1). The statement includes arbitrary restrictions on the family of d. Fix 0<η<1/4. For d≤M^(1−η), the quotient runs through consecutive integers and d is coprime to D; h(dk) therefore has period D and mean m. Its count error is O(D/M) per d; these errors sum to o(1). For M^(1−η)<d≤M, at least one prime factor p is ≥M^((1−η)/3)≥M^(1/4). Fix the remaining product e (including e=1). Its possible reciprocal mass sum is bounded uniformly by 1+μ+μ². In the range M^(1−η)/e<p≤M/e with p≥M^(1/4), the sum of reciprocal primes is O(η)+o(1), uniformly in e, by the prime reciprocal Mertens estimate (both endpoints clipped to [M^(1/4),M]). Thus the boundary reciprocal sum is O(η)+o(1). The number of boundary products is O(M/log M) by summing π(M/e)≪M/(e log M) in the same range. Each interval count per d is at most 1/d+1/M. First take M→∞, then η→0. In particular the linear moments E_I hN and E_J hN differ by o(1).

**Ordered increments.** Order Q by increasing p and write cost x_p=log_M p. For a current label q write N_< for the count of present predecessors. Telescoping gives the source increment of (N−2)_+ as 1_{q|v}1_{N_<≥2}, and the target increment of (N−1)_+ as 1_{q|v}1_{N_<≥1}. On a source divisible by q, every present predecessor p belongs to the compatible set p<q with x_p≤1−x_q. Partition this set into C_q with x_p≤(1−x_q)/2 and L_q the rest. At most one L_q label can be present. Put b_q=sum_{C_q} 1/p, l_q=sum_{L_q} 1/p, t_q=b_q+l_q.

On the source the event of at least two predecessors is bounded by the count of cheap-cheap pairs plus cheap-expensive pairs. For the latter count only feasible triples p p' q≤M; the other triples never occur. On the target the event of at least one predecessor is bounded below by the count of C_q singletons minus the count of C_q pairs. All these divisors times q are ≤M. The replacement just proved applies simultaneously (q is the largest label of each tuple, and each tuple has bounded multiplicity). Bounding the compatible source sums by the full reciprocal products, the source hinge minus target hinge, weighted by h and divided by M, is at most

    m sum_q (1/q) [b_q²/2 + b_q l_q − b_q + b_q²/2] + o(1)
      = m sum_q (1/q) b_q(t_q−1) + o(1).

Define T_q=sum_{p<q}1/p, c=sum_{x_p≤1/2}1/p and a=sum_{x_p≤1/3}1/p (all sums restricted to Q). In every case t_q≤min(c,T_q). If c≤1 all terms are nonpositive. If c>1 then a≥c−log(3/2)−o(1)>0.59 eventually, since this bounds the mass between exponents 1/3 and 1/2. For x_q≤1/3 every predecessor is cheap: b_q=t_q=T_q. The first 0.59 units of reciprocal mass therefore contribute at most integral_0^0.59 t(t−1)dt+o(1)<−0.105; the mesh is at most 1/Y. All positive contributions lie beyond T_q=1 and have size at most integral_1^u t(t−1)dt+o(1)<0.044 (on all other labels use b_q≤T_q). This leaves fixed slack. Thus the weighted hinge difference is ≤o(1). Converting these integer hinges back to caps uses the equality of the two linear moments up to o(1), proved above. This completes the claim.

The proof controls absolute o(M), with no sparse relative rate. For extensions to near-binary bulk prices one must handle arbitrary high target valuations before applying any supposed L1 continuity. Without additional truncation it is safe to state just the binary theorem.
