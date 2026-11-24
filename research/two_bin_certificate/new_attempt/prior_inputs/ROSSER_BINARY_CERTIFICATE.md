# A product-truncated certificate for binary raw prime weights

## Statement

Let `P` be an arbitrary finite set of primes at most `M`. Put

    X(t) = sum_(p in P) v_p(t).

For every interval `I` of `M` consecutive positive integers,

    sum_(a=1)^M (X(a)-2)_+ <= sum_(b in I) (X(b)-1)_+.

The proof below uses no restriction on the number of active prime factors, includes every prime power, and is uniform in the interval shift. It is a binary-weight result; no claim about arbitrary real weights or the complete Erdős 708 problem is made here.

## Recursive sieve polynomial

Write `d(S)=prod_(p in S) p`. A subset `S` of `P` is feasible if `d(S)<=M`. We construct coefficients `q_S` satisfying:

1. `q_empty=1`, `q_{p}=-1` for each prime, and all coefficients are in `{0,(-1)^|S|}`.
2. `q_S=0` whenever `d(S)>M`.
3. With `Q(B)=sum_(S subseteq B) q_S`, one has `Q(B)<=0` for every nonempty subset `B` of `P`.
4. For every nonempty feasible `B`, `Q(B)` is either `0` or `-1`.
5. For every nonempty feasible `B`, `q_B!=0` implies `Q(B)=0`.

For the empty prime set use the polynomial `Q=1`. For the induction step let `p` be the smallest prime, and construct `q` on the larger primes with the same cutoff `M`. Call a feasible set `S` on those primes internal if `p*d(S)<=M`, and boundary otherwise. Define the new polynomial by

    Q_new(x) = (1-x_p) sum_(S internal) q_S*x_S
               + sum_(S boundary, q_S<0) q_S*x_S.

Thus an internal coefficient is retained and paired with its negative after adjoining `p`; a negative boundary coefficient is retained, and a positive boundary coefficient is deleted.

The elementary arithmetic point is that a boundary set is maximal feasible among the larger primes: adjoining any new larger prime multiplies its product by at least `p`.

For a target subset containing `p`, the paired terms cancel, leaving only negative boundary coefficients. For a target subset not containing `p`, the old polynomial is reduced by a sum of nonnegative deleted coefficients. This proves property 3.

For a feasible subset containing `p`, no boundary subset can occur; its polynomial value is zero. For a feasible nonempty subset `B` not containing `p`, any boundary subset of `B` has to equal `B` itself. Therefore the value can change only when the positive coefficient `q_B=1` is deleted. In that case the inductive property 5 gives the old value `Q(B)=0`, so the new value is `-1` and the new coefficient is zero. Otherwise the old value is unchanged. Properties 4 and 5 follow. The sign rule and singleton coefficients follow directly from the construction.

## Arithmetic transfer, with the floor errors paid exactly once

Let `B(t)` be the set of primes in `P` dividing `t`, and set

    F(t)=X(t)-1+Q(B(t)).

If `X(t)=0`, then `F(t)=0`. Otherwise property 3 gives

    F(t) <= X(t)-1 = (X(t)-1)_+.

For `a<=M`, its radical subset `B(a)` is feasible. Properties 4 and 5 give

    F(a) >= (X(a)-2)_+.

Moreover, for every negative coefficient `q_S=-1` with `|S|>=3`, the source integer `a=d(S)` satisfies `Q(S)=0`, and therefore

    F(d(S)) = |S|-1 = (X(d(S))-2)_+ + 1.

Every such negative coefficient has a distinct source integer available to pay its one-unit transfer error.

To see the transfer explicitly, expand

    X(t)=sum_(p in P) sum_(j>=1) 1_(p^j divides t).

The constant and first prime-power terms cancel against `-1+Q`. The remaining prime-power terms (`j>=2`) all have positive coefficients. The remaining squarefree terms have coefficients `q_S`, with `|S|>=2`, and every negative term has odd cardinality at least three and modulus at most `M`.

For any positive modulus `d`, the number of multiples in an interval of `M` consecutive integers is

    floor(M/d)+epsilon_d,  epsilon_d in {0,1}.

Consequently, if `N_-` is the number of negative squarefree coefficients of cardinality at least three,

    sum_(b in I) F(b) >= sum_(a=1)^M F(a) - N_-.

There are only finitely many prime-power terms relevant to either finite interval. All positive terms transfer without loss. Charging each possible negative loss to its distinct source `d(S)` yields

    sum_(a=1)^M F(a) - N_- >= sum_(a=1)^M (X(a)-2)_+.

This proves the statement.

## General-weight obstacle

The induction above exploits exact cancellation for a binary prime occurrence: the remainder of `(1-X)_+` becomes zero after that occurrence. For real prime weights, the analogous recursion couples thresholds `t` and `t-w_p`; its boundary coefficients need not have magnitude at most one or alternating signs. Therefore this proof cannot currently be integrated over weight profiles or applied to arbitrary raw weights without a new argument. It does not yet establish the uniform terminal cluster inequality.

The failure of a simple probabilistic lift is pointwise. If `w_p=w_q=1/2` and `b=pq`, then `(X(b)-1)_+=0`. Independently replacing each weight by a Bernoulli variable of the same mean produces expected binary target hinge `1/4`. A common-threshold replacement produces expectation `1/2`. Thus averaging binary certificates incurs an additional target cost with no direct justification for charging it to the source reserve.

## A consequence for genuine global optimizers

At a genuine positive joint optimizer, at least one active weight lies in `(0,1/2]`.

Indeed, suppose all positive weights are strictly larger than `1/2`, and fix its full source tail `A`. On the coordinate box from the current weight vector to the vector that sets every active weight equal to one, every target integer containing at least two active prime occurrences already has load strictly greater than one. An integer with one active occurrence never has positive target hinge anywhere in that box. Therefore the fixed-source dual objective

    D_A(v) = sum_(a in A) X_v(a) - sum_(b in I) (X_v(b)-1)_+

is affine throughout that box. Every coordinate strictly between zero and one has zero derivative at an optimizer for `A`; coordinates already equal to one do not change. Raising all active weights to one therefore preserves `D_A`. The binary theorem gives `D_A<=2|A|`, contradicting a positive joint excess at budget `(2+delta)|A|`.

This is a structural consequence, not the missing arbitrary-weight theorem. It neither controls the primes with weights at most one half nor proves the requested terminal cluster bound.
