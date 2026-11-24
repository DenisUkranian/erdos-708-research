# Controlled substantial core weights and a one-prime remainder

## Status

This note proves a joint source-specific hinge estimate with an error exponential in the number of substantial core coordinates and linear in the number of possible remainder primes, but independent of the ambient length. The complete proof, including the aggregate-core-cap strengthening, has passed a separate internal mathematical audit. This is not external peer review or a solution of the unrestricted conjecture.

The key improvement is to cap the **whole substantial core** at one. This removes the earlier base error exp(O(k log k)). Restoring its aggregate raw tail costs a single exponential error. Every remainder prime pays the level error only once, regardless of its exponent range.

## 1. The theorem

For every epsilon>0 there is c_epsilon>0 such that the following holds for every integer k>=0. Put

    eta=c_epsilon/(k+1).

Let E and R be disjoint finite prime sets. All but at most k weights in E are at most eta. The other E-weights and all R-weights may be arbitrary nonnegative numbers. Define

    X(n)=sum_{p in E union R}w_p v_p(n).

Let A be a set of distinct integers in [2,M], each divisible by at most one distinct prime from R. Arbitrary powers of that prime and arbitrary unweighted cofactors are allowed. For every positive M-term interval I,

    sum_{a in A}(X(a)-2-epsilon)_+
       -sum_{b in I}(X(b)-1)_+
          <=B_{epsilon,k}(1+|R|),                         (1)

where

    B_{epsilon,k}=4^k binom(k+floor(1/eta),k)  for k>=1,
    B_{epsilon,0}=0.                                     (2)

More precisely, the right side can be replaced by

    B_{epsilon,k}+sum_{r in R}min(B_{epsilon,k},m_r),
    m_r=#{a in A:r divides a}.                           (3)

In particular,

    B_{epsilon,k}<=D_epsilon^k,
    D_epsilon=4e(1+2/c_epsilon),                          (4)

for k>=1. All estimates are uniform in M, prime values, weights, source sets and shifts. R may be restricted to the primes actually appearing in the sources. In the older notation A_{epsilon,k}+B_{epsilon,k}|R|, one may now take A_{epsilon,k}=B_{epsilon,k}.

## 2. Inherited conditional comparison and the mean split

It suffices to treat 0<epsilon<=1. Let

    F={p in E:w_p>eta},   L=E\F,   |F|<=k,
    V(n)=sum_{p in L}w_p v_p(n),
    mu_L=sum_{p in L}w_p/(p-1),
    ell=1+epsilon,   c=2+epsilon.

Discard light primes greater than M before computing mu_L; restoring them later only increases the target hinge.

The inherited conditional diffuse comparison states that, for real T>0, any positive interval J of length T, and s>=0,

    #{a<=T:gcd(a,product F)=1,V(a)>s+ell}
       <=#{b in J:gcd(b,product F)=1,V(b)>s},              (5)

provided

    (1+e_k(kappa))mu_L+eta 2^(k+1-j)
       <=(ell-eta)(1-e_k(r)),
    r=floor(ell/eta)>=16, j=floor(r/2), kappa=r-j,

where

    e_k(t)=3^k e(t/2)+3*4^k 2^(1-t/2),
    e(u)=C[(u/2)^(-u/4)+2^(1-u/2)].

Its full proof is in the preceding synthesis, including arbitrary sizes of the excluded primes and real interval lengths. For u>=16,

    e_k(u)<=3C 3^k 2^(-u/4)+6*4^k 2^(-u/2).

Choose R_epsilon>=16 so that
3C 2^(-R_epsilon/4)+6*2^(-R_epsilon/2)<=epsilon/16.
It suffices to choose

    c_epsilon<=epsilon^2/128,
    (1+epsilon)/c_epsilon>=max(32,2R_epsilon+2).

Then r>=32k+2R_epsilon, kappa>=16k+R_epsilon and j>=k+1. At mu_L<=1+epsilon/2 the parameter inequality has margin at least

    46epsilon/128-191epsilon^2/2048>0.

Thus (5) holds uniformly at every smaller length whenever mu_L<=1+epsilon/2.

If instead mu_L>=1+epsilon/2, the inherited elementary prefix moments give

    sum_{a<=M}min(V(a),2)>=M.

Adding all other nonnegative coordinates preserves this condition. Ordinary prime-power counts then imply

    sum_{a<=M}(X(a)-2)_+
       -sum_{b in I}(X(b)-1)_+
          <=M-sum_{a<=M}min(X(a),2)<=0.

