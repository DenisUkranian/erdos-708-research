# The corrected full-tail deficit and finite downward price changes

24 November 2026. This note does not prove the uniform raw asymptotic.
It records an exact distinction in the proposed remaining inequality and
a general stability lemma for a genuinely paired raw optimum. Neither
claim is an arithmetic transfer theorem.

## 1. What the reserve-corrected inequality actually says

Fix c=2+delta, a weight vector w, its own strict full tail

    A={a<=M:X_w(a)>c}, n=|A|,

and an actual interval I of length M. Write

    Phi_A(w)=sum_A X_w(a)-sum_I(X_w(b)-1)_+.

For the proved two-bin kernel, let

    Gamma=sum_A K_{h(a)}(a)-sum_I K_M(b),
    R_A=sum_A[K_{h(a)}(a)-X_w(a)+2],
    R_I=sum_I[(X_w(b)-1)_+-K_M(b)].

Then, exactly,

    Gamma-R_A-R_I = Phi_A(w)-2n = J_c(w)+delta*n.       (1)

Thus the proposed estimate

    Gamma <= R_A+R_I+o_delta(n)

is precisely Phi_A(w)<=2n+o_delta(n) on this optimizer class. It is a
correct sufficient target, but merely substituting (1) is not progress
towards its proof. At a genuine paired optimum Phi_A(w)=L_raw(A,I).

There is a further distinction worth preserving:

    J_2(w) = Phi_A(w)-2n
             +sum_{a<=M, 2<X_w(a)<=c}(X_w(a)-2).       (2)

The corrected full-tail quantity in (1) is not J_2(w) when there is a
nonempty middle tail. A claim about J_2 must retain the last sum in (2).

## 2. Exact finite-pruning loss at the same paired optimum

Assume w is genuinely optimal for the boxed raw cover of this fixed A,
and z is a paired primal optimum. The boxes are on the primal z variables.
The original dual only requires w>=0; w<=1 is chosen using the clipping
theorem. Hence exact positive-price rows include w_p=1. Stationarity for
an artificially restricted weight cube alone would not suffice.
The needed complementary conditions
are

    z_b=1 if X_w(b)>1,
    z_b=0 if X_w(b)<1,
    sum_I z_b v_p(b)=sum_A v_p(a) whenever w_p>0.       (3)

Take any coordinatewise downward change 0<=w'_p<=w_p. Define

    Delta(t)=X_w(t)-X_w'(t),
    D=sum_A Delta(a).

Only coordinates that were active can change. Multiplying the whole
prime-row equalities in (3) by w_p-w'_p gives

    D=sum_I z_b Delta(b).                             (4)

**Lemma.** The exact raw-dual loss is

    Phi_A(w)-Phi_A(w')
      =sum_{b:X_w(b)>1}(1-X_w'(b))_+
          +sum_{b:X_w(b)=1} z_b Delta(b).              (5)

In particular,

    0 <= Phi_A(w)-Phi_A(w') <= D.                      (6)

**Proof.** On an old hot position,

    (X_w-1)_+-(X_w'-1)_+=min(Delta,X_w-1).

On an old cold or boundary position the hinge decrease is zero. Hence

    Phi_A(w)-Phi_A(w')
       =D-sum_{b:X_w(b)>1}min(Delta(b),X_w(b)-1).

Substitute (4). For old hot positions z_b=1, and

    Delta-min(Delta,X_w-1)=(1-X_w')_+.

For old cold positions z_b=0. Old boundary positions contribute
z_b Delta(b). This proves (5); (6) also follows directly.

The sets of active divisors and the values K_{h(a)}(a) may change
discontinuously when a price reaches zero. Equation (5) is unaffected:
those jumps cancel between Gamma and the reserves in (1). In particular,
the corrected deficit is stable in the weighted source-demand norm D,
even when the individual kernel terms are not.

This is a statement about the original paired optimum. It does not
assert new row equalities for w', its new strict tail, or another primal.

## 3. Exact zero-loss criterion for infinitesimal support padding

Equation (5) gives a useful criterion without assuming D is small.
If every old hot target stays at load at least one, and every old target
tie with z_b>0 loses zero load, then Phi_A(w')=Phi_A(w).

A concrete sufficient condition is:

* every retained price w'_p is an integer multiple of 1/Q;
* Delta(b)<1/Q for every b in I.

Indeed, X_w'(b) is a nonnegative integer multiple of 1/Q. If
X_w'(b)<1, then X_w'(b)<=1-1/Q, so the strict inequality Delta(b)<1/Q
forces X_w(b)<1. Thus an old hot target cannot cross below one, and an
old tie cannot lose a positive amount. Equation (5) yields zero loss.

Now suppose w is a global maximizer of J_c, and A is its own full tail.
Since w'<=w, no source outside A can enter the new tail. Therefore

    J_c(w')=Phi_A(w')-c*n
               +sum_{a in A}(c-X_w'(a))_+.

If the pruning has zero raw-dual loss, the right side is at least
J_c(w). Global maximality forces equality, so w' is also a global
maximizer and no old source can fall strictly below c.

Consequently, among global maximizers chosen to minimize sum_p w_p,
there cannot be a nonzero removable padding block satisfying the two
quantized conditions above. The result applies even if the small prices
occur in genuine sources; it is stronger than simply discarding
zero-demand coordinates. It does not bound Q or the number of remaining
active coordinates.

If only D=o_delta(n) is known, (6) instead gives an o_delta(n) raw loss.
This is the correct way to control support changes; an estimate for the
uncorrected kernel alone is not justified.

## 4. A finite global-variation consequence

For a global maximizer and the same downward change, combine (5) with
J_c(w')<=J_c(w). One obtains the exact necessary inequality

    sum_{a in A}(Delta(a)-(X_w(a)-c))_+
      <=sum_{b:X_w(b)>1}(Delta(b)-(X_w(b)-1))_+
         +sum_{b:X_w(b)=1}z_b Delta(b).                (7)

Thus the source loss caused by sources crossing their threshold is
paid by target hot positions crossing one and by original target ties.
All prime powers enter through the whole-row identity (4).

This records finite, rather than infinitesimal, optimality. By itself it
does not supply the required uniform estimate: it is still necessary to
choose an arithmetic downward variation whose right side is controlled
by a single available target budget.

## 5. Effect of the user's counterexample

The user's tiny positive prices inflate h(a) to a, even though their
load contribution can be made arbitrarily small. That is a real
discontinuity of the uncorrected full-prefix kernel, not a contradiction
to either pointwise inequality.

For the stated construction the strict tail X>2+delta is empty. It
therefore supplies no obstruction to the full-tail corrected objective
in (1). At an optimized instance, (5)--(6) show precisely how a small
weighted-demand block can be removed without retaining a spurious
active-part transfer claim. If a block is only described as having small
individual prices, its total weighted source demand must still be
estimated; small prices alone do not imply D=o(n).

## Remaining gap

No arithmetic choice of a pruning block or finite downward variation
was found that proves Phi_A(w)<=2n+o_delta(n) uniformly on all genuine
positive joint optima. The common source/target kernel theorem remains
valid, while its unconditional full-prefix transfer is disproved by
the verified counterexample. The equations here do not close
Erdos 708.
