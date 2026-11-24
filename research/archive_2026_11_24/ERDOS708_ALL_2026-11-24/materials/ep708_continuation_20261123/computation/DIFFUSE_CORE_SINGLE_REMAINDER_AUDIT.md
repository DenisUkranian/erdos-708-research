# Independent audit: diffuse core and one distinct remainder prime per source

Date: 2026-11-23.

Audited candidate: `../analytic/DIFFUSE_CORE_SINGLE_REMAINDER.md`, Sections
1–8 and the stated dependencies, followed by the subsequently written
Section 9. The base result and the one-substantial-core-coordinate
extension were checked separately; see Section 7 below for the latter.

## Verdict

**PASS.** The proof establishes the stated source-specific hinge inequality
at threshold 2+epsilon. No substantive correction is required. The argument
handles arbitrary powers of the one allowed remainder prime and arbitrary
nonnegative remainder weights. It does not require separation of prime
sizes, bounded reciprocal mass, or bounded cardinality of the remainder
support.

The conclusion is restricted to vectors whose core weights are diffuse.
It does not establish the unrestricted fractional or integer conjecture.
The audit relies on the previously audited uniform diffuse level comparison
and its high-mean moment bound; those include the standard fundamental-lemma
input. This is an internal mathematical audit, not formal verification or
external referee approval.

## 1. Parameters and all-scale use of the level comparison

For 0<epsilon<=1, put ell=1+epsilon and c=2+epsilon. With

    rho=(1+3epsilon/4)/(1+epsilon),

the limiting ratio in the candidate's parameter condition is

    (1+epsilon/2)/(1+epsilon) < rho < 1.

Hence a positive eta can indeed be chosen to satisfy that condition together
with eta<=epsilon^2/128 and the required carrier cutoffs. The denominator
`(ell-eta)(1-e(r))` is positive for sufficiently small eta.

The source and target carrier coefficients differ by precisely this ratio.
Retaining it in the existing diffuse proof gives the displayed strict
level comparison, not only a non-strict coefficient-one bound. It holds at
each smaller rescaled length. Core primes above such a length change no
prefix load and can be removed for the comparison, then restored on the
target side. Removing them decreases the mean. Thus no unsupported
short-interval or support-invariance assertion is used.

Core primes above the original M are discarded before the high/low-mean
split. This preserves every source load and only reduces target loads.
For epsilon>1, the theorem at epsilon=1 suffices by monotonicity.

## 2. The high-mean branch remains valid with all remainder weights

The condition eta<=epsilon^2/128 is exactly the previous moment threshold
with delta=epsilon/2. Consequently core mean at least 1+epsilon/2 implies

    sum_{a<=M} min(V(a),2) >= M.

Adding any nonnegative remainder load preserves this inequality. Moreover,
prime-power counts in the target interval dominate their prefix counts
separately, even for arbitrary nonnegative remainder weights. Therefore

    Delta_2(X) <= M-sum_{a<=M}min(X(a),2) <= 0.

Restricting the nonnegative source hinge to A and increasing its threshold
to 2+epsilon are both safe. This branch needs no one-remainder-prime source
restriction.

## 3. Exact source increments: the base is counted once

For the low-mean branch write

    H_h(v)=(v-h)_+,
    D_{h,r}(n)=H_h(V(n)+u_r(v_r(n)))-H_h(V(n)).

All increments are nonnegative. The candidate's prime-power telescoping
formula is exact: it is the integral of the derivative of the hinge, with
possible endpoint equalities affecting only a set of integration measure
zero.

On a source a with at most one distinct R prime, at most one capped
coordinate u_r is nonzero. Hence

    H_c(V(a)+U(a))=H_c(V(a))+sum_r D_{c,r}(a).

The proof correctly uses this identity only on A. It does NOT assert the
same identity for all prefix integers, which may contain multiple R primes.
After the identity is used, its nonnegative terms can be enlarged separately
from the distinct subset A to the full prefix. The base term is enlarged and
charged exactly once.

For each prime-power increment the integration variable v lies in [0,1].
Thus the target threshold s=1-v is nonnegative, and the source threshold is
`c-v=s+ell`. This keeps every application inside the proved level-comparison
range. Because E and R are disjoint, `V(r^j t)=V(t)`.

Prefix multiples of r^j rescale to a prefix of length floor(M/r^j); target
multiples rescale to a consecutive interval containing at least that many
integers. A subinterval of exactly the prefix length may be selected. Extra
target positions have nonnegative contributions. If the prefix length is
zero, its contribution vanishes. This proves the individual increment bound

    sum_prefix D_{c,r} <= rho sum_target D_{1,r}

uniformly in r, j, and the shift.

## 4. Target superadditivity has the required direction

The needed pointwise inequality is

    H_1(x)+sum_i[H_1(x+z_i)-H_1(x)] <= H_1(x+sum_i z_i)

for x,z_i>=0. For x>=1 it is equality. For x<1, setting t=1-x reduces it
to `sum_i(z_i-t)_+ <= (sum_i z_i-t)_+`. If any summand is positive, the
left side subtracts t at least once, and all omitted z_i are nonnegative.
This proves the stated direction.

Thus the combined target increments fit into a SINGLE target hinge. An
integer with many remainder primes supplies extra nonnegative interaction;
it does not require repeated use of the core hinge. Combining this inequality
with the previous source identity establishes the strict capped estimate.

## 5. Simultaneous cap-and-tail restoration

For every remainder prime put

    u_r(e)=min(w_r e,1),    t_r(e)=(w_r e-1)_+,
    U=sum_r u_r(v_r),      T=sum_r t_r(v_r).

