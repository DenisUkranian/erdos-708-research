# A diffuse core with arbitrarily many possible one-prime remainders

## Status and significance

This is a source-specific gluing argument whose Sections 1--9 have passed independent internal audits. It uses the uniform level comparison for a diffuse raw core, together with superadditivity of the target hinge increments. No prime-size separation, reciprocal-mass hypothesis, support-cardinality bound, or restriction on the interval shift is imposed. Section 9 adds a further one-exception core extension. No external verification or general solution is claimed.

In particular, it applies directly to the structural class in which every source has at most one R-prime occurrence, regardless of how many R-primes have substantial dual weights. It proves the required coefficient-two approximate hinge bound for every vector whose E-core weights are diffuse, and Section 9 permits one arbitrary core coordinate without error. The companion note `CONTROLLED_CORE_SINGLE_REMAINDER.md` now extends the method to k substantial core coordinates with an explicit error independent of M. The unrestricted growing-core case remains open.

## 1. Main theorem

For every epsilon>0 there exists eta_epsilon>0 with the following property. Let E and R be disjoint finite sets of primes, and let

    V(n)=sum_{p in E}w_p v_p(n),        0<=w_p<=eta_epsilon,
    W(n)=sum_{r in R}w_r v_r(n),        w_r>=0,
    X(n)=V(n)+W(n).

Let A be any set of distinct integers in [2,M], and suppose every source is divisible by at most one **distinct** prime from R. Arbitrary powers of that one R-prime are allowed. Prime factors outside E union R, on which the load is zero, are also allowed.

For every positive interval I of M consecutive integers,

    sum_{a in A}(X(a)-2-epsilon)_+
       <= sum_{b in I}(X(b)-1)_+.                          (1)

The exceptional R-weights may be arbitrary nonnegative numbers in this auxiliary theorem. In the raw covering dual they are, as usual, clipped to [0,1]. The constant eta_epsilon is independent of E, R, M, A, all individual prime sizes, and the shift.

The stated one-distinct-prime condition is stronger than needed for an individual weight vector: it suffices that each source has at most one R-prime with a positive weight. We use the structural formulation above to avoid a weight-dependent source class.

## 2. Uniform level comparison retained with a strict ratio

It suffices to treat 0<epsilon<=1. Put

    ell=1+epsilon,
    c=1+ell=2+epsilon,
    mu_E=sum_{p in E}w_p/(p-1).

Use the error e(t)->0 from the audited uniform sieve estimate. Choose eta=eta_epsilon>0 so small that

    eta<=epsilon^2/128,
    r=floor(ell/eta)>=8,
    j=floor(r/2),
    kappa=r-j,

and

    [(1+e(kappa))(1+epsilon/2)+eta 2^(1-j)]
       /[(ell-eta)(1-e(r))]
       <= rho_epsilon,
    rho_epsilon=(1+3epsilon/4)/(1+epsilon)<1.               (2)

The denominator is positive for small eta. Such a choice exists because the ratio on the left tends to (1+epsilon/2)/(1+epsilon), strictly below rho_epsilon.

The partial prime-power carrier proof then gives, whenever mu_E<=1+epsilon/2,

    #{a<=T:V(a)>s+ell}
       <= rho_epsilon #{b in J:V(b)>s}                    (3)

for every real length T>0, every positive interval J of that length, and every s>=0. To be precise, the carrier source coefficient is

    [(1+e(kappa))mu_E+eta 2^(1-j)]/(ell-eta),

and the target coefficient is 1-e(r); their quotient is bounded by (2). This is the audited diffuse proof with its strict ratio retained.

In particular, integrating over s>=1 gives

    sum_{a<=M}(V(a)-c)_+
       <= rho_epsilon sum_{b in I}(V(b)-1)_+.              (4)

The same estimates hold at all smaller lengths. Primes above a given prefix length may be removed and then restored on the target side; their removal decreases mu_E and changes no prefix load.

## 3. The large-mean case

Discard core primes greater than M before computing mu_E. This changes no source load and only decreases the target load. If

    mu_E>=1+epsilon/2,

the previously proved elementary moment estimate

    E_prefix(V-mu_E)^2<=8eta mu_E

implies

    sum_{a<=M}min(V(a),2)>=M,

because eta<=epsilon^2/128. Adding the nonnegative R-load preserves the capped inequality. Prime-power counting gives

    Delta_2(M,I,X)
      <= M-sum_{a<=M}min(X(a),2)<=0.

Passing from the full prefix to the source subset and increasing the prefix threshold to c proves (1). This case does not require the one-prime restriction on the sources.

It remains to consider mu_E<=1+epsilon/2, when (3)--(4) apply.

## 4. Capping the R-coordinates

For each r in R, set

    u_r(e)=min(w_r e,1),
    t_r(e)=(w_r e-1)_+,
    U(n)=sum_{r in R}u_r(v_r(n)),
    T(n)=sum_{r in R}t_r(v_r(n)).

