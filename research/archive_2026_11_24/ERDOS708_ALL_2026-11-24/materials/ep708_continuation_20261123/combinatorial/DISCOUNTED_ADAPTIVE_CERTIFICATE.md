# A discounted adaptive certificate and separated-support covers

Date: 2026-11-23.

## Status and main consequence

This note proves a source-class extension of the preceding separated-support
argument. The pointwise multiplicity bounds have been independently audited
by the parent and analytic research agents. The proof is not a solution of
unrestricted Erdős Problem 708, and no priority claim is made.

**Theorem.** Fix alpha>0 and a prescribed function Y(M)>=2 such that

    log Y(M)=o(sqrt(log M)).

Let A be any set of n distinct integers in [2,M], every prime factor of
which is either at most Y(M) or at least M^alpha. There is no restriction
on the number of large-prime occurrences in a source, and no restriction
on the number of small-prime occurrences. For every epsilon>0, for all
sufficiently large M, uniformly in A and in every positive interval I of
M consecutive integers,

    L_raw(A,I)<=(2+epsilon)n.                              (T1)

Consequently, uniformly in this hereditary source class as n tends to
infinity,

    tau(A,I)<=(2+o(1))n.                                   (T2)

The ambient length M is fixed when subsets are considered; it need not
equal max A. The integer conclusion uses the separately audited hereditary
raw-LP transfer lemma and the known quadratic long-interval gate.

The improvement over the previous linear certificate is that alpha may
be any fixed positive number. The earlier requirement alpha>1/(2e)
is unnecessary. The proof accepts a bounded number of positive carriers
at a target, since the source fibres are diluted by a factor tending
to zero. A growing-parameter extension is given in Sections 6--7.

## 1. General carrier hypotheses

Let Q and R_0 be disjoint finite prime sets. Let D be a finite set of
positive integers d<=M such that:

* d is supported on Q union R_0;
* every R_0-prime dividing d is at most T_d=M/d;
* the number Omega_R(d) of R_0-prime occurrences in d is at most an
  integer t>=0, counting multiplicity.

There is no upper bound on the number of Q-prime occurrences in d.
For a positive integer b, write X(b)=sum_p w_p v_p(b), with arbitrary
nonnegative weights on a finite prime support containing Q union R_0.
Set h_d=(X(d)-1)_+ and H_1(b)=(X(b)-1)_+.

Choose an integer ell>=1. If d does not divide b, set K_d(b)=0.
Otherwise define

    s_d(b)=#{r in R_0:r<=T_d and r divides b/d},
    K_d(b)=1[gcd(b/d,product Q)=1] (1-s_d(b)/ell).           (1)

The counter s_d records distinct prime values, even when b/d contains
more than one occurrence of a prime. Positive terms have 0<K_d<=1.

## 2. Two explicit pointwise multiplicity bounds

Define

    C_1(t,ell)=binom(2t+ell-1,t),                           (2)

and

    C_2(t,ell)=(t+ell)
       sum_{j=0}^{ell-1}binom(t+ell-1,j)(t+1)^j.           (3)

Let C(t,ell)=min(C_1,C_2). Empty-degree cases use the usual binomial
conventions; in particular t=0 causes no difficulty.

**Lemma.** For every positive integer b,

    sum_{d in D}h_d K_d(b)<=C(t,ell)H_1(b).                (4)

### Proof of the coarse bound C_1

If no K_d(b) is positive, the assertion is immediate. Otherwise choose
the numerically smallest positive carrier d_0, so T_0=M/d_0 is the
largest threshold among all positive carriers. Put

    S={r in R_0:r<=T_0 and r divides b},     k=|S|.

Every prime of S either divides d_0 or divides b/d_0. The first class
has at most t distinct members; the second has at most ell-1 members
because positivity means s_{d_0}(b)<ell. Therefore

    k<=t+ell-1.                                           (5)

All positive carriers have the same Q-part: the full Q-smooth part
of b. Indeed, the Q-coprimality condition excludes any extra Q-factor
in b/d. For any other positive d, its R_0-primes are at most
T_d<=T_0, divide b, and hence belong to S. Its R_0-part has degree at
most t. There are

    sum_{j=0}^t binom(k+j-1,j)=binom(k+t,t)
       <=binom(2t+ell-1,t)

possible monomials, including the constant monomial. When k=0 this
count is simply one, so the displayed binomial total still applies.
The common Q-part and the R_0-monomial determine d uniquely.
This proves the C_1 bound on the number of positive carriers.

For each positive carrier, d|b implies h_d<=H_1(b), and K_d<=1.
All other weighted terms are nonpositive. Summing proves (4) with C_1.

### Proof of the sharper bound C_2

Order S increasingly. For any positive d, the primes in S at most
T_d form a prefix of that ordered set, giving at most k+1 choices.
Every prime outside this prefix has exponent zero in d, by the
self-smoothness hypothesis.

