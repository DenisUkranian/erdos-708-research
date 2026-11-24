# Gluing arbitrary pure-core sources to separated rough factors

## Status

This note proves joint fractional estimates proposed by the parent research agent. A complete independent internal audit checked Sections 1--8, including the strict A/B/C contraction, adaptive certificate, sieve tail, fibre bounds, and uniform quantifiers, and found no remaining substantive error. This is not a claim of external verification. Sections 1--7 close the pure-core excess term in the earlier separated one-rough-prime result. Section 8 also permits arbitrary rough-prime occurrences above a polynomial cutoff. Neither theorem proves unrestricted Erdős 708: explicit prime-range hypotheses remain.

The proof uses one shared target hinge sum. It does not add the costs of two independently constructed covers. Integer transfer is a separate step and is not assumed here.

## 1. Statement and quantifiers

Let Y=Y(M)>=2 and Z=Z(M)>1 be prescribed functions such that, as M tends to infinity,

    log Y = o(sqrt(log M)),
    log Y = o(log Z).                                      (1)

Fix epsilon>0. For all sufficiently large M, uniformly over the following data, the conclusion below holds:

* Q is any finite set of primes at most Y;
* R is any finite set of primes at least Z;
* A is any set of distinct integers in [2,M], all of whose prime factors lie in Q union R;
* every source containing a prime of R has exactly one R-prime occurrence, counting multiplicity;
* I is any positive interval of M consecutive integers;
* all raw prime weights are in [0,1].

The last source condition applies also to sources with no Q-factor: a source consisting of a single R-prime is permitted, whereas a source with two R-prime occurrences is not covered by this theorem.

For sufficiently large M the two prime sets are disjoint. Write

    X(a)=V(a)+W(a),
    V(a)=sum_{q in Q}w_q v_q(a),
    W(a)=sum_{r in R}w_r v_r(a),
    c=2+epsilon.

Then

    sum_{a in A}(X(a)-c)_+
        <= sum_{b in I}(X(b)-1)_+.                         (2)

Consequently the raw boxed covering relaxation satisfies

    L_raw(A,I) <= (2+epsilon)|A|.                           (3)

The threshold in M may depend on epsilon and on the two functions in (1), but not on Q, R, A, the weights, the source cardinality, or the interval shift. The ambient M need not equal max A; it is enough that max A<=M. This fixed-ambient formulation is relevant to hereditary arguments.

## 2. Previously proved analytic input and a strict version

For reference, the audited uniform sieve estimate has the following form. There is an absolute C and a decreasing function

    e(t)=C[(t/2)^(-t/4)+2^(1-t/2)],       t>=4,

with e(t)->0, such that an interval J of real length T>=z^t satisfies

    #{m in J: gcd(m,product P)=1}
      = T product_{p in P}(1-1/p) [1+error],
    |error|<=e(t),                                         (4)

for every subset P of the primes at most z, uniformly in its shift.

The partial prime-power carrier proof in
`ep708_synthesis_20261123/analytic/DIFFUSE_RAW_WEIGHTS.md`
also gives a strict level ratio. Here are the exact parameters needed, so that the strictness is not inferred merely from a non-strict theorem.

It is enough to consider 0<epsilon<=1. Put ell=1+epsilon and choose eta=eta_epsilon>0 sufficiently small that eta<=epsilon/24. Define

    r=floor(ell/eta)>=8,
    j=floor(r/2),
    kappa=r-j,
    A_eta=(1+e(kappa))(1+epsilon/4)+eta 2^(1-j),
    B_eta=(ell-eta)(1-e(r)).

We can and do require B_eta>0 and

    A_eta/B_eta <= rho_epsilon,
    rho_epsilon=(1+epsilon/2)/(1+epsilon)<1.                (5)

Such a choice is possible because, as eta decreases to zero, the ratio on the left tends to (1+epsilon/4)/(1+epsilon), strictly below rho_epsilon. All these choices depend on epsilon alone.

If 0<=w_q<=eta and

    mu=sum_{q in Q}w_q/(q-1)<=1+epsilon/4,

