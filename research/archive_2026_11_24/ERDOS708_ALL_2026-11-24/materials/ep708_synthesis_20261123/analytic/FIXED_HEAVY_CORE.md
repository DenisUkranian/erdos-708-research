# A fixed number of substantial weights and an arbitrary diffuse remainder

## Status

This is a partial result developed jointly with the parent research agent. A separate internal audit checked the exceptional-prime sieve, the conditional carrier comparison, and the exact-part decomposition without finding a substantive error. It is not a proof of unrestricted Erdős problem 708 or a claim of external verification. Section 6 gives a limited quantitative growing-core extension, not an estimate for an unrestricted number of exceptional weights.

The argument uses the fundamental lemma of the combinatorial sieve and the partial prime-power carrier construction in `DIFFUSE_RAW_WEIGHTS.md`. All additional steps, including their uniformity in the exceptional primes, are written out here.

## Theorem

For every epsilon>0 and nonnegative integer k, there exists eta_{epsilon,k}>0 such that the following holds. Let P be any finite set of primes, with weights 0<=w_p<=1. Suppose there is an exceptional set E of at most k primes such that

    w_p <= eta_{epsilon,k} for every p outside E.

For every positive integer M and every interval I of M consecutive positive integers,

    Delta_{2+epsilon}(M,I,w)
      := sum_{a<=M}(X_w(a)-2-epsilon)_+
           - sum_{b in I}(X_w(b)-1)_+
      <= 2^{k+1}(1+log_2 M)^{k+1}.                         (T)

The constant eta depends only on epsilon and k. The bound is uniform in the actual exceptional primes, the diffuse support, all weights, M, and the interval shift.

