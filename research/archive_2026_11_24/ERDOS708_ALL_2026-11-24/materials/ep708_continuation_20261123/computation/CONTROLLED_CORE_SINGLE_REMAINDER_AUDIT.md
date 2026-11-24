# Independent audit: controlled substantial core and one-prime remainders

Date: 2026-11-23.

Audited candidate: `../analytic/CONTROLLED_CORE_SINGLE_REMAINDER.md`, first
in its coordinate-cap version and then with the stronger aggregate-core
cap. Sections 1–8 below record the first audit; Section 9 audits the
subsequent sharp upgrade and supersedes the older A+B|R| bound.

## Verdict and scope

**PASS on both versions, including the sharp aggregate-cap upgrade.** No substantive
mathematical correction is required. The conditional diffuse input is the
previously audited theorem with at most k excluded primes. The present proof
correctly turns its negative shifted levels into one exceptional upper-set
count and controls that count by finite divisor differences.

The latest error is `B_{epsilon,k}(1+|R|)`, with
`B_{epsilon,k}<=D_epsilon^k`, and is independent of M. The sharper
source-dependent version is `B+sum_r min(B,m_r)`. The proof
allows arbitrary powers of the one distinct R prime in a source, arbitrary
nonnegative raw substantial/remainder weights, and arbitrarily large shifts.

This is an internal audit, not formal verification or external referee
approval. The result does not remove the exponential dependence on k and
does not settle unrestricted Erdős 708.

## 1. Uniform choice eta=c_epsilon/(k+1)

For 0<epsilon<=1, the cited error bound satisfies

    e_k(t)<=epsilon/16 when t>=16k+R_epsilon

after fixing R_epsilon. The two relevant exponential factors are bounded by
`3^k*2^(-t/4)` and `4^k*2^(-t/2)`, so a threshold linear in k is sufficient.

With `(1+epsilon)/c_epsilon>=max(32,2R_epsilon+2)`, taking the floor in
`r=floor((1+epsilon)/eta)` still gives the needed bounds for r, j, and kappa.
In particular j>=k+1, so the high-power error `eta*2^(k+1-j)` is at most eta.
The conditional comparison therefore follows from

    (1+epsilon/16)(1+epsilon/2)+eta
      <=(1+epsilon-eta)(1-epsilon/16).

The difference of right and left sides is

    3epsilon/8-3epsilon^2/32-2eta+eta*epsilon/16,

which is positive for eta<=epsilon^2/128 and 0<epsilon<=1. Thus one
c_epsilon works simultaneously for every k and every choice of excluded
prime values. The epsilon>1 case follows from epsilon=1 by monotonicity.

Light primes above M are explicitly removed before the mean split. The
high-mean branch is therefore legitimate and gives zero error. Removing
them changes no source load; restoring them only increases the target.

## 2. Finite differences of the capped exceptional upper set

Let the actual heavy set have f<=k primes and weights w_i>eta. Put
`b_i=ceil(1/w_i)`. Each capped profile `u_i(j)=min(w_i*j,1)` is constant
from exponent b_i onward.

The coefficient at a multi-index j is the alternating difference over only
its positive coordinates. This is the correct divisor-inversion formula;
zero coordinates do not introduce an invalid subtraction-one corner. It
telescopes exactly to `1_{Z(n)>s}`.

If any j_i>b_i, the two layers in that coordinate coincide and the
coefficient vanishes. On the remaining grid, put z_i=(j_i-1)_+. Then
z_i<b_i, so `u_i(z_i)=w_i*z_i` exactly, including weights greater than one.
If the minimum-corner load exceeds s, all corners equal one and the
alternating sum cancels. The zero multi-index has coefficient zero because
s>=0 and the zero load does not exceed s. Thus every nonzero coefficient
must obey

    eta*sum_i z_i<=s.

Stars and bars gives `binom(f+floor(s/eta),f)` possible z-vectors; each has
at most 2^f preimages j, and each coefficient has absolute value at most
2^f. Hence the L1 norm is at most

    4^f binom(f+floor(s/eta),f)
      <=4^k binom(k+floor(s/eta),k).

This support bound is valid at s=0 and at the endpoint s=1. No assumption
that the exceptional upper set is a nested chain is made.

## 3. The one-sided divisor-count discrepancy has the correct sign

