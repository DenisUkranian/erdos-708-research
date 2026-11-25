# Cold-quotient descent: arithmetic stress test

Date: 24 November 2026.

## Scope and result

No proof or counterexample to descent (D) on genuine positive global
maxima was obtained. Two useful facts were checked:

1. Full-tail structure and the nonnegative quotient reserves alone do not
   force even one positive cold quotient. There are actual arithmetic
   full tails with source excess much larger than sqrt(M), while every
   cold quotient has nonpositive surplus. In the explicit family below,
   exact whole-prime rows exclude optimality, and the target banks pay
   the entire excess. This is a counterexample to a source-only
   intermediate localization claim, not to (D).
2. Optimization over the actual CRT phases gives a valid one-prime
   averaging inequality. Its direction is an upper bound on the target
   removal marginal, not the lower bound needed for (D). Differentiating
   this inequality as though it were an equality is invalid.

No new value of g(n) is computed or claimed.

## 1. An exact source-only obstruction with unit positive prices

Let P be a positive integer and let R be any nonempty set of primes in
(4P,5P]. Write k=|R|, take M=125P^3, and use w_p=1 on R and w_p=0
elsewhere. Fix 2<c<3. Thus X(t) counts the R-prime occurrences of t,
including multiplicities.

Every degree-three monomial in R lies strictly above 64P^3>M/2 and at
most M. Every degree-four monomial exceeds M. It follows that the full
strict source tail is exactly

    A = { products of three members of R, with repetitions allowed }.

There are no further inactive cofactors, since multiplying one of these
monomials by any integer >=2 exceeds M. Unique factorization gives

    n = binom(k+2,3),
    S_c = sum_A(X(a)-c) = (3-c) binom(k+2,3),
    D_p(A) = (k+1)(k+2)/2   for every p in R.          (1)

The last identity follows either by counting occurrences or by symmetry:
the total number of occurrences is 3 binom(k+2,3), distributed equally
over k primes.

A cold d>=2 satisfies X(d)<1. Since all positive prices equal one, it
must contain only zero-price primes and has X(d)=0. Its quotient prices
are unchanged, apart from deletion of primes exceeding N=floor(M/d).
But N<=M/2 and no number <=M/2 contains three R-prime occurrences.
Therefore every induced actual quotient has no source tail, so

    Q_d <= 0  for every cold d>=2 and every actual target interval I. (2)

Taking R to be all primes in (4P,5P], the prime number theorem gives
k~P/log P. Hence S_c is of order P^3/(log P)^3, whereas sqrt(M) is of
order P^(3/2). Thus S_c/sqrt(M) tends to infinity.

Consequently, an attempted inequality S_c <= C sqrt(M) + C' max Q_d
on arbitrary complete source tails is false. All nonnegative source,
endpoint and clipping reserves in the exact quotient formula are
already included in Q_d here.

### Why this family is NOT a counterexample to (D)

For any fixed p in R, consider all banks of interval multiples of pq,
as q ranges over R (including q=p). Every position in these banks is
strictly hot, since X(pq)=2.

Each bank has at least

    floor(M/(pq)) >= 5P

positions. For distinct q,r, their least common multiple is pqr when
q,r differ from p, and p^2r when one equals p. In either case it exceeds
64P^3. An M-term interval therefore contains at most two common
positions. Bonferroni gives the actual common union estimate

    U_p := | union_(q in R) (I intersect pq Z) |
         >= 5Pk - 2 binom(k,2)
          = 5Pk-k(k-1).                               (3)

As R lies in an interval of P integers, k<=P. Consequently

    U_p - D_p(A)
      >= 5Pk - (3/2)k^2 - k/2 - 1
      >= (7/2)k^2 - k/2 - 1 > 0.                     (4)

If these weights were raw-optimal for their own full tail, all members
of the union in (3) would have z_b=1. Their p-valuation alone exceeds
D_p(A), contradicting the exact active p-row. Thus genuine optimality
fails, for every actual interval.

There is also a direct payment proof. At a hot target b, let r(b) be
the number of distinct active primes p whose pair-bank union contains b.
Then r(b)<=X(b), and X(b)>=2 implies

    X(b)-1 >= r(b)/2.

Summing this inequality and (3) gives

    H >= (k/2)[5Pk-k(k-1)].                           (5)

Since P>=k, the right side is at least 2k^3+k^2/2, exceeding
binom(k+2,3)>S_c. Hence J_c<0 for every actual target interval.

The lesson is exact: if the cold quotients carry no excess, the desired
arithmetic argument must establish compensating target payment. Full
tail structure does not supply localization by itself. This example is
not presented as a new solved factorization class.

## 2. What global phase optimality does give

Use the actual capped phase normalization at a joint optimum. Fix an
active prime p, put E=floor(log_p M)+1, w=w_p, and write

    Y_i = sum_(q!=p) w_q v_q(x+i),  1<=i<=M.

Changing the p-adic phase while keeping all other prime phases fixed is
realizable by CRT, including the extra digit needed to realize the
capped p-valuations exactly. The source prefix is unchanged.

For k>=1 define

    A_i(k) = (Y_i+kw-1)_+ - (Y_i+(k-1)w-1)_+.

Let H be the actual target penalty and H_without_p=sum_i(Y_i-1)_+.
At a globally minimizing target phase, the present penalty is at most
its average over the p^E possible p-phases. Since the probability that
the capped p-valuation is at least k is p^(-k), this gives

    H-H_without_p <= sum_(k=1)^E p^(-k) sum_i A_i(k). (6)

Every A_i(k) lies between zero and w. In particular the right side is
at most Mw/(p-1), but (6) retains the exact distribution of all other
loads near the target threshold.

This inequality can be used together with, but does not replace,
whole-prime complementary-slackness rows. It cannot be differentiated
to identify their derivatives: the current phase need not equal its
average, and a nonzero value gap has no prescribed derivative sign.

Most importantly, (6) bounds the present target marginal from above.
A lower bound required to pay the source excess does not follow from
it without another argument.

## 3. Search direction and exact unresolved point

The required inequality is a compensation-or-localization theorem:
either actual target banks already pay all but O_c(sqrt M) of the
source excess, or some cold quotient carries a sufficient fraction of
the remaining signed excess. The example in Section 1 forces the
compensation alternative. The averaging inequality (6) does not prove
that alternative uniformly.

No uniform bound on the remaining signed excess, and no proof that
the whole-prime rows plus full tail and phase optimality force (D),
has been obtained in this audit.
