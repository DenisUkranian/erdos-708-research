# Exact checks for Erdős Problem 708

Date: 22 November 2026. These files are research intermediates, not a claimed
solution of Erdős Problem 708. No external publication or priority is claimed.

## A genuine obstruction to the proposed hub-budget route

Let

\[
A=\{60,66,70,78,84,90\},\quad n=6,\quad M=90,
\]

and put \(L=\operatorname{lcm}(A)=180180\). Take the actual interval

\[
I=\{L-44,\ldots,L+45\}=\{180136,\ldots,180225\}.
\]

Every element of \(A\) is greater than 45 and divides \(L\). Consequently
**the unique multiple in \(I\) of every source element is \(L\)**. There is no
freedom to improve the choice of hubs.

The source prime support is \(\{2,3,5,7,11,13\}\), and each source element has
three distinct prime factors. Therefore the Chen/Preil group bound is

\[
t+\sum_{a\in A}\omega(a)-\sum_{b\text{ hub}}|S_b|
=1+18-6=13>12=2n.
\]

This refutes the proposed **sufficient condition** that one can always choose
multiples as hubs whose prime-by-prime fill budget is at most \(2n\). It does
not refute the original problem. It occurs inside the remaining parameter
range \(2n<M<16n^2\).

In fact the exact product-cover number of this interval is only **4**. An
optimal cover is

\[
\{180140,180144,180145,180180\}.
\]

The stronger prime-power count-cover problem has exact optimum **6**. Thus
one must distinguish (1) the independent-prime charging bound, (2) the joint
prime-power count cover, and (3) the original product cover.

`verify_hub_obstruction.py` uses exact 0/1 dynamic programming over capped
integer demands to establish both optima, checks uniqueness of every hub,
and checks final product divisibility. It uses only Python's standard
library. Its output is `hub_obstruction_certificate.json`.

## The matching argument and its already-known scope

For arbitrary choices \(a\mid b_a\in I\), let \(C_b\) be the sources mapped
to hub \(b\), and \(S_b\) their union of prime supports. Then

\[
\tau(A,I)\le |\{b_a\}|+\sum_a\omega(a)-\sum_b |S_b|.
\]

For a fixed prime \(p\), construct the bipartite graph connecting each
source \(a\) divisible by \(p\) to interval elements divisible by
\(p^{v_p(a)}\). A source-saturating matching exists by the nested-neighborhood
Hall condition

\[
\#\{a\in A:p^e\mid a\}\le\lfloor M/p^e\rfloor
\le\#\{b\in I:p^e\mid b\}.
\]

Within each collision block containing \(p\), match a source of maximum
\(p\)-valuation to its hub. These sources and hubs are distinct. Augmenting
paths extend this partial matching to a full matching **while preserving
the set of already matched right-side vertices**. The assignments can be
changed; insisting that each original assignment remain fixed would be
incorrect. If the source count is \(k_p\) and there are \(c_p\) such hubs,
this extension adds exactly \(k_p-c_p\) right-side vertices. Taking the union
over primes proves the displayed upper bound.

This is an independent reformulation of Chen's collision-cycle inequality,
also stated as Theorem B in the following October notes. It is **not a new
result**:

- <https://github.com/chy4pro/erdos-708-explicit-upper-bounds>
- <https://github.com/dpreil-ydlp/open-problems/blob/master/math/erdos708/NOTES.md>

It immediately handles every source set in which each element has at most
two distinct prime factors, giving \(\tau\le2n-1\). The obstruction above
shows why merely choosing the hubs more cleverly cannot extend this
particular numerical charging bound to all source sets.

## An unbounded-gap theorem for the same charging bound

Fix an integer \(r\ge3\), let \(D\) be the product of the first \(r\)
primes, and let odd \(K\to\infty\) satisfy \(\gcd(K,D)=1\). Put

\[
A_K=\{Dk:(K+1)/2\le k\le K\}\cup\{(D-1)K\},
\quad n=(K+3)/2,\quad M=DK.
\]