For the source hinge, 1-Lipschitz monotonicity gives

    (V+U+T-c)_+ <= T+(V+U-c)_+.

For the target hinge there is equality:

    (V+U+T-1)_+ = T+(V+U-1)_+.

Indeed, if T>0, at least one capped coordinate equals one, so V+U>=1.
If T=0, equality is immediate. This observation works for arbitrarily many
remainder primes simultaneously; it is not restricted to a one-prime
target.

Each profile t_r is nondecreasing and starts at zero. Expanding it in
nonnegative prime-power increments yields

    sum_{a in A}T(a) <= sum_{a<=M}T(a) <= sum_{b in I}T(b).

This is the only tail comparison required. It is valid for arbitrary
nonnegative w_r and arbitrary powers in the source's one distinct R prime.
The final balance is

    source raw hinge
      <= target tail + rho*(target capped hinge)
      <= target raw hinge.

No negative term is discarded in the wrong direction, and no base or tail
budget is counted twice.

## 6. Stronger contraction and precise remaining scope

When each source has at most one R occurrence counting multiplicity, and
all R weights are <=1, every source tail vanishes. In the low-core-mean
branch, the stronger factor-rho estimate therefore survives for the full
raw target load. The candidate correctly restricts this stronger statement
to those hypotheses; it does not claim it for arbitrary source powers or
unbounded remainder weights.

Consequently, on the previously derived minimal-obstruction source class,
any raw dual objective above (2+epsilon)n must contain a substantial core
weight. Large weights confined to the remainder band cannot supply such an
obstruction. This is a necessary restriction on a possible dual witness,
not a solution for arbitrary substantial core weights. The subsequently
audited extension below strengthens this restriction to at least two
substantial core weights.

Empty supports, zero weights, the empty source set, dually zero-load prime
factors outside E union R, and M=1 cause no difficulty. The structural
one-distinct-prime hypothesis may indeed be weakened for a single vector
to at most one positive-weight R coordinate per source.

## 7. Separate audit of the written one-heavy-core extension

**Section 9 verdict: PASS.** This is an additional arbitrary core coordinate,
not merely one exception among the entire support. The number of possible
substantial R coordinates remains unrestricted.

Let q be the exceptional core prime, let V_0 be the diffuse load on the
other core primes, and put C=V_0+w_q v_q. The excluded-prime conditional
level theorem from `FIXED_HEAVY_CORE.md` applies with k=1. Its sufficient
condition is exactly the one reproduced in the new section:

    (1+e_1(kappa))*mu_0 + eta*2^(2-j)
       <= (ell-eta)*(1-e_1(r)).

The requirements r>=16 and kappa>=8 agree with the domains of that
conditional theorem. Taking eta sufficiently small works uniformly at
mu_0<=1+epsilon/2, since the limiting source coefficient is strictly below
ell=1+epsilon. The constants are uniform in the value of q, including q
larger than the interval length.

Decomposing at exact q-exponent j gives the rescaled real length T/q^j and
the target level s-w_q*j. For nonnegative levels, the conditional comparison
is directly applicable. The equality boundary w_q*j=s is correctly retained
in this branch, with target level zero.

If w_q>0, the negative-level exponents form the suffix

    j>=j_0=floor(s/w_q)+1.

Every target with such an exponent automatically exceeds the target level,
whereas the source count can be bounded by all prefix integers in the
suffix. After summing the suffix, these are simply the multiples of q^j_0.
Their target count is at least floor(T/q^j_0), exactly the prefix count.
Keeping ALL target exponents, including those with q^j>T, is essential and
is explicitly done in the written proof. Thus no per-exponent error is
introduced. When w_q=0, there is no negative-level suffix.

The same suffix argument indeed works for any nondecreasing nonnegative
q-adic profile: the exponents where the profile exceeds s form either an
empty set or an upper suffix. This observation is used only where the
source and target load have the same such profile.

The resulting C-level comparison has coefficient one, rather than the
strict rho of the diffuse-only case. Coefficient one is enough. The load C
is nonnegative and unchanged under multiplication by powers of any r in R,
because q is a core prime and E and R are disjoint. Every increment and
target-superadditivity step in the base proof therefore applies with C in
place of V. The simultaneous raw R-tail restoration also remains valid.

For the high-mean branch, use only the diffuse part V_0 in the moment bound.
Adding q and all R coordinates increases min(X,2), so automatic H_2 still
holds. The proof should be read with the established convention that light
primes greater than M are removed BEFORE computing mu_0 and choosing the
high/low branch; making this convention explicit at the start of Section 9
would be a useful expository clarification, not a mathematical repair.

The stronger conclusion is consequently justified: a source-specific raw
dual witness above (2+epsilon)n in the stated structural class must have at
least TWO core weights exceeding the new diffuse threshold. It still does
not rule out such witnesses with two or more substantial core weights.

## 8. A concrete limit of the naive multiple-exception extension

For two exceptional primes, a negative-level upper set of smooth parts need
not have its minimum shifted count on the prefix. For example, take primes
2 and 3 with weights one and a level s with 0<=s<1. The upper set is the
integers divisible by 2 or 3. It contains two points, 2 and 3, in the
three-term prefix {1,2,3}, but only one point, 6, in {5,6,7}.

This disproves only the proposed intermediate assertion that an arbitrary
upward-closed smooth-part condition has prefix-minimal interval counts. It
does NOT disprove the desired hinge inequality, the gluing theorem, or Erdős
708. A several-heavy-coordinate extension must retain an additional source
threshold gain or a quantitative error bound instead of reusing the
single-chain argument without change.
