# A finite-error completion criterion for the unrestricted asymptotic

Date: 23 November 2026.

## Status

This note proves the common terminal implication used by the three proof
ladders. It does not construct the required payment system. In particular,
the reduction below is not a proof of the unrestricted Erdős 708 asymptotic.
Its advantage is that an arbitrarily small asymptotic exceptional fraction
is unnecessary: for each fixed delta, a sufficiently small fixed fraction
already gives a strict contradiction.

## 1. The actual global optimizer and the inherited tail estimate

Fix 0<delta<=1 and c=2+delta. For an M-term positive interval I, let

    X(a)=sum_p w_p v_p(a),  0<=w_p<=1,
    J_c(w)=sum_{a<=M}(X(a)-c)_+ - sum_{b in I}(X(b)-1)_+.

Let w be a positive global maximizer, A={a<=M:X(a)>c}, and n=|A|.
We use the previously established complete-tail bound, with B=B_delta>=1:

    sum_{a in A} exp((X(a)-c)/(2B)) <= 2n.                 (1)

We also use F=L_raw(A,I)<=C_delta n and the paired raw optimum. These are
inputs from the preceding checkpoint, not new assumptions on the size
or composition of the prime support.

## 2. Fractional exceptional mass

For any numbers 0<=q_a<=1 and t=sum_A q_a>0, Jensen's inequality gives

    sum_A q_a (X(a)-c)
      <= 2B t log((sum_A q_a exp((X(a)-c)/(2B)))/t)
      <= 2B t log(2n/t).                                 (2)

The assertion at t=0 is interpreted as zero. This version handles
fractionally served sources as well as an exceptional subset.

## 3. A single shared target budget

Suppose that 0<=theta_a<=1 and nonnegative payments P(a,b) satisfy

    sum_{b in I} P(a,b) >= theta_a (X(a)-2),
    sum_{a in A,b in I} P(a,b) <= H+E,
    H=sum_{b in I}(X(b)-1)_+,  E>=0.

For example, the stronger pointwise condition

    sum_a P(a,b) <= (X(b)-1)_+

gives E=0. There is no requirement that each target serve only one source;
payments may share a target provided its capacity is charged only once.

Put t=sum_A(1-theta_a). By (2),

    J_c(w)
      <= 2B t log(2n/t) - delta(n-t) + E.                (3)

Proof: H+E >= sum_A theta_a(X(a)-2), and therefore

    J_c(w) <= sum_A(1-theta_a)(X(a)-c)
              -delta sum_A theta_a + E.

Now apply (2). No coordinate balance is moved to a replacement source
set, and no new integer rounding is involved.

## 4. Explicit fixed tolerances

Set

    theta_delta = delta / [32 B log(64B/delta)].          (4)

Since B>=1 and delta<=1, theta_delta<1/4. If t<=theta_delta n, then

    2B (t/n) log(2n/t) <= delta/8.

Indeed, write L=log(64B/delta)>1. At the right endpoint,
log(2/theta_delta)=L+log L<=2L, and x log(2/x) is increasing for
0<x<=1/4. Also delta(1-t/n)>=3delta/4. Thus (3) yields

    J_c(w) <= -(5delta/8)n + E.                         (5)

In particular E<=delta n/4 gives J_c(w)<=-(3delta/8)n<0.

Consequently a proof ladder may fix all its accuracy parameters in terms
of delta first. It is enough to serve a 1-theta_delta fraction of the
sources, with a total shared-budget error at most delta n/4. Demanding
an o(n) exceptional set at every intermediate stage is stronger than
necessary and can introduce avoidable circular parameter choices.

## 5. Why this really would close the unrestricted asymptotic

Suppose the payment construction in Section 4 is proved uniformly for
all positive global optimizers with sufficiently large n, without
restrictions on M, the interval shift, the prime support, or the weights.
Then no such large positive optimizer exists. All positive optimizers
have n<=N_delta. The inherited bound F<=C_delta n gives

    max_w J_{2+delta}(w) <= C_delta N_delta.

Using the exact maximization identity

    max_w J_c(w)=max_{S subseteq [2,M]}(L_raw(S,I)-c|S|),

we obtain a uniform additive-constant fractional bound

    L_raw(S,I) <= (2+delta)|S| + C_delta N_delta.          (6)

As delta>0 is arbitrary, (6) gives the uniform fractional asymptotic.
The already available raw-fractional-to-integer transfer then yields
g(n)<=(2+o(1))n. This last transfer is not reproved here.

The exact 2n conjecture does not follow from this criterion: the positive
delta margin is used in (3)--(5).

### Spending some of the slack inside the carrier definition

More generally, fix 1<=tau<c-1 and gamma=c-1-tau>0. Replace each source
payment X(a)-2 by X(a)-(1+tau). If payments serve fractions theta_a of
these demands from the same target budget, the identical proof gives

    J_c(w) <= 2B t log(2n/t) - gamma(n-t) + E.            (7)

The fixed tolerance in (4) is then replaced by

    theta_gamma = gamma / [32 B log(64B/gamma)].

In particular tau=1+delta/2 leaves gamma=delta/2. A carrier d|a with
X(a/d)<=tau pays X(a)-(1+tau) at every target multiple of d. The exact
threshold one is therefore unnecessary for the asymptotic problem.
This enlargement is useful before starting a Hall or capacity argument.

## 6. Work still required

The common missing object is the payment construction, not (3). The
adaptive-matching route seeks it through all cold-complement choices;
the diffuse route seeks a joint bank estimate whose errors are measured
at scale n; the signed-certificate route seeks an aggregate transfer
without losing either inactive cofactors or target capacity. Each route
has additional arithmetic content beyond this terminal implication.
