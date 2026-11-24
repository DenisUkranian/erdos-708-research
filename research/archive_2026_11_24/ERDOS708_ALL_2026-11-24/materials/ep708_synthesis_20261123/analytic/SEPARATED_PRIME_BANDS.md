# Exact coefficient two for separated prime bands

Date: 2026-11-23.

## Status and scope

The argument below passes an internal mathematical audit, including arbitrary
interval shifts, real rescaled lengths, distinctness of assigned positions,
and the repair budget. It uses the standard uniform fundamental lemma of the
combinatorial sieve, Mertens' product estimate, and Chebyshev's prime-counting
upper bound. It is not a formal proof artifact or a claim of external referee
approval. No priority claim is made.

This proves a restricted **exact** coefficient-two theorem with a growing,
possibly dense small-prime support. Every source outside the pure small-prime
part must have exactly one large prime occurrence. Unrestricted exact and
asymptotic Erdős 708 remain unresolved by this argument.

All logarithms are natural. Let A be a set of n distinct integers in [2,M],
and let I={x+1,...,x+M}, where M is a positive integer and x>=0 is an integer.
The length M is an ambient bound; equality M=max(A) is not required. For an
integer a, Omega(a) counts prime factors with multiplicity.

## 1. External estimates and their uniformity

The uniform sieve lemma in Section 1 of `DIFFUSE_RAW_WEIGHTS.md` supplies a
decreasing function e(kappa), kappa>=4, tending to zero, such that

    (1-e(kappa)) T theta_Q
      <= #{m in J: gcd(m,Q_product)=1}
      <= (1+e(kappa)) T theta_Q,                              (1)

whenever Q is any subset of the primes at most Y, Y>=2, J is a half-open
real interval of length T>=Y^kappa, and

    Q_product=product_{q in Q}q,
    theta_Q=product_{q in Q}(1-1/q).

Empty products equal one. The constants are independent of Q, its
cardinality, the interval shift, and T. One may take

    e(kappa)=C_s[(kappa/2)^(-kappa/4)+2^(1-kappa/2)]

with an absolute constant C_s. The standard fundamental lemma gives relative
error O(u^(-u/2)) and additive error O(Y^u); take u=kappa/2 and use the
elementary theta_Q>=1/Y. Thus this version applies even to nonintegral T and
arbitrarily large shifts; it is not a short-interval prime-distribution
estimate.

Primary references for the sieve input are J. C. Lagarias, *Math 675:
Combinatorial Sieve: Fundamental Lemma*, pages 1–2,
<https://websites.umich.edu/lagarias/675notes/Estimate5-2015.pdf>, and
A. Granville and K. Soundararajan, *Multiplicative number theory: The
pretentious approach*, Theorem 1.4.2,
<https://dms.umontreal.ca/~andrew/PDF/Book.To1.4.pdf>.

We also use the standard consequences of Mertens' product theorem and
Chebyshev's estimate: there are absolute constants c_0,C_0>0 such that, for
every real Y,T>=2,

    product_{p<=Y}(1-1/p) >= c_0/log Y,
    pi(T) <= C_0 T/log T.                                   (2)

The usual large-argument estimates extend to all arguments >=2 by decreasing
c_0 and increasing C_0. No numerical values for these constants or for the
final separation exponent are claimed here.

## 2. Exact small-prime-part bins

Let Q be a subset of the primes at most Y, and let R be a finite set of
primes at least Z, with 2<=Y<Z. Partition the sources as

    A=A_Q disjoint-union A_R,

where every a in A_Q is Q-smooth, and every a in A_R has the form

    a=d(a) r(a),     d(a) Q-smooth,     r(a) in R.             (3)

The integer one is Q-smooth, so prime sources in R are allowed. Condition
(3) means exactly one R-prime occurrence, of exponent one, in each such
source. No other source prime factors are allowed.

For every distinct d occurring in (3), let

    m_d=#{a in A_R:d(a)=d},     T_d=M/d,
    B_d={b in I: d|b and gcd(b/d,Q_product)=1}.               (4)

Every b in B_d has exact Q-part d: all its powers of primes in Q multiply
to d. Consequently the B_d are pairwise disjoint. This remains true for
d=1 and for arbitrary prime powers in d.

The distinct sources with the same d correspond to distinct large primes
r<=T_d. Therefore

    m_d <= pi_R(T_d) <= pi(T_d),     T_d>=Z,                 (5)

where pi_R(T)=#{r in R:r<=T}.

Dividing the target interval by d gives exactly the integer points of

    J_d=(x/d,(x+M)/d],

