# Independent audit of the analytical peeling and transfer arguments

Reviewed: `../analytic/ANALYTIC_RESULTS.md`, 22 November 2026.

## Verdict

**PASS for the stated all-scale peeling theorem and the conditional H2
transfer.** This is a written-proof audit, not a conclusion inferred from
random testing. H2 itself remains unproved, and the argument does not prove
the exact bound `2n`.

## 1. The peeling invariant

Maintain an explicit target integer `H` dividing the actual product of the
currently selected subset `B`. The target need not equal that product.
Unexpected factors in the selected interval positions are allowed and can
be used in later stages.

For a rough group with largest prime `p > Z`, processing groups in increasing
`p` ensures that before its first source is inserted, `p` does not divide
the target. It may already divide the actual covering product; that causes
no difficulty in the cumulative-GCD extension lemma. The gcd with the new
source is at most `a/p <= floor(M/p)`. Before any necessary insertion the
budget gives `|B|+1 <= K < p`, so the extension threshold is satisfied.

### Stage 2, `p^2 <= M`

There are at least `floor(M/p) >= p > Z >= K` interval multiples of `p`.
Adding a fresh multiple for each requested copy preserves divisibility of
the enlarged target, regardless of incidental factors already present.
The total construction accounting ensures fewer than `K` selected points
before each addition.

### Stage 2, `p^2 > M`

Every source contains `p` at most once. No source in another largest-prime
group can contain `p`: a source of smaller largest prime cannot do so by
definition, and a source of larger largest prime `q` would be at least
`pq > p^2 > M`. No smooth source contains `p` either.

Consequently the current **target** has exactly one `p` factor before this
group's extra copies are supplied. If the actual product has valuation
`u >= m_p`, it already pays for all `m_p-1` extra target copies. If `u<m_p`,
at most `u` selected positions are multiples of `p`. The interval contains
at least `m_p` such multiples, because the original group consists of
`m_p` distinct multiples of `p` in `[1,M]`. Adding `m_p-u` fresh multiples
therefore suffices. This number is at most `m_p-1`.

Changing the target in this stage changes only its `p` valuation; all other
target valuations were already covered. Carriers shared between different
prime groups cannot invalidate that invariant.

### Stage 3

The remaining requests are the entire cofactors `a/p`, not just their smooth
parts. Each has at least `p > K` multiples in the interval. Selecting fresh
positions therefore pays for every cofactor in full, including additional
copies of `p` when `p^2 <= M`, as well as any other rough primes. Repeated
cofactors are paid on distinct positions. Unit cofactors can be omitted.

The budget `|B0| + t + (r-t) + (r-t)` is exactly the stated
`K=|B0|+2r-t`. If there is a rough group, `Z<M` automatically; the assumptions
then imply `K<M`, consistent with selecting a subset of the interval.

## 2. H2 and the boxed LP

The LP retains `0 <= x_b <= 1`; it does not allow repeated use of an interval
position. For a dual coordinate above one, lowering it to one changes the
interval hinge penalty linearly on every multiple of that prime. The
interval total valuation is at least the valuation of `M!`, which dominates
the distinct sources' total valuation. Thus this clipping cannot decrease
the dual objective. H2 bounds the clipped objective by `2m` for any selected
smooth source subset of size `m`.

At an optimal vertex, at most the number of active prime rows can have
strictly fractional variables. If at least one is fractional, rounding up
uses strictly less than the LP value plus that count. Integer cardinality
gives the `-1` in `|B0| <= 2m+pi(Z)-1`. If the optimum is already integral,
the same bound remains true because `pi(Z)>=1`. A nonempty smooth set has
at least one active prime. The empty smooth set is handled separately.

For rough sources present, the resulting peeling budget is at most
`2n+pi(Z)-1`, hence at most `Z=q_n`. If there are no rough sources, rounding
alone proves the claimed bound. The proof therefore covers all `M`, without
a quadratic-to-cubic gap.

The threshold exists since `pi(4n)<=2n`. The cases `n=1`, no smooth sources,
no rough sources, and an integral LP optimum do not produce exceptions.
The quoted prime-count asymptotic yields the displayed
`2n+(2+o(1))n/log n` bound conditionally on H2.

## 3. Suggested presentation clarification

Keep the explicit target `H` and actual covering product separate when
presenting Stage 2. Saying merely that the current selected product has
one copy of `p` would be false. The note correctly says that the **target**
has one copy in the `p^2>M` case.

This audit makes no priority claim for the peeling refinement, LP reduction,
or resulting conditional theorem.
