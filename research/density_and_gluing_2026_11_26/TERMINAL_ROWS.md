# Peeling near-terminal pair fibers at their exact two-position budget

Let J=[1,M], I=(x,x+M] in positive integers and A⊂J consist of n distinct rows. Fix K>0 and n≥M/(log M)^K. Write L=log M, D=log L, H_0=exp(L/[D(log D)^2]). Remove every row a=h p q with h≤H_0, H_0<p<q primes, and write E for this set, R=A\E. These two large prime factors are unique. For either ordinary product cover τ or the stronger prime-power level number H, uniformly in A,I,

    C(A,I) ≤ C(R,I)+2|E|+o(n)

provided C(R,I)=O(n), as ensured by the project's uniform three-per-row bound. For fixed-gap inheritance this proviso may instead be treated trivially if C(R,I)>3n. In particular a fixed-gap counterexample descends to its complement. All counts use the original ambient M.

## Uniform cofactor expansion

Give a row the neighborhood of targets divisible by hp whose exact part supported on primes ≤H_0 is h. Different h have disjoint neighborhoods. Fix h, put U=M/h and restrict to any nonempty row subset. Let P be the set of its smaller prime factors p and λ=Σ_P 1/p. Since p≤sqrt U, π(U/p)≪U/(pL) uniformly; there are at most this many q per p. Thus the number of rows is ≤C U λ/L. Also λ=O(log D), by the prime reciprocal Mertens estimate since log(M)/log H_0=D(log D)^2.

