# Audit of the two supplied dot reductions

Status: the two stated reductions are valid under the explicit hypotheses
below. The first actually bounds the number of affected sources by o(n),
in addition to supplying a matching. A further varying-core argument
removes a periodic-core assumption for a triple-large-prime reduction at
the scale P >> n^(3/5). None of these results by itself proves the
unrestricted surplus bound or Erdős 708.

## 1. Repeated active cofactors near the n scale

Fix constants b>0, L, C0, C1. Let E be a set of retained active primes
with b<=w_p<=1, and put

    Y(t)=sum_{p in E} w_p v_p(t).

Let A be a source set of size n, and let z_b in [0,1], b in an actual
M-term interval I, satisfy

    z_b=1 whenever Y(b)>1,
    sum_{b in I} z_b Y(b)<=C1 n.

These conditions hold when Y is a coordinate restriction of a genuinely
paired original raw optimum and its selected weighted demand is O(n).
Take any subset T of sources with 2<Y(a)<=L, each assigned a prime
p(a) in E satisfying

    P<=p(a)<=C0 n,
    k=ceil(L/b),
    P=n/(log n)^(1/(4k)),
    H=(log n)^(1/(2k)).

The constants b,L,k must be fixed as n grows. Let nu_E(a) be the full
E-part of a and put d(a)=nu_E(a)/p(a). Let m_d count the assigned sources
with this active cofactor d.

### Multiplicity bound, including inactive factors

Every assigned source has the form a=d p u, with u E-free. Consequently

    m_d <= sum_{P<=p<=C0 n} floor(M/(dp))
        <= (M/d) s_n,
    s_n=sum_{P<=p<=C0 n}1/p=O(log log n/log n).

The first inequality deliberately permits every positive u, so arbitrary
inactive factors do not invalidate it. The estimate for s_n follows
uniformly by partial summation from the prime-count bound on this short
multiplicative range.

Also Y(d)=Y(a)-w_p>1, Omega(d)<=k, and M/d>=p>=P.

### One common target capacity

Remove the targets with Y(b)>H. They number at most C1 n/H, since they
are saturated. Every bank of d-multiples therefore has a surviving set B_d
of size

    |B_d| >= M/d-1-C1 n/H = (1-o(1)) M/d,

uniformly over every occurring d. Indeed n/(HP)=(log n)^(-1/(4k)).
Every member of B_d is still Y-hot and hence saturated.

Distribute the m_d unit demands uniformly over B_d. A surviving target
b has Y(b)<=H, hence at most H/b retained prime occurrences. The number
of distinct retained divisors of b of total degree at most k is at most

    binom(floor(H/b)+k,k)=O_{b,k}(H^k)=O_{b,k}(sqrt(log n)).

All raw target powers are included in this count. Its total incoming mass
is consequently at most

    O_{b,k}(s_n H^k)=O_{b,k}(log log n/sqrt(log n))=o(1).

For large n this is below one, so this is a feasible fractional matching
of every assigned active-cofactor copy. The finite bipartite matching
polytope then gives an integral matching of those copies.

### Stronger consequence

The support of this fractional matching lies entirely in {b:Y(b)>1}.
That set has at most C1 n members. Summing the pointwise o(1) incoming
mass therefore proves the stronger statement

    |T|=O_{b,k,C0,C1}(n log log n/sqrt(log n))=o(n).

The argument thus eliminates these sources from a hypothetical extremum
at small cardinality cost. Under the full-tail exponential moment bound,
their ORIGINAL weighted source demand is also o(n).

Scope caution: d is the retained active part of a/p. The matching does
not claim divisibility by the complete cofactor a/p when its discarded
prime factors have positive original prices. Those discarded demands
must be accounted for by the existing normalization budget.

## 2. Triple-large sources with an actual periodic lower load

Let A have n elements, each with X(a)>2, for clipped raw weights X, and
let z be paired with that same A. Thus every X-hot target is saturated
and each positive-price prime row is tight. Fix P>1 and suppose

    log M/log P <= K

for a fixed constant K. Let R be the positive-price primes at least P
that appear together with another distinct positive-price prime at least
P in some source. If p is in R, choose a source containing p and another
such prime q. Every multiple of a/q is hot, contains p, and there are
at least q>=P such multiples in I. Thus

    D_p(A)>=P,
    sum_{p in R}D_p(A)<=Kn,
    |R|<=Kn/P.                                         (1)

