# A global substantial-weight mass bound from sparse hot targets

## Status

This note proves an arithmetic necessary inequality for every clipped weight vector on an interval. Applied to an actual minimal raw obstruction, it controls the harmonic mass of all substantial weights on a quantitatively specified lower prime range. It makes no small-support, few-heavy-coordinate, or prime-gap assumption about the source set.

The inequality does not prove J_weak. In particular, the complementary prime ranges remain uncontrolled. The final section records the exact obstruction to extending this argument by dropping its rounding term.

## 1. General interval setup

Let I be a positive interval of M consecutive integers. Let w_p be nonnegative weights with finite support, and define

    X(n)=sum_p w_p v_p(n),
    H={b in I:X(b)>1},
    h=|H|.

Fix eta>0 and an integer s>=1 satisfying s eta>1. In the intended clipped application 0<eta<=1 and

    s=floor(1/eta)+1>=2.

For a cutoff z>=2, let

    P_eta(z)={p<=z:w_p>=eta},
    k=|P_eta(z)|,
    mu=sum_{p in P_eta(z)}1/p.

Put

    E_s(k)=binom(k,s)+(s+1)binom(k,s+1),

with binomial coefficients zero when the lower index exceeds k.

### Main finite inequality

For every such weight vector and interval,

    min(mu,1/2)
      <= s[(h+1)/M]^(1/s)
         +[2 s! (h+E_s(k))/M]^(1/s).                    (1)

There is no hypothesis on the sizes or number of primes outside P_eta(z), nor on the interval shift. All raw powers remain in X.

## 2. First-hot-number bound

For each p in P_eta(z), every multiple of p^s is hot because
s w_p>=s eta>1. There are at least floor(M/p^s) such multiples in I. Hence

    floor(M/p^s)<=h,
    p^s>M/(h+1),
    1/p<[(h+1)/M]^(1/s).                                (2)

More generally, every integer d with X(d)>1 satisfies

    floor(M/d)<=h.

Thus X(d)<=1 for all d<=M/(h+1). The strict boundary is included: if d<=M/(h+1), its bank contains at least h+1 targets.

If P_eta(z) is empty, (1) is immediate. Otherwise let

    a=max_{p in P_eta(z)}1/p.

Equation (2) bounds a by the first term's scale.

## 3. A one-sided Bonferroni polynomial

For any nonnegative integer N,

    1[N>=s] >= binom(N,s)-(s+1)binom(N,s+1).             (3)

For N<s both sides are zero. For N=s the right side is one. For N>=s+1 it equals binom(N,s)(s+1-N), which is nonpositive.

Choose a subset Q of P_eta(z) with reciprocal mass mu' satisfying

    mu'<=1/2,
    mu'>=min(mu,1/2)-a.                                 (4)

If mu<=1/2, use the full set. Otherwise accumulate primes until the first crossing of 1/2 and use the preceding partial set, or the exact partial set if equality occurs. Its missing mass is at most the largest summand a.

For b in I, let N_Q(b) be the number of distinct primes of Q dividing b. If N_Q(b)>=s, then X(b)>1. Therefore h is at least the sum over I of the polynomial on the right of (3).

Let e_j denote the j-th elementary symmetric polynomial in the numbers 1/p, p in Q. Ordinary divisibility counts give

    sum_{b in I}binom(N_Q(b),s)
        >=M e_s-binom(|Q|,s),
    sum_{b in I}binom(N_Q(b),s+1)
        <=M e_{s+1}+binom(|Q|,s+1).

These inequalities remain valid when a product of primes exceeds M: the resulting floor or ceiling error is still at most one. Hence

    h>=M[e_s-(s+1)e_{s+1}]-E_s(k).                      (5)

No independence assumption about prime divisibility has been used.

## 4. Lower bound for the symmetric-polynomial expression

By counting an additional distinct coordinate,

    (s+1)e_{s+1}<=mu' e_s.

Since mu'<=1/2,

    e_s-(s+1)e_{s+1}>=(1/2)e_s.                         (6)

