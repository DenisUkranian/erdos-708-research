# A same-threshold comparison for the low substantial-weight block

## Status and scope

This note proves a finite signed-certificate estimate. Combined with the enlarged Bonferroni cutoff, it gives an o(m) same-threshold hinge error for the low substantial-weight block of an actual sparse obstruction.

It does not assert an O(k^2) error for arbitrary substantial support. It does not compare the combined low, high, and diffuse blocks, and it does not prove J_weak.

## 1. Finite statement

Let P be a finite set of k primes, let eta<=w_p<=1 for p in P, and put

    X_P(n)=sum_{p in P}w_p v_p(n),
    mu_P=sum_{p in P}1/p.

Let s be an integer at least 2 such that ceil(1/eta)<=s. There is an explicit constant C_s, independent of the primes, their weights, M, and the shift x, such that every interval I={x+1,...,x+M}, x>=0, satisfies

    sum_{n<=M}(X_P(n)-1)_+
      -sum_{b in I}(X_P(b)-1)_+
       <= C_s [M mu_P^{s+1}+k^s+k^{s+1}].                 (1)

For k=0 both sides vanish. No hypothesis concerning an optimum or a source set is used in this finite inequality.

## 2. Cap each prime profile, retaining its full raw tail

Write

    y_p(n)=min(w_p v_p(n),1),
    Y(n)=sum_{p in P}y_p(n),
    T(n)=X_P(n)-Y(n),
    nu(n)=#{p in P:p|n}.

Whenever T(n)>0, at least one y_p(n) equals one. Hence

    (X_P(n)-1)_+=(Y(n)-1)_++T(n).                         (2)

The function T is a sum of nonnegative prime-power indicators, so

    sum_{b in I}T(b)>=sum_{n<=M}T(n).                     (3)

Thus it suffices to bound the capped hinge discrepancy. Equations (2)--(3) keep all target prime powers; they do not truncate a raw target exponent at a source level.

Each y_p has J_p=ceil(1/w_p)<=s nonzero exponent levels before becoming constant at one.

## 3. A finite-degree certificate

For a nonempty prime subset S define the presence-Mobius coefficient

    c_S(n)=sum_{R subset S}(-1)^{|S|-|R|}
                  (sum_{p in R}y_p(n)-1)_+.

It vanishes if any prime in S does not divide n. The exact Boolean inversion identity is

    (Y(n)-1)_+=sum_{nonempty S subset P}c_S(n).            (4)

For |S|=j, each summand has absolute value at most j, and therefore

    |c_S(n)|<=j*2^j.                                     (5)

Put

    T_s(n)=sum_{1<=|S|<=s}c_S(n),
    A_s=sum_{j=1}^s j*2^j*binom(s+1,j),
    B_s=s+1+2A_s,
    K(n)=T_s(n)-A_s*binom(nu(n),s+1).                    (6)

If nu(n)<=s, (4) gives K(n)=(Y(n)-1)_+. If nu>=s+1, then, for every j<=s,

    binom(nu,j)<=binom(s+1,j)*binom(nu,s+1).

Using (5),

    |T_s(n)|<=A_s*binom(nu(n),s+1).

Thus K(n)<=0<=(Y(n)-1)_+ in this case. Moreover nu<=(s+1)binom(nu,s+1), so in all cases

    0<=(Y(n)-1)_+-K(n)<=B_s*binom(nu(n),s+1).             (7)

The constant A_s may also be written

    A_s=(s+1)[2*3^s-2^{s+1}].

The nonnegative prefix error in (7) has sum at most

    B_s M e_{s+1}((1/p)_{p in P})
      <=[B_s/(s+1)!] M mu_P^{s+1}.                       (8)

## 4. Total variation of the divisor expansion

For a fixed S of size j, each exponent coordinate of c_S is constant beyond J_p and vanishes at exponent zero. Finite successive differences therefore give an exact expansion

    c_S(n)=sum_{1<=e_p<=J_p, p in S}
             beta_{S,e} 1_{prod_{p in S}p^{e_p}|n}.

There are at most s^j exponent tuples. Each coefficient is a sum of 2^j signed values of c_S, so (5) implies

    sum_e |beta_{S,e}|<=j*(4s)^j.                         (9)

