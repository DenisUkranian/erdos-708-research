# Optimal coverage, logarithmic conservation, and the log-cap support

## Status

This note develops a global variational route on an actual optimal raw dual. It proves exact coverage and transportation identities and a new finite bound on every coordinate changed by a logarithmic cap. No extra factorization class is assumed.

The remaining coverage-loss estimate is not proved. The final sections state exactly what the variational calculation supplies, what it does not supply, and where products of short threshold-one active parts would have to enter.

## 1. Optimal setup

Let A subset [2,M] consist of m distinct integers, and let I be a positive interval of M consecutive integers. Let w be an optimal clipped raw dual vector and z a paired optimal boxed primal. Write

    P={p:w_p>0},
    X(n)=sum_{p in P}w_p v_p(n),
    H={b in I:X(b)>1},
    T_1={b in I:X(b)=1},
    h=|H|,
    F=Phi_A(w)=sum_{b in I}z_b.

Complementary slackness gives z_b=1 on H, z_b=0 where X(b)<1, and

    sum_{b in I}z_b v_p(b)=D_p(A)    for every p in P.      (1)

Only active rows will be used in weighted equalities. All target valuations are kept in full.

## 2. One coverage functional for every monotone perturbation

For every coordinatewise shrink 0<=u<=w, define X_u(n)=sum_p u_p v_p(n). Then

    Phi_A(u)=sum_{b in I}z_b min(X_u(b),1),                 (2)

and therefore

    F-Phi_A(u)=sum_{b in I}z_b(1-X_u(b))_+.                (3)

**Proof.** Equation (1) gives sum_A X_u=sum_I z_b X_u(b). Whenever X_u(b)>1, the original X(b)>1 and hence z_b=1. Thus the unweighted target hinge equals sum_I z_b(X_u(b)-1)_+. Subtraction proves (2). Every selected target has X(b)>=1, so sum z_b=F and (3) follows.

This formula simultaneously includes all disjoint-band deletion identities. It is a single coverage budget over the fixed measure z, not one target budget for each prime or source.

As a simple consequence, if a random shrink retains each coordinate with expected factor 1-theta, then its expected loss is at most theta F. Indeed, for a selected target with old load x>=1 and new load y in [0,x],

    (1-y)_+ <= 1-y/x.

Taking expectations and summing proves the claim, without any independence assumption. This estimate alone does not permit a drastic sparsification at a small loss: retaining only a small expected fraction gives a correspondingly large upper bound on the loss.

## 3. The exact local directional derivative

Let q be any signed perturbation supported on P, and put Q(b)=sum_p q_p v_p(b). For sufficiently small positive perturbation sizes that preserve coordinate feasibility, the one-sided directional derivative is

    Phi_A'(w;q)
      =-sum_{b in T_1}[(1-z_b)(Q(b))_+ + z_b(-Q(b))_+].    (4)

Indeed, the hot targets contribute Q(b), the cold targets contribute zero, and threshold-one targets contribute (Q(b))_+ to the derivative of the hinge. Equation (1) replaces the source derivative by sum z_b Q(b), giving (4).

Thus the only local curvature comes from target ties. Along a feasible direction preserving every tie load, the objective is affine and locally constant until another target crosses threshold one. A proposed second-variation argument must provide an arithmetic direction or a controlled finite crossing; there is no unexploited strict concavity in the raw LP objective itself.

## 4. Logarithmic transportation and the cold initial segment

For any positive integer n let

    s_P(n)=product_{p in P}p^{v_p(n)}

be its full active-prime part. Equation (1), weighted by log p, gives the exact conservation law

    sum_{b in I}z_b log s_P(b)
      =sum_{a in A}log s_P(a)
      <=m log M.                                         (5)

Assume h+1<M and put

    T=M/(h+1)>1.

Every positive integer d<=T has X(d)<=1. Otherwise all of its at least floor(M/d)>=h+1 interval multiples would lie in H.

Consequently every hot target has s_P(b)>T. Every threshold-one target satisfies s_P(b)>sqrt T: if d=s_P(b) had d^2<=T, then X(d^2)=2, contradicting the cold initial segment. Hence

    h log T+sum_{b in T_1}z_b log s_P(b)<=m log M,          (6)

and in particular

    h<=m log M/log T.                                     (7)

At a minimal raw obstruction F=O_c(m), so h=O_c(m). Along the upper quadratic scale M=m^{2+o(1)}, (7) gives h<=(2+o(1))m. It does not control the additional mass selected at threshold one.

For any lambda>0, logarithmic conservation also gives

    F<=lambda m log M
        +sum_{b:z_b>0}z_b(1-lambda log s_P(b))_+.          (8)

When lambda log T>=1, the error in (8) is supported only on threshold-one targets with small active parts. Thus the logarithmic route isolates a precise boundary deficit; it does not justify discarding it.

## 5. Every coordinate changed by the logarithmic cap has small total harmonic mass

Fix epsilon>0 and put

    a=1/(2+epsilon),
    lambda=(2+epsilon)/log M,
    E_lambda={p in P:w_p>lambda log p}.

Assume M>1 and T>1 as above. For p in E_lambda set

    s_p=floor(1/w_p)+1.

Then s_p w_p>1. The complete interval bank of p^{s_p} is hot and is fully selected. Its contribution to the active p-row gives

    D_p(A)>=s_p floor(M/p^{s_p}).                         (9)

