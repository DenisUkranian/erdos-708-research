# Raw minimality, deletion banks, and the global dual obstruction

## Status and scope

The reductions and identities in Sections 1--7 below are proved for the full
source class. They do not prove the unrestricted asymptotic conjecture.
Sections 2--4 and 7 received a separate internal audit by the combinatorial
agent, with no correction required. This is not external or formal review.
The remaining expansion statement in Section 8 is explicitly a candidate,
not a theorem. No arithmetic source relaxation is identified with an actual
minimal failing instance.

Let `A` be distinct integers in `[2,M]`, let `I={x+1,...,x+M}`, `x>=0`,
and put

    D_p(A)=sum_{a in A} v_p(a).

The boxed raw covering LP is

    L(A,I)=min sum_{b in I} y_b
    subject to 0<=y_b<=1 and sum_b y_b v_p(b)>=D_p(A).

Full supply follows from `product A | M! | product I`, so this finite LP is
feasible. Its dual can be written

    F_A(w)=sum_{a in A} X_w(a)-sum_{b in I}(X_w(b)-1)_+,
    X_w(t)=sum_p w_p v_p(t),  w_p>=0.

Only source primes are needed. An optimum can be clipped to `0<=w_p<=1`:
when `w_p>1`, every p-bearing target is already above load one, and the
objective's slope in that coordinate is
`D_p(A)-sum_I v_p(b)<=0`. Lowering the coordinate to one cannot reduce
the objective.

## 1. Minimal RAW failure at a fixed ambient interval

Fix `c>2`, M and I. Suppose A has the least cardinality among subsets of a
given source set satisfying

    L(A,I)>c|A|.

Write `m=|A|`, `F=L(A,I)=cm+e`, where `e>0`, and

    K=c(m-1)+1.

Every proper subset S has `L(S,I)<=c|S|`, with the ORIGINAL M and I.
In particular every deletion admits a fractional cover `y^a` of cost at
most `c(m-1)=K-1`.

For an optimal clipped full dual w, deletion dual feasibility gives

    F-X_w(a) <= L(A\{a},I) <= c(m-1).

Therefore every source satisfies the stronger exact condition

    X_w(a)>=c+e>c.                                       (1)

This removes the source positive-part ambiguity for this particular
optimal dual. It does not make an arbitrary arithmetic source family a
raw-minimal failure.

Clipping also gives `X_w(a)<=Omega(a)<=log_2 M`, so

    0<e<=min_{a in A}(X_w(a)-c)<=log_2 M-c.

Thus `L(A,I)=cm+O(log M)`. In any paired primal optimum, every target
with load strictly greater than one has value one. Consequently the
TOTAL number of such hot targets, not only the bank-union size, is at
most `cm+log_2 M-c`.

## 2. A residual prime-unit repair lemma

For any partial fractional selection y, define its positive deficits by

    d_p=max(D_p(A)-sum_b y_b v_p(b),0).

It can be extended to a full fractional cover with additional cost at
most `sum_p d_p`. Whenever a prime is deficient, full supply guarantees
enough remaining valuation in the unused capacities `1-y_b`. Buying
fractional mass at targets divisible by this prime costs no more than
the valuation supplied, since every positive integer valuation is at
least one. Greedily filling one deficit never increases any other one.
All purchased masses respect the box constraints.

The integer version uses at most one new position per missing prime
unit. Here the fractional version is needed and is explicitly justified.

## 3. Nearly full saturation of the entire deletion-bank union

For a source a, define

    U_a=union_{q prime,q|a} {b in I : a/q divides b}.

For EVERY deletion fractional cover y of cost at most `K-1`, one has

    sum_{b in U_a}(1-y_b)<1.                             (2)

Indeed, otherwise buy a total mass one using residual capacities inside
U_a. For each used target choose a witnessing removed prime q. The
new valuations cover the source vector `v(a)` except for a nonnegative
vector of total mass at most one: the witness primes are averaged with
the purchased masses. Section 2 repairs those remaining deficits at
cost at most one. The total cost would be at most

    c(m-1)+2<cm<F,

a contradiction. Thus one must not replace (2) by the false statement
that every individual target of U_a has y_b=1. That stronger statement
belongs to integer deletion covers, not fractional ones.

For each q|a, its bank has at least q positions. Equation (2) implies

    K-1 >= sum_b y_b > q-1,
    hence q<K<cm.                                       (3)

All source primes are therefore below cm in the raw-minimal class.

