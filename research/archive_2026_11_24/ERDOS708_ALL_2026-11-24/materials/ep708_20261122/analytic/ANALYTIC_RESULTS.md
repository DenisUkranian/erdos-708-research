# Erdős 708: analytical work, 22 November 2026

## Status

The general inequalities `g(n) <= 2n` and `g(n) <= (2+o(1))n` are **not proved here**. This note records a complete all-scale peeling argument, a conditional transfer from the hinge inequality without an interval-size gap, and an audit and repair of one binary sparse-sieve step. No priority claim is made. The transfer develops the source-subset argument in Ziming Wang's `raw-transfer.tex`; the first-source saving develops Bergström's cumulative-GCD peeling argument.

Throughout, `A` is a set of `n` distinct integers at least two, `M >= max A`, and `I` is a positive interval of `M` integers. A cover is a **subset**, so every position is used at most once. Zero-containing and negative intervals reduce by the usual singleton/reflection arguments.

## 1. All-scale whole-cofactor peeling with a saving per large-prime group

Fix an integer `Z >= 2`. Let `A0` contain the sources whose largest prime factor is at most `Z`. Let `r = |A \ A0|`, and let `t` be the number of distinct largest prime factors of those `r` sources. Suppose `B0` covers `A0`. Put

`K = |B0| + 2r - t`.

**Theorem.** If `r > 0` and `Z >= K`, then `B0` extends to a cover of `A` using at most `K` positions. No hypothesis such as `Z^2 > M` is required.

### Extension lemma

Suppose `H | product(B)`, `h <= M`, and `gcd(H,h) <= floor(M/(|B|+1))`. Then one unused interval position can be added so that its enlarged product is divisible by `Hh`.

Indeed, use an unused multiple of `h` if one exists. Otherwise `h` divides the current product, as does `H`, hence their least common multiple does. There are at least `|B|+1` multiples of `gcd(H,h)` in `I`; one is unused and supplies the missing factor. For a unit request, no position need be added.

### Proof of the theorem

Group each rough source by its largest prime `p > Z`, and write its group as `a_{p,1},...,a_{p,m_p}`.

1. **First complete source in each group.** Process the groups in increasing `p`. Before the first source of a new group is processed, the target product consists of smooth sources and one source from groups with smaller largest prime. Thus `p` does not divide this target `H`. Consequently

   `gcd(H,a_{p,1}) <= a_{p,1}/p <= M/p < M/Z`.

   The extension lemma adds at most one position. There are at most `|B0|+t <= K` positions at the end of this stage.

2. **One chosen prime from every remaining source.** For each group, supply `m_p-1` additional copies of `p`.

   - If `p^2 <= M`, the interval contains at least `floor(M/p) >= p > Z >= K` multiples of `p`. Add a fresh multiple for every requested copy; there are never `K` forbidden positions before an addition.
   - If `p^2 > M`, no source at most `M` contains `p` twice, and no source whose largest prime is different can contain `p`. The target after stage 1 therefore has `p`-valuation exactly one. The interval contains at least `floor(M/p) >= m_p` multiples of `p`, since the original sources in this group are distinct multiples of `p`. If the current product has valuation `u < m_p`, at most `u` current positions are divisible by `p`, leaving at least `m_p-u` unused multiples. Add those needed. This uses at most `m_p-1` positions.

   Intersections between carriers of different large primes are harmless; only the total target valuations matter.

3. **Remaining complete cofactors.** For every `j >= 2`, supply `d=a_{p,j}/p`. It has at least `floor(M/d) >= p > Z >= K` multiples in the interval. Put each nonunit cofactor on a fresh position. This uses at most another `sum_p(m_p-1)=r-t` positions.

The total is at most `|B0|+t+(r-t)+(r-t)=K`. All cofactors in the final stage use fresh positions, so repeated primes and repeated cofactors do not create double counting. The proof permits additional large primes, and additional copies of the chosen prime, inside a cofactor.

### Computational stress check

`test_peeling.py` implements the construction, maintaining exact integer divisibility after every stage. It passed 11,438 random rough-only instances and 6,000 random mixed instances, with up to eight sources, maxima up to 500, and shifts up to 10^7. These checks support implementation correctness; the theorem rests on the argument above.

## 2. A gap-free conditional transfer from H2

For weights `0 <= w_p <= 1`, write `X_w(k)=sum_p w_p v_p(k)`. Assume the global hinge inequality

`sum_{a=1}^M (X_w(a)-2)_+ <= sum_{b in I} (X_w(b)-1)_+`.

The raw boxed relaxation uses coefficients `v_p(b)` and constraints `0 <= x_b <= 1`. The adjective **raw** refers only to the absence of demand capping on these coefficients; it never permits `x_b > 1`.

Finite LP duality gives

`L_raw(A,I)=max_{w>=0} [sum_{a in A} X_w(a) - sum_{b in I}(X_w(b)-1)_+]`.

Clipping a dual coordinate `w_p>1` down to one cannot reduce the objective: every affected interval hinge is still linear, and the interval supplies at least the total `p`-valuation of the distinct sources in `[1,M]`. Thus H2 implies `L_raw(A,I) <= 2|A|`.

Let `q_n >= 2` be the least integer with

`q_n >= 2n + pi(q_n) - 1`.

It exists, since `q_n <= 4n` follows from `pi(4n) <= 2n`.

**Conditional theorem.** H2 implies, for every `n`,

`g(n) <= 2n + pi(q_n) - 1 = 2n + (2+o(1))n/log n`.

In particular it implies the asymptotic conjecture, for **all interval lengths**.

