# Aggregate prime blocks and covers of disjoint support components

Date: 2026-11-23.

## Status and two distinct conclusions

The weighted block argument below passes a direct audit of the proposed
root construction. Its integer component corollary was independently
checked by the parent, analytic, and computation agents.

The auxiliary weighted theorem allows a common diffuse load and many
disjoint blocks of substantial weights. The source-class corollary is
different: every source is supported entirely within one of a partition
of disjoint prime blocks. In that corollary no common prime is shared
between blocks, and no restrictions are placed on the weights.

The argument in Section 8 gives an integer consequence for block size
k(M)=o(log M), but a subsequent scope check shows that this class already
has eventual EXACT 2n from the inherited quadratic gate and an elementary
Rankin estimate. Section 8.1 proves that stronger dependent consequence.
The asymptotic route is retained as a correct but redundant argument,
not as a newly uncovered source class. Neither argument yields a theorem
from merely bounding omega(a) for each individual source.

## 1. Weighted block theorem

For every epsilon>0 there is c_epsilon>0 with the following property.
Fix k>=1 and put

    eta=c_epsilon/(k+1),
    B_{epsilon,k}=4^k binom(k+floor(1/eta),k).

Let P be a finite set of light primes with 0<=w_p<=eta, and let
F_1,...,F_b be pairwise disjoint nonempty prime blocks, each disjoint
from P and of size at most k. Every weight on every F_i is greater
than eta; these weights may be arbitrary nonnegative real numbers.
Define

    V(n)=sum_{p in P}w_p v_p(n),
    X_i(n)=sum_{p in F_i}w_p v_p(n),
    X(n)=V(n)+sum_i X_i(n).

Let A be distinct sources in [2,M], each using primes from at most one
of the F_i. Arbitrary powers are allowed, and primes outside all the
listed weighted sets cause no problem. Then for every positive M-term
interval I,

    sum_{a in A}(X(a)-2-epsilon)_+
      <=sum_{b in I}(X(b)-1)_+ + b B_{epsilon,k}.          (1)

Blocks unused by every source may be discarded before counting b:
discarding them leaves the source loads unchanged and can only decrease
the target hinge. The case of no substantial block has zero error.
For an epsilon-dependent constant D_epsilon>=1,

    B_{epsilon,k}<=D_epsilon^k.                           (2)

This is a weighted source-specific theorem. It is not an integer
source-class theorem when the common light primes can occur across
different blocks, because an arbitrary dual vector need not be diffuse
on those shared primes.

## 2. Inherited conditional input and the large-mean alternative

It is enough to consider 0<epsilon<=1. Put ell=1+epsilon and c=2+epsilon.
The already audited conditional diffuse theorem supplies c_epsilon so
that eta=c_epsilon/(k+1) has the following property.
If

    mu_V=sum_{p in P}w_p/(p-1)<=1+epsilon/2,

then for every finite prime set F disjoint from P with |F|<=k, every
real length T>0, every positive interval J of that length, and s>=0,

    #{a<=T:(a,product F)=1,V(a)>s+ell}
       <=#{b in J:(b,product F)=1,V(b)>s}.                (3)

In particular F may be empty. The parameter eta can also be chosen
at most epsilon^2/128. Its uniform linear dependence on 1/(k+1)
was proved in the controlled-exception theorem of the preceding
investigation, using the conditional sieve error

    e_k(u)=3^k e(u/2)+3*4^k*2^(1-u/2).

If mu_V>=1+epsilon/2 after deleting light primes greater than M,
the elementary high-mean capped-mass estimate gives

    sum_{a<=M}min(V(a),2)>=M.

Adding nonnegative block loads preserves this inequality. Ordinary
prime-power counting then gives H_2 for the full raw load X, and
therefore proves (1) without any error or block condition.
Deleted primes contribute no source load and can be restored on the
target side. Thus it remains to prove (1) under the low-mean condition
in (3). These inherited statements are precisely the conditional
comparison and high-mean alternative already proved in the prior
analytic notes; no new unproved input is being assumed.

