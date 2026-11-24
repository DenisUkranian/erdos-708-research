# Two precise constraints on the surplus proof attempt

## Scope

These are auxiliary results. They neither bound the unrestricted maximum
of J_(2+delta) nor prove Erdős 708. The first gives a sharp finite
obstruction to universal nonnegative pointwise divisor kernels. The
second is a necessary arithmetic restriction on logarithmically cut
coordinates at a sparse hot target set.

## 1. A nonnegative pointwise kernel needs threshold at least 13/6

Let f=(f_1,...,f_6) range over {0,1/2,1}^6. Consider a function

\[
 G(f)=\sum_t c_t\prod_{i:t_i>0}1_{f_i\ge t_i},
 \qquad c_t\ge0,
\]

where each threshold t_i lies in {0,1/2,1}. Suppose

\[
 (\textstyle\sum_i f_i-c)_+\le G(f)
                  \le(\textstyle\sum_i f_i-1)_+          \tag{1}
\]

at every state. Then c>=13/6. Conversely, (1) is feasible at c=13/6.

### Lower bound

The upper bound at states of total load at most one forces every
constant or singleton coefficient to vanish. It also forces every
two-coordinate atom with thresholds (1/2,1/2) to vanish.

Let h=(1/2,...,1/2), e=(1,...,1), and let 1_S have ones on a four-element
set S and zero elsewhere. For each surviving orthant atom of support
size s, its total contribution to

\[
 G(h)+\frac13\sum_{|S|=4}G(1_S)
\]

is at most twice its coefficient. Indeed, the atom belongs to
C(6-s,4-s) four-one states. When s=2 its all-half contribution is zero
and C(4,2)/3=2. When s=3 its all-half contribution is at most one and
C(3,1)/3=1. For s>=4 the sum is at most 1+1/3. Every surviving atom is
present at e, so

\[
 G(h)+\frac13\sum_{|S|=4}G(1_S)\le2G(e)\le10.             \tag{2}
\]

If c<3, the lower bound in (1) and (2) give

\[
 (3-c)+5(4-c)\le10,
\]

or c>=13/6. For c>=3 the conclusion is immediate.

### A kernel attaining 13/6

Set

\[
 G(f)=\frac5{36}\sum_{i\ne j}1_{f_i=1}1_{f_j\ge1/2}
       +\frac1{24}\sum_{|S|=3}\prod_{i\in S}1_{f_i\ge1/2}.       \tag{3}
\]

If t coordinates are positive and k of them equal one, then

\[
 \sum_i f_i=(t+k)/2,\qquad
 G=\frac5{36}k(t-1)+\frac1{24}\binom t3.                    \tag{4}
\]

The lower bound G>=((t+k)/2-13/6)_+ follows from nonnegativity and
the affine inequality without the positive part. For fixed t, its
difference has slope (5t-23)/36 in k. Thus it is enough to check k=t
for 0<=t<=4 and k=0 for t=5,6. The nontrivial endpoint differences are
1/24 at (t,k)=(3,3), zero at (4,4), 1/12 at (5,0), and zero at (6,0);
the t<=2 cases are immediate.

For the upper bound, t<=1 gives G=0. For t>=2, the difference
(t+k)/2-1-G has slope (23-5t)/36. It is therefore enough to check k=0
for t=2,3,4 and k=t for t=5,6. The respective differences are
0, 11/24, 5/6, 29/36, and 0. This proves (1) at c=13/6 without relying
on a numerical feasibility calculation.

The threshold-two six-coordinate obstruction in Chen's `sec_remains.tex`
motivated this calculation. The weighted combination (2) and the exact
attaining kernel (3) strengthen that finite method obstruction.

### Meaning for the arithmetic problem

For six prime profiles with increments 1/2 at p and 1/2 at p^2, the
orthants are precisely nonnegative divisor-indicator terms restricted
to the displayed valuation grid. Consequently no universal pointwise
nonnegative divisor certificate can prove the threshold 2+delta
inequality when 0<delta<1/6.

This does not obstruct signed certificates, certificates whose lower
domination holds only after summation, or certificates using the actual
arithmetic source range and a summable error. It is not a counterexample
to J_(2+delta).

## 2. Cold divisors force logarithmically cut weights to be substantial

Let w_p in [0,1], let I have M consecutive positive integers, and let

\[
 H=\{b\in I:X_w(b)>1\},\qquad h=|H|,\qquad T=M/(h+1)>1.
\]

Every integer d<=T satisfies X_w(d)<=1: otherwise every interval
multiple of d would be hot, while there are at least floor(M/d)>=h+1
such multiples.

Fix lambda>0, and suppose p is cut by the logarithmic cap, that is,

\[
 w_p>\lambda\log p.
\]

Let s=floor(1/w_p)+1. Then s w_p>1, so the cold-divisor conclusion
implies p^s>T. Consequently

