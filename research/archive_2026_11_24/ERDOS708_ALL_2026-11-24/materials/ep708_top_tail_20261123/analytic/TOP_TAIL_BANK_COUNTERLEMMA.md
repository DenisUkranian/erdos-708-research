# Primewise bank-product dominance still fails for a complete hot top tail

## Status and purpose

The source set in this note is the complete strict superlevel of clipped prime load two, not merely an arbitrary divisor upset. Every source has load at least 11/5. Nevertheless the union of all prime-deletion banks has a deficit in one prime row.

This rules out the intermediate assertion that the top-tail condition and source load greater than two, by themselves, imply coordinatewise bank-product dominance. It does not refute a weighted joint inequality, optimal-row balance, or the requested unrestricted asymptotic. In particular, the weights below are not asserted to be optimal for the new source set.

## 1. Previously verified arithmetic certificate used here

Use the exact CRT certificate already recorded in

    ep708_global_20261123/combinatorial/BANK_PRODUCT_COUNTEREXAMPLE.md

and its adjacent `bank_product_certificate.json` and verifier. Its numerical data are

    N=11763, H=5881, p=11777, M=pN=138532851.

There is a specified integer C for which the N-term interval

    J={C-H,...,C+H}

has the following certified properties:

1. None of its elements is divisible by p.
2. The union

       V={t in J:some prime r<=N/2 divides t}

   has exactly 10352 elements.
3. Every one of the 1411 elements of J outside V avoids **all** primes at most N, not just those at most N/2.
4. There are exactly 10353 composite integers between 4 and N.

Take the M-term positive interval

    I={p(C-H-1)+1,...,p(C+H)}.

Its p-multiples are exactly pt with t in J, and each has p-adic valuation one. The CRT certificate and its independently verified arithmetic are unchanged; the new step below is to enlarge the source set to a full hot superlevel.

## 2. Complete top-tail source set

Let

    P={p} union {r:r is prime and r<=N},
    w_p=1,
    w_r=3/5 for every prime r<=N, and w_r=0 otherwise,
    X(a)=v_p(a)+(3/5) sum_{r<=N, r prime}v_r(a).

Define

    A_*={a in {2,...,M}:X(a)>2}.                         (1)

Since p^2>M, selected sources divisible by p have at least two occurrences from primes at most N, and selected sources not divisible by p have at least four. Their loads are therefore at least 11/5 and 12/5, respectively. Unselected loads are at most 9/5. If n_*=|A_*|, it is exactly the set of the n_* largest loads on {2,...,M}, with a strict gap between selected and unselected values. It is a divisibility upset. Also M=pN belongs to A_*, since N=3^2*1307 and X(M)=14/5. Hence max A_*=M.

Every selected source has X(a)>=11/5>2. All prices are exact clipped rational numbers. Source prime factors outside P may occur; their weights are zero, as permitted in the raw dual. The additional exact sieve count in Section 5 gives n_*=56063090 and verifies 2n_*<M<16n_*^2. This is a cardinality check for the stated counterlemma, not a computation of g(n).

The complete superlevel also has the full price-monotone exchange property: if a belongs to A_*, q divides a, r is prime with w_r>=w_q, and ar/q<=M, then ar/q belongs to A_*. Its load is X(a)-w_q+w_r>=X(a)>2. Thus this exchange property, together with the strict top-tail condition, also does not suffice for the coordinatewise assertion refuted below.

## 3. The exact deficient prime row

For any source set A, write

    U(A,I)=union_{a in A} union_{q prime,q|a}
               {b in I:a/q divides b}.

Since p>N, one has p^2>M=pN. Every source divisible by p is uniquely a=ps with s<=N and has p-adic valuation one. All prime factors of s belong to P. Therefore

    ps in A_*  iff  s is composite,
    D_p(A_*)=10353.                                    (2)

Now consider a target pt with t in J.

If t is outside V, the certified avoidance of every prime at most N and the condition p does not divide t give

    X(pt)=1.

For every a in A_* and every prime divisor q of a,

    X(a/q)=X(a)-w_q>=6/5>1.

Thus a/q cannot divide pt. This proves pt is outside U(A_*,I).

Conversely, if t belongs to V, choose a prime r<=N/2 dividing t. The source

    a=2rp<=pN=M

has load 11/5 and belongs to A_*, including r=2 where the repeated small prime contributes two copies of 3/5. Deleting the prime occurrence 2 gives the quotient rp, which divides pt. Hence pt belongs to U(A_*,I).

We have proved the exact identity

    U(A_*,I) intersect pZ={pt:t in V}.

Every such target has p-adic valuation one, so

    V_p(U(A_*,I))=10352<10353=D_p(A_*).                 (3)

Consequently the product of the complete hot top-tail source set does not divide the product of its full prime-deletion bank union.

No enumeration of A_* or new search for the original covering function is used. Equations (2)--(3) follow from the already checked length-N CRT certificate and the complete-superlevel definition.

## 4. Why this is not a counterexample to the required statement

The conditions checked here are exact top-tail selection, maximum source M, clipped weights, and source loads greater than two. They do not include the tight active-row conditions of an optimal raw solution.

For an actual optimal raw pair, every hot target is saturated, and therefore every active prime satisfies

    V_p(U(A,I))<=D_p(A).

In fact, the two-row calculation in Section 5 shows that the displayed weights cannot be optimal on any interval of this length. The example is not a minimal raw failure. Those missing conditions cannot be silently supplied.

The remaining viable bank route must use the full joint weighted balance, or derive a contradiction from all the active rows simultaneously. It cannot replace that task by coordinatewise bank-product dominance based only on top-tail closure and load greater than two.

## 5. Exact size and a certified failure of the active two-row balance

The source parameters were additionally checked by an integer prime-power
sieve in ../audit/count_top_counterexample.py. It forms Omega_Q on the prefix
by adding one for every divisibility p^j, selects Omega_Q>=4, and also selects
the p-multiples with Omega_Q>=2. This is exactly (1), since p^2>M.
The saved output is ../audit/count_top_counterexample.json. It gives

    n_*=56063090,        n_*/M=0.4046916640732385...,
    D_2(A_*)=101157183,
    2n_*=112126180<M=138532851<16n_*^2.

The displayed weights are provably nonoptimal, not merely unchecked.
Every target multiple of 4 has load at least 6/5 and would therefore have
z_b=1 in any paired optimum with these weights. Its raw two-row supply
on any length-M interval is at least

    2 floor(M/4)+sum_{j>=3}floor(M/2^j)=103899623.

This exceeds D_2(A_*) by 2742440. Because w_2=3/5>0, the active row
would have to be an equality; it cannot be. The example therefore
demonstrates both the failure of top-tail bank-product dominance and
the indispensable extra force of actual simultaneous optimal-row balance.

The sieve does not solve a covering problem and does not compute g(n).