Efficiency and w_p(s_p-1)<=1 imply

    p^{s_p-1}<M^a,
    p<M^a,
    p^{s_p}<M^{2a}.                                      (10)

The cold initial segment gives p^{s_p}>T. Combining with (10),

    p>T/M^a                 for every p in E_lambda.       (11)

Write q_M=M^{2a-1}<1. Since p^{s_p}/M<q_M, the floor in (9) satisfies

    floor(M/p^{s_p})
       >=(1-q_M)M/p^{s_p}.

Also 1/p<M^a/p^{s_p}. Therefore

    1/p <= M^{a-1} D_p(A)/[(1-q_M)s_p].                   (12)

Finally, p^{s_p}>T implies 1/s_p<log p/log T. Summing (12) and using the source logarithmic bound gives the finite inequality

    sum_{p in E_lambda}1/p
      <= [m M^{a-1} log M]/[(1-M^{2a-1})log T].            (13)

No fixed weight threshold is needed: (13) covers all changed coordinates, including weights tending to zero. No independent per-level demand equality is asserted; (9) uses the raw p-row and its saturated hot bank.

At an actual minimal raw obstruction on the upper quadratic scale M=m^{2+o(1)}, equations (11)--(13) yield

    min E_lambda >= M^{1/2-a-o(1)},
    sum_{p in E_lambda}1/p <= M^{a-1/2+o(1)}=o(1).         (14)

If E_lambda is empty, the minimum statement is omitted and the harmonic statement is immediate. These are consequences of a general finite estimate, not a proof restricted to an assumed prime-support class.

For comparison, a weaker form that does not absorb the floor is

    sum_{p in E_lambda}1/p
       <=m M^{a-1}log M/log T+M^{2a-1}.

That weaker form was independently audited before the harmless relative-floor improvement in (13).

## 6. Target regularization is affordable for the coverage loss

Let E be any subset of P such that every source has at most K occurrences from E, counting multiplicity. Summing the exact active rows gives

    sum_{b in I}z_b Omega_E(b)=sum_{a in A}Omega_E(a)<=Km.

Hence, for every L_0>0,

    sum_{b:Omega_E(b)>L_0}z_b<=Km/L_0.                    (15)

This bounds selected mass, not an unweighted count when z_b is fractional. Since the coverage loss at a target is at most z_b, the entire contribution of these targets to any loss in (3) can be discarded at a cost at most Km/L_0.

Likewise logarithmic conservation (5) gives, for every R>0,

    sum_{b:s_P(b)>M^R}z_b<=m/R.                          (16)

For fixed R, the remaining active parts have M^{o(1)} divisors uniformly. An elementary proof is enough: for every xi>0, split prime factors at 2^{1/xi}; for a larger prime, e+1<=2^e<=p^{xi e}, while the finitely many smaller primes contribute a finite constant. Thus tau(n)<=C_xi n^xi, and for n<=M^R one may take xi arbitrarily small after fixing R.

On the upper quadratic scale, (11) bounds the number of E_lambda occurrences in every source by a constant depending only on epsilon. Therefore (15)--(16) permit, within any prescribed small linear coverage-loss budget, restriction to selected targets with a bounded number of log-cap coordinates and M^{o(1)} active divisors.

These truncations do not permit discarding their full hinge contributions: a discarded target can have very large load. They are valid specifically because the variational loss in (3) is bounded by one unit of selected mass per target. A complete charging argument still has to account for carrier banks that meet the discarded targets; no such step is assumed here.

## 7. The unresolved log-cap coverage estimate

Define the monotone cap

    u_p=min(w_p,lambda log p).

Every source then has

    X_u(a)<=lambda log a<=2+epsilon.

There is also a useful lower-load restriction. Let e(n) be the full E_lambda-part of n. If X_u(n)<=lambda log T, then

    lambda log e(n)<=X_u(n)<=lambda log T,

so e(n)<=T and the cold-prefix property gives X(e(n))<=1. The coordinates outside E_lambda were unchanged. It follows that

    X(n)<=1+X_u(n)       whenever X_u(n)<=lambda log T.     (17a)

Thus a source with X(a)>c has X_u(a)>=min(c-1,lambda log T). If lambda log T>=1, every target contributing positively to the cap loss has original load X(b)<2. This locates the unresolved loss at threshold-one and low-hot positions; it does not estimate its total mass.

By (2)--(3), the exact lost objective is

    F-Phi_A(u)=sum_{b in I}z_b(1-X_u(b))_+.                (17)

A sufficiently small bound for (17) would contradict an original failure at a larger coefficient. Equations (11)--(14) show that the coordinates responsible for the loss are arithmetically sparse in a quantitatively strong sense near the quadratic scale. They do not prove that their coverage loss is small.

In particular, a small reciprocal sum cannot be replaced by a small selected demand sum: selection may concentrate on rare prime divisibilities. The exact row equalities only give sum z_b X_E(b)=sum_A X_E(a), which can still be of order m.

There is a second potential route using (8). Threshold-one active parts d have X(d)=1, and the product of any two such parts has raw load two. Their product banks, when the products are at most M, are forced hot and consume the same active-prime supply. A proof would need to charge the total boundary deficit in (8), or the loss in (17), to these overlapping banks with a single target capacity. Summing a separate bank contribution for every pair is not justified.

No such joint charging estimate is established here. The full J_weak inequality remains unproved, including the intermediate and dense scales not resolved by the logarithmic potential.
