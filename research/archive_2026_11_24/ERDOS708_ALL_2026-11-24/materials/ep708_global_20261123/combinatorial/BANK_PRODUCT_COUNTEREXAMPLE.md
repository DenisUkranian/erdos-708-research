# A counterexample to universal prime-deletion bank-product divisibility

## Statement and scope

For a finite set \(A\subseteq\{2,\ldots,M\}\) and an interval \(I\) of
\(M\) consecutive positive integers, write

\[
 U(A,I)=
 \bigcup_{a\in A}\ \bigcup_{\substack{q\mid a\\q\ \mathrm{prime}}}
 \{b\in I:a/q\mid b\}.
\]

The assertion

\[
 \prod_{a\in A}a\ \mid\ \prod_{b\in U(A,I)}b                         \tag{1}
\]

is false in general. The example below has every source of total prime
degree at least three. It even satisfies the numerical prime-cap and
quadratic ambient restrictions arising in the usual minimality reduction.
It does **not** satisfy the necessary forced-bank size restriction, and
therefore is not a counterexample to Erdős problem 708, to its proposed
asymptotic bound, or to the remaining joint weighted-bank inequality.

Everything needed to specify and check the example is contained in the
adjacent files:

- bank_product_certificate.json: all CRT residues and rough offsets, with
  the exact center and period in hexadecimal;
- verify_bank_product_counterexample.py: independent standard-library
  verifier, which reads only this certificate;
- bank_product_verification.json: the actual verification output.

The construction was suggested by an earlier \(\Omega\ge2\) matching
obstruction. The present certificate and verification are autonomous.

## 1. A finite CRT neighborhood with a deficiency of one

Set

\[
 N=11763=3^2\cdot1307,\qquad H=5881,\qquad N=2H+1,
\]

and let

\[
 S=\{s:4\le s\le N,\ s\text{ composite}\}.
\]

Trial division gives

\[
 \pi(N)=1409,\qquad |S|=N-1-\pi(N)=10353.                         \tag{2}
\]

The certificate specifies one residue \(c_r\) for each prime \(r\le N\),
and 1411 distinct offsets \(k\in[-H,H]\), satisfying

\[
 c_r+k\not\equiv0\pmod r
 \quad\text{for every listed offset and every prime }r\le N.     \tag{3}
\]

Let \(p=11777\), the first prime greater than \(N\). Define \(C\) to be
the least nonnegative simultaneous solution of

\[
 C\equiv c_r\pmod r\quad(r\le N,\ r\text{ prime}),\qquad
 C\equiv H+1\pmod p.                                             \tag{4}
\]

All moduli in (4) are different primes. Thus (4), together with the
certificate's full residue table, is an exact specification of the
integer \(C\). Its hexadecimal expansion is also included. The verifier
reconstructs \(C\) from scratch by successive CRT steps and checks
every residue and the full period. In particular, \(C>H+1\).

Put \(J=[C-H,C+H]\cap\mathbb Z\). The union of all proper
prime-deletion quotient neighborhoods of \(S\) in \(J\) is

\[
 V=\bigcup_{s\in S}\ \bigcup_{\substack{q\mid s\\q\text{ prime}}}
     \{t\in J:s/q\mid t\}
   =\{t\in J:\text{some prime }r\le N/2\text{ divides }t\}.        \tag{5}
\]

Indeed, \(s/q\ge2\) and any prime factor of this quotient is at most
\(s/q\le N/2\), proving the first inclusion. Conversely, for every
prime \(r\le N/2\), the source \(2r\in S\) has quotient
\((2r)/2=r\), proving the reverse inclusion.

The 1411 offsets in (3) are outside \(V\). Directly marking the
multiples of primes \(r\le N/2\) in this length-\(N\) interval gives

\[
 |V|=10352<10353=|S|.                                           \tag{6}
\]

The verifier checks this exact count, not merely its upper bound.
In fact the complement \(J\setminus V\) is exactly the 1411 saved
offsets. No unproved assertion about simultaneous prime values is used.

## 2. Lifting the deficient neighborhood to a product deficit

Define

\[
 A=\{ps:s\in S\},\qquad M=pN=138532851,
\]

and take

\[
 I=\{p(C-H-1)+1,\ldots,p(C+H)\}.                                 \tag{7}
\]

Because \(N\in S\), the largest source is exactly \(M\).
The interval (7) has exactly \(pN=M\) elements. Its multiples of
\(p\) are precisely

