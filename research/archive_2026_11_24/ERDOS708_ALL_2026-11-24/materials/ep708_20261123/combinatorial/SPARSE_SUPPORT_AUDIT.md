# Independent audit of the sparse-support H2 lemma

Date: 2026-11-23 (user-facing Kyiv date).

Audited file: `../analytic/SPARSE_SUPPORT_H2.md`.

## Verdict

**PASS.** The stated sufficient condition proves the raw valuation version
of H2 for every interval length and every shift. It does not prove H2 for
arbitrary supports or solve Erdős Problem 708.

With `P` a finite prime support, `p>=y>=2`, `k=|P|`, and `0<=w_p<=1`, put

`mu_0=sum(1/p)`, `mu_w=sum(w_p/(p-1))`.

The sufficient condition is

`3 mu_w + mu_0 + (k+1)/y <= 1`.

The claimed consequence is the inequality between the prefix hinge at
threshold two and the shifted interval hinge at threshold one for
`X_w(t)=sum w_p v_p(t)`.

## Main points checked

1. **Subset-sum step.** For a list of terms in `[0,1]` with total greater
   than two, a sublist with total in `[4/3,2]` always exists. If two terms
   are at least `2/3`, use them. Otherwise place the at most one large term
   first, and take the first partial sum reaching `4/3`. The crossing term
   is less than `2/3`, so the resulting sum is less than two. Endpoints
   are harmless.

2. **Carrier size.** Applied to the prime-factor multiset, the chosen
   divisor `d` has weight at most two, so a positive-weight prime factor
   remains whenever `X_w(a)>2`. Its size is at least `y`. This justifies
   `d<=a/y`, even with repeated prime powers and zero weights elsewhere.

3. **Prefix estimate.** The pointwise upper bound sums nonnegative terms,
   so using every eligible carrier is legitimate. The summatory estimate
   `sum_{u<=L}X_w(u)<=L sum_p w_p/(p-1)` follows by finite floor sums and
   the geometric series. No independence assumption is used.

4. **Signed pointwise estimate.** For a target `b`, let `s` be its full
   `P`-smooth part. For every contributing proper divisor `d<s`, some
   prime of `P` divides `s/d`; hence
   `1-sum_p [dp|b] <= 0`. The sole possible positive summand is `d=s`,
   where its weight is exactly `X_w(b)-1`. Thus the signed certificate
   is bounded by the target hinge. This remains true for prime powers:
   a single remaining copy of a prime is enough to make the bracket
   nonpositive.

5. **Interval loss.** For each carrier, the bounds
   `N_I(d)>=M/d-1` and `N_I(dp)<=M/(dp)+1` give the displayed loss of
   `k+1`. They also apply when `dp>M`; such a modulus can still have one
   multiple in the shifted interval, and that possibility is included.

6. **Sign needed for the last step.** The hypothesis guarantees
   `beta=1-mu_0-(k+1)/y >= 3 mu_w >= 0`. Therefore replacing each carrier
   weight by its lower bound `1/3` does not reverse an inequality.

7. **Boundary cases.** An empty carrier family makes the prefix hinge
   zero. Empty support and zero weights also pose no problem. A real
   cutoff `M/y` is interpreted as an integer inequality, without assuming
   divisibility. No bound on the magnitude of the interval shift enters.

The conservative weight-free condition `min(P)>=5k+2` follows exactly as
claimed, by bounding `mu_w<=k/(y-1)` and `mu_0<=k/y`.

## A small specialization: unit weights

If every nonzero weight is one, each hot source has at least three prime
factors counted with multiplicity. Choose any two copies for the carrier.
Then the carrier has weight exactly two and coefficient `h_d=1`, rather
than merely `h_d>=1/3`.

The same proof consequently establishes H2 under the weaker condition

`mu_w + mu_0 + (k+1)/y <= 1`.

A conservative weight-free sufficient condition is `y>=3k+2`, since

`k/(y-1)+(2k+1)/y <= (3k+1)/(y-1) <= 1`.

This is a specialization of the audited method, not a claim of priority
or a solution for unrestricted supports.

## Definition warning

Chen's bounded atom-system H2 uses a per-prime function taking values in
`[0,1]`; the raw valuation H2 here uses `w_p v_p(t)`, which need not be
bounded by one. The sparse-support proof is directly valid for the latter.
Its proof does not silently rely on the per-prime cap from the former.