then the carrier proof gives, at every real length T, shift J, and level s>=0,

    #{a<=T: V(a)>s+ell}
       <= rho_epsilon #{b in J: V(b)>s}.                   (6)

Indeed, if F_s is its carrier family, the source count is at most

    [A_eta/(ell-eta)] sum_{d in F_s}(T/d) V_{Pmax(d)},

whereas the target count is at least the same carrier sum times 1-e(r). Their ratio is exactly A_eta/B_eta. The carriers allow a partial final prime-power block. The low-power terms are controlled by (4), and the high-power tail is eta 2^(1-j). These are exactly the estimates in the audited diffuse proof, now retaining their ratio rather than replacing it by one. Thus (5) proves (6).

Integrating (6) over s>=1 gives the strict hinge estimate

    sum_{a<=M}(V(a)-2-epsilon)_+
       <= rho_epsilon sum_{b in I}(V(b)-1)_+.              (7)

## 3. A uniform smooth-number bound

Let Psi(M,Y) be the number of positive integers at most M all of whose prime factors are at most Y. Put L=log M and y=log Y. The elementary Rankin estimate used in the earlier dense-support theorem gives

    Psi(M,Y) <= M exp(-L/(4y)+4y).                          (8)

For clarity, take sigma=1/(4y). For every p<=Y,

    z_p=p^(-1+sigma)<=exp(1/4)/p,
    z_p/(1-z_p)<=4/p.

Therefore

    product_{p<=Y}(1-p^(-1+sigma))^(-1)<=Y^4,

and Rankin's inequality yields (8).

In particular, for every fixed J>=0,

    [Psi(M,Y) log_2 M] / [M/Y^J]
      <= (log_2 M) exp(-L/(4y)+(J+4)y)
      =: omega_J(M) -> 0                                  (9)

under the first condition in (1). To check the logarithmic factor as well, y=o(sqrt L) implies L/y is much larger than both y and log L. Thus the negative exponent dominates (J+4)y+log log_2 M. This limit is uniform in the prime subset Q and in all weights.

## 4. A strict pure-core budget for every weight vector

Let

    A_Q={a in A: all prime factors of a lie in Q},
    H(V)=sum_{b in I}(V(b)-1)_+,
    S_Q(V)=sum_{a in A_Q}(V(a)-2-epsilon)_+.

For all sufficiently large M,

    S_Q(V) <= rho_epsilon H(V)                            (10)

uniformly over every vector 0<=w_q<=1, with the same rho_epsilon<1 as in (5). There are three cases.

### Case A: all weights small and the weighted mean low

Suppose max_q w_q<=eta and mu<=1+epsilon/4. The distinct pure-core sources form a subset of the full prefix, so (7) directly gives (10). This includes the empty core and the zero weight vector; if H(V)=0, the same inequality forces S_Q(V)=0.

### Case B: all weights small and the weighted mean high

Suppose max_q w_q<=eta and mu>=1+epsilon/4. The elementary first-moment estimate for raw valuations gives

    sum_{a<=M}V(a) >= M(mu-3eta).

Here all q<=Y<M for large M. Since every prime-power count in I is at least its prefix count,

    H(V) >= sum_{b in I}V(b)-M
         >= M(mu-3eta-1)
         >= epsilon M/8,                                 (11)

by eta<=epsilon/24. No second-moment estimate is needed in this case.

On the other hand, every pure-core source is Y-smooth, and V(a)<=Omega(a)<=log_2 M. Therefore

    S_Q(V) <= Psi(M,Y) log_2 M.

By (9) with J=0, this is o(M), uniformly in the weights. Its ratio to (11) tends to zero, and is eventually at most rho_epsilon.

### Case C: at least one core weight is substantial

Suppose some w_q>=eta. Let

    j_q=ceil(2/w_q),
    J_epsilon=ceil(2/eta),
    D=q^(j_q)<=Y^(J_epsilon).

Every multiple of D has V>=2. Since M/Y^(J_epsilon) tends to infinity,

    H(V) >= floor(M/D) >= M/(2Y^(J_epsilon))               (12)

