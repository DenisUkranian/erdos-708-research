> CORRECTION, 24 November 2026: the user subsequently supplied a valid full-prefix active-part counterexample with deficit Theta(M^(10/17)). The searches below are historical negative searches and missed the tiny-positive-background support mechanism. They do not support the unrestricted transfer conjecture.

# Checks of the hyperbolic certificate and the unproved aggregate transfer

These checks do not calculate g(n), do not optimize the original raw covering problem, and do not prove the remaining arithmetic inequality.

## Exact verification

`check_hyperbolic_certificate.py` independently evaluates all subset maxima with Fraction arithmetic. It checks 4,742 weighted-size profiles, including exhaustive n<=3 inputs from weights {0,1/4,1/2,3/4,1} and sizes {1,2,5}; 1,120 larger random rational profiles; and seven source-sharp families with 2k equal-size occurrences. It also verifies the exact ambient-prefix obstruction M=18,w2=w3=1,I=[9,26]. All checks pass. Uniform validity follows from the written proof, not from these finite checks.

## Exploratory arithmetic transfer searches

The tested candidate was the stronger whole-prefix inequality

    sum_{a<=M} K_{h(a)}(a) <= sum_{b in I} K_M(b),

and also its version using K_a(a). Both unrestricted full-prefix versions have now been disproved by the user's construction; the searches below predate that correction. All target phase arrays in the following searches are realizable by actual intervals through CRT; the extra lift avoids valuations above floor(log_p M)+1. Computation uses doubles and is exploratory, not an exact certification of every candidate.

1. A bounded-shift probe used M=18,20,24,30,36,48,60,80,100, two hundred random profiles per length, and shifts up to twenty thousand. No actual-size source violation was found.
2. `probe_crt_kernel.cpp` tested 74 nontrivial structured profiles at M=300,1000,3000,10000. Prices were .4,.5,.6,.75,1 on bands [M^alpha,M^(alpha+.23)], with alpha=0,.12,.2,.27, sometimes with an additional price .75 at prime2. Each case used80 independent phase patterns and300 phase-coordinate improvements. No violation of either active-part or actual-size prefix transfer was found.
3. `probe_crt_random.cpp` tested618 heterogeneous profiles at M=60,100,180,300,600,1000,3000. Prices came from {.1,.2,...,1}, with random supported primes up to M^beta, beta in [.25,.65]. Cases with M<=180 used two complete coordinate sweeps over every capped residue of each active prime; larger cases used500 phase-coordinate improvements after50 independent patterns. No violation was found.
4. `probe_crt_joint.cpp` jointly optimized prices and phases from96 starts at M=60,90,120,180. The source kernel sum was constrained to be at least .5 to exclude the trivial zero vector. There were up to eight alternating rounds, with prices on the grid {0,1/12,...,1}, exhaustive capped residues in each prime coordinate, and additional price changes by1/60 or1/120. The largest observed source-minus-target difference was -.1. This was a local alternating search, not a certified global maximum.

These experiments did not resolve the aggregate arithmetic transfer. The subsequently supplied counterexample disproves the unrestricted actual-size and active-part full-prefix formulations as well. Only the own-full-tail, reserve-corrected target remains open here.
