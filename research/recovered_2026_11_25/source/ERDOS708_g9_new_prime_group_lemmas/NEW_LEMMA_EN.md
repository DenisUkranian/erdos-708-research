# A uniform prime-group bundling lemma for Erdős–Surányi 708 (n=9)

**Status:** Rigorous sufficient criterion, **not** a proof that `g(9)=12`. 2026-11-24.
It depends on the separate upper bounds `g(k) <= f(k)` for `k<=8`, specifically
`f(1),...,f(8) = 1,2,4,5,6,8,9,11`. The code is a certificate search, not
an independent proof of those upstream finite bounds.

Let `A` contain nine distinct integers `>=2`, `M=max(A)`, and `I` be an
arbitrary interval of `M` consecutive **positive** integers. Let `p>=13` be
prime, occurring in precisely `d` of the source integers, `1<=d<=8`, and
suppose every such source has p-adic valuation exactly 1. Write them as
`p*u[1],...,p*u[d]`. Let `f=f(9-d)` and `s=12-f-d`. The values are:

| d | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| f | 11 | 9 | 8 | 6 | 5 | 4 | 2 | 1 |
| s | 0 | 1 | 1 | 2 | 2 | 2 | 3 | 3 |

**Theorem (prime-group bundled cover).** If, for some chosen anchor `u[a]`,
the other `d-1` cofactors admit a partition into `s` (possibly empty)
**ordered** groups with products `h[1],...,h[s]` such that

`(f+d+j)*h[j] <= M` for every `j=1,...,s`, 

then for **every** interval `I` of length `M` there exists `B subset I` with
`|B|<=12` and `prod(A) | prod(B)`.

**Proof.** First cover the `9-d` sources not divisible by `p` with `<=f`
positions using the upstream bound (valid also at any longer interval
length by taking a subinterval). Let `D` be their product. Add the complete
anchor source `p*u[a]` to the *required product* in at most one new position:
`gcd(D,p*u[a]) | u[a] <= M/p < M/(f+1)`. The one-step gcd-extension lemma
applies: if a fresh multiple of the source is unavailable, all its multiples
are already selected, so one can instead append a fresh multiple of the gcd.
After this stage the product of selected positions is divisible by
`D*p*u[a]`, and at most `f+1` positions are selected.

Next supply the `d-1` remaining p-units. There are at least `d` multiples
of `p` in `I`, since `floor(M/p)>=d` (the `d` distinct source multiples
`p*u[i]` lie in `[1,M]`). Each additional p-multiple contributes at least
one unit. If none is available, all at least `d` interval p-multiples are
already selected, and the required `p^d` is already present. Thus at most
`d-1` new positions are needed to reach the required product
`D*p^d*u[a]`. At most `f+d` positions are selected.

For each `j`, choose a fresh multiple of `h[j]`. Such a multiple exists
because the interval contains at least `floor(M/h[j]) >= f+d+j`
multiples, while at most `f+d+j-1` positions were previously selected.
The selected product is now divisible by
`D*p^d*u[a]*prod(h[j]) = prod(A)` and the number of selected positions is
at most `f+d+s=12`. QED.

**Corollaries.** If `p` divides exactly three sources with cofactors
`u1<=u2<=u3`, the sufficient condition reduces to `12*u1*u2 <= M`
(the largest cofactor is used as anchor). If `p` divides exactly four
sources, `11*u1*u2 <= M` is sufficient (put the two smallest cofactors
in the first bundle and the third in the second). For `p^2>M` the
unit-valuation hypothesis holds automatically. Hence a counterexample to
`g(9)<=12` can contain a prime `p>sqrt(M)` in exactly three sources only
if `12*u1*u2 > M`, which also implies `p < sqrt(12M)`.

Script: `bundle_certificate.py`. A returned certificate gives a fixed
multiplicative decomposition, and its displayed integer inequalities
can be audited independently. A `null` return does not imply that 12
positions are insufficient.

## Simultaneous disjoint-prime-group extension

This is the version implemented by `multigroup_certificate.py`. Choose a
set of distinct primes `p_1,...,p_k >=13` such that every source is divisible
by **at most one** of them, always to exponent exactly one. Put `d_i` for
the number of sources containing `p_i`, and `m=sum(d_i)` (`1<=m<=9`).
Let `f=f(9-m)` (with `f(0)=0`) and `s=12-f-m>=0`. In each prime group
choose one anchor `p_i*u_i`. Partition **all other cofactors** into `s`
ordered bundles with products `h_j` obeying

`(f+m+j)*h_j <= M` for all `j=1,...,s`.

Then `tau(A,I)<=12` for every interval of length `M`.

**Proof.** Cover the `9-m` sources not divisible by any chosen prime in
`f` positions. Append the `k` full anchors one at a time using the
one-step gcd extension: in the required product built so far, prime `p_i`
never appears (the source groups are disjoint), and hence the gcd with
the next anchor is bounded by its cofactor `u_i<=M/p_i`; this fits the
next-stage capacity because `p_i>=13` and no more than 12 total slots are
scheduled. Each anchor adds at most one new position, so there are at most
`f+k` positions now. For each `p_i`, add at most `d_i-1` unused multiples
of that prime until its required total p-adic exponent `d_i` is present.
There are at least `d_i` interval multiples of `p_i` because `d_i`
distinct source multiples already lie in `[1,M]`; exhausting them already
supplies `d_i` units. Altogether this stage costs at most
`sum(d_i-1)=m-k`, giving at most `f+m` positions. Finally append fresh
multiples of each bundled `h_j` in order. The displayed slot capacities
guarantee that each is fresh. The total number of positions is at most
`f+m+s=12`, and their product contains the product of all nine sources. QED.