This proves (1) with zero error. Henceforth assume the low-mean case.

## 3. A two-sided finite-divisor variation bound

For the moment cap each exceptional coordinate individually:

    Z_ind(n)=sum_{q in F}min(w_q v_q(n),1),
    f_s(n)=1[Z_ind(n)>s], s>=0.

For every real T>0 and interval J of length T,

    |sum_{a<=T}f_s(a)-sum_{b in J}f_s(b)|
       <=4^k binom(k+floor(s/eta),k).                     (6)

If F is empty or s>=k, the function is identically zero.

Write F={q_1,...,q_f}, f<=k, and b_i=ceil(1/w_qi). Let
u_i(j)=min(w_qi j,1), g_s(j)=1[sum_i u_i(j_i)>s].
Its divisor coefficients are

    a_j(s)=sum_{e_i in {0,1}, e_i<=j_i}
                (-1)^(sum e_i) g_s(j-e).                 (7)

Subtract one only in positive coordinates. Coordinatewise telescoping gives

    f_s(n)=sum_{j:prod_i q_i^ji divides n}a_j(s).

If some j_i>b_i, adjacent saturated layers coincide, so a_j=0. Each coefficient has absolute value at most 2^f. For a nonzero index put z_i=(j_i-1)_+. If sum_i u_i(z_i)>s, all corners in (7) equal one and cancel. The zero index also has coefficient zero because s>=0.

On the remaining grid j_i<=b_i, one has z_i<b_i and u_i(z_i)=w_qi z_i>=eta z_i. A nonzero coefficient therefore requires sum_i z_i<=s/eta. There are binom(f+floor(s/eta),f) such z-vectors. Every zero z_i permits j_i=0 or1, while a positive z_i determines j_i. Thus

    sum_j |a_j(s)|
       <=4^f binom(f+floor(s/eta),f)
       <=4^k binom(k+floor(s/eta),k).                     (8)

For any divisor d, its prefix count is floor(T/d) and its interval count is that number or one more. Hence its discrepancy has absolute value at most one. Applying the triangle inequality to the finite expansion proves (6) in both signs.

## 4. Cap the whole substantial core at one

Now use the aggregate cap

    X_F(n)=sum_{q in F}w_q v_q(n),
    Z(n)=min(X_F(n),1),
    T_F(n)=X_F(n)-Z(n),
    C(n)=V(n)+Z(n).

For 0<=s<1,

    1[Z(n)>s]=1[X_F(n)>s]=1[Z_ind(n)>s].                 (9)

For s>=1 the first upper set is empty. Thus (6) implies

    |sum_{a<=T}1[Z(a)>s]-sum_{b in J}1[Z(b)>s]|
       <=B_{epsilon,k}   (0<=s<1),                       (10)

and the difference is zero for s>=1. Integrating from0 to1 gives

    |sum_{a<=T}Z(a)-sum_{b in J}Z(b)|
       <=B_{epsilon,k}.                                 (11)

The aggregate cap is nonlinear, but exact F-part conditioning still applies. Decompose n=h t with h the full F-smooth part and gcd(t,product F)=1. Then C(n)=Z(h)+V(t). For Z(h)<=s, apply (5) at length T/h and level s-Z(h)>=0. For Z(h)>s, the target condition is automatic and the source count is bounded by the unrestricted prefix count of that exact part.

Sum all negative-level pieces before estimating them, including all target h>T. This gives

    #{a<=T:C(a)>s+ell}-#{b in J:C(b)>s}
       <=sum_{a<=T}1[Z(a)>s]-sum_{b in J}1[Z(b)>s].       (12)

For 0<=s<=1 the defect is at most B_{epsilon,k}. For s>=1 it is nonpositive. Integrating (12) over s>=1 therefore gives the exact base comparison

    sum_{a<=M}(C(a)-c)_+
       <=sum_{b in I}(C(b)-1)_+.                        (13)

There is no base error depending on k.

## 5. The remainder increment error is paid once per prime

For r in R put

    u_r(e)=min(w_r e,1),  t_r(e)=(w_r e-1)_+,
    U(n)=sum_R u_r(v_r(n)),
    T_R(n)=sum_R t_r(v_r(n)).

For h=c or1 define

    D_{h,r}(n)=(C(n)+u_r(v_r(n))-h)_+-(C(n)-h)_+.

The exact increment identity is

    D_{h,r}(n)=sum_{j>=1}1[r^j divides n]
        integral_{u_r(j-1)}^{u_r(j)}1[C(n)>h-v] dv.       (14)

