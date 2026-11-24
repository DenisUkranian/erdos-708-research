# Necessary arithmetic cores and the remaining closure bottleneck

## Scope

The unrestricted exact and asymptotic versions of Erdős Problem 708 remain
unproved here. This note derives necessary conditions for a hypothetical
counterexample of least source cardinality. It does not claim a new uniform
long-interval threshold or an unrestricted upper bound.

Fix a hypothetical counterexample `(A,I)`, where A has n distinct integers
at least two, M=max(A), I consists of M consecutive positive integers, and
n is the least possible counterexample cardinality. Write K=2n-1. For every
a in A, every cover B_a of A\{a} of size at most K-1 is available by the
minimality assumption. Arguments below apply to every such cover.

The full interval product covers the full source product. Hence whenever a
selected set is deficient in a prime valuation, an unused interval position
containing that prime exists. Adding it reduces the total positive valuation
deficit by at least one. This elementary repair rule is used throughout.

## 1. Closure and the exact boundary in the divisor gap

For every prime p dividing a, every interval multiple of a/p belongs to B_a.
Otherwise add an unused multiple of a/p and repair the one remaining p-unit,
using at most two additional positions. This would cover A in at most 2n.

Consequently

    a/P^+(a) > M/K,     equivalently a > P^+(a) M/K,

and all source primes are strictly below K. Indeed an a/p bank has at least
floor(Mp/a) positions and must fit inside B_a of size K-1.

Also every source has Omega(a)>=3, counting multiplicity. A source requiring
at most two prime units could be supplied by at most two repairs directly.
This statement is about Omega, not the number of distinct primes.

No source has a divisor d with

    K < d <= M/K.

For a=dv, the d-bank has at least K positions. Choose a fresh d-multiple.
The v-bank has at least floor(M/v)>=d>=K+1 positions, since M>=dv and d is
an integer greater than K. Therefore a second fresh position exists after
the first is added. This settles the strict endpoint issue without assuming
coprimality of d and v. When M<K^2 the displayed divisor gap is empty.

## 2. All forced prime-deletion banks must fit together

Let P(a) be the distinct prime support of a and let

    U_a = union_{p|a} {b in I : a/p divides b}.

Then U_a is contained in B_a. The intersection of any two distinct banks
is precisely the set of interval multiples of a, including when a has
repeated prime powers. Inclusion-exclusion therefore gives the exact identity

    |U_a| = sum_{p|a} N_I(a/p) - (omega(a)-1) N_I(a) <= K-1.

In one complete period of length a this union has

    c(a) = 1 + sum_{p|a}(p-1)

positions. Thus the simple uniform necessary condition is

    floor(M/a) c(a) <= K-1.

For the maximum source a=M it becomes the exact condition

    1 + sum_{p|M}(p-1) <= K-1.

The code computes the stronger exact minimum of |U_a| over all interval
shifts. It never enumerates CRT shifts. Define Star(L,R) as the multiples of
L together with the multiples of L/q for the distinct primes q in R. Its
period has 1+sum(q-1) marked positions. Write M=tL+r. The minimum is t times
the period population plus the minimum number of marks in an r-term cyclic
window. A minimum occurs immediately after a marked position; a two-pointer
scan through the sorted marks evaluates it exactly. With R empty this is
simply floor(M/L), and with one prime it is floor(M/(L/q)).

## 3. Exact valuation identities and uniform lower bounds

For any prime p, inclusion-exclusion also gives

    v_p(product U_a)
      = sum_{q|a} sum_{b in I, a/q|b} v_p(b)
        - (omega(a)-1) sum_{b in I, a|b} v_p(b).

There is a useful nonnegative level-count implementation. If p^e exactly
divides a, then

    U_a intersect p^r Z = U_a,                            r<e,

and

    U_a intersect p^r Z = Star(a p^(r-e), P(a)\{p}),       r>=e.

The central multiples of the new period are retained when P(a)\{p} is
empty. Summing the exact minimum cardinalities of these level sets gives
a rigorous uniform lower bound V_p(a;M) for v_p(product U_a).

The individual level minima may occur at different shifts. Their sum is
therefore a lower bound, not a claim to equal the minimum total valuation.
Once L exceeds M max(R), with max(empty)=1, the corresponding star has an
M-term gap and its minimum is zero; later levels also contribute zero.

The period algorithm was checked against exhaustive one-period counts in
316 small cases. Those checks supplement the general period argument.

## 4. Two-prime removal gives global demand constraints

Suppose a has two prime occurrences p,q, allowing p=q only if p^2 divides a,
and pq>=K. Then in a least-cardinality counterexample

    D_p(A) > v_p(product B_a) >= v_p(product U_a) >= V_p(a;M),

where D_p(A)=sum_{a' in A}v_p(a').

To prove this, suppose B_a already meets the full p-demand. A multiple of
a/(pq) can be chosen outside B_a, because its bank has at least pq>=K
positions. After it is added, only one q-unit can remain missing. Repair
that unit. If p=q, the p-demand was already complete. Either case contradicts
the counterexample. Interchanging p and q gives the analogous condition.

These inequalities involve the FULL demand of A, not merely v_p(a).
For an arbitrary n-source set in [1,M], the exact universal upper bound is

    D_p(A) <= sum_{j>=1} min(n, floor(M/p^j)).

It follows by counting how many of the n distinct sources can have each
valuation level. A stronger upper bound is obtained by choosing the n
largest valuations among the remaining arithmetic candidate pool, respecting
mandatory sources such as a and M. If this maximum is at most V_p(a;M),
then a cannot occur. Iterating this deletion rule is valid: the candidate
pool always remains a superset of any hypothetical least-cardinality A.

