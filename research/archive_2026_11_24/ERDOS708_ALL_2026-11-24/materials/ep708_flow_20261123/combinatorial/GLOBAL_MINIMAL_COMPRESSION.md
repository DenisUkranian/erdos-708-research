# Global minimum-cardinality failure and exact compression rules

## Status

These statements use a minimum-cardinality raw failure among **all**
subsets of the fixed ambient set \([2,M]\), for one fixed target interval
\(I\) of length \(M\). They strengthen the source-set normalization, but
do not prove the required flow cut inequality or J_weak.

For a source set \(A\), write \(F(A)\) for its boxed raw covering LP,
and for a nonnegative clipped dual vector \(w\) write

\[
 X(n)=\sum_p w_pv_p(n),\qquad
 \Phi_A(w)=\sum_{a\in A}X(a)-\sum_{b\in I}(X(b)-1)_+.
\]

Fix \(c>2\), and suppose a failure \(F(A)>c|A|\) exists. Let \(m\)
be the smallest cardinality of any such failure. Among all source sets
of cardinality \(m\), choose \(A\) to maximize \(F(A)\), and among
those maximizers choose one maximizing \(\sum_{a\in A}a\). All these
choices exist because the ambient set is finite. Let \(w\) be any
optimal clipped raw dual for this chosen set, and put

\[
 F(A)=cm+e,\qquad e>0.
\]

## 1. The selected sources form a weighted upper level set

For every \(a\in A\) and every \(b\in[2,M]\setminus A\),

\[
 X(b)\le X(a),\qquad
 X(b)=X(a)\Longrightarrow b<a.                         \tag{1}
\]

Indeed, replacing \(a\) by \(b\) changes the value at the same dual
vector by \(X(b)-X(a)\). If this difference is positive, the new raw
LP is larger than the chosen global maximum. If the difference is zero,
the new LP is at least the same maximum and therefore equals it; a larger
integer \(b>a\) then contradicts the second choice of \(A\).

Consequently \(A\) consists of the \(m\) largest pairs
\((X(n),n)\), ordered lexicographically. In particular it is an upward
closed set for divisibility:

\[
 a\in A,\quad a\mid b,\quad b\le M
 \quad\Longrightarrow\quad b\in A.                    \tag{2}
\]

This includes multiples formed with zero-weight prime factors. It follows
also that every source satisfies

\[
 a>\frac{M}{m+1},                                      \tag{3}
\]

since otherwise its at least \(m+1\) positive multiples in \([2,M]\)
would all belong to \(A\).

Minimum cardinality gives the stronger load bound

\[
 X(a)\ge c+e\qquad(a\in A).                            \tag{4}
\]

For the proper subset obtained by deleting \(a\),
\(F(A\setminus\{a\})\ge\Phi_{A\setminus\{a\}}(w)
=cm+e-X(a)\), while global minimum cardinality makes this LP at most
\(c(m-1)\). This proves (4). No optimality of the restricted dual for
the smaller set is needed.

## 2. Exact uncrossing, including the collision condition

The following statement only requires global minimum cardinality, not
the maximizing and tie-breaking choices above.

Let \(a,b\in A\) be distinct, and put
\(g=\gcd(a,b)\), \(l=\operatorname{lcm}(a,b)\). If

\[
 X(g)\le c,\qquad l\le M,
\]

then necessarily

\[
 l\in A\setminus\{a,b\}.                              \tag{5}
\]

To prove this, (4) shows that neither source divides the other, and that
\(g\notin A\). If \(l\notin A\), replace the two sources \(a,b\)
by the single source \(l\). This gives a valid set \(A'\) of
\(m-1\) distinct integers in \([2,M]\), with

\[
 \Phi_{A'}(w)=F(A)-X(g)
            \ge cm+e-c>c(m-1),
\]

a contradiction. Thus (5) holds. One could equivalently first replace
\(a,b\) by \(g,l\), preserving every prime demand, and then delete
the low-load source \(g\); the one-step proof also covers \(g=1\).

The collision in (5) is essential. The conclusion is **not**
\(l>M\). In the normalized set of Section 1, any admissible lcm is
already selected by (2), so the basic two-source uncrossing operation is
systematically blocked by this collision.

For example, the integers \(30,154,2310\), with unit weights on
\(2,3,5,7,11\), have source loads \(3,3,5\), while
\(\gcd(30,154)=2\) has load one and the lcm 2310 is already present.
This is only an illustration of the collision, not a raw failure or a
counterexample to a flow inequality.

## 3. A general merge rule

Let \(S\subseteq A\), \(|S|=k\ge2\), and let
\(l=\operatorname{lcm}_{a\in S}a\le M\). Define its weighted overlap

\[
 O(S)=\sum_{a\in S}X(a)-X(l)\ge0.
\]

If \(l\notin A\setminus S\), replacing \(S\) by \(l\) produces
a valid source set of cardinality \(m-k+1\). Global minimum
cardinality therefore forces

\[
 O(S)\ge c(k-1)+e.                                    \tag{6}
\]

Indeed the new dual value is \(cm+e-O(S)\), which must be at most
\(c(m-k+1)\). In particular, if \(O(S)<c(k-1)+e\), then the
admissible lcm must already lie outside \(S\) in \(A\). If \(l\in S\),
the overlap is simply the sum of the other source loads and (6) already
follows from (4).

The two-source condition (5) is a convenient weaker form of (6), since
then \(O(S)=X(g)\).

## 4. Why this does not yet close a hot-divisor cut

A deficient cut in the hot-divisor network can be a proper subset
\(S\) of the globally normalized set \(A\). The target neighborhood
of an lcm can strictly contain the union of the neighborhoods of its
factors: a target may combine one cold prime contribution from each
factor into a hot common divisor with the lcm. Thus replacing a pair by
its lcm changes not only the source demand but also the available target
capacity. The extra target capacity has no sign that permits it to be
discarded in a deficient-cut argument.

Moreover, (2) guarantees many of the duplicate-lcm collisions that block
the cardinality reduction. A proof using this normalization must control
these existing join elements and their shared target capacities. Neither
(1)--(6) nor the previously proved private-bank and common-hot-divisor
conditions provide that control.

The remaining task is still the joint flow cut estimate, with every
target hinge charged only once. No general uncrossing theorem removing
all collisions or all mixing capacity is proved here.
