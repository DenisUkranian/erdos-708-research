# A demand-stable envelope for the two-bin kernels

24 November 2026. This note does not prove the missing tail-transfer bound or the asymptotic in Erdős 708. It gives a uniform stability tool prompted by the user's counterexample to full-prefix transfer.

## 1. The discontinuity that the counterexample exploits

Write X_w(t)=sum_p w_p v_p(t), and let h_w(t) be the product of all prime powers in t whose prices are positive. The proved source kernel is

    F_w(a)=K^w_{h_w(a)}(a).

As a previously zero price becomes positive, h_w(a) can change by a large numerical factor. A root using only the old positive-price primes can thereby become eligible. Its payment need not tend to zero with the new price. Thus F_w is monotone in prices but is not, in general, Lipschitz in the removed weighted demand.

For fixed M, the target kernel is

    T_{M,w}(b)=K^w_M(b).

Both F and T are monotone under coordinatewise increases of prices. For F, this uses both the monotonicity of r_w(d) and the enlargement of the active-part size. The pointwise bounds already proved are

    (X_w(a)-2)_+ <= F_w(a),
    0 <= T_{M,w}(b) <= (X_w(b)-1)_+.

## 2. General monotone envelope lemma

Fix an integer t and a nonnegative function B_w(t) that is monotone in every coordinate w_p. Define

    E_w[B](t) = inf_{0<=v<=w}
                   { B_v(t) + X_w(t)-X_v(t) }.

The infimum is over coordinatewise price reductions. Only primes dividing t affect the expression; prices at other coordinates may be set to zero.

**Lemma.** If 0<=w'<=w, then

    0 <= E_w[B](t)-E_w'[B](t)
       <= X_w(t)-X_w'(t).                            (1)

