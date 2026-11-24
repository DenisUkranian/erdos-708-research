# Hot divisors containing a prescribed high-weight prime

## Scope

This note proves necessary conditions on an actual raw-minimal
obstruction. It does not prove the global estimate J_weak.
There is no assumption on the number of prime factors, the number of
substantial weights, or the separation of prime sizes.

Let \(A\subseteq[2,M]\) be a set of \(m\) distinct integers and let
\(I=\{x+1,\ldots,x+M\}\), with \(x\ge0\). For clipped nonnegative weights
\(0\le w_p\le1\), put

\[
 X(n)=\sum_p w_pv_p(n),\qquad
 H=\{b\in I:X(b)>1\},\qquad h=|H|.
\]

Suppose the weights are paired with an optimal boxed primal cover
and every source satisfies \(X(a)>c>2\), as in the raw-minimal
reduction. Complementary slackness then implies

\[
 \sum_{b\in H}v_p(b)\le D_p(A)
 :=\sum_{a\in A}v_p(a)
 \quad\text{for every active prime }w_p>0.                 \tag{1}
\]

All target valuations in (1) are retained in full.

## 1. A cold initial segment

Set

\[
 L=\left\lfloor\frac{M}{h+1}\right\rfloor.
\]

Every integer \(d\le L\) satisfies \(X(d)\le1\). Indeed, if \(X(d)>1\),
all target multiples of \(d\) are in \(H\); there are at least
\(\lfloor M/d\rfloor\ge h+1\) of them, a contradiction.

In particular, whenever \(p\le L\),

\[
 w_p\left\lfloor\frac{\log L}{\log p}\right\rfloor\le1.    \tag{2}
\]

For fixed \(\eta>0\), let
\(k_\eta=\lfloor1/\eta\rfloor+1\). Every prime of weight
\(w_p\ge\eta\) satisfies

\[
 p^{k_\eta}>L,\qquad p>L^{1/k_\eta},                      \tag{3}
\]

because \(k_\eta w_p>1\). Statements (2)--(3) are useful when
\(L\ge2\); the cold-segment assertion itself also covers \(L<2\).

For a raw-minimal failure \(F=cm+e\), the previous reduction gives
\(e=O(\log M)\) and \(h\le F\). Thus \(L\) is at least
\(\lfloor M/(cm+O(\log M)+1)\rfloor\), with constants independent of
the shift \(x\).

## 2. A prescribed-prime partition lemma

For a source \(a\), write
\[
 s=X(a),\qquad u=\max_{q\mid a}w_q.
\]
Primes in this maximum range over all prime occurrences of \(a\);
repeated occurrences have the same weight and zero-weight occurrences
are allowed.

**Lemma.** Let \(p\mid a\), put \(v=w_p\), and let \(k\ge2\) be an
integer. If

\[
 s>k+(k-1)(u-v),                                         \tag{4}
\]

then there exists a divisor \(d\mid a\) such that

\[
 p\mid d,\qquad X(d)>1,\qquad
 d\le p^{\,1-1/k}a^{1/k}.                                \tag{5}
\]

**Proof.** Remove one occurrence of \(p\) from \(a\). We partition all
remaining prime occurrences into \(k\) groups. Build the first \(k-1\)
groups successively, stopping each group as soon as its weight exceeds
\(1-v\). Every such group has weight at most \(1-v+u\), because the
last added occurrence has weight at most \(u\).

These successive choices are possible. Indeed, (4) is equivalent to

\[
 s-v>k(1-v)+(k-1)u.
\]

After any \(j\le k-1\) completed groups, the unused weight is greater
than

\[
 (k-j)(1-v)+(k-1-j)u.
\]

In particular, before each required choice it is greater than \(1-v\),
and after the first \(k-1\) groups it remains greater than \(1-v\).
Take all unused occurrences as the last group. Zero-weight occurrences
may be assigned to any group; they do not affect these inequalities.

Let the products of the groups be \(b_1,\ldots,b_k\). Then
\(\prod_i b_i=a/p\) and \(X(b_i)>1-v\) for every \(i\).
At least one of these products is at most \((a/p)^{1/k}\).
For such an index set \(d=pb_i\). It is a divisor of \(a\), it has
weight greater than one, and it satisfies (5). \(\square\)

The proof treats repeated prime factors as distinct occurrences, so
it does not assume squarefreeness.

## 3. Consequences for actual prime demands