Inside the prefix, all but at most ell-1 primes must have their
FULL exponent v_r(b) in d. Every deficiency v_r(d)<v_r(b) makes
r divide b/d and is counted in s_d(b).

Choose the at most ell-1 exceptional primes, then choose their
exponents in d. Each such exponent belongs to {0,...,t}, since
Omega_R(d)<=t. The nonexceptional exponents are already fixed by b.
Thus the number of positive carriers is at most

    (k+1)sum_{j=0}^{ell-1}binom(k,j)(t+1)^j
       <=C_2(t,ell).

Some of these choices fail other restrictions or determine the same
carrier; this only enlarges an upper bound. The same signed-sum
argument now proves (4) with C_2, and hence with their minimum.
End proof.

## 3. Uniform average of the discounted certificate

Suppose Q is a subset of primes at most Y>=2. Put

    theta_Q=product_{q in Q}(1-1/q),     mu_0=sum_{r in R_0}1/r.

Assume every occupied carrier has T_d>=Z, and consider parameters
t=t(M), ell=ell(M), Y=Y(M), Z=Z(M), with Z tending to infinity.
It is enough to impose

    mu_0/ell<=1/4,                                       (6)
    log Y=o(log Z),                                      (7)
    (log Y)^2/(ell log Z)->0.                            (8)

The bound in (6) must hold uniformly for the admitted source sets.

**Lemma.** Uniformly in d and every positive M-term interval I, for
all sufficiently large M,

    G_d:=sum_{b in I}K_d(b)>=(1/2)theta_Q T_d.             (9)

### Proof

Let C_Q(J) count integers in the real half-open interval J coprime
to product Q. With T=M/d and J=(x/d,(x+M)/d], exact division gives

    G_d=C_Q(J)-(1/ell)
         sum_{r in R_0,r<=T}C_Q(J/r).                    (10)

Fix kappa>=4 so that the error e(kappa) in the audited uniform
fundamental-lemma estimate is at most 1/16. This kappa is absolute
and remains fixed even when t and ell grow.
Put U=T/Y^kappa. By (7), U>=sqrt(T) and T>=Y^kappa uniformly for
large M.

Apply the lower sieve bound to the positive count and the upper
sieve bound to every subtraction with r<=U. Since these intervals
have lengths at least Y^kappa, their combined contribution is at least

    theta_Q T [1-mu_0/ell-e(kappa)(1+mu_0/ell)]
      >=(43/64)theta_Q T.                               (11)

For r>U, use C_Q(J/r)<=T/r+1 and enlarge to all primes in (U,T].
Chebyshev and partial summation give

    sum_{U<r<=T}(T/r+1)
      =O(T(1+kappa log Y)/log T).

The discarded coprimality condition only enlarges this upper bound.
Mertens' product estimate gives theta_Q>=c_0/log Y, uniformly for
all prime subsets Q and all Y>=2. Therefore the remaining negative
tail, after the factor 1/ell, has relative size at most

    O((1+kappa log Y)log Y/(ell log T))
      =O_kappa((log Y)^2/(ell log Z))=o(1).              (12)

Subtracting (12) from (11) proves (9). The constants are independent
of the shift, the carrier, and the source set. End proof.

The argument uses only distinct-prime counts in the negative term.
It is valid even when the interval contains a huge integer divisible
by many of the source primes simultaneously.

## 4. Source fibres and the mixed hinge

Let A be distinct sources in [2,M] supported on disjoint Q union R,
where every R-prime is at least Z. Let A_R consist of those sources
containing an R-prime. For a in A_R, remove one largest-prime occurrence:

    p(a)=Pmax(a) in R,     d(a)=a/p(a).

Let D be their distinct quotients and R_0 the R-primes appearing in
those quotients. Then D has the self-smooth property used above:
each R_0-prime dividing d is at most p(a)<=M/d. Also T_d>=Z.

Suppose the other carrier assumptions hold. If m_d is the source
fibre size, distinctness gives m_d<=pi(T_d). By Chebyshev and (9),

    m_d/G_d<=C_0 log Y/log Z,                             (13)

with an absolute C_0.

Now restrict weights to [0,1]. Then X(a)<=X(d)+1, so for every
epsilon>=0,

    (X(a)-2-epsilon)_+<=h_d.

Use (13), positivity of G_d, and then the pointwise bound (4):

    sum_{a in A_R}(X(a)-2-epsilon)_+
      <=sum_d m_d h_d
      <=C_0(log Y/log Z)sum_d G_d h_d
      <=C_0 C(t,ell)(log Y/log Z) H(X),                  (14)

where H(X)=sum_{b in I}(X(b)-1)_+.
Thus mixed sources consume a vanishing proportion of the common
target hinge whenever

    C(t,ell)log Y/log Z ->0.                             (15)

The pointwise multiplicity need not be one. The vanishing fibre
ratio absorbs its growth subject to (15).

## 5. Proof of the fixed-alpha theorem

