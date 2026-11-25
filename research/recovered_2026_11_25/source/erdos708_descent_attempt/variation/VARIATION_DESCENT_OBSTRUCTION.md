# Genuine globality and formal cold quotients are still insufficient without the floor laws

24 November 2026. This note diagnoses a proposed proof method. It does **not** refute arithmetic descent (D), and it does not prove any new bound for Erdős 708.

## Result

The earlier six-coordinate obstruction can be strengthened to a **unique global optimum** whose every nontrivial formal cold quotient has negative surplus. Thus the argument cannot pass from full-tail globality, complete coordinate balances, all divisor-orthant count inequalities, and the quotient-reserve identity alone to (D). The numerical prefix/interval floor laws are indispensable.

Take c=21/10 and six formal prime coordinates. There are 90 source profiles:

- 3 copies of (1,1,1,1,1,1);
- one copy of 2 times the indicator of each of the 15 four-element subsets;
- 12 copies of each singleton unit vector.

There are 90 target profiles:

- 6 copies of (2,2,2,2,2,2);
- 4 copies of each doubled singleton;
- 3 copies of each of the 15 two-element indicator vectors;
- 15 zero vectors.

At w_i=1/2 the full source tail has 18 members, coordinate demand 23 in every row, and raw optimum F=39. Select all six large targets and all 24 doubled singletons, and select mass 1/5 at each of the 45 pair targets. Every row supplies exactly 12+8+3=23, at total cost 39. The surplus is

    J = 39 - (21/10)*18 = 6/5.

Every target pair has load one and fractional selection strictly between zero and one. Complementary slackness for this feasible optimal primal forces w_i+w_j=1 for every pair at any optimal dual for the same tail. Therefore that dual is uniquely w_i=1/2.

## Exact global verification

For arbitrary weights in the cube, the singleton source profiles have load <=1<c and contribute nothing. The three identical all-one profiles can be selected all together or not at all. A subset of the four-element profiles is encoded by a graph G on six vertices: its edges are the omitted pairs. If k is its edge count, deg_i its degrees, and h in {0,1} records the three all-one profiles, then

    n_A = k+3h,
    D_i(A) = 2(k-deg_i)+3h.

The target system is symmetric, so only the sorted degree sequence matters. Enumerating all 2^15 edge subsets yields 102 degree sequences, hence 204 cases. For each case the accompanying JSON file supplies an explicit rational feasible raw primal cover of cost <=(21/10)n_A+6/5. The only case reaching this upper bound is the complete graph with h=1, namely the displayed 18-member tail. Every other nonempty case has a certified surplus upper bound at most -7/10; the empty case gives zero.

All statements are independently checked with integer/Fraction arithmetic by `check_abstract_globality.py`. The verifier does not call an optimizer. It checks coverage of every graphical degree sequence, box constraints, all six demand inequalities, exact rational costs, all 729 nontrivial-or-zero divisor threshold patterns, and the quotient computations. The construction of the covers used an LP solver, but correctness of the upper certificates does not rely on its floating-point output.

Weak duality for each source choice gives a global upper bound 6/5, attained by w_i=1/2. The preceding equality and complementarity argument proves unique globality.

## Every formal cold quotient is negative

At these weights a nonzero exponent vector has load below one iff it is one singleton unit vector. Conditioning on any coordinate p being present and deleting one copy of p produces 25 source and 25 target profiles. Scaling the prices by 1/(1-w_p)=2 makes every retained weight exactly one, so no clipping gain occurs.

The source quotient loads are:

    3 profiles of load 5;
    10 profiles of load 7;
    12 profiles of load 0.

The target quotient loads are:

    6 profiles of load 11;
    19 profiles of load 1.

Consequently every such quotient has

    Q_p = 3*(5-21/10)+10*(7-21/10)-6*(11-1) = -23/10.

There are no new-tail, endpoint or clipping reserves in this formal quotient. Replicating every profile L times keeps the unique maximizer and gives J=(6/5)L while every cold quotient stays negative. Thus an abstract analogue of D, with an error C sqrt(90L), fails for every fixed C.

## Exactly why this does not refute arithmetic D

These profiles are not a prefix [1,M] and a consecutive target interval. Nor do their formal quotients have lengths floor(M/p) for actual primes.

Already each formal coordinate occurs in 25L of the 90L source positions. An actual prime would require floor(90L/p)=25L. This is impossible: for p<=3 the count is at least 30L, and for p>=5 it is at most 18L. The discrepancy is linear in L, whereas the permitted final error is only square-root in L. Higher orthants also lack the exact numerical product laws.

The exact prime-specific formula floor(M/d), and the target count being floor(M/d) or ceil(M/d) for actual numerical d, must therefore enter any successful argument before applying D. More finite price variations or KKT manipulation cannot supply those missing relations.

## Research outcome

No arithmetic bound proving D was obtained from price variations. The available integrated finite-variation identities already hold in this countermodel. This note is a checked limitation of that proof avenue, not a replacement goal or a partial solution of the original asymptotic.
