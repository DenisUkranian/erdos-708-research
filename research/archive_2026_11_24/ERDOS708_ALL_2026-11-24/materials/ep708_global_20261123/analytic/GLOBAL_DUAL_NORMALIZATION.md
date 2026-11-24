# Global dual normalization at an integer-minimal obstruction

## Status and purpose

The lemmas in this note are proved reductions for the unrestricted problem. They impose no bound on the size of the demand core, no bound on the number of substantial weights, and no prime-size gap.

They do **not** prove the missing coefficient-two estimate. Their purpose is to preserve the original integer-minimal instance and its actual prime demands while removing low-load sources at total weighted cost o(m). The final section states the remaining joint inequality precisely and distinguishes a sufficient normalization from a proof of that inequality.

## 1. Fixed original instance and notation

Fix delta>0, put c=2+3delta, and retain a fixed ambient integer M and a positive M-term interval I. Let A be an inclusion-minimal failing source set:

    m=|A|,
    tau(A,I)>c m,
    tau(B,I)<=c|B| for every proper subset B of A.

The empty subset has covering cost zero. All subsets retain the original interval I and ambient M.

Let P be the set of source primes, r=|P|, and

    D_p(A)=sum_{a in A}v_p(a).

The already established forced-bank argument gives p<c m for every source prime, hence

    r=O_delta(m/log m)=o_delta(m).

The quadratic gate gives M<16m^2. We use no restriction beyond the full minimal-obstruction class.

For the later level budget, retain the original definitions

    K=floor(c(m-1))+1,
    E={p in P:p<=sqrt K} union {p in P:D_p(A)>p},
    R=P\E.

The inherited forced-bank reduction gives |E|=O_delta(sqrt(m/log m)); every source has at most one occurrence from R, and that prime is its unique largest prime. These are necessary properties of the original unrestricted minimal instance, not added hypotheses selecting a smaller class.

Let z=(z_b) be an optimal boxed raw primal solution, 0<=z_b<=1. Let w be an optimal clipped dual vector, 0<=w_p<=1, and define

    X(a)=sum_{p in P}w_p v_p(a),
    H_I(w)=sum_{b in I}(X(b)-1)_+,
    Phi_A(w)=sum_{a in A}X(a)-H_I(w),
    F=L_raw(A,I)=Phi_A(w).

Basic-solution rounding gives tau(A,I)<=F+r. Therefore

    F>c m-r.                                            (1)

No per-deletion rounding error will be summed below.

## 2. All proper subsets control the TOTAL source shortfall

### Lemma 1

For every nonnegative weight vector w, not necessarily optimal,

    sum_{a in A}(c-X(a))_+
       <=(c m-Phi_A(w))_+.                              (2)

In particular, at an optimal clipped vector,

    sum_{a in A}(c-X(a))_+<r.                            (3)

The strict inequality may be weakened to <=r throughout.

### Proof

Let

    S={a in A:X(a)>c}.

If S=A, the left side of (2) is zero, so (2) is immediate. Otherwise S is a proper subset, possibly empty. Keep the SAME target hinge and the SAME weight vector, including coordinates absent from S. Weak duality still gives

    Phi_S(w)=sum_{a in S}X(a)-H_I(w)
       <=L_raw(S,I)<=tau(S,I)<=c|S|.

Coordinates with zero source demand merely make this weak dual objective smaller; no removal or reallocation of the target hinge is required. The same inequality for S empty reads -H_I(w)<=0.

Algebraically,

    Phi_S(w)-c|S|
      =Phi_A(w)-c m+sum_{a in A\S}(c-X(a)).

The last sum is exactly the positive-part shortfall in (2), because X(a)<=c on A\S. Thus the shortfall is at most c m-Phi_A(w). In this case that right side must be nonnegative; if it were negative, proper-subset minimality would already be contradicted. This proves (2), including the empty-set case.

For the optimal vector, combine (2) with (1). If F>c m, (2) forces every source load to exceed c. If F<=c m, the total shortfall is less than r. In both cases (3) follows.

This is a single estimate using the full family of proper subsets. It does not add an O(r) loss for each one-point deletion.

## 3. Retain all but o(m) sources above 2+2delta

Put

    h=c-delta=2+2delta,
    G={a in A:X(a)>h},
    B=A\G,
    W=sum_{a in B}X(a).

Every removed source has c-X(a)>=delta. Therefore Lemma 1 gives

    |B|<=r/delta,
    W<=(c-delta)r/delta=O_delta(r)=o_delta(m),             (4)
    |G|=m-O_delta(r).

All source prime-power demands remain the actual demands of the original A. G is a set used inside the dual calculation, not a replacement of the original minimality hypothesis.

The same-hinge dual value on G satisfies the stronger estimate

    Phi_G(w)>=c|G|-r.                                   (5)