In particular, **all** primes `p>sqrt(M)` automatically satisfy both
prerequisites: no source `<=M` contains `p^2` or the product of two of
these primes. Simultaneous certificates therefore handle arbitrarily many
such large-prime groups (with total multiplicity at most nine), using one
shared budget rather than counting the groups as independent covers.

For instance, with `M=400` and sources
`A={2,3,46,58,69,87,145,161,400}`, take `p=23` and `q=29`.
A three-source group for each is represented by anchors `46` and `58`;
after four positions covering the other sources and six positions for
both prime groups, products `35` and `9` occupy slots 11 and 12.
The independent inequalities are `11*35<=400` and `12*9<=400`.
The certificate is valid for **every** shift.

### Exact numerical prime-band pruning for groups of size three

Suppose `p^2>M`, and `p` occurs in exactly three sources with distinct
cofactors `1<=u1<u2<u3<=T=floor(M/p)`. The preceding one-group lemma
proves the desired 12 bound whenever `12*u1*u2<=M`. Since
`u1<=T-2` and `u2<=T-1`, **every** triple of such sources is already
covered if

`12*(T-2)*(T-1) <= M`.

Thus any unhandled triple requires

`12*(floor(M/p)-2)*(floor(M/p)-1) > M`,

an exact integer test. This restricts the range of possible p without
examining other six sources or any interval shift. For example:

| M | lower bound for floor(M/p) | allowable p with p>sqrt(M) | number of possible primes |
|---:|---:|---|---:|
| 500 | 8 | 23..62 | 10 |
| 2,000 | 15 | 47..133 | 18 |
| 10,000 | 31 | 101..322 | 41 |
| 19,999 | 43 | 142..465 | 56 |

The condition is **necessary only for a triple group of exactly three
sources**; it is not asserted for a prime that divides four or more sources.
The full count in the last column was independently enumerated by exact
integer arithmetic and trial division for primality (or the sympy prime
sieve in the exploratory notebook). These counts are informational: the
underlying mathematical implication uses only the displayed integer
inequality.

### Uniform restriction on all large primes in a putative counterexample

Assuming `g(8)<=11` and `g(7)<=9`, a prime `p>=13` present in only
one or two sources can be eliminated by at most 12 positions.

For one source `a=p^r*u`, apply the one-step gcd extension to the
11-position cover of the other eight sources. The other eight have no
`p`, hence `gcd(D,a)|u<=M/p<=M/13<M/12`.

For two sources, write them `a=p^r*u` and `b=p^s*v`, `r>=s>=1` and
`p` does not divide `u*v`. Cover the other seven sources in nine
positions. Apply the gcd extension to `a` (the gcd divides `u<M/13`).
This takes at most one more position and makes the selected product
divisible by `D*a`. If it lacks the additional p-factor `p^s`, then an
unused multiple of `p^s` exists: otherwise *all* at least two interval
multiples of `p^s` were already selected, one of them supplying at
least `p^r` (the one used for `a`, or present before the gcd repair),
and the other at least `p^s`. Add the unused multiple if needed. Finally
append one fresh multiple of `v=b/p^s`, possible because
`v<=M/p^s<=M/13` and at most eleven positions are selected.
Therefore 12 suffice.

Hence any counterexample must have each active `p>=13` in at least
three source integers. In the residual range `M>=121`, it additionally
requires

`p<=M/5` for every active `p>=13`.

Indeed, if `p>M/5`, then `floor(M/p)<=4`; the prime appears to exponent
one, and its group size is either 3 or 4. For a size-three group the two
smallest distinct cofactors are at most 2 and 3, so
`12*u1*u2 <=72 < M`, and the prime-group lemma covers the case.
For a size-four group the two smallest cofactors are 1 and 2, so
`11*u1*u2 <=22 < M` and the lemma again applies. This is a
**global all-shift necessary condition** for the remaining finite search.

The same integer-bundle criterion yields a **uniform large-prime exclusion**
with stronger elementary bounds at larger M:

| If `M>=` | Then every active `p>=13` in a counterexample must satisfy |
|---:|---|
| 121 | `p<=M/5` |
| 144 | `p<=M/6` |
| 240 | `p<=M/7` |
| 360 | `p<=M/8` |

For a row `(M0,k)`, assume `p>M/k`. Then `T=floor(M/p)<=k-1`
and, because `p>=13>k`, necessarily `p^2>M`. By the earlier
large-prime-support lemma, `p` must appear in at least three sources,
so its distinct cofactors form a subset of `{1,...,k-1}` of size at
least 3. It is enough to check the prime-group bundling certificate
for **all** such subsets at `M=M0`: as M increases, bin capacities
can only increase. Respectively 5, 16, 42 and 99 nontrivial
cofactor subsets were checked exhaustively with exact integer arithmetic;
all have a 12-slot certificate. These tiny finite tables can also be
checked by hand, and do **not** involve exploring possible interval
shifts.

The explicit complete 162-case data appear in
`prime_band_certificates.json`. The *independent checker*
`check_band_certificates.py` re-generates all subsets and checks
(1) no omissions or duplicates, (2) the exact chosen anchor,
(3) every cofactor occurs in precisely one bundle, and
(4) every slot bound holds as an integer inequality.
The search program `build_band_certificates.py` is separate.
