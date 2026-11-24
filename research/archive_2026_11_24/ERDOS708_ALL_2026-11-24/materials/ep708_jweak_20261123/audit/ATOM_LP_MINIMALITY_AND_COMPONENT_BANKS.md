# The prime-power-count LP and its minimal obstructions

## Status and purpose

This is an internally checked reduction for the unrestricted problem. It does not prove the prime-power-count bound, the original asymptotic conjecture, or J_weak. The LP below is stronger than the usual valuation LP. Its minimal obstructions must be chosen independently; conclusions about them must not be silently assigned to a minimal obstruction for the valuation LP.

The new finite consequence in Section 6 is a bound on the sum of all complete prime-power components of every source. Its proof uses actual interval banks and tight active rows, not an abstract incidence relaxation.

## 1. The stronger LP

Let A be a set of m distinct integers in [2,M], and let I={x+1,...,x+M}, with x>=0. For every source prime p and 1<=j<=E_p=max_{a in A} v_p(a), define

    N_A(p^j) = #{a in A : p^j divides a}.

The prime-power-count LP is

    L_at(A,I) = min sum_{b in I} z_b
    subject to 0<=z_b<=1,
               sum_{b in I, p^j|b} z_b >= N_A(p^j)
               for every p,j.

The whole interval is feasible because N_A(p^j)<=floor(M/p^j)<=N_I(p^j). Summing its constraints over j shows that every feasible point is also feasible for the valuation LP. Thus

    L_raw(A,I) <= L_at(A,I).

An integral feasible point supplies each prime's source exponents on distinct target positions. It therefore gives a product-divisibility cover, although some product-divisibility covers do not satisfy these stronger count constraints.

The dual has nonnegative prices alpha_{p,j}. Put

    u_p(e)=sum_{j<=e} alpha_{p,j},
    U(n)=sum_p u_p(v_p(n)).

Then

    L_at(A,I) = max_alpha [ sum_{a in A} U(a)
                            - sum_{b in I} (U(b)-1)_+ ].       (1)

Every profile is nondecreasing and is constant above its final source level. No claim that U is completely additive is made.

## 2. Each prime profile can be capped at one

For each p replace u_p by u'_p=min(u_p,1), and write t_p=u_p-u'_p. Both u'_p and t_p are nondecreasing profiles with nonnegative prime-power increments. Let U'=sum_p u'_p and T=sum_p t_p.

