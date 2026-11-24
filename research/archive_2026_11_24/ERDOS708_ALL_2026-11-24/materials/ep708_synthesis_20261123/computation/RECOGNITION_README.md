# Unified exact-2n recognition certificates

## Scope and status

`exact2n_recognition.py` is a standalone Python 3.10+ program, using only the
standard library. It recognizes sufficient conditions for a distinct source
set `A subset [2,M]` to have a product cover of size at most `2|A|` in **every**
interval `{x+1,...,x+M}`, for every integer `x>=0`.

The interval length **M stays fixed after every deletion**, even when the
maximum source is deleted. A successful certificate proves an existence
bound; this program does not construct the interval cover.

The unrestricted exact and asymptotic versions of Erdős 708 remain open in
this work. A result `UNKNOWN` means only that these sufficient rules did not
recognize the input. It does not assert infeasibility, a counterexample, or
the failure of some other proof. The mathematical arguments have internal
AI-assisted audits, not formal verification or external referee approval.
No priority claim is made.

The program includes Wang's quadratic theorem as an **external base case**.
When used, the certificate explicitly records it. The verifier checks that
`M>=16m^2`; it does not formally verify Wang's proof. The cited public working
manuscript is Ziming Wang, *Fractional-to-Integer Transference and Five-Prime
Bounds for Interval Divisor Covers*, section “The quadratic coefficient-two
gate”, in
<https://github.com/science-prince/erdos-708-interval-divisor-covers>.
Its proof also works for ambient `M>=max(A)`: every source-size comparison
uses `a<=M`, with no step requiring a source equal to M. The local proof was
checked for this extension.

## Commands

Generate the structured example bundle and verify it in a separate process:

```bash
python exact2n_recognition.py --demo --output recognition_examples.json
python exact2n_recognition.py --verify recognition_examples.json
```

For an input file containing either an integer list or an object such as
`{"sources":[8,27,125],"M":144}`:

```bash
python exact2n_recognition.py --sources input.json --output certificate.json
python exact2n_recognition.py --verify certificate.json
```

The optional `--M` argument overrides an input file's M. Otherwise M defaults
to `max(A)`; the empty source set defaults to M=1. Duplicate, nonintegral,
or less-than-two sources are rejected. There is no SciPy dependency and no
import from an earlier project directory. Exact trial division is used for
factorization; runtime is not promised for arbitrary enormous integers.

The JSON contains the original sources and M, ordered deletions, the current
cardinality and exact numerical witness at each step, the residual sources,
and a base-case certificate. The verifier replays the trace from the original
A and recomputes demands, prime factors, cardinalities, and Hall bounds.
It accepts any valid deletion order; it does not rerun the recognizer's
ordering heuristic to validate a certified result. Generator and verifier
share exact arithmetic helpers, so this is not a second independently written
implementation of factorization or counting.

## Base cases

Write m for the number of sources currently remaining.

1. **Empty set:** use no positions.
2. **Whole interval:** if `M<=2m`, use the full interval. Its product is
   divisible by M!, and the product of distinct sources in `[2,M]` divides M!.
3. **Wang's external quadratic theorem:** `M>=16m^2`.
4. **Finite cofactor Hall criterion:** for composite sources put
   `d(a)=a/Pmax(a)`. Let Q be the union of prime supports of these nonunit
   cofactors and let `r_A(d)` be the number of sources with cofactor d. Require,
   for every distinct d,

       floor(M/d) - sum_{q in Q, d*q<=M} ceil(M/(d*q)) >= r_A(d).

For completeness, the fourth criterion uses the signed counting function

    K_D(b)=sum_{d in D} 1[d|b]*(1-sum_{q in Q, q<=M/d}1[d*q|b]).

For any subset of sources and its distinct cofactors D, at most one summand
can be positive. A positive summand requires d to be the full smooth part of
b on primes `Q intersect [2,M/d]`. As d increases the cutoff decreases, so
there cannot be two such fixed points. Thus `K_D(b)<=1[b belongs to the union
of the cofactor neighborhoods]`. Interval counts give the displayed lower
bound; summing it supplies Hall's condition for all subsets. Prime sources
have cofactor one and can be assigned afterward to unused positions.

The resulting injection supplies every source except its removed largest
prime. At most m prime units remain. The full interval supplies the complete
source product, so each still-missing unit can be repaired using an unused
position. The final cover has at most 2m positions. The argument uses only
`a<=M`, so it remains valid with the original ambient length after peeling.

