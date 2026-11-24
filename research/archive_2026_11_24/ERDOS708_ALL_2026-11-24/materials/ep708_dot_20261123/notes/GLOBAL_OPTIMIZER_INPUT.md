# Global surplus maximizers and a valid reduction of the shift space

## Scope

Fix c>2 and define, for an actual positive M-term interval I,

    J_c(w)=sum_{2<=a<=M}(X_w(a)-c)_+
              -sum_{b in I}(X_w(b)-1)_+,
    X_w(n)=sum_p w_p v_p(n).

This note proves exact optimization and shift-reduction facts. It does not prove a uniform bound J_c<=C_c, a nonpositive surplus theorem, or an amplification theorem converting every positive finite surplus into unbounded surplus.

## 1. Global maximization supplies genuine optimality

Let F(A,I) denote the boxed raw covering LP for A subset [2,M]. Include A=empty with F(empty,I)=0. Then

    max_{w>=0}J_c(w)
      =max_{A subset [2,M]}[F(A,I)-c|A|].                 (1)

Indeed, for each w,

    sum_{a<=M}(X_w(a)-c)_+
       =max_A sum_{a in A}(X_w(a)-c).

The finite maximum over A commutes with the supremum over w, and ordinary boxed-cover duality gives (1). Coordinates p>M may be removed: they contribute nothing on the source side and only increase the target hinge. The usual raw-dual clipping permits a maximizer with 0<=w_p<=1.

If w is a global maximizer in (1) and

    A*={a in [2,M]:X_w(a)>c},

then w is genuinely optimal for F(A*,I). Otherwise replacing it by a better raw dual for the same A* would strictly increase J_c. Conversely, merely declaring a high-load full-tail set for an arbitrary price vector does not establish this optimality.

We additionally normalize away every zero-demand coordinate: if p divides no member of A*, set w_p=0. This leaves every load on A* unchanged and only decreases loads outside A*, so the strict full tail remains exactly A*. The target hinge can only decrease. Since the starting vector was a global maximizer, its J_c value is therefore preserved, as is genuine raw optimality for A*. After this normalization, every active prime p with w_p>0 divides at least one source. Global maximality alone, without this extra normalization, would not exclude gratuitous positive prices on zero-demand coordinates.

### Rational weights and source ties

For each fixed A, the raw covering LP has rational data and admits a rational optimal dual. Choose an A maximizing the right side of (1), and choose a rational optimal dual for it. Its J_c value is again the global maximum. Thus a rational global maximizer exists.

If c is irrational, no integer source can satisfy X_w(a)=c at this rational maximizer. This eliminates source ties, but not target ties X_w(b)=1. In a proof aimed at a given threshold 2+delta, one may work at a slightly smaller irrational threshold and retain a positive margin. This observation is a normalization device, not a bound for the maximum.

## 2. An optimum can be supported by actual target-tie equations

Among all global maximizers choose one minimizing sum_p w_p. For its full tail A*, it also minimizes this sum among raw dual optimizers: every raw optimizer for A* would again be a global J_c maximizer.

Use raw dual variables w_p>=0 and h_b>=0, with

    h_b>=sum_p w_pv_p(b)-1.

The raw optimal face, followed by the minimum-sum face, is a nonempty face of a pointed rational polyhedron. It has a vertex. Every such minimum-sum optimum has w_p<=1: clipping a price above one preserves or improves raw optimality and strictly decreases sum_p w_p.

At a vertex let P+={p:w_p>0}, r=|P+|. The actual target vectors

    (v_p(b))_{p in P+},  for targets with X_w(b)=1,

span R^r. Otherwise a nonzero direction orthogonal to all those vectors could be varied slightly in both signs, preserving positive coordinates and all strict hot/cold inequalities; setting h_b to the resulting hinge would express the vertex as an interior point of a feasible segment.

Consequently one can choose r linearly independent actual target-tie equations determining the positive prices. This does not bound r, the valuation entries, or the resulting denominators independently of M. The artificial upper constraints w_p<=1 are not being used as the reason for this vertex structure.

## 3. Actual target exponents can be capped when the shift is allowed to change

The following reduction changes the interval. It must not be applied to fixed-interval row equations without reoptimization.

**Lemma.** Fix M, a finite prime set P, and x>=0. For p in P put

    e_p=floor(log_p M)+1,