\[
 \{pt:t\in J\}.
\]

Condition (4) makes the residues of \(J\) modulo \(p\) precisely
\(1,2,\ldots,N\). Since \(N<p\), none of these \(t\)'s is divisible
by \(p\). Consequently every multiple of \(p\) in \(I\) has
\(p\)-adic valuation exactly one.

For \(s\in S\) and a prime \(q\mid s\), the bank obtained from
\(a=ps\) by deleting \(q\) contains \(pt\) precisely when
\(s/q\mid t\). The other bank, obtained by deleting \(p\), contains
\(pt\) precisely when \(s\mid t\), since \(\gcd(s,p)=1\).
This last condition implies \(s/q\mid t\) for any prime divisor
\(q\) of the composite \(s\), and hence adds no new \(p\)-multiple.
It follows exactly that

\[
 U(A,I)\cap p\mathbb Z=\{pt:t\in V\}.                            \tag{8}
\]

Equations (2), (6), and (8) now give

\[
 v_p\!\left(\prod_{a\in A}a\right)=10353,\qquad
 v_p\!\left(\prod_{b\in U(A,I)}b\right)=10352.                    \tag{9}
\]

Thus (1) fails by exactly one unit in the \(p\)-row.
Every \(a=ps\) has \(\Omega(a)=1+\Omega(s)\ge3\).

## 3. Why this does not refute the required minimal-case inequality

Let \(m=|A|=10353\). The chosen lifting prime satisfies

\[
 p=11777<2m-1=20705,
\]

and

\[
 M=138532851<16m^2=1714953744.
\]

Thus those two necessary numerical restrictions alone do not rule out
the construction.

However, \(4p\in A\), and deleting \(p\) from this source gives
cofactor \(4\). Therefore \(U(A,I)\) contains the entire bank of
multiples of \(4\), whose cardinality is at least

\[
 \lfloor M/4\rfloor=34633212>10m.
\]

In any least-cardinality failure with budget \(cm\), for
\(2<c\le10\), every individual deletion bank must fit inside a
deletion cover of size at most
\(\lfloor c(m-1)\rfloor\). This bank cannot fit. The construction
therefore lies outside the relevant minimal class.

There is also substantial oversupply in every other source-prime row.
For a source prime \(r\ne p\), write
\(D_r=\sum_{s\in S}v_r(s)\). Then \(D_r\ge1\) and

\[
 D_r\le\sum_{j\ge1}\lfloor N/r^j\rfloor\le N/(r-1).
\]

Since the multiples of \(4r\) belong to the bank of \(4\), we have

\[
 \begin{aligned}
 v_r\!\left(\prod_{b\in U(A,I)}b\right)
 &\ge\lfloor M/(4r)\rfloor\\
 &\ge \frac p8\,D_r-1\\
 &\ge \left(\frac p8-1\right)D_r
 >1471D_r.                                                       \tag{10}
 \end{aligned}
\]

The middle inequality uses \((r-1)/r\ge1/2\); the final one uses
\(p=11777\). This remains a valid lower bound when \(r=2\):
multiples of \(4r=8\) are still contained in the bank of \(4\).

In particular, for clipped nonnegative prime weights \(w_r\le1\),
if every source has
\(X_w(a)=\sum_r w_rv_r(a)>2\), then

\[
 \sum_{r\ne p}w_rD_r>(2-w_p)m\ge m.
\]

By (9) and (10),

\[
 \sum_{b\in U(A,I)}X_w(b)-\sum_{a\in A}X_w(a)
 >1470\sum_{r\ne p}w_rD_r-w_p>0.                                \tag{11}
\]

Thus this particular product-divisibility counterexample actually
satisfies the desired direction of joint weighted surplus whenever
all sources have weight greater than two. It falsifies the
coordinatewise shortcut, not the remaining joint statement.

## Verification

Run the adjacent Python verifier with no arguments. It independently
checks primality, the source count and maximum, all CRT residues,
all 1,988,099 rough-offset avoidance conditions, all individual source
prime-deletion quotients, the exact neighborhood mask, the lifted
interval and \(p\)-valuations, and the stated scope restrictions.

Only the length-\(11763\) quotient interval is enumerated. The very large
shift and the length-\(138532851\) lifted interval cause no approximation
or numerical overflow: all arithmetic uses exact Python integers.
