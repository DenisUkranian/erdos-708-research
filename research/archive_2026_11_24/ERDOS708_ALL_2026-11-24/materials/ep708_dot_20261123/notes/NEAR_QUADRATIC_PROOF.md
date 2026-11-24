# Audit and completion of the near-quadratic surplus argument

## Status and scope

The argument supplied from dot is valid after the details below are made
explicit. Fix c=2+delta>2 and constants kappa,Lambda>0. There is no
sequence of positive global surplus maxima, with full-tail size n tending
to infinity, satisfying

    kappa n^2 <= M <= Lambda n^2.

This is a restriction on every genuine extremal obstruction, not an
assumed source-factorization class. The standard quadratic ambient gate
handles M>=16n^2, so Lambda=16 suffices in the intended application.
The unrestricted surplus bound is still not established: the first
group's error deteriorates as n^2/M grows.

All matching statements below are used directly to charge the target
hinge. No separate integer cover is united with another cover, and no
target valuation is spent twice without an explicit inequality.

## 1. Extremal inputs and an updated weighted-deficiency implication

Write X(a)=sum_p w_p v_p(a), with 0<=w_p<=1. Let w maximize J_c at fixed
M,I, let A={a<=M:X(a)>c}, n=|A|, and suppose J_c(w)>0. Let F be the raw
LP optimum for this same A and let z be paired with w. Then

    F=cn+J_c(w),
    L_raw(A minus S,I) <= F-c|S|,
    z_b=1 whenever X(b)>1.

The previously proved full-tail moment bound and the elementary bound
mu=O_c(1) give a constant C0=C0(c) with

    sum_{a in A}X(a)<=C0 n,   F<=C0 n.

Consequently, if K=# {b in I:X(b)>1}, then K<=C0 n. Also every prime
dividing any actual source a satisfies p<C0 n. Indeed, deletion of a
costs at most F-c. If p>=F-c+1, its cofactor bank has at least p positions
and at least one unit of remaining fractional capacity. Buying one unit
supplies a/p, and repairing the sole possible missing p-unit costs at
most one using full-interval supply. This gives cost at most F-c+2<F.
The argument includes source primes of price zero.

There is a constant B0=B0(c) such that every subset U of the complete
tail A, of cardinality t>0, satisfies

    sum_{a in U} X(a) <= c t + 2 B0 t log(2n/t).        (1)

For proof, use the already proved conditional MGF

    sum_{a in A} exp((X(a)-c)/(2B0)) <= 2n

and apply Jensen to U. In particular t=o(n) now implies weighted demand
o(n), uniformly even in the sparse regime. The older Hall note's warning
that t=o(n) need not suffice is superseded on these complete tails by (1).

If matched sources are assigned distinct targets within a group and each
assigned carrier h divides its source a, has X(h)>1, and has cold
complement X(a/h)<=1, then its target pays at least

    X(h)-1 >= X(a)-2.

If all but t sources can be charged this way, with any intergroup reuse
separately justified, the exact consequence is

    J_c(w) <= sum_{unmatched a}(X(a)-c)-delta(n-t).       (2)

Thus (1) makes a sufficiently small constant fraction of unmatched
sources harmless; t=o(n) is more than sufficient.

## 2. Finitely many hot divisors near the cold threshold

Set T=M/(K+1). Every integer d<=T is cold: otherwise its at least
floor(M/d)>=K+1 interval multiples would all be hot.

First, K tends to infinity whenever A is nonempty and M tends to infinity.
More precisely, any a with X(a)>2 has a hot divisor d<=a^(2/3).
If a prime p>a^(2/3) divides a, the complementary divisor a/p is hot,
since X(p)<=1. Otherwise all prime factors are at most a^(2/3). If one
lies in [a^(1/3),a^(2/3)], it and its complement are both at most a^(2/3).
If none does, multiply factors smaller than a^(1/3) until first reaching
a^(1/3); that product and its complement are again at most a^(2/3).
Their total load exceeds two, so one is hot. Therefore

    K >= floor(M^(1/3)).                                (3)

Fix C>=1 and let D_C={d<=CT:X(d)>1}. Every such d exceeds T.
Its interval bank has at least (K+1)/C-1 positions. Two such banks have
intersection at most

    M gcd(d,e)/(de)+1 <= (K+1) gcd(d,e)/T+1.             (4)

