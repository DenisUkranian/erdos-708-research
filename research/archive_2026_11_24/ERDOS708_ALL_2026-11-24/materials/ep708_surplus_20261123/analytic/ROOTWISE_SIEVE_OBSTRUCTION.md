# What a rootwise sieve comparison cannot prove

## Status and scope

The unrestricted estimate

\[
 J_{2+\delta}(w)
 =\sum_{a\le M}(X_w(a)-2-\delta)_+
  -\sum_{b\in I}(X_w(b)-1)_+\le C_\delta
\]

is not proved here. This note examines one proposed way to prove it:
compare each canonical first-crossing source fibre with the target fibre
having exactly the same earlier prime part.

That rootwise comparison fails, even with an additive error bounded in
terms of delta, even when the source cofactor has just one further
active prime occurrence. This failure is compatible with a sparse full
source tail and sparse hot targets. It is not a counterexample at an
optimal pair and does not refute the requested global inequality.

## 1. A genuine threshold-gap improvement in the star estimate

For 0<=u<=1, R>=0 and delta>0 put

\[
 \psi_{u,\delta}(R)
 =(u+R-1-\delta)_+-(R-1-\delta)_+.
\]

Then

\[
 0\le\psi_{u,\delta}(R)
       \le\frac{uR}{1+\delta}.                       \tag{1}
\]

If R>=1+delta, the increment equals u and (1) follows. If
R<1+delta, the only nontrivial case has u+R>1+delta, and (1) is
equivalent to

\[
 (1+\delta-u)(1+\delta-R)\ge0.
\]

Thus the c=2+delta canonical-star argument really improves the earlier
weighted-tail coefficient by a factor 1/(1+delta). It is not necessary
to distribute delta separately over the individual stars.

Recall that an eligible star carrier d with rightmost prime q satisfies
dq<=M. Its signed exclusion terms have moduli dr with r<q. All of those
moduli are therefore at most M. In this particular certificate, deleting
large-modulus negative terms is not the missing step.

The elementary averaged lower bound for one carrier still contains the
unweighted reciprocal mass of the excluded earlier primes. Keeping the
same exclusion in the source upper bound suggests comparing rough
source cofactors with rough target cofactors. The next construction
shows why this cannot be done separately for each root in the short
sieve range.

## 2. Primary covering input

Let P(x) be the product of the primes at most x. Ford, Green, Konyagin,
Maynard and Tao define Y(x) as the greatest length of an interval that
can be covered by one residue class modulo each prime at most x. Their
equations (1.2) and (1.3) give

\[
 Y(x)\gg x\frac{\log x\,\log\log\log x}{\log\log x},
 \qquad Y(x)=j(P(x))-1.
\]

In particular, for all sufficiently large x there is an integer interval
J of length

\[
 T=\lfloor x\sqrt{\log x}\rfloor
\]

such that every member of J has a prime divisor at most x. Indeed, the
displayed lower bound exceeds T, and the Chinese remainder theorem
turns the covering residue classes into divisibility by those primes.
The interval can be shifted by an arbitrary multiple of P(x), so take
it positive and write J={C+1,...,C+T}.

Primary reference: K. Ford, B. Green, S. Konyagin, J. Maynard and T. Tao,
*Long gaps between primes*, arXiv:1412.5029v3, Definition 1,
Lemma 1.1 and equations (1.2)--(1.3), pages 3--4.

<https://arxiv.org/pdf/1412.5029>

Only the covering consequence is used below; no assertion about an
arbitrary prime-free interval is substituted for it.

## 3. A growing one-root counterexample

Fix 0<delta<1 and choose a fixed a with delta<a<1. For sufficiently
large x choose primes

\[
 x/4<\ell<x/2,\qquad x<q<2x,
\]

and let T,J be as above. Set

\[
 d=\ell q,\qquad M=dT,\qquad
 I=\{dC+1,\ldots,d(C+T)\}.
\]

Thus I has exactly M elements and its d-multiples are exactly dk with
k in J. The length parameter satisfies

\[
 T<q^2,
\]

once x is sufficiently large.

Assign the following clipped nonnegative raw weights:

* w_ell=a;
* w_r=1 for every prime q<=r<=T;
* w_p=epsilon_x>0 for all other primes p<=x;
* all remaining weights are zero.