For each positive integer divisor d and each half-open real interval J of
length T_0, its target count is at least floor(T_0/d) and at most that count
plus one. Therefore its prefix count minus target count lies in [-1,0].
Positive divisor coefficients contribute nonpositively to the exceptional
upper-set defect; each negative coefficient contributes at most its absolute
value. The L1 estimate consequently proves the claimed upper bound,
uniformly in the real length, shift, and actual prime sizes.

This handles the known fact that a two-prime upper set may contain fewer
points on a shifted interval than on the prefix. The proof bounds this
possible positive defect instead of asserting it is zero.

## 4. Negative exact-core levels are summed globally

At exact F-smooth part h, the shifted target level is s-Z(h). For Z(h)<=s,
the conditional diffuse theorem is applied at real length T_0/h and a
nonnegative threshold. Its source-to-target defect is nonpositive.

For Z(h)>s, the target condition is automatic. The source count is bounded
by all prefix integers with that exact F-part. Summing ALL these negative
pieces, including every target exact part h>T_0, gives precisely the
prefix-minus-target count of `1_{Z>s}`. Consequently the level defect is
bounded by the signed upper-set discrepancy before its finite-difference
upper bound is applied.

There is no separate error per h and no replacement of the exceptional
condition by an unrestricted count on the wrong side. The comparison also
remains valid when the signed exceptional discrepancy is negative.

## 5. The base and per-R errors are those claimed

For target levels s in [0,1], the finite-difference variation is at most

    B_{epsilon,k}=4^k binom(k+floor(1/eta),k).

For the base hinge, integrate the level comparison over s>=1. The source
threshold is s+ell, so this gives the source hinge at c=1+ell=2+epsilon.
Since the entire capped exceptional load is at most k, the exceptional
event vanishes for s>=k. Its integrated error is therefore at most

    A_{epsilon,k}=(k-1)_+ 4^k binom(k+floor(k/eta),k).

The integration interval is empty for k=0 or 1, as stated. For k=0 the
level error also vanishes, so both constants can be set to zero.

For a fixed R prime, each prime-power increment has integration variable
v in [0,1], hence target threshold 1-v in [0,1]. After division by r^j,
use an N-term target subinterval, with N=floor(M/r^j). The comparison
incurs at most B at that level. When N=0 the prefix contribution is zero.

Crucially,

    sum_{j>=1}(u_r(j)-u_r(j-1))<=1.

Thus the TOTAL integrated error for that prime is at most B, independent
of the number of powers considered and of M. The core C is invariant under
r-powers because F, the light core, and R are disjoint.

## 6. Source identity, one target hinge, and all raw tails

At each source at most one capped R coordinate is nonzero. Its hinge is
therefore one core base hinge plus the sum of individual R increments.
The base estimate is applied once; the per-prime estimates add B|R|.
The target increments obey the same superadditive inequality already
audited for the diffuse-core theorem and fit into one shared target hinge.

All heavy F and all R coordinates were capped. Their raw tails are restored
TOGETHER. If their total tail T is positive, at least one corresponding
capped coordinate equals one, so C+U>=1. Hence the target hinge equals
`T+(C+U-1)_+`, while the source hinge is at most `T+(C+U-c)_+`.
Every tail is a nondecreasing prime-power profile, so its source-subset sum
is no greater than its full prefix sum and then no greater than its target
sum. No additional error is introduced by unbounded raw weights or powers.

Removing R coordinates absent from the sources is legitimate: they change
no source load and only decrease the target load. Thus the sharper count of
active remainder primes can indeed replace the size of a larger supplied R.

## 7. Growth rates and the meaning of exclusion

For k>=1, `floor(1/eta)<=(k+1)/c_epsilon<=2k/c_epsilon`. The standard
binomial bound yields

    B_{epsilon,k}<=[4e(1+2/c_epsilon)]^k=D_epsilon^k.

The analogous estimate with `floor(k/eta)<=k(k+1)/c_epsilon` gives
`A_{epsilon,k}=exp(O_epsilon(k log(k+1)))` as an upper bound. These are
independent of M and of the actual weights and primes.

If active |R|=O(n/log n) and
`k<=(1-delta)log log n/log D_epsilon`, then

    B|R|=O(n/(log n)^delta)=o(n),
    A=n^{o(1)}=o(n).

The resulting raw objective is at most `(2+epsilon)n+o(n)`. This excludes
a FIXED POSITIVE LINEAR excess over that expression, not an arbitrarily tiny
positive excess over exactly `(2+epsilon)n`. To exclude a putative violation
of `(2+epsilon)n`, apply the theorem with epsilon/2 first and absorb the
o(n) term. This is the only scope clarification recommended.