## 4. The correct fractional pair-bank lemma

Suppose `pq|a`, counting occurrences and allowing p=q, and `pq>=K`.
Then

    D_p(A)>(q-1)v_p(a/q).                               (4)

To prove this, every deletion cover y as above supplies from the
`a/q` bank alone more than

    (N_I(a/q)-1)v_p(a/q) >= (q-1)v_p(a/q).

If the opposite inequality to (4) held, y would already supply the FULL
p-demand of A. The `a/(pq)` bank has at least pq positions, and its
residual capacity is at least `pq-(K-1)>=1`. Buy mass one there. After
that, only one q-unit can remain deficient; the p-demand was already
fully covered. Section 2 repairs it for cost at most one. Again the
total cost is below cm. The repeated-prime case is valid as well.

The factor q-1 is essential in this proof. An integer forced-bank
argument with factor q cannot be imported without an additional step.

Define

    E={p in P:p<=sqrt K} union {p in P:D_p(A)>=p},
    R=P\E.

Every source contains at most one OCCURRENCE from R, and that occurrence
is its unique largest prime. If r in R occurred with another occurrence
q>=r, then rq>K and (4) would imply

    D_r>(q-1)v_r(a/q)>=r-1,

contrary to `D_r<=r-1`.

The same logarithmic demand budget as in the integer argument gives

    |E|=O_c(sqrt(m/log m)),

because `sum_{D_p>=p} p log p <= sum_a log a <=m log M` and the ambient
quadratic theorem forces `M<16m^2`. The small-prime part contributes at
most `pi(sqrt K)`. Also `|P|<=pi(cm)=o(m)`, so rounding a boxed LP vertex
costs only o(m) positions.

## 5. Exact deletion primal--dual gap identity

Keep the SAME optimal full dual w from Section 1. Let y be any deletion
cover for A without a, of cost `C_a<=c(m-1)`. Write `X_b=X_w(b)` and
`X_a=X_w(a)`. Then

    G_a=C_a-F+X_a

has the exact decomposition

    G_a = sum_p w_p [sum_b y_b v_p(b)-D_p(A)+v_p(a)]
          + sum_{X_b>1}(1-y_b)(X_b-1)
          + sum_{X_b<1} y_b(1-X_b).                      (5)

Every term is nonnegative. Thus

    0<=G_a<=X_a-c-e.                                    (6)

This identity keeps oversupply, unpurchased hot-target capacity and
purchased cold-target capacity in ONE budget. They cannot each be
charged the full source excess independently.

Let `wmax(a)=max_{q|a}w_q`. Every target in U_a has
`X_b>=X_a-wmax(a)>1`. Equations (5)--(6) therefore sharpen (2) to

    sum_{b in U_a}(1-y_b)
       <= (X_a-c-e)/(X_a-1-wmax(a)) <1.                 (7)

The numerator may be zero. The denominator is positive because
`wmax(a)<=1` and `X_a>c>2`.

## 6. Full optimality gives a JOINT union constraint

Let `U=union_{a in A}U_a`, and let y* be a primal optimum paired with w.
Every target in U has load above one by (1), so complementary slackness
forces `y*_b=1` on U. Every row with `w_p>0` is tight. Consequently

    sum_{b in U}v_p(b)<=D_p(A) for every p with w_p>0,
    sum_{b in U}X_w(b)<=sum_{a in A}X_w(a),
    |U|<=F.                                            (8)

These are necessary conditions for an ACTUAL raw-minimal failure. In
particular, an arbitrary bank-union example whose source prime demand
exceeds the union at one coordinate does not establish these joint
conditions at all active coordinates or establish LP optimality.

For every subset S of A and every cover y of A\S of cost at most
`c(m-|S|)`, consider a fractional matching from S to the bank unions U_a,
with target capacities `1-y_b`. A perfect such matching would buy one
cofactor mass per source, then at most |S| prime-unit repairs, yielding
cost below cm. Hence some nonempty T subset S must satisfy the exact
fractional Hall obstruction

    sum_{b in union_{a in T}U_a}(1-y_b)<|T|.             (9)

For S=A the empty cover is allowed. The assertion concerns residual
matching capacity, not a hypothetical ordinary graph independent of y.

## 7. Exact same-delta transfer from INTEGER to RAW minimality

