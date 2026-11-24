# Global hot-set constraints and a sparse-optimal mean bound

## Status

The inequalities below hold for the full arithmetic setup. They impose no
small-core hypothesis, bound on the number of substantial weights, or gap
between prime sizes. They are necessary constraints on an actual optimum,
not a proof of J_weak. The exponential-moment argument and its constants
were independently checked by the analytic agent.

Let A contain m distinct integers in `[2,M]`, and let
`I={x+1,...,x+M}`, `x>=0`. All source primes are at most M. For clipped
weights `0<=w_p<=1`, put

    X(n)=sum_p w_p v_p(n),
    mu=sum_p w_p/(p-1),
    H={b in I:X(b)>1},  h=|H|,
    rho=m/M.

Write `F=sum_A X-sum_I(X-1)_+` for this weight vector's dual value.
At an optimal raw vector, F is the boxed raw LP value.

## 1. Every sufficiently small integer is cold

If an integer d has X(d)>1, every interval multiple of d lies in H.
Consequently

    floor(M/d)<=h,
    d>M/(h+1).                                          (1)

Thus X(d)<=1 for every integer d<=M/(h+1), not merely for selected source
divisors. Put `L0=floor(M/(h+1))`. Whenever p<=L0,

    w_p floor(log L0/log p)<=1.                          (2)

In particular, if w_p>eta and `s=floor(1/eta)+1`, then p^s>L0.
This consequence uses the actual number h of hot targets. Replacing h by
an upper bound is allowed but weakens it.

At a least-cardinality raw failure of budget c>2, the previously proved
deletion argument gives

    F=cm+e, 0<e<=log_2 M-c,
    h<=F=cm+O(log M), M<16m^2.                           (3)

Every hot target is fully selected in the paired optimum, so the bound on
h applies to the entire hot set, not just a chosen bank union.

## 2. A uniform exponential-moment estimate

Set `t=log(3/2)`. Then, for every clipped source-prime weight vector,

    (1/M) sum_{n=1}^M exp(t X(n)) <= exp(mu).             (4)

For a proof, expand the nonnegative multiplicative divisor coefficients

    exp(t X(n))=sum_{d|n} g(d),
    g(p^j)=exp(t w_p j)-exp(t w_p(j-1))>=0.

Ordinary multiple counts imply

    (1/M)sum_{n<=M}exp(tX(n))
      <=sum_d g(d)/d
       =product_p (p-1)/(p-exp(t w_p)).

Every Euler factor converges because exp(t w_p)<=3/2<2<=p. Convexity on
`0<=w<=1` gives `exp(tw)-1<=w/2`. Also
`p-exp(tw)>=p-3/2>=(p-1)/2`. Therefore

    log[(p-1)/(p-exp(tw))]
      =log[1+(exp(tw)-1)/(p-exp(tw))]
      <=w/(p-1).

Summation proves (4), uniformly in M, the weights, and their support.

By Jensen's inequality and distinctness of the actual sources,

    exp[(t/m)sum_A X]
      <=(1/m)sum_A exp(tX)
      <=(M/m)exp(mu).

Hence

    sum_A X <=(m/t)[log(M/m)+mu].                        (5)

No independence approximation for prime divisibility is used.

## 3. Uniform prefix-mean error with all raw powers

Put

    mu_M=(1/M)sum_{n<=M}X(n).

For M>=2,

    0<=mu-mu_M<=e_M,
    e_M=[3 pi(M)+sqrt(M) log_2 M]/M=O(1/log M).          (6)

Indeed, for `J_p=floor(log M/log p)`, the discrepancy for one prime is

    sum_{j<=J_p}[p^(-j)-floor(M/p^j)/M]
       +sum_{j>J_p}p^(-j)
      <=(J_p+2)/M.

The tail bound uses `p^(J_p+1)>M` and `(1-1/p)^(-1)<=2`.
Summing is legitimate because w_p<=1. The total number of prime powers
at most M is at most `pi(M)+sqrt(M)log_2 M`; this proves the displayed
explicit bound. Its asymptotic form uses the ordinary Chebyshev bound.

Equation (6) is a prefix estimate only. It does not truncate target
valuations, which may be much higher at an unbounded shift.

## 4. The sparse-optimal weighted mean is at most one asymptotically

The affine hinge bound and ordinary prime-power multiple counts give

    sum_I(X-1)_+ >=sum_I X-M>=sum_{n<=M}X(n)-M.

Combine this with (5)--(6). Whenever rho<t,

    (1-rho/t)mu
       <=1-F/M+(rho/t)log(1/rho)+e_M,                   (7)

and therefore

    mu <=[1-F/M+(rho/t)log(1/rho)+e_M]/(1-rho/t).        (8)

At an actual raw-minimal failure, F>cm, so

    mu <=[1-c rho+(rho/t)log(1/rho)+e_M]/(1-rho/t).

Along any such sequence with rho=m/M->0,

    mu <=1+O(rho log(1/rho))+O(1/log M)=1+o(1).         (9)

The constants are absolute apart from the harmless fixed budget c. For
an integer-minimal failure with only `F>cm-r`, the same proof adds `r/M`
to the numerator; this still tends to zero under the known row bound.

This is an aggregate necessary condition on every optimal clipped
vector in the sparse-source regime. It neither proves the desired
hot-source density transfer nor excludes a dense-source regime.

## 5. Full capped-core moments have small arithmetic discrepancy

