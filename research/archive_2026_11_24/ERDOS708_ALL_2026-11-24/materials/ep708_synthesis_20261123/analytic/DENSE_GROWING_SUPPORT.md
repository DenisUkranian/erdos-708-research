# A uniform hinge inequality for growing dense prime supports

## Status and scope

This is a partial result about the dual hinge inequality for Erdős problem 708, not a proof of the general problem. An independent internal audit checked the explicit constants, both weight regimes, the periodic approximation, and the growing-support corollary without finding a substantive error. This is not a claim of external verification.

The support may contain every prime up to a growing cutoff. Thus its reciprocal-prime mass need not remain bounded. On the other hand, the theorem does not allow arbitrary interactions between this small-prime support and larger primes. Also, if the source integers themselves are entirely supported on the polylogarithmic prime sets below, their cardinality is already small enough for the known quadratic interval-length theorem. The new statement concerns the possible support of dual obstructions; it is not claimed to close a previously untreated class of source configurations.

All logarithms are natural. For a finite prime set P, weights 0 <= w_p <= 1, and positive integers n, write

    X_w(n) = sum_{p in P} w_p v_p(n).

For a real c > 1, let H_c denote

    sum_{n <= M} (X_w(n) - c)_+
        <= sum_{b in I} (X_w(b) - 1)_+,

where I is any interval of exactly M consecutive positive integers.

## Theorem

Fix c > 1 and beta with 1/c < beta < 1. There is an explicit function F_{c,beta}(Y), for Y >= 2, such that

    log F_{c,beta}(Y) = O_{c,beta}(Y^{1+beta}),

and H_c holds whenever M >= F_{c,beta}(Y), uniformly in all finite prime sets P contained in [2,Y], all weights in [0,1], and all interval shifts.

Consequently, for every fixed theta satisfying

    0 < theta < c/(c+1),

H_c holds for all sufficiently large M, uniformly for every weight vector supported on the primes

    p <= (log M)^theta.

In particular, H_2 holds uniformly on all prime supports below (log M)^theta for every fixed theta < 2/3.

## Explicit constants

Set

    a = (1 + c beta)/2,
    g = c beta - a > 0,
    h = c - a > 0,
    B_beta = 1 / [beta (1 - 2^{beta-1})].

Here 1 < a < c beta < c. Use log^+(u) = max(0,log u), and choose

    A = 1 + max {
        g,
        (g/h)(log 2 + 1/beta),
        B_beta + log^+(2/[e beta(a-1)]) + 1/beta
    }.

For Y >= 2 define

    rho_0 = g / (A Y^beta),
    delta = ((c-1)/Y) exp(-c/rho_0),
    L = c/rho_0
        + log max { 1, 2Y(1+log Y)/(c-1) }.

One valid threshold is

    F_{c,beta}(Y)
      = [4Y^2/(c-1)] (L/log 2 + 1)
        exp { Y(L+log Y) + c/rho_0 }.

No assertion of practical numerical efficiency is made for these constants.

## 1. A uniform exponential-moment bound

For any P contained in [2,Y], put

    C_P(beta) = product_{p in P} (1-1/p)/(1-p^{beta-1}).

Because 0 < p^{beta-1} <= 2^{beta-1} < 1,

    log C_P(beta)
      <= sum_{p in P} -log(1-p^{beta-1})
      <= [1/(1-2^{beta-1})] sum_{m=2}^{floor Y} m^{beta-1}
      <= B_beta Y^beta.                                      (1)

The last step uses the decreasing function t^{beta-1} and its integral over [1,Y].

The case P empty is immediate. Otherwise let

    rho = max_{p in P} w_p/log p.

If rho = 0, both hinges vanish. Otherwise set t = beta/rho. Then t w_p <= beta log p. The function f(n) = exp(t X_w(n)) has a nonnegative divisor expansion f(n) = sum_{d|n} h(d), where h is multiplicative and

    h(p^j) = exp(t j w_p) - exp(t(j-1)w_p) >= 0.

For primes outside P these coefficients vanish. Therefore

    sum_{n<=M} exp(t X_w(n))
      = sum_d h(d) floor(M/d)
      <= M sum_d h(d)/d
      = M product_{p in P} (1-1/p)/(1-exp(t w_p)/p)
      <= M C_P(beta).                                       (2)

Every Euler factor converges because exp(t w_p)/p <= p^{beta-1} < 1. The elementary inequality

    (u-c)_+ <= exp(t(u-c))/(e t)

now gives

    sum_{n<=M}(X_w(n)-c)_+
      <= M [rho C_P(beta)/(e beta)] exp(-beta c/rho).           (3)

## 2. Small weights: H_c at every length

Suppose 0 < rho <= rho_0. The explicit choice of A ensures

    Y exp(-h/rho) <= 1/2,                                    (4)

and

    [2Y C_P(beta) rho/(e beta(a-1))] exp(-g/rho) <= 1.          (5)