Fix delta>0. Suppose there are arbitrarily large source sets failing
the integer budget `(2+3delta)|A|`. For each original interval M,I,
first take an integer failing subset A_0 of least cardinality m_0.
The integer forced-bank lemma gives source primes below
`(2+3delta)m_0`; the quadratic gate gives `m_0>sqrt(M)/4`.
Rounding a boxed LP vertex costs at most the number of source-prime
rows, so

    L(A_0,I)> (2+3delta)m_0-pi((2+3delta)m_0)
             > (2+2delta)m_0

for all sufficiently large M.

At the SAME M,I, choose a subset B of A_0 of least cardinality satisfying

    L(B,I)>(2+2delta)|B|.

Apply Sections 1--6 with `c=2+2delta`, `m=|B|`. Its own quadratic gate
gives `m>sqrt(M)/4 -> infinity`; its own prime cap and core use this m,
not m_0. In particular, the remaining sufficient global target is

    L(B,I)<=(2+delta)m+o(m)

on these actual raw-minimal instances. This would contradict their
defining lower bound. The optimal dual has ALL source loads above
`2+2delta`, whereas the test threshold can be `2+delta`, leaving a
linear delta*m margin. A merely o(m) upper bound on the excess ABOVE
the raw-minimality coefficient itself would not suffice.

## 8. A global bank expansion candidate and a targeted exact test

A possible sufficient statement would be:

    If 0<=w_p<=1 and X_w(a)>2 for every a in A, then
    sum_{b in U(A,I)}X_w(b)>sum_{a in A}X_w(a).

It would contradict (8), but it is NOT proved here. Coordinatewise
bank-product domination is already false, as recorded by the separate
exact lifted Hall certificate in the combinatorial directory. That
counterexample does not by itself settle this weighted statement.

`joint_bank_closure.py` tests the weighted candidate for fixed actual
CRT-realizable intervals and rational clipped weights. It optimizes over
ALL source subsets of the strictly-hot candidates using one exact
integral maximum-closure computation. Source nodes have positive profit
X(a), target nodes cost X(b), and source-to-cofactor-to-target arcs force
selection of the actual full bank union. A nonempty selection with
nonnegative profit would refute the displayed strict auxiliary claim,
not Problem 708. An empty optimizer with profit zero does not prove
strict positivity for every nonempty selection, much less a universal
theorem. The independent witness validator uses only the Python standard
library and exact integer arithmetic.

## 9. An independently checked alternative: normalize the integer obstruction

This alternative retains the original integer-minimal source set and its
optimal raw dual. Let `c=2+3delta`, `m=|A|`, `r=|P|`, and suppose
`tau(A,I)>cm` while every proper source subset has an integer cover within
its c-budget. Rounding gives

    L(A,I)>cm-r.

Choose an optimal clipped dual w and put `T={a in A:X(a)<c}`. If T is
nonempty, the same w is feasible for the dual of A without T, so

    L(A,I)-sum_{a in T}X(a) <= L(A\T,I) <= c(m-|T|).

Consequently

    sum_{a in T}(c-X(a)) <= cm-L(A,I) < r.               (10)

The complement may be empty; its LP value is then zero, so this causes
no exception. If T itself is empty, handle it directly: it is NOT valid
to assert `0<=cm-L` when L may exceed cm.

Set `B={a:X(a)<=c-delta}` and `G=A\B`. Either B is empty, or (10) gives

    |B|<r/delta,
    sum_{a in B}X(a)<=(c-delta)r/delta.                  (11)

All sources of G satisfy `X(a)>c-delta=2+2delta`. Therefore every target
in its full prime-deletion bank union U_G has load strictly larger than
`1+2delta`, and is saturated in the full optimal primal for A.
Complementary slackness gives, for every active row,

    V_p(U_G)<=D_p(A)=D_p(G)+D_p(B).

In particular the stronger sum of POSITIVE row oversupplies satisfies

    sum_{p:w_p>0} w_p (V_p(U_G)-D_p(G))_+
       <=sum_p w_p D_p(B)
       =sum_{a in B}X(a)
       =O_delta(r)=o(m).                               (12)

This is not merely a signed weighted-total comparison: no cancellation
between excessive and deficient prime coordinates is used. The original
integer minimality gives `r<=pi(cm)=o(m)` and `M<16m^2`. The retained G
has `|G|=m-o(m)` and inherits source-only factorization restrictions, but
it is not asserted to be a minimal failure itself.

Thus a genuinely uniform lower bound of order m for the left side of
(12), for these normalized data, would close the asymptotic problem.
Such a global lower bound is not established by this normalization.