The ordered-product formula for e_s gives

    s! e_s >=(mu'-(s-1)a)_+^s.

Indeed, at every stage of an ordered selection of s distinct coordinates, the already excluded reciprocal mass is at most (s-1)a. When the displayed lower bound is positive, each remaining sum is at least that amount; otherwise the claim is trivial.

Using (4),

    e_s >=[min(mu,1/2)-s a]_+^s/s!.

Substitute into (5)--(6):

    h+E_s(k)
       >=M [min(mu,1/2)-s a]_+^s/(2s!).

Taking s-th roots and then applying (2) proves (1).

## 5. Consequence at an actual minimal raw obstruction

Suppose A is a fixed-ambient inclusion-minimal raw failure at a fixed budget c>2, with m=|A|. Let F=L_raw(A,I)>c m and choose an optimal clipped dual vector.

Complementary slackness makes every member of H fully selected, so

    h<=F.

A fractional cover of a deletion costs at most c(m-1). Repairing the removed source by at most Omega(a)<=log_2 M prime units gives

    F<=c(m-1)+log_2 M.                                  (7)

The ambient quadratic theorem gives M<16m^2, hence m>sqrt M/4 and log M=o(m). Consequently h=O_c(m).

For fixed eta, take s=floor(1/eta)+1 and

    z=M^[1/(2(s+1))].

Chebyshev's prime-count bound yields

    k<=pi(z)=O_s(z/log M),
    E_s(k)=O_s(k^(s+1))
          =O_s(sqrt M/(log M)^(s+1))
          =o_s(m).                                     (8)

Thus the finite inequality (1) implies the global necessary bound

    min( sum_{p<=M^[1/(2(s+1))], w_p>=eta}1/p, 1/2 )
       <=C_{c,s}(m/M)^(1/s)                             (9)

for all sufficiently large m, uniformly in the actual source set, prime values and interval shift.

In particular, along any obstruction sequence with m/M->0, the minimum in (9) is eventually attained by the first argument, and

    sum_{p<=M^[1/(2(s+1))], w_p>=eta}1/p
       =O_{c,s}((m/M)^(1/s))->0.                        (10)

The same deduction applies to an integer-minimal obstruction once an optimal raw vector and the already proved F=O_c(m) bound are used. No source-class restriction has been inserted.

This is a mass restriction on ALL substantial coordinates in that range, not a restriction to only finitely many such coordinates.

## 6. Relation to the sparse weighted mean

A separate global calculation gives the following useful companion estimate. For t=log(3/2), the positive divisor expansion of exp(tX(n)) implies

    (1/M)sum_{n<=M}exp(tX(n))<=exp(mu_w),
    mu_w=sum_p w_p/(p-1),

for clipped source-prime weights. Jensen's inequality over the actual distinct source set gives

    sum_{a in A}X(a)
       <=(m/t)[log(M/m)+mu_w].

Together with the affine hinge lower bound and the uniform prefix-mean error, this forces mu_w<=1+o(1) when m/M->0 at an actual minimal obstruction. That calculation has been independently checked; its full proof is in the computation agent's companion note.

The weighted-mean bound and (10) concern different quantities. Equation (10) controls an unweighted reciprocal sum over all coordinates above a fixed weight threshold. Neither estimate gives the missing full target hinge comparison by itself.

## 7. What the argument does not justify

The rounding term E_s(k) in (1) is essential to this proof. Replacing z by the largest source prime without controlling that term would introduce errors of order k^(s+1), which can be much larger than m. The fact that the same hot target may support many prime tuples does not permit those errors to be silently dropped.

The bound also does not control substantial weights on primes above M^[1/(2(s+1))]. Distinctness and the source size constrain their joint occurrences, but no valid global summation across all those scales has been proved here.

When m/M stays bounded away from zero, (9) may be quantitatively uninformative. One cannot conclude that every minimal obstruction lies in the sparse regime.

Therefore J_weak remains unproved. This note supplies a genuine aggregate arithmetic inequality forced by sparse hot targets; it does not turn that necessary condition into the requested coefficient-two conclusion.
