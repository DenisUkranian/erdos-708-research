# Exact prime-conserving excess flow at a minimal covering LP

## Scope

This is an exact structural theorem for the unrestricted boxed valuation LP. It preserves every active prime's source and target capacities, including full target valuations. It does not compute any value of g(n), assume a restricted source class, or prove J_weak.

The result is useful in two ways. It provides a precise flow representation of a minimal optimum. It also identifies the limitation of a flow that only transports individual prime contributions: the only remaining deficiency in this network is exactly the unresolved global LP excess.

## 1. Setup and the network

Let A be a set of m distinct integers in [2,M], let I={x+1,...,x+M}, x>=0, and let

    L(A,I)=min sum_b z_b,
    0<=z_b<=1,
    sum_b z_b v_p(b)>=D_p(A)=sum_{a in A}v_p(a).

Assume that a fixed real c satisfies

    L(S,I)<=c|S| for every proper subset S of A.             (1)

All subsets keep the same ambient M and the same interval I. Choose an optimal nonnegative dual w, write

    X(n)=sum_p w_p v_p(n),
    h_b=(X(b)-1)_+,
    H_I=sum_{b in I}h_b,
    F=L(A,I)=sum_A X-H_I.

Only the finite source-prime set is used. The weights need not be rational for the theorem. They may be clipped to [0,1], but this particular flow argument does not require clipping.

Construct a finite network with four layers:

    source -> source integer a -> prime p -> hot target b -> sink.

The capacities are

    source -> a: q_a=(X(a)-c)_+;
    a -> p:      w_p v_p(a);
    p -> b:      w_p v_p(b);
    b -> sink:   h_b.

Only targets with h_b>0 need be included. Zero-capacity edges may be omitted. All target exponents v_p(b) are their actual values; they are not truncated at M or at the largest source exponent.

Let D=sum_A q_a. A flow in this network transports weighted prime mass, preserving the prime label. It does not require a target to share a hot divisor with any one source.

## 2. The exact maximum-flow value

**Theorem.** Under (1), the maximum flow in the above network is exactly

    min(D,H_I).                                            (2)

If F>cm, then every X(a)>c and

    D=H_I+(F-cm),                                         (3)

so the flow deficiency is exactly F-cm. If F<=cm, every source quota is routable.

**Proof.** The upper bound min(D,H_I) is immediate. It remains to prove the matching lower bound by examining all cuts.

Fix a cut. Let S be the source integers on the source side and let P be the prime vertices on that side. Source integers with q_a=0 can be moved to the sink side without increasing the cut capacity. Thus assume X(a)>c for every a in S. Write

    X_P(n)=sum_{p in P}w_p v_p(n),
    w_P=(w_p 1_{p in P})_p.

After optimizing the target vertices' sides, the cut capacity is

    sum_{a not in S}q_a
    +sum_{a in S,p not in P}w_p v_p(a)
    +sum_{b in I}min(h_b,X_P(b)).                          (4)

Equivalently, its deficiency relative to the total source quota D is

    sum_{a in S}X_P(a)-c|S|
      -sum_{b in I}min(h_b,X_P(b)).                        (5)

For every target,

    min((X(b)-1)_+, X_P(b)) >= (X_P(b)-1)_+,               (6)

because 0<=X_P(b)<=X(b). Therefore (5) is at most

    Phi_S(w_P)-c|S|,
    Phi_S(v)=sum_{a in S}X_v(a)-sum_{b in I}(X_v(b)-1)_+.

If S is proper, this is nonpositive by weak duality and (1). If S=A, it is at most F-cm by optimality of w for A. Consequently every cut has deficiency at most max(F-cm,0).

If F>cm, apply (1) to A\{a} using the same target hinge. It gives

    X(a)>=F-c(m-1)=c+(F-cm)>c

for every a. Thus (3) holds. The cut using all source and prime vertices has target capacity H_I and deficiency F-cm, so the maximum flow is H_I.

If F<=cm, all cuts have nonpositive deficiency. Thus all D units can be routed. In particular D<=H_I, also following from the global shortfall inequality

    sum_A(c-X(a))_+ <= (cm-F)_+.

