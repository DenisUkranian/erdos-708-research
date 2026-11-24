# Global full-tail optimality and every full divisibility cut still leave an arithmetic gap

24 November 2026. Internal research note. This is an abstract squarefree incidence model, **not** an arithmetic counterexample to Erdős 708. It gives a precise obstruction to deriving the requested bound from finite weight variations, secondary normalization, exact active rows, all full divisibility-cluster cuts, and divisor-count domination alone.

The model has a unique positive global maximizer in the price cube. Thus choosing minimum support, minimum sum of prices, or any further tie-breaking rule does not remove it. All finite weight variation inequalities are automatically satisfied at the same full-tail optimum. All ordinary divisor-count inequalities hold; the one-coordinate and two-coordinate counts agree exactly. What fails is the arithmetic requirement that each individual modulus count differs between the prefix and an equal-length interval by at most one.

## 1. Exact profiles

There are twenty formal prime coordinates, indexed by V={1,...,20}. A profile is a subset of V, and its load is the sum of the prices on that subset. Set c=21/10.

The source prefix consists of:

- one copy of every five-element subset of V;
- 102 copies of every two-element subset of V;
- 17,442 empty profiles.

The target consists of:

- 272 copies of every two-element subset of V;
- 646 copies of V itself.

Both sides have M=52,326 formal positions. The same profile may have multiple copies, just as different integers may have identical valuations on a prescribed active support. These profiles are not asserted to have an arithmetic realization.

Take w_i=1/2 for every i. The strict full tail is precisely the set A of five-element profiles, so

    n=binom(20,5)=15,504.

Every source in A has load 5/2 and source excess 2/5. Target pairs have load one; each full target has load ten. Therefore

    source excess = (2/5)*15,504 = 31,008/5,
    target penalty = 646*(10-1) = 5,814,
    J_c(w) = 1,938/5 > 0.                                  (1)

## 2. The same full tail has an exact paired raw optimum

Select each pair target with mass z=5/8 and every full target with mass z=1. A given coordinate occurs in

    binom(19,4)=3,876

full-tail source profiles. Its selected target supply equals

    (5/8)*272*19 + 646 = 170*19+646 = 3,876.

Thus every active row is exact. The selected cost is

    F=(5/8)*272*binom(20,2)+646
     =32,946=(17/8)n.

Target complementarity holds: all strictly hot targets are fully selected and the other selected targets have load exactly one. The displayed prices and z are a primal-dual optimum for A, including the unrestricted nonnegative raw dual. In particular

    F-cn=1,938/5=J_c(w).

## 3. Every nonempty full divisibility-cluster cut holds

For a nonempty formal squarefree divisor G, let k=|G|. The source pairs never contribute source excess at these prices. Every full target contains G. Hence

    D_G = (2/5)*binom(20-k,5-k)-5,814 <= 0,                 (2)

where the binomial coefficient is zero for k>5. The largest source term occurs at k=1 and equals (2/5)*3,876=7,752/5<5,814.

For divisors with a repeated prime factor, both source and target incidence counts are zero. Thus (2) covers every nonunit formal divisor, including all prime powers. These are cuts for the complete source prefix and complete target, not cuts for a selected subfamily of sources.

## 4. Every ordinary divisor-count domination also holds

For a fixed squarefree k-coordinate divisor, the total source and target counts are as follows.

| k | Source count | Target count |
|---|---:|---:|
| 1 | binom(19,4)+102*19=5,814 | 272*19+646=5,814 |
| 2 | binom(18,3)+102=918 | 272+646=918 |
| 3 | binom(17,2)=136 | 646 |
| 4 | 16 | 646 |
| 5 | 1 | 646 |
| 6,...,20 | 0 | 646 |

Repeated-prime moduli have zero on both sides. Thus target count is at least source count for every divisor, and all individual-prime and pair counts are exact.

The complete prime counts also imply that clipping any coordinate above one down to one cannot decrease the joint objective: the target hinge decreases by exactly the clipped amount times that prime's total count, whereas the source hinge decreases by at most the same amount. The price-cube global maximum established below is therefore also the unrestricted nonnegative global maximum.

## 5. All binary Rosser inequalities hold

Fix any coordinate set B. A five-element source profile S has r=|S intersect B| in {0,...,5}. For every such integer,

    (r-2)_+ <= (1/3)*binom(r,2).

Summing over all five-element source profiles gives

    sum_source (Omega_B-2)_+
       <= (1/3)*binom(18,3)*binom(|B|,2)
        =272*binom(|B|,2).

The padded source pairs contribute zero. The pair targets alone give exactly 272*binom(|B|,2) to sum_target (Omega_B-1)_+; full targets add a nonnegative amount. Thus every binary Rosser inequality, on every coordinate subset, holds. This proof requires no search over subsets.

This section claims only the proved binary threshold pair (2,1). It does not claim all higher integer-threshold comparisons. For example, on all twenty coordinates the proposed threshold pair (4,2) would read 15,504<=646*(20-2)=11,628 and fails here. An independently established theorem at that higher threshold would therefore supply additional information not included in this obstruction.

## 6. Genuine global maximality, without a numerical optimization claim

