# A general two-bin certificate for the raw surplus problem

24 November 2026; corrected after the user's counterexample. The combinatorial certificate remains valid for every weight profile and every number of prime occurrences. The unrestricted full-prefix active-part transfer is now DISPROVED with deficit Theta(M^(10/17)); see the correction audit in the bundle's counterexample/audit directory. The own-full-tail, reserve-corrected estimate remains unproved. Neither result closes Erdős 708.

## 1. The certificate on a finite weighted set

Let u_i be weights in [0,1] and l_i positive sizes, indexed by a finite set V. Put U=sum_i u_i and L=sum_i l_i. For a nonempty set E define

    r(E) = max(0, min(min_{i in E} u_i, (sum_{i in E}u_i - 1)/|E|)).

For each i permit precisely the sets E containing i for which

    2 sum_{j in E}l_j - l_i <= L.

Let m_i be the maximum r(E) over the permitted sets, with maximum zero if there is no positive candidate. Then

    (U-2)_+ <= sum_i m_i <= (U-1)_+.                 (1)

The upper inequality in fact holds for *arbitrary* choices of permitted families, independently in each row i.

### Upper bound: one common budget

Every m_i is at most u_i. If all m_i vanish, the conclusion is immediate. Otherwise select i and E attaining the largest value r=max_j m_j>0. For every j in E, m_j<=r; hence

    sum_{j in E}(u_j-m_j)
      >= sum_{j in E}u_j - |E|r >= 1.

Outside E, every u_j-m_j is nonnegative. Thus U-sum_i m_i>=1. This argument pays all rows from the same total budget; it does not sum independent root-bank capacities.

### Lower bound: first failure in two bins

Put v_i=u_i-m_i, so 0<=v_i<=1. Suppose sum_i v_i>2. Process the indices in nonincreasing order of m_i, attempting to place each item of size v_i into one of two bins of capacity one. Use any rule when both bins can accept it. Since the total size exceeds two, some item i must fail. If S and T are the contents of the bins at the first failure, then

    v_i+sum_{j in S}v_j>1,
    v_i+sum_{j in T}v_j>1,

and m_j>=m_i for every j in S union T. The sets E={i} union S and F={i} union T intersect only in i, and

    [2 l(E)-l_i]+[2 l(F)-l_i]
        =2(l_i+l(S)+l(T)) <= 2L.

At least one, say E, is therefore permitted in row i. Delete from E every j other than i with u_j=m_i and v_j=0. This preserves the strict inequality sum_E v>1 and the size condition. The failed item satisfies v_i>0, so i remains. For every remaining j, u_j>m_i: this follows from m_j>=m_i and v_j>=0, after the deletion. Moreover

    sum_{j in E}(u_j-m_i)
      =sum_{j in E}[v_j+(m_j-m_i)]
      >=sum_{j in E}v_j>1.

Consequently both min_E u_j and (sum_Eu_j-1)/|E| are strictly greater than m_i. Thus r(E)>m_i, contradicting the definition of m_i. We conclude sum_i v_i<=2, which proves the lower inequality in (1).

No separation of large and small weights, bounded number of factors, or gap between sizes is used.

## 2. Exact waterfilling without size restrictions

If every subset containing i is permitted, there is a unique theta>=0 satisfying

    sum_i(u_i-theta)_+=1

when U>1. The maxima are then exactly m_i=min(u_i,theta), and their sum equals U-1. Indeed, r(E)<=theta for every E because sum_E(u_i-theta)<=1. The set H={i:u_i>theta} attains theta for every i in H; adjoining any i with u_i<=theta gives r(H union {i})=u_i. For U<=1 all r(E) vanish.

The two-bin theorem quantifies exactly the loss caused by the numerical size restriction: at most one additional unit of total load.

## 3. Arithmetic realization, including all prime powers

Let 0<=w_p<=1 and X(t)=sum_p w_p v_p(t). Only primes with w_p>0 need be included in the following definitions. For a positive integer d whose prime factors are active, put

    Omega(d)=sum_p v_p(d),
    r_w(d)=max(0, min(min_{p|d}w_p, (X(d)-1)/Omega(d))),

with r_w(1)=0. Define for each active prime p and integer t

    m_{p,M}(t)=max {r_w(d): d|t, p|d, d^2<=M p},
    K_M(t)=sum_p v_p(t) m_{p,M}(t),