This proves (2). No arithmetic approximation, cut enumeration, or numerical optimization is used. End of proof.

### Exact connection with block-deletion loss

For every prime subset P there is the pointwise identity

    min((X-1)_+,X_P)=(X-1)_+-(X_{P^c}-1)_+.               (14)

Let ell(P)=F-Phi_A(w_{P^c}) be the loss caused by deleting P from the original optimal vector. Equation (5) can then be written exactly as

    ell(P)-sum_{a not in S}X_P(a)-c|S|.                   (15)

Optimizing over S gives

    ell(P)-sum_{a in A}min(X_P(a),c).                     (16)

Indeed the maximizing S consists of the sources with X_P(a)>c, which automatically had positive original quotas. Thus the prime-conserving cut problem is governed by the same block-deletion loss function as the earlier optimal-band argument. It supplies a useful exact representation, not an extra unaccounted gain in the hinge budget.

## 3. A designated source can absorb the entire excess

Suppose F=cm+e with e>0. For any chosen a_0 in A, replace the source quotas by

    d_a=X(a)-c-e 1_{a=a_0}.                               (7)

Minimality gives X(a)>=c+e, so all d_a are nonnegative, and

    sum_A d_a=H_I.                                       (8)

**Corollary.** There is a flow that sends exactly d_a units from every source a and fills every hot target capacity h_b exactly.

**Proof.** In the cut expression above, subtract e whenever a_0 belongs to S. A proper source set already had nonpositive deficiency. For S=A, the upper bound F-cm=e is cancelled exactly. All cuts therefore permit the full total H_I in (8). End of proof.

The theorem was independently checked by another collaborating agent, including cuts containing only part of the prime set and the full target powers.

## 4. Disintegration of the remaining weighted demand

Choose a paired optimal primal z. Complementary slackness gives z_b=1 at hot targets, z_b=0 when X(b)<1, and

    sum_b z_b v_p(b)=D_p(A)  whenever w_p>0.                (9)

Decompose the flow of Section 3 into paths a->p->b, and denote their weighted amounts by f_{a,p,b}. Define source residuals

    r_{a,p}=w_p v_p(a)-sum_b f_{a,p,b}

and target residuals

    s_{b,p}=z_b w_p v_p(b)-sum_a f_{a,p,b},                (10)

where f vanishes at non-hot targets. These quantities are nonnegative. By (9), for every active prime

    sum_a r_{a,p}=sum_b s_{b,p}.                           (11)

Their totals satisfy

    sum_p r_{a,p}=c+e 1_{a=a_0},                          (12)

and

    sum_p s_{b,p}=1       if X(b)>1,
                   z_b   if X(b)=1,
                   0     if X(b)<1.                     (13)

Thus the optimal primal cost is represented by a remaining weighted mass of c per source, with the entire excess e attached to any designated source. Every hot target contributes exactly one residual unit, and threshold-one targets contribute their actual z_b.

This is a disintegration of weighted valuation mass. It does not assign a source integer to one or two target integers, and it does not assert that arbitrary source-to-target path bundles multiply to a divisor of a single target.

## 5. The exact limitation for J_weak

In a raw-minimal failure at c=2+2delta, the quotas in (7) are approximately X(a)-2-2delta. Raising them to X(a)-2-delta adds delta*m units, apart from the existing excess adjustment. The total available target hinge remains H_I. Proving that this extra linear mass can be paid is precisely the missing global estimate; the flow theorem does not supply it.

A path a->p->b only guarantees that the same active prime occurs at both endpoints. It does not imply

    X(gcd(a,b))>1,

nor that b is a multiple of a/p or of any other hot divisor of a. Replacing this graph by a hot-divisor or cofactor graph therefore requires a new argument. In particular, restricting w to the prime union of a source subset may make a target hot using contributions from several different sources, although no one of those sources shares a hot divisor with that target.

Conversely, making a conjectured flow easier by adding all same-prime paths does not reveal a further hidden cut obstruction: (2) shows that this network already has no deficiency beyond the global quantity F-cm.

Any successful continuation must use the additional arithmetic of actual cofactor banks to improve the global cost, rather than infer that improvement solely from this prime-conserving routing normal form.