If alpha>1 there are no mixed sources, so use the pure-core theorem.
Otherwise put Z=M^alpha and t=floor(1/alpha). Each source has at
most t R-prime occurrences, so its quotient certainly satisfies
Omega_R(d)<=t.

Every r in R_0 occurs alongside the removed prime p(a)>=r, hence
r<=sqrt(M). Therefore, by Mertens' reciprocal-prime estimate,

    mu_0<=max(0,log(1/(2alpha)))+o(1).

For alpha=1/2 the possible endpoint prime contributes o(1); for
alpha>1/2 the cofactor R-support is empty. Choose a fixed integer
ell so large that mu_0/ell<=1/4 for all sufficiently large M.

The number C(t,ell) is now a fixed constant depending only on alpha.
The hypothesis log Y=o(sqrt(log M)) implies all of (7), (8), and
(15). Equation (14) consequently gives

    sum_{a in A_R}(X(a)-2-epsilon)_+<=o(1)H(X),            (16)

uniformly in the clipped weight vector.

For the pure-Q sources, the independently audited strict contraction
in GLUING_ARBITRARY_PURE_CORE.md gives, for every fixed epsilon>0,

    sum_{a in A_Q}(X(a)-2-epsilon)_+
      <=rho_epsilon H(V)<=rho_epsilon H(X),
    rho_epsilon<1,

where V uses only the Q weights. Its hypotheses permit arbitrary
pure-Q source sets and arbitrarily many Q-prime occurrences.
For large M the coefficient in (16) is at most 1-rho_epsilon.
Adding proves the shared-hinge inequality for all sources.

The clipped raw dual therefore yields (T1). The admitted source
class is hereditary at fixed ambient M. The audited note
HEREDITARY_RAW_INTEGER_TRANSFER.md then gives (T2), using the
known ambient quadratic gate M>=16m^2 for a least failing subset.
No independent primal covers are combined, and no target capacity
is counted twice.

## 6. Exact sufficient conditions with a growing number of rough factors

The same proof applies to prescribed Y(M), Z(M), integers t(M), ell(M),
and source classes for which:

* log Y=o(sqrt(log M)), to obtain the strict pure-core contraction;
* each mixed-source quotient has Omega_R(d)<=t;
* every mixed source has its largest prime at least Z, and the
  quotient R-primes satisfy the self-smooth condition;
* the uniform reciprocal bound mu_0/ell<=1/4 holds;
* conditions (7), (8), and (15) hold.

These are sufficient conditions, not an unrestricted bound.
For the simple support class all R-primes>=Z, one may take

    t=floor(log M/log Z)

in the nonempty case. Deleting sources preserves this class and
can only shrink R_0, so the integer transfer remains available.

When t tends to infinity and Z tends to infinity, the cofactor
restriction R_0 subset [Z,sqrt(M)] and Mertens imply
mu_0<=log t+o(1), with an immaterial bounded allowance for endpoints.
One may safely choose

    ell=ceil(4 log(2t)+4).

The sharper multiplicity bound gives

    log C(t,ell)<=log C_2(t,ell)
       <=8(log t)^2+O(log t).                            (17)

For example, bound the sum in (3) by ell times
[(t+ell-1)(t+1)]^(ell-1). The nonexceptional prime exponents are
already fixed by the target integer; adding an unrestricted
exponent factor for them would lose this sharper estimate.

## 7. One explicit subpolynomial rough cutoff

Fix constants 0<a<1/2 and c>0 such that

    8c^2<1-a.

Let

    Y(M)=exp((log M)^a),
    Z(M)=exp(log M / exp(c sqrt(log log M))).

Then t=floor(log M/log Z) has
log t=c sqrt(log log M)+o(1). Choose ell as in Section 6.
Equation (17) gives

    C(t,ell)<=(log M)^(8c^2+o(1)).

Moreover

    log Y/log Z=(log M)^(a-1+o(1)),
    (log Y)^2/(ell log Z)=(log M)^(2a-1+o(1))->0.

Consequently (15) follows from 8c^2+a-1<0, and all other hypotheses
of Section 6 hold. Thus (T1)--(T2) remain valid for sources whose
primes are at most Y(M) or at least this Z(M), with arbitrarily many
rough occurrences allowed by the size bound.

For a concrete choice, take a=1/3 and c=1/4. Then

    Y=exp((log M)^(1/3)),
    Z=exp(log M / exp((1/4)sqrt(log log M))),
    C(t,ell)<=(log M)^(1/2+o(1)),
    C(t,ell)log Y/log Z<=(log M)^(-1/6+o(1))->0,
    (log Y)^2/(ell log Z)=(log M)^(-1/3+o(1))->0.

The rough threshold is M raised to the exponent
exp(-(1/4)sqrt(log log M)), which tends to zero. Thus this example
does not require a fixed positive power threshold for rough primes.

This is an example, not an optimized cutoff. It still leaves a
substantial intermediate prime range untreated and does not give
the unrestricted exact or asymptotic conjecture.
