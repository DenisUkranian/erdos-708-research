# Arbitrary unions of initial prime fibers have uniform upper transfer constant two

Let $A$ be a union of arbitrary initial prime fibers,
\[
 A=\bigcup_{p\in P}\{p,2p,\ldots,k_p p\}\subset[1,M],\qquad n=|A|.
\]
Here $P$ is a set of distinct primes and the positive integers $k_p$ are unrestricted apart from $T_p=p k_p\le M$. For every translate $I$ consisting of $M$ positive consecutive integers there exists $B\subset I$ with $ |B|\le2n+o(n)$ and
\[
 |B\cap d\mathbb Z|\ge |A\cap d\mathbb Z| \qquad(d\text{ a prime power}).
\]
The error is uniform in $P,M,I$ and the cutoffs. Root ranks or number of overlaps are unrestricted. This also covers subsets of relative density $1-o(1)$ in such a union. The latter follows by using the cover for the containing union.

## A size integral for the canonical source

Write $\mu(x)=\sum_{T_p\ge x}1/p$, $\lambda(x)=\min(1,\mu(x))$ for $0<x\le M$. Write $C=\sup\{0<x\le M:\mu(x)\ge1\}$, taking zero if the set is empty. Write $L=\int_0^M\lambda(x)\,dx$. We have the exact bound
\[
 2n\ge\int_0^M(2\lambda-\lambda^2)\,dx\ge L\ge C.
\]
Order the primes by nonincreasing $T_p$ and choose retention probabilities $u_p\in[0,1]$ by filling the cumulative reciprocal mass up to one, taking all roots if the total reciprocal mass is at most one. For each layer the retained mean mass is $\sum_{T_p\ge x}u_p/p=\lambda(x)$. Retain primes independently. The expected two-term inclusion-exclusion lower bound for the union of the retained fibers is
\[
 \sum_p u_p k_p-\sum_{p<r}u_p u_r
  \left\lfloor{\min(T_p,T_r)\over pr}\right\rfloor
 \ge\int_0^M(\lambda-\lambda^2/2)\,dx.
\]
The expected union size is at most $n$. Primes with $T_p>C$ were fully retained, hence $\sum_{T_p>C}k_p\le L\le2n$. Also $k_p\le n$ and $|P|\le n$, as each root $p$ itself lies in $A$.

## One target vector handles all cutoffs

For every $p\in P$ with $p\le n$, let $S_p\subset I$ be any set of $\lfloor M/p\rfloor$ multiples of $p$ with the largest $p$-adic valuations. Nesting of the divisibility classes and the interval count imply
\[
 |S_p\cap p^j\mathbb Z|\ge\lfloor M/p^j\rfloor\quad (j\ge1).
\]
For every $p\in P$ with $p>n$, reserve $k_p$ multiples of $p$ in $I$ at weight one. There are at least $\lfloor M/p\rfloor\ge k_p$ available. Let $D$ be the union of these reserved sets. Give $b\in I$ weight
\[
 y_0(b)={1\over M}\int_0^M\left[\lambda(x)+(1-\lambda(x))
  1_{\{b\in\bigcup_{p\le n,\ T_p\ge x}S_p\}}\right]dx,
 \qquad y(b)=\max(y_0(b),1_D(b)).
\]
The union in the indicator runs over $p\in P$. Set $\ell=L/M$. Then $y_0\ge\ell$, and summing the bank sizes bounds the cost by
\[
 \sum_b y(b)\le L+\sum_{p\le n}{1\over p}\int_0^{T_p}(1-\lambda)dx
    +(1-\ell)\sum_{p>n}k_p .
\]
Replacing the last term by the analogous sum of integrals changes this upper bound by at most $\sum_{p>n}p^{-1}\int_0^{T_p}\lambda\,dx\le\sum_{p>n}2n/p=o(n)$. Indeed the roots up to $n\sqrt{\log n}$ number $O(n/\sqrt{\log n})$ by Chebyshev's prime bound and each summand here is at most two. Each of the at most $n$ remaining summands is at most $2/\sqrt{\log n}$. The resulting main bound is
\[
 \int_0^M[\lambda+(1-\lambda)\mu]dx
 =\int_0^M(2\lambda-\lambda^2)dx\le2n.
\]
The same split shows $\sum_{p\in P}\min(1,2n/p)=o(n)$, uniformly.

## Counting the defects across all prime powers

A prime $q>n$ contributes to a source row $ph$ only when $q=p$, because $h\le n$. Its exponent must be one. The reserved sets therefore meet every request with such a base.

