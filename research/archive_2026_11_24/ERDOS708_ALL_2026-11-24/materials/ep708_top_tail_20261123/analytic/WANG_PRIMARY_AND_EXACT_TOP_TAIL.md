# Primary-source verification and the exact top-tail target

## Status

This is a verification of the cited transfer and quadratic gate, not a new transference theorem. It also records exactly which finite source maximization gives the requested top-tail expression. No per-instance rounding assertion is assumed or reproved here.

## 1. Primary files actually checked

The current primary files were fetched through the GitHub connector on 23 November 2026. Ordinary web retrieval returned `DisabledError`; the connector returned the full requested source content and the following Git blob identifiers:

* [raw-transfer.tex](https://github.com/science-prince/erdos-708-interval-divisor-covers/blob/main/papers/main-paper/raw-transfer.tex), blob `652a6c28dc52abd22116084746aff569021207a7`;
* [main.tex](https://github.com/science-prince/erdos-708-interval-divisor-covers/blob/main/papers/main-paper/main.tex), blob `17f471ea0073e00e8b0245505a62529c643cbf60`.

The definitions are in main.tex, lines 22--35; the quadratic appendix is at lines 268--362. The raw theorem and its proof are in raw-transfer.tex. Only links and content identifiers are reproduced here; this note does not redistribute the external source files.

## 2. Domains and the raw transfer

An original source set consists of n distinct integers at least two, with maximum M. The interval has exactly M consecutive integers. Raw fractional programs are defined on positive intervals, with one row for each demanded prime and the genuine box constraints 0<=x_b<=1:

    L_raw(A,I)=min sum_{b in I} x_b,
    subject to sum_{b in I}v_p(b)x_b >= D_p(A).

Let ell(n) be the supremum of this raw value over positive original instances, and h(n) the analogous demand-capped supremum. The source states

    ell(n)<=h(n)<=g(n),
    limsup g(n)/n = limsup h(n)/n = limsup ell(n)/n.

More precisely, with

    G_n=max_{0<=m<=n}[ell(m)+2(n-m)],
    K_n=ceil(G_n),       Z_n=2K_n,

the finite raw envelope is

    g(n)<=K_n+pi(Z_n)-1.

This raw theorem has **no restriction on M relative to n**. Its proof uses the existing finite linear bound to control the envelope, but it does not assume a fractional constant at least three. The condition c>=3 in main.tex belongs to a different, demand-capped transfer theorem.

The theorem does not claim that an arbitrary raw feasible vector is demand-capped feasible. It also does not claim a pointwise estimate tau(A,I)<=L_raw(A,I)+o(n). These distinctions are explicit in the primary source.

An unrestricted uniform raw bound

    ell(n)<=(2+o(1))n

therefore suffices for the requested unrestricted asymptotic. Here the error is a function of n alone, uniform over both M and the interval shift.

## 3. The exact quadratic gate, including the ambient version

The primary appendix proves

    M>=16n^2  ==>  tau(A,I)<=2n.                         (1)

The printed statement uses an original instance with max A=M. Inspection of the proof shows that it only uses

    A subset {2,...,M},   |A|=n,   |I|=M;

equality max A=M is not used. Consequently the same proof gives the ambient version of (1) whenever the sources lie below the interval length M.

The constants in the proof check as follows. Put Y=M/n and D=M^(2/3). For a difficult divisor type d, define u_d=d/p_d, where p_d is its least prime, k_d=floor(n/u_d)+1 and q_d=floor(M/d). The source's estimates give

    m_d/q_d <=1-u_d/(4n),
    c_de/(q_d q_e) <=2M u_d/(M-D)^2.

Since n>=2 implies M>=64, one has D<=M/4. The total off-diagonal contribution is at most

    32 u_d n/(9M) <=2u_d/(9n).

The resulting row sum is at most 1-u_d/(36n), strictly below one. This is the stated Hall step. The later ordinary-factor and residual placements use at least n and at least floor(sqrt M)>=4n candidate positions, respectively. None of these steps needs a source equal to M.

Thus a possible failure at coefficient greater than two lies in M<16n^2. This removes a range; it does not establish the raw estimate in the remaining range.

## 4. Exact maximization over source sets with maximum M

Fix M>=n+1, a positive interval I={x+1,...,x+M}, and nonnegative prime weights. Primes exceeding M do not occur in any source and can be set to zero. The boxed raw dual can be optimized with 0<=w_p<=1, p<=M. Put

    X_w(a)=sum_{p<=M}w_p v_p(a),
    H_I(w)=sum_{b in I}(X_w(b)-1)_+.

For fixed w, maximization over all n-element A subset {2,...,M} with max A=M is exactly

    X_w(M)+Top_{n-1}{X_w(a):2<=a<M}-H_I(w).             (2)

Top_0 is zero. The forced M term must not be replaced by an unrestricted Top_n without explanation. Since there are finitely many candidate source sets, their maximum commutes with the dual supremum. Thus (2), uniformly bounded by 2n+o(n), is exactly the unrestricted raw target at this fixed M and shift, rather than a weaker sampled-source version.

To justify clipping, lowering one w_p>1 to one leaves the target hinge linear on every affected column and changes the objective by

    (w_p-1)[sum_{b in I}v_p(b)-D_p(A)]>=0.

The full interval supplies every row. Weights on primes absent from A can also be set to zero without reducing the fixed-A objective.

## 5. Which top-source properties are legitimate

Ties in Top can be broken in favor of larger integers. This makes the selected set a divisibility upset in {2,...,M}: if a is selected and ka<=M, then ka is selected too. The forced M term is consistent with this rule.

For a source-minimal raw failure at a coefficient c>2, every selected source has X_w(a)>c, including a=M. Deleting any source with load at most c would preserve a failure. If deletion lowers the maximum source, the shorter original interval can be chosen inside the old ambient interval; a feasible vector on it extends by zero. This is why the ambient/original distinction does not invalidate the deletion argument.

These facts do not give coordinatewise product dominance for the union of prime-deletion banks. The companion note `TOP_TAIL_BANK_COUNTERLEMMA.md` gives an exact full-superlevel example with all source loads at least 11/5 where that coordinatewise assertion still fails. The remaining optimal-row conditions must therefore be used, not discarded.

## 6. Remaining scope

The primary transfer, its domains, the constant 16 in the quadratic gate, and formula (2) have been verified. None supplies the missing uniform estimate in (2). The general asymptotic claim remains unproved in this work.
