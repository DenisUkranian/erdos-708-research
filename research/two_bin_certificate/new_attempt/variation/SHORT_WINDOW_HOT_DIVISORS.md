# A quadratic bound for the number of small hot divisors

24 November 2026. This is a new proved counting lemma. It does not prove
the uniform full-tail estimate or the asymptotic Erdős 708 conjecture.

## 1. An elementary interval-difference lemma

Let I be any interval of M consecutive integers and let S be a subset of I
with |S|=K. Let D be an integer with 1<=2D<=M. Define

    H_D={d:1<=d<=D, I intersect dZ is a subset of S}.

Put q=floor(M/(2D)). Then

    |H_D| <= binom(floor(K/q),2).                       (1)

In particular, throughout the same range 1<=D<=M/2,

    |H_D| <= 8 (KD/M)^2.                               (2)

**Proof.** Partition the first 2Dq positions of I into q consecutive
blocks of length 2D. One block B contains at most floor(K/q) points of S.
For every d<=D, B contains at least two consecutive multiples of d.
If d belongs to H_D, both of these multiples lie in S intersect B and
their difference equals d. Thus every d in H_D occurs as a positive
difference of two elements of S intersect B. There are at most
binom(|S intersect B|,2) such differences, proving (1). When D<=M/2,
q>=M/(4D), and (2) follows from binom(k,2)<=k^2/2. All endpoint errors
have been retained. No assumption on the shift is made.

This proof counts distinct positive differences, not pairs with
multiplicity. A chosen pair cannot represent two different integers d.

## 2. Application to the actual hot set

For any nonnegative prime prices, including all raw prime powers, put

    X(t)=sum_p w_p v_p(t),
    S={b in I:X(b)>1}, K=|S|,
    H(y)=#{d<=y:X(d)>1}.

Every multiple of a hot integer is hot. Consequently, with D=floor(y),

    H(y) <= binom(floor(K/floor(M/(2D))),2)              (3)

whenever 1<=2D<=M. In particular,

    H(y) <= 8 (Ky/M)^2       (1<=y<=M/2).              (4)

This replaces the earlier O(C^7) clustering estimate near the cold
threshold by O(C^2). Indeed, T=M/(K+1) is cold below its endpoint, and

    H(CT) <= 8 C^2 (K/(K+1))^2 <= 8 C^2               (5)

provided CT<=M/2. The remaining bounded-K cases can be treated separately
when needed; (3) is the exact finite statement.

For every fixed B>0 and sufficiently large M,

    H(B sqrt(M)) <= 8 B^2 K^2/M.                       (6)

At a genuine positive global optimum, the known uniform first-moment
bound gives K<=C_c n. Hence

    H(B sqrt(M)) = O_{c,B}(n^2/M).                     (7)

In the sparse regime n/M->0 this number is o(n), even if n/sqrt(M)
diverges. No assumption of a small active-prime support is used.

There is also a weighted version. The existing conditional full-tail
first-moment theorem applies on the shorter prefix [1,floor(y)] at
threshold one. The positive-extremum bound on sum_p w_p/(p-1) is unchanged
when primes above y are omitted. Consequently

    sum_{d<=B sqrt(M), X(d)>1} X(d)
       = O_{c,B}(n^2/M)=o(n)                            (7a)

in the same sparse regime. This is still a bound on distinct integers d,
not on the loads of all copies of d among the original source factors
or the selected target profiles.

## 3. What this counts, and what it does not

Equations (3)--(7) count distinct hot integers. They do not count copies
of a carrier among sources, nor the number of target positions divisible
by it. A single hot d can have floor(M/d) or ceil(M/d) fully selected
multiples. These multiplicities cannot be dropped from a matching or
capacity calculation.

For example, with only w_2=1 and c between 2 and 3, the own prefix tail
has n=floor(M/8), while an interval has about M/4 hot positions. There
are only O(log M) different hot active parts up to sqrt(M). This example
is not a positive global optimum, but it demonstrates that counting
profile types alone does not pay for their copies.

## 4. A quantitative bound for sources with two hot complementary factors

Assume T=M/(K+1)>=2 and M is sufficiently large. Every hot integer h
satisfies h>T, since all floor(M/h)>=K+1 of its interval multiples would
otherwise be hot. Let E be the set of integers a<=M admitting a
factorization a=hk with X(h)>1 and X(k)>1. Choose the smaller factor h,
so h<=sqrt(M). Then

    |E| <= sum_{h<=sqrt(M), X(h)>1} H(M/h)
         <= 8 K^2 sum_{h<=sqrt(M), X(h)>1} 1/h^2.       (8)

For the last inequality, M/h<=M/2 because h>T>=2. Divide the h range
into (2^j T, 2^(j+1) T], truncating the last interval at sqrt(M).
Equation (4) bounds the number in each interval by
32 K^2 4^j T^2/M^2, so its contribution to the reciprocal-square sum is
at most 32 K^2/M^2. Consequently

    |E| <= 256 (K^4/M^2)
            [1+log_2^+(sqrt(M)/T)],                   (9)

after increasing the harmless endpoint constant if the range is empty.
In soft notation this is

    |E| = O((K^2/M)^2 log(2+K^2/M)).                   (10)

Thus, when K=O_c(n), the bound is
O_c((n^2/M)^2 log(2+n^2/M)), not O_c(n^2/M).
This may exceed n deep in the sparse subquadratic branch. The new
root-counting lemma therefore does not by itself dispose of sources
with two hot complementary factors.

## 5. The exact unresolved use in the logarithmic budget

At the same original paired optimum,

    sum_{b in I} z_b log h_w(b)
       =sum_{a in A} log h_w(a) <= n log M.             (11)

Therefore selected targets with h_w(b)>M^(1/2+eta) have total selected
mass at most n/(1/2+eta). The missing term is the mass, or an independent
valid payment, of selected targets with smaller active part.

Equation (7) makes the number of possible small hot active parts o(n)
in the sparse regime. It does not make their total selected mass o(n).
Nor does it remove the exponential 2^H loss in the old unrestricted
Hall inclusion-exclusion argument. A new argument must retain repeated
copies and the shared target capacity while using this sharper count.

No new value of g(n) has been computed, and no partial support class is
claimed as a solution of the requested general asymptotic.