Over b=h v in the interval let k(v)=Σ_{p∈P}1_{p|v} when v has no prime factor ≤H_0 and zero otherwise. The first moment is ≥c U λ/log H_0. Indeed on the p-multiples, v/p traverses an interval of length U/p≥sqrt U and must have no factor ≤H_0. The uniform profile theorem applied to the primes ≤H_0 gives this count ≥c (U/p)/log H_0: the independent geometric probability is the Mertens product and the total variation error is O(exp(−c' D(log D)^2 log D)), much smaller than 1/log H_0. One can instead apply the fundamental lemma directly at quotient length U/p.

We give the sharper second moment, needed for the indicated cutoff. The standard elementary upper sieve bounds the count without primes ≤H_0 on any real quotient interval of length T≥1 by

    O(T/min(log H_0, log(2T))).

For T large, use the primes up to min(H_0,T^(1/K_0)) with the fixed upper-sieve constant K_0, Mertens' product and bounded divisibility remainders; for bounded T use the trivial bound. Thus the diagonal contributes O(Uλ/log H_0). For distinct p,p' the quotient length is T=U/(pp')≥1, so the contribution is O(T/min(log H_0,log(2T))). For T≥H_0 these terms total O(Uλ²/log H_0). For T<H_0, fix p and split 2^j≤T<2^(j+1). Allowing all primes p' in the corresponding factor-two range, p'≥sqrt U/(2H_0)>M^(1/3) for large M, hence their reciprocal sum in any such band is O(1/L) by the prime-counting upper bound. Summing 1/(j+1) gives a total O(Uλ log log(3H_0)/L) for these pairs. The second moment is therefore

    ≪ (U λ/log H_0) [1+λ+ (log H_0/L)log log(3H_0)].

By Cauchy–Schwarz, the neighborhood size divided by the row count is

    ≫ L / [log H_0 (1+λ+(log H_0/L)log log(3H_0))] ≫ D log D.

Disjointness between h gives this same expansion Γ≫D log D for every subset of E, not just full fibers.

**Elementary alternate cutoff.** If only H_0=exp(L^c) with fixed c<1/2 is needed, use the same lower bound on the first moment and omit all quotient sieving in the second: since pp'≤U, the second moment is O(Uλ(1+λ)), λ=O(D), hence Γ≫L^(1−2c)/D. This is already ≫D and gives all consequences below with this cutoff. For c<1/3 even the worst-case log_2 H_0 singleton repair suffices.

## Completing around an arbitrary prior cover

Let F be an optimal cover for R and match rows in E to distinct anchor positions outside F. Deleting F from all neighborhoods leaves Hall deficiency m≤|F|/Γ. Indeed a deficient subset S must have Γ|S|≤|N(S)|<|F|+|S|, giving |S|<|F|/(Γ−1); one can get |F|/Γ directly from |S|−|N(S)\F|≤min(|S|,|F|−(Γ−1)|S|)≤|F|/Γ. Choose a matching of all but m rows.

For ordinary τ, the product over F and the matched anchors covers the product of R times all matched hp, since positions are distinct. Deficits are at most the valuations of all matched q's and the unmatched rows. Every unsatisfied prime unit can be obtained from a position not yet selected, since the whole interval has all the source valuations. For H, original R level demands and the levels in the matched hp are covered disjointly; for each prime add positions of highest available valuation up to its maximum level deficit. Both new costs are at most 2|E| plus Σ_{a unmatched}Ω(a). No reuse of already credited multiplicities is assumed.

For any m distinct rows in J the latter sum is ≪m[log(eM/m)+log log(3M)]. In fact E_J (3/2)^Ω(u) ≤ ∏_{p≤M}(1−1/p)/(1−3/(2p)) ≪ (log M)^C by nonnegative divisor increments, Euler factors and Mertens. Apply Jensen on the m rows. Since m≤O(n/(D log D)), n≥M/L^K and v↦v log(eM/v) is increasing up to M, the total is O_K(n/log D)=o(n). This proves the stated peeling inequality.

If C(A,I)>(2+δ)n then C(R,I)>2|R|+δ n−o(n). The uniform three theorem gives |R|≫δ n, hence its density remains comparable on the logarithmic scale. Without that bound the elementary Ω-entropy estimate alone forces |R|≥M/(log M)^(K+2) for large M, enough to reapply the critical density theorem. Its proof does not require max R=M. Apply the calibrated pair-density inverse to R at the same M and choose the excluded price-core cutoff y≥H_0, for instance y=H_0. Its profile comparison error on quotients of length at least M^γ/2 for any fixed γ>0 is smaller than any fixed negative power of L since log M/log H_0=D(log D)^2. Consequently every hot pair p,q lies above H_0, and C_{pq}(R)>0 forces pq≤M/H_0. Otherwise any witnessing a∈R would give a=h p q with h≤H_0, hence a∈E. In particular every lifted pair now has quotient length ≥H_0−1 and actual occupancy strictly greater than (2+δ/128)(|R|/M)floor(H_0) (apply [the doubled-density theorem](TWO_BASELINES.md) with gap parameter δ/2), tending to infinity much faster than any log power for n=M/(log M)^K. The same pair is genuinely populated in the original source, although its multiplicative density gain is relative to the retained source R. Fixed exponents H_0=M^η are not proved by this argument at sparse polylogarithmic density.

**Unconditional partial theorem.** If all rows have the form h p q as above, F is empty, Hall covers every row with its fresh hp anchor and a single q repair. This gives H(A,I)≤2n exactly at these parameters for every shift.

## Dependence on the existing bank theorem

The earlier research/uniform_three_2026_11_26/POWER_CORE.md already proves a stronger second-moment bound (also for prime-power labels and fixed small polynomial sieve cutoffs), and attributes the upper/lower quotient sieve to Ford, Sieve Methods, Theorem 3.6, https://ford126.web.illinois.edu/sieve2023.pdf. The advance here is the expansion against an arbitrary previously selected covering set, the entropy bound on the total repair of the few unmatched original rows, and hence actual inheritance of a fixed gap by the complement. The two-rough-atom-only consequence is independently covered by the earlier theorem.

## Why direct endpoint counting cannot replace the peel

Choose 0<a<b<1/4 fixed with λ=log(b/a) small. Take all products pq in (X/2,X] with p in (X^a,X^b] and q prime, let M=max A. Every q is >X^(3/4), so this representation is unique. The PNT uniformly at X/p and X/(2p), followed by partial summation in p, gives M~X and n~c X/log X where c=(1/2)∫_a^b du/[u(1−u)]. The marginal enrichment C_p/[t floor(M/p)] is asymptotic uniformly to 1/[2c(1−log_X p)], and can exceed any prescribed constant by narrowing the band. With weight one on the smaller primes, each source carries score two while μ~λ is small. Nonetheless every occupied pair pq is the actual source a>M/2, and its canonical fiber has size exactly one. This is a counterexample to inferring long fibers solely from the source pair excess, not to the covering conjecture, since H≤2n on these semiprimes. In a direct endpoint reciprocal-sum estimate one may improve log y to about (log M)/2 for H=M^o(1) by orienting p≤q and using q≥sqrt(M/H). The raw upper then costs O(Mμ(1+log H)/log M), already on the n scale for bounded H in the critical regime.
