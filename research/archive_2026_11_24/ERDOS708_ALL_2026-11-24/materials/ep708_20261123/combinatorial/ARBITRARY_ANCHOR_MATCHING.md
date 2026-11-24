# Matching after exact exclusion of a fixed set of anchor primes

Date: 2026-11-23 (Kyiv).

This is an unconditional theorem for a restricted class of source
sets. It does not solve unrestricted Erdős problem 708. The argument
has been checked independently within the research session; no
priority claim or formal-verification claim is made.

## 1. Definitions and theorem

Let `Q` and `R` be disjoint finite prime sets, and suppose

`max Q < y <= min R`,

where the restriction involving `max Q` is omitted if `Q` is empty.
Write

`k=|Q|`, `C=2^k`, `eta=product_{q in Q}(1-1/q)`,

`mu_R=sum_{r in R}1/r`,

`pi_R(t)=#{r in R:r<=t}`,

`rho_y(R)=sup_{t>=y}(pi_R(t)+1)/t`,

`tau_y(R)=sup_{t>=y}pi_R(t)/t`.

Assume

`eta(1-mu_R) >= C rho_y(R)+tau_y(R)`.                            (H)

Let `A` be a set of `n` distinct integers in `[2,M]`, each of whose
prime factors belongs to `Q union R`. Let `I` be any interval of `M`
positive consecutive integers. Put

`A_R={a in A: some r in R divides a}`,

`A_Q=A\A_R`, `n_R=|A_R|`.

Then there is an injective assignment `a -> b_a in I` for all
`a in A_R` such that

`a/Pmax(a) divides b_a`.

Consequently there is a subset `B of I` satisfying

`product A divides product B`,

`|B| <= 2n_R + sum_{a in A_Q}Omega(a)`.                          (1)

In particular, if `A_Q` is empty, the exact bound `|B|<=2n` holds.
Here `Omega(a)` counts prime-factor occurrences with multiplicity.

The case `R` empty can be treated separately by prime-unit repair;
the theorem and its asymptotic consequences concern nonempty `R`.

## 2. A coprimality count with a uniform error

Let `L=product_{q in Q}q`. For any real interval `J` of length `T`,
Möbius inversion gives

`#{m in J: gcd(m,L)=1}`
`=sum_{e|L}mu(e) #{m in J:e|m}`
`=eta T+E`, with `|E|<=C`.                                      (2)

Indeed, every multiple count differs from `T/e` by at most one,
and `L` has exactly `C` squarefree divisors. If `r in R`, the count of
integers in `J` that are both divisible by `r` and coprime to `L`
equals the coprimality count in `J/r`, because `gcd(r,L)=1`.

## 3. Hall's condition for composite sources containing an R-prime

For each composite source `a in A_R`, write

`p=Pmax(a) in R`, `d(a)=a/p>1`.

Give `a` every target neighbor `b in I` divisible by `d(a)`.
Consider any subset `S` of these composite sources, and let

`D={d(a):a in S}`

be its distinct quotient set. For `d in D`, put `T_d=M/d`. Every
prime divisor of `d` from `R` is at most the removed prime `p`, hence
at most `T_d`, and `T_d>=p>=y`.

For a target integer `b in I`, define the signed certificate

`K_D(b)=sum_{d in D}1[d|b] 1[gcd(b/d,L)=1]`
`                    *[1-sum_{r in R,r<=T_d}1[r|b/d]]`.          (3)

We claim

`K_D(b)<=1[b in N(S)]`,                                         (4)

where `N(S)` is the union of the divisibility neighborhoods.

To prove this, any positive summand in (3) has value one. It forces
`d` to be the full smooth part of `b` supported on

`Q union (R intersect [2,M/d])`.

This is because every prime divisor of `d` belongs to that set, and
the coprimality condition and the zero negative sum exclude every
additional occurrence of those primes in `b/d`.

There cannot be two positive summands. If `d<e` were both positive,
then `M/d>M/e`; the full smooth part at the larger threshold would be
at least the full smooth part at the smaller threshold. This would
give `d>=e`, a contradiction. All remaining summands are nonpositive.
Outside `N(S)` every divisibility indicator vanishes, so (4) follows.

For a fixed `d`, formula (2) applied to `I/d` and to `I/(dr)` gives