Suppose in addition that \(p\) is active, so that (1) applies.
The entire \(d\)-bank obtained from (5) is hot and contains at least
\[
 N=\lfloor M/d\rfloor
\]
positions. Its full \(p\)-valuation is at least
\[
 N v_p(d)+v_p(N!).
\]
Since \(a\le M\) and \(v_p(d)\ge1\), we obtain

\[
 \boxed{\quad
 D_p(A)\ge
 \left\lfloor (M/p)^{\,1-1/k}\right\rfloor .
 \quad}                                                 \tag{6}
\]

There is no restriction on \(x\). After dividing the \(d\)-bank by
\(d\), its quotients are consecutive positive integers; this is why the
factorial term is valid even when individual target valuations are
larger than \(\log_p M\).

Three useful specializations are:

1. If \(p\) has maximum weight in \(a\), then \(u=v\); for every
   integer \(k<s\), (6) holds.
2. In particular, a maximum-weight prime of any source with \(X(a)>2\)
   obeys
   \[
   D_p(A)\ge\lfloor\sqrt{M/p}\rfloor.
   \]
3. If \(X(a)>2+\delta\), every active occurrence satisfying
   \(w_p\ge u-\delta\) obeys the same square-root bound. If
   \(X(a)>3\), it applies to every active prime divisor of \(a\),
   because \(u-v\le1\).

For the last specialization the inequality is strict where needed:
\(s>2+\delta\ge2+u-v\), respectively \(s>3\ge2+u-v\).

## 4. A harmonic restriction on the selected prime set

Let \(Q_k\) be any set of active primes such that each \(p\in Q_k\)
occurs in at least one source for which (4) holds with this same
integer \(k\). One source may witness several primes.
Because \(p\le M\), the argument of the floor in (6) is at least one,
so \(\lfloor t\rfloor\ge t/2\) gives

\[
 \frac12 M^{1-1/k}
 \sum_{p\in Q_k}\frac{\log p}{p^{1-1/k}}
 \le\sum_{p\in Q_k}D_p(A)\log p
 \le\sum_{a\in A}\log a
 \le m\log M.
\]

Hence

\[
 \sum_{p\in Q_k}\frac{\log p}{p^{1-1/k}}
 \le\frac{2m\log M}{M^{1-1/k}}.                          \tag{7}
\]

If every prime of \(Q_k\) is at least \(Y>1\), then
\[
 \frac{\log p}{p^{1-1/k}}
 \ge \frac{Y^{1/k}\log Y}{p},
\]
and therefore

\[
 \boxed{\quad
 \sum_{p\in Q_k}\frac1p
 \le
 \frac{2m\log M}
 {M^{1-1/k}Y^{1/k}\log Y}.
 \quad}                                                 \tag{8}
\]

For \(k=2\), this becomes
\[
 \sum_{p\in Q_2}\frac1p
 \le\frac{2m\log M}{\sqrt{MY}\log Y}.
 \]

One can use \(Y=L^{1/k_\eta}\) for a set consisting of qualifying
primes of weight at least \(\eta\), by (3). This is a necessary
restriction derived from the actual optimum, not a new assumption on
the sources.

## 5. What this does not establish

The selected primes need not include every active source prime.
Even for \(k=2\), the right side of (8) need not tend to zero
uniformly throughout \(M<16m^2\). It can be large when \(M/m\)
grows slowly. Moreover, sparsity of a set of maximum-weight primes
does not by itself assign the shared target hinge to all remaining
core primes.

Thus these partition and demand estimates do not prove J_weak.
They supply an additional constraint on any actual obstruction and
identify precisely where a further joint argument is still needed.

## 6. Sharpness of the local divisor bound

The prescribed-prime product bound cannot be improved by using only
the weight and factorization of a single source. Fix integers
\(k\ge2\), \(r\ge2\), take one prime \(p\), and put

\[
 a=p^{\,k(r-1)+1},\qquad w_p=\frac1{r-1}.
\]

Then \(X(a)=k+1/(r-1)>k\), while the smallest hot divisor is exactly
\(p^r\). The bound in (5) is attained:

\[
 p^{1-1/k}a^{1/k}=p^r.
\]

For instance, \(a=p^3,w_p=1\) has load three but no hot divisor at
most \(\sqrt a\). This is only an obstruction to that stronger local
divisor assertion. It is not an actual minimal covering obstruction:
the global demand and saturation conditions are additional essential
information.