The correction term in (6) is a sum of squarefree divisibility indicators. Consequently K has a signed divisor expansion whose coefficient absolute sum is at most

    V_s(k)=sum_{j=1}^s j*(4s)^j*binom(k,j)
                +A_s*binom(k,s+1)
           <=C'_s(k^s+k^{s+1}).                         (10)

For every positive divisor d, its interval count differs from its prefix count by zero or one. Thus, regardless of the signs in K,

    sum_{n<=M}K(n)-sum_{b in I}K(b)<=V_s(k).              (11)

Combining (7)--(11), then restoring the raw tails by (2)--(3), proves (1). The argument uses actual divisor counts at every modulus, including moduli larger than M.

## 5. The actual sparse-obstruction scale

Fix eta and take s=floor(1/eta)+1. Let

    y=M^{1/(s+1)},
    P={p<=y:w_p>=eta}.

The independently proved Bonferroni absorption and shell bootstrap give, along every actual sparse-obstruction sequence,

    mu_P=O_{c,eta}(rho^{1/s}),  rho=m/M->0.               (12)

Because every prime in P is at most y,

    k<=y*mu_P,
    k^{s+1}<=M mu_P^{s+1},
    k^s<=M^{s/(s+1)}mu_P^s
         =O_{c,eta}(m M^{-1/(s+1)}).                     (13)

Also M mu_P^{s+1}=O_{c,eta}(m rho^{1/s}). Substitution into (1) yields the uniform estimate

    sum_{n<=M}(X_P(n)-1)_+
      <=sum_{b in I}(X_P(b)-1)_+
          +O_{c,eta}(m[rho^{1/s}+M^{-1/(s+1)}])
      =sum_{b in I}(X_P(b)-1)_++o(m).                     (14)

This is a bound at the actual m scale. The corresponding generic estimate (1) can be much larger than k^2, so it is fully consistent with the verified quartic same-threshold counterexample.

## 6. What remains unproved

Equation (14) compares only one low substantial-weight block at threshold one. It does not assert that a hinge for a sum of blocks equals the sum of their hinges. The targets supporting the low block may also be needed by the diffuse and high-prime blocks.

Therefore any use of (14) in J_weak still requires a joint allocation or an exact decomposition that charges the target hinge once. No such general decomposition is proved in this note.

## 7. A valid joint reduction by an aggregate cap

There is nevertheless one useful exact reduction that keeps the target hinge joint. Let U=X_P be the raw low substantial-prime load, let V be any nonnegative remaining load, and put

    alpha(n)=min(U(n),1),  T(n)=(U(n)-1)_+.

Pointwise,

    (U+V-1)_+=(alpha+V-1)_++T.                            (15)

Indeed T>0 forces alpha=1, and otherwise T=0. For any source subset A of the prefix, define the auxiliary hinge functional

    Phi_A[W]=sum_{a in A}W(a)-sum_{b in I}(W(b)-1)_+.

Then (15) gives

    Phi_A[U+V]
      =Phi_A[alpha+V]+sum_A T-sum_I T
      <=Phi_A[alpha+V]+sum_{n<=M}T(n)-sum_I T.             (16)

At the actual sparse-obstruction scale, (14) bounds the final difference by o(m). Thus

    Phi_A[U+V]<=Phi_A[alpha+V]+o(m).                       (17)

The entire low substantial block has been replaced by one bounded composite coordinate alpha in [0,1]. Since s*eta>1, alpha is determined exactly by the truncated state vector (min(v_p(n),s))_{p in P}. Equation (17) spends the raw low tail once, using an exact identity in the full joint hinge. It does not add independently chosen covers.

The new load alpha+V is generally not a raw linear prime-price vector. The remaining raw prime rows retain their old equalities, and every new hot target was already hot, but there is no automatic tight composite-alpha row. Proper-subset minimality for the original raw LP cannot simply be reapplied to this auxiliary functional.

Finally, unconditional state total variation does not control every correlation between alpha and the high-prime or diffuse loads. Bounding Phi_A[alpha+V] at the desired coefficient still requires a new joint argument.