### Proof

Split at `Z=q_n`, and retain the `m` smooth sources. If `m>0`, solve their raw boxed LP on the full interval (or on a contained interval of their maximum length). At an optimum vertex at most `pi(Z)` coordinates are fractional. Rounding upward gives a smooth cover with

`|B0| <= 2m + pi(Z) - 1`.

For `m=0`, use the empty cover. The all-scale peeling theorem then adds at most `2(n-m)-t`, and its required budget is at most `2n+pi(Z)-1 <= Z`. If there are no rough sources, the smooth rounding itself proves the result. This proof never requires `M < Z^2` and hence leaves no quadratic-to-cubic interval band.

The estimate `q_n=2n+O(n/log n)` follows from `2n-1 <= q_n <= 4n` and the prime number theorem (an elementary `pi(x)=O(x/log x)` suffices for the big-O version); then `pi(q_n)=(2+o(1))n/log n`.

**Outstanding obligation:** prove H2 itself, or an adequate uniformly relaxed hinge estimate. The transfer theorem does not discharge that obligation and does not prove the exact bound `2n`.

### The simpler previously known envelope

For a final account, the simpler Wang bound is sufficient: take `Z=4n`. The smooth cover costs at most `2m+pi(4n)-1`. Choose one prime `p>Z` from each remaining source and cover these chosen prime copies on at most `n-m` positions; this step only overlaps the smooth cover in prime coordinates that the smooth sources do not require. Each remaining whole cofactor has more than `Z` candidate multiples. Put those cofactors on fresh positions, giving `g(n)<=2n+pi(4n)-1`. This argument already covers every `M`; the optimization above is unnecessary for the main logical conclusion.

## 2a. Why direct averaging of binary weights loses a macroscopic term

Set `P_t={p:w_p>=t}` for `0<t<=1`, and `Omega_t(b)=sum_{p in P_t}v_p(b)`. Then `X_w(b)=integral_0^1 Omega_t(b) dt`. Jensen followed by a hypothetical binary H2 gives

`sum_[1,M] (X_w-2)_+ <= integral_0^1 sum_I (Omega_t-1)_+ dt`.

However, at each positive integer `b` the last integrand has the exact integral

`integral_0^1 (Omega_t(b)-1)_+ dt = X_w(b)-max_{p|b}w_p`.

The needed expression is `(X_w(b)-1)_+`. The loss is

`min(X_w(b),1)-max_{p|b}w_p >= 0`.

This loss is not uniformly `o(n)`. With only `w_2=1/2`, it equals `1/2` at every multiple of four and zero elsewhere, totaling about `M/8`. For `M` of order `n^2`, it is much larger than the entire desired error budget. The original one-prime inequality is nevertheless true: the example diagnoses a loss in this proof route, not a counterexample to H2. Separating prime-by-prime excess before averaging removes this one-prime loss, but intersections of distinct primes still produce positive losses; two clipped contributions of `1/2` produce loss `1/2` at a joint multiple. A successful argument must control the coupled Jensen gaps or use a stronger matching/transport statement.

## 3. A false numerical step in the smooth-hinge manuscript, and a repair

Bergström's smooth-hinge manuscript asserts, for every binary prime set of harmonic mass `0<mu<1`, the numerical inequality

`mu/(1+mu) > (mu^2 + sum_p p^(-2))/2`.

This is false. For `S={2,3,7}`:

`mu=41/42`, `sum_p p^(-2)=673/1764`,

`mu/(1+mu)=41/83 < 1177/1764=(mu^2+sum_p p^(-2))/2`.

The discrepancy is `25367/146412 > 0`. The stated restriction `p <= L^(1/2-theta)` does not exclude this fixed set when `L` is large. This invalidates the displayed comparison, not H2 itself.

### Corrected binary sparse lemma

Let `S` be a finite set of `k` primes; put `mu=sum_{p in S}1/p` and `sigma2=sum_{p in S}1/p^2`. Let `J` be any interval of `L` consecutive positive integers. Then

`#{b in J : some p in S divides b} >= L(mu-(mu^2-sigma2)/2) - k - k(k-1)/2`.

This is the two-term Bonferroni inequality, using `N_J(p) >= L/p-1` and `N_J(pq) <= L/(pq)+1`.

On the initial segment, numbers with `Omega_S(a)>=2` are covered by prime squares and distinct prime pairs, so

`#{a<=L : Omega_S(a)>=2} <= L(mu^2+sigma2)/2`.

Consequently the desired level-count comparison follows whenever

`L mu(1-mu) >= k(k+1)/2`.

For example, if `mu <= 1-delta`, all selected primes are at most `L^(1/2-theta)`, and `L` is sufficiently large in terms of `delta,theta`, the condition holds uniformly: `mu >= k/L^(1/2-theta)` and `k <= L^(1/2-theta)` make the error ratio tend to zero. This repairs the binary sparse regime using Bonferroni directly. It does **not** handle all fractional weights or the transition `mu` arbitrarily close to one.

## Sources checked

- Ziming Wang, `https://github.com/science-prince/erdos-708-interval-divisor-covers`, especially `papers/main-paper/raw-transfer.tex`.
- C. Bergström, `https://github.com/pathscale/erdos-708-asymptotic`, whole-cofactor peeling.
- C. Bergström, `https://github.com/pathscale/erdos-708-remediation`, `paper/erdos708-smooth-hinge.tex`.
- Haoyu Chen, `https://github.com/chy4pro/erdos-708-explicit-upper-bounds`.

All statements marked conditional remain conditional. No communication or publication to the source authors was performed.
