# A reciprocal comparison for Boolean knapsack moments

Let positive costs c_i and budget B specify feasible subsets by c(S) <= B. Suppose random U is feasible, V is arbitrary, and for every feasible S, Pr(S subset U) = Pr(S subset V). Discard infeasible singletons when treating reciprocal losses: none occur in U and extra V coordinates only decrease a reciprocal (for a full cap comparison, restrict attention to individually feasible labels, or assume their inclusion probabilities are all matched). Let a>0 and 0<=w_i<=a. Write X=sum of the selected weights. Then

    E[a/(a+X(V))] <= E[min(1,2a/(a+X(U)))].

## Proof

Fix t>0 and sort coordinates from most expensive to least, breaking ties arbitrarily. Write y_i=exp(-tw_i), z_i=1-y_i. Construct a multilinear polynomial Q with feasible monomials, majorizing the product of y_i over present coordinates. Start at Q=1. When adding coordinate j, let q_S denote the current coefficient. If S+j is feasible, pair q_S with -z_j q_S at S+j, exactly multiplying that contribution by 1-z_j 1_j. If S+j is infeasible, keep q_S if nonnegative and replace it by y_j q_S if negative. This is the larger of q_S and y_j q_S, so it upper bounds the exact multiplication for both states of j. All coefficients keep sign (-1)^|S| or are zero. Induction proves global majorization. Consequently E exp(-tX(V)) <= E Q(V) = E Q(U).

Fix a feasible row U of size m. At an absent coordinate j, the only possible boundary subset S of the already-present row R is S=R: if i were in R outside S, c_i>=c_j and c(S)+c_i>=c(S)+c_j>B, contradicting feasibility. At a present coordinate there are no boundary subsets anywhere inside the current row, as the extended row is feasible. Thus conditional on this fixed row the entire reserve can be described exactly.

List its coordinates in processing order as i_1,...,i_m. For k=1,...,m, let d_k be zero for even k and otherwise the sum of weights of absent j between i_k and i_{k+1} (or after i_m at the last stage) such that c({i_1,...,i_k})+c_j>B. Write L_k=d_1+...+d_k, L_0=0. The coefficient of the k-prefix at its creation has magnitude exp(-t L_{k-1}) product_{l<=k} z_{i_l}: it is born by multiplication of the previous prefix coefficient, whose magnitude was damped by exactly exp(-td_{k-1}) since its creation. Clipping within the k-th gap adds its magnitude times (1-exp(-td_k)) to the polynomial's value on the row. Each subsequent present coordinate scales this already-accrued value by y_i. Therefore

    Q(U) = exp(-tX(U)) + sum_{k=1}^m
           (exp(-tL_{k-1}) - exp(-tL_k)) K_k(t),
    K_k(t) = product_{l<=k}(1-exp(-tw_{i_l})) product_{l>k}exp(-tw_{i_l}).

The base term and the K_k are probabilities of disjoint binary strings (all failures, or exactly a successful prefix followed by failures); hence Q(U)<=1.

Integrate against a exp(-at)dt on (0,infinity). Let F_k(D) denote the integral of K_k(t)exp(-tD). Drop zero-price coordinates (their contribution to either load is zero, and the marginal laws on the positive coordinates still agree); thus F_k(0)>0. The ratio K_{k+1}(t)/K_k(t)=exp(tw_{i_{k+1}})-1 is increasing. This implies R_{k+1}(D)<=R_k(D) for D>=0, where R_k(D)=F_k(D)/F_k(0): reweighting a distribution by an increasing function decreases its mean of the decreasing function exp(-Dt), by the covariance sign inequality. Since R_k(0)=1, the sum over k of [R_k(L_{k-1})-R_k(L_k)] is at most one by telescoping with that order. The integrated reserve is consequently at most max_k F_k(0).

Set x=exp(-at), s=sum_{l>k}w_{i_l}/a, h=sum_{l<=k}w_{i_l}/a<=k. Then

    F_k(0) = integral_0^1 x^s product_{l<=k}(1-x^(w_i/a)) dx
            <= integral_0^1 x^s(1-x)^k dx
            = [1/(s+k+1)] product_{j=1}^k [j/(s+j)]
            <= 1/(s+h+1) = a/(a+X(U)).

Together with the integrated base and Q(U)<=1, this proves the assertion, including the row U empty, where the reserve is zero.

## Application to equal prices

Assume all positive prices equal and scale to 1; for this statement the thresholds after scaling are 2 on the source and 1 on the target. For each coordinate i with positive inclusion probability, condition on i being present. The residual source profile is feasible for budget B-c_i; inclusion moments for its feasible sets still match, since the corresponding moments with i attached match and the inclusion probabilities of i agree. Additional individually incompatible labels on the target can simply be ignored for an upper bound on a reciprocal. Apply the displayed theorem with a=1 to the residual. Sum the inequalities weighted by Pr(i present). Every nonempty target row of size m contributes m/m=1, and every nonempty source row contributes m min(1,2/m)=min(m,2). This proves Pr(V nonempty)<=E min(|U|,2). With matching first moments it is equivalently the global unweighted hinge comparison. The separate archived binary Rosser result gives the corresponding arithmetic inequality with prime multiplicities and finite-interval remainders.

The conditional comparison here is smooth. In contrast, replacing the conditional reciprocal by 1_{X>s} and shifting the source threshold by one fails on the 14-row example.

## An arithmetic consequence with arbitrary primes, powers and interval shifts

Fix a>0 and allow arbitrary 0<=w_p<=a, depending on M. For X(t)=sum_{p<=M} w_p v_p(t) and a positive interval I of M consecutive integers, the preceding argument gives uniformly

    sum_{b in I} a/(a+X(b))
        <= sum_{u<=M} min(1,2a/(a+X(u))) + o(M).

For Boolean prime indicators use c_p=log p and B=log M. The monomials are exactly indicators of divisibility by squarefree d<=M. The integrated coefficient at d has absolute value at most the integral against a exp(-at)dt of the product of (1-exp(-tw_p)) for p|d, since boundary replacements only damp magnitudes and internal copies multiply by z_p. It is <=1/(1+omega(d)) by the substitution used in the proof. Each divisor count differs by at most one between the two intervals, and sum_{d<=M}1/(1+omega(d))=o(M). To see the last statement, first restrict omega to prime divisors among a fixed initial set, then let M grow: by CRT their indicators are asymptotically independent with probabilities 1/p. As the set of primes grows this count tends to infinity in probability, by divergent mean and variance bounded by its mean. This bound on the normalized discrepancy is independent of the active set, weights and shift.

For full powers fix y and K. Classify each integer by its residue modulo L=product_{p<=y}p^K. On each class r the small-prime load truncated at K equals s_r. Use the kernel at parameter a+s_r for the large-prime indicators, multiplied by a/(a+s_r). An arithmetic monomial of the construction on this class is the intersection of a fixed residue modulo L and divisibility by a squarefree d<=M made up of primes >y; CRT again gives count discrepancy at most one. The total discrepancy over the L classes is o_{y,K}(M). The target kernel only decreases when discarded prime powers are restored. The normalized prefix load lost on average is at most

    sum_{p>y} 1/[p(p-1)] + sum_{p<=y} 1/[p^K(p-1)].

For the small-prime sum the omitted exponents start with K+1. The right-hand capped reciprocal is Lipschitz in normalized load and the capped class bound min(a/(a+s_r),2a/(a+X_truncated)) is at most min(1,2a/(a+X_truncated)). First let M grow with y,K fixed, then choose y and K to make the lost load arbitrarily small. This proves the stated o(M) uniformly.