If T(n)>0, then some u'_p(v_p(n))=1. Consequently

    (U(n)-1)_+ = (U'(n)-1)_+ + T(n).                         (2)

Each prime-power indicator occurs in T with nonnegative coefficient. Therefore

    sum_A T <= sum_{n<=M} T(n) <= sum_I T.                    (3)

Subtracting (2) in the dual objective and using (3) proves that capping never decreases the objective. An optimal dual can thus be chosen with

    0<=u_p(e)<=1 for every p,e.                              (4)

This is a cap on the whole profile of one prime. It is not a truncation of the actual target valuation followed by use of an uncapped linear price.

## 3. Minimality at the same ambient interval

Fix c>2. Suppose A is inclusion-minimal subject to L_at(A,I)>cm, with the same M and I retained when a source is removed. Write

    F=L_at(A,I)=cm+e,  e>0.

Choose an optimal capped dual and any optimal primal z. Removing a source a leaves the same target hinge in a feasible dual for A\{a}; rows with zero demand may be retained. Hence

    F-U(a) <= L_at(A\{a},I) <= c(m-1),
    U(a) >= c+e > c > 2.                                   (5)

Thus every source has at least three distinct primes with positive profile value. In particular U(a)<=omega(a)<=log_2 M gives

    0<e<=log_2 M-c,  F=cm+O(log M).                         (6)

Let H={b in I:U(b)>1}. Complementary slackness gives

    z_b=1 for b in H,
    |H|<=F,
    sum_{b in I,p^j|b} z_b = N_A(p^j)
       whenever alpha_{p,j}>0.                             (7)

These are properties of this atom LP optimum. They are not inherited from a valuation-LP optimum.

## 4. A cubic gate that genuinely preserves the count constraints

If M>=8m^3, the stronger integer count problem has a cover of at most 2m positions. Here is the full argument, included to avoid importing the valuation-only quadratic gate without justification.

Put C=M/(2m). Then C^2>=M and C^(3/2)>=M. Regard a source a as the product of its pairwise coprime complete components q=p^{v_p(a)}.

At most one component can exceed C. If one does, the remaining factor is less than 2m<=C. If every component is at most C, merge components while their product is at most C. Three final products would have every pair product greater than C and hence total product greater than C^(3/2)>=a, a contradiction. Thus each source splits into at most two coprime parts, each either a single component greater than C or an integer at most C. No complete p-component is split between two parts.

For a fixed prime p, assign the large p-components in descending exponent order to distinct interval multiples of their required powers. The j-th component in this order occurs in a distinct source, so at least j source integers and hence at least j target integers are divisible by that power. This greedy assignment succeeds. Different primes may use the same target, because their count constraints concern different prime rows.

Now assign all small parts to fresh target multiples, avoiding every previously used position. Each small part has at least floor(M/C)=2m candidate positions; there are at most 2m parts altogether. The assignment succeeds. For each prime, its complete components are assigned to distinct positions, so every threshold count N_A(p^j) is met.

Therefore an atom-minimal failure satisfies

    M<8m^3,  m>M^(1/3)/2.                                 (8)

The known M>=16m^2 valuation-cover gate does not automatically apply here: its factor splits may divide a single complete prime-power component between positions.

## 5. Full-component deletion banks and tight count rows

For a source a and any prime q|a, let Q_q=q^{v_q(a)} and define

    C_q(a)={b in I : a/Q_q divides b}.

Removing a whole q-component changes U(a) by at most one. Every b in C_q(a) therefore satisfies

    U(b)>=U(a)-u_q(v_q(a))>c-1>1.                           (9)

Thus C_q(a) is contained in H, including when q is inactive.

Choose any other active prime p|a and a level j<=v_p(a) with alpha_{p,j}>0. Then every element of C_q(a) is divisible by p^j. By (7),

    N_A(p^j) >= |C_q(a)| >= floor(M Q_q/a) >= Q_q.          (10)

At least three primes in a are active, so such a p exists for every q. Consequently every complete source component obeys

    q^{v_q(a)} <= m.                                      (11)

This includes inactive source primes. In particular every source prime is at most m, and all source prime-power levels are at most m.

The number R(A)=sum_p E_p of all LP rows, not merely the active rows, satisfies

    R(A) <= sum_{j>=1} pi(m^(1/j))
          <= pi(m)+sqrt(m) log_2 m = o(m).                 (12)

At a basic optimum at most R(A) variables are strictly between zero and one. Rounding these variables upward therefore produces a count cover of cost less than or equal to F+R(A). This useful rounding fact does not provide an upper bound on F itself.

## 6. A stronger union inequality and component-sum restriction

Fix a source a and an active level p^j|a. Write

    Q_q=q^{v_q(a)},  t_a=floor(M/a),
    S_a=sum_{q|a}(Q_q-1).

Take the union of all full-component deletion banks except the p-bank:

    V_{a,p} = union_{q|a,q!=p} C_q(a).

This union is contained in H and in the p^j row. For any two different q,r,

    lcm(a/Q_q,a/Q_r)=a.

All intersections of two or more of these banks are consequently exactly the a-multiples. The exact union count is

    |V_{a,p}| = sum_{q|a,q!=p} N_I(a/Q_q)
                 -(omega(a)-2) N_I(a).                    (13)

In every complete period of length a, the union has exactly

    1+sum_{q|a,q!=p}(Q_q-1)

positions. Split the actual length-M interval into t_a complete periods and a remaining interval. The remaining contribution is nonnegative. From tightness of the active row,

    N_A(p^j) >= |V_{a,p}|
      >= t_a [1+S_a-(Q_p-1)].                             (14)

This retains the actual source count N_A(p^j) and can be substantially stronger than replacing it by m.

Let r_a be the number of active primes in a; r_a>=3 by (5). Choose one active level for each such prime and sum (14). Each corresponding demand is at most m, whereas the sum of Q_p-1 over the chosen active primes is at most S_a. Hence

    r_a m >= t_a [r_a+(r_a-1) S_a],

and therefore

    S_a <= [r_a/(r_a-1)] [m/t_a-1]
         <= (3/2)[m/t_a-1].                               (15)

All complete source components occur in S_a, including inactive ones. No target capacity is spent more than once in a single row. Summing row inequalities only uses the separate necessary upper bounds N_A(p^j)<=m.

A related finite prohibition follows directly from (14): an active level with demand N_A(p^j) cannot occur in a source for which

    floor(M/a) [1+sum_{q|a,q!=p}(q^{v_q(a)}-1)]
       > N_A(p^j).                                       (16)

These are necessary conditions on an actual minimum. They have not been shown to be jointly impossible.

For any two distinct complete components Q_q,Q_r, there is a third active prime p different from q,r. Keeping just those two components in (14) gives the additional exact restriction

    Q_q+Q_r <= m/t_a+1.                                   (18)

In particular the two largest complete components satisfy (18).

## 7. Relation to the global goal

The universal atom hinge inequality

    sum_{n<=M}(U(n)-c)_+ <= sum_{b in I}(U(b)-1)_+           (17)

for all capped monotone prime profiles is equivalent to L_at(A,I)<=c|A| for every source subset A. In one direction, sum_A U<=c|A|+sum_prefix(U-c)_+ and use (1). In the other direction, take A={n<=M:U(n)>c}; the same dual objective violates the LP bound if (17) fails. An empty A cannot violate (17).

Thus the atom route encounters the known general monotone-profile hinge problem. No counterexample to its threshold-two version is established here.

A uniform asymptotic bound L_at(A,I)<=(2+o(1))|A| would suffice for the original integer conjecture, because L_raw<=L_at. One may use the already proved fixed-ambient integer-minimal reduction for the original valuation problem: all source primes then lie below c|A| for a fixed c>2, so raw-LP vertex rounding costs at most pi(c|A|)=o(|A|), while the ambient quadratic gate makes the minimal sizes tend to infinity. As usual, finitely small sizes can be absorbed in an additive constant before taking a minimal failure.

This implication would exclude the original minimal-obstruction class. It would not establish a pointwise J_weak inequality for a previously fixed raw dual vector. The two duals, their minimizers, their prime profiles, and their budgets must remain distinct throughout the argument.

The raw first-hot-power argument also does not transfer to the capped-profile setting. A single p-power has U(p^e)=u_p(e)<=1 for every e, even if one of the increments alpha_{p,j} is large. Thus the earlier inference that substantial raw prime weights must occur on primes tending to infinity cannot be imported into this atom-minimal class.

## 8. Audit status and unresolved step

The cap identity, minimality reduction, cubic gate, tight-row bank count, and complete-period union count are exact arguments. The component-sum implication (15) received an independent derivation by another collaborating agent.

The unresolved step is a uniform global estimate on the atom LP or on the original J_weak hinge budget. The bounds on individual components, their sum, the number of rows, and the hot set do not themselves furnish that estimate. No finite search, restricted source class, or external referee/formal verification is claimed in this note.