Here is an explicit packing argument. Put L=ceil(4C) and
alpha=1/(4L^2). For all sufficiently large K depending only on C,
there cannot be L members with every pairwise gcd<=alpha T.
Bonferroni would give their bank union size at least

    L[K/(2C)] - binom(L,2)[2alpha K+1] > K.

Choose a maximal pairwise-separated subfamily; it has at most L-1
members. Every d in D_C has gcd(d,r)>alpha T with some representative r.
For g=gcd(d,r), both integers d/g and r/g are at most C/alpha.
For fixed r and a pair (j,k)=(r/g,d/g), d=r k/j is determined. Hence

    |D_C| <= (L-1) ceil(C/alpha)^2 = O(C^7).             (5)

All counts concern actual interval banks. No independent residue model
is substituted. The threshold on K can be taken O(C^2), up to absolute
constant factors.

In this extremal setup the bound O(C^7) is in fact uniform also below
that K threshold. Equation (3) gives M<(K+1)^3, hence T<(K+1)^2. If
K=O(C^2), the trivial bound |D_C|<=CT is O(C^5). Thus (5), with a
larger absolute constant, holds for every C>=1 whenever a source of
load greater than two exists. This observation also justifies the
variable-kappa use of (5) in Section 9.

## 3. First source group: a small hot carrier

Fix a large parameter B, later chosen only in terms of c. Choose

    B' >= max(B,C0+2,sqrt(Lambda)+1).

Let H be the set of hot integers h<=B'n, and write H0=|H|. Since

    T >= kappa n^2/(C0 n+1),

