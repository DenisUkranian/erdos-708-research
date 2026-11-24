# A uniform approximate hinge inequality for diffuse raw weights

## Status

This is a partial result with an independent internal audit of its carrier argument, weighted moments, and one-exception extension. No substantive error was found; no external verification or solution of unrestricted Erdős 708 is claimed. The main theorem is uniform over arbitrary growing prime supports and requires every individual dual weight to be small. Section 5 also allows one arbitrary exceptional prime weight.

The only external input is the standard fundamental lemma of the combinatorial sieve. All other estimates and the carrier argument are included below.

## Main theorem

For every epsilon > 0 there exists eta_epsilon > 0 such that the following holds. Let P be any finite set of primes, let 0 <= w_p <= eta_epsilon, and put

    X(n) = sum_{p in P} w_p v_p(n).

For every positive integer M and every interval I of M consecutive positive integers,

    sum_{a<=M}(X(a)-2-epsilon)_+
        <= sum_{b in I}(X(b)-1)_+.                           (H)

The constants are uniform in P, M, the weights, and the shift of I. In particular, the total unweighted reciprocal mass of P is unrestricted.

Primes greater than M may be removed at the beginning: they contribute zero to the prefix, while restoring them can only increase the interval hinge. Thus the proof assumes P is contained in [2,M]. The case M=1 is immediate.

## 1. Uniform sifting at a large fixed parameter

There is a nonnegative decreasing function E(k), defined for real k >= 4, with E(k) tending to zero as k tends to infinity, such that the following holds. Let z >= 2, let Q be any subset of the primes at most z, and write

    V_Q = product_{q in Q}(1-1/q).

If J is any half-open interval of real length T >= z^k, then

    (1-E(k)) T V_Q
      <= #{m in J: gcd(m,product_{q in Q}q)=1}
      <= (1+E(k)) T V_Q.                                    (S)

Intervals used below contain only positive integers; the same counting assertion is valid more generally.

For completeness, the standard fundamental lemma gives

    S(J,Q) = T V_Q [1+O(u^{-u/2})] + O(z^u),

uniformly in J, Q, z, and u >= 1. Indeed, the remainder in each divisibility count is at most one. The dimension-one condition holds for every subset of the primes, with common absolute constants. Take u=k/2. The elementary product bound

    V_Q >= product_{m=2}^{floor z}(1-1/m)
        = 1/floor z >= 1/z

shows that the relative additive error is at most O(2^{1-k/2}). Consequently one can take, after increasing an absolute constant C,

    E(k) = C[(k/2)^{-k/4} + 2^{1-k/2}],       k >= 4.         (1)

Both displayed terms decrease on this range.

External reference: J. C. Lagarias, *Math 675: Combinatorial Sieve: Fundamental Lemma*, theorem on page 1 and the interval example on page 2:

https://websites.umich.edu/lagarias/675notes/Estimate5-2015.pdf

An interval-specific version for arbitrary subsets of the small primes also appears in A. Granville and K. Soundararajan, *Multiplicative number theory: The pretentious approach*, Theorem 1.4.2:

https://dms.umontreal.ca/~andrew/PDF/Book.To1.4.pdf

## 2. A general level comparison under a weighted mean condition

Let ell > 0, and suppose 0 <= w_p <= eta < ell, where

    r = floor(ell/eta) >= 8,
    J = floor(r/2),
    kappa = r-J >= 4.

Put

    mu = sum_{p in P} w_p/(p-1).

Assume

    (1+E(kappa)) mu + eta 2^{1-J}
       <= (ell-eta)(1-E(r)).                                (2)

Then, for every s >= 0,

    #{a<=M: X(a)>s+ell} <= #{b in I: X(b)>s}.                 (3)

### 2.1 Partial prime-power carriers

Order the prime occurrences in an integer by increasing prime, retaining multiplicity. For a source a with X(a)>s+ell, let d be the prefix of these occurrences at the first time the accumulated weight exceeds s. Primes outside P are omitted from this ordering. Thus, with p=Pmax(d),

    X(d/p) <= s < X(d) <= s+eta.                            (4)

Crucially, the last p-power block is allowed to be partial. Every P-prime q<p occurs in d to its full exponent in a, while some further copies of p may remain in a/d.

The cofactor t=a/d is coprime to every P-prime below p, and

    X(t)>ell-eta.

Since each prime occurrence contributes at most eta, t has at least r P-prime occurrences, counting multiplicity. All these primes are at least p. Hence

    t >= p^r,
    T_d := M/d >= p^r.                                     (5)

Let F_s be the finite family of all P-smooth integers d satisfying (4) and d p^r<=M. Every heavy source has its carrier in F_s.