Indeed,

    Phi_G(w)-c|G|
      =F-c m+sum_{a in B}(c-X(a))
      >=F-c m>-r.

If G is proper, minimality also gives Phi_G(w)<=c|G|. If G=A, (5) is unchanged. In particular, the retained instance has a dual value within o(m) of coefficient c, and every retained source has load strictly greater than 2+2delta.

## 4. Exact complementary-slackness decomposition

Let

    H={b in I:X(b)>1},
    T={b in I:X(b)=1}.

Complementary slackness gives:

    z_b=1 for b in H,
    z_b=0 for X(b)<1,
    sum_{b in I}z_b v_p(b)=D_p(A) whenever w_p>0.          (6)

Consequently

    sum_{a in A}X(a)
      =sum_{b in H}X(b)+sum_{b in T}z_b,
    F=|H|+sum_{b in T}z_b.                              (7)

These formulas retain all raw prime powers.

A vertex has at most r fractional coordinates. This does NOT imply that the entire threshold-one mass sum_T z_b is O(r): many such coordinates can equal one.

For an exact counterexample to that inference, take

    A={2,4,...,2m}, M=2m, I={1,...,2m}, w_2=1.

Every even target must be fully selected to meet the full 2-adic supply demanded by A. There is one active dual weight and no fractional coordinate. For m>=2 the full source-prime count is r=pi(m)=o(m), because the other source primes have zero dual weight. The threshold-one mass is the number of even targets not divisible by four, namely ceil(m/2), which is not O(r). This example only disproves the rounding-to-boundary-mass shortcut; it is not a counterexample to problem 708.

## 5. The retained global bank union is fully saturated

For a retained source a in G and any prime occurrence q dividing a, let

    C_q(a)={b in I:a/q divides b},
    U_G=union_{a in G} union_{q|a} C_q(a).

Every b in C_q(a) has

    X(b)>=X(a/q)=X(a)-w_q
         >h-1=1+2delta.

Hence U_G is a subset of H and z_b=1 at every member of U_G, in the FULL optimal primal solution for A. This does not rely on fractional deletion-cover saturation.

Write

    V_p(U_G)=sum_{b in U_G}v_p(b).

For every active prime w_p>0, equation (6) implies

    V_p(U_G)<=D_p(A).                                   (8)

This controls the global union once, including all overlaps.

### Lemma 2: small weighted excess relative to retained demands

Define

    Xi=sum_{p:w_p>0}w_p (V_p(U_G)-D_p(G))_+.

Then

    Xi<=sum_p w_p(D_p(A)-D_p(G))
       =W
       <=(c-delta)r/delta
       =o_delta(m).                                    (9)

Indeed, by (8), each positive excess over D_p(G) is at most D_p(A)-D_p(G). Multiplication by nonnegative w_p and summation prove the claim. Inactive coordinates have zero weight and cause no change.

Thus exact balance at the original A yields approximate coordinatewise balance at G, with a single total weighted error o(m). There is no multiplier |G| or |R|.

The same saturation argument applies to every divisor d of a source with X(d)>1: every target multiple of d is hot and fully selected. Thus U_G may be enlarged to the union of all such hot-divisor banks for retained sources; inequalities (8)--(9) remain valid for the enlarged union. In particular, prime-deletion banks obtained by deleting a zero-weight source prime are not omitted: their divisors retain the full source load. All target positions are in the original interval I.

### Prime powers are summed before the positive part

If N_S(p^j) denotes the number of members of S divisible by p^j, the exact expression in (9) is

    Xi=sum_p w_p (sum_{j>=1}[N_{U_G}(p^j)-N_G(p^j)])_+.

It is NOT the sum of the positive parts at individual prime-power levels. Both deficits and excesses at different levels of the same prime belong to one valuation row. For the elementary example G={2,4} and U={8}, the differences at 2,4,8 are -1,0,+1; their row total is zero, whereas the sum of their positive parts is one.

Target levels are not truncated at M or at the largest source exponent. A shifted target may contain higher powers, and all of them remain in the actual valuation sum. The example is an algebraic warning about row aggregation, not a claimed minimal obstruction.

## 6. A factorial refinement of every active bank constraint

Fix an active prime p, a source a in G, and q|a. Put

    d=a/q,
    N=floor(M/d).

The entire d-bank is saturated. Rescaling b=d t produces a real interval of length M/d with at least N integer points. Its p-adic valuation is bounded below by ordinary prime-power counts:

    D_p(A)
      >=sum_{b in C_q(a)}v_p(b)
      >=N v_p(d)+sum_{j>=1}floor(N/p^j)
      =N v_p(d)+v_p(N!).                               (10)

Since M/d>=q, N>=q. In particular, whenever p divides a/q and q>=p,

    D_p(A)>=q v_p(a/q)+1>p.                             (11)

