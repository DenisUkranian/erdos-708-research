# Bounded substantial-weight multiplicity derived from a sparse obstruction

## Status and scope

This note proves a new necessary reduction on a hypothetical **actual** minimal raw obstruction. It imposes no source factorization hypothesis. It does not prove J_weak. The reduction applies along the sparse regime m/M -> 0; it does not establish that every obstruction is in that regime.

The inputs are the independently checked finite inequality in `SPARSE_HOT_BONFERRONI.md` and the exponential-moment estimate in `../audit/GLOBAL_SPARSE_MEAN_AND_HOTSET.md`.

## 1. Exact weighted exceptional-set estimate

Let P_0 be any finite set of primes and let

    mu_0 = sum_{p in P_0} 1/p,
    Omega_0(n) = sum_{p in P_0} v_p(n).

Let 0<=w_p<=1 be any finitely supported raw weights, and write

    X(n)=sum_p w_p v_p(n),
    mu_w=sum_p w_p/(p-1).

For every integer t>=1 and M>=1,

    sum_{n<=M, Omega_0(n)>=t} X(n)
        <= M (t+mu_w) h_t((1/p)_{p in P_0})
        <= M (t+mu_w) mu_0^t.                              (1)

Here h_t is the complete homogeneous polynomial: the sum of 1/d over all P_0-smooth integers d with Omega_0(d)=t. Repeated prime powers are included.

**Proof.** Let D_t be the set of P_0-smooth positive integers d with Omega_0(d)=t. Every n counted on the left has at least one divisor d in D_t. Since X is nonnegative,

    sum_{n<=M, Omega_0(n)>=t} X(n)
      <= sum_{d in D_t} sum_{k<=M/d} X(dk).

For such d, X(d)<=t. Complete additivity and the elementary prefix estimate give

    sum_{k<=M/d} X(dk)
      = floor(M/d) X(d) + sum_{k<=M/d} X(k)
      <= (M/d)(t+mu_w).

The prefix estimate follows directly from

    sum_{k<=N} X(k)
      = sum_p w_p sum_{j>=1} floor(N/p^j)
      <= N sum_p w_p/(p-1).

Finally, the expansion of (sum_{p in P_0}1/p)^t contains every monomial of h_t with a positive integer coefficient at least one. This proves (1). No independence, squarefreeness, or interval averaging is used.

## 2. Application to an actual sparse minimal raw obstruction

Fix c>2. Suppose a sequence of fixed-ambient inclusion-minimal raw failures has source sets A subset [2,M], m=|A|, intervals I of length M, and optimal clipped dual weights w satisfying

    F=L_raw(A,I)>c m,
    rho=m/M -> 0.

The already proved reductions give

    X(a)>c for every a in A,
    F<=c(m-1)+log_2 M,
    M<16m^2,
    h=|{b in I:X(b)>1}|<=F=O_c(m),
    mu_w<=1+o(1).                                         (2)

Fix a substantial-weight threshold eta in (0,1], independent of m, and set

    s=floor(1/eta)+1,
    z=M^[1/(2(s+1))],
    P_low={p<=z:w_p>=eta}.

In particular s eta>1. The finite Bonferroni estimate, with its rounding error retained, implies

    mu_low=sum_{p in P_low}1/p=O_{c,eta}(rho^(1/s)).        (3)

This holds uniformly over all actual source sets and shifts along the stated sparse regime.

Define the exceptional source set

    B={a in A:Omega_{P_low}(a)>=2s},
    G=A\B.

Applying (1) with t=2s and using (2)--(3),

    W_B:=sum_{a in B}X(a)
       <=M(2s+mu_w) mu_low^(2s)
       =O_{c,eta}(M rho^2)
       =O_{c,eta}(m rho)=o(m).                            (4)

Since every source has X(a)>c, also |B|<=W_B/c=o(m).

Every remaining a in G contains at most 2s-1 occurrences of primes in P_low. A prime larger than z can occur at most 2s+1 times in total in any integer at most M: 2s+2 such occurrences would have product strictly greater than z^(2s+2)=M. Consequently

    sum_{p:w_p>=eta} v_p(a) <=4s      for every a in G.     (5)

Thus a constant number of substantial-weight occurrences per retained source is **derived**, with all prime powers counted. The global number of substantial prime coordinates is not bounded by this statement.

Moreover every substantial prime satisfies

    p^s>M/(h+1),
    p>[M/(h+1)]^(1/s) -> infinity.                        (6)

This is the first-hot-bank bound, not an imposed lower cutoff.

## 3. What survives after the exceptional sources are removed

The dual vector remains the original optimal vector for A. We do not assert that it is optimal for G or that G is itself minimal. Its same-interval dual value satisfies the exact relation

    Phi_G(w)=Phi_A(w)-W_B>c m-o(m)=c|G|-o(m).              (7)

Let U be any subset of the full hot set H; in particular, it may be a union of hot-divisor banks belonging to retained sources. Every target in U is saturated in the full optimum for A. Therefore, for every active prime p,

    V_p(U)<=D_p(A).

The coordinatewise weighted excess against the retained demands is bounded by

    sum_p w_p (V_p(U)-D_p(G))_+
       <=sum_p w_p (D_p(A)-D_p(G))
       =W_B=o(m).                                        (8)

Thus both the global target budget and the previously derived near-balance condition survive. Target powers are not truncated at source exponents or at M.

## 4. Exact remaining issue

The following facts are now jointly necessary in the sparse regime:

* all retained source loads exceed the same fixed c>2;
* the total weighted reciprocal mean is at most 1+o(1);
* for each fixed eta>0, after a weighted o(m) deletion every retained source has at most 4(floor(1/eta)+1) occurrences of weights at least eta;
* the least prime carrying such a weight tends to infinity;
* all target positions of load greater than one belong to an O(m)-sized saturated set, and its active-row excess is controlled by (8).

These are restrictions on an actual obstruction, rather than a new assumed source class. They still do not give the required joint hinge inequality.

In particular, a previous theorem conditional on **at most K exceptional coordinates globally** cannot be applied: (5) is a per-source occurrence bound, not a global support bound. Nor can one substitute K=O(1/eta) into a diffuse-weight hypothesis eta<=c_delta/(K+1). That would require a numerical inequality of the form 1<=O(c_delta), which is not furnished by choosing eta smaller. The distinction prevents a circular use of the earlier controlled-core theorem.

The unresolved step is a single joint target-hinge estimate for a diffuse block and these unboundedly many substantial coordinates, using the bounded occurrence condition and actual saturation/demand balance. The interval hinge may not be independently spent once per substantial prime or once per source.

The regime in which m/M stays bounded away from zero also remains outside this reduction. Neither issue is solved by (1)--(8).