### 2.2 An exact target certificate

For d in F_s, put p=Pmax(d),

    Q_p = {q in P:q<p},
    V_p = product_{q in Q_p}(1-1/q),

and define

    K_d(b) = 1_{d|b} 1_{gcd(b/d,product_{q in Q_p}q)=1}.

For every positive integer b,

    sum_{d in F_s} K_d(b) <= 1_{X(b)>s}.                    (6)

To see this, a positive K_d forces d to contain the full prime-power blocks of b at all P-primes smaller than p. At p, (4) identifies the first occurrence crossing s. Thus a positive term corresponds to the unique first crossing of s in the ordered prime occurrences of b. This also proves X(b)>s. The allowance of further p-factors in b/d is essential and does not cause duplicate crossings.

Multiples of d in I correspond to a half-open interval of integers of real length T_d=M/d. By (5), (S), and (6),

    #{b in I:X(b)>s}
       >= sum_{d in F_s} (1-E(r)) T_d V_p.                  (7)

### 2.3 Bounding the source cofactors

Fix d in F_s and abbreviate T=T_d. It suffices to count the enlarged cofactor set

    A_d = {t<=T: gcd(t,product Q_p)=1, X(t)>ell-eta}.

Every member has at least r P-prime occurrences, all at least p. Markov's inequality gives

    |A_d| <= (ell-eta)^{-1} sum_{t in A_d} X(t).              (8)

Expand the sum of X into prime-power divisibility indicators. If q>=p, j<=J, and some t in A_d is divisible by q^j, then t/q^j still has at least r-j such occurrences. Therefore

    T/q^j >= p^{r-j} >= p^kappa.                            (9)

For these terms the upper bound in (S) applies after dividing by q^j. Since q is not in Q_p, this division preserves coprimality to Q_p. Terms failing (9) are zero before enlarging the set. It follows that the contribution of all j<=J is at most

    (1+E(kappa)) T V_p
        sum_{q in P,q>=p} w_q sum_{j>=1} q^{-j}
       <= (1+E(kappa)) T V_p mu.                            (10)

For j>J, discard coprimality and the heavy-source condition. The contribution is at most

    T sum_{q in P,q>=p} w_q/[q^J(q-1)]
       <= T eta sum_{m=p}^infinity 1/[m^J(m-1)]
       <= T eta p^{1-J}/(p-1).

The last inequality follows by replacing m^{-(J-1)} with p^{-(J-1)} and telescoping the remaining sum of 1/[m(m-1)]. Also

    V_p >= product_{m=2}^{p-1}(1-1/m) = 1/(p-1).

Consequently the high-power contribution is at most

    T V_p eta p^{1-J} <= T V_p eta 2^{1-J}.                 (11)

This estimate is why the argument works for the raw valuations, even though a whole prime-power block may have weight larger than eta.

Combining (8)--(11) and using (2),

    |A_d| <= (1-E(r)) T_d V_p.

Summing over carriers and comparing with (7) proves (3). Integrating (3) over s>=1 yields

    sum_{a<=M}(X(a)-1-ell)_+
        <= sum_{b in I}(X(b)-1)_+.                          (12)

## 3. Large weighted means give H_2 automatically

Suppose P is contained in [2,M] and 0<=w_p<=eta. Denote expectation over the uniform prefix {1,...,M} by E_0. Then

    mu - 3eta <= E_0 X <= mu,                               (13)

and

    E_0 (X-mu)^2 <= 8eta mu.                                (14)

To verify (13), put e_p=floor(log M/log p). The total rounding loss from powers p^j<=M is at most eta: different prime powers are different integers, so there are at most M-1 of them. The omitted tail for each p is

    w_p/[p^{e_p}(p-1)] <= 2eta/M.

There are at most M primes in the support, so the omitted tails total at most 2eta.

For distinct primes p and q, counting multiples gives

    E_0[v_p v_q] <= 1/[(p-1)(q-1)].

For a single prime,

    E_0[v_p^2] <= (p+1)/(p-1)^2.

Thus

    E_0 X^2 <= mu^2 + sum_p w_p^2 p/(p-1)^2
              <= mu^2 + 2eta mu.

Combining this with the lower mean bound in (13) proves (14).

Let 0<delta<=1 and eta<=delta^2/32. If 1+delta<=mu<=4, the function x -> min(x,2) is 1-Lipschitz, so

    E_0 min(X,2)
      >= min(mu,2) - sqrt(E_0(X-mu)^2)
      >= 1+delta - sqrt(32eta) >= 1.                         (15)