a half-open interval of real length T_d. If Z>=Y^kappa, (1) gives

    |B_d| >= (1-e(kappa)) theta_Q T_d.                       (6)

This estimate is uniform in M,d,Q,R,x. No integer-length rounding is
silently omitted: it is already included in the sieve remainder in (1).

## 3. Finite sufficient comparison and the global repair bound

**Proposition.** Suppose kappa>=4, e(kappa)<1, Z>=Y^kappa, and

    (1-e(kappa)) theta_Q
       >= sup_{T>=Z} pi_R(T)/T.                             (7)

Then every interval I as above has a product cover of size at most

    2|A_R| + sum_{a in A_Q} Omega(a).                        (8)

For a finite nonempty R={r_1<...<r_s}, the supremum in (7) is exactly
`max_{1<=j<=s} j/r_j`. For R empty it is zero. Thus (7) is a finite
sufficient comparison, although the unspecified absolute sieve constant
does not provide a practical numerical threshold here.

**Proof.** Equations (5)–(7) show |B_d|>=m_d for every d. Choose m_d
distinct targets from B_d and assign them to the corresponding sources.
Different d use disjoint bins. This gives exactly |A_R| distinct targets,
and their product is divisible by product_{a in A_R}d(a).

Relative to the product of all sources, the total missing prime-valuation
units are at most

    |A_R| + sum_{a in A_Q}Omega(a):                          (9)

one unit for each removed prime r(a), plus all units of the pure Q sources.
Additional prime factors already present in the chosen targets can only
reduce the deficit.

Because the sources are distinct and <=M,

    product A | M! | product I.

If a selected product is deficient at a prime p, some unused target in I
is divisible by p; otherwise the full interval would have the same
deficiency. Add one such target. Each addition decreases the total positive
valuation deficit by at least one and never increases it. Starting from
the |A_R| assigned targets, at most the number in (9) of these repairs
suffice, proving (8).

This is **one global repair phase**. It does not combine independent covers
of A_Q and A_R, so there is no reuse or double counting of their target
capacities. End proof.

For a particular source set it is also enough to check the weaker
source-dependent comparisons `(1-e(kappa))theta_Q T_d>=m_d` for its actual
fibres; (7) is a convenient support-only sufficient condition.

## 4. An absolute power separation suffices

**Theorem.** There is an absolute real constant kappa_0>=4 such that the
following holds for all parameters, without an asymptotic qualifier. If
Y>=2, Z>=Y^kappa_0, and A has the form (3), then the bound (8) holds for
every ambient M>=max(A) and every integer shift x>=0.

In particular, if A_Q is empty, every such instance has a cover of size
at most 2n.

**Proof.** Choose kappa_0 large enough that

    e(kappa_0)<=1/2,     kappa_0>=2C_0/c_0.                 (10)

This is possible because e(kappa)->0. Since Q is a subset of the primes
at most Y, (2) gives

    theta_Q >= c_0/log Y.

For every T>=Z>=Y^kappa_0,

    (1-e(kappa_0))theta_Q
       >= c_0/(2log Y)
       >= C_0/log T
       >= pi_R(T)/T.                                      (11)

Thus (7) holds, and the proposition proves (8). End proof.

The constant kappa_0 is not computed and is not claimed to be practical.
The theorem is stronger than requiring Z->infinity and log Y=o(log Z):
that asymptotic separation eventually satisfies the fixed exponent (10).
For example, Y=M^{o(1)} and Z=M^alpha for any fixed alpha>0 satisfy the
separation eventually. The one-large-prime-occurrence restriction (3)
still applies; it is not removed by the growth assumption.

## 5. Pure small-prime sources and exact/asymptotic consequences

Write n_Q=|A_Q|, n_R=|A_R| and n=n_Q+n_R. Bound (8) implies

    tau(A,I) <= 2n + sum_{a in A_Q}(Omega(a)-2)_+.           (12)

Therefore:

* If every pure Q source has Omega(a)<=2, the bound is exactly 2n.
  More generally, the same conclusion follows from
  `sum_{a in A_Q}Omega(a)<=2n_Q`.
* For a sequence with n->infinity, if
  `sum_{a in A_Q}(Omega(a)-2)_+=o(n)`, the upper bound is
  `(2+o(1))n`, uniformly in the interval shift.
* When A_Q is empty, no restriction on the size, density, or reciprocal
  mass of Q is needed beyond Q being contained in the small-prime band.

No matching lower coefficient is claimed. An unrestricted pure Q component
may have a large excess in (12); the theorem does not absorb that component
for free. Likewise, sources with two or more R-prime occurrences are outside
the stated class. These are real restrictions, so the theorem does not
settle the general problem or the general dense central interval range.
