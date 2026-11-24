# Binary Rosser cuts at a raw optimum, and their exact limitation

24 November 2026. This note does not close the general Erdős 708 asymptotic.
It audits the previously proved binary theorem, derives its simultaneous
subset cuts at a genuine raw optimum, and gives an abstract positive global
optimizer satisfying **all** those cuts. The abstract construction is not an
integer-interval counterexample.

## 1. Audited exact binary theorem

The complete proof is in
`ep708_terminal_20261124/capture/ROSSER_BINARY_CERTIFICATE.md`.
For every finite set of primes B, with Ω_B(t)=sum_(p in B) v_p(t), and every
interval I of M positive consecutive integers,

    sum_(a<=M) (Ω_B(a)-2)_+ <= sum_(b in I) (Ω_B(b)-1)_+.       (1)

There is no error term and all powers are retained. This uses a different
certificate from the exponential certificate whose truncation remains open.

Here is the key arithmetic audit. Introduce primes in decreasing order.
Maintain squarefree coefficients q_S in {0,(-1)^|S|}, supported at product(S)<=M,
with q_empty=1 and singleton coefficients -1. Their Boolean polynomial Q(B)
is nonpositive on every nonempty B; on feasible B it belongs to {0,-1}; and
q_B!=0 on feasible B implies Q(B)=0.

When introducing the next smallest prime p, pair every internal coefficient
q_S with its negative at S union {p}, where p*product(S)<=M. On the boundary
retain negative coefficients and delete positive ones. For feasible B not
containing p, a boundary subset S of B must equal B: a missing q>p would imply
q*product(S)<=product(B)<=M, contrary to p*product(S)>M. This proves the
inductive properties, including the special reserve condition Q(B)=0 when
q_B!=0.

The target minorant F=Ω_B-1+Q is at most (Ω_B-1)_+ everywhere and at least
(Ω_B-2)_+ on the prefix. Constants and singleton coefficients cancel.
All remaining prime-power coefficients are positive. Each negative mixed
coefficient equals -1, has modulus d<=M, and has its own distinct source d
where F(d)-(Ω_B(d)-2)_+=1. That source pays the possible one-unit negative
floor error of that coefficient. Thus (1) follows. No unproved truncation
step is used here.

## 2. A general simultaneous cut family

Let A be any source set of n integers in [1,M], and let w,z be a genuinely
paired raw optimum. For every active prime p,

    sum_I z_b v_p(b)=sum_A v_p(a).

Fix any subset B of the active primes and put k(t)=Ω_B(t). Then (1), the
source inequality sum_A k-2n<=sum_prefix(k-2)_+, and the exact rows give

    sum_(b in I:k(b)>0) z_b
       <= 2n + sum_(b in I) (1-z_b)(k(b)-1)_+.               (2)

The stronger reserve-preserving form is

    sum_(b:k(b)>0) z_b
       <= sum_(a in A) min(k(a),2)
          -sum_(a<=M,a not in A) (k(a)-2)_+
          +sum_(b in I) (1-z_b)(k(b)-1)_+.                  (3)

Indeed z*k-(k-1)_+=z*1_(k>0)-(1-z)*(k-1)_+ pointwise.
The full subset family (2)--(3) is valid simultaneously; no prime-power
layer balance or replacement source set is used.

For B={p:w_p>1/2}, the final term vanishes exactly. Any k(b)>=2 forces
X_w(b)>1 and z_b=1. Hence

    sum_I z_b 1_{some prime of weight >1/2 divides b} <=2n.  (4)

Writing F=sum_I z_b, the selected mass with no such prime is at least F-2n.
Every position with z_b>0 has X_w(b)>=1. Therefore the low-price source demand
satisfies

    sum_(p:0<w_p<=1/2) w_p D_p(A) >= F-2n.                 (5)

At a positive J_(2+delta) optimum this is strictly larger than delta*n.
This strengthens the old qualitative necessity of at least one price<=1/2;
it does not bound the low-price demand from above.

## 3. Joint integration is exact, but does not create a raw estimate

