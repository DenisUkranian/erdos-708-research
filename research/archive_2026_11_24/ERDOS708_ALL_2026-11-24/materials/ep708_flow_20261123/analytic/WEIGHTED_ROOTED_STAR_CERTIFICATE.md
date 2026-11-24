# A canonical weighted rooted-star certificate and its exact local obstruction

## Status

This note constructs a global, finite, signed target certificate for arbitrary clipped raw weights. It handles repeated prime occurrences, has a unique positive root at every target, and does not sum an independent target budget over arbitrary source patterns.

The certificate leads to a weighted-tail counting problem. A simple prefix-unweighted/tail-weighted condition proves it in a sparse-support regime, but that condition is not the requested general theorem. More importantly, Section 6 gives an exact counterexample to the tempting replacement by an individual exact-sieve comparison for each root, even at total weighted mean less than one. Thus a successful global proof must retain cancellation between roots.

J_weak is not proved here.

## 1. Ordered prime occurrences and the first crossing

Let P be a finite set of primes with 0<w_p<=1 and put

    X(n)=sum_{p in P}w_p v_p(n).

Primes outside P have weight zero. Order the P-prime occurrences in an integer increasingly by prime, retaining multiplicity.

For any integer with X(n)>1, its root B is the product of the first occurrences up to and including the first crossing of load one. Put p_0=Pmax(B). Equivalently,

    X(B/p_0)<=1<X(B),
    h_B=X(B)-1 in (0,w_{p_0}] subset (0,1].               (1)

All prime-power blocks at primes below p_0 are complete in B, but the p_0 block may be partial.

After removing the first total weight one, the remaining ordered weight pieces are

    h_B, followed by the weights of the occurrences outside B.

Their total is X(n)-1.

For 0<u<=1 and R>=0 define

    psi_u(R)=(u+R-1)_+-(R-1)_+
            =min(u,(u+R-1)_+).

The following exact elementary bounds will be used:

    0<=psi_u(R)<=u,
    psi_u(R)<=u R,
    psi_u(R)>0 implies R>0.                              (2)

For R<=1, the nontrivial inequality in (2) is
u+R-1<=uR, equivalent to (1-u)(1-R)>=0. For R>=1 it is immediate.

If the remaining ordered pieces are u_0,...,u_l and R_i is the sum of those strictly after u_i, telescoping gives

    (X(n)-2)_+=sum_{i=0}^l psi_{u_i}(R_i).                (3)

This is the weighted version of deleting a final unit of weight. It does not replace a small last atom by a full unit without accounting for the difference.

## 2. Finite carrier family and the signed target kernel

Fix M. Let B range over P-smooth roots satisfying (1), with B p_0<=M. There are two kinds of terms.

* The base term has d=B, coefficient u=h_B, and q=p_0.
* A star term has d=B q^j, coefficient u=w_q, where q in P, q>=p_0, j>=1, and d q<=M.

For q=p_0, the exponent j counts occurrences beyond those already in B. For q>p_0, it counts the first j occurrences of q outside B.

Let Q_B={p in P:p<p_0}. For either kind of carrier define

    K_{B,d}(b)
      =1[d|b] - sum_{p in Q_B}1[dp|b].                   (4)

Equivalently, when d|b it is 1 minus the number of Q_B primes dividing b/d; otherwise it is zero.

The complete target kernel is

    K(b)=sum_{all eligible base and star terms}u K_{B,d}(b).

### Pointwise target bound

For every positive integer b,

    K(b)<=(X(b)-1)_+.                                    (5)

**Proof.** A positive term in (4) has value one and requires b/d to contain no Q_B prime. Since d differs from B only by a power of q>=p_0, this says precisely that B contains every prime-power block of b below p_0 in full. Condition (1) then identifies B as the unique first-crossing root of b.

Thus at most one root B can have positive terms. Every term from another root is nonpositive and can be discarded in an upper bound. For the unique positive root, the base contributes at most h_B and all eligible positive stars contribute at most

    sum_{q>=p_0}w_q v_q(b/B).

Their total is X(b)-1. Eligibility can only remove nonnegative terms. If X(b)<=1 there is no positive root at all. This proves (5).

The argument counts all raw powers at targets. No truncation at source exponents is made.

## 3. Exact source decomposition and a weighted first-moment upper bound

For a carrier with parameters B,d,q,u, set T_d=M/d and

    X_{>=q}(t)=sum_{r in P,r>=q}w_r v_r(t).

Its total source contribution to (3), summed over the complete prefix, is exactly

    sum_{t<=T_d, gcd(t,product Q_B)=1}
          psi_u(X_{>=q}(t)).                             (6)

To verify this, n=dt has root B precisely when t contains no Q_B prime. In a base term the cofactor contains all occurrences after B. In a star term q^j, the factors of t at primes below q occur before the current occurrence and do not enter its right-tail load; its factors at q and above are exactly that tail. This remains true when q=p_0 and when q is repeated.