Then X=V+U+T. All u_r are nondecreasing, take values in [0,1], and vanish at zero. For the moment we prove the stronger capped estimate

    sum_{a in A}(V(a)+U(a)-c)_+
       <= rho_epsilon sum_{b in I}(V(b)+U(b)-1)_+.          (5)

## 5. Individual increments and the one-prime source identity

For h equal to c or 1, define

    D_{h,r}(n)
      =(V(n)+u_r(v_r(n))-h)_+-(V(n)-h)_+.

These functions are nonnegative. The exact telescoping identity is

    D_{h,r}(n)
      =sum_{j>=1}1_{r^j|n}
          integral_{u_r(j-1)}^{u_r(j)}1_{V(n)>h-v} dv.     (6)

For each v in these integrals, s=1-v>=0 and c-v=s+ell. Also V(r^j t)=V(t), because E and R are disjoint. Multiples of r^j in the prefix rescale to the prefix of length N=floor(M/r^j); those in I rescale to a consecutive interval with at least N positions. If N=0 the prefix term vanishes. Otherwise apply (3) to any N-term subinterval of the target quotient interval. The extra target positions have nonnegative contributions. Integrating and summing gives

    sum_{a<=M}D_{c,r}(a)
       <= rho_epsilon sum_{b in I}D_{1,r}(b).              (7)

For each source a, at most one capped R-coordinate is nonzero. Therefore

    (V(a)+U(a)-c)_+
      =(V(a)-c)_+ + sum_{r in R}D_{c,r}(a).                (8)

This is the step that uses the one-distinct-R-prime hypothesis. It is an exact identity on the source set; it is not asserted for arbitrary prefix integers.

Since A is a distinct subset of the prefix and all increments are nonnegative, equations (4), (7), and (8) imply

    sum_{a in A}(V(a)+U(a)-c)_+
      <=rho_epsilon sum_{b in I}
           [(V(b)-1)_+ + sum_{r in R}D_{1,r}(b)].          (9)

The base hinge has been used only once.

## 6. Target increments use shared capacity without overcounting

For every x>=0 and any finite list z_i>=0,

    (x-1)_+ + sum_i[(x+z_i-1)_+-(x-1)_+]
       <=(x+sum_i z_i-1)_+.                               (10)

If x>=1, this is equality. If x<1, put t=1-x>0. The assertion becomes

    sum_i(z_i-t)_+ <= (sum_i z_i-t)_+.

If no summand is positive it is immediate. Otherwise, summing over the positive terms subtracts t at least once, and adding the remaining z_i can only increase the right side. This proves (10).

Apply (10) at each target with x=V(b) and z_i=u_r(v_r(b)). The bracket in (9) is bounded by (V(b)+U(b)-1)_+. Thus (9) proves (5). This superadditivity of the target increments is precisely what permits arbitrarily many possible R-primes without paying for the core hinge repeatedly.

## 7. Restoring all raw R-prime powers

Pointwise, for c>1,

    (V+U+T-c)_+ <= T+(V+U-c)_+,
    (V+U+T-1)_+  = T+(V+U-1)_+.                           (11)

The second identity holds because T>0 forces at least one u_r to equal one, and hence V+U>=1. Every t_r is a nondecreasing prime-power profile. Consequently

    sum_{a in A}T(a)<=sum_{a<=M}T(a)<=sum_{b in I}T(b),      (12)

by distinctness and the usual count of multiples of each prime power.

Using (5), then (11)--(12),

    sum_{a in A}(X(a)-c)_+
      <=sum_{b in I}T(b)
          +rho_epsilon sum_{b in I}(V(b)+U(b)-1)_+
      <=sum_{b in I}(X(b)-1)_+.

This proves the theorem with the full raw loads, including arbitrary powers of the single R-prime in a source and arbitrary nonnegative R-weights.

## 8. A stronger contraction on the minimal-obstruction source class

If every source has at most one R-prime occurrence, counting multiplicity, and all R-weights are at most one, then T(a)=0 at every source. In the low-core-mean case the preceding argument gives the strict estimate

    sum_{a in A}(X(a)-2-epsilon)_+
       <=rho_epsilon sum_{b in I}(X(b)-1)_+.               (13)

Indeed the source capped and raw loads agree, so (5) applies directly; restoring target tails can only increase its right side.

In particular, on the minimal-obstruction structural class described in the continuation task, every dual vector with all E-core weights at most eta_epsilon has objective at most (2+epsilon)n. This conclusion is independent of the number or sizes of the R-primes and of their reciprocal mass.

A dual witness exceeding (2+epsilon)n must therefore have at least one substantial weight in the E-core itself. Large weights supported only on the light-prime band R cannot cause the remaining obstruction.

## 9. One substantial core coordinate can also be included

### The stronger theorem

For every epsilon>0 there exists eta_epsilon^*>0 such that (1) remains true if one core prime q has an arbitrary nonnegative weight, while every other E-core weight is at most eta_epsilon^*. The R-weights are still arbitrary nonnegative numbers, and every source is still allowed an arbitrary power of at most one distinct R-prime. The sets E and R are disjoint, so q is not in R.

