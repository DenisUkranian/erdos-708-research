# A smooth-number reserve for every fractional price above the seventh root

Let J=[1,M], let I be any interval of M positive integers, and write X(b)=Σw_p v_p(b), with prices in [0,1]. Prices may be arbitrary at p≤y=M^o(1) and p>M^(1/7), with zero prices between these sets. Then uniformly over all choices and shifts,

    E_I min(X,1) ≤ E_J min(X,2) + o(1).

This gives the coefficient two for these dual vectors at positive source density, subject to the original rounding error. The result uses a buffer of canonical positions with only small factors or an incompatible large factor. The numerical constant in the last analytic inequality is certified by [integer arithmetic](verify_smooth_reserve.py).

## Difference between the two prefix counts

Use the [ordered prefix argument](../unrestricted_shifts_2026_11_26/MACROSCOPIC_PRICES.md). The positive-price primes above M^(1/7) form Q. Powers above the first may be discarded for this capped comparison at a normalized cost o(1). In a contributing source prefix write q for the current prime, B for the nonempty shortest earlier prefix crossing the target threshold, r=max B, and d=q times the product of B. On every counted canonical row the next present earlier prime can be chosen in L={p∈Q:r<p<q, dp≤M}. Only retain B with L nonempty. The excluded set is E={p∈Q:p<r,p not in B}. Dividing a multiple of d by d leaves, on the source interval, a quotient up to H=M/d. Write e, l for the reciprocal masses of E,L. As in the cited argument, the target event for B requires d and absence of E; the canonical event is contained in d times absence of E and presence of at least one L. Core and prefix eligibility factors are common to both and nonnegative.

For any fixed B, at the level of reciprocal main terms, the desired comparison follows if either e+l≤1, or the canonical proportion of H-quotients with no E or L is at least the reciprocal mass of all *feasible pairs* of distinct E-primes (pair product ≤H). Indeed the first condition is the earlier union bound. For the second, the canonical upper event has proportion at most 1−Pr_J(E hit)−Pr_J((E∪L) not hit). The target lower event has proportion at least 1−Pr_I(E hit). Single E-prime terms have identical reciprocal main terms. By the union bound on the target and two-term Bonferroni on the source, their difference is at most the sum over compatible pairs from E. The comparison is used only on d-multiples and with the common core factors. The aggregate justification below applies to each of these counts.

Put Y=M^(1/7), and measure logarithms in base Y. Set t=log_Y r, h=log_Y H, and v=log_Y q. We have h+v+t≤7 and every prime in E∪L is at most min(H,q). Hence e+l≤log(min(h,v))+o(1) by Mertens. If min(h,v)≤exp(1), the first condition works up to o(1). Otherwise

    1≤t≤7−2 exp(1),    h≤7−exp(1)−t,    u₀=(7−t)/2 ∈ [exp(1),3].

## Canonical positions paying for the error

Let ρ be the Dickman function. The canonical proportion of quotients whose prime factors are all ≤Y is ρ(h)+o(1), uniformly for the bounded exponents here. This follows directly from finite inclusion-exclusion over primes >Y, the prime reciprocal estimate, and Riemann sums. If h≤u₀ this gives at least ρ(u₀)+o(1) by monotonicity.

If h>u₀, then v<u₀ and h−u₀<1, since h≤7−exp(1)−t and u₀≤3. Additional disjoint canonical positions have a prime >Y^u₀; their remaining cofactor is at most Y. Thus they avoid E and L, their large prime is unique, and their proportion is log(h/u₀)+o(1). Since −ρ'(z)=ρ(z−1)/z≤1/z for z>1, the two contributions again give at least ρ(u₀)+o(1).

The canonical proportion allowed for the source E-pair error is at most

    P(t)=½ ∫_{1≤x,y≤t, x+y≤7−exp(1)−t} dx dy/(xy) + o(1).

This uses the prime reciprocal theorem and the fact that a pair dividing a canonical quotient has product at most H. For u₀∈[exp(1),3], inclusion-exclusion gives

    ρ(u₀)=1−∫_1^u₀ dx/x + ½∫_{x,y≥1, x+y≤u₀} dx dy/(xy).

The accompanying script certifies ρ(u₀)−P(t)>0.003 on the whole interval 1≤t≤7−2 exp(1). It rounds exp(1) down to 2.718, bounds each exponent by the enclosing cells of width 1/2000, and multiplies rational lower or upper cell masses. Only rectangles wholly inside the positive triangle are added. All rectangles that can intersect the negative pair region are subtracted. Since the upper and lower integral bounds use integers throughout, the final strict slack also absorbs the o(1) main-term errors.

## Transfer with the core and varying d

All the smoothing and pair computations can be made after summing over prefixes. More explicitly, expand the canonical Y-smooth predicate by inclusion-exclusion over all primes >Y dividing the quotient, up to the largest degree with product ≤H. Its main term is the alternating reciprocal sum over the same feasible tuples. This tends to ρ(h) uniformly in the bounded range of h, by Mertens and Riemann integration over simplices in the variables log_Y p. The main terms for the additional large prime and the E-pair upper bound follow from the same one- and two-dimensional estimates. Each coefficient after the hinge integration is a bounded function of the prefix and the small-prime core. For each term, all additional quotient divisors involve macroscopic primes and are coprime to the core, so quotienting the source on the resulting modulus leaves the same core profile. Each product divisor counted at a given degree is ≤M and has O(1) representations here (including the case of coincidence of a quotient prime with a divisor of d). The sum of their reciprocals is O(1). For moduli ≤M^(1−η) with η>0 fixed, the subpower smooth-profile comparison gives aggregate error o(1) after normalization by M. For moduli in the remaining strip the normalized aggregate counts are O(η)+o(1), by fixing all prime factors but one, applying Mertens and the prime counting upper bound to that last prime, as in the original prefix proof. For repeated prime factors in moduli, their aggregate reciprocal mass is o(1) and count is o(M): an occurrence of p² with p>Y gives at most MΣ_{p>Y}1/p² many possible integers. Sending η to zero completes the transfer. The disjoint target prefix events then give the claimed comparison.