For \(K\ge2D\), the extra element is distinct from the other elements,
\(\gcd(A_K)=1\), and the prime-support hypergraph is connected: all of the
first group share the prime support of \(D\), while the extra element
shares the prime support of \(K\) with the source element \(DK\).
All elements exceed \(M/2\), so the set is automatically closed under
proper multiples up to \(M\). The usual subinterval lower bounds on ordered
source elements also hold.

Let \(L=\operatorname{lcm}(A_K)\), and use the genuine interval
\(I_K=\{L-M/2+1,\ldots,L+M/2\}\). Every source has the unique multiple
\(L\) in this interval. The forced one-hub bound \(U_K\) satisfies

\[
U_K=1+\sum_{a\in A_K}\omega(a)-|P(A_K)|
\ge1+r(n-1)-\pi(K)=(r-o(1))n.
\]

Here every active prime is at most \(K\), since \(K\ge D\), and
\(\pi(K)=o(K)\). Also \(2n<M<16n^2\) for all sufficiently large \(K\).
Thus **no absolute constant times \(n\)** can bound this particular hub
charging expression for all genuine instances, even after the elementary
gcd, connectedness, upper-half, and divisor-closure reductions.

The original cover remains small in this family. Select all \(K\) multiples
of \(D\) in \(I_K\). Their product, divided by the product of the first
group of sources, is a multiple of

\[
D^{(K-1)/2}\,((K-1)/2)!.
\]

Indeed, after division by \(D\) the selected numbers form \(K\) consecutive
positive integers, whose product is divisible by \(K!\). Since
\((K-1)/2\ge D-1\), that quotient supplies \(D-1\). An additional multiple
of \(K\) outside the selected multiples of \(D\) supplies the remaining
factor \(K\). Such a point exists: the interval contains exactly \(D\)
multiples of \(K\), and exactly one of them is also divisible by \(D\).
Consequently

\[
\tau(A_K,I_K)\le K+1=2n-2.
\]

This is a no-go result for a sufficient charging argument, with an explicit
valid cover for the very same intervals. It is not a disproof of either
Erdős conjecture. The general family was derived in this session; no claim
of literature priority has been checked or made.

### A support-component consequence

Let \(r\) be the number of active primes, and let \(c\) be the number of
connected components of the hypergraph whose edges are the source prime
supports. Then

\[
\tau(A,I)\le\sum_a\omega(a)-r+c.
\]

Indeed, replacing source edges by their collision-block unions can only
join components. The total rank \(\sum_b(|S_b|-1)\) of those unions is at
least \(r-c\). This is a straightforward consequence of the known group
inequality, not an asserted new solution.

## Audit of an unrelated small-case slot-packing claim

In Bergström's November small-case manuscript, Subcase 3b uses
\(D_q(A)=\sum_{a\in A}v_q(a)\ge3\) to infer an individual prime-power size
bound. That implication is not valid. The configuration

\[
A=\{2464,3018,3080,3520,3521,4024\},\quad M=4024
\]

satisfies the listed preceding structural restrictions (connected gcd
graph, gcd 1, closure under multiples up to \(M\), minimum/subinterval
bounds, \(d_{11}=d_{503}=3\), and \(D_7=3\)). Here \(q=503\le M/8\) and
\(D_q=3\), but \(\lfloor\log_q M\rfloor=1\). Thus the stated repeat demand
is \(q^2=253009>M/8\), contrary to that paragraph's asserted slot capacity.
This diagnoses a proof gap, not a counterexample to \(g(6)=8\). The separate
error in Subcase 3a concerning common multiples in shifted intervals is
locally repairable and is not used to reject the result.

Primary source:
<https://zenodo.org/records/24366897/files/erdos708-paper.tex?download=1>.

## What remains

No counterexample to \(g(n)\le2n\) and no proof of either full conjecture was
obtained here. A route through hub assignments must account for **joint
multi-prime filling** or exploit valuation surplus; the independent-prime
budget can be too large even when the true covering number is very small.