## Extension rules used for peeling

For a current source a, the rest of the certificate supplies a cover B of
`A minus {a}` using at most `2m-2` positions. Each rule below extends B using
at most two additional positions. No minimal-counterexample assumption is
needed by this recognizer.

Whenever a chosen product is deficient in a prime valuation, an unused
interval position containing that prime exists: otherwise the full interval
would have the same deficiency, contradicting full-interval supply.

**At most two prime units.** If `Omega(a)<=2`, repair its at most two units.
Omega counts prime factors with multiplicity.

**Two-prime saturation.** Choose two prime occurrences p,q in a, allowing
`p=q` only when `p^2|a`. Require

    p*q >= 2m-1,     D_p(A) <= q*v_p(a/q).

If some multiple of `a/q` lies outside B, add it and repair at most one
q-unit. Otherwise B contains the entire `a/q` bank. That bank has at least
q positions, and therefore already supplies the whole p-demand by the
second inequality. A multiple of `a/(pq)` can then be chosen outside B:
its bank has at least `pq>=2m-1` positions. After adding it, at most one
q-unit remains; when p=q even this remaining unit is unnecessary.

**Prime-power-bank saturation.** Suppose `a=p^e*q`, for primes p,q, with
q=p permitted, and require `m*p^e<=M`. A fresh multiple of `p^e`, if
available, again leaves at most one q-unit. Otherwise B contains every
multiple of `p^e`. These supply at least

    e*floor(M/p^e) + sum_{j>e}floor(M/p^j)
      >= sum_{j>=1}min(m,floor(M/p^j)) >= D_p(A)

p-units. The last inequality uses distinctness of the m sources. Thus at
most one q-unit remains. This rule is specific to a prime-power cofactor;
the same cutoff cannot be asserted for an arbitrary cofactor.

The recognizer chooses only sources already satisfying a verified rule.
Its preference for removing an exclusive small cofactor prime is an ordering
heuristic, not an additional mathematical assumption.

## Structured demonstrations

Let R be all 35 cubic monomials, repetitions allowed, on the primes
`{11,13,17,19,23}`. Then `max(R)=23^3=12167`.

| Input | n | Ambient M | Ordered deletions | Base case | Status |
|---|---:|---:|---|---|---|
| R plus 6,9 | 37 | 12167 | 6: Omega<=2 | Hall on 36 sources | CERTIFIED |
| R plus 8,27 | 37 | 12167 | 8: prime-power bank | Hall on 36 sources | CERTIFIED |
| R plus 4096,11875 | 37 | 12167 | 11875: two-prime saturation | Hall on 36 sources | CERTIFIED |
| R plus 27,12928 | 37 | 12928 | 12928: two-prime saturation | Hall on 36 sources | CERTIFIED |
| R plus 8,27,125 | 38 | 12167 | 8, then 27: prime-power banks | Hall on 36 sources | CERTIFIED |
| 64 selected 11-smooth sources in (2048,4096] | 64 | 4096 | None | No supported base | UNKNOWN |

The direct Hall criterion fails on all five mixed inputs, and Wang's
quadratic criterion fails both initially and at their residual Hall bases.
These examples therefore test the combined proof, not merely a redundant
code path. The third input is especially useful: every source has at least
three prime factors with multiplicity. For `a=11875=5^4*19`, use p=5,q=19:

    p*q=95 >= 73,     D_5(A)=4 <= 19*4=76.

The prime-power-bank rule alone cannot delete this source because
`37*625>12167`. Initially, the Hall row d=121 has lower bound -7 against
fibre size 5. After the two-prime deletion, all residual Hall rows pass
(minimum margin zero). The final all-shift cover bound is 74.

The fourth example deletes the original maximum source 12928. Its residual
maximum is 12167, but all Hall counts continue to use ambient M=12928.
The fifth example recomputes the current m at two successive peeling steps,
38 and 37. Its final bound is 76.

The bundle also checks the direct Hall, full-interval, empty, and external
Wang bases. Generation rejects three intentionally altered certificates:
a forged demand, a changed ambient length below the original maximum, and
a forged Hall lower bound. These finite checks validate the implementation
and its concrete certificates; they are not a computational proof of the
unrestricted conjecture.
