# Independent audit: the mixed separated-support certificate

Date: 2026-11-23.

**Status: PASS.** This note independently verifies the weighted adaptive
certificate, its uniform sieve-tail bound, and the mixed-source hinge
estimate in Section 8 of
`../analytic/GLUING_ARBITRARY_PURE_CORE.md`. Sections 1--7 of that note,
including the strict pure-core contraction, also pass the mathematical
audit after the intermediate carrier coefficients in Section 2 were
corrected. This is a restricted theorem, not a solution of unrestricted
Erdős Problem 708.

The only external analytic inputs are the previously audited uniform
fundamental-lemma estimate, Chebyshev's prime-counting upper bound, and
Mertens' product and reciprocal-prime estimates. Every interval of real
length T below means a positive half-open interval, with its integer
points understood.

## 1. Precise abstract certificate lemma

The certificate works under the following slightly more general
hypotheses. Let Y(M)>=2 and Z(M)>1 be prescribed functions with

    (log Y)^2=o(log Z).

Let Q and R be disjoint finite prime sets with Q contained in [2,Y]
and R contained in [Z,infinity). Let A be a set of distinct integers
in [2,M] supported on Q union R, and let I be any positive M-term
interval. For a source containing an R-prime, put

    p(a)=Pmax(a),     d(a)=a/p(a),     T_d=M/d.

For large M, the separation ensures that p(a) belongs to R. Let D be
the set of these distinct quotients, and R_0 the union of their
R-prime supports. Assume that a fixed delta>0 satisfies

    mu_0=sum_{r in R_0}1/r <=1-delta.                       (1)

An empty mixed-source class is trivial. Otherwise Z<=M, and every
occupied quotient has T_d>=p(a)>=Z. Every R-prime dividing d is at
most p(a), hence at most T_d.

Write theta_Q=product_{q in Q}(1-1/q). Uniformly over occupied fibres,
all shifts, all support choices, and all source sets, the signed
counts defined below satisfy, for sufficiently large M,

    G_d >=(delta/2)theta_Q T_d,                            (2)
    m_d <=beta_M G_d,    beta_M=O_delta(log Y/log Z)=o(1),  (3)

where m_d is the number of source preimages of d. Thresholds may
depend on delta and the prescribed functions Y,Z, but not on the
source set, its cardinality, its weights, or the interval shift.

If Z>M, the mixed-source class is empty. The growth condition forces
log Z to tend to infinity because log Y>=log 2.

## 2. Unique positivity and the weighted pointwise inequality

For b in I set K_d(b)=0 if d does not divide b. Otherwise define

    K_d(b)=1[gcd(b/d,product Q)=1]
           (1-sum_{r in R_0,r<=M/d}1[r divides b/d]).

A positive term equals one. It forces d to be exactly the full
smooth part of b supported on

    Q union (R_0 intersect [2,M/d]).                       (4)

This uses both facts that d has no other prime factors and that the
cofactor b/d contains no additional occurrences from this set.
Repeated prime powers cause no difficulty.

There cannot be two positive terms. If d<e were positive, the prime
set in (4) for d would contain that for e. Its full smooth part would
therefore be at least as large, giving d>=e, a contradiction.

Let X(b)=sum_p w_p v_p(b) for any nonnegative weights, and set
h_d=(X(d)-1)_+. If d|b, then h_d<=(X(b)-1)_+. All nonpositive K_d
terms remain nonpositive after multiplication by h_d, and there is
at most one positive term. Thus

    sum_d h_d K_d(b)<=(X(b)-1)_+.                          (5)

For G_d=sum_{b in I}K_d(b) and H(X)=sum_{b in I}(X(b)-1)_+,

    sum_d h_d G_d<=H(X).                                  (6)

This is a signed-certificate argument. Negative summands are not
silently discarded before their averages are estimated.

## 3. The uniform lower bound on G_d

Let C_Q(J) count the integers in a real interval J coprime to
product Q. For T=M/d and J=(x/d,(x+M)/d], exact division gives

    G_d=C_Q(J)-sum_{r in R_0,r<=T}C_Q(J/r).                 (7)

Division by an R-prime preserves the Q-coprimality condition.

Choose a fixed kappa>=4, depending only on delta, so that the
audited uniform sieve error satisfies e(kappa)<=delta/8. Put
U=T/Y^kappa. Since T>=Z and (log Y)^2=o(log Z), uniformly over all
occupied fibres, T>=Y^kappa and U>=sqrt(T) for large M.

The base count and terms with r<=U have quotient lengths at least
Y^kappa. Applying the lower sieve bound to the base and the upper
bound to these subtracted terms gives

    theta_Q T [(1-e(kappa))
       -(1+e(kappa))sum_{r in R_0,r<=U}1/r]
      >=theta_Q T [1-mu_0-e(kappa)(1+mu_0)]
      >=(3delta/4)theta_Q T.                              (8)

For U<r<=T use only C_Q(J/r)<=T/r+1. Enlarging the prime set to all
primes bounds the remaining subtraction by

    T sum_{U<r<=T}1/r+pi(T).                               (9)

Chebyshev's estimate and partial summation imply, for U>=sqrt(T),

    sum_{U<r<=T}1/r
      <=C/log T+C integral_U^T dt/(t log t)
      =O((1+log(T/U))/log T)
      =O((1+kappa log Y)/log T).                          (10)

