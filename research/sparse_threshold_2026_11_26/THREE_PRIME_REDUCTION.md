# A fixed gap in the next exponent range forces three comparable primes

Let $A$ be a set of $n$ distinct integers in $[1,M]$, with $n\le M^{41/50}$. Let $B(A)$ count those rows $a\in A$ admitting a factorization $a=hpqr$ with three distinct primes of exponent one in $a$ satisfying

$$
M^{0.259}<p,q,r<M^{0.281},\qquad h\le M^{0.191}.
$$

For some absolute $c>0$, uniformly in all positive windows $I$ of length $M$ and all such $A$,

$$
H(A,I)\le 2n+B(A)+O(n^{1-c}).
$$

In particular, if the actual product-cover cost exceeds $(2+\delta)n$ for fixed $\delta>0$, then $B(A)\ge(\delta-o(1))n$. This identifies a necessary class in the not-yet-covered part of $M\ge n^{50/41}$. The theorem above does not itself give the unrestricted two-per-row bound at exponent $50/41$.

## Proof

Fix $\beta=41/50$, $G=1-\beta=9/50$. Use the parameters, heavy extraction and records from [the main construction](FIVE_QUARTERS.md) with these fixed exponents. The cubic range is already covered. For every record with at least three retained high bands the old weight condition holds, since $\beta/G=41/9<16/3$, and the minimum of $(k+1)^2/k$ over integers $k\ge3$ is $16/3$. There are boundedly many possible values of $k$, so the parameter choices can preserve a fixed margin. Records with no high bands always qualify.

All qualifying records and main labels are treated by the main construction. The [one-exceptional-band proof](SEVEN_TERM_TRANSFER.md) continues to work at this fixed $\beta$, since $41/50<14/17$ and $41/50<5/6$. The restriction $\beta<9/11$ in that proof served to ensure that records with two retained high bands qualified automatically.

Consider a nonqualifying quotient label with two retained high bands of lower endpoint exponents $x\le y$. Let $H$ denote its numerical value and $d$ its extraction divisor, so that the original row is $dH$. The record weight estimate and the bound $H\le M^{\beta+\lambda}$ give, for arbitrarily small fixed $\eta>0$ after choosing the proof parameters,

$$
x+y>3G-\eta,\qquad x+2y\le\beta+\eta.
$$

There are three distinct prime bases, one in each retained band and another at least $M^y$ from the omitted or tied largest band. Their exponents as log-base-$M$ numbers are all at least $x\ge6G-\beta-3\eta$ and at most $\beta-3G+2\eta$, since the other two contribute at least $x+y$. Their product is at least $M^{x+2y}\ge M^{(3/2)(x+y)}$. Choose $\eta>0$ sufficiently small, for example below $10^{-4}$. These bounds put every prime strictly between $M^{0.259}$ and $M^{0.281}$ and the product above $M^{0.809}$. Since $4(0.259)>\beta+\eta$, all three occur to exponent one in $H$. The divisor $d$ is unitary in its row, hence none of the three divides $d$. The remaining cofactor of the original row is at most $M^{0.191}$. Each such exceptional quotient therefore comes from a different row counted by $B(A)$.

For each such exceptional label $H=vpqr$, remove one of its three specified prime atoms, say $r$, leaving $U=H/r$. We have $U\le M^{0.82+\eta-0.259}<M^{0.562}$. Feed $U$ back into the ordinary quotient placement, with its own record computed anew. In inequality (3) of [the main construction](FIVE_QUARTERS.md), the proof bounds the sum of the logarithms of selected primes and one extra prime by $\log_M U$. One can therefore use $0.562$ in place of $\beta+\lambda$ at precisely this step. Since $0.562/G<4$, every new record satisfies the usual lower bound on its color probability with a uniform margin. The other comparisons still use the original $X$, $M$ and $G$. Refine the fixed constants to handle both the new and the old margins.

Keep the original quotient labels for qualifying records and the one-high-band procedure. Replace each remaining two-high-band label by just one $U$ for the placement construction. Each replacement divides its own original occurrence. Consequently the joint count of ordinary and replacement quotient tasks divisible by any $w$ is still at most $X/w$, including coincidences between labels coming from different groups. This is exactly the multiplicity input both for placing equal labels and for restoring their screened parts. Single-atom tasks can simply be deferred. The removed prime $r$ is distinct from all prime bases of $U$ and is preserved as a deferred singleton. Thus every modified original row requires at most one additional slot. Repair that singleton in the final nested-level step along with all other outstanding labels. The number of affected rows is at most $B(A)$, giving the claimed bound.