**Proof.** The upper bound follows by using any candidate v<=w' in the infimum for w, then taking the infimum over such v. For the lower bound, take any v<=w and put v'_p=min(v_p,w'_p). Monotonicity gives B_v>=B_v'. Coordinatewise,

    w_p-v_p >= w'_p-v'_p,

because v_p<=w_p and w'_p<=w_p. Therefore

    B_v + X_w-X_v >= B_v' + X_w'-X_v'
                        >= E_w'[B].

Taking the infimum over v proves the lower bound. No continuity or attainment of the infimum is needed.

This is the greatest monotone minorant of B whose upward change is at most the corresponding weighted valuation change: any such minorant C has

    C_w <= C_v+X_w-X_v <= B_v+X_w-X_v

for every v<=w, hence C_w<=E_w[B].

## 3. Source and target envelopes preserve the useful bounds

Define

    C_w(a)=inf_{0<=v<=w}{K^v_{h_v(a)}(a)+X_w(a)-X_v(a)},
    D_{M,w}(b)=inf_{0<=v<=w}{K^v_M(b)+X_w(b)-X_v(b)}.

Then

    (X_w(a)-2)_+ <= C_w(a) <= K^w_{h_w(a)}(a),        (2)
    0 <= D_{M,w}(b) <= K^w_M(b) <= (X_w(b)-1)_+.      (3)

For (2), every candidate is nonnegative and at least X_w(a)-2, since

    K^v_{h_v(a)}(a) >= (X_v(a)-2)_+ >= X_v(a)-2.

The upper bounds follow by choosing v=w. The general lemma applies to both envelopes, including when a price crosses zero and the active part changes discontinuously.

The envelopes do not define a new arithmetic transfer theorem. In particular, no claim is made that their full-prefix sums transfer to arbitrary intervals.

## 4. A single-demand stability estimate at the original paired optimum

Let A be any source set, and let w,z be a genuinely paired boxed raw optimum for this same A,I. Thus

    sum_{b in I} z_b v_p(b)=sum_{a in A}v_p(a) (w_p>0),
    z_b=1 whenever X_w(b)>1.

For any coordinatewise reduction w'<=w, put

    Delta(t)=X_w(t)-X_w'(t),
    D=sum_{a in A}Delta(a)=sum_{b in I}z_b Delta(b).

Define the envelope defect

    G(A,I,w)=sum_{a in A}C_w(a)-sum_{b in I}D_{M,w}(b).

Then

    |G(A,I,w)-G(A,I,w')| <= D.                        (4)

Indeed the decrease of the source sum lies in [0,D] by (1). The target decrease is nonnegative and at most Delta(b) pointwise. It vanishes wherever X_w(b)<=1, by (3). On every remaining position z_b=1, so its total is at most sum_I z_b Delta(b)=D. The difference of two quantities in [0,D] has absolute value at most D.

This accounts for the removed demand once, rather than charging it independently to the source and target. It preserves the original source set and the original row equations; no row balances are asserted for w' as a new optimum.

## 5. Why this does not close the remaining inequality

For the own tail A={X_w>2+delta}, define

    R_A^C=sum_A[C_w-(X_w-2)] >=0,
    R_I^D=sum_I[(X_w-1)_+-D_{M,w}] >=0.

The exact identity is still

    J_{2+delta}=G-delta|A|-R_A^C-R_I^D.

Replacing the original kernel by its envelope changes the defect and the reserves together. The combination G-R_A^C-R_I^D is unchanged; it is the original raw dual objective relative to budget two. Equation (4) is a proved cleanup/stability tool, not a numerical upper bound for G. An arithmetic estimate on the genuine full tail is still needed.

## 6. The user's infinitesimal-support counterexample is removed by this envelope

Use p,W,M,Q as in the user's construction:

    W=floor(p^(10/7)), M=pW,
    Q={q prime: W^.31<q<=W^.32},
    w_p=1, w_q=.01,

and let w^0 be the price vector obtained by setting all filler prices to zero. Write mu_W=sum_{q in Q}1/q, which tends to mu=log(32/31).

The main-price source kernel F_{w^0} is exactly .005 on a=p*t with at least two Q-prime occurrences in t, and zero elsewhere. Here every exponent is counted: p^2*q>M, p^3>M, and at most three Q occurrences can accompany one p. If there are at least two Q occurrences, the least one q satisfies q^2<=the Q-active part, making pq eligible in the p-row. With only one such occurrence it is ineligible at the active-part source scale. All q-row payments remain zero.

Consequently

    sum_{a<=M}F_{w^0}(a)
       <= .005 W (mu_W^2/2+o(1)).                    (5)

The upper bound follows by counting unordered pairs of Q occurrences; repeated-prime pairs contribute o(W).

For any target b with v_p(b)=1 and at least one Q divisor,

    D_{M,w^0}(b)=.005.                               (6)

To check the lower bound in (6), let v<=w^0, beta=max_{q|b,q in Q}v_q, and s=1-v_p, t=.01-beta. The only possible positive roots are pq in row p. The candidate defining D is at least

    .5(.01-s-t)_+ + s+t >= .005.

The choice v=w^0 attains equality. The sum over Q divisors in the removed-price cost is at least .01-beta, including all their powers.

On the p-quotient interval of length W, the two-term inclusion-exclusion lower bound gives

    #{t: some q in Q divides t}
       >= W(mu_W-mu_W^2/2)+o(W).

The error in pair floors is O(|Q|^2)=O(W^.64)=o(W). Removing the O(W/p+1) positions with another p occurrence does not affect the main term. Therefore, uniformly in the interval shift,

    sum_{b in I}D_{M,w^0}(b)
       >= .005 W(mu_W-mu_W^2/2+o(1)).                (7)

For positive filler prices bounded by epsilon, (1) bounds the total source-envelope increase by epsilon sum_{a<=M}Omega(a), while the target envelope only increases. Choose epsilon so that this source increase is o(W). Combining (5)--(7) gives

    sum_{a<=M}C_w(a)-sum_{b in I}D_{M,w}(b)
       <= -.005(mu-mu^2+o(1))W <0.

Thus the particular counterexample mechanism cannot survive the support-stable envelopes. This calculation is a diagnosis of the instability, not a proposed restricted-class replacement for the general task.

## 7. Why the original one-row construction cannot acquire a high tail for free

In the main prices of the user's construction, a<=M has either:

* no p, hence at most five Q occurrences and load at most .05;
* one p, hence at most three Q occurrences and load at most 1.03;
* two p occurrences and no Q occurrence, hence load exactly 2.

Tiny fillers can keep the total load below 2+delta. Two obvious modifications necessarily activate additional target payments:

* To allow a source p^2*q one needs M>=p^2*q. This is exactly the inequality making pq eligible in the q-row, since (pq)^2/q=p^2*q.
* To make p*q1*q2*q3 exceed 2+delta by raising the common Q price, that price must exceed (1+delta)/3. Every pure Q triple is then hot. Its q-row modulus satisfies d^2/q<=W^(6*.32-.31)=W^1.61<M=W^(1.7+o(1)), so the new pure-Q payments cannot be omitted.

These observations do not exclude every possible tail-supported counterexample. No such stronger counterexample and no full-tail transfer theorem were obtained here.