For a nonnegative measure lambda on price thresholds, integrate (3) with
B_t={p:w_p>t}. Put eta_p=int_0^{w_p} d lambda(t), and
Y(a)=sum_p eta_p v_p(a), where v_p(a) is the ordinary prime valuation.
The left side becomes the selected sum of the largest transformed
occurrence price. The first source term becomes the sum of its two largest
transformed occurrence prices. The other terms become the corresponding
one- and two-largest-price remainders. All budgets are counted only once.

After substituting the exact whole-row balance for the transformed prices,
this is precisely the integrated binary theorem. In particular, the
unselected-target term does not disappear: at a cold target several small
prices may have total load below one while k(b)>=2.

## 4. An exact abstract positive global optimizer satisfying every cut

This section concerns an abstract valuation incidence system, **not** an
actual prefix and interval. It isolates why (2)--(3), even jointly with all
row balances and global optimality, cannot be a standalone completion.

Use seven distinct formal primes. The source side has 15 copies of their
full seven-element set and 41 empty positions. The target side has one
copy of every triple (35 positions) and one copy of every pair (21 positions).
Both sides have 56 positions. Give each prime price 2/5. Let 0<delta<1/3
and c=2+delta.

The own full tail consists exactly of the 15 source copies, all with load
14/5. Each target triple has load 6/5 and is selected with z=1; each target
pair has load 4/5 and is unselected with z=0. Every prime occurs in 15 source
copies and exactly binom(6,2)=15 selected target triples. Thus every whole
row is exact. The primal cost is 35, and

    J_c = 15*(14/5-c)-35*(1/5) = 35-15c = 5-15delta >0.   (6)

These prices are a global maximum, not just a stationary point. For an
arbitrary price vector u in [0,1]^7, let s=sum u_i. The source hinge sum is
15*(s-c)_+. Jensen's inequality on all triples and all pairs gives

    target H >=35*(3s/7-1)_+ +21*(2s/7-1)_+.

For s<=c the surplus is nonpositive. For c<s<=7/3 it is at most
15*(s-c)<=35-15c. For 7/3<=s<=7/2 it is at most 35-15c. For s>=7/2 it is
at most 56-6s-15c<=35-15c. Equal prices 2/5 attain the bound.

Every binary subset inequality also holds. For a subset B of s formal
primes the source side of (1) is 15*(s-2)_+, whereas the target side is

    binom(s,2)*(7-s) + 2*binom(s,3) + binom(s,2).

For s=0,1,2,3,4,5,6,7 the two lists are respectively

    source: 0, 0, 0, 15, 30, 45, 60, 75;
    target: 0, 0, 6, 17, 32, 50, 70, 91.

Thus all 128 subsets obey (1), and consequently (2)--(3). All nonempty
source profiles are in the own full tail; the outside-tail source reserve
is zero. The unselected pair positions supply exactly the terms that stop
the integrated cuts from giving a raw cost at most 2n.

Repeating every position k times gives n=15k and cost 35k=(7/3)n, with a
linear positive joint surplus. This repetition is only an abstract
incidence construction. It is not asserted to be realizable by consecutive
integer intervals or by their complete source prefixes.

For c=21/10 one may instead choose every price equal to 17/50. The same
global maximum 7/2 and all the same exact rows/cuts remain valid. Now a
source has load 119/50=2.38, whereas every proper subprofile has at most
102/50=2.04<c. Thus the source profiles are threshold-minimal: the additional
formal rule requiring every hot proper divisor to be a source is vacuous.
Target triples have load 51/50>1 and pairs load 34/50<1. This strengthening
still does not supply an arithmetic realization; numerical prefix closure
and mandatory-bank densities remain absent.

## 5. Remaining arithmetic requirement

The binary theorem itself is a genuine unconditional arithmetic theorem.
Its extracted subset inequalities forget enough arithmetic that even their
entire family admits the explicit positive global model above. To close
the raw asymptotic one still has to use actual divisibility locations,
mandatory banks, numerical divisor sizes, or an equivalent joint arithmetic
constraint. No such uniform closing inequality is proved here.