Here are direct checks. Both left sides increase with rho, so it suffices to use rho = rho_0. We have rho_0 <= 1. For (4),

    h/rho_0 = (hA/g)Y^beta
      >= (log 2 + 1/beta)Y^beta >= log(2Y),

using log Y <= Y^beta/beta. For (5), the logarithm of its left side at rho_0 is at most

    log^+(2/[e beta(a-1)]) + log Y
      + B_beta Y^beta - A Y^beta <= 0,

by (1), rho_0 <= 1, Y^beta >= 1, and the defining lower bound for A.

Since X_w(n) <= rho log n, the prefix hinge vanishes if M <= exp(c/rho). Otherwise choose a prime p attaining rho and put

    j = ceil(a/w_p),       D = p^j.

Then

    j w_p - 1 >= a-1,
    D <= Y exp(a/rho) <= (1/2)exp(c/rho) < M/2,

where (4) was used. Every interval I contains at least floor(M/D) >= M/(2D) multiples of D. Hence

    sum_{b in I}(X_w(b)-1)_+
      >= [(a-1)M/(2Y)] exp(-a/rho).                           (6)

The ratio of the right side of (3) to the right side of (6) is bounded by the left side of (5). This proves H_c for every M in the small-weight regime.

## 3. The remaining weights: periodic approximation with individual exponents

Assume rho >= rho_0. For every p in P choose

    T_p = ceil(L/log p),
    Z_w(n) = sum_{p in P} w_p min(v_p(n),T_p).

Then Z_w is periodic with period

    R = product_{p in P} p^{T_p},

and is bounded by

    B = sum_{p in P} T_p <= Y(L/log 2 + 1).                  (7)

Choose a prime p with w_p/log p >= rho_0 and set

    j = ceil(c/(rho_0 log p)).

Since L >= c/rho_0, we have j <= T_p. On every multiple of p^j,

    Z_w(n) >= w_p j >= c.

The nonnegative periodic function

    (Z_w(n)-1)_+ - (Z_w(n)-c)_+

equals c-1 at such positions. Its average over a complete period is therefore at least

    (c-1)p^{-j} >= ((c-1)/Y) exp(-c/rho_0) = delta.            (8)

Only the prefix truncation error is needed. The identity

    (v_p(n)-T_p)_+ = sum_{j>T_p} 1_{p^j|n}

gives

    sum_{n<=M}(X_w(n)-Z_w(n))
      <= M sum_{p in P} w_p/[p^{T_p}(p-1)]
      <= M exp(-L) sum_{p<=Y} 1/(p-1)
      <= M exp(-L)(1+log Y)
      <= M delta/2.                                         (9)

The last inequality follows from the definition of L, including the case where the maximum appearing there equals 1.

Each of the two truncated hinges is nonnegative, bounded by B, and R-periodic. Its sum over any interval of length M differs from M times its full-period mean by at most RB. The hinge function is 1-Lipschitz, and the interval hinge can only decrease under truncation. Combining (8) and (9),

    Delta_c := sum_{n<=M}(X_w(n)-c)_+
                 - sum_{b in I}(X_w(b)-1)_+
      <= -delta M + 2RB + M delta/2
      = -delta M/2 + 2RB.                                   (10)

Thus H_c holds when M >= 4RB/delta. Finally,

    log R = sum_{p in P} T_p log p
      <= |P|L + sum_{p in P} log p
      <= Y(L+log Y).

Together with (7), this bounds 4RB/delta by the displayed F_{c,beta}(Y), completing the uniform proof.

## 4. The growing-support consequence

The constants c and beta are fixed. The definitions give

    1/rho_0 = O_{c,beta}(Y^beta),
    L = O_{c,beta}(Y^beta),
    log F_{c,beta}(Y) = O_{c,beta}(Y^{1+beta}).

Given theta < c/(c+1), choose beta with

    1/c < beta < 1,
    theta(1+beta) < 1.

For Y = (log M)^theta,

    log F_{c,beta}(Y)
      = O_{c,beta}((log M)^{theta(1+beta)}) = o(log M).

Consequently M >= F_{c,beta}(Y) for all sufficiently large M. This proves the corollary uniformly over all weights and shifts.

## What this does and does not establish

1. The support may be the full set of primes below (log M)^theta. The theorem therefore handles growing dense dual supports whose unweighted reciprocal-prime mass is unbounded.
2. The threshold is uniform over the weights, including weights tending to zero with M. This is the reason for the separate exponential-moment argument.
3. The statement is valid for every c > 1, with a c-dependent exponent range and length threshold. No uniformity as c decreases to 1 is asserted.
4. There is no composition theorem here for combining a small-prime hinge inequality with a large-prime hinge inequality at the same threshold. Proving the separate inequalities does not establish H_c for the sum of the two loads.
5. The theorem concerns dual weight supports. It is not claimed as a new improvement over the known M >= 16n^2 theorem when every source integer is itself supported on these small primes.