## 3. Exact comparison of each capped block increment

Cap the WHOLE block:

    U_i(n)=min(X_i(n),1),     T_i(n)=X_i(n)-U_i(n).

In particular 0<=U_i<=1 even if a source contains many distinct
primes from that block. For h equal to c or 1, define

    D_{h,i}(n)=(V(n)+U_i(n)-h)_+-(V(n)-h)_+.

Every D_{h,i} is nonnegative. We claim

    sum_{a<=M}D_{c,i}(a)<=sum_{b in I}D_{1,i}(b).          (4)

Fix i and decompose each integer uniquely as n=d t, where d is its
exact F_i-smooth part and t is coprime to product F_i.
Because P and F_i are disjoint,

    V(d t)=V(t),     U_i(d t)=U_i(d).

At a fixed d<=M, the source and target quotient intervals have the
same real length M/d, and

    D_{h,i}(d t)
       =integral_0^{U_i(d)} 1[V(t)>h-v] dv.

For every v in this integration range, s=1-v>=0 and
c-v=s+ell. Apply (3), excluding F_i, to the two quotient
intervals, then integrate. Summing over d<=M proves (4);
target integers with exact F_i-part greater than M contribute
nonnegatively and need not be used.

The real-length formulation in (3) avoids an unmentioned rounding
of quotient endpoints. Negative target thresholds never occur,
because the whole block was capped at one.

## 4. Source identities and shared target capacity

For each source, at most one U_i is nonzero. Thus on A,

    (V+sum_i U_i-c)_+
      =(V-c)_+ +sum_i D_{c,i}.                            (5)

Apply (3) with F empty and integrate over s>=1 to compare the base
hinge on the full prefix and target. Use distinctness to enlarge
the source base and each nonnegative increment to the full prefix,
and use (4). This gives

    sum_{a in A}(V(a)+sum_i U_i(a)-c)_+
      <=sum_{b in I}[(V(b)-1)_+ +sum_i D_{1,i}(b)].

For any x>=0 and z_i>=0,

    (x-1)_+ +sum_i[(x+z_i-1)_+-(x-1)_+]
      <=(x+sum_i z_i-1)_+.                               (6)

If x>=1 this is equality. Otherwise put t=1-x>0 and use
sum_i(z_i-t)_+<=(sum_i z_i-t)_+.
Hence

    sum_{a in A}(V(a)+sum_i U_i(a)-c)_+
      <=sum_{b in I}(V(b)+sum_i U_i(b)-1)_+.              (7)

The common diffuse base is counted only once. This is the exact
capped-block inequality, before restoring the raw block tails.

## 5. Uniform variation of one aggregate cap

Fix a block F of f<=k primes, all with weights greater than eta.
Let X_F be its raw load and U_F=min(X_F,1).
For 0<=v<1, the event X_F>v is unchanged if each individual
coordinate w_p v_p(n) is capped at one.

Set b_p=ceil(1/w_p), and on the exponent lattice define

    g_v(e)=1[sum_{p in F}min(w_p e_p,1)>v].

It is constant in coordinate p after exponent b_p. Its finite
multidimensional difference coefficients are

    a_j(v)=sum_{delta in {0,1}^f}
               (-1)^|delta| g_v(j-delta),

where g_v is defined as zero when any coordinate is negative.
Telescoping gives

    g_v(v_p(n):p in F)
       =sum_j a_j(v) 1[product_{p in F}p^(j_p) divides n].

The expansion is finite: a_j=0 if some j_p>b_p.
Each coefficient has absolute value at most 2^f.
If a_j is nonzero, put z_p=max(j_p-1,0).
Then g_v(z)=0; otherwise every nonnegative vertex of the difference
has value one and the alternating sum cancels. The all-zero
index also has coefficient zero, since g_v(0)=0.

