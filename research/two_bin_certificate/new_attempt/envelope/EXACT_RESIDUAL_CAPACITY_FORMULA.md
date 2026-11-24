# Exact residual-capacity formula for the source envelope

24 November 2026. This is a general proved formula for the stable source envelope. It does not prove its transfer to an arbitrary interval and does not solve Erdős 708.

## 1. Definitions

For 0<=w_p<=1, let X_w(t)=sum_p w_p v_p(t). The source two-bin kernel is

    F_w(a)=K^w_{h_w(a)}(a),

and the stable source envelope is

    C_w(a)=inf_{0<=v<=w}[F_v(a)+X_w(a)-X_v(a)].

Keep the original target K^w_M. No target regularization is used in the proposed transfer under investigation.

Let P be the primes dividing a with positive original price, and write e_p=v_p(a). For S subset P put

    h_S=product_{p in S}p^{e_p}.

For this fixed support S define a finite linear program R_S(w):

    maximize  sum_{p in S} e_p y_p

    subject to 0<=y_p<=v_p<=w_p for p in S,

    Omega(d) y_p <= Omega(d) v_p - X_v(d)+1

for every p in S and every nonunit divisor d of h_S with p|d and d^2<=h_S p. Here X_v(d)=sum_{q in S}v_q(d) v_q. The repeated symbol v_q(d) in this last display denotes the usual integer valuation, while v_q is the price variable; in implementation these are stored separately. Put R_empty=0.

**Theorem.**

    C_w(a)=X_w(a)-max_{S subset P}R_S(w).             (1)

In particular all of the active-part discontinuity has been replaced by a finite maximum of ordinary linear programs. For rational input prices, the envelope value and some attaining price reduction are rational. The formula includes arbitrary powers and arbitrary numerical prime sizes.

## 2. Removing the minimum-weight cap from one row

Fix a price vector v and an active source h. For a row p, let D_p be its permitted divisors: p|d, d|h, d^2<=hp. This family is closed under removing any prime occurrence other than a designated occurrence of p.

Set

    A_p=max_{d in D_p} (X_v(d)-1)_+/Omega(d),

with a zero maximum when necessary. Then the actual row maximum is exactly

    m_p=min(v_p,A_p).                                (2)

The upper bound follows from r_v(d)<=v_p and r_v(d)<=(X_v(d)-1)_+/Omega(d).

For the reverse bound, assume A_p>0 and choose a maximizing occurrence set E. If some occurrence j other than the designated p has price v_j<A_p, removing it increases the average excess:

    [sum_{i in E\{j}}v_i-1]/(|E|-1)
       - [sum_{i in E}v_i-1]/|E|
       = (A_p-v_j)/(|E|-1)>0.

Eligibility is preserved under removal, contradicting maximality. Thus every other occurrence has price at least A_p. If v_p>=A_p, the root itself has r_v(d)=A_p. If v_p<A_p, its minimum price is v_p and r_v(d)=v_p. This proves (2). Repeated copies of p are handled as separate occurrences; at most the designated one is exempt from removal.

## 3. Fully paid positive coordinates can be deleted

Define total residual capacity

    R(v)=X_v(a)-F_v(a)
        =sum_p e_p (v_p-m_p).

Suppose a positive coordinate p satisfies m_p=v_p. It contributes zero to R(v). Delete that coordinate by setting its price to zero. The active part shrinks and every remaining root family only shrinks; all remaining root prices are unchanged or decrease. Therefore every remaining row maximum weakly decreases and its residual weakly increases. The deleted row has zero residual before and after. Hence deleting the coordinate cannot decrease R(v).

Repeat until either all coordinates have disappeared or every remaining positive coordinate has m_p<v_p. This is a finite deletion process. It does not claim that the original raw dual objective is preserved: this is an optimization of the source envelope at a single integer a.

## 4. Proof of the LP formula

First take an arbitrary price reduction v<=w and perform the deletion process in Section 3. Let S be the resulting support. For each p in S, (2) and m_p<v_p give m_p=A_p. Thus

    y_p=v_p-m_p>0

