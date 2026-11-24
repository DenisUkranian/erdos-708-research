# Cold-bank credit from any uniform covering constant

24 November 2026. The local credit below is proved for arbitrary raw prices
and all shifts. No joint estimate closing the dense branch or the general
Erdős 708 asymptotic is obtained.

## 1. Scaled hinge transfer does not need a price bound

Assume a known uniform covering constant C0: every finite set S of distinct
integers in [1,N] can be covered in the product-divisibility sense by at
most C0*|S| distinct integers from any N-term positive interval J. The same
argument works directly from the corresponding uniform raw LP bound.

Let Y(t)=sum_p u_p v_p(t), with arbitrary nonnegative prices u_p, and let b>0.
There is no assumption u_p<=b. Apply the cover bound to

    S={t<=N:Y(t)>C0*b}.

If B is its cover, product divisibility gives sum_S Y<=sum_B Y. Since
Y(s)<=b+(Y(s)-b)_+ for each selected s,

    sum_S Y <= b*C0*|S| + sum_J (Y-b)_+.

Therefore

    sum_(t<=N) (Y(t)-C0*b)_+ <= sum_(s in J)(Y(s)-b)_+.   (1)

This is homogeneous raw duality. No primewise overflow trimming or
replacement of the original valuation rows is necessary.

## 2. One cold divisor pays its whole source cluster

Let X(t)=sum_p w_p v_p(t), let I be any interval of M positive consecutive
integers, and let

    A={a<=M:X(a)>c},   c=2+delta.

Fix a divisor g<=M with x=X(g)<1, and put b=1-x and N=floor(M/g).
The quotient set {s:g*s in I} consists of N or N+1 consecutive positive
integers, so it contains an N-term interval J. Complete additivity is
exact even if g and s share primes:

    X(g*s)=x+X(s).

Suppose epsilon>0 and

    c-epsilon-x >= C0*(1-x),

equivalently

    1-x <= (1+delta-epsilon)/(C0-1).                   (2)

Using (1) on J, monotonicity in the source threshold, and the nonnegative
additional quotient position if present, yields

    sum_(b' in I:g|b') (X(b')-1)_+
      >= sum_(a<=M:g|a) (X(a)-c+epsilon)_+
      >= sum_(a in A:g|a) (X(a)-c) + epsilon*|A_g|,    (3)

where A_g={a in A:g|a}. This proof is uniform in M, the shift, the divisor,
all weights, all prime powers, and the number of active coordinates.
Neither global optimality nor density is used.

The same conclusion applies to any assigned subcluster S subset A_g,
because the right side for S is at most the displayed full-cluster sum.
Thus merging several source clusters into a common divisor g satisfying
(2) is legitimate if their target capacity is paid once through bank g.

## 3. What the local credit does not establish

For multiple divisors g_i, the left side of (3) repeatedly uses the same
capacity (X(b')-1)_+ whenever several g_i divide one target b'. Pairwise
merging whenever X(gcd(g_i,g_j)) reaches the threshold in (2) does not make
the remaining bank credits pointwise summable.

Here is an exact arithmetic incidence demonstration. Take C0=12,
delta=1/10, epsilon=1/20. The cold merge threshold is

    x0=1-(1+delta-epsilon)/(C0-1)=199/220.

Choose twelve distinct actual primes and give each price 199/2200. Let
B be their product, and take the 66 divisors g consisting of any ten of
the twelve primes. Then

    X(g)=x0,   X(gcd(g,g'))<=9*(199/2200)<x0 (g!=g'),
    X(B)=597/550,   (X(B)-1)_+=47/550.

Every g is eligible for (3), with equality in its threshold condition.
No pair can be merged by the proposed x0-gcd rule. Yet the target B lies
in all 66 banks, and every local target expression at B equals 47/550.
Adding them would spend 66 copies of the same positive target capacity.

The example can be placed in any sufficiently long actual interval that
contains B. It is not asserted to be a positive global optimizer. Its
purpose is to disprove the pointwise additive step after pairwise cold
merging. It does not disprove (3), the desired raw asymptotic, or a joint
argument that additionally uses the original whole-row balances.

More generally, take many primes of equal price x0/k and all their k-fold
products as anchors. Every distinct pair has gcd-load below x0, while one
target containing all primes can meet an arbitrarily large anchor family.
Thus no absolute overlap bound follows from that pairwise stopping rule.

## 4. Remaining dense-branch obligation

The local raw constant supplies a genuine cold-divisor merge credit. It
does not supply a simultaneous assignment of the original target hinge to
all remaining clusters. The needed new arithmetic estimate must use
actual bank unions and the true optimum's whole-prime rows to control this
joint assignment, including boundary targets with X=1. No such estimate
was proved in this attempt.

In particular, no statement J_(2+delta)=o(M) for all dense full tails is
claimed. The local theorem is not presented as a new restricted-class
replacement for the requested general result.