Since z_p<b_p, the capped value at z_p is w_p z_p.
Thus sum_p z_p<=v/eta. There are
binom(f+floor(v/eta),f) possible z-vectors. Each zero coordinate
permits at most two values of j_p, and positive coordinates
determine j_p uniquely. Therefore

    sum_j |a_j(v)|
      <=4^f binom(f+floor(v/eta),f)
      <=B_{epsilon,k}.                                   (8)

For each divisor in this finite expansion, the number of its
interval multiples differs from its prefix count by at most one.
Consequently

    |sum_{b in I}1[X_F(b)>v]-sum_{a<=M}1[X_F(a)>v]|
      <=B_{epsilon,k}.

Integrate over v in [0,1], using
U_F(n)=integral_0^1 1[X_F(n)>v] dv. It follows that

    |sum_{b in I}U_F(b)-sum_{a<=M}U_F(a)|
      <=B_{epsilon,k}.                                   (9)

The bound has no dependence on M, the interval shift, the actual
prime values, or the sizes of the weights above eta.

## 6. Restoring all raw block tails simultaneously

The linear raw block load has its interval sum at least its prefix
sum, by prime-power counting. Since T_i=X_i-U_i, equation (9) gives

    sum_{a<=M}T_i(a)<=sum_{b in I}T_i(b)+B_{epsilon,k}.

Let U=sum_i U_i and T=sum_i T_i. Pointwise,

    (V+U+T-c)_+<=T+(V+U-c)_+,
    (V+U+T-1)_+=T+(V+U-1)_+.

For the second identity, T>0 forces at least one U_i=1.
By distinctness and nonnegativity, sum_A T<=sum_{a<=M}T.
Combine these facts with (7) and the preceding tail bounds to
obtain (1).

Finally, for k>=1, floor(1/eta)<=2k/c_epsilon, and the standard
binomial bound gives

    B_{epsilon,k}
      <=[4e(1+2/c_epsilon)]^k.

This proves (2), with a constant depending only on epsilon.

## 6.1 Two-prime blocks have zero tail error

There is an exact improvement when every substantial block has size at
most two. For two distinct primes p,q and arbitrary weights a,b>=0, put

    T(n)=(a v_p(n)+b v_q(n)-1)_+.

Then for every positive M-term interval,

    sum_{n<=M}T(n)<=sum_{n in I}T(n).                     (9a)

To prove this, define f(i,j)=(a i+b j-1)_+ on nonnegative integer
exponents. The axis differences f(i,0)-f(i-1,0) and
f(0,j)-f(0,j-1) are nonnegative. For i,j>=1 the mixed difference

    f(i,j)-f(i-1,j)-f(i,j-1)+f(i-1,j-1)

is also nonnegative. This is the increasing-increment property of
the convex hinge function, with increments a and b. Since f(0,0)=0,
two-dimensional telescoping expresses T(n) as a nonnegative linear
combination of divisibility indicators 1[p^i q^j divides n].
Every such indicator has interval sum at least its prefix sum,
proving (9a). For any finite prefix and interval the relevant
valuation ranges are finite, so no convergence issue arises.

The same statement for a one-prime block is ordinary prime-power
counting. Therefore every block tail in Section 6 has exact prefix
dominance when |F_i|<=2. Equation (7) then restores all tails with
NO error. In this case the weighted theorem strengthens to

    sum_{a in A}(X(a)-2-epsilon)_+
      <=sum_{b in I}(X(b)-1)_+,

with eta chosen for two exclusions and independently of the number
of blocks. The source restriction is still that it uses at most
one substantial block, in addition to the shared diffuse load.

This does not extend to all three-prime block tails: the example
F={11,13,17}, M=221, I={2313,...,2533}, with unit weights, has
prefix tail sum five and interval tail sum four. Thus exact
tail dominance beyond two coordinates cannot be assumed.

## 7. A uniform bound for one small prime support

Let A be any distinct sources in [2,M] whose combined prime support
has size at most k. For any clipped raw dual vector, put every
coordinate of weight at most eta into V, and all remaining
coordinates into a single substantial block F.

The source block condition is then automatic. Applying (1) with
at most one block and using the raw dual identity gives

    L_raw(A,I)<=(2+epsilon)|A|+B_{epsilon,k}.

