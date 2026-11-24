# Five-coordinate obstruction to all unweighted integer-threshold cuts

Construction proposed by the parent agent; independently checked here on
24 November 2026. This is an **abstract incidence model, not an actual
integer prefix and interval**. It is not a counterexample to Erdős 708.

## 1. Profiles, prices, and exact rows

There are five formal prime coordinates: a main coordinate h and four
light coordinates. Set

    w_h=1,    w_light=1/3,    c=21/10.

The original source side consists of three copies of the full five-set
and ten empty positions. The target side consists of three copies of
the singleton {h}, all four triples of light coordinates, and all six
pairs of light coordinates. Both sides have M=13 formal positions.

The own full source tail A has n=3 positions, each of load 7/3. Every
proper subprofile of a source has load at most two, so these source
profiles are threshold-minimal for c>2. Put z=1 on the three main
singletons and the four light triples, and z=0 on the light pairs.
The selected target profiles all have load exactly one; the unselected
pairs have load 2/3. Each coordinate occurs three times in A and three
times among selected targets. Thus all whole-coordinate rows are exact.

The primal cost and joint surplus are

    F=7,    n=3,    J_c=7-3c=7/10 >0.                 (1)

The source-side total prime counts can also be made identical to the
target-side total prime counts, without changing any conclusion below.
Add three singleton copies of each light coordinate to the source side,
and twelve empty target positions. Both sides then have M=25 positions.
The full source tail remains A. Total counts are three for h and six
for every light coordinate on both sides; selected rows are still three.

## 2. Global maximality

Take arbitrary coordinate prices in [0,1]. Write u for the price of h
and s for the sum of the four light prices. The source hinge sum is

    3*(u+s-c)_+.

The added source singletons, if present, contribute zero. The main
singleton targets also have zero hinge throughout the cube. Convexity
of the hinge, applied separately to the four light triples and the six
light pairs, gives

    H >= 4*(3s/4-1)_+ + 6*(s/2-1)_+.                 (2)

The surplus is nondecreasing in u for fixed light prices, so u=1 is
optimal. On s<=c-1 the resulting upper bound is nonpositive; on
c-1<=s<=4/3 it increases to 7-3c; on 4/3<=s<=2 it equals 7-3c; on
s>=2 it is 13-3c-3s<=7-3c. Thus (1) is the true global maximum.
The given equal light prices 1/3 attain equality in Jensen and in (1).

For the fixed source set A, the same prices are also a genuine optimum
of the unrestricted nonnegative raw dual, paired with the displayed z:
primal feasibility, every positive-price row equality, and target
complementarity hold. The cube restriction is not being used to assert
row equality at w_h=1.

## 3. Every unweighted integer-threshold cut holds

For any coordinate subset B and any integer k>=1, consider the cut

    sum_prefix (Ω_B-2k)_+ <= sum_target (Ω_B-k)_+.    (3)

This section checks (3) as a family of extra proposed constraints; it
does not assert a new arithmetic theorem for all k.

Let l be the number of light coordinates in B, and let h_B be zero or
one according as the main coordinate is absent or present. The source
side of (3) equals

    3*(l+h_B-2k)_+.

The main singleton target contributions vanish for every k>=1. The
target side equals

    (4-l)*(l-k)_+ + l*(l-1-k)_+
       + binom(l,2)*(2-k)_+.

For l=0,1,2,3,4 these values are respectively

    k=1: 0, 0, 3, 8, 14;
    k=2: 0, 0, 0, 1, 4.

At k=1 the largest source values, taking h_B=1, are
0,0,3,6,9, so every cut holds. At k=2 the source can be positive only
for l=4,h_B=1, where it equals three and the target equals four. For
k>=3 the source is zero. Thus every subset B and every k>=1 passes (3).
Added source singletons and target empty positions change neither side.

Using the exact selected rows, (3) is equivalently the reserve-preserving
selected-target cut

    sum_target z_b min(Ω_B(b),k)
      <= sum_(a in A) min(Ω_B(a),2k)
          -sum_(a not in A) (Ω_B(a)-2k)_+
          +sum_target (1-z_b)(Ω_B(b)-k)_+.

The outside-source term is zero even in the augmented model. Hence these
stronger presentations of all cuts also hold. Any nonnegative combination
or integration of them remains valid on the displayed positive global
model and therefore cannot, by itself, prove an asymptotic cost at most 2n.

## 4. The missing arithmetic is explicit

Every source contains h and every light coordinate. A mixed two-coordinate
divisor h*p has weighted load 4/3>1. No target profile contains both h and
any light coordinate at all.

If this model were realized by actual primes, actual sources <=M, and an
interval of M consecutive positive integers, then d=h*p would divide a
source and satisfy d<=M. The target interval would contain at least
floor(M/d)>=1 multiples of d, all hot. The model has zero such target
positions. This contradiction excludes an arithmetic realization.

Indeed it already violates full divisor-count domination for these mixed
moduli, despite equality of all individual prime counts in the augmented
model. This is why the example is not a counterexample to the desired
number-theoretic result and is not progress toward its proof. It is a
precise obstruction to completing the proof from unweighted threshold
cuts, globality, source-threshold minimality, and individual row balances
alone.

Repeating every formal position r times preserves all statements and gives
n=3r, F=7r and J_c=(7/10)r. Replication does not repair the missing arithmetic.