for all sufficiently large M. The same bound S_Q(V)<=Psi(M,Y)log_2M, now combined with (9) at J=J_epsilon, shows that the ratio of S_Q(V) to (12) tends uniformly to zero. It is eventually at most rho_epsilon.

The three cases prove (10). In particular, the strict pure-core budget does not assume that the pure-core sources have bounded Omega, bounded cardinality, or a bounded number of prime factors in their combined support.

## 5. Uniform dilution of the mixed-source fibres

Every source outside A_Q has a unique representation

    a=d r,
    d is Q-smooth,
    r is a prime in R.

Let m_d be the number of such sources with the same d, and let N_d be the number of target positions b in I whose exact Q-smooth part is d. These target bins are disjoint. If m_d>0, set T=M/d; then T>=r>=Z and

    m_d <= #{r in R:r<=T} <= pi(T),                         (13)

because distinct sources in a fibre have distinct r.

Set kappa_M=log Z/log Y. By (1), kappa_M tends to infinity. The target count N_d is the number of integers coprime to product Q in a shifted interval of length T>=Y^(kappa_M). Therefore (4) gives

    N_d >= (1-e(kappa_M)) theta_Q T,
    theta_Q=product_{q in Q}(1-1/q).                       (14)

Use absolute constants c_0,C_0>0 such that

    theta_Q>=c_0/log Y,
    pi(T)<=C_0 T/log T.

The first estimate follows from Mertens' product theorem and remains valid for every subset Q; the second is the usual uniform Chebyshev upper bound. Enlarging constants handles all Y,T>=2. Combining (13)--(14), for all sufficiently large M,

    m_d <= beta_M N_d,
    beta_M=(2C_0/c_0)(log Y/log Z) -> 0.                   (15)

The estimate is uniform over all occupied fibres. If Z>M, no such fibre exists and the mixed-source contribution is zero.

## 6. The joint hinge estimate

For a mixed source a=d r, the one-occurrence hypothesis and w_r<=1 give

    (X(a)-2-epsilon)_+
      =(V(d)+w_r-2-epsilon)_+
      <=(V(d)-1)_+.

Consequently, by (15),

    sum_{a in A\A_Q}(X(a)-2-epsilon)_+
      <= sum_d m_d(V(d)-1)_+
      <= beta_M sum_d N_d(V(d)-1)_+
      <= beta_M H(V).                                     (16)

The last inequality uses exact Q-parts: V(b)=V(d) throughout the bin with exact Q-part d. Bins not occupied by a source contribute nonnegatively to H(V).

For all sufficiently large M, beta_M<=1-rho_epsilon. Adding (10) and (16) therefore gives

    sum_{a in A}(X(a)-2-epsilon)_+
      <= (rho_epsilon+beta_M)H(V)
      <= H(V)
      <= sum_{b in I}(X(b)-1)_+.

This proves (2). Both source classes were charged to the same core hinge H(V), with coefficients summing to at most one. No independent integer covers or independently rounded LP solutions were combined.

## 7. The raw fractional consequence

For a distinct source set in [2,M], the boxed raw dual is

    L_raw(A,I)=max_{0<=w_p<=1}
        [sum_{a in A}X_w(a)-sum_{b in I}(X_w(b)-1)_+].

Clipping the dual weights to [0,1] is valid because the full interval supplies every source prime demand. This dual identity and clipping argument are proved in the audited consolidated section `ep708_synthesis_20261123/sections/analytic.tex`, Lemma `an:lp-bridge`.

For each clipped vector,

    sum_{a in A}X_w(a)
      <= (2+epsilon)|A|+sum_{a in A}(X_w(a)-2-epsilon)_+.

Apply (2) and then maximize over the dual weights to obtain (3).

There is no row-count or integer-rounding assertion hidden in this argument. A separate hereditary or transference argument is required to deduce an integer-cover theorem when the rough prime set has many rows.

## 8. Arbitrarily many rough-prime occurrences above a polynomial cutoff

### The stronger theorem