Let Q be a positive integer and restrict to primes of R coprime to Q.
Let S be an actual Q-periodic nonnegative lower load satisfying

    X(b)>=S(b)+sum_{p in R, gcd(p,Q)=1}w_p v_p(b)

on the target interval. Consider sources that have three distinct such
active primes p,q,r and satisfy

    S(a)+w_p+w_q>1

for at least one oriented pair p,q from the triple. The third prime r
must range over R as well; an arbitrary inactive third prime cannot be
silently substituted in the proof. Suppose

    epsilon=nQ/P^2 ->0.

Then the number of these sources is O_K(n^2 Q/P^2)=o(n).

### Fixed row and residue

Fix p in R and a residue ell modulo Q. For every eligible q choose the
bank C_q of targets b in I with pq|b and b=ell modulo Q. It is entirely
hot, since S(b)=S(ell). Put

    L_q=M/(Qpq).

The existence of a triple source witnessing q gives M/(pq)>=r>=P,
so L_q>=P/Q. The exact arithmetic-progression counts give

    |C_q|>=L_q-1,
    |C_q intersect C_q'|<=L_q/q'+1    (q!=q').          (2)

Write s for the number of eligible q and W=sum_q L_q. Then
s<=|R| and s<=QW/P. By (1), a nonempty R also implies P<=Kn and hence
Q/P<=K epsilon. Consequently the total rounding and overlap errors in
the first Bonferroni bound are O_K(epsilon)W:

    |union_q C_q| >= (1-O_K(epsilon))W.                 (3)

For example, ordered intersection sums are bounded by

    (s/P)W+s(s-1) <= (s/P+sQ/P)W.

Every qualifying source for this fixed p,ell is counted by at least one
choice of q and a third r in R. Its count is at most

    sum_q sum_{r in R\{p,q}}(L_q/r+1)
    <= |R|(1/P+Q/P)W
    = O_K(epsilon)W.                                  (4)

The unions in (3) for different ell are disjoint. They are saturated
and every position in them contains p, so their combined cardinality
is at most D_p(A). Equations (3)--(4), followed by (1), give

    |T| <= O_K(epsilon) sum_{p in R}D_p(A)
         =O_K(n^2Q/P^2).

Full raw target powers cause no problem: the cardinality of a saturated
p-divisible union is bounded by its full p-valuation, which is bounded
by D_p(A). Different q banks are counted through their union. Summing
different p rows is legitimate because the source side has at most K
large-prime occurrences per source.

## 3. Removing the periodic-core assumption at P >> n^(3/5)

Assume the same full-tail/paired hypotheses, M<=16n^2, and

    P/n^(3/5) -> infinity.

Let T consist of all sources with at least three distinct active primes
at least P. For sufficiently large n, P^4>M. Therefore every a in T has
exactly three large prime occurrences and can be written uniquely, up
to ordering the three primes, as

    a=u p q r,  p,q,r>=P distinct,
    1<=u<=U=floor(M/P^3)<P.

The primes p,q,r are coprime to every possible u. Use R and (1) above;
K can be bounded by an absolute constant in this range.

Fix p. For each q occurring with p in a source of T, choose any one
source witness a=u_q p q r. Define the actual
bank

    C_q={b in I:p q u_q divides b},
    L_q=M/(p q u_q)>=P.

Every such bank is hot because X(pq u_q)=X(a)-w_r>1. Since u_q<P,
distinct q,q' cannot divide either small cofactor, and

    lcm(pq u_q,pq' u_q')=p q q' lcm(u_q,u_q').

In particular,

    |C_q intersect C_q'|<=L_q/q'+1.

As L_q>=P and the number of eligible q is at most |R|<=Kn/P,
Bonferroni gives

    |union_q C_q| >= (1-O_K(n/P^2)) sum_q L_q.          (5)

For fixed p,q there are at most |R|U sources u p q r, because both r
and the integer u determine the source. Since L_q>=P, this is at most

    (|R|U/P)L_q.

Sum over q, use (5) and saturation of the common p row, and then sum
over p. Each source of T is counted at least once, so

    |T| <= O_K(|R|U/P) sum_p D_p(A)
         =O_K(n^2 M/P^5)
         =O_K(n^4/P^5)=o(n).                           (6)