The core C is invariant under multiplication by r-powers. For fixed j, divide source and target r^j-multiples by r^j. The source quotient is a prefix of length N=floor(M/r^j); the target quotient contains at least N consecutive positions. Apply (12) on an N-term target subinterval at s=1-v in[0,1]; when N=0 the source count is zero.

The total integration width across all j is at most one. Consequently

    sum_{a<=M}D_{c,r}(a)
       <=sum_{b in I}D_{1,r}(b)+B_{epsilon,k}.            (15)

At each source, at most one R-coordinate is present. Hence

    (C(a)+U(a)-c)_+
       =(C(a)-c)_++sum_R D_{c,r}(a).                     (16)

All increments are nonnegative. Apply (13) once and (15) for each r. On targets use, for x,z_i>=0,

    (x-1)_++sum_i[(x+z_i-1)_+-(x-1)_+]
       <=(x+sum_i z_i-1)_+.

For x>=1 this is equality; for x<1 it follows from
sum_i(z_i-t)_+<=(sum_i z_i-t)_+ with t=1-x>0. Therefore

    sum_{a in A}(C(a)+U(a)-c)_+
       <=sum_{b in I}(C(b)+U(b)-1)_++B_{epsilon,k}|R|.   (17)

For the refinement, the actual source increment for r is also at most m_r, since every increment is at most one and vanishes off r-multiples. Combining this with (15) replaces its error B by min(B,m_r).

## 6. Restore the aggregate core tail with one additional error

The aggregate tail T_F is not a sum of independent prime-power profiles. Its prefix dominance is not asserted. Instead, linear raw prime-power dominance and (11) imply

    sum_{a<=M}T_F(a)-sum_{b in I}T_F(b)
       =sum_prefix X_F-sum_I X_F+sum_I Z-sum_prefix Z
       <=B_{epsilon,k}.                                 (18)

Since T_F>=0, restriction to A preserves this upper bound. The remainder tail is still a sum of nondecreasing prime-power profiles, so

    sum_{a in A}T_R(a)<=sum_{b in I}T_R(b).

The full raw load is X=C+U+T_F+T_R. If T_F+T_R>0, either Z=1 or some capped remainder coordinate equals one. Thus C+U>=1, giving the exact target identity

    (X-1)_+=T_F+T_R+(C+U-1)_+.

On sources,

    (X-c)_+<=T_F+T_R+(C+U-c)_+.

Combining these facts with (17)--(18) proves (1) and its refined version (3). All raw prime powers are retained.

## 7. Quantitative consequences and scope

For k>=1, floor(1/eta)<=(k+1)/c_epsilon<=2k/c_epsilon. Applying
binom(N,k)<=(eN/k)^k proves (4).

If |R|<=C n/log n and, for a fixed gamma in(0,1),

    k<=(1-gamma) log log n / log D_epsilon,

then

    B_{epsilon,k}|R|=O(n/(log n)^gamma)=o(n),
    B_{epsilon,k}=O((log n)^(1-gamma))=o(n).

The raw dual objective is at most (2+epsilon)n+o(n). Thus a witness at least (2+2epsilon)n is excluded for sufficiently large n under these conditions. This does not exclude an arbitrarily tiny excess above (2+epsilon)n.

The integer-transfer companion proves that sources with a designated core of size o(log log M), and at most one distinct prime outside that core, satisfy tau<=(2+o(1))n uniformly. No prime-size separation is needed; powers of the outside prime are allowed. Fixed-ambient minimality forces source primes below c m and m>sqrt(M)/4, so both the present defect and LP rounding are o(m). All core weights are unrestricted in this application.

That is the integer consequence of this controlled-weight method. The separate direct construction in SHARED_CORE_POLYLOGARITHMIC.md proves the stronger shared-core source class |E|<=c_0(log M)^2/log log M for an absolute c_0>0. It uses nested outside-prime-power matching, exact core-part bins and a global repair, rather than enlarging the number of substantial coordinates covered by the present uniform fractional estimate.

With R empty, the theorem gives an ambient-independent full-prefix hinge defect at most D_epsilon^k whenever at most k weights are substantial. This improves the earlier polylogarithmic-in-M exceptional-core estimate. The one-core-coordinate theorem in DIFFUSE_CORE_SINGLE_REMAINDER.md gives zero error for k=1 after choosing its light threshold.

The unrestricted demand core can still contain O(sqrt(n/log n)) primes. The exponential dependence on k does not control that entire class. The general asymptotic conjecture remains unproved by this argument.
