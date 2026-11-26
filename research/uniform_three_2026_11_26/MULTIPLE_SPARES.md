# Several spare primes in the fractional-price comparison

Use J=[1,M] and a positive interval I of M consecutive integers. For prime prices in [0,1] let X be the sum of prices weighted by the prime valuations at a position. A core of primes up to y=M^o(1), with y tending to infinity, may have arbitrary prices. Assume all other nonzero prices have support Q in (M^a,M] for fixed a>0. Fix an integer k≥1. For p∈Q with p≤sqrt M assume w_p≤1/k. There is no additional bound on prices above sqrt M. Let t be a nonnegative number satisfying

    (t-e)^k / k! ≤ max over odd 1≤j≤k of T_j(e)   for every 0≤e≤t,
    T_j(e) = sum_{i=0}^j (-e)^i/i!.

If the reciprocal mass of Q up to M^((1-ka)/2) is at most t+o(1), then

    E_I min(X,1) ≤ E_J min(X,2) + o(1),

uniformly in the shift. This controls the boxed dual in the positive-density regime for an optimizing vector satisfying the conditions. It does not impose the conditions on arbitrary optimizers.

For k=1 take t=1. Full active support above M^a is allowed when a≥1/(1+2e), where e here is Euler's number. For k=3 take t equal to the real zero of 1−t+t²/2−t³/6 (between 1.59 and 1.60). Indeed T_3(e)−(t−e)^3/6 is concave in e for t>1 and nonnegative at both ends, since t³<6. All primes above M^a may be active when a≥1/(3+2 exp(t)), approximately 0.0778, with prices at most 1/3 through sqrt M and arbitrary thereafter. In general all support is allowed when a≥1/(k+2 exp(t)), by the prime reciprocal estimate. If k is large one can take t=c k for any fixed c>0 satisfying c+1+log c<0. For the largest odd j≤k, Taylor's formula gives T_j(e)≥exp(−e)−e^(j+1)/(j+1)!, and Stirling shows that the sum of the latter error and (t−e)^k/k! is o(exp(−c k)) uniformly on [0,c k].

## Proof

Use the [one-spare-prime proof](../unrestricted_shifts_2026_11_26/MACROSCOPIC_PRICES.md) to reduce to the ordered hinge increments for a current prime q∈Q. After subtracting the core, at a fixed point of integration one needs to dominate the canonical event that q is present and its earlier Q-load exceeds 1+u by the target event that q is present and its earlier Q-load exceeds u, with 0≤u≤1. Dependence on the core enters only through bounded eligibility functions. Earlier Q-primes on a canonical row with q are all below sqrt M because they are smaller than q and divide its cofactor. Thus each has price at most 1/k.

For a counted canonical row let B be the shortest increasing prefix of its earlier present Q-primes whose load exceeds u. Put r=max B and d=q times the product of B. Removing the last k earlier primes reduces the earlier load by at most one, hence B omits at least k further earlier primes. Let L_B consist of all Q-primes that can occur in a tuple of k distinct primes of Q in (r,q) whose product times d is at most M. Retain B only if some such tuple exists. Upper bound the canonical event assigned to B by the sum of its feasible k-tuple indicators, with the divisibility of d included. The reciprocal sum per prefix, after the factor 1/d, is at most l^k/k! for l=sum_{p in L_B}1/p.

As in the one-prime proof the target prefix is uniquely B if d divides the position, its load crosses u at r, and each p in E_B={p∈Q:p<r, p not in B} is absent. For every subset of E_B of size at most k the product times d is ≤M, because every member is smaller than each of the k available continuations. Bonferroni at any odd order j≤k therefore bounds the target probability from below by T_j(e)+o(1) after division by the common factor 1/d, where e=sum_{p in E_B}1/p. The error in replacing the elementary symmetric sums by e^i/i! is o(1) uniformly, since the mesh is at most M^(-a), e≤log(1/a)+O(1) and k is fixed. The order j can be chosen separately for each B.

For any p in L_B a feasible continuation containing it includes k−1 other primes >M^a, at least one prime of B >M^a, and q>p. Hence p² M^(ka)<M. Every member of E_B is yet smaller. The disjoint masses thus satisfy e+l≤t+o(1). The stated polynomial inequality gives the required comparison prefix by prefix, and target prefixes are disjoint.

For clarity the arithmetic comparison does not require relative errors for individual moduli. The normalized total errors are o(1) after summation. All coefficient functions are bounded functions of the smooth core; every divisor includes at most floor(1/a) macroscopic primes and occurs with bounded multiplicity. The total reciprocal mass of these divisors is bounded in terms of a. Up to M^(1−η) the uniform core histogram comparison on quotient intervals permits replacement by geometric core means times reciprocal divisor with aggregate error o(1). In (M^(1−η),M] the reciprocal sum is O_a(η)+o(1), by fixing all prime factors but one and using Mertens for that last prime >M^a. Their number is O_a(M/log M), by the prime counting upper bound after fixing the other factors. Hence both the real counts and comparison contributions from this strip have aggregate normalized size O_a(η)+o(1). Let η decrease to zero. Dropping repeated macroscopic prime levels changes capped means by o(1), since positions hit by any such square have proportion at most sum_{p>M^a}1/p²+π(M)/M. This completes the comparison.
