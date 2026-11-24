# Dense prime supports below exp(o(sqrt(log M)))

## Status

This is a further partial result developed jointly with the parent research agent. Its proof replaces the full periodic approximation by a sieve approximation. A separate internal audit checked the Rankin bound, the exact smooth-part decomposition, the uniform sieve errors, and the integer-cover consequence without finding a substantive error. This is not a claim of external verification, and it does not settle unrestricted Erdős problem 708.

Unlike the earlier polylogarithmic support theorem, the covering consequence below is not restricted to source families already forced into the known quadratic long-interval regime by their small cardinality.

## 1. Uniform approximate hinge theorem

For each epsilon>0 there are constants gamma_epsilon>0 and M_epsilon such that the following holds. Suppose M>=M_epsilon,

    2<=Y<=exp(gamma_epsilon sqrt(log M)),

and X(n)=sum_{p in P}w_p v_p(n), where P is any subset of the primes at most Y and 0<=w_p<=1. Then every positive interval I of M consecutive integers satisfies

    sum_{a<=M}(X(a)-2-epsilon)_+
        <= sum_{b in I}(X(b)-1)_+.                          (1)

The statement is uniform over the support, weights, and interval shift.

Let eta_epsilon be any small-weight threshold from `DIFFUSE_RAW_WEIGHTS.md`. Define

    J_epsilon=ceil(2/eta_epsilon),
    gamma_epsilon=[16(J_epsilon+5)]^{-1/2}.                 (2)

This gamma is one valid choice; M_epsilon is then sufficiently large. No practical size claim is made for either constant.

Consequently, if Y=Y(M) satisfies

    log Y=o(sqrt(log M)),

then for every fixed epsilon>0, (1) holds for all sufficiently large M. One example is

    Y=exp((log M)^a),       0<a<1/2.

A fixed positive multiple gamma sqrt(log M) in the exponent is allowed for a fixed epsilon with sufficiently small gamma. The argument does not give one fixed gamma>0 working simultaneously for all epsilon tending to zero.

## 2. The geometric reference distribution

The empty support is trivial. Otherwise let

    theta_P=product_{p in P}(1-1/p).

Give each P-smooth positive integer h mass theta_P/h. This is a probability distribution, since its total mass is the corresponding convergent Euler product times theta_P. Under this distribution,

    E X=sum_{p in P}w_p/(p-1)<=1+log Y.                    (3)

Write g_j(x)=(x-j)_+, for j=1,2. If some weight w_p>=eta_epsilon, let j=ceil(2/w_p). Then j<=J_epsilon, and X(h)>=2 on all h divisible by p^j. Since g_1-g_2 equals one when X>=2 and is nonnegative everywhere,

    E[g_1(X)-g_2(X)] >= p^{-j} >= Y^{-J_epsilon}.           (4)

This is the positive gap that will dominate the sieve and tail errors.

## 3. Uniform tail estimate

Put

    u=log M/log Y,
    H=sqrt(M),
    sigma=1/(4log Y),
    R=sum_{h>H, h P-smooth} X(h)/h.

The raw load satisfies X(h)<=log h/log 2. Rankin's inequality gives

    R <= [H^{-sigma}/log 2]
            sum_{h P-smooth} (log h)/h^{1-sigma}.           (5)

For p<=Y,

    z_p=p^{-1+sigma}<=exp(1/4)/p,
    z_p/(1-z_p)<=4/p,

where exp(1/4)<4/3 was used. Thus

    F:=product_{p in P}(1-p^{-1+sigma})^{-1}<=Y^4,           (6)

because log F<=4 sum_{p<=Y}1/p<=4log Y. Differentiating this finite Euler product gives

    sum_{h P-smooth}(log h)/h^{1-sigma}
       = F sum_{p in P} (log p)z_p/(1-z_p)
       <=4Y^4(log Y)^2.                                    (7)

Here sum_{p<=Y}(log p)/p<=log Y sum_{m=2}^{floor Y}1/m<=(log Y)^2. Since H^{-sigma}=exp(-u/8), (5)--(7) prove

    R <= (4/log 2)Y^4(log Y)^2 exp(-u/8).                   (8)

The estimate is uniform in both P and the weights.

## 4. Sieve approximation of exact smooth-part counts

Use the uniform sieve error e(t) from `DIFFUSE_RAW_WEIGHTS.md`:

    e(t)=C[(t/2)^{-t/4}+2^{1-t/2}],        t>=4.             (9)

