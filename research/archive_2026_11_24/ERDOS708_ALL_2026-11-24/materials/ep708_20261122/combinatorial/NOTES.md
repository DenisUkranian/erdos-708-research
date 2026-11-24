# Combinatorial investigation of Erdős Problem 708

Date: 2026-11-22.

## Status

This investigation does not prove `g(n) <= 2n` or the asymptotic conjecture.
The statements below are proved elementary reductions, a check of a proposed
matching shortcut, and a reconstruction of the known support-component bound.
The latter is **not claimed as new**.

Let `A` be a set of distinct integers in `[2,M]`, and let `I` be an interval
of `M` positive integers. Write `P = product(A)`. For every prime `p` and
integer `e >= 1`, the number of elements of `I` divisible by `p^e` is at
least `floor(M/p^e)`, hence at least the number of elements of `A` divisible
by `p^e`.

## 1. The proposed prime-quotient matching

The sources are integers `m <= M` with `Omega(m) >= 3`. A source `m` is
adjacent to `b in I` when `m/p` divides `b` for at least one prime `p | m`.

An injective matching of all sources would imply the weighted hinge
inequality `H_2`. Indeed, for any prime weights `0 <= w_p <= 1`, put
`W(t) = sum_p v_p(t) w_p`. On a matched edge one has
`W(b) >= W(m/p) >= W(m)-1`, and therefore
`(W(b)-1)_+ >= (W(m)-2)_+`. The sources omitted from the graph have
`W(m) <= Omega(m) <= 2`, so their left-hand hinge contribution vanishes.

This matching statement is only a sufficient condition. It remains
unproved in this investigation.

### 1.1 Exact restrictions on a Hall obstruction

Let `N(m)` denote the target neighborhood. If `m | m'`, then
`N(m')` is a subset of `N(m)`. To see this, if `m'/q | b`, then:

* if `q | m`, the integer `m/q` divides `m'/q`;
* otherwise `m` divides `m'/q`, and any prime quotient `m/p` divides it.

Consequently a Hall-deficient source set can be enlarged to an upward
closed set under divisibility without enlarging its neighborhood.

If `S` has `u = |N(S)| < |S|`, then every prime factor `p` of every
`m in S` satisfies

`p <= floor(M/(m/p)) <= u`.

Also `m/p > M/(u+1)` for every such quotient. Thus a counterexample may be
sought entirely among `u`-smooth sources, with all their prime quotients in
`(M/(u+1), M/2]`. This is a reduction, not a contradiction.

### 1.2 A rigorous failure of the largest-prime-only shortcut

Take `M = 440`, `I = {4401,...,4840}`, and

`S = {2k : 1 <= k <= 220, k composite, k != 169}`.

There are `220 - 1 - pi(220) - 1 = 171` sources, since `pi(220)=47`.
Each source has at least three prime factors counted with multiplicity.

If only the largest prime may be deleted, all resulting quotients are
divisible by one of `4,6,10,14,22`. Indeed a composite `k <= 220`, other
than `169`, has least prime factor in `{2,3,5,7,11}`. Conversely all five
basic quotients occur: use sources `8,18,50,98,242`.

The neighborhood is therefore exactly the union of multiples of
`4,6,10,14,22` in `I`. Its center is `4620`. Dividing the even offsets by
two identifies this neighborhood with integers in `[-109,110]` divisible
by at least one of `2,3,5,7,11`.

The omitted positive integers up to `109` are `1` and the 24 primes from
`13` through `109`; no composite with all prime factors at least `13` is
that small. Their negative counterparts are also omitted, whereas `110`
is included. Hence the neighborhood has `220 - 2*25 = 170` elements.

This is an exact Hall violation, `171 > 170`, for the restricted rule.
It is **not** a counterexample to the full rule: for example, deleting
the prime `2` from source `18` permits quotient `9` and introduces the
additional target `4401`.

### 1.3 Exact CRT counterexample if the source condition is weakened to Omega >= 2

The full any-prime-quotient rule is false if all composite sources are
included. This is an unconditional finite construction; it assumes no
prime-tuple conjecture.

Take `M=11763`, `H=5881`, and let `K` be the 1411 distinct offsets in
`omega2_hall_certificate.json`, all in `[-H,H]`. The certificate gives,
for every prime `p <= M`, one residue `c_p` such that

`c_p + k != 0 (mod p)` for every `k in K`.

The Chinese Remainder Theorem supplies a positive integer center `C>H`
satisfying `C=c_p (mod p)` simultaneously. The full residue list is the
primary description of the shift; a hexadecimal representative is also
saved for reproducibility. Let `I=[C-H,C+H]`.

There are `pi(11763)=1409` primes up to `M`, so the source set of all
composites in `[1,M]` has

`M-1-pi(M)=10353`