\[
 \lambda\log T<\lambda s\log p<s w_p\le1+w_p,
\]

and hence

\[
 \boxed{\quad w_p>\lambda\log T-1.\quad}                 \tag{5}
\]

This assertion uses actual full raw valuations. It does not truncate
target prime-power levels and does not assume a levelwise balance.

For example, at a family of paired optimal instances with h=O(n),
M=n^(2+o(1)), and lambda=(2+delta)/log M, every cut coordinate has

\[
 w_p>\delta/2+o(1).
\]

Thus arbitrarily tiny cut weights are not an obstruction in that
near-quadratic range. Formula (5) does not bound the total selected
target coverage lost under the logarithmic cap. That collective loss
remains the missing part of this variation argument.

## 3. Abstract domination and actual paired optimality still do not suffice

The positive-kernel obstruction has an exact interpretation as an
abstract incidence system. This is useful for distinguishing missing
arithmetic from missing optimization bookkeeping.

There are six formal prime coordinates. A position has an exponent
vector in {0,1,2}^6. Take 90 source positions with the following profiles:

* three copies of (1,1,1,1,1,1);
* one copy of 2*1_S for each of the 15 four-element subsets S;
* twelve copies of e_i for each of the six coordinates i.

Take 90 target positions with these profiles:

* six copies of (2,2,2,2,2,2);
* four copies of 2e_i for each of the six coordinates i;
* three copies of e_i+e_j for each of the 15 unordered pairs.
* fifteen zero profiles.

### Every divisor orthant has at least as many target occurrences

For a divisor threshold t, count positions whose exponent vector
dominates t coordinatewise. A threshold above two in any coordinate
has zero count on both sides. The constant threshold has count 90 on
both sides. All other cases are as follows; a ``one threshold'' means
that every nonzero coordinate of t equals one.

| Support and threshold type | Source count | Target count |
|---|---:|---:|
| One coordinate, threshold one | 25 | 25 |
| One coordinate, threshold two | 10 | 10 |
| Two coordinates, both thresholds one | 9 | 9 |
| Two coordinates, at least one threshold two | 6 | 6 |
| Three coordinates, all thresholds one | 6 | 6 |
| Three coordinates, at least one threshold two | 3 | 6 |
| Four coordinates, all thresholds one | 4 | 6 |
| Four coordinates, at least one threshold two | 1 | 6 |
| Five or six coordinates, all thresholds one | 3 | 6 |
| Five or six coordinates, at least one threshold two | 0 | 6 |

Thus this system has the elementary domination for every divisor
indicator. All individual prime-power marginal counts are exactly
equal on the two full sides; their raw valuation sum is 35 in every
coordinate on each side.

### The displayed weight vector is genuinely paired optimal

Give each formal prime weight 1/2. For 2<c<3, the entire strict source
tail has 18 positions: the three load-three profiles and the fifteen
load-four profiles. Its demand in every raw coordinate is

\[
 D_i=3+2\binom53=23.
\]

The six large target profiles have load six, the 69 nonzero remaining
target profiles have load one, and the 15 added targets have load zero.
The added singleton source profiles have load 1/2 and do not enter the
strict tail. Hence the raw dual objective on the full tail is

\[
 3\cdot3+15\cdot4-6(6-1)=39.                         \tag{6}
\]

Select every one of the six load-six targets, every one of the 24
singleton targets, and mass 1/5 at each of the 45 pair targets. Every
raw row then has exactly

\[
 6\cdot2+4\cdot2+5\cdot3/5=23
\]

selected valuation units. The selected cost is

\[
 6+24+45/5=39.
\]

This proves both feasibility and equality with (6). The price vector is
therefore an actual boxed raw dual optimum for its actual full tail,
with every positive row tight and all hot targets saturated.

At these prices the surplus is

\[
 J_c=39-18c>0\quad\hbox{if }2<c<13/6.                 \tag{7}
\]

Replicate every position L times. Orthant domination and the explicit
paired optimum persist, and (7) becomes L(39-18c). The continuous
surplus objective on the price cube has a global maximizer, whose
surplus is at least this value. At that maximizer the abstract
full-tail/paired-optimal and global price-variation identities hold
automatically. Thus imposing those identities cannot by itself repair
the obstruction.

### Precisely what this does and does not show

These profiles have not been realized by the prefix [1,M] and an actual
integer interval. Their replication is not an arithmetic amplification.
In particular, the full restrictions imposed by the numerical sizes of
the primes and their products, and by actual interval multiple counts,
are absent.

The example shows that a proof using only orthant-count domination,
clipped raw prices, full-tail optimality, saturated hot targets, tight
raw rows and the resulting global variational identities cannot establish
the desired constant surplus bound. A valid proof must additionally use
the arithmetic relations between the actual divisors and M. No failure
of the arithmetic J_c inequality follows from this abstract system.