For any interval B of real length T>=Y^t, the number of its integers coprime to product P differs from T theta_P by at most e(t)T theta_P. This follows from the standard fundamental lemma of the combinatorial sieve, uniformly for every subset P of the primes up to Y and every shift.

Decompose each positive integer uniquely as h t, with h its exact P-smooth part and gcd(t,product P)=1. For h<=H, both the prefix and interval counts at this smooth part are coprimality counts in intervals of real length M/h>=sqrt(M)=Y^{u/2}. They therefore have relative error at most e(u/2).

The contribution of h>H to the prefix threshold-two hinge is at most MR, because the number of prefix multiples of h is at most M/h. Discard the nonnegative target contribution from h>H. By (3)--(4), the small-part model gap loses at most R on truncation, since 0<=g_1(X)-g_2(X)<=X. Consequently

    Delta_2/M
      <= -Y^{-J_epsilon}+2R+2e(u/2)(1+log Y).              (10)

This estimate is valid whenever some individual weight is at least eta_epsilon and u>=8.

## 5. The errors are uniformly smaller than the gap

Write L=log M and y=log Y. Let gamma be the value in (2), so

    log 2<=y<=gamma sqrt(L),
    u=L/y.

After dividing (8) by Y^{-J_epsilon}, its right-hand side is

    (4/log 2)y^2 exp((J_epsilon+4)y-L/(8y)).                 (11)

Both the polynomial factor and the exponent increase with y. At y=gamma sqrt(L), the exponent equals

    [(J_epsilon+4)gamma-1/(8gamma)]sqrt(L)
      = -gamma(J_epsilon+6)sqrt(L).

Thus (11) tends to zero uniformly throughout the allowed range of Y.

For u>=16, (9) implies

    e(u/2)<=3C2^{-u/4}.

The ratio of the last error in (10) to Y^{-J_epsilon} is therefore at most

    6C(1+y) exp(J_epsilon y-(log 2)L/(4y)).                 (12)

Again the exponent increases with y. Its value at the upper endpoint is a negative constant times sqrt(L), because

    J_epsilon gamma^2 < 1/16 < (log 2)/4.

Hence (12) also tends to zero uniformly. For all sufficiently large M, the two errors in (10) sum to at most Y^{-J_epsilon}. This proves H_2 whenever at least one individual weight is at least eta_epsilon.

If every weight is at most eta_epsilon, the diffuse-weight theorem gives H_(2+epsilon) at every length and for every support, without a restriction on Y. Combining the two cases proves (1).

External source for the sieve input: J. C. Lagarias, *Math 675: Combinatorial Sieve: Fundamental Lemma*, theorem and interval example, pages 1--2:

https://websites.umich.edu/lagarias/675notes/Estimate5-2015.pdf

## 6. An actual restricted integer-cover consequence

Let A be a set of n distinct integers at least two, let M=max A, and suppose every prime factor of every source is at most Y(M), where

    log Y(M)=o(sqrt(log M)).

Then, uniformly in the interval shift,

    tau(A,I)<=(2+o(1))n                                    (13)

as n tends to infinity, for every interval I of length M.

To justify this directly, fix epsilon>0. The source-prime dual weights may be clipped to [0,1], and (1) gives a raw boxed LP value at most (2+epsilon)n. A basic feasible boxed covering solution has at most pi(Y) fractional coordinates, so rounding those coordinates up gives an integer cover of size at most

    (2+epsilon)n+pi(Y).                                    (14)

If M<16n^2, then n>sqrt(M)/4, while pi(Y)<=Y=M^{o(1)}=o(sqrt(M)). Thus the final term in (14) is o(n). If M>=16n^2, the known quadratic long-interval theorem already gives an exact cover of size at most 2n. Since epsilon was arbitrary, these two ranges prove (13).

The LP rounding assertion here has a specific reason: the number of source-prime rows is at most pi(Y)=o(n) in the remaining range. It is not an assertion that arbitrary raw fractional covers can always be rounded at o(n) cost.

The long-interval input is the written elementary theorem in Ziming Wang's `erdos-708-interval-divisor-covers` manuscript, appendix section “The quadratic coefficient-two gate”, whose conditions and proof were independently checked earlier in this investigation:

https://github.com/science-prince/erdos-708-interval-divisor-covers

## Remaining gap

The cutoff exp(o(sqrt(log M))) still excludes prime factors on polynomial scales M^alpha. The general problem allows those factors, including their interactions with the dense small-prime part. Neither the uniform hinge theorem nor the restricted integer-cover consequence above supplies that missing comparison.