A nonzero source contribution has a positive right tail. Some prime at least q therefore remains in the cofactor, implying T_d>=q. This justifies the stated eligibility conditions: every omitted term has source contribution zero.

Summing (6) over the finite family gives exactly the left side of H_2:

    sum_{n<=M}(X(n)-2)_+.

Using (2), then dropping the coprimality restriction, gives the useful upper bound

    source contribution of (B,d,q,u)
       <=u sum_{t<=T_d}X_{>=q}(t)
       <=u T_d sum_{r in P,r>=q} w_r/(r-1).               (7)

This is a **weighted** reciprocal tail. The source may have arbitrary inactive cofactors; no false prime-count fibre bound is used.

## 4. Target average and a finite sufficient condition

On every interval I of length M, ordinary divisibility counts give

    sum_{b in I}K_{B,d}(b)
      >=T_d(1-sum_{p in Q_B}1/p)-(|Q_B|+1).              (8)

It follows from (5)--(8) that H_2 holds whenever every eligible carrier satisfies

    sum_{p in Q_B}1/p
      +sum_{r in P,r>=q}w_r/(r-1)
      +( |Q_B|+1 )/T_d <=1.                              (9)

A stronger but simpler condition is that for every p_0 in P,

    sum_{p in P,p<p_0}1/p
      +sum_{r in P,r>=p_0}w_r/(r-1)
      +(#{p in P:p<p_0}+1)/p_0 <=1.                      (10)

Indeed q>=p_0 and T_d>=q.

As a consistency check, if sum_{p in P}1/p<=1-epsilon and min P tends to infinity, then (10) eventually holds uniformly. The difference between 1/(p-1) and 1/p has vanishing total, and the rounding ratio is bounded by (pi(p_0)+1)/p_0, uniformly tending to zero for p_0>=min P. This validates the weighted certificate beyond the unit-weight special case.

This corollary is not a solution of the general problem: the unweighted prefix in (9) may be large even when the total weighted mean is at most one.

## 5. The exact-sieve variant has a unique positive budget too

One may replace (4) by the nonnegative exact kernel

    K^exact_{B,d}(b)
      =1[d|b]1[gcd(b/d,product Q_B)=1].                   (11)

The same unique-root proof gives sum u K^exact<=(X-1)_+.

It is tempting to compare each source expression (6) separately with u times the interval count in (11). Such an assertion would remove the unweighted first-order loss in (8). The next section shows that this local assertion is false, even at small weighted mean. One cannot simply apply a separate first-moment sieve bound to every root and declare the global sum proved.

## 6. Exact local counterexample, including weighted mean below one

Take

    P={2,3,5,7,11,13},
    w_2=1/10, w_13=1,
    w_3=w_5=w_7=w_11=1/1000.

The total weighted reciprocal mean is

    sum_p w_p/(p-1)=18435/100000=0.18435<1.

Let B=26. It is a first-crossing root with p_0=13 and h_B=1/10, since X(2)=1/10 and X(26)=11/10.

Set M=338=B*13 and use the base carrier d=B, so T_d=13. The source quotients coprime to Q_B={2,3,5,7,11} are 1 and 13. The latter has X_{>=13}(13)=1, and therefore the source expression (6) equals

    psi_{1/10}(0)+psi_{1/10}(1)=1/10.

It is the contribution of the actual source integer 338, whose raw load is 21/10.

Now take

    I={2939,...,3276},

an interval of exactly 338 integers. Its multiples of 26, after division by 26, form

    J={114,...,126}.

Every integer in J is divisible by one of 2,3,5,7,11. In particular, the only odd cases that are not immediately multiples of 3 or 5 are 119=7*17 and 121=11^2. Thus the exact target count in (11) is zero. The proposed local comparison would read 1/10<=0 and is false.

This does not refute H_2 or J_weak. The interval targets excluded from this root have different first-crossing roots because of additional earlier prime factors, so other carriers can compensate globally. Their last root prime need not be smaller: for example, the root of 26*114 is 156 and still has largest prime 13. The example does not satisfy actual optimality or minimal-obstruction balance. It refutes only the attempted independent exact-sieve inequality for each rooted fibre, including its proposed weighted-mean justification.

## 7. Exact remaining task

The canonical rooted-star construction resolves a genuine multiplicity issue: positive roots do not share the target budget, and repeated occurrences are handled exactly. It also converts the source bound to a weighted reciprocal tail rather than an unweighted count of possible final primes.

What it does not yet control is the aggregate transfer between roots caused by the missing earlier primes in the source cofactors. The local counterexample shows that this transfer cannot be ignored, even with weighted mean below one. A valid global proof must sum those source/target root changes with their signs, or use the actual tight demand rows to pay them once.

No such aggregate estimate is established here. In particular, neither (9) nor the separate exact-sieve comparison proves J_weak on the full minimal-obstruction class.
