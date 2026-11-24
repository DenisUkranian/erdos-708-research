# Independent audit: the four-large-prime case for g(7)<=9

Verdict: the proposed argument is valid under g(4)<=5, g(5)<=6 and
g(6)<=8. It eliminates the four-large-prime residue, not the entire
seven-source problem.

## Forced source pattern

Suppose A is a counterexample requiring at least ten points and has four
active primes at least 11. Prime-support elimination forces every such
prime to divide at least three sources. Two-source peeling gives p^2>M/9
for each. Thus any two large-prime occurrences have product greater than
M/9; a third occurrence would multiply this by at least 11 and exceed M.
Every source therefore contains at most two large-prime occurrences.

Call a prime low when p<=sqrt(M), and high otherwise. A low prime has
total demand at least four: support at least four already suffices;
support exactly three with any repeated exponent also suffices; support
exactly three and all exponents one is eliminated by the square-gain
lemma, at cost g(4)+2*3-2<=9. High primes have demand at least three.

If l is the number of low primes, total demand is at least 12+l and at
most 14, so l<=2. Three high primes would require at least nine source
incidences, although every source contains at most one high prime, which
is impossible with seven sources. Thus l=2. Equality now holds throughout:
both low primes have demand four; both high primes have demand three;
all seven sources have large-prime degree two.

There are six low-high sources and one low-low source, possibly a square.
Write low primes p1,p2 and high primes q1,q2. Each cross core p_i*q_j is
greater than M/3, since p_i>sqrt(M)/3 and q_j>sqrt(M). Its source cofactor
is therefore 1 or 2, and each cross core has multiplicity at most two.

If the seventh core is p1*p2, the cross multiplicity matrix has every
row and column sum three, hence, after relabeling, is

    1 2
    2 1.

If the seventh core is p1^2, the row sums are two and four and the column
sums are three, giving

    1 1
    2 2.

Each multiplicity-two cross core occurs with source cofactors exactly
1 and 2. Hence at least one source with cofactor 2 exists, and the product
of all six cross cofactors is at most 16.

## Bank construction and valuation accounting

For each distinct core d, select m_d distinct interval multiples of d,
where m_d is its source multiplicity. Such a bank exists because
m_d<=floor(M/d). Require one bank to contain a prescribed multiple of a
full source with cofactor 2. This is possible while keeping all its bank
entries distinct.

At a union point b, the assigned core types form a simple ordinary graph
plus any loops. Let k be the number of assigned types, e the number of
ordinary edges, l the number of loops, and v the number of present primes.
The assigned demand is 2e+2l, while the point supplies at least v+l units.
The total local valuation deficit is therefore at most 2e+l-v, and

    1 + local_deficit - k <= 1+e-v.

The global prime-unit deficit is at most the sum of these local deficits:
positive parts are subadditive, and surplus valuations only help. Unit
deficits can be repaired with fresh interval points because the complete
interval product covers the full source product. Consequently the total
cover size is at most seven plus the sum of positive cycle costs 1+e-v.

In the low-square case, the ordinary graph is K(2,2). Positive cost is
one and requires all four cross edges. There is at most one such point,
because it is divisible by q1*q2>M. Thus the core needs at most eight.

In the low-low edge case, the ordinary graph is K(2,2) plus p1*p2. Every
cycle is a triangle through that low edge or the cross four-cycle.
All triangle points coincide because the low-edge bank has multiplicity
one. A triangle and a four-cycle point must also coincide: the triangle's
high vertex has a cross edge of multiplicity one, and both cycles use
that same bank. Hence all positive cycle cost occurs at one point.

If its cost is at most one, the core again needs at most eight. Cost two
requires all five distinct core types to meet at one hub. The only two
remaining bank entries come from the two multiplicity-two cross banks,
and each is different from the hub. These three points supply at least
two units of each of the four primes. Thus each low prime has deficit at
most two and each high prime deficit at most one.

Each low prime is repaired with at most one point. If a p^2-multiple is
already selected, it gives at least one extra unit beyond the preceding
two-unit baseline, so the remaining deficit is at most one; repair that
unit if necessary. If no p^2-multiple is selected, choose a fresh one,
which exists because p^2<=M, and it supplies the at-most-two-unit deficit.
Each high prime likewise needs at most one repair point. This exceptional
case therefore uses at most 3+4=7 core points.

All constructions retain the prescribed full-source point with cofactor 2.

## Completing the small factors

Write the seventh source as d0*s0, where d0 is its low-low edge or square.
Since d0>=11^2=121, s0<=M/121. The cross cofactors have product at most 16,
and the retained prescribed point already supplies a factor 2. The remaining
small-factor product Q therefore satisfies

    Q <= 8*s0 <= 8M/121 < M/9.

The core cover uses at most eight points. There are at least nine multiples
of Q in I, so a fresh multiple of Q completes all source demands in at most
nine points. The small-prime allocation does not double-count the core,
because all core primes are at least 11 and every remaining cofactor is
composed of 2,3,5,7.

This contradicts the proposed counterexample. Therefore a genuine
counterexample to g(7)<=9 has at most three active primes at least 11.

## A wording correction to the more general bank lemma

If a bank theorem promises to retain an arbitrary prescribed full-source
multiple, that source must have nontrivial selected core. A source with
core 1 does not belong to any of the banks being counted; inserting its
point can cost an extra point. The four-prime argument above explicitly
prescribes a cross source, so it satisfies this requirement.