Let E be any finite prime set with k=|E| and define the auxiliary load

    Y(n)=sum_{p in E}min(w_p v_p(n),1).

This caps each prime contribution at one; it does NOT truncate at a
source exponent. Let

    beta_{p,j}=min(w_p j,1)-min(w_p(j-1),1)>=0.

The sum over all j is one for w_p>0, and zero when w_p=0. Expanding an
integer power Y^q as an ordered sum of products of its divisibility
indicators gives nonnegative coefficients on indicators
`1[lcm(d_1,...,d_q)|n]`. Their total coefficient mass is at most k^q.
Every such indicator has interval-minus-prefix count between zero and
one. Therefore, for every integer q>=1,

    0<=sum_{b in I}Y(b)^q-sum_{n<=M}Y(n)^q<=k^q.        (10)

In particular the first and second moment errors are at most k and k^2.
For the actual demand core, `k^2=O(m/log m)=o(m)`.

All target powers are included in this identity. Even if the full
per-prime cap requires many levels, their coefficient mass is one; the
bound does not count those levels or silently omit them. Equation (10)
is about the capped auxiliary load, not about raw powers themselves.

## 6. Exact obstacle to using two moments as a hinge proof

Equal first two moments do not determine the needed hinge. An actual
integer-interval example is

    Y(n)=1[11|n]+1[13|n]+1[17|n],
    M=221, I={2313,...,2533}.

The three prime counts are 20,17,13 in both the prefix and I. Each of
the three pair products 143,187,221 has exactly one multiple in each
interval. Thus

    sum_prefix Y=sum_I Y=50,
    sum_prefix Y^2=sum_I Y^2=56.

The prefix has three separate pair positions and no triple position.
In I, all three pair counts occur at the single triple multiple 2431.
Consequently

    sum_prefix(Y-1)_+=3,
    sum_I(Y-1)_+=2.                                    (11)

This is not a counterexample to Problem 708 or J_weak. It identifies the
specific information missing from a proposed proof using only (10) for
q=1,2. No uniform hinge conclusion is claimed from those moment bounds.

## 7. Sparse reduction to bounded heavy occurrence count per source

Fix a weight threshold `0<eta<=1`, and put `s=floor(1/eta)+1`.
The independently audited Bonferroni bound in
`../analytic/SPARSE_HOT_BONFERRONI.md` gives, on every actual sparse
obstruction sequence and with `z=M^[1/(2(s+1))]`,

    mu_low=sum_{p<=z,w_p>=eta}1/p
           <=C_{c,s} rho^(1/s).                         (12)

The following elementary divisor estimate converts this harmonic mass
bound into a WEIGHTED deletion bound, without losing a factor log M.
For any finite prime set Q, any integer t>=1, and
`mu_Q=sum_{p in Q}1/p`, let `Omega_Q(a)=sum_{p in Q}v_p(a)`. Then

    sum_{a<=M, Omega_Q(a)>=t} X(a)
       <= M(t+mu) mu_Q^t,                               (13)

and the number of such integers is at most `M mu_Q^t`.

To prove this, let D_t consist of the distinct Q-smooth monomials of
total degree t, with repeated primes allowed. Every exceptional a is
divisible by at least one d in D_t. Additivity gives

    X(dk)=X(d)+X(k),  X(d)<=t,
    sum_{k<=N}X(k)<=N mu.

Thus the weighted union bound is at most

    sum_{d in D_t,d<=M} sum_{k<=M/d} X(dk)
      <=M(t+mu)sum_{d in D_t}1/d
      <=M(t+mu)mu_Q^t.

The final inequality holds because the expansion of `(sum_Q 1/p)^t`
contains every unordered degree-t monomial with a coefficient at least
one. Repetitions therefore cause no missing multiplicity.

Apply (13) to the low heavy primes in (12). Taking t=2s gives discarded
weighted demand `O_{c,s}(M rho^2)=o(m)`. Taking the smaller t=s+1 also
works and improves the occurrence bound:

    discarded weighted demand
       =O_{c,s}(m rho^(1/s))=o(m),                      (14)

using the independently proved `mu<=1+o(1)` from Section 4. The number
discarded is o(m) as well. Every remaining source has at most s low
heavy occurrences. Every prime above z contributes more than log z to
its logarithm, so a source at most M has at most `2s+1` such occurrences.
Consequently every retained source has at most

    3s+1                                                (15)

heavy occurrences in total. The global number of heavy PRIME VALUES is
still unrestricted. The threshold eta is fixed before the limit.

This is a necessary reduction of a hypothetical unrestricted sparse
obstruction, not an assumed restricted source class. It does not by
itself give a new covering theorem. In particular:

* bounded heavy occurrences per source do not imply that their shared
  support breaks into disjoint bounded components;
* a gluing lemma requiring `eta<=c_delta/(K+1)` cannot simply be invoked
  with `K` of order `1/eta`, since that parameter choice is circular;
* the complementary dense-source regime has not been excluded.

The cold-prefix bound additionally forces every heavy prime to tend to
infinity along the sparse sequence. This may help a subsequent
conditioning estimate, but no such estimate is asserted here.

## Remaining obligation

The cold-prefix restriction, sparse mean bound, and capped moment
identities are global constraints, not a replacement of the full target
by a restricted source class. A proof must still combine actual source
demands, overlapping hot banks, and the single target hinge uniformly
over all scales. Neither a sparse-source density-transfer theorem nor
the complementary dense-source hinge estimate has been established in
this note.