where an empty maximum is zero. These are maxima over actual divisors, not formal exponent profiles.

Each occurrence of p in t is a separate item of weight w_p and size log p. A divisor containing p can be represented by a subset containing any designated occurrence of that prime, so every occurrence in the same prime row has the same maximum m_{p,M}(t). Repeated prime factors are therefore counted exactly, with no squarefree assumption.

For every positive integer t, the upper half of (1), which allows arbitrary row families, gives

    0 <= K_M(t) <= (X(t)-1)_+.                        (2)

For t<=M, let h(t) be its full active part. The sizes of all active occurrences sum to log h(t)<=log M. Every set permitted by the lower-bound theorem corresponds to a divisor satisfying d^2<=h(t)p<=M p. Hence enlarging to the definition above gives

    K_M(t) >= (X(t)-2)_+   for every t<=M.             (3)

The stronger local statement uses K_{h(t)}(t), with h(t) in place of M. In particular, for every a<=M,

    (X(a)-2)_+ <= K_{h(a)}(a) <= K_a(a) <= K_M(a).

This is the distinction between eligibility at the active part, the actual source size, and the ambient target threshold.

## 4. Keep the actual source size in the arithmetic transfer

The sharper source function is K_{h(a)}(a), not K_M(a). It still covers (X(a)-2)_+ and is no larger than K_a(a). It discards roots that become eligible only because the ambient M or an inactive cofactor is larger than the active part. This discarded mass is a useful reserve, not an error to add back. In the following identities we use this active-part kernel. The same identities and nonnegative reserves remain valid with K_a(a).

### Exact remaining transfer

Fix c=2+delta, A={a<=M:X(a)>c}, n=|A|, and any actual M-term interval I. Define the nonnegative reserves

    R_source=sum_{a in A}[K_{h(a)}(a)-(X(a)-2)],
    R_target=sum_{b in I}[(X(b)-1)_+-K_M(b)].

Then the following is an exact identity:

    J_c = sum_{a in A}K_{h(a)}(a)-sum_{b in I}K_M(b)
          -delta*n-R_source-R_target.                (4)

Equivalently, with the full prefix sum, one must also subtract sum_{a<=M,a notin A}K_{h(a)}(a). This latter reserve can be large and must not be discarded silently.

Thus a sufficient new arithmetic inequality would be

    sum_{a in A}K_{h(a)}(a) - sum_{b in I}K_M(b)
       <= R_source + R_target + o_delta(n).

That inequality is not proved here. Unrestricted transfer of the full-prefix kernel sum is false, by the subsequently supplied counterexample. The useful proved content is source coverage and target common-budget feasibility for one explicit divisor kernel, for arbitrary weight profiles and all powers. The corrected expression equals Phi_A(w)-2|A| exactly, so rewriting it is not an arithmetic estimate. The map w -> K_{h_w(a)}^w(a) can jump when prices reach zero; fixed-scale continuity cannot be transferred to this moving scale.


## 5. A checked distinction: ambient-prefix transfer is false

Take M=18, w_2=w_3=1, all other prices zero, and I=[9,26]. Direct exact rational evaluation gives

    sum_{a<=18}K_18(a)=17/2,
    sum_{b=9}^{26}K_18(b)=8.

Thus unrestricted transfer of the *ambient* prefix kernel is false. At c=21/10, the full tail is {8,12,16,18}, whose ambient kernel sum is 13/2, so this does not refute the tail-restricted assertion. It also does not refute actual-size-source transfer. The accompanying checker verifies the exact values and independently tests the pointwise theorem in rational arithmetic; the proof, rather than the finite checks, establishes uniformity.

## 6. The constant two in the pointwise source theorem is sharp

Let there be 2k items, all sizes equal, and all weights u=1/k+epsilon with 0<epsilon<=1-1/k. A root eligible in row i has at most k items, and r(E) is maximized at cardinality k, giving m_i=u-1/k=epsilon. Hence

    sum_i m_i=2k epsilon=sum_i u_i-2.

Thus the lower constant two cannot be reduced for this specific general size certificate, even though a separate arithmetic aggregate might enjoy additional slack. This sharp example allows arbitrarily many occurrences and arbitrarily small prices.