This extension concerns a substantial coordinate **inside the core**, in addition to the arbitrarily many possible substantial coordinates in R. It is not merely the previously known one-exception theorem on the full support.

### 9.1 Conditional diffuse level comparison

Write

    V_0(n)=sum_{p in E\{q}}w_p v_p(n),
    C(n)=V_0(n)+w_q v_q(n),
    ell=1+epsilon.

Remove light primes greater than M before computing mu_0; restoring them only increases the target load. Choose eta_epsilon^* small enough that eta_epsilon^*<=epsilon^2/128 and the audited conditional diffuse level comparison with the excluded prime set {q} applies whenever

    mu_0=sum_{p in E\{q}}w_p/(p-1)<=1+epsilon/2.

The choice is uniform in the actual prime q. Explicitly, it is enough to use the k=1 case of the conditional theorem in
`ep708_synthesis_20261123/analytic/FIXED_HEAVY_CORE.md`:

    #{a<=T: gcd(a,q)=1, V_0(a)>s+ell}
       <=#{b in J: gcd(b,q)=1, V_0(b)>s}                   (14)

for every real interval length T>0, every shift J, and every s>=0. Its parameter condition is

    (1+e_1(kappa))mu_0+eta 2^(2-j)
        <=(ell-eta)(1-e_1(r)),
    r=floor(ell/eta)>=16, j=floor(r/2), kappa=r-j,

which holds uniformly at mu_0<=1+epsilon/2 for sufficiently small eta. This follows because e_1(t)->0 and the limiting sides are 1+epsilon/2 and 1+epsilon.

### 9.2 Exact q-parts remove all negative-level errors jointly

Under this low-mean condition, the full core C itself satisfies

    #{a<=T:C(a)>s+ell}<=#{b in J:C(b)>s}                  (15)

for every real length T>0, every shifted interval J of that length, and s>=0.

To prove it, decompose each integer uniquely as q^j t with gcd(t,q)=1. Since V_0(q^j t)=V_0(t), the shifted level for the j-th piece is s-w_q j.

For every j with s-w_q j>=0, apply (14) at real length T/q^j, using the scaled target interval. This compares the source and target contributions at exact q-exponent j.

If w_q=0, all pieces are of this kind. Otherwise the remaining exponents form one suffix

    j>=j_0,      j_0=floor(s/w_q)+1.

For this suffix, the target condition is automatic, since V_0>=0 and s-w_q j<0. The source contribution is at most the number of prefix integers divisible by q^j0, namely floor(T/q^j0). The total target contribution from the whole suffix is exactly the number of multiples of q^j0 in J, which is at least floor(T/q^j0).

Importantly, the target suffix includes exact q-parts q^j>T as well. The comparison is made after summing the suffix, not by assigning a separate inclusion-exclusion error to each exponent. This proves (15) with zero additive error.

The same proof works for any nondecreasing nonnegative q-adic profile in place of w_q j, since the set of exponents where that profile exceeds s is still a suffix.

### 9.3 Gluing the R-remainders

Apply the argument of Sections 4--7 with C in place of V. The only properties it uses are nonnegativity, invariance under multiplication by powers of every r in R, and the uniform level comparison with gap ell. All three hold for C. Equation (15) has coefficient one rather than the strict rho_epsilon, but coefficient one is sufficient for the target superadditivity argument and the final raw-tail comparison.

Thus (1) follows in the low-mu_0 case. In the high-mu_0 case, remove primes greater than M before computing the mean and use the elementary moment estimate for V_0: it yields sum_{a<=M}min(V_0(a),2)>=M. Adding both the q-coordinate and the R-load preserves this inequality, so the automatic H_2 comparison proves the assertion.

This establishes the stronger theorem at every M and every shift. In the minimal-obstruction structural class, any dual witness exceeding (2+epsilon)n must consequently have at least **two** core weights exceeding eta_epsilon^*. Arbitrarily many substantial weights in R, and one arbitrary substantial core coordinate, are insufficient.

## Dependencies and remaining issue

The only inherited ingredients are the fully audited diffuse level comparison, its elementary high-mean alternative, and ordinary prime-power divisibility counts. No separated-support sieve estimate, smooth-number bound, independent integer cover, or additive rounding assumption is used in the gluing step.

For one exception, Section 9 sums the negative-level pieces exactly as a nested chain of prime-power multiples. For several exceptions, the corresponding upper set is not a single chain, so the same zero-error count argument does not apply. The companion controlled-core note resolves that counting step with a finite divisor expansion and an aggregate cap on the whole substantial core. Its shared-hinge error is B_{epsilon,k}(1+|R|), independent of M, with B_{epsilon,k}<=D_epsilon^k. The aggregate raw core tail costs this error once; each remainder prime also pays it at most once. This is o(n) in the stated controlled-core range. The remaining task is to improve that dependence for the much larger cores still allowed by general minimal-obstruction structure.