Fix alpha>1/(2e) and epsilon>0, and let Y(M)>=2 satisfy logY=o(sqrt(logM)). Let Q be any set of primes at most Y, and R any set of primes at least M^alpha. Let A be any distinct source set in [2,M] supported on Q union R. There is now **no restriction on the number of R-prime occurrences in a source**. For all sufficiently large M, uniformly over Q, R, A, the shift, and all weights in [0,1],

    sum_{a in A}(X(a)-2-epsilon)_+
        <= sum_{b in I}(X(b)-1)_+,                         (17)

and hence

    L_raw(A,I)<=(2+epsilon)|A|.                            (18)

Here alpha is fixed. If alpha>1, no source at most M can have an R-prime, so the assertion reduces to the pure-core case. We may therefore assume alpha<=1 in the proof.

### 8.1 The cofactor prime set and its reciprocal mass

Let A_R=A\A_Q. For each a in A_R, remove one occurrence of its largest prime:

    p(a)=Pmax(a) in R,
    d(a)=a/p(a).

For large M, all Q-primes are smaller than all R-primes, since logY=o(logM). Thus p(a) is indeed in R. Let D be the set of distinct cofactors d(a), and let

    R_0={r in R:r divides some d in D}.

If r divides d(a), then r<=p(a) and r p(a)<=a<=M. Therefore

    R_0 subset [M^alpha,sqrt M].                           (19)

Mertens' reciprocal-prime estimate gives a fixed delta=delta_alpha>0 such that, for all sufficiently large M,

    mu_0=sum_{r in R_0}1/r<=1-delta.                       (20)

For 1/(2e)<alpha<1/2, the upper bound for this sum is log(1/(2alpha))+o(1)<1, so one may choose delta=(1-log(1/(2alpha)))/2. For alpha>1/2 the set R_0 is empty. At alpha=1/2 it contains at most the endpoint prime, so its mass tends to zero; delta=1/2 works eventually in both cases alpha>=1/2.

Every d in D is smooth over Q union R_0. Moreover, with T_d=M/d,

    Pmax(d)<=p(a)<=T_d,
    T_d>=M^alpha,                                         (21)

where Pmax(1)=1. The first assertion is independent of the choice of source in a fibre and is the required self-smoothness property.

### 8.2 A weighted adaptive fixed-point certificate

For d in D, put h_d=(X(d)-1)_+. Define K_d(b)=0 if d does not divide b. Otherwise set

    K_d(b)=1_{gcd(b/d,product Q)=1}
              [1-sum_{r in R_0,r<=T_d}1_{r|b/d}].         (22)

Then, for every positive integer b,

    sum_{d in D} h_d K_d(b)<=(X(b)-1)_+.                   (23)

Indeed, a positive term in (22) equals one and requires no extra Q-factor in b/d and no extra R_0-prime at most T_d. By (21), all prime divisors of d are among Q union (R_0 intersect [2,T_d]). Thus positivity forces

    d=smooth_{Q union (R_0 intersect [2,M/d])}(b).

The right side is nonincreasing as d increases, so there is at most one fixed point. Every other K_d is nonpositive. At the possible positive term, X(d)<=X(b), so h_d<=(X(b)-1)_+. This proves (23). The argument permits repeated prime powers in d and in b.

Write

    G_d=sum_{b in I}K_d(b),
    theta_Q=product_{q in Q}(1-1/q).

We next prove the uniform lower bound

    G_d >= (delta/2)theta_Q T_d.                           (24)

### 8.3 Sieve estimate for the certificate

Choose a fixed kappa>=4 so large that e(kappa)<=delta/8. Abbreviate T=T_d. The interval of quotients b/d has real length T, and

    G_d=S_Q(J_d)-sum_{r in R_0,r<=T}S_Q(J_d/r),

where S_Q counts integers coprime to product Q. Division by r preserves this coprimality, since Q and R_0 are disjoint.

