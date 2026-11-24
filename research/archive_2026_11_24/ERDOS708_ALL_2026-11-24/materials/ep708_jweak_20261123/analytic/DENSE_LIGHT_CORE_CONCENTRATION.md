# Concentrating the diffuse core in a dense minimal obstruction

## Status

This note gives a uniform, rigorous reduction in the previously untreated dense regime m/M>=rho_0>0. It does not prove J_weak. In particular, replacing the light core by a constant leaves a genuinely arithmetic heavy-profile inequality, recorded explicitly below.

We use the original raw LP and its original minimal-obstruction source structure. No new source factorization hypothesis is imposed.

## 1. A finite second-moment lemma for capped profiles

Let E be a finite set of k primes. For p in E let u_p(j), j>=0, be a nondecreasing profile with u_p(0)=0 and 0<=u_p(j)<=1. Put

    V(n)=sum_{p in E} u_p(v_p(n)).

Let G_p be independent geometric variables with

    Pr(G_p=j)=(1-1/p)p^(-j), j>=0,
    v=sum_p E[u_p(G_p)],
    sigma^2=sum_p Var(u_p(G_p)).

For every positive interval J of M consecutive integers,

    |M^(-1)sum_J V-v| <= k/M,
    |M^(-1)sum_J V^2-(v^2+sigma^2)| <= k^2/M,              (1)

and consequently

    M^(-1)sum_J (V-v)^2
       <=sigma^2+(k^2+2vk)/M.                             (2)

The same estimates hold for J={1,...,M}, uniformly in the other interval's shift.

**Proof.** Write alpha_{p,j}=u_p(j)-u_p(j-1)>=0. For each p, sum_j alpha_{p,j}<=1. The expansion

    u_p(v_p(n))=sum_{j>=1}alpha_{p,j}1[p^j|n]

has total coefficient mass at most one. Replacing each interval divisibility count by M/p^j has error at most one, even when p^j>M. The expansion of u_p(v_p(n))^2 also has nonnegative increments with total mass at most one. For p!=q, the product profile has nonnegative coefficients of total mass at most one at the moduli p^i q^j. The k diagonal terms and 2 binom(k,2) cross terms therefore give error at most k^2 in the unnormalized second moment. Infinite expansions follow by monotone convergence. This proves (1), and (2) follows by expanding the square.

For the particular capped raw profiles

    u_p(j)=min(w_p j,1),       0<=w_p<=eta,
    mu_E=sum_{p in E}w_p/(p-1),

we have v<=mu_E and

    sigma^2 <= sum_p w_p^2 p/(p-1)^2 <=2 eta mu_E.          (3)