so p^{e_p}>M. There exists x'>=0 such that, simultaneously for every p in P and every j=1,...,M,

    v_p(x'+j)=min(v_p(x+j),e_p).                          (2)

**Proof.** Preserve x modulo p^{e_p}. At most one j in the interval can satisfy p^{e_p}|x+j, since p^{e_p}>M. If there is such a j0, exactly one of the p possible lifts of x modulo p^{e_p+1} would make x'+j0 divisible by p^{e_p+1}; choose any other lift. This makes its valuation exactly e_p. Every other position already has valuation below e_p, unchanged by the congruence. If no such j0 exists, choose any lift. The moduli p^{e_p+1} for different p are coprime, so CRT gives all choices simultaneously, with a nonnegative representative x'. This proves (2).

For every nonnegative price vector supported on P, the new actual interval I' satisfies

    X_w(x'+j)<=X_w(x+j)

pointwise. Its target hinge is no larger, while the source prefix is unchanged. Therefore

    J_c(w;M,I')>=J_c(w;M,I).                             (3)

This statement is simultaneous in w, not a formal clipping of fixed target integers. For a uniform-in-shift upper bound it is enough to examine these actual bounded-exponent patterns.

In particular, for fixed M and all source primes p<=M, the worst surplus over shifts is attained within a finite CRT residue space, followed by a compact price optimization. A paired primal for the old interval need not remain feasible or optimal in the new one. If the weights are required to be genuinely optimal, one must optimize for the new interval again; inequality (3) preserves the existence of a violation.

## 4. Why periodic replication with unchanged prices does not amplify surplus

This section answers a proposed amplification mechanism; it is not a restricted-support substitute for the general problem.

Fix a nonempty finite P, fixed positive prices w_p, and c>1. Choose p0 in P, put

    e=ceil(c/w_{p0}),
    gamma0=(c-1)p0^{-e}>0.

Choose an integer L>=e so large that

    tau_L=sum_{p in P} w_p/[p^L(p-1)]<=gamma0/2.

Set

    X_L(n)=sum_{p in P}w_p min(v_p(n),L),
    Q=product_{p in P}p^L,
    W=sum_{p in P}w_p.

The truncated load is Q-periodic. Over one full period, the average gap

    (X_L-1)_+-(X_L-c)_+

is at least gamma0: on the fraction p0^{-e} of residues divisible by p0^e, the load is at least c and the gap is c-1.

The prefix raw tail satisfies

    sum_{a<=M}(X_w(a)-X_L(a))
      <=M sum_{p in P}w_p sum_{j>L}p^{-j}=M tau_L.

Each truncated hinge has size at most LW. Its sum over an arbitrary M-term interval differs from M times its period average by at most QLW. Hence, uniformly for every actual shift,

    J_c(w;M,I)
       <=-gamma0*M+M*tau_L+2QLW
       <=-(gamma0/2)M+2QLW.                             (4)

Thus a fixed finite collection of prices eventually has strictly negative surplus in every interval. Concatenating periods or dilating the ambient length while retaining that same price system cannot amplify a positive finite surplus.

The constants in (4) depend on P and w. This argument does not rule out an amplification that introduces more active primes and changes prices. No such valid prime-growing amplification has been constructed here. In particular, the equivalence between a uniform O_c(1) bound and exact nonpositivity has not been established.

## 5. At a positive global extremum the linear moment surplus is o(n)

This consequence uses the previously established absolute linear cover bound F(B,I)<=C0|B| and the ambient quadratic gate M>=16|B|^2 => F(B,I)<=2|B|. Any valid fixed absolute C0 suffices; its numerical optimization is irrelevant here.

Choose a positive global surplus maximum over weights and shifts at the fixed M, in the bounded-exponent pattern space of Section 3. Apply the zero-demand-coordinate normalization from Section 1: it preserves the same full tail and maximum value, and does not change the interval or its bounded-exponent pattern. Let this full tail have size n, value J_c=e>0, and F=cn+e. Thus the active support is contained in the set of primes dividing the sources.

For every a in A, global surplus maximality gives

    F(A\{a},I)<=c(n-1)+e=F-c.                          (5)

Every source prime p satisfies

    p<F-c+1<C0 n.                                      (6)

For otherwise, choose a source a divisible by p and an optimal fractional cover of A\{a}. The bank of multiples of a/p has at least p members. Its remaining total target capacity is at least p-(F-c)>=1. Buying exactly one unit of that capacity supplies the entire cofactor a/p; the only possible remaining source deficit is one p-unit. Full-interval p-valuation dominance allows that deficit to be repaired at cost at most one. The total cost is at most F-c+2<F, a contradiction.

Because all zero-demand coordinates have been removed, (6) applies in particular to every active prime. This is the justification for restricting the active-prime sum in (7) to primes below C0 n.

The quadratic gate gives M<16n^2. Since actual target exponents are capped as in Section 3, ordinary multiple counts now imply the exact bounds

    0<=sum_{b in I}X_w(b)-sum_{a<=M}X_w(a)
      <=sum_{p active} e_p
      <=2*pi(C0 n)+pi(sqrt M)+O(M^{1/3}log M)
      =O(n/log n).                                     (7)

For the middle inequality, expand e_p=1+floor(log_p M) into prime-power levels. Each prefix/interval count difference is zero or one. At the final allowed exponent p^{e_p}>M the prefix count is zero, and all higher actual target counts vanish. The levels j>=3 contribute at most O(M^{1/3}log M).

Thus the full raw linear moments differ by o(n) in this normalized extremal setting. Equation (7) is a genuine consequence of moving to an actual bounded pattern and then optimizing again; it is not a truncation of the rows of an arbitrary original interval. It controls the linear moments, not the nonlinear hinges, so the desired surplus estimate still does not follow.

## Conclusion

Global maximization supplies genuine raw optimality for its full source tail. Rational vertices and actual target-tie bases are available. Optimizing over shifts permits a genuine CRT reduction of high target powers, with a changed interval, and bounds the raw linear moment surplus by O(n/log n) at a positive extremum. Fixed-price periodic replication has a negative linear drift. None of these facts provides the missing quantitative uniform bound for the global surplus.