There is also the sharper bound

    Delta_{2+epsilon}
      <= 2^{|E|+1} sum_{h<=M, h E-smooth}(Z(h)-1)_+,          (T')

where Z(h)=sum_{p in E}w_p v_p(h). The integer h=1 is included and contributes zero.

Proof convention: discard all primes greater than M at the outset, before computing the diffuse mean or making the case split below. They contribute nothing to the prefix, and restoring them only increases the interval hinge. The exceptional set is intersected with [2,M] as well; its removed primes could not occur in an exceptional smooth part h<=M.

## 1. A uniform sieve estimate with arbitrary exceptional primes

Let E have at most k primes, and let Q be a set of primes at most z, disjoint from E. Write

    V_Q = product_{q in Q}(1-1/q),
    theta_E = product_{p in E}(1-1/p).

There is a decreasing function e_k(r) tending to zero as r tends to infinity such that, for every real interval J of length T>=z^r,

    #{n in J: gcd(n,product(Q union E))=1}
       = T V_Q theta_E (1+O_bound(e_k(r))),                  (1)

where O_bound(e) means an error of absolute value at most e. The statement is uniform in E, including exceptional primes much larger than T.

Here is a precise derivation. The ordinary fundamental lemma supplies a decreasing e_base(u)->0, for u>=4, such that sifting by any subset of the primes at most z in an interval of length at least z^u has relative error at most e_base(u). As established in `DIFFUSE_RAW_WEIGHTS.md`, one may take

    e_base(u)=C[(u/2)^{-u/4}+2^{1-u/2}]                     (2)

with an absolute C. This follows from the standard fundamental-lemma remainder bound and the elementary product lower bound V_Q>=1/z.

Split E into E_small={p in E:p<=z} and E_large={p in E:p>z}. Put Q_0=Q union E_small, V_0=product_{p in Q_0}(1-1/p), and F=product_{p in E_large}p. Inclusion-exclusion gives the exact identity

    S(J,Q union E)=sum_{f|F} mu(f) S(J/f,Q_0).                (3)

Take r>=8 and split these divisors at f=T/z^{r/2}. For small f, (2) applies to length T/f, so the total approximation error is at most

    e_base(r/2) T V_0 sum_{f|F}1/f.

Dividing by the desired density T V_0 product_{p in E_large}(1-1/p) bounds the relative error by

    3^k e_base(r/2),                                       (4)

since (1+1/p)/(1-1/p)<=3.

For each large f, both its exact count and the magnitude of its main term are bounded by

    T/f+1 <= z^{r/2}+1,
    T V_0/f <= z^{r/2},

respectively. There are at most 2^k such divisors. Their combined error is therefore at most 3*2^k z^{r/2}. Since

    V_0>=1/z,
    product_{p in E_large}(1-1/p)>=2^{-k},

the relative error is at most

    3*4^k z^{1-r/2} <= 3*4^k 2^{1-r/2}.                    (5)

Thus a valid uniform choice in (1) is

    e_k(r)=3^k e_base(r/2)+3*4^k 2^{1-r/2},   r>=8.         (6)

For fixed k this tends to zero. No restriction on the sizes of E was used.

External source for the standard input: J. C. Lagarias, *Math 675: Combinatorial Sieve: Fundamental Lemma*, pages 1--2:

https://websites.umich.edu/lagarias/675notes/Estimate5-2015.pdf

## 2. Conditional level comparison for the diffuse part

Let V(n)=sum_{p in L}w_p v_p(n), where L is disjoint from E and every w_p<=eta. Put

    mu_L=sum_{p in L}w_p/(p-1).

Fix ell>eta and define

    r=floor(ell/eta)>=16,
    J=floor(r/2),
    kappa=r-J>=8.

If

    (1+e_k(kappa)) mu_L + eta 2^{k+1-J}
        <= (ell-eta)(1-e_k(r)),                             (7)

then, for every real T>0, every half-open positive interval B of length T, and every s>=0,

    #{a<=T: gcd(a,product E)=1, V(a)>s+ell}
       <= #{b in B: gcd(b,product E)=1, V(b)>s}.             (8)

The allowance of real T is useful below and follows directly from the interval sieve estimates.

### Proof

Use the first crossing of s in the ordered light-prime occurrences of a, allowing a partial last p-power block. The carrier d>1 has

    V(d/p)<=s<V(d)<=s+eta,

with p=Pmax(d). The remaining cofactor is coprime to all light primes below p and to E, and has load greater than ell-eta. It therefore has at least r light-prime occurrences, all at least p. Hence T/d>=p^r.

For each eligible d>1, define K_d(b)=0 when d does not divide b, and otherwise define

    K_d(b)=1_{d|b}
            1_{gcd(b/d, product E * product_{q in L,q<p}q)=1}.

Every positive term is the unique first crossing of s among the ordered light-prime occurrences of b. Moreover d is coprime to E, so positivity forces b to be coprime to E. Consequently

    sum_d K_d(b)<=1_{gcd(b,product E)=1, V(b)>s}.             (9)

Write V_p=product_{q in L,q<p}(1-1/q), and U=T/d. The lower bound in (1) gives a target contribution at least

    (1-e_k(r)) U V_p theta_E                               (10)

for each carrier.

For the source contribution, apply Markov's inequality to its heavy cofactors and expand their load into prime-power divisibility indicators. For j<=J, removing q^j leaves at least r-j light-prime occurrences, so a nonzero term necessarily has

    U/q^j>=p^{r-j}>=p^kappa.

The upper estimate (1), with sifting set E together with the light primes below p, applies at that length. Dividing by q^j preserves coprimality because q is a light prime at least p. Summing these low-exponent contributions gives at most

    (1+e_k(kappa)) U V_p theta_E mu_L.                       (11)

For j>J, discard all coprimality conditions. Exactly as in the diffuse proof, the contribution is at most

    U eta p^{1-J}/(p-1).

Since V_p>=1/(p-1) and theta_E>=2^{-k}, this is at most

    U V_p theta_E eta 2^{k+1-J}.                            (12)

Divide the sum of (11) and (12) by ell-eta. Condition (7) makes the result at most (10). Summing over carriers proves (8). All source and target counts were for real interval lengths; integer rounding is already contained in the sieve remainder bounds.

## 3. Choosing the small-weight threshold

It is enough to treat 0<epsilon<=1. Let

    ell=1+epsilon,
    delta=epsilon/2.

For fixed epsilon and k, choose eta=eta_{epsilon,k} sufficiently small that

    eta<=epsilon^2/128,
    r=floor(ell/eta)>=16,

and (7) holds with mu_L replaced by 1+epsilon/2. Such a choice exists by (6): as eta tends to zero, the left side tends to 1+epsilon/2 and the right side tends to 1+epsilon.

Assume first that mu_L<=1+epsilon/2. The conditional level comparison (8) then holds at every length and shift with the same parameters.

## 4. Decomposition by the exact exceptional-prime part

Every positive integer a has a unique decomposition

    a=h t,
    h is E-smooth,
    gcd(t,product E)=1.

Let Z(h)=sum_{p in E}w_p v_p(h). Since L and E are disjoint,

    X_w(a)=Z(h)+V(t).

Fix s>=0. For each h<=M, the prefix contribution to the level X_w>s+ell is counted over t<=M/h, while the target contribution to X_w>s is counted over a shifted interval of real length M/h.

If s-Z(h)>=0, comparison (8) applies directly and gives no positive defect for this h.

If s-Z(h)<0, every target t coprime to E automatically satisfies V(t)>s-Z(h). The source count is at most the total number of prefix t coprime to E. By ordinary finite inclusion-exclusion, the difference between the two unrestricted coprimality counts is at most 2^{|E|+1}: each count differs from (M/h)theta_E by at most 2^{|E|}.

Target integers with exceptional part h>M contribute nonnegatively and may be discarded from a lower bound. Summing the preceding estimates gives

    #{a<=M:X_w(a)>s+ell} - #{b in I:X_w(b)>s}
      <= 2^{|E|+1}
          #{h<=M: h E-smooth, Z(h)>s}.                       (13)

Integrating (13) over s>=1 proves (T'). The exact-part decomposition, rather than simply conditioning on divisibility by h, is essential here.

Because every exceptional weight is at most one,

    Z(h)<=Omega(h)<=log_2 M.

There are at most (1+log_2 M)^{|E|} E-smooth integers h<=M, as each exponent is between zero and floor(log_2 M). Hence (T') implies (T).

## 5. Large diffuse means

With the primes already restricted to [2,M] by the proof convention above, suppose

    mu_L>=1+epsilon/2,

the elementary prefix moment calculation gives

    E_prefix(V-mu_L)^2<=8eta mu_L,

and, because eta<=epsilon^2/128,

    sum_{a<=M}min(V(a),2)>=M.

Adding exceptional coordinates preserves this inequality. The general comparison

    Delta_2<=M-sum_{a<=M}min(X_w(a),2)

therefore gives H_2 for the full load. This is stronger than (T). Together with the low-mean case, it completes the proof.

## 6. A quantitative choice and a growing-core corollary

There is a constant c_epsilon>0, depending only on epsilon, such that one may take

    eta_{epsilon,k}=c_epsilon/(k+1).                         (14)

Here is a direct verification, again taking 0<epsilon<=1. For u>=16, (2) gives

    e_base(u/2)<=3C 2^{-u/4},

because u/4>=4 and hence (u/4)^{-u/8}<=2^{-u/4}. Thus

    e_k(u)<=3C 3^k 2^{-u/4}+6*4^k 2^{-u/2}.                (15)

Choose an integer R_epsilon>=16 so large that

    3C 2^{-R_epsilon/4}+6*2^{-R_epsilon/2}<=epsilon/16.

If u>=16k+R_epsilon, (15) implies e_k(u)<=epsilon/16. Choose c_epsilon small enough that

    c_epsilon<=epsilon^2/128,
    (1+epsilon)/c_epsilon>=max(32,2R_epsilon+2).

With eta as in (14), r=floor((1+epsilon)/eta) then satisfies

    r>=32k+2R_epsilon,
    kappa=r-floor(r/2)>=16k+R_epsilon,
    J=floor(r/2)>=k+1.

Consequently e_k(kappa),e_k(r)<=epsilon/16, and the extra tail in (7) is at most eta. Substituting mu_L<=1+epsilon/2, eta<=epsilon^2/128, and these estimates in (7) verifies it with positive margin. For example, the difference between the resulting right-hand lower bound and left-hand upper bound is at least

    (46/128)epsilon - (191/2048)epsilon^2 > 0.

This proves (14) and keeps the high-mean condition unchanged.

One consequence of (14) and (T) is the following genuine growing-core estimate: if k=o(log M/log log M) and all but at most k weights are at most c_epsilon/(k+1), then

    Delta_{2+epsilon} <= M^{o(1)} = o(sqrt(M)).               (16)

For the original cardinality scale there is a sharper convenient formulation. Fix delta in (0,1), let A be a set of n distinct sources in [2,M], and assume

    M<=16n^2,
    k<=(1-delta) log n/log log n,

with n tending to infinity. If all but at most k weights are at most c_epsilon/(k+1), then

    Delta_{2+epsilon}<=n^{1-delta+o(1)}=o(n).                (17)

Indeed, the logarithm of the bound in (T) is

    (k+1)[log 2+log(1+log_2 M)]
       <= (1-delta+o(1))log n.

Therefore the raw dual objective of such a vector satisfies

    sum_{a in A}X_w(a)-sum_{b in I}(X_w(b)-1)_+
       <= (2+epsilon)n+n^{1-delta+o(1)},                    (18)

since sum_{a in A}X_w(a) is at most (2+epsilon)n plus the full prefix hinge. This is an exclusion of a class of raw dual witnesses. It is not a claim that a per-instance integer cover has size equal to the raw LP value plus o(n).

## Consequences and limits

For a fixed number k of substantial weights, the defect in (T) is a fixed power of log M. In the nontrivial interval-length range M<16n^2, this is o(n). This is the quantitative scale needed in the usual raw dual inequality at cardinality n, provided the relevant dual vectors have this fixed-k property.

The result does not imply that all dual vectors have this property. Section 6 permits a logarithmic number of substantial coordinates with an explicit shrinking threshold, but in the growing-core obstruction found by the combinatorial analysis the number of core primes may be O(sqrt(n log n)). Substituting that much larger k into (T) is ineffective. No estimate uniform in an unrestricted k has been proved.