satisfies 0<=y_p<=v_p<=w_p and, for every eligible d,

    y_p <= v_p - (X_v(d)-1)/Omega(d).

These are precisely the displayed LP constraints. Its objective is the residual after deletion, which is at least R(v). Consequently

    max_S R_S(w) >= sup_{0<=v<=w}R(v).                (3)

Conversely, take any feasible LP vector v,y on S. Its positive-price support may be a smaller set S0. For p with v_p=0, feasibility forces y_p=0. Every root eligible at the actual active part h_{S0} is also eligible at the larger h_S. The LP inequalities therefore imply

    A_p(actual) <= v_p-y_p.

The right side is nonnegative, and (2) gives

    v_p-m_p(actual) >= y_p.

Summing proves R(v)>=sum e_p y_p. Hence

    sup_{0<=v<=w}R(v) >= max_S R_S(w).                (4)

Equations (3)--(4) prove equality. Since

    C_w(a)=X_w(a)-sup_{0<=v<=w}R(v),

we obtain (1). Each LP is compact and feasible, and there are finitely many supports. An optimizing LP solution yields an actual price vector with at least its residual; equality of the extrema shows that this vector attains the envelope as well.

The two-bin lemma implies R(v)<=2 for every v, so (1) recovers

    (X_w(a)-2)_+ <= C_w(a).

## 5. Uniform shaving is insufficient, already for three binary primes

Let a=pqr with distinct primes and w_p=w_q=w_r=1. Every row has an eligible pair, but no eligible triple. Therefore along uniform reductions v_p=v_q=v_r=t,

    F_v(a)=3(t-1/2)_+,
    inf_{0<=t<=1}[F_v(a)+3(1-t)]=3/2.

Deleting one whole coordinate leaves an active semiprime, whose source kernel is zero, at removed-load cost one. The pointwise lower bound gives

    C_w(a)=1.

Thus the actual envelope cannot be replaced by the one-parameter family (w-s)_+ without losing information. Global finite variations along that family remain valid, but they do not calculate the per-source optimal reduction.

## 6. An exact nontrivial capacity check

Let a=p^3 q, where p,q are distinct primes and q>p^2, with both original prices equal to one. In the full two-coordinate support:

* The p-row permits p,p^2,p^3 and no divisor containing q.
* The q-row permits q,pq and no divisor p^i q with i>=2.

Write u=v_p, v=v_q. The effective LP constraints are

    y_p<=u, y_p<=1/3,
    y_q<=v, 2y_q<=1+v-u,
    0<=u,v<=1.

Therefore

    3y_p+y_q <= 3y_p+1-u/2
                  <= 1+(5/2)y_p <= 11/6.

Equality is attained at

    u=y_p=1/3, v=1, y_q=5/6.

The one-coordinate supports have capacities at most 3/2 and 1. Consequently

    max_S R_S=11/6,     C_w(p^3q)=4-11/6=13/6.        (5)

For example, a=40 with p=2,q=5 realizes this exactly. This is not a computation of g(n). It shows that the envelope does not simply collapse to (X-2)_+, even for binary prices: here that hinge is 2, while the envelope is 13/6.

For comparison, with binary prices and a squarefree active part, keeping any two active coordinates proves C_w(a)=(X_w(a)-2)_+. This observation is only a check of the formula, not a claim of an interval theorem.

## 7. Remaining arithmetic question

The proposed assertion

    sum_{a<=M} C_w(a) <= sum_{b in I} K^w_M(b)

is neither proved nor disproved in this note. The exact formula (1) makes the source side accessible to finite LP certificates and exposes the need for heterogeneous price reductions. It does not compare the numerical divisor families at the two intervals, and cannot replace that missing arithmetic step.

The existing binary raw-weight Rosser theorem bounds the full target hinge. It does not automatically establish this stronger inequality with K_M on the target, since K_M can be strictly smaller than that hinge.