For example P=n^(3/5)log n gives |T|=O(n/(log n)^5).
The key arithmetic safeguard is U<P: without it, the displayed lcm
formula and intersection estimate can fail through cross-prime factors.
No minimization of u_q, or generic numerical-minimum bank principle, is
needed.

This corollary is a necessary reduction on every actual extremum, not a
theorem assuming a common small periodic core. It still leaves sources
with at most two primes above this threshold and sources whose active
primes all lie below it. No coefficient-two conclusion is drawn.

## 4. Repeated large prime occurrences are covered as well

The corollary in Section 3 extends from three distinct primes to three
large active prime occurrences, counting multiplicity. Define R_2 to be
the active primes at least P that occur in a source with at least two
large active occurrences, allowing these to be the same prime.

For p in R_2, delete one other large occurrence q from a witnessing
source a. When q=p, at least one p occurrence remains. The cofactor
bank is hot, contains p, and has at least q>=P targets. Thus

    D_p(A)>=P,
    sum_{p in R_2}D_p(A)<=Kn,
    |R_2|<=Kn/P.

Because P^4>M, a source with at least three large occurrences has one
of the forms u p q r, u p^2 q, or u p^3, with u<=U=M/P^3<P and the
displayed p,q,r distinct whenever separate letters occur.

For u p^2 q, fix the doubled prime p. For each q choose one witness
u_q p^2 q and the hot bank of p q u_q-multiples (delete one p).
Its expected size L_q=M/(p q u_q) is at least p>=P. Distinct q-bank
intersections satisfy the same estimate as Section 3 because u_q<P.
Consequently their union has cardinality at least

    (1-O_K(n/P^2))sum_q L_q

and at most D_p(A). For fixed p,q there are at most U sources, so

    # {sources of type u p^2 q}
       <=O_K(U/P)sum_pD_p(A)
       =O_K(nM/P^4).                                  (7)

For u p^3, there are at most U sources for each p in R_2, hence their
number is at most |R_2|U=O_K(nM/P^4) as well.

Together with (6), this proves

    # {a in A: sum_{p active,p>=P}v_p(a)>=3}
       =O_K(n^2M/P^5+nM/P^4)=o(n)

whenever M<=16n^2 and P/n^(3/5)->infinity. The result includes all raw
prime powers and needs no fixed periodic remainder. It is still only
a necessary reduction of a hypothetical global extremum, not a proof
of its nonexistence.

## 5. Exact limitation of the active-prime first-crossing route

This section records an unclosed step, not a further theorem resolving
the unrestricted problem.

Fix a source a with X(a)>2+delta. Order only its positive-price prime
occurrences increasingly, and let d be the first prefix whose load
exceeds delta. If p is the last prime occurrence entering d, then

    delta<X(d)<=delta+1,
    X(a/d)>1,
    a/d>=p^2.                                         (8)

The second inequality follows from the first and the source-tail
threshold. The third holds because the remaining active part contains
at least two occurrences, each at least p; all prices are at most one.
Inactive factors are retained in a/d and cause no difficulty in (8).

For a fixed crossing prefix d, source quotients avoid all earlier
active primes q<p. Targets in the same first-crossing cell must obey
the same avoidance condition. The ambient quotient interval has
length approximately M/d, which (8) bounds below by p^2. A cofactor
bank obtained by deleting one remaining occurrence q has quotient-bank
length at least q>=p; its members still need the preceding-prime
avoidance condition to remain in this same cell.

The verified low-state theorem controls the reciprocal mass only for
the substantial primes up to y=M^(1/(s+1)), with s fixed after the
weight cutoff is fixed. The crossing prime p may exceed y. Therefore
that theorem does not supply small reciprocal mass for the entire
set of earlier active primes below p. Its near-total bank-retention
estimate can only be invoked for the controlled low-prime set.

For the whole preceding-prime sieve, the available size information
M/d>=p^2 reaches the critical lower-sieve parameter two; it supplies
no proved uniform cell comparison on the n scale. Applying a
union bound to that larger prime set, or asserting that its loss is
o(1) because the low-prime loss is o(1), is unjustified. Exact prime
row balances and hotness have not been shown to repair this missing
joint estimate.

No arithmetic counterexample to the desired general transport bound
was obtained. No O(r) or o(n) bound for unrestricted all-prime-deletion
Hall deficiency was proved. The restricted reductions above therefore
do not establish J_(2+delta)<=C_delta or g(n)<=(2+o(1))n.