For large M, T>=M^alpha>=Y^kappa. Split the subtracted primes into r<=T/Y^kappa and T/Y^kappa<r<=T. On the first group, all quotient intervals have length at least Y^kappa. Apply (4) to the base count and these subtracted counts. Their combined contribution is at least

    theta_Q T[(1-e(kappa))
          -(1+e(kappa))sum_{r in R_0,r<=T/Y^kappa}1/r]
      >= theta_Q T[1-mu_0-e(kappa)(1+mu_0)]
      >= (3delta/4)theta_Q T.                             (25)

For the remaining primes, discard coprimality and use the crude count T/r+1. Put U=T/Y^kappa. Uniformly for T in [M^alpha,M], we have logU=logT-kappa logY and kappa logY=o(logT). Partial summation and the Chebyshev bound yield

    sum_{U<r<=T, r prime}1/r
      <= C/logT + C log(logT/logU)
      <= C'(1+kappa logY)/logT.

Consequently the entire remaining subtraction is at most

    sum_{U<r<=T}(T/r+1)
      <= C'' T(1+kappa logY)/logT.                         (26)

Since theta_Q>=c_0/logY, the ratio of (26) to theta_Q T is

    O( (logY)(1+kappa logY)/logT )
      =o(1),                                             (27)

uniformly over d, by logT>=alpha logM and logY=o(sqrt(logM)). For all sufficiently large M, (26) is therefore at most (delta/4)theta_Q T. Combining with (25) proves (24).

### 8.4 Dilution of source fibres and the common target budget

Let m_d=#{a in A_R:d(a)=d}. Distinct sources in a fixed fibre have distinct removed primes p(a)<=T_d, so m_d<=pi(T_d). By (24), Chebyshev's upper bound, and the lower bound for theta_Q,

    m_d/G_d <= C_alpha (logY/logT_d)
              <= C'_alpha (logY/logM)
              =: beta_M -> 0.                            (28)

All constants are independent of the particular source set and weights. The prime-demand condition D_p(A)>p or its negation is not used here.

For a=d p(a), complete additivity and w_{p(a)}<=1 give

    (X(a)-2-epsilon)_+ <= (X(d)-1)_+ = h_d.

Thus, using (28), then (23),

    sum_{a in A_R}(X(a)-2-epsilon)_+
      <=sum_{d in D}m_d h_d
      <=beta_M sum_{d in D}G_d h_d
      <=beta_M sum_{b in I}(X(b)-1)_+.                     (29)

The pure-core strict contraction (10) is unchanged and gives

    sum_{a in A_Q}(X(a)-2-epsilon)_+
      <=rho_epsilon H(V)
      <=rho_epsilon sum_{b in I}(X(b)-1)_+.

For sufficiently large M, rho_epsilon+beta_M<=1. Adding this inequality to (29) proves (17), and the raw dual argument of Section 7 proves (18).

The target certificate in this extension is signed, but its average G_d is positive by (24). Its positive terms are unique at each target position, so (29) does not double count physical target capacity.

## Primary analytic inputs

The sieve estimate (4) is the audited consequence of the fundamental lemma of the combinatorial sieve, with interval divisibility remainders bounded by one:

* J. C. Lagarias, *Math 675: Combinatorial Sieve: Fundamental Lemma*: https://websites.umich.edu/lagarias/675notes/Estimate5-2015.pdf
* A. Granville and K. Soundararajan, *Multiplicative number theory: The pretentious approach*, Theorem 1.4.2; the same text records the elementary Chebyshev bounds: https://dms.umontreal.ca/~andrew/PDF/Book.To1.4.pdf

For the Mertens product estimate used only in the fibre dilution step:

* T. Tao, *Mertens' theorems*, especially the product statement: https://terrytao.wordpress.com/2013/12/11/mertens-theorems/

## Remaining scope restriction

Sections 1--7 remove the earlier restriction on arbitrary pure-core sources in the separated one-rough-prime class. Section 8 removes the one-occurrence restriction when all rough primes are at least M^alpha for fixed alpha>1/(2e). Both results retain logY=o(sqrt(logM)); the unrestricted problem includes primes in the intermediate range between this core cutoff and M^alpha. None of these hypotheses follows for the general growing core in a possible minimal obstruction to Erdős 708.