elements. Every one of the 1411 distinct targets `C+k`, `k in K`, has
no prime divisor at most `M`, and therefore cannot be divisible by any
nontrivial prime quotient `m/p` of a composite source `m<=M`. Thus there
are at most `M-1411=10352` neighbors. This proves a strict Hall
violation.

The verifier also computes the neighborhood exactly. For all-composite
sources it is precisely the set of targets divisible by a prime
`q<=M/2`: each allowed quotient has such a prime factor; conversely the
source `2q` permits quotient `q`. The exact neighborhood count is
**10352**, so the deficiency is **one**.

The deterministic builder begins with the offsets `-1,1` and both signs
of primes in `(sqrt(H),H]`. In increasing prime order it removes a least
occupied residue class, preferring residue zero in a tie, until the next
prime exceeds the number of survivors. This produces the saved set `K`.
The proof does not rely on this search procedure: the independent
verifier checks the final offsets, every residue condition, CRT
consistency, and the exact neighborhood directly.

Files:

* `build_omega2_certificate.py`: deterministic builder, standard library;
* `omega2_hall_certificate.json`: exact offsets and CRT residues;
* `verify_omega2_certificate.py`: independent verifier using trial-division
  primality rather than the builder's sieve;
* `omega2_hall_verification.json`: checked counts and PASS result.

This construction refutes only the weakened `Omega>=2` matching lemma.
It is neither a counterexample to the `Omega>=3` matching proposal nor a
counterexample to Erdős Problem 708. No minimality or priority claim is
made.

## 2. Collision repair and the support-component bound

Let `E = sum_{a in A} omega(a)`, let `r` be the number of active primes,
and let `c` be the number of connected components of the bipartite
incidence graph with vertices `A` and the active primes, where `a` is
adjacent to `p` if `p | a`.

Then

`tau(A,I) <= E-r+c`.

### Proof, including arbitrary prime powers

Choose a multiple `b_a in I` of every `a`, and let `B0` be the distinct
chosen values. Group the sources by their chosen target. Write `t=|B0|`.

Fix a prime `p`. Let `s_p` be the number of sources divisible by `p`,
and `g_p` the number of source groups containing at least one such source.
Set `R_p=s_p-g_p`.

For an exponent level `e`, let:

* `d_e` be the number of sources with `v_p(a) >= e`;
* `c_e` be the number of all interval targets with `v_p(b) >= e`;
* `z_e` be the number of initially selected targets with that property;
* `g_e` be the number of source groups containing a source at that level.

We have `c_e >= d_e`, `z_e >= g_e`, and `d_e-g_e <= s_p-g_p=R_p`.
The last inequality follows by summing `k-1` over the nonempty groups:
at any exponent level a group contributes no more than its contribution
at level one.

Adjoin up to `R_p` unused targets with the largest `p`-adic valuations.
At level `e`, the resulting number of selected targets is

`min(c_e, z_e + R_p) >= d_e`.

If fewer than `R_p` unused targets exist, select all of them; the same
formula applies. Summing over exponent levels gives enough total
`p`-valuation. Taking the union of these repairs for all primes costs at
most `sum_p R_p`; overlap between different prime repairs only helps.

Now form the bipartite graph between the `t` target groups and the `r`
active primes. It has `sum_p g_p` edges. Contracting groups of source
vertices cannot increase the number of connected components, so it has
at most `c` components. Its edge count is consequently at least
`t+r-c`. Therefore

`|B| <= t + sum_p(s_p-g_p) <= t+E-(t+r-c)=E-r+c`.

### Consequences and limitation

The cycle rank of the original incidence graph is
`beta=E-n-r+c`, so the bound is equivalently `tau <= n+beta`.
In particular an acyclic incidence graph gives `tau <= n`, even when
individual source integers have arbitrarily many distinct prime factors
and arbitrary prime powers.

For squarefree semiprime sources viewed as graph edges, this becomes
`tau <= 2n-r+c`. It gives `11` for the connected `K_{4,2}` example with
eight sources and six primes.

This is a known support-component argument and is not a solution to the
general problem. Dense incidence hypergraphs can have cycle rank greater
than `n`; counting every cycle as one additional target discards useful
joint divisibility and can be far from optimal.

## 3. A weaker arithmetic form

For completeness, a simpler prime-unit repair gives

`tau(A,I) <= Omega(P/lcm(A)) + c`.

Each initially chosen group supplies its least common multiple. Missing
prime valuation units may be repaired one at a time because the entire
interval product is divisible by `P`. The graph on groups and prime-power
layers shows that the sum of the `Omega` values of the group least common
multiples is at least `Omega(lcm(A))+t-c`.

This weaker form was independently reconstructed first. It is dominated
by the support-component bound: for each prime, the total exponent minus
the maximum exponent is at least the number of sources containing that
prime minus one.