`sum_{b in I} 1[d|b]1[gcd(b/d,L)=1]`
`                    *[1-sum_{r in R,r<=T_d}1[r|b/d]]`

`>= eta T_d[1-sum_{r in R,r<=T_d}1/r]`
`   -C[pi_R(T_d)+1]`

`>= T_d[eta(1-mu_R)-C rho_y(R)]`

`>= T_d tau_y(R) >= pi_R(T_d)`,                                (5)

where (H) was used in the penultimate step.

For each `d`, there are at most `pi_R(T_d)` source preimages: any such
source has the form `dr` with `r in R`, `r<=T_d`. Distinct sources
cannot have the same pair `(d,r)`. Thus

`|S|<=sum_{d in D}pi_R(T_d)`.

Summing (4)--(5) gives `|N(S)|>=|S|`. Hall's theorem proves the
required injective assignment for all composite sources in `A_R`.

If a source in `A_R` is itself prime, its quotient is one and every
target is a neighbor. Assign these prime sources afterward to unused
targets. There is enough room, because `n_R<=n<=M-1`.

## 4. Prime-unit repairs prove the covering bound

Let `B_0={b_a:a in A_R}`. The assignment gives `|B_0|=n_R` and

`product_{a in A_R}(a/Pmax(a)) divides product B_0`.

Relative to the product of all sources in `A`, the sum of the positive
prime-valuation deficits of `product B_0` is therefore at most

`n_R+sum_{a in A_Q}Omega(a)`.                                   (6)

The product of all integers in `I` is divisible by `M!`: after writing
`I={x+1,...,x+M}`, this is the integrality of
`(x+1)...(x+M)/M! = binomial(x+M,M)` for nonnegative integer `x`.
Also `product A` divides `M!`, since the sources are distinct and lie
in `[1,M]`.

Whenever a prime valuation is still deficient, some unused target
contains that prime. Otherwise the full interval product would have
the same deficient valuation, contradicting the preceding paragraph.
Add one such target. The total remaining deficit drops by at least
one and never increases at another prime.

After at most the number of additions in (6), all deficits disappear.
The resulting subset has size at most

`n_R+[n_R+sum_{a in A_Q}Omega(a)]`,

which is (1). This proof handles possible overlaps directly by adding
only unused targets; it does not combine independently chosen covers.

## 5. A restricted asymptotic consequence with fixed anchors

Fix `Q` and `epsilon>0`. If `min R` tends to infinity and

`mu_R<=1-epsilon`,

then (H) holds for all sufficiently large `min R`, because

`rho_y(R)<=sup_{t>=y}(pi(t)+1)/t -> 0`,

and similarly `tau_y(R)->0`. The constants `C` and `eta` are fixed.

The number of `Q`-smooth positive integers at most `M` is at most

`product_{q in Q}(1+floor(log M/log q))`.

Each has at most `log M/log 2` prime-factor occurrences. Hence

`sum_{a in A_Q}Omega(a)=O_Q((1+log M)^(|Q|+1))`.                 (7)

In the regime `M<=16n^2`, this is `o(n)`. The already known exact
`2n` theorem for `M>=16n^2` handles the complementary regime. Thus
the present argument yields `2n+o(n)` for this restricted family of
source sets, uniformly in the interval shift.

This leaves unrestricted intermediate prime ranges untreated.

## 6. Optional sharper version using only non-anchor cofactor primes

Let `R_0` be the union of the `R`-prime supports of the quotients
`a/Pmax(a)` for composite `a in A_R`. In (3), only primes from `R_0`
need to be excluded, while the source-preimage count still uses `R`.
The same proof therefore works under the weaker condition

`eta[1-mu_0(R_0)]`
` >= sup_{T>=y}{C[pi_{R_0}(T)+1]+pi_R(T)}/T`.                   (8)

Every prime in `R_0` is at most `sqrt(M)`. Consequently, if `Q` is
fixed and every non-anchor source prime is at least `M^alpha`, with
fixed `alpha>1/(2e)`, then (8) holds for all sufficiently large `M`:

`mu_0(R_0)<=log((1/2)/alpha)+o(1)<1`

when `alpha<1/2`, while the density-error term tends to zero. The
case `alpha>=1/2` is immediate or has only a possible boundary square.
Together with (7) and the same large-`M` theorem, this gives another
explicit restricted `2n+o(n)` class with the same fixed anchors.