The extra one follows from v_p(N!)>=1. This comparison does not need a product threshold pq>=K. For active coordinates with D_p(A)<=p, each occurrence in a retained source is therefore unique and is that source's unique largest prime. The remaining active heavy-demand core can still be large; (10)--(11) do not close its joint contribution.

## 7. Why a quadratic number-of-levels error is not immediate

For the original demand core E, let

    J_E=sum_{p in E}max_{a in A}v_p(a).

In the subquadratic range, J_E=O_delta(sqrt(m/log m)). To see this, split p<=m^(1/4), whose contribution is O(m^(1/4)) using the prime-count bound and log M=O(log m). Every larger prime has at most nine possible source levels for large m, so the remaining contribution is at most 9|E|.

Hence an actually joint error

    O_delta(J_E^2+|R|)

would be o(m). No such error estimate is proved here.

In particular, it cannot be obtained merely by taking absolute values in the finite divisor expansion of a capped upper set. With k unit-weight coordinates and only their first levels, the function

    f_s=1[at least one coordinate present],  0<=s<1,

has exact Boolean/divisor coefficient

    (-1)^(|S|+1)

on EVERY nonempty subset S of the k coordinates. Its coefficient L1 norm is 2^k-1, although the number of levels is J=k. This is an exact obstruction to that algebraic shortcut. It does not refute a quadratic bound exploiting the actual demands, cancellations, or the single shared target hinge in a minimal obstruction.

## 8. The exact remaining joint inequality

Set t=2+delta. All sources of G have X(a)>2+2delta>t. Therefore

    sum_{a in G}(X(a)-t)_+=sum_{a in G}X(a)-t|G|.

A sufficient missing estimate, restricted to the normalized optimal data above, is

    sum_{a in G}(X(a)-2-delta)_+
       <=H_I(w)+C_delta Xi+o_delta(m),                  (12)

uniformly in the original M,I,A and their full prime-power arithmetic. The error Xi is already o(m) by (9). This estimate counts the target hinge once.

If (12) were proved, it would give Phi_G(w)<=(2+delta)|G|+o(m), and (4) would imply

    F=Phi_G(w)+W<=(2+delta)m+o_delta(m).

This is the requested raw bound on the original integer-minimal class. It also contradicts (5), with a fixed gap 2delta|G|-o(m).

Even the weaker inequality obtained by adding delta|G| to the right side of (12) would contradict (5), leaving a gap delta|G|-o(m). It would therefore suffice to exclude the original budget (2+3delta)m, although it would not be the literal stronger raw estimate at the same delta.

Equation (12) is a meaningful normalization of the remaining obligation: it is required only for optimal vectors whose retained sources are all hot and whose global bank union has the approximate active-demand balance (9). It is not established by these reductions. On G there is no low-load credit, so without a new arithmetic estimate it remains the substantive missing inequality.

An optional stronger route is a quantitative weighted expansion

    sum_p w_p(V_p(U_G)-D_p(G))>=gamma_delta |G|

for some gamma_delta>0 under the actual normalized hypotheses. This would contradict (9) directly. It is only a proposed sufficient lemma; no universal weighted expansion theorem is claimed.

Alternatively, since U_G is hot, retaining just its hinge gives the sufficient bank-residual inequality

    |U_G|+sum_p w_p(D_p(G)-V_p(U_G))
       <=(2+delta)|G|+o_delta(m).

Replacing the signed residual COORDINATEWISE gives

    |U_G|+sum_p w_p(D_p(G)-V_p(U_G))_+.

This expression exceeds the signed one by exactly Xi=o(m). This is the sum of the coordinatewise positive parts, not the positive part of their total weighted sum. The formulation preserves overlap and full valuations, but is not proved here.

## 9. Low-load credit: the weaker exact identity

For any source set and any weights, define

    Delta_t(A,I,w)=sum_{a in A}(X(a)-t)_+-H_I(w).

Then the identity

    Delta_t(A,I,w)-sum_{a in A}(t-X(a))_+
       =Phi_A(w)-t|A|                                  (13)

holds exactly. Thus an all-vector bound on Delta_t is stronger than the raw dual bound whenever a substantial low-load credit is present.

For an optimal vector at the present integer-minimal obstruction, Lemma 1 shows that this credit is at most r whenever t<=c. It is already o(m). The normalization therefore removes a real distinction between hinge and raw objectives on the relevant optimal data, while avoiding a claim about all weight vectors.

## Conclusion of this attempt

The global low-load normalization, saturation and weighted-excess estimates (2)--(11) are proved. They preserve the original demands and yield the exact missing obligation (12). Neither (12), its linear-slack variant, nor the proposed weighted bank expansion has been proved in this note. No restricted source class is offered as a replacement for the global target.