Choose epsilon_x so small that the combined load from the third group
is less than (1-a)/2 at every integer in [1,M] union I. This is possible:
the set of relevant integers is finite, and all their valuations are
finite. Also require epsilon_x<=(log x)^(-2).

For every prime r in [q,T], the prefix source

\[
 A_r=\ell q r\le M
\]

has load 2+a. Its canonical first-crossing root, obtained by ordering
prime occurrences increasingly and stopping as soon as the cumulative
load exceeds one, is exactly d=ell q. The source factor ell alone has
load a<1, and including q raises the load to 1+a. This includes the
case r=q, with the second q occurrence lying after the root.

The contribution of this single root's source fibre at threshold
2+delta is therefore at least

\[
 (a-\delta)\bigl(\pi(T)-\pi(q)+1\bigr)\longrightarrow\infty.       \tag{2}
\]

Now a target multiple b=dk has canonical root exactly d only if k has
no prime divisor at most x. Any such extra factor lies before q in the
ordered factorization, so it either changes the earlier prime part of
the root or causes the crossing to occur even earlier. But every k in J
has a prime divisor at most x. Hence

\[
 \#\{b\in I:\text{the canonical root of }b\text{ is }d\}=0.        \tag{3}
\]

The source cofactor r is free of all the excluded earlier primes. Thus
(2)--(3) retain exactly the same earlier-prime exclusion on both sides.
There is only one active prime occurrence after d in each displayed
source. Nevertheless, the rootwise source/target discrepancy is
unbounded.

Consequently no estimate of the form

\[
 \text{source hinge mass assigned to }d
 \le C_\delta\,\text{target hinge mass with root }d+C'_\delta
\]

can hold uniformly for all carriers and all shifts, even in the branch
T<q^2. A target outside the exact-root fibre must be allowed to pay for
this source mass if the global argument is to work.

## 4. The example can be sparse on both full sides

Let A be the *entire* strict tail {2<=n<=M:X_w(n)>2+delta}, not only
the sources displayed above. The construction does not assert that w
maximizes J, or that its active rows are balanced for A.

The reciprocal weighted mean tends to zero:

\[
 \sum_p\frac{w_p}{p-1}
 \le \frac{a}{\ell-1}
  +\sum_{q\le r\le T}\frac1{r-1}
  +\epsilon_x\sum_{p\le x}\frac1{p-1}
 =o(1).                                                     \tag{4}
\]

Here the middle sum tends to zero by Mertens' theorem, since
log(T)/log(q) tends to one. Prefix mean domination then gives |A|=o(M).

A hot target either has a prime divisor r in [q,T] or is divisible by
ell^2. Indeed, otherwise its load is at most a+(1-a)/2<1. Hence

\[
 \frac{|\{b\in I:X_w(b)>1\}|}{M}
 \le\sum_{q\le r\le T}\frac1r
    +\frac{\pi(T)}M+\frac1{\ell^2}+\frac1M=o(1).             \tag{5}
\]

The full tail is also large enough to lie in the nontrivial quadratic
range. For large x, every product of three distinct primes in [q,2q]
is at most M, since M/(8q^3) tends to infinity. These sources have load
three, exceeding 2+delta. The prime number theorem therefore gives

\[
 |A|\gg(x/\log x)^3\gg\sqrt M.
\]

Thus neither sparsity of the full hot set, nor sparsity of the full
source tail, nor the condition M<16|A|^2 rescues a rootwise comparison.
This remains a method counterexample rather than a balanced optimal
counterexample. In particular, these estimates do not assert the
optimality-specific bound |{b in I:X_w(b)>1}|=O(|A|).

## 5. What remains open in this route

In the large sieve-parameter range, a fundamental-lemma argument can
compare the matching rough densities. The example above has
log(T)/log(q) tending to one, where a uniform positive lower rough
density need not exist.

The target positions lost from the exact-root fibre do not disappear
from the full target hinge. They acquire different earlier roots.
A global proof would have to transfer payment between those roots
while using the actual simultaneous row balances of a J-maximizer.
Neither (1) nor the covering obstruction supplies that transfer.

No conclusion J_{2+delta}<=C_delta, and no solution of Erdős 708,
is claimed.