If mu>=4, Chebyshev's inequality and (14) give

    Pr_0(X<2) <= 8eta mu/(mu-2)^2 <= 8eta,

and therefore

    E_0 min(X,2) >= 2(1-8eta) >= 1.                         (16)

The last step uses eta<=delta^2/32<=1/32.

Finally, each prime-power divisibility count is at least as large in I as in the prefix, so sum_I X >= sum_{a<=M}X(a). Hence

    Delta_2
      = sum_{a<=M}(X(a)-2)_+ - sum_{b in I}(X(b)-1)_+
      <= M - sum_{a<=M}min(X(a),2).                         (17)

Equations (15)--(17) prove H_2 whenever mu>=1+delta and eta<=delta^2/32, uniformly in all the other parameters.

## 4. Choice of parameters and proof of the main theorem

It is enough to treat 0<epsilon<=1, since increasing the prefix threshold decreases its hinge. Set

    ell = 1+epsilon,
    delta = epsilon/2.

Choose eta>0 sufficiently small that eta<=epsilon^2/128, r=floor(ell/eta)>=8, and condition (2) holds with mu replaced by 1+epsilon/2. Such a choice exists: as eta tends to zero, r and kappa tend to infinity, the left side of (2) tends to 1+epsilon/2, and the right side tends to 1+epsilon.

If the actual mu<=1+epsilon/2, Section 2 proves (H). If mu>=1+epsilon/2, Section 3 gives H_2, which implies (H). These cases cover every mu. Restoring any discarded primes above M only increases the target hinge. This proves the theorem.

## 5. Adjoining one arbitrary prime weight

The main theorem remains valid if one prime q has an arbitrary nonnegative weight, while every other prime weight is at most eta_epsilon. In particular, an obstruction to H_(2+epsilon) must have at least two individual weights exceeding eta_epsilon.

Here eta_epsilon is chosen as in Section 4. Write V for the raw load from the light primes, excluding q, and let mu_light be their sum of w_p/(p-1), after harmlessly discarding primes greater than M.

If mu_light>=1+epsilon/2, Section 3 gives

    sum_{a<=M} min(V(a),2) >= M.

Adding the q-load only increases this capped prefix sum. The general identity (17) therefore proves H_2 for the full raw load.

Suppose now that mu_light<=1+epsilon/2. Section 2 gives the level comparison

    #{a<=N:V(a)>s+ell} <= #{b in J:V(b)>s},

with ell=1+epsilon, for every nonnegative s, every integer length N, and every shifted interval J of that length. This assertion is available uniformly at all smaller lengths as well: if necessary discard primes greater than N, which only decreases the weighted mean and only decreases the target load. Also V(q^j t)=V(t).

First adjoin any nondecreasing bounded q-adic profile u(j) in [0,1], with u(0)=0. Set c=1+ell=2+epsilon. Expanding each hinge in the successive q-power increments gives, for h equal to c or 1,

    (V(n)+u(v_q(n))-h)_+
      = (V(n)-h)_+
        + sum_{j>=1} 1_{q^j|n}
            integral_{u(j-1)}^{u(j)} 1_{V(n)>h-v} dv.        (18)

The base hinges satisfy H_c by integrating the light-prime level comparison over s>=1. For each increment, the target threshold is s=1-v>=0, and the source threshold is c-v=s+ell. Multiples of q^j in the prefix rescale to {1,...,floor(M/q^j)}; those in I rescale to a consecutive interval containing at least that many integers. Apply the uniform light-prime level comparison to a subinterval of that length; if the length is zero, the prefix increment is zero. Any extra target is harmless. Thus each prefix increment in (18) is at most its target increment, proving H_c for V+u(v_q).

Finally take

    u(j)=min(w_q j,1),
    T(j)=(w_q j-1)_+.

For c>1,

    (V+u+T-c)_+ <= T+(V+u-c)_+,
    (V+u+T-1)_+  = T+(V+u-1)_+.

The second identity holds because T>0 implies u=1. The nondecreasing q-adic function T has prefix sum no greater than its sum over I, by counting multiples of each q-power. Hence adjoining the raw q-tail preserves H_c. This proves the one-prime extension for arbitrary w_q>=0.

## Consequence and unresolved issue

A violation of H_(2+epsilon), if one exists, must have at least two individual prime weights greater than eta_epsilon. Thus arbitrarily diffuse dual vectors, even with one exceptional prime coordinate, cannot supply an obstruction, regardless of how large or dense their support becomes.

This does not bound the number of substantial weights, and it does not give a rule for adjoining a diffuse block to a block of two or more arbitrary substantial weights. The latter mixture remains outside the theorem and is part of the general Erdős 708 problem.

