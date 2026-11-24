# Independent audit of the unrestricted asymptotic route

## Conclusion

The fixed-ambient minimality reductions, the deletion-cover identities, and
the optimal-dual normalization described below are valid for the **full
source class**. No unrestricted coefficient-two proof has been obtained.
The remaining global weighted bank estimate is still an unproved step.
This is an internal mathematical audit, not formal verification or external
referee approval. No priority claim is made.

## 1. Proved raw-minimal reduction and exact identities

The complete proofs are in `RAW_MINIMALITY_AND_DELETION_IDENTITIES.md`.
For the same delta>0 and the SAME original M,I, an integer-minimal failure
of budget `(2+3delta)m_0` satisfies

    L_raw(A_0,I)>(2+3delta)m_0-pi((2+3delta)m_0)
                  >(2+2delta)m_0

for sufficiently large M. Taking a least-cardinality RAW failing subset B
at coefficient `c=2+2delta` is therefore legitimate. Its own size m obeys
`m>sqrt(M)/4`, so it tends to infinity. Its own prime cap is
`p<K=c(m-1)+1<cm`; hence its rounding loss remains o(m).

For an optimal clipped raw dual, write `L_raw(B,I)=cm+e`, `e>0`.
Every source satisfies

    X(a)>=c+e>c,
    e<=log_2 M-c.

For every deletion fractional cover y of cost at most c(m-1), the FULL
union U_a of that source's prime-deletion banks has residual capacity

    sum_{b in U_a}(1-y_b)<1.

Buying one residual mass across different cofactor banks leaves at most
one total prime-unit deficit, so the usual two-position idea has a valid
fractional counterpart. It does not imply pointwise saturation of each
deletion-cover position.

The correct fractional pair-bank condition is

    pq|a, pq>=K  =>  D_p>(q-1)v_p(a/q).

Consequently `E={p<=sqrt K} union {D_p>=p}` and its complement have the
usual one-outside-occurrence structure, with
`|E|=O(sqrt(m/log m))`. The q-1 and D_p>=p thresholds are intentional.
The residual-union repair, pair-bank condition, and same-delta transfer
received a second independent internal audit with no correction required.

For the SAME optimal full dual and any deletion primal y, the gap is exactly

    C_a-L_raw(B,I)+X(a)
      = weighted prime oversupply
        + sum_{X(b)>1}(1-y_b)(X(b)-1)
        + sum_{X(b)<1}y_b(1-X(b)).

It is nonnegative and at most `X(a)-c-e`. This is one shared budget;
its different terms cannot each be charged the full source excess.

## 2. Written normalization audit: PASS after two local clarifications

`../analytic/GLOBAL_DUAL_NORMALIZATION.md` was read in full. Its main
claims and remaining-obligation statements are correct. In the original
integer-minimal instance, with `r=|P|=o(m)` and `c=2+3delta`,

    sum_A(c-X(a))_+ <=(cm-L_raw(A,I))_+<r.

Discarding B={X<=c-delta} loses at most r/delta sources and total weighted
demand O_delta(r). The retained G has all loads above 2+2delta. Its entire
bank union U_G is saturated in the FULL optimal primal for A. Thus

    Xi=sum_p w_p(V_p(U_G)-D_p(G))_+
       <=sum_{a in B}X(a)=O_delta(r)=o(m).

The positive part is taken **coordinatewise**, so this bound uses no
cancellation between deficient and excessive rows. G is not asserted to
be minimal itself. The factorial refinement
`D_p(A)>=N v_p(a/q)+v_p(N!)`, `N=floor(M/(a/q))`, is also valid.

The audit found and the author corrected one local example error: for
`A={2,4,...,2m}`, the full source-prime count is r=pi(m), not one. There is
one active dual coordinate. Its threshold-one primal mass is still
ceil(m/2), so the example correctly disproves the claim that all such
boundary mass is O(r). The coordinatewise meaning of the residual
positive part is now written explicitly. No other correction was needed.

## 3. Exact counterexample scope independently checked

The standard-library verifier
`../combinatorial/verify_bank_product_counterexample.py` was run
independently with `python -I` and returned PASS. It checked 1,988,099
rough-residue conditions and 27,390 source prime-deletion quotients.

The exact lifted construction has

    |A|=10353, lifting prime p=11777, M=138532851,
    D_p(A)=10353, V_p(U(A,I))=10352.

It disproves universal product divisibility by the bank-union product,
even though every source has at least three prime occurrences. It is
NOT an Erdos 708 counterexample or a minimal obstruction: one individual
cofactor-4 bank already has at least 34,633,212 positions. Moreover the
written proof correctly shows that this very example has STRICT positive
joint weighted surplus whenever all source loads exceed two. It therefore
does not refute the weighted statement needed by the current route.

## 4. Directed joint-weighted search: no counterexample found

`joint_bank_closure.py` optimizes over all strictly-hot source subsets for
a fixed actual CRT interval and clipped rational weights. It uses one
integer maximum-closure problem, not an enumeration of covering minima.
The final implementation also detects nonempty equality optima by taking
the maximal source side of an optimum cut. Actual valuations are fixed
exactly by the CRT powers, and integer-capacity bounds are checked.

Three final directed cases at M=20000 used, respectively, 9650, 10895,
and 3244 hot candidates, with light-small-prime, heavy-large-prime, and
rough-support weights. The residue choices either spread large primes
or concentrate them in positions free of small primes. Each returned an
empty maximal optimum and zero profit. The final records and reproduction
commands are described in `DIRECTED_BANK_SEARCH_STATUS.txt`.

No nonempty witness to failure of weighted bank surplus was found. These
negative finite computations are NOT evidence establishing a universal
lemma. No further optional cases are being run. The standard-library
witness checker validates arithmetic data, not a universal assertion.

## 5. Precise unresolved global step

A sufficient estimate on the normalized OPTIMAL data would be

    sum_{a in G}(X(a)-2-delta)_+
       <=sum_{b in I}(X(b)-1)_+ + C_delta Xi + o_delta(m).

Here Xi is already o(m), all valuations are raw, and the target hinge is
counted once. Neither this estimate, its linear-slack variant, nor a
sufficient global weighted bank-expansion theorem has been proved by the
present audit. The reductions preserve the global problem; they do not
replace it with a theorem for a restricted family.