For each remaining relevant $d=q^j$, with $q\le n$ and positive demand $a_d=|A\cap d\mathbb Z|$, put $c=\max(C,T_q)$ if $q\in P$, and $c=C$ otherwise. The target contributes at least $\lfloor M/d\rfloor$ at every layer $x\le c$, from the flat part for $x\le C$ and from $S_q$ for $C<x\le T_q$ if applicable. For $x>c$ its flat part contributes at least $\lambda(x)\lfloor M/d\rfloor$ per layer. Thus
\[
 \sum_{d\mid b} y(b)\ge{\lfloor M/d\rfloor\over M}\,g_d
 \ge g_d/d-1,\qquad
 g_d=c+\int_c^M\mu(x)dx=c+\sum_{T_p>c}(T_p-c)/p .
\]
We used $g_d\le M$. The source rows up to $c$ cost at most $c/d$. For rows above $c$ the active primes have $p\ne q$. Each contributes only if $k_p\ge d$, in which case its contribution is at most
\[
 \lfloor k_p/d\rfloor-\lfloor c/(pd)\rfloor
 \le (T_p-c)/(pd)+\min(1,c/(pd)).
\]
Consequently $a_d\le g_d/d+E_d$, where
\[
 E_d=\sum_{T_p>c,\ k_p\ge d}\min(1,c/(pd)).
\]
In all cases $c/d\le2n$, since $C\le2n$ and $T_q/q^j\le k_q\le n$. Writing $R(k)$ for the number of prime powers up to $k$,
\[
 \sum_d E_d\le\sum_{T_p>C}R(k_p)\min(1,2n/p)=o(n).
\]
Indeed $R(k)=o(k)$ and $\sum_{T_p>C} k_p\le 2n$, giving a bound $2n\sup_{k\ge K}R(k)/k$ for the large cutoffs. The small cutoffs contribute at most $K\sum_{p\in P}\min(1,2n/p)=o_K(n)$. Let $K\to\infty$.

The number of relevant levels for small bases is $o(n)$ uniformly. If $q^j\mid ph$ then $q^j\le n$ for $q\ne p$ and $q^{j-1}\le n$ for $p=q$. All these powers have $q\le n$ and $q^j\le n^2$, so their number is at most $2\pi(n)+O(n^{2/3}\log n)$.

## Integrality

Keep the reserved targets at weight one. For each relevant small-base level impose the lower bound equal to the smaller of its original integer demand and the amount attained by $y$. Minimize total weight with these bounds in the unit cube and choose an optimal extreme point. There are at most as many fractional coordinates as level constraints, by the active-constraint rank bound. Rounding them all up costs $o(n)$. On each still-undercovered level add unused multiples of $d$ until demand is met. There are enough because $a_d\le\lfloor M/d\rfloor\le |I\cap d\mathbb Z|$. The total repair is bounded by $\sum_d(E_d+1)=o(n)$. This proves the assertion.

The proof gives the explicit uniform error $O(n/\log\log(10n))$. The root split gives $\sum_p\min(1,2n/p)=O(n/\sqrt{\log(2n)})$. Take $K=(\log(2n))^{1/4}$ and use $R(k)=O(k/\log(2k))$. The small-cutoff contribution becomes $O(n/(\log(2n))^{1/4})$, and the large-cutoff contribution is $O(n/\log\log(10n))$. All other error terms are smaller. The positive diagonal term in two-term inclusion-exclusion also allows one to subtract $\sum_p u_p^2 k_p/p$ from the main $2n$ bound, with the same additive error.

## Sharp collision repair for bounded cofactors

Suppose every prefix length is at most $K$. Write $m=\sum k_p$, $D=\operatorname{lcm}(1,\ldots,K)$. If $\lfloor M/D\rfloor\ge m$, then $H(A,I)\le m\le n+K\pi(K)$. For every fixed $K$ this gives $H(A,I)\le n+O_K(1)$ for all sufficiently large $n$, uniformly in the roots and target shift. In fact $m\le K\pi(M)=o_K(M)$, while all intersections of different source fibers involve two roots at most $K$; deleting the at most $K\pi(K)$ rows from those small-root fibers leaves disjoint fibers.

For each root take $k_p$ consecutive target multiples of $p$. The multiset $T$ of their union dominates every prime-power demand if repetitions are counted. At level $q^j$, the $p\ne q$ groups individually hit at least $\lfloor k_p/q^j\rfloor$ and the $p=q$ group at least $\lfloor k_p/q^{j-1}\rfloor$. In particular the ordinary union $F$ already covers all levels $d>K$, because only the generating prime $p=q$ can supply such a level on the source side. Keep every member of $F$ and replace each excess copy by a fresh target position in the same residue class modulo $D$. There are at least $m$ positions in every class, which is enough for the whole multiset. This preserves every small level $d\le K$, since $d\mid D$, and gives an actual set of size $m$.

The same repair applies to arbitrary subsets in prime fibers with quotient upper bound $K$. Choose an assignment of source rows to their roots $p$. In each target $p$-bank take any actual quotient cover that dominates those assigned cofactors separately at every prime-power level, padding the local bank up to its source cardinality for the root level if necessary. Call the sum of local costs $s$. For $q^j>K$ all source demand comes from its own root; this root's quotient level $q^{j-1}$ is paid by its local bank (the case $j=1$ follows from padding). For $q^j\le K$ the multiset of local banks dominates. The same replacements give $H\le s$ whenever $\lfloor M/D\rfloor\ge s$. No pair-count or target overlap hypothesis is needed.
