# Complete audit of the 32 n^(5/2) minimal-counterexample argument

Date: 2026-11-23. Reconstructed from the supplied summary of dot's
argument. The proof below is rigorous. Its range is already covered by
the stronger known quadratic long-interval theorem; it is not a new
best general bound.

## Theorem

For every set `A` of `n` distinct integers in `[2,M]` and every
positive interval `I` of `M` consecutive integers,

`M>=32 n^(5/2)` implies a product cover with at most `2n` positions.

The ambient length `M` is held fixed during induction; it is not reset
to the maximum of a smaller source set.

## 1. Basic minimal-counterexample facts

Induct on `n`. The case `n=1` is immediate. Suppose `n>=2` and the
claim fails, while it holds for smaller source sets at this same
ambient length. Put

`K=2n-1`, `c=M/K^3`, `L=M/K=cK^2`.

For every source `a`, every cover `B_a` of `A\{a}` with at most
`K-1` positions contains all interval multiples of `a/q`, for every
prime `q|a`; otherwise that quotient and at most one further prime
unit cover `a`. As proved in `PAIR_BANK_AND_CORE_REDUCTION.md`, this
gives

`q<K` for every source prime, and `a/q>L` for every prime occurrence.

There is also no source divisor in

`(K,L]`.                                                       (1.1)

Indeed, if `d|a` and `K<d<=L`, choose a fresh multiple of `d`, which
has at least `K` candidates. The complementary factor `a/d` has at
least `d>=K+1` candidates, so a fresh complementary multiple is still
available after the first addition. Together they cover `a` in two
new positions. The full interval supply ensures the usual unit
repairs used above.

If `c>=1`, every source exceeds `L>=K^2`. Its numerically least
divisor above `K` is less than `K^2`, since all its prime factors are
less than `K` and all proper divisors are at most `K`. This contradicts
(1.1). Hence assume `0<c<1`.

The numerical hypothesis gives

`c=M/K^3 >= 32n^(5/2)/(2n-1)^3 > 4/sqrt(n)`,

so in particular

`c^2K>=1`.                                                     (1.2)

The rest of the structural argument uses only `0<c<1` and (1.2).

## 2. A divisor above K has a large prime occurrence

Take the least divisor `d>K` of a source. It exists because every
source exceeds `L>K`. Every proper divisor of `d` is at most `K`.
If `Omega(d)>=3`, remove its smallest prime. The remaining divisor
is at least `d^(2/3)`, so `d<=K^(3/2)<=cK^2=L`, contradicting (1.1).
The divisor cannot be prime, because every source prime is below `K`.
Thus `d=pq` for two prime occurrences, and its larger prime satisfies

`q>sqrt(c) K`.                                                  (2.1)

## 3. The small part and the exact three-large-occurrence structure

Put `U=1/sqrt(c)`. No source divisor lies in `(U,cK]`.
Indeed, such a divisor `t` would be smaller than the prime `q` from
(2.1), since `q>sqrt(c)K>cK`. Thus `qt|a`, and

`K<qt<cK^2=L`,

contradicting (1.1).

Every source prime therefore is either at most `U` or greater than
`cK`. The full part `u` supported on primes at most `U` satisfies

`u<=U`.                                                       (3.1)

Otherwise its least divisor above `U` would be at most
`U^2=1/c<=cK`, again forbidden. This step uses `c^2K>=1`.

Call occurrences greater than `cK` large. Two large occurrences have
product greater than `c^2K^2>=K`, so (1.1) forces every such pair
product above `L`. Four large occurrences would therefore have
product greater than `L^2>M`, because `cK>1`. There are at most three.

There cannot be at most two: delete a prime occurrence so that the
quotient contains at most one large occurrence. This quotient is at
most `UK=K/sqrt(c)<=cK^2=L`, contradicting the forced-bank condition
`a/q>L`. The inequality follows from `c^(3/2)K>1`, itself a consequence
of `c^2K>=1` and `c<1`.

Consequently every source is exactly

`a=u p q r`, with `u<=U`,                                     (3.2)

where `p,q,r` are three large prime occurrences, with repetition
allowed. No assumption bounding `Omega(a)` was made: the small part
may contain repeated prime factors.

## 4. The essential-demand step

This is the step that needs more than forced-bank inclusion.

Fix any large prime occurrence `p` in a source (3.2). The other two
large occurrences have product above `L=cK^2`, so one of them, say
`q`, satisfies `q>sqrt(c)K`. Also `pq>L>K`.

The two-prime removal lemma from `PAIR_BANK_AND_CORE_REDUCTION.md`
therefore applies and gives

`D_p(A)>v_p(product C_q(a))>=|C_q(a)|>=q>sqrt(c)K`.              (4.1)

For completeness: if the full `p`-demand were already covered by
`B_a`, choose a fresh multiple of `a/(pq)`, possible because there
are at least `pq>K` such targets, and repair at most one remaining
`q`-unit. This contradicts minimality. The argument also covers
repeated primes.

Let `h` be the number of distinct large primes in the source set.
There are exactly `3n` large-prime occurrences across all sources.
Hence (4.1) implies

`h<3n/(sqrt(c)K)<=2/sqrt(c)=2U`,                               (4.2)

where `n>=2` was used.

## 5. Counting distinct sources

By unique factorization, (3.2) describes at most

`floor(U) binomial(h+2,3)`

distinct integers. Since `U>1` and `h<2U`, this is less than

`U (4U)^3/6 = 64/(6c^2)`.

But `c>4/sqrt(n)` gives

`64/(6c^2)<(2/3)n`,

a contradiction. This completes the induction and the theorem.

## Audit conclusion and what it does not prove

The `32 n^(5/2)` route is valid once the essential-demand argument in
Section 4 is supplied and the hypotheses `0<c<1`, `c^2K>=1` are made
explicit. Bank inclusion alone would not justify (4.1).

This derivation does not establish a quadratic threshold. For
`M=C n^2` with fixed `C`, the parameter `c=M/K^3` is of order `1/n`,
so `c^2K>=1` fails as `n` grows. One cannot carry the exact
three-large-occurrence classification into that regime without a
different argument. The claimed quadratic word sketch must therefore
be audited separately. The already verified Wang theorem
`M>=16n^2 => tau<=2n` is a stronger independent result.

