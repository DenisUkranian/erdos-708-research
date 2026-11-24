# A complete finite CRT model for the H2 search

## Scope

This note gives a rigorous finite reduction and documents adversarial searches.
It proves neither H2 nor either version of Erdős Problem 708. Numerical mixed
integer solver bounds are not presented as exact-arithmetic proof certificates.
All phase patterns below are realizable on an actual interval of consecutive
positive integers by the Chinese remainder theorem.

Write

\[
\Delta_2(M,x,w)=\sum_{a=1}^M(X_w(a)-2)_+
 -\sum_{j=1}^M(X_w(x+j)-1)_+,
\qquad X_w(b)=\sum_{p\in P}w_pv_p(b).
\]

## Lemma 1: large-prime pruning

For the purpose of maximizing Delta2 at a fixed M, weights on primes p>M/4
may be set to zero. Indeed, if p divides an integer a<=M with Omega(a)>=3,
then the two remaining prime factors, counted with multiplicity, imply
4p<=a<=M. Thus every source affected by such a prime has Omega(a)<=2 and
cannot contribute to the left hinge for any weights in [0,1]. Removing the
weight leaves the left side unchanged and cannot increase the right side.

This statement uses the full Omega, not the weighted number of factors.
It is independent of any unproved covering or matching assertion.

## Lemma 2: at most 2M relevant patterns per prime

Fix p<=M and let E=floor(log_p M), d=p^E, Q=p^(E+1)>M. For minimization of
the right hinge, there is no need to retain valuations greater than E+1.
There is at most one interval index j with p^(E+1) dividing x+j; changing
the next p-adic digit of x can keep its valuation exactly E+1 while leaving
all lower valuations unchanged. Other primes are independent by CRT.

Index the phase by s=-x mod Q. For each fixed r=s mod d, the lower E levels
are fixed. Among its p possible next digits, each s in {1,...,M} gives a
single position of valuation E+1. All s outside {1,...,M} give the same
pattern for this r, and only one representative is needed. There are M
occupied next-digit choices in total and at most d empty representatives.
Thus at most M+d<=2M valuation vectors suffice.

These representatives are exact, not relaxations. For an occupied s, use
-x congruent to s+Q modulo pQ, making the high position have valuation
exactly E+1. For an empty s, use -x congruent to s modulo pQ. CRT combines
these congruences for all p in P; its least nonnegative representative x
already gives a positive interval {x+1,...,x+M}.

Consequently a counterexample for fixed M,P exists if and only if one
exists among these finite combinations of patterns and weights in [0,1].
The infinitely many possible shifts introduce no additional patterns
relevant to this minimization.

## Exact one-prime coordinate optimization

For fixed contributions Y_j from other primes and fixed weight w_p, write

\[
 (Y_j+w_pv_p(x+j)-1)_+-(Y_j-1)_+
 =\sum_{h=1}^{v_p(x+j)}\big[(Y_j+hw_p-1)_+
 -(Y_j+(h-1)w_p-1)_+\big].
\]

At level h, the contribution is the sum of its nonnegative increments over
one residue class modulo p^h. The residue classes at successive levels
must be compatible. A bottom-up minimum on the p-adic tree finds the exact
best coordinate phase. At the final level, a missing child has zero cost;
if all p children contain interval positions, one higher valuation is
unavoidable and its least increment must be paid. Ignoring this last case
would be an incorrect truncation.

The implementation was compared with exhaustive phase enumeration in 55
cases, all primes p<=M for 2<=M<=15, with nontrivial rational loads/weights.
The proof above, rather than those tests, justifies the general reduction.

## A global mixed integer formulation

For each p, select one valuation vector v[p,r] using binary y[p,r]. Let w_p
be continuous in [0,1], and use u[p,r]=w_p*y[p,r]. The usual exact binary
linearization is

- 0<=u[p,r]<=w_p;
- u[p,r]<=y[p,r];
- u[p,r]>=w_p+y[p,r]-1;
- sum_r y[p,r]=1.

The interval hinge h_j is constrained by

\[
 h_j\ge0,\qquad h_j\ge\sum_{p,r}v[p,r]_j u[p,r]-1.
\]

For each source a with Omega_P(a)>2, let K_a=Omega_P(a)-2 and introduce
binary z_a and continuous t_a satisfying

\[
 0\le t_a\le K_a z_a,\quad
 t_a\ge X_w(a)-2,\quad t_a\le X_w(a)-2z_a.
\]

These equations force t_a=(X_w(a)-2)_+. Minimizing sum_j h_j-sum_a t_a
therefore gives minus the global maximum of Delta2 for this fixed M,P.
The code uses floating-point HiGHS to search this exact mathematical model.
Any candidate violation is re-evaluated using rational weights and integer
valuations; a solver status alone is not a proof certificate.

## Executed searches and limits

- `h2_crt_search.py`: 15,398 local CRT/LP trials, M from 40 to 2,000,
  initial supports of 6 to 12 primes. No positive Delta2 was found. Some
  supports contained irrelevant large primes, which the later pruning
  observation removes. This is not exhaustive.
- `h2_ratio_search.py`: 5,992 local searches for the raw fractional covering
  coefficient, M up to 4,000. The best exact exhibited dual ratio was 44/35
  with 11 nonzero prime weights. This is a lower-bound witness, not an upper
  bound, and has no claimed novelty. Sharpness constructions approaching 2
  are already known, so this finite value is not progress on the conjecture.
- `h2_global_phase_milp.py`: five bounded runs at fixed rational weights.
  For M=40 and P={2,3,5,7,11,13}, all weights one, the solver returned a
  global phase minimum RHS=42, while LHS=18. Other runs reached their
  time limits. Numerical dual bounds are recorded separately.
- `h2_joint_milp.py`: bounded global phase-and-weight runs. M=20 returned
  objective zero; M=40 and M=60 reached time limits with no violation.
  All three sizes are already covered by Chen's capped-atom reduction
  and the five-prime theorem (raw H2 for M<78), and are only implementation
  checks. They are not new mathematical finite cases.
- `h2_hinge_ratio_search.py`: the adaptive follow-up directly maximizes the
  nonzero hinge ratio LHS/RHS, avoiding the zero-weight stationary solution.
  5,155 starts were completed, with best exhibited ratio 636/1039<1.
- `h2_sparse_region_search.py`: 663 starts (572 with nonzero initial left
  hinge) restricted to M>100 and the necessary region
  sum min(X_w(a),2)<M, using small and clustered medium primes. No violation.
- `h2_six_prime_search.py`: the same region with exactly six supporting
  primes and an additional search restriction w_p>=1/10, preventing local
  collapse to the already known at-most-five-prime setting. No violation
  was found; final counts are in its JSON file.

All search seeds and budgets are in the scripts. `*_results.json` files
contain the rational evaluations and CRT phases. None of these searches
excludes a counterexample with different M, support, weights, or phases.

## Independent mathematical audits

The proofs in `../analytic/AMPLIFICATION.md` and
`../analytic/SPARSE_SUPPORT_H2.md` were independently rederived and checked.
No substantive error was found in either. The latter
proves H2 for all M and shifts under
3 sum w_p/(p-1)+sum 1/p+(|P|+1)/y<=1 when every p>=y.
These are rigorous partial conclusions, unlike the search non-findings.
No literature-priority assertion is made.