A least-cardinality counterexample also has connected prime support. If
its source hypergraph split into prime-disjoint components, cover each
smaller component and take the union. Overlaps in the selected positions
are harmless because the demanded prime coordinates are disjoint.
Thus candidate components disconnected from the mandatory source M can
be removed. The code uses this necessary condition as well.

## 5. A prime-power-bank saturation lemma

This is a stronger local exclusion for a broad source family.

**Lemma.** If B contains every interval multiple of p^e and
floor(M/p^e)>=n, then B already supplies the full p-demand of any set of
n distinct sources in [1,M].

Indeed,

    v_p(product B)
      >= e floor(M/p^e) + sum_{j>e} floor(M/p^j)
      >= en + sum_{j>e} floor(M/p^j)
      >= sum_{j>=1} min(n,floor(M/p^j))
      >= D_p(A).

**Consequence.** A least-cardinality counterexample cannot contain

    a=p^e q,     p,q prime,     p^e<=M/n,

where q=p is allowed. Closure for removal of q puts every p^e multiple
inside B_a, so the lemma supplies the entire p-demand. At most one q-unit
remains, and it can be repaired. In particular such a source is excluded
whenever q>=n, because a<=M implies p^e=a/q<=M/n.

This does NOT replace M/K by M/n for arbitrary cofactors. The prime-power
form is essential to the stated saturation argument.

## 6. Reproducible finite arithmetic cores

`necessary_core.py` generates every surviving integer source a<=M, applies
the exact tests above, and exports the demand inequalities and deletion
trace. Its JSON records the least-cardinality hypotheses explicitly.
No original interval-cover search or random CRT sampling is performed.

Representative results at n=100 are:

| M | Initial candidate count | Final count | Result |
|---|---:|---:|---|
| 10000 | 2285 | 2041 | Arithmetic core survives |
| 20000 | 3549 | 3286 | Arithmetic core survives |
| 30000 | 4591 | 4232 | Arithmetic core survives |
| 40000 | 5197 | 5197 | Required maximum source excluded by d=200 |
| 146969=47*53*59 | 438 | 33 | Required maximum source excluded by the demand bound |

In the last case, the forced 47-valuation is at least 112, whereas the
maximum possible 47-demand of 100 sources drawn from the candidate pool,
including M, is only 90. This is an exact finite exclusion of these
least-counterexample parameters. It is not a uniform threshold theorem,
and it does not assert g(100)<=200 without the minimality hypothesis.

Reproduce or check the exported trace with, for example:

    python necessary_core.py --n 100 --M 146969
    python necessary_core.py --verify core_n100_M146969.json

## 7. A large exact witness to the limitations of these filters

`dense_core_family.py` constructs 16384 distinct sources with

    M=268435456=n^2,     K=32767,

using powers of two times four-prime odd monomials on the primes at most
113, together with M and an odd power of three. The full exact source list
and checks are in `dense_core_family_certificate.json`.

This family has gcd one and connected support. Its cofactor support contains
every prime at most 113 and has reciprocal mass greater than one. Nevertheless:

* every source has at least three prime factors counted with multiplicity;
* every prime-deletion cofactor exceeds M/n, hence also M/K;
* the forbidden divisor interval is empty;
* every product of two prime occurrences is at most 113^2=12769<K;
* therefore every critical two-prime demand condition is vacuous;
* every forced union has at most 676 positions for every shift, far below
  the allowed 32766;
* the source-prime charge is 76735, so the elementary sum-of-omega bound
  does not give 2n;
* the finite sparse cofactor certificate fails: for source 2^21*3^4 and
  cofactor 2^21*3^3, its floor/ceiling lower bound is -1, below fibre size 1.

The family thus survives the listed source-only arithmetic filters. It is
NOT a counterexample. In particular, no covers B_a with all the universal
minimal-counterexample properties are asserted to exist. At x=0 the original
instance is trivially covered by A itself. The distinction between a source
relaxation and the actual universal closure property is essential.

The phenomenon is not confined to this one finite example. Let n tend to
infinity through powers of two, put M=n^2, and choose Y=n^beta with
1/4<beta<1/2. There are more than n four-prime monomials on odd primes at
most Y for all sufficiently large n: the standard prime-counting lower
bound gives their number on the order of at least Y^4/(log Y)^4 >> n.
Normalize selected monomials into (M/2,M] by powers of two, and add M and
an odd power of three. Include the monomials 3p^3 to ensure connectedness
and that every prime p<=Y enters the cofactor support. These mandatory
choices are o(n). The resulting source-only families have all pair products
below K and forced unions of size O(Y)=o(n), while their cofactor reciprocal
mass grows without bound by divergence of the sum of prime reciprocals.
These standard prime-distribution facts are needed only for this infinite-
family observation; the finite certificate above is purely integer/rational.

This identifies the bottleneck: local bank cardinalities and two-prime
removals do not control the joint valuation deficits of a small cover of
A\{a}. A stronger argument must exploit the fact that this cover actually
supplies the other source demands, including exchanges or joint saturation
of several prime coordinates. Merely repeating source-only pair tests does
not resolve the dense central range.

## Audit of the separate growing-support hinge result

The proof in `../analytic/DENSE_GROWING_SUPPORT.md` was independently checked,
including all explicit constants, both small-rho bounds, individual truncation
exponents, the periodic mean gap, the tail estimate, and the final comparison
4RB/delta<=F. The audit passed, subject only to making the empty-support case
explicit before taking a maximum over P. It proves a dual-support theorem;
it is not used here to claim a new source-set threshold.
