# A simple exact nine-point witness for g(7)

Take

    A={289,323,361,391,437,493,551}
     ={17^2,17*19,19^2,17*23,19*23,17*29,19*29}.

Then M=max(A)=551 and

    product(A)=17^5*19^5*23^2*29^2.

Set

    N=17^2*19^2*23*29=69,587,443,
    I={N-275,...,N+275}.

Thus I is the interval [69,587,168,69,587,718] of exactly 551 positive integers, corresponding to shift x=69,587,167.

## Lower bound

At N the valuations at (17,19,23,29) are (2,2,1,1). Every other point of I is divisible by at most one of these four primes. Indeed, if b=N+d, 0<|d|<=275, were divisible by two of them, their product would divide d, whereas their smallest pair product is 17*19=323>275.

Moreover, every off-center point has 17- and 19-valuations at most one. A second power would divide both N and b and hence d, but 17^2=289 and 19^2=361 exceed 275.

If a covering set contains N, its remaining demands are (3,3,1,1). Since off-center points serve at most one active prime and the first two valuation caps are one, at least 3+3+1+1=8 further points are needed. The cover has at least nine points.

If a covering set omits N, the 17- and 19-demands require at least five points each, and the 23- and 29-demands require at least one point each. These four groups are disjoint, so at least twelve points are needed. No restriction on the off-center 23- or 29-valuations is needed for this argument.

Consequently tau(A,I)>=9, and hence g(7)>=9.

## Matching nine-point cover of this instance

Use the offsets

    0,17,34,51,19,38,57,23,29

from N. They give nine distinct points in I. The center supplies 17^2*19^2*23*29; the three positive multiples of 17 supply three more 17-units, the three positive multiples of 19 supply three more 19-units, and offsets 23 and 29 supply the two remaining units. Their product is divisible by product(A). Therefore tau(A,I)=9 exactly.

## Verification

`python3 g7_exact/verify_lower9_simple.py` checks the source factorization, every point's off-center restrictions, both lower-bound budgets, interval membership and distinctness of the displayed cover, and its exact product divisibility. It uses only Python's standard library and integer arithmetic.

The recorded output is `g7_exact/lower9_simple_verification.json`.