Also pi(T)=O(T/log T). Mertens' product bound, enlarged to cover
all Y>=2, gives theta_Q>=c_0/log Y for every prime subset Q.
Therefore the ratio of (9) to theta_Q T is at most

    O((1+kappa log Y)log Y/log T)
      <=O_kappa((log Y)^2/log Z)=o(1).                    (11)

The constant absorbs the bounded lower endpoint log Y>=log 2.
For large M this tail is at most (delta/4)theta_Q T.
Equations (8)--(11) prove (2).

The fixed-kappa sieve error and the unsieved tail are different
losses: the former consumes a fixed portion of the harmonic slack,
and the latter tends to zero uniformly.

## 4. Fibre dilution and mixed sources

Sources with the same quotient d have the form d p(a), with distinct
removed primes p(a)<=T_d. Thus m_d<=pi(T_d). Combining Chebyshev,
(2), and theta_Q>=c_0/log Y proves

    m_d/G_d<=C_delta log Y/log T_d
             <=C_delta log Y/log Z=beta_M=o(1).

For weights in [0,1], X(a)<=X(d)+1. Hence for every epsilon>=0,

    (X(a)-2-epsilon)_+<=(X(d)-1)_+=h_d.

Consequently,

    sum_{a in A_R}(X(a)-2-epsilon)_+
      <=sum_d m_d h_d
      <=beta_M sum_d G_d h_d
      <=beta_M H(X).                                     (12)

Positivity of each G_d, established in (2), justifies the middle
inequality. No restriction on the number of R-prime occurrences in
a source was used. Prime sources have d=1 and h_d=0.

## 5. The polynomial-cutoff specialization

Suppose min R>=M^alpha for fixed alpha>1/(2e), and
log Y=o(sqrt(log M)).

If r belongs to R_0, it occurs in some quotient a/Pmax(a).
The removed prime is at least r, so a>=r^2. This remains true when
the two occurrences have the same prime value. Therefore

    R_0 subset [M^alpha,sqrt(M)].

For alpha<1/2, Mertens' reciprocal-prime estimate gives

    mu_0<=log(1/(2alpha))+o(1)<1.

A fixed positive delta smaller than 1-log(1/(2alpha)) therefore
works for all large M. For alpha=1/2 the possible cofactor support
contains at most the endpoint prime sqrt(M), so its reciprocal mass
tends to zero. For alpha>1/2 it is empty.

With Z=M^alpha, condition (11) becomes

    (log Y)^2/log Z=(log Y)^2/(alpha log M)->0.

Thus the proposed Section 8 satisfies all hypotheses, including the
endpoint alpha=1/2 and repeated-prime cases. The bound beta_M is
O_alpha,delta(log Y/log M).

## 6. The pure-core and shared-budget steps

For the gluing conclusion, impose the additional pure-core cutoff
log Y=o(sqrt(log M)). It is already part of the polynomial-cutoff
specialization. The abstract mixed certificate alone does not replace
this pure-core hypothesis when the mixed-source class is empty.

The strict pure-core theorem in the analytic note proves, for each
fixed epsilon>0 and all sufficiently large M, that

    sum_{a in A_Q}(V(a)-2-epsilon)_+
      <=rho_epsilon H(V),       rho_epsilon<1.

Its three cases pass the audit:

* Small weights and low weighted mean retain a strict ratio in the
  audited diffuse carrier proof. If S is the carrier sum, the precise
  bounds are source<=A_eta S/(ell-eta) and target>=(1-e(r))S;
  their ratio is A_eta/B_eta. These intermediate coefficients have
  been corrected in the analytic note.
* Small weights and high mean give H(V)>=epsilon M/8 from the
  first-moment bound. The smooth-source count times log_2 M is o(M).
* A weight at least eta supplies a prime-power bank with
  H(V)>=M/(2Y^J). Rankin's estimate makes the total pure-source
  hinge o(M/Y^J), uniformly in the prime subset and weights.

Since V<=X pointwise, H(V)<=H(X). Adding the pure-core estimate and
(12), and taking M large enough that rho_epsilon+beta_M<=1, gives

    sum_{a in A}(X(a)-2-epsilon)_+<=H(X).

The clipped raw dual then yields
L_raw(A,I)<=(2+epsilon)|A|. Both source classes use one common
target-hinge budget, so no physical position is counted twice.

## 7. Quantifiers, integer transfer, and scope

All hypotheses retain the original ambient M when sources are
deleted. Subsets retain the support restrictions, while R_0 can
only shrink. Thus the classes are hereditary at fixed M.

The separate note
`../computation/HEREDITARY_RAW_INTEGER_TRANSFER.md` also passes a
logical audit. A least failing subset has all source primes below
K=floor(c(m-1))+1<=cm, and therefore at most pi(cm)=o(m) prime rows.
Row-count rounding costs at most that amount. The ambient quadratic
gate M>=16m^2 forces every failing subset to have m>sqrt(M)/4,
so the uniform large-M fractional bound and the small rounding error
apply together. No additive-constant threshold or dependence on a
moving source maximum is hidden in this step.

The new results still impose a gap between the subexponential core
and the rough support. The arbitrary-occurrence theorem additionally
uses harmonic slack for cofactor rough primes; the polynomial
condition alpha>1/(2e) is a sufficient way to obtain that slack.
Neither assumption follows for the unrestricted growing core of a
minimal counterexample.
