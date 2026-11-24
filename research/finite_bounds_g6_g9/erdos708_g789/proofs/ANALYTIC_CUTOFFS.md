# Rigorous smooth-source analytic tails for Erdős 708

These results concern the at-most convention. Let A consist of n distinct
positive integers at least 2, put M=max A, and let I be any M consecutive
positive integers. A cover is a subset of I whose product is divisible by
the product of A.

## 1. Removing one prime factor

Assume every (n-1)-element source set admits a cover of at most r elements.
If some a in A has a prime factor p for which

    floor(M / (a/p)) >= r+1,

then A admits a cover of at most r+2 elements in every I.

Proof: Cover A\{a} by B0 of size at most r, using a subinterval of I of
length max(A\{a}) if needed. Choose an unused multiple b of a/p in I.
Then B1=B0 union {b} covers (product A)/p and has size at most r+1.
If B1 already covers product A, finish. Otherwise its only possible deficit
is exactly one unit of p-adic valuation. Since the distinctness of A gives
product A | M!, and M! divides the product of any M consecutive positive
integers, at least one element c of I\B1 is divisible by p. Adding c repairs
the last deficit and gives at most r+2 elements. This argument also handles
prime powers in a: only one copy of p is removed.

In particular, p>=r+1 is sufficient, since a<=M. A counterexample to the
r+2 bound must therefore use only primes at most r. It must also satisfy
a/p>M/(r+1) for every source a and every p|a.

Consequences, with the prior bounds explicitly separated:

* Given g(5)<=6, proving g(6)<=8 reduces to {2,3,5}-smooth source sets.
* Given g(6)<=8, proving g(7)<=10 reduces to {2,3,5,7}-smooth source sets.
* Given g(7)<=10, proving g(8)<=12 reduces to {2,3,5,7}-smooth source sets.
* Given g(8)<=12, proving g(9)<=14 reduces to {2,3,5,7,11}-smooth source sets.

These are reductions, not proofs that the reduced finite ranges pass.

## 2. Distinctness bounds the largest-prime demand

For any fixed prime p, let q_i=p^{v_p(a_i)}, arranged in nonincreasing
order q_1>=...>=q_n. For each i, all of the corresponding first i source
integers are distinct multiples of q_i: powers of a common prime are
nested under divisibility. Thus i*q_i<=M. Multiplying gives

    p^{sum_a v_p(a)} = product_i q_i <= M^n/n!.

The argument does not require the a_i to have different p-adic valuations.

## 3. A self-contained descending prime packing lemma

For t>n slots, set C_j=floor(M/j), 1<=j<=t. Take all prime factors of
Q=product A, with multiplicity, in nonincreasing order. Assign each factor
to any bin whose current product remains at most its capacity. If this
procedure fails at prime p, and p<=C_t, then every current bin product B_j
satisfies

    B_j >= max(floor(M/(jp))+1, p).

Indeed, failure gives B_j*p>C_j. No bin is empty, since p<=C_t, and every
factor already assigned is at least p. Consequently the part Q_{>=p} of Q
supported on primes at least p satisfies

    Q_{>=p} >= T_p(M)
             := p * product_{j=1}^t max(floor(M/(jp))+1, p).

The extra factor p is the prime whose placement failed. For every p,
Q_{>=p}<=M^n; when p is the largest allowed source prime, Section 2 improves
this to Q_{>=p}<=M^n/n!.

If all prime factors pack successfully, call the resulting bin products
h_1,...,h_t (empty products may be dropped). Since h_j<=floor(M/j), I has
at least j multiples of h_j. Choose a multiple of h_j outside the at most
j-1 previously chosen interval elements. Their product is divisible by
Q, so this is a cover of size at most t. No cumulative-GCD theorem or
external slot-packing theorem is needed.

## 4. A finite check proves an infinite analytic tail

The strict inequality floor(M/(jp))+1>M/(jp) implies

    T_p(M) > M^t/(t! p^{t-1}).

Let d_p=n! for the largest allowed prime and d_p=1 otherwise. Hence the
packing criterion T_p(M)>M^n/d_p holds whenever

    d_p * M^{t-n} > t! * p^{t-1}.

The script analytic_cutoffs.py computes the least integer coarse threshold
using integer binary search, checks the finitely many smaller M by the
exact product T_p(M), and thereby proves the following infinite tails:

