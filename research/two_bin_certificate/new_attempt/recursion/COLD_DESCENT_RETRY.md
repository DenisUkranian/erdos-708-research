# Cold-descent retry after the full-prefix kernel counterexample

24 November 2026. This note does not establish the general asymptotic.
The user's deficit Theta(M^(10/17)) concerns the full kernel sum and has
an empty high-load source tail; it does not contradict a square-root
bound for the genuine surplus Delta_c(M).

## 1. The exact remaining arithmetic obligation

The existing quotient construction is valid. For a cold d, tau=1-X(d)>0,
N=floor(M/d), trimming a possible extra endpoint in the quotient target
and clipping w/tau gives a genuine interval instance Q_d at length N.
The new-tail, endpoint, and clipping reserves all have the favorable
sign and must be retained.

An inequality J_c <= (4/3) max(0,max_d Q_d)+C_c sqrt(M), on an appropriate
genuine maximizing pair, would imply Delta_c(M)=O_c(sqrt(M)); together
with the previously proved near-quadratic exclusion and a decrease of
the source budget, it would give the intended asymptotic. The existing
papers do not prove this arithmetic inequality. The linear selector
optimization does not strengthen it: under that selector's single
linear cost constraint the optimum is attained at one cold divisor.

The formal six-coordinate unique global optimizer in the earlier
descent audit has all formal cold quotients negative. Thus globality,
complete rows, all abstract orthants, and the favorable quotient
reserves alone are insufficient. The exact numerical floor(M/d) laws
must be used before any successful inference of this kind.

## 2. An exact phase-averaging fact for a zero-load divisor

The following small arithmetic fact is proved here. It does not have
the contraction coefficient needed to close the problem.

Fix c>2, M, finitely supported nonnegative weights w, an actual target
interval I of M positive integers, and an integer d in [2,M] with
X(d)=0. Put

    S_c(t)=sum_{a<=t}(X(a)-c)_+,
    H(I)=sum_{b in I}(X(b)-1)_+,
    N=floor(M/d).

There exists another actual interval I' of length M with exactly the
same sequence of loads as I, and an N-element consecutive interval Q
of quotients of the d-multiples in I', such that

    J_c(w;N,Q) >= S_c(N)-H(I)/d.                       (1)

Deleting weights on primes larger than N and clipping, if necessary,
can only improve the quotient surplus. In particular, at an extremum
over shifts the newly selected parent shift is tied with the old one.

Proof. Partition the M positions of the old interval by their index
modulo d. Each class has N or N+1 positions. From a class with N+1
positions remove one endpoint. The trimmed classes have total target
hinge at most H(I), so some trimmed class costs at most H(I)/d.

Every prime dividing d has zero weight and is coprime to every active
prime. For each active prime q, choose an exponent E_q exceeding all
q-valuations attained on the old interval. The Chinese remainder
theorem permits a new shift which preserves the old shift modulo every
q^(E_q+1), while making precisely the selected index class consist of
multiples of d. Consequently all active valuations, and hence every
load on the M positions, are preserved exactly. The shift can be made
positive by adding a common modulus.

The quotients of the retained consecutive d-multiples form N consecutive
positive integers. Since X(d)=0, their loads equal the parent loads.
Their target hinge is therefore at most H(I)/d, while their source
hinge is S_c(N). This proves (1), including every prime power.

Rearranging (1) gives the exact sufficient estimate

    J_c(w;M,I) <= d Q_d + S_c(M)-d S_c(floor(M/d)),    (2)

for this realizable quotient Q_d and a tied parent shift.

## 3. Why this is not the missing recurrence

The coefficient of Q_d in (2) is d, not a contraction compatible with
the square-root scale. For d=2 it is 2, already larger than sqrt(2).
The source dilation term S_c(M)-d S_c(floor(M/d)) can also be much
larger than sqrt(M): take unit weights on primes in (4P,5P], M=125P^3,
and 2<c<3. All high-load sources are triple products in (M/2,M], so
S_c(floor(M/d))=0 for every d>=2, whereas S_c(M) has order
P^3/(log P)^3. The old exact row/union audit proves that actual target
banks more than compensate this source concentration. Thus source
dilation alone cannot be discarded or bounded at square-root scale.

Also, a zero-load divisor d>=2 is not guaranteed for a prescribed
weight system. Tiny positive support padding, or genuinely positive
prices on all small primes, prevents assuming that such a divisor is
small. No claim is made that the lemma selects a useful d at every
global optimum.

## 4. Outcome

No new inequality controlling the genuine signed surplus by O_c(sqrt M)
was proved in this retry. In particular, there is no justified transfer
from the user's empty-tail kernel counterexample to the genuine
surplus, and no justified inference of cold descent merely from the
finite-variation identities. The missing compensation-or-localization
estimate remains arithmetic: target banks must pay the concentrated
source dilation term whenever no suitably strong shorter surplus is
present.