The source pair profiles have load at most two throughout the cube, so they never enter the source hinge at c=21/10. For arbitrary prices v in [0,1]^20,

    J(v)=sum_{|S|=5}(sum_{i in S}v_i-c)_+
          -272*sum_{i<j}(v_i+v_j-1)_+
          -646*(sum_i v_i-1)_+.                         (3)

On each cell cut out by the target hyperplanes v_i+v_j=1 and sum_i v_i=1, the negative target part is affine. The source part is convex. A maximum on a cell can therefore be attained at a vertex.

At sum_i v_i<=1 the objective is zero. A positive vertex consequently has sum_i v_i>1, so the total-sum hyperplane is not an active constraint. Every vertex of the cube cut out by equations v_i+v_j=1 is half-integral: a connected component of tight pair equations is either fixed by a coordinate bound at zero or one, or contains an odd cycle and is forced to 1/2. A bipartite component with no bound retains a free parameter and cannot define a vertex.

It remains to consider prices with i ones, j halves, and 20-i-j zeroes. By symmetry their value depends only on i,j.

For fixed i>=1, the source part is a convex sequence as j increases. Indeed a hinge of a sum of nonnegative coordinate increments is supermodular, and the source sum is symmetric in the coordinates being changed from zero to 1/2. Thus successive increments are nondecreasing. The target pair part is

    272*[binom(i,2)+ij/2],

and the full-target part is 646*(i+j/2-1); both are affine in j. Hence J(i,j) is a convex sequence, whose maximum occurs at j=0 or j=20-i.

At j=0 all prices are binary. Section 5 and c>2 imply J(i,0)<=0.

At j=20-i all coordinates are positive, every five-element source belongs to the tail, and direct counting gives

    J(i,20-i)=1,938/5 - 969*i.                           (4)

This is negative for every i>=1.

For i=0, the values j=0,1,2 give zero. On 2<=j<=20 the full-target penalty is affine, the pair-target penalty is zero, and the source part is a convex sequence. Its maximum is therefore at j=2 or j=20. The latter gives (1).

Consequently the only target-cell vertex attaining the positive global maximum is the all-half vector. Convexity on every target cell then shows that it is the unique global maximizer in the cube. This proves genuine full-tail optimality and excludes any minimum-support or minimum-price-sum escape.

At this optimizer the price-defining target ties are precisely the pair equations v_i+v_j=1. Any full-rank basis of these equations contains an odd cycle: a bipartite tight component would retain its alternating one-parameter variation. Thus secondary optimality does not even force an acyclic tie basis in this model. This observation concerns tie equations, not a claim that every possible target-dependent root allocation must be cyclic.

## 7. Every proper cold-core quotient is globally nonpositive

The only nonempty cold divisor profiles at the displayed optimum are single coordinates, each of load t=1/2. Cold-core descent raises the threshold to

    (c-t)/(1-t)=16/5.

Fix one such coordinate p and divide all p-bearing profiles by p. The source quotient consists of all four-element subsets of the remaining nineteen coordinates, together with 102 copies of every singleton. The target quotient consists of 272 copies of every singleton and 646 copies of the full nineteen-set. Both quotient sides have 5,814 positions.

For arbitrary new prices v in [0,1]^19, the singleton source and target hinges vanish. The quotient objective is

    Q(v)=sum_{|S|=4}(sum_{i in S}v_i-16/5)_+
            -646*(sum_i v_i-1)_+.

For sum v_i<=1 it is zero. On sum v_i>=1 it is convex; the vertices of that cube section are binary. At a binary vertex with k positive coordinates, k>=1,

    Q(v)=(4/5)*binom(k,4)-646*(k-1) <= 0.

Indeed binom(k,4)/(k-1)=k(k-2)(k-3)/24 for k>=4, which is increasing up to k=19 and equals 646/3 there; its product with 4/5 is strictly below 646. The cases k<=3 are immediate. Thus the quotient has global maximum zero for all new prices, not only for the rescaled old prices. Its source and target singleton-coordinate counts also agree, so the clipping argument extends this conclusion to all nonnegative prices.

Consequently even the assertion that every proper cold-core quotient is globally nonpositive does not, together with the other displayed properties, permit a purely incidence-based gluing step. The target overlap still needs an arithmetic argument.

## 8. The precise missing arithmetic

An actual M-term prefix and actual M-term translated interval have, for every positive integer modulus d,

    0 <= count_I(d)-floor(M/d) <= 1.

The source prefix count is floor(M/d). The abstract model obeys the weaker domination law but violates the upper bound one: a three-coordinate divisor occurs 136 times in the source and 646 times in the target, a discrepancy of 510.

Thus the example does not refute any theorem which uses the complete numerical interval structure. It does show that the following data, even together, do not force J_c<=0 or J_c=o(n):

- genuine joint global maximality of the same strict full tail;
- exact selected rows and full complementarity;
- all finite price variations and any secondary normalization;
- all full divisibility-cluster cuts D_g<=0;
- divisor-count domination for every modulus, with equality for single primes and prime pairs;
- every binary Rosser inequality.

Replicating every formal position preserves all these properties and makes J_c/n=1/40 fixed. The actual interval discrepancy failure is replicated too; replication does not create an arithmetic counterexample.

The next inference must use the simultaneous small floor errors for actual moduli, or another property of actual translated intervals. Merely summing the new full-cluster cuts reuses target penalties and cannot supply the missing step.
