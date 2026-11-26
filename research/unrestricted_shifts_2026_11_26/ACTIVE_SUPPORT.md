# Fractional prices on a support of bounded reciprocal mass

Let J=[1,M] and I be any positive interval of M integers. For prices in [0,1] put X(v)=sum_{p<=M} w_p v_p(v). Let Y=floor(sqrt(log M)), Q={p>Y:w_p>0}, and lambda=sum_{Q}1/p. Uniformly if lambda<=1-exp(-1)+o(1),

    E_I min(X,1) <= E_J min(X,2)+o(1).

In particular these dual vectors cannot produce a fixed positive excess at any fixed source density. Prices on the support may vary arbitrarily.

## Reduced loads

Discard all repeat occurrences of primes >Y before computing either cap. Only O(M/Y+pi(M))=o(M) positions in either interval contain such a repeat, independent of shift. Truncate each smaller valuation at floor(log_p Y); again the exceptional fraction is o(1), by splitting at sqrt(Y). The retained small-prime score s is periodic with period D=lcm(1,...,Y)=M^o(1). Write W for the sum of Q-prices as Boolean indicators and h for the indicator of s<1. The caps on discarded positions change by at most two. Sums below are normalized by M.

We use two uniform elementary estimates. For bounded D-periodic f in [0,1], d coprime to D, let m(f) be its period mean. The error in E[f 1_{d|v}]-m(f)/d is at most O(D/M), and also O(1/d+1/M); these bounds apply independently even if f depends on d. For squarefree Q-products d of at most r primes with r fixed, the sum of these absolute errors over d<=M is o(1), uniformly for bounded lambda. For d<=M^(1-eta) use the first estimate. Larger d have a factor p>=M^((1-eta)/r). For each remaining product e the permitted primes in (M^(1-eta)/e,M/e] above that lower cutoff have reciprocal sum O_r(eta)+o(1), by Mertens, and count O_r(M/(e log M)). Sum using sum_e 1/e <=exp(lambda), then take eta to zero. Constants uniform for the choice of active support and bounded functions. Products with one distinguished constituent have multiplicity at most r. Empty products satisfy the estimate directly.

The conditional first moments of W agree on I,J up to o(1) for every bounded periodic weighting, by this estimate for r=1. In particular on s>=1, the target cap 1 is bounded by the source cap 2, up to periodic discrepancy. On s<1 the truncated linear means of s+W agree across intervals. It therefore suffices to compare E_J h(s+W-2)_+ <= E_I h(s+W-1)_+ + o(1).

## Allocation by largest prime

Fix R. Sources with more than R active labels have total contribution to the left bounded by o_R(1), uniformly as R grows, since X's small part is <1 on these rows, and E_J binom(K,k)<=lambda^k/k! for K the number of distinct active labels. For example, E_J K 1_{K>R} <= 2^(-R) E_J K2^K <= 2^(1-R)lambda exp(lambda).

For the remaining sources having at least one label, let p be their largest, T their set of earlier labels, d=product(T), with dp<=M and |T|<R. Define F_T=h(s+sum_{q in T}w_q-1)_+. It is nonnegative, bounded by R and D-periodic. Since w_p<=1, each such row's source hinge is at most F_T. Enlarge its source class to all multiples of dp. Its total contribution is thus at most

    sum_{p,T} m(F_T)/(dp) + o_R(1) [as M grows for fixed R].

The error estimate above applies because dp has unique largest factor p and thus unit multiplicity. On a target allocate a_p=1/[p(1-lambda_<p)] to each p, with lambda_<p=sum_{q in Q,q<p}1/q. Their sum is at most integral_0^lambda du/(1-u)=-log(1-lambda)<=1+o(1). For any one p, the profile below p determines at most one T. If its earlier profile is exactly T, its target hinge dominates F_T. By a union bound its F_T-weighted expectation there is at least the expectation on multiples of d minus the sum of expectations on multiples of dq over earlier q outside T. Here dq<dp<=M. This lower bound is at least m(F_T)(1-lambda_<p)/d, up to divisor errors. The errors after multiplying by a_p and summing are o(1) for fixed R: at each p the products d are unique, dq has multiplicity at most R, and the uniform error lemma bounds the whole sum for this p; then use sum a_p<=1+o(1). The o(1) surplus in allocation is harmless even for unbounded target hinges, since only F_T<=R is used per allocated branch (equivalently divide the a_p by max(1,sum a_p)). Thus the target pays the displayed source bound. Empty-label source rows contribute zero here. First take M to infinity and then R to infinity. This proves the comparison.
