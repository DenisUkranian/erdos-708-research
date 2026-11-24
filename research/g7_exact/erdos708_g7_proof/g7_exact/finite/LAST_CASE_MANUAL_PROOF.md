# A direct nine-point cover for the final one-large-prime demand

24 November 2026. This is an independent, noncomputational certificate for the last demand left by the one-large-prime enumeration.

**Claim.** Every interval I of 55 consecutive positive integers contains at most nine distinct points whose product is divisible by

    2^4 * 3^9 * 5^2 * 11^4.

**Proof.** There are at least two multiples of 27 in I. Choose two consecutive ones, u and v. Exactly one of them is even, hence exactly one is a multiple of 18. Since I contains at least floor(55/18)=3 multiples of 18, choose a fresh multiple w of 18 outside {u,v}. Since I contains at least floor(55/6)=9 multiples of 6, choose a fresh multiple t of 6 outside {u,v,w}.

The four distinct points u,v,w,t supply at least 3+3+2+1=9 units of 3-adic valuation. They also include three distinct even points: one of u,v, together with w and t. Their product is therefore divisible by 2^3 * 3^9.

Choose any multiple z of 50 in I, which exists because 50<=55.

- If z is not among the four selected points, adjoining it supplies an additional factor 2*5^2.
- If z is already selected, the factor 5^2 is already supplied without using it in the previous demand accounting. Adjoin any fresh even point; there are at least 27 even points in I. This supplies the one possibly missing unit of 2-adic valuation.

Thus in both cases at most five points cover 2^4 * 3^9 * 5^2.

Finally, I contains at least floor(55/11)=5 distinct multiples of 11. Choose four of them to cover 11^4, and unite this set with the preceding five-point cover. The two demands concern disjoint prime sets, so overlaps between the two selected sets are harmless. The union has at most nine elements and its product is divisible by the stated demand. QED.

The argument applies to every shift of the interval and does not use any hypothesis on its originating seven-source set. In the enumeration's five-coordinate order (2,3,5,7,11), it certifies the demand (4,9,2,0,4), and every coordinatewise smaller demand.

This argument is independent of the CRT enumeration. The generic CRT checker also returned `ALL_PASS` for this demand: 309 recursion nodes and 11 exact multicover calls. That computation is corroboration; the elementary proof above is a complete certificate by itself.