An optimal boxed vertex has at most k fractional positions.
Rounding them upward therefore gives

    tau(A,I)<=(2+epsilon)|A|+B_{epsilon,k}+k.               (10)

This statement is uniform over actual prime values and all positive
ambient intervals with M>=max A. It is also the R-empty case of
the upgraded aggregate-core theorem.

## 8. Disjoint prime-support components of size o(log M)

Let the source-prime set admit a partition into disjoint blocks
P_1,...,P_s, each of size at most k=k(M), such that every source
has ALL its prime factors in a single block. Group the sources
accordingly as A_i, with n_i=|A_i|, and discard empty groups.
Let n=sum_i n_i.

Fix epsilon>0. If n_i<=sqrt(M)/4, the known ambient quadratic
theorem gives an exact cover of A_i using at most 2n_i positions
of the SAME original interval I.

For every remaining group, use (10). There are fewer than
4n/sqrt(M) such groups. Choose one cover for each group and take
their union. This union is a cover of all of A even when the
chosen subsets overlap: each prime p is demanded by exactly one
group, and the union contains that group's full cover. No other
group adds source demand at p.

Consequently the quantitative estimate is

    tau(A,I)<=(2+epsilon)n
                +[4n/sqrt(M)](B_{epsilon,k}+k).           (11)

If k(M)=o(log M), then B_{epsilon,k}<=D_epsilon^k=M^{o(1)}
and k=M^{o(1)}, so the last term is o(n), uniformly in the
number and sizes of the blocks, their prime values, and the shift.
Take epsilon fixed first and then arbitrarily small. Since n tends
to infinity only if M tends to infinity, (11) yields

    tau(A,I)<=(2+o(1))n.                                  (12)

No prime-size separation is used in this result. The quadratic gate
is essential here for groups with few sources, so their individual
additive errors are not paid.

## 8.1 Scope correction: the component class already has exact 2n

For any prime set Q of size at most k, Rankin's inequality at exponent
1/4 gives

    Psi_Q(M)<=M^(1/4) product_{p in Q}(1-p^(-1/4))^(-1).

List its primes increasingly as p_j, so p_j>=j+1. Since
-log(1-x)<=x/(1-x) and p^(-1/4)<=2^(-1/4), one has

    log product_{p in Q}(1-p^(-1/4))^(-1)
      <=[1/(1-2^(-1/4))]sum_{j<=k}(j+1)^(-1/4)
      <=C k^(3/4),
    C=4/[3(1-2^(-1/4))].

This estimate is uniform over the actual prime values. For k=o(log M),
it implies

    n_i<=Psi_{P_i}(M)<=M^(1/4+o(1))<sqrt(M)/4

for EVERY component, once M is sufficiently large. The inherited
quadratic theorem therefore gives an exact 2n_i cover for every group.
The prime-disjoint union argument then yields tau(A,I)<=2n exactly.

Thus there are eventually no large groups requiring the additive
fractional estimate in Section 8. The integer class k=o(log M) must
not be advertised as a new consequence unavailable from earlier
results. The weighted shared-diffuse-load theorem in Sections 1--6
remains a valid auxiliary statement, with different hypotheses.

## 9. Scope and comparison with the unrestricted core

The component condition is equivalent to saying that the connected
components of the prime co-occurrence relation generated by the
sources contain at most k(M) prime values. A bound on the number
of primes in EACH individual source does not imply this condition:
successive sources may connect arbitrarily many different primes.

The weighted theorem in Section 1 is more flexible about a shared
diffuse load, but it applies to a weight vector satisfying that
diffuseness assumption. The dependent integer component conclusion
applies to every dual vector because the entire source support is
partitioned into small components; Section 8.1 shows that the
inherited long-interval theorem already settles it exactly.

A general minimal counterexample may have one connected prime
support with a growing shared dense core. Neither (1) nor (12)
eliminates that case. These are restricted upper-bound theorems,
not a claim that unrestricted Erdős 708 is solved.