Indeed, for independent copies G_p,G'_p, the cap is 1-Lipschitz, so

    Var(min(w_p G_p,1))
      = E[(min(w_p G_p,1)-min(w_p G'_p,1))^2]/2
      <=w_p^2 Var(G_p).

The geometric variance is p/(p-1)^2, and p/(p-1)<=2.

## 2. Applying the lemma to the actual demand core

Fix c>2 and an original fixed-ambient **integer-minimal** obstruction A subset [2,M], m=|A|: its integer cover cost is greater than cm, while every proper source subset has integer cost at most c times its cardinality in the same interval. Let w be optimal clipped raw dual weights. If r is the number of source-prime rows, the established rounding estimate gives F>cm-r, with r=o(m). Use the already proved original core

    K=floor(c(m-1))+1,
    E={p<=sqrt K} union {p:D_p(A)>p},
    R=P\E.

We retain the established bounds

    |E|=O_c(sqrt(m/log m)),
    each source has at most one occurrence of a prime in R,
    M<16m^2.

Assume now m/M>=rho_0>0. Since m<=M, M and m are comparable, and

    k^2/M=O_{c,rho_0}(1/log M)=o(1).                       (4)

The earlier global large-mean exclusion also bounds the raw weighted mean by an absolute constant at any asymptotically relevant failing dual vector. It is enough here to use the weaker bound

    mu_w=sum_p w_p/(p-1)<=2                               (5)

for all sufficiently large M. Alternatively, all the following estimates remain valid with mu_w displayed, without using (5).

Let E_light={p in E:w_p<=eta}, and apply Section 1 to

    V(n)=sum_{p in E_light}min(w_p v_p(n),1).

Its model mean is denoted by v. Equations (2)--(5) give, both on the prefix and on I,

    M^(-1)sum (V-v)^2 <= 4 eta+o_{c,rho_0}(1).             (6)

The error is uniform in the actual source set, all weights, and the interval shift.

## 3. Raw tails and the one-occurrence remainder

The cap is handled before concentration. Write

    T(n)=sum_{p in E_light}(w_p v_p(n)-1)_+.

Let X'=X-T. If T(n)>0, at least one of the retained capped profiles equals one. Hence X'(n)>=1 and the exact identity

    (X(n)-1)_+=T(n)+(X'(n)-1)_+

holds. Every summand of T is a nondecreasing prime-adic profile. Counting prime-power multiples gives

    sum_{a in A}T(a)<=sum_{a<=M}T(a)<=sum_{b in I}T(b).

Therefore the original dual objective is at most the capped-core objective:

    Phi_A(X)<=Phi_A(X').                                  (7)

Next remove the raw coordinates p in R with w_p<=eta. The original source structure implies that their total contribution to any source is at most eta. Removing them can only decrease the target hinge. Thus, if Y denotes the load from all remaining coordinates, excluding V,

    Phi_A(X)<=Phi_A(V+Y)+eta m.                            (8)

The load Y has nonnegative prime-adic increments and retains all powers of the remaining raw coordinates. No target valuation is truncated without the preceding exact tail argument.

## 4. Replacing the light core by its model mean

The hinge is 1-Lipschitz. Cauchy--Schwarz, using A subset [1,M], gives

    Phi_A(V+Y)
      <= Phi_A(v+Y)
          +sum_{a in A}|V(a)-v|+sum_{b in I}|V(b)-v|
      <= Phi_A(v+Y)
          +(sqrt(m/M)+1)M sqrt(4eta+o(1)).                 (9)

Combining (8)--(9),

    F<=Phi_A(v+Y)+eta m+O_{c,rho_0}(M sqrt eta)+o(M).       (10)

Consequently, for any prescribed xi>0, eta can be fixed sufficiently small in terms of xi and rho_0 so that the total error in (10) is at most xi m for all sufficiently large M. This use of a fixed positive lower bound on m/M is essential.

## 5. An affine exclusion and a strict light-mean deficit

The nonnegative profile increments of Y imply

    sum_I Y>=sum_{a<=M}Y(a)>=sum_{a in A}Y(a).              (11)

If v>=1, the target hinge is everywhere linear and

    Phi_A(v+Y)<=mv-M(v-1)<=m.                              (12)

If 0<=v<=1, put t=1-v. The affine bound (Y-t)_+>=Y-t and (11) give

    Phi_A(v+Y)<=m+(M-m)t.                                 (13)

In particular, whenever t<=rho/(1-rho), where rho=m/M<1, the right side is at most 2m. Thus the dense branch is already excluded when the light mean is sufficiently near or above one, allowing for the small error in (10).

More quantitatively, fix 0<xi<c-1. If the error in (10) is at most xi m, then F>cm-r implies, for all sufficiently large m,

    v<1,
    1-v >= (c-1-xi-r/m)rho/(1-rho).                        (14)

up to replacing a strict inequality by a harmless weak one. Therefore the light-core model mean in any remaining dense obstruction is bounded away from one by a positive amount depending on c, rho_0, and xi.

If a separately raw-minimal obstruction is being used and the same structural core bounds have been established for it, the corresponding assertion has r=0. The distinction is not needed for the original integer-minimal application above.

## 6. The exact heavy-profile inequality still needed

For the remaining case t=1-v>0, the coordinates still present in Y may also be capped at height one. Write Y_bar for that capped load. Its removed tails have prefix sums at most interval sums; wherever a removed tail is positive, Y_bar>=1, and hence v+Y_bar>=1. Thus the same exact tail argument gives Phi_A(v+Y)<=Phi_A(v+Y_bar). For the latter objective,

    Phi_A(v+Y_bar)
       = sum_{a in A}Y_bar(a)+m(1-t)
          -sum_{b in I}(Y_bar(b)-t)_+.

Thus a sufficient next inequality is

    sum_{a in A}Y_bar(a)-sum_{b in I}(Y_bar(b)-t)_+
       <=(1+t+o(1))m,                                    (15)

uniformly on the actual retained source structure. Here t is bounded below by (14); the retained coordinates have original raw weights greater than eta, and each profile in Y_bar has height at most one.

Equation (15) has **not** been proved. The second moments in Section 1 justify replacing the small-weight core by a constant. They do not justify replacing the substantial coordinates by their means, nor do they by themselves control a hinge from its first two moments. In particular, the uniform o(M) two-threshold comparison for the full core remains open in this argument.

This note therefore gives a genuine dense-branch reduction and an excluded subregime, not a proof that every obstruction must be sparse.