## 8. Integer source-class consequence to be stated separately

The audited bounds support the separate transfer proof for source sets with
a core of k(M)=o(log log M) arbitrary primes and at most one DISTINCT
outside prime per source, arbitrary powers allowed. At a minimal failing
subset of size m in the fixed ambient interval, prime deletion forces every
active prime below c*m. Thus both active |R| and the number of LP rows are
at most pi(c*m). Rounding adds that row count, producing total error

    A_{epsilon,k(M)} + (B_{epsilon,k(M)}+1)pi(c*m).

The quadratic gate forces m>sqrt(M)/4. It follows that A=M^{o(1)}=o(m)
and `(B+1)pi(c*m)=o(m)`. This is a restricted uniform integer asymptotic
class, to be proved in `../sections/transfer.tex`. It does not handle the
much larger core still allowed by the general minimal-counterexample
structure.

## 9. The stronger aggregate-core cap: separate audit and current result

**Verdict: PASS.** Replace the sum of individual F-coordinate caps by

    X_F(n)=sum_{q in F}w_q v_q(n),
    Z(n)=min(X_F(n),1),    T_F(n)=X_F(n)-Z(n).

Keep the separate capped R profiles, their sum U, and their exact raw tails
T_R. The full capped core is now C=V+Z, and the total load is
`X=C+U+T_F+T_R`.

### Exact-part conditioning remains valid despite the nonlinear cap

Z depends only on the exact F-smooth part h, so it is constant on each
conditioned fibre. V is unchanged after dividing by h. The conditional
diffuse comparison therefore applies exactly as before at shifted level
s-Z(h). Nonlinearity of the aggregate cap causes no additional condition.

For s>=1 there are NO negative shifted levels, since Z<=1. Hence the
capped-core base hinge comparison has zero additive error after integrating
over s>=1. This replaces the earlier A_{epsilon,k} term.

For 0<=s<1, the event Z>s is exactly the event

    sum_{q in F}min(w_q v_q(n),1)>s.

If any raw coordinate reaches one, both events hold; otherwise the summed
individual caps equal X_F. Thus the previous finite-difference estimate
applies without change on this level range. At s=1, Z>s is empty and is
handled directly; the event equivalence is not claimed at that endpoint.

### Both discrepancy signs and the aggregate-tail balance

Each divisor's target count minus prefix count belongs to [0,1]. Therefore
the same L1 variation bound B controls BOTH signs of the upper-set count
discrepancy. Integrating over 0<=s<1 gives

    |sum_prefix Z-sum_target Z|<=B.

The unbounded raw heavy load X_F is additive in prime-power indicators, so
its target sum is at least its prefix sum. Consequently the direction of
the aggregate-tail estimate is

    sum_prefix T_F-sum_target T_F
      <=sum_target Z-sum_prefix Z<=B.

The source-subset sum of T_F is no greater than its prefix sum because T_F
is nonnegative. This reasoning does not incorrectly assume that T_F itself
has nonnegative prime-power increments; generally it need not.

The R tails still have exact prefix-to-target domination separately. If
T_F>0, then Z=1. If T_R>0, then one R cap equals one. Thus any positive
total tail forces C+U>=1, and

    (X-1)_+=T_F+T_R+(C+U-1)_+

holds exactly on the target. The source hinge has the corresponding upper
bound with threshold 2+epsilon. Restoring the tails adds only B, so

    Delta_{2+epsilon}(A,I,w)<=B(1+|R|).

All these comparisons remain valid for arbitrary nonnegative raw weights,
including unbounded weights, and for arbitrary powers in the sources.

### Source-dependent remainder refinement

Let m_r count the sources divisible by r. Each capped source increment at r
is at most u_r<=1, while target increments are nonnegative. Its defect is
therefore at most m_r. The previous level argument bounds that same defect
by B, so it is at most min(B,m_r). Summing and restoring the aggregate tail
gives the valid refinement

    Delta_{2+epsilon}(A,I,w)<=B+sum_r min(B,m_r).

This counts the core-tail error once. Since each source has at most one
distinct R prime, sum_r m_r<=|A|, although that coarser estimate alone does
not give the desired asymptotic result.

### Updated transfer convention

The current `../sections/transfer.tex` uses the sharp error

    B_{delta,k(M)}+(B_{delta,k(M)}+1)pi(c*m),

with no A term. All prior uniform integer conclusions remain valid. The
small-core result still requires k(M)=o(log log M) because of the possible
number of active remainder primes, not because of a separate base error.
