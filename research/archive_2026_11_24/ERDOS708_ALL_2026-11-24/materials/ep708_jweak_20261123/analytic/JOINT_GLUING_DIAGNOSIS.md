# Exact status of the remaining joint gluing step

## 1. What has been proved in this continuation

Two unrestricted necessary reductions are now available on actual hypothetical obstructions.

In the sparse regime m/M -> 0, the full optimum has O(m) hot positions and weighted reciprocal mean at most 1+o(1). The finite Bonferroni inequality controls all substantial weights on a lower prime range. Summing over prime-power monomial divisors then permits a weighted o(m) source deletion after which, for every fixed substantial-weight threshold eta, each source has at most 4(floor(1/eta)+1) substantial prime occurrences. Their least prime tends to infinity. The original full-optimum row balance survives with weighted excess o(m). These statements are proved in `SPARSE_HOT_BONFERRONI.md` and `SPARSE_BOUNDED_HEAVY_OCCURRENCES.md`.

In the dense regime m/M>=rho_0>0, the actual demand core has k^2=o(M). The small-weight part of that core can therefore be capped and replaced by its model mean v, with error O(M sqrt eta)+o(M). Raw tails are accounted for exactly and the one-occurrence remainder loses at most eta m. An affine estimate excludes v near or above one. The remaining case is a heavy-profile hinge comparison with positive target threshold t=1-v. The full proof and exact residual inequality are in `DENSE_LIGHT_CORE_CONCENTRATION.md`.

An independent optimal weight-band deletion lemma creates a gap between the retained light and substantial weights at a small linear loss in the objective. It removes the numerical eta*K circularity in the old conditional diffuse estimate. It does not bound the global number of substantial coordinates. Its proof is in `../combinatorial/OPTIMAL_BAND_DELETION.md`.

None of these statements proves J_weak.

## 2. Why a per-source occurrence bound is not a global pattern bound

The following elementary construction isolates the bookkeeping problem. It is **not** an optimal or balanced counterexample to the desired theorem.

Choose active primes p_1<p_2<p_3 and give them weight one. All other prime weights are zero. For an integer L, let

    U_L={u:1<=u<=L, gcd(u,p_1p_2p_3)=1},
    A={p_1p_2p_3 u:u in U_L},
    M=p_1p_2p_3 L.

Every source has exactly three active prime occurrences and load three. The least active prime can tend to infinity.

There are two tempting ways to define a carrier after deleting the largest active prime p_3. Each has a different obstruction.

### 2.1 Collapsing inactive cofactors invalidates a prime-count fibre bound

If only the active cofactor d=p_1p_2 is retained, all |U_L| sources belong to this one fibre. Its target scale is T=M/d=p_3 L.

For sufficiently large p_1,

    |U_L| >= L(1-1/p_1-1/p_2-1/p_3)-3.

Thus |U_L| is comparable to L. On the other hand, by choosing L so large that log L/p_3 tends to infinity, the standard prime-count upper bound gives

    pi(T)=O(p_3 L/log(p_3 L))=o(L).

Consequently the assertion "a source fibre obtained by deleting one active prime contains at most pi(T) sources" is false when arbitrary inactive or light cofactors have been collapsed. Distinct actual sources need not have distinct active cofactors or distinct deleted primes.

### 2.2 Retaining inactive cofactors invalidates bounded positive multiplicity

Instead retain every full cofactor

    d_u=p_1p_2 u,       u in U_L.

Now choose the positive integer

    b=p_1p_2 lcm{u:u in U_L}.

It is divisible by every d_u. Its active load is exactly two, because the least common multiple is coprime to p_1p_2p_3. Hence its target hinge is exactly one.

Consider any of the earlier discounted carrier brackets that subtract only additional active primes dividing b/d_u. For every u, there is no such additional active prime: p_1 and p_2 have each been removed exactly once, and p_3 does not divide b. Thus every bracket is one. The adaptive source-size condition is also satisfied, since

    M/d_u=p_3 L/u>=p_3>p_2.

Therefore the positive carrier sum at this one target equals |U_L|, although every carrier has only two active prime occurrences. A bound depending only on the number of active occurrences cannot hold for this family of full carriers.

The integer b can be placed inside a positive interval of length M, so this is a genuine pointwise target obstruction, not a formal Boolean assignment.

The example does not satisfy the necessary optimality balance. Indeed, the whole bank of p_1p_2-multiples is hot and already has at least p_3 L positions, far more than the source count. The full-optimum constraints would rule it out. Its purpose is narrower: it shows exactly why the two naive carrier summations do not follow from bounded active degree and a large least active prime alone.

## 3. What an additional proof would have to control

A successful proof may still use these carriers, but it must use the original arithmetic demands or the full hot-set balance to control the trade-off between source-fibre multiplicity and target-pattern multiplicity. It cannot use the prime-count estimate from Section 2.1 after collapsing light cofactors, or the bounded-positive-multiplicity estimate from Section 2.2 after retaining them.

The conditional diffuse estimate applies to a fixed excluded prime set of controlled size. Applying it separately to each source's small heavy pattern does not enforce the absence of all other heavy primes and does not authorize spending the same target hinge independently for each pattern. A valid inner light-prime first-crossing certificate, summed before the outer heavy patterns, would be one possible way forward; no such complete certificate has been established here.

Similarly, in the dense reduction the constant t=1-v satisfies 0<t<=1. Rescaling the residual heavy load by 1/t makes its coordinate profiles as large as 1/t, so the old unit-height results cannot simply be invoked at threshold two. Nor does a same-threshold first-moment or second-moment comparison imply the required two-threshold hinge comparison.

## 4. Conclusion for the requested theorem

The established inequalities give additional necessary structure on every putative obstruction and identify a concrete invalid summation shortcut. They do not prove J_weak, and no counterexample to J_weak has been produced. The outstanding statement remains a single joint target-hinge estimate on the actual balanced minimal-obstruction class, with all source multiplicities and prime powers retained.