equation (5) gives H0=O_{c,kappa,B'}(1).

Let A1 consist of sources having at least one hot divisor h<=B'n.
Remove all sources expressible as a=hk with both h and k hot and at
most B'n. There are at most H0^2 such sources. This removes every case
where an A1 source has a small hot divisor h with a hot complement:
h>T implies a/h<=M/h<K+1<=C0 n+1<=B'n for large n.

Choose one hot carrier h for each remaining A1 source. Its complement
is cold, so the target bank pays X(a)-2. Match each source to a distinct
interval multiple of its chosen carrier. For any Hall subset S, let D
be its distinct chosen carriers. The source integers in S lie in the
prefix union of these divisibility classes. Inclusion-exclusion and
the exact multiple-count error in {0,1} show

    |union_{h in D}(I intersect hZ)|
       >= |union_{h in D}([1,M] intersect hZ)|-2^|D|
       >= |S|-2^H0.

Hence all but at most 2^H0 sources in this group can be matched.
Including the both-hot exceptions, the first-group loss is at most

    H0^2+2^H0.                                         (6)

## 4. Second source group: divisor gap and large cold blocks

Let A2=A minus A1. Every divisor of an A2 source that is at most B'n
is cold. Put

    G=M/(B'n).

Because B'^2>Lambda, G<=B'n. No A2 source has a divisor d in [G,B'n]:
both d and a/d would be at most B'n and hence cold, contradicting X(a)>2.

Every a in A2 has a divisor u satisfying

    u>=sqrt(Bn),   u<=B'n,   X(u)<=1.                   (7)

To construct u, use a prime factor p>=sqrt(Bn) if one exists; the prime
bound p<C0n gives the upper endpoint. Otherwise multiply prime factors
until their product first reaches sqrt(Bn); it is then less than Bn.
The process can be completed since a>B'n. All multiplicities and zero
weights are permitted.

The initial carrier d=a/u is hot, exceeds B'n, and its bank has at least
floor(M/d)>=u>=sqrt(Bn) positions. Its complement u is cold.

## 5. Merging second-group banks is legitimate

Whenever two current carriers d,e have gcd g>=G, merge them into g and
associate all their sources with that carrier. The divisor gap forces
g>B'n: g divides every source previously associated with either carrier,
and [G,B'n] contains no source divisor.

For each associated source a, the new complement obeys

    a/g <= M/g < G <= B'n,

and is therefore cold. Thus g is hot and X(g)-1>=X(a)-2 for every
associated source. Its bank contains both old banks, so bank size never
decreases. This merge can be repeated finitely many times, reducing the
number of carriers each time.

At termination the carriers satisfy

    d>B'n,
    gcd(d,e)<G for distinct carriers,
    N_d:=#(I intersect dZ)>=q0:=sqrt(Bn)-1.             (8)

No payment is lost under this merging operation. The proof uses the
source divisor gap, not the incorrect assertion that an arbitrary gcd
of two hot integers must be hot.

## 6. A quantitative Hall bound from a single second-moment calculation

Take any subset S of A2, s=|S|. Let d_1,...,d_k be its associated
distinct carriers, N_i their actual bank sizes, and Q=sum_i N_i.
Since the s distinct sources lie among prefix multiples of these
carriers and every interval bank dominates its prefix count, Q>=s.
Also k<=Q/q0.

Write nu(b)=# {i:d_i divides b}. For i!=j, exact interval counting and
(8) imply

    |bank_i intersect bank_j|
      <= (G/M)(M/d_i)(M/d_j)+1
      <= (G/M)(N_i+1)(N_j+1)+1.

Consequently

    sum_b nu(b)^2 <= Q+alpha_n Q^2,

where

    alpha_n = [1/(B'n)](1+1/q0)^2 + 1/q0^2.            (9)

Cauchy-Schwarz, used once for the union, gives

    |N(S)| >= Q^2/(Q+alpha_n Q^2)
            = Q/(1+alpha_n Q)
            >= s/(1+alpha_n s)
            >= s-alpha_n n^2.                         (10)

The monotonicity in Q justifies replacing Q by s even when Q is large.
Thus the second-group Hall deficiency is at most ceil(alpha_n n^2),
and

    alpha_n n^2 = [1/B'+1/B+o(1)]n.                    (11)

The +1 errors from all pairwise interval intersections have been retained
in (9), through k^2<=Q^2/q0^2. They have not been dropped or separately
charged to multiple target budgets.

## 7. The two group matchings can share a target without overspending

Within each group the matched targets are distinct. Suppose a target b
receives a first-group carrier h<=B'n and a second-group carrier d>B'n.
Their gcd g divides an A2 source and is at most h. If g>=G, the divisor
gap would force g>B'n, impossible. Therefore

    g<G<=T,

where the last inequality follows from B'n>=K+1. In particular X(g)<=1.
Since lcm(h,d) divides b,

    X(b)-1 >= X(h)+X(d)-X(g)-1
             >= (X(h)-1)+(X(d)-1).                    (12)

Thus the same target can pay the two assigned charges, one from each
group. Every matched source receives at least X(a)-2. This is the
explicit common-capacity inequality; two independent budgets are not
being added without justification.

## 8. Contradiction and quantifiers

Let t be the number of removed or unmatched sources. Equations
(6) and (11) give

    t/n <= 1/B'+1/B+o(1),                              (13)

for fixed c,kappa,Lambda,B,B'. Applying (1) to the unmatched subset and
then (2),

    J_c(w)/n
      <= 2B0 (t/n) log(2n/t)-delta(1-t/n).             (14)

Choose B, and then B' as above, sufficiently large in terms of c that
the right side is negative whenever t/n<=3/B. Next let n tend to
infinity. This contradicts J_c(w)>0.

The order is fixed c,kappa,Lambda; choose B,B'; then n sufficiently
large. The finite number of small n does not by itself establish the
unrestricted surplus theorem, because kappa is still fixed here.

## 9. What deteriorates as M/n^2 tends to zero

The second-group estimates (7)--(14) do not deteriorate with kappa.
The obstruction is the first group. Write kappa_n=M/n^2 and retain fixed
c,B,B'. The packing bound gives, for large enough n,

    H0 <= C1(c,B') kappa_n^(-7).                       (15)

The first-group source loss is bounded only by

    H0^2+2^H0.                                         (16)

Hence this proof extends, without a new method, whenever

    kappa_n^(-7)=o(log n).

For example it excludes positive extremal sequences with
M>=n^2/(log n)^a for any fixed a<1/7. The both-hot loss H0^2 is then
only polylogarithmic; the exponential inclusion-exclusion loss is the
binding term.

To close the unrestricted asymptotic by this argument one must replace
(16) by an o(n) loss uniformly when n^2/M is unbounded, or avoid the
first-group matching through another valid joint charge. Pairwise
cold-gcd information alone does not let arbitrary many first-group
charges be added: with h_1=pq,h_2=pr,h_3=qr and unit prices, a target
divisible by pqr has hinge two but the three carrier charges sum to
three. This elementary example diagnoses the multiway overlap issue;
it is not a full-tail optimum or an arithmetic counterexample to J_c.

No estimate disposing of the first group throughout M=o(n^2) has been
proved in this audit.