| n | slots t | allowed primes | all M at least |
|---|---|---|---|
| 6 | 8 | 2,3,5 | 9360 |
| 7 | 10 | 2,3,5,7 | 19170 |
| 8 | 12 | 2,3,5,7 | 12320 |
| 9 | 14 | 2,3,5,7,11 | 24206 |

For n=6, the last failed arithmetic inequality at p=3 is M=9359. For n=7,
the last failed inequality at p=5 is M=19169. These failures only mean that
this sufficient packing estimate fails; they do not exhibit mathematical
counterexamples.

Thus, given the indicated prior small-n bounds, only the corresponding
smooth source sets with M<9360 or M<19170 remain to be checked. The interval
shift x is not checked by this analytic argument and remains arbitrary.
The tail itself is universal in x because the distinct-multiple construction
uses only the length of I.

## Status

This note proves the reductions and analytic tails. It does not assert
g(6)=8 or g(7)<=10 without a separate verified treatment of the finite
smooth source sets. In particular, it supplies no proof that g(7)=9.

## Independent finite checks completed separately

The adjacent check_g6_independent.py enumerates every actual eligible six-source
subset below 9360 and validates the 277 cumulative-GCD certificates it uses.
It does not import the Pareto search code. Its run checked 1,045,917 source
subsets and returned PASS.

The adjacent check_smooth_exhaustive.cpp is a second independent checker for
the seven- and eight-source reductions. It trial-factors every integer below
the respective cutoffs, calculates rigorous rough-part envelopes to eliminate
entire values of M, and enumerates every actual remaining source subset. For
each distinct product demand it checks a direct prime-union bound, an explicit
ordinary slot-packing witness, or a separately validated cumulative-GCD witness.
It imports no Pareto frontier code and does not trust the source generator.

The n=7 run checked 23,743,770 actual subsets after rough-envelope pruning;
the n=8 run checked 599,136,880. Both returned PASS. Thus the finite portions
support g(7)<=10 and g(8)<=12, given g(5)<=6 and the intervening verified
six-source result. The external g(5)<=6 theorem is attributed to Tripodo,
"Sharp finite cases of the Erdős–Surányi interval-product problem", version
https://hexagonmath.org/pdf/2611.00694v1 . These checks do not independently
rebuild the cited Lean development for g(5).

The n=9 run also returned PASS. It considers all 701 eligible smooth maxima
below 24206. A global rough-part envelope discharges 500 maxima; for the
remaining 201 it covers 137,818,182,175 possible source subsets, using
rigorous recursive rough-part and prime-union envelopes to discharge most
branches at once. It directly checks 3,611,037 distinct leaf demand vectors.
All 74 cumulative-GCD certificates are validated independently before this
enumeration. The result is recorded in g9_independent_fast_result.json.

The recursive prime-union envelope at a branch adds the current demand
to, in each prime coordinate independently, the sum of the largest required
number of exponents among future candidates. This vector dominates every
completion. The recursive rough-part envelope multiplies the current rough
part by the product of the largest required number of rough parts among
future candidates. If all rough-part bounds are strictly below the failure
thresholds T_p(M), every completion packs successfully. These two pruning
rules are sufficient bounds and do not depend on the original Pareto code.

The C++ checker uses exact integer arithmetic throughout. Its global
rough-part envelopes use a small base-10^9 positive-integer implementation;
the recursive n=9 envelopes use unsigned 128-bit integers only after
asserting M<=4000. Then M^9<2^128, and all relevant source-product upper
bounds fit. Failure thresholds are safely saturated at M^9+1. Assertions
must remain enabled (do not compile with -DNDEBUG).

Reproduction examples after compiling check_smooth_exhaustive.cpp with
g++ -O3 -std=c++17:

    ./check_smooth_exhaustive 7 10 19170 4 certificates7.txt
    ./check_smooth_exhaustive 8 12 12320 4 certificates8.txt
    ./check_smooth_exhaustive 9 14 24206 5 certificates9.txt

Taken together with the analytic tails and the prior g(5)<=6 theorem,
the finite checks prove g(6)<=8, g(7)<=10, g(8)<=12, and g(9)<=14.
They do not identify the exact values of g(7), g(8), or g(9).
