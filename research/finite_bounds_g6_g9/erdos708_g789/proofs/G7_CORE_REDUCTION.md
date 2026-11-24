# A rigorous reduction for an attempted nine-element upper bound

Assume the verified bounds g(5)<=6 and g(6)<=8. This note does **not** prove
g(7)<=9; it restricts any possible counterexample.

## Two removed primes can share one repair slot

Let A contain seven distinct source integers, with maximum M. Suppose two
distinct sources a,b have prime divisors p|a and q|b satisfying

    p>=8, q>=8, and pq<=M/9.

The primes may coincide. Cover the other five sources in at most six
elements of I. Since a/p<=M/p and b/q<=M/q, each cofactor has at least eight
multiples in I. Choose unused multiples of a/p and b/q successively; after
these choices at most eight interval elements have been used. Finally pq
has at least nine multiples, so an unused multiple of pq exists. These
at most nine elements cover the full product of A. All inequalities are
integer-safe: pq<=M/9 means 9pq<=M.

## Supports of one or two sources

If a prime P>=11 divides exactly one source a=P^e u, cover the other six
sources in at most eight picks. Choose a multiple m of a in I. If m was
unused, adding it gives nine. If m was already selected, its P^e supply
is free because none of the other source demands uses P. An unused
multiple of u exists (there are at least P>=11 such multiples), and
adding it gives nine.

If P>=11 divides exactly two sources a=P^e u and b=P^f v, with e<=f and
P not dividing uv, cover the other five sources in at most six picks.
Choose a multiple m of b. Two distinct sources divisible by P^e and
bounded by M imply 2P^e<=M, so there are at least two multiples of P^e in I.
Supply the total P^{e+f} by m and, if needed, another such multiple.
If m was new, the cofactor v is supplied together with m; one unused
multiple of u completes the cover in at most nine picks. If m was already
selected, P is still free relative to the other five source demands;
at most one new P^e multiple and two unused cofactor multiples u,v complete
the cover. Both cofactors have at least P>=11 multiples, so these choices
can be made outside all earlier picks. Again the total is at most nine.

## Consequence for the unresolved large-prime part

Suppose a seven-source counterexample to the nine-element bound exists.
Every active prime P>=11 then satisfies:

1. P divides at least three source integers.
2. P>sqrt(M)/3. Otherwise choose any two sources containing P and apply
   the first lemma with p=q=P, because P^2<=M/9.
3. Each source contains at most two such large-prime occurrences,
   counting multiplicity. If M>729, then (sqrt(M)/3)^3>M. If M<=729,
   the product of three such occurrences is at least 11^3=1331>M.

Consequently there are at most four distinct active primes P>=11, since
each appears in at least three sources while the total number of their
occurrences is at most 2*7=14.

After removing those at most four primes, all source cofactors are
{2,3,5,7}-smooth. A source containing two large-prime occurrences has
smooth cofactor at most 8, because their product is strictly greater
than M/9. A source containing one large-prime occurrence has smooth
cofactor less than 3sqrt(M).

This is a structural reduction only. The at-most-four-large-prime cases
with their smooth cofactors remain unproved for the target bound nine.
