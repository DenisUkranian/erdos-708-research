# Re-optimizing the project's density-independent 0.3168 certificate

Let t=n/M have a fixed positive limit, with t≤1/2. Using §2 of the project's [density proof](../density_2026_11_26/PROOF.md), write W for its middle-prime load, V=Var_J W, x=(μ−1)_+, m=(1−μ)_+, and a=max(x,G) for the target hinge lower bound. Set E=B_L+B_Q+B_ν+ν²+D. The report gives

    Φ/M ≤ t + Cov_J(1_A,W) −(1−t)a+o(1),  V≤μ−E+o(1).

The [prior verification script](../density_2026_11_26/verify-variance.js) is the DENSITY-INDEPENDENT, variance-only certificate (there is no source bonus R, as confirmed in the final paragraph of §4):

    m+E+x+2(G−x)_+ = m+E−x+2a ≥ 0.3168.

In particular V≤s+2a+o(1) with s=1−0.3168=427/625. This holds regardless of t; the cited report needed the certificate only above t=0.406, but the independent inequality does not use that restriction. The Cauchy–Schwarz inequality now gives

    Φ/M ≤ t+sqrt(t(1−t)(s+2a))−(1−t)a+o(1).

When t≤s/(1+s)=427/1052, the displayed function of a≥0 is nonincreasing and is maximized at a=0. Thus

    τ/n ≤ 1+sqrt((427/625)(1−t)/t)+o(1).

This is a re-optimization of the existing density-independent certificate, distinct from the elementary bound H≤3n/2+M/4 and using earlier numerical work. It beats the unrestricted three-per-row result for t>427/2927 (~0.1458832). For t=1/5,1/4,1/3 the bounds are respectively 1+2 sqrt(427)/25, 1+sqrt(1281)/25 and 1+sqrt(854)/25. At t≥0.396 the project's published coefficient two for the ordinary cover is stronger. Repeating that proof verbatim for the grouped level-cover replaces its small-prime valuation load by a nonnegative monotone small-profile load, if the extension is separately recorded. The elementary H-bound needs no such extension.

## Using the .3960 certificate at other densities

Let r=t/(1−t), r0=20980/32000=1049/1600, c1=1−.3444=1639/2500. For t≤12720/32000 and s≥1 with sr≥r0, replace the original squared remainder by

    R_s=E_J [W−E_J W−s(1_A−t)/(1−t)]².

On J outside A its distance at a load threshold a_i is (a_i−μ+sr)_+² up to o(1). Every difference in the telescoping threshold lower bound is nondecreasing in sr: the derivative of (b+c)_+²−(a+c)_+² is nonnegative for b≥a. Removing A in the Bonferroni probability estimate costs at most t≤12720/32000. These are the only two uses of density in the density-dependent certificate, as seen in PROOF.md §4, SPLIT-TRIPLES.md and verify-3960.js. Thus the exact unchanged certificate bounds Γ_base+R_s≥.3444. Its cross terms depending on D, mixed target charges and the subsequent parameter-box argument are unchanged. As above V−R_s−2a≤c1+o(1). Expanding the square now gives the exact covariance identity

    Cov_J(1_A,W)=(1−t)(V−R_s)/(2s)+st/2.

Since s≥1 and a≥0,

    τ/n ≤ 1 + s/2 + c1/(2sr) + o(1).

Set s=max(1,r0/r,sqrt(c1/r)) to minimize the right side subject to the indicated conditions. In particular at t=1/3 this gives 3617969/1678400≈2.155606. The strict threshold for getting less than 2 in the branch s=r0/r is t>1100401/2778865≈.39598937. This changes the previously quoted 39.60% threshold only marginally; it is the quantitative open-density curve that is more significant. As in the existing theorem, a fixed strict margin absorbs rounding, so the integer statement τ≤2n is then exact for all large M. At equality one may claim only the asymptotic coefficient two. In the interior branch s=1 the original certificate gives the existing higher-density conclusion.
