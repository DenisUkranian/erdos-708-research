# Erdős 708: finite-support amplification analysis

## Status

No proof of the general asymptotic conjecture or of H2 is claimed. The theorem below rules out one natural amplification mechanism: a finite defect cannot persist to arbitrarily large interval lengths while using the same finite set of primes, even when the weights are allowed to vary.

Write `X_w(m)=sum_p w_p v_p(m)`, with `0<=w_p<=1`, and

`Delta_2(M,I,w)=sum_{m<=M}(X_w(m)-2)_+ - sum_{b in I}(X_w(b)-1)_+`.

Here `I` is any positive interval of `M` consecutive integers.

## Theorem: uniform eventual H2 for a fixed finite prime support

For every fixed finite set `P` of primes there is a finite `M0(P)` such that

`Delta_2(M,I,w)<=0`

for all `M>=M0(P)`, all intervals `I`, and all weights supported on `P`. The threshold is uniform in the weights and the shift.

### Small-weight regime

Assume `P` is nonempty, put `Q=max P`, and let

`rho=max_{p in P} w_p/log p`.

If `rho=0`, there is nothing to prove. Set

`C_P=product_{p in P} (1-1/p)/(1-p^(-1/8))`.

Choose a positive `rho0` so small that

`Q exp(-1/(2 rho0)) <= 1/2`

and

`(32 Q C_P rho0/(7e)) exp(-1/(4 rho0)) <= 1`.

Such a choice exists. The left sides are increasing functions of `rho0`, so both estimates hold for every `0<rho<=rho0`.

Take `t=7/(8 rho)`. Since `t w_p <= (7/8) log p`, a nonnegative Dirichlet-convolution expansion of the multiplicative function `exp(t X_w(m))` yields

`sum_{m<=M} exp(t X_w(m)) <= M product_p (1-1/p)/(1-exp(t w_p)/p) <= M C_P`.

Indeed, its convolution with the Möbius function is supported on `P`-smooth integers and has nonnegative prime-power coefficients `exp(tjw_p)-exp(t(j-1)w_p)`.

The elementary inequality `(u-2)_+ <= exp(t(u-2))/(e t)` therefore gives

`sum_{m<=M}(X_w(m)-2)_+ <= M (8 rho C_P/(7e)) exp(-7/(4 rho))`.  (1)

On the other hand, `X_w(m)<=rho log m`. Thus if `M<=exp(2/rho)`, the left side of H2 is zero. Otherwise choose a prime `p` attaining `rho`, write `w=w_p>0`, and put `j=ceil(3/(2w))`, `D=p^j`. Then

`w j-1 >= 1/2`,

`D <= Q exp(3/(2 rho)) <= M/2`.

Every interval of length `M` contains at least `floor(M/D)>=M/(2D)` multiples of `D`. Consequently

`sum_{b in I}(X_w(b)-1)_+ >= M/(4Q) exp(-3/(2 rho))`.  (2)

The ratio of (1) to (2) is at most

`(32 Q C_P rho/(7e)) exp(-1/(4 rho)) <= 1`.

This proves H2 for every `M` whenever `rho<=rho0`.

### Remaining weights: a uniform periodic approximation

Now suppose `rho>=rho0`. Let `k=|P|`,

`a0=rho0 log 2`, `T0=ceil(2/a0)`, and `delta0=Q^(-T0)`.

Select an integer `T>=T0` so large that

`eta_T=sum_{p in P} 1/(p^T(p-1)) <= delta0/2`.

Define

`Y_w(m)=sum_{p in P} w_p min(v_p(m),T)`,

which has period `R=product_{p in P} p^T` and is bounded by `kT`.

There is a prime `p` with `w_p>=a0`. On multiples of `p^T0`, `Y_w>=2`, and hence

`(Y_w-1)_+-(Y_w-2)_+ = 1`.

The mean difference over a complete period is therefore at least `p^(-T0)>=delta0`, uniformly in the weights. The difference is nonnegative everywhere.

For either nonnegative periodic hinge, its sum over any interval of length `M` differs from `M` times its period mean by at most `R kT`. Moreover, using the 1-Lipschitz property of a hinge,

`sum_{m<=M} [(X_w(m)-2)_+-(Y_w(m)-2)_+] <= sum_{m<=M}(X_w(m)-Y_w(m)) <= M eta_T`.

The interval hinge is at least the corresponding truncated hinge. Combining the estimates gives

`Delta_2(M,I,w) <= -delta0 M/2 + 2 R kT`.

Thus one explicit, very large threshold is

`M0(P)=ceil(4 R kT/delta0)`.

Together with the small-weight regime this proves the theorem.

## Consequences and their limits

1. For a fixed finite prime support, all H2 counterexamples, if any, have bounded `M`. Their weights and interval shifts may still vary.
2. Therefore repeating a finite valuation pattern by making the interval longer, keeping its prime support fixed, cannot amplify a positive H2 defect. This remains true if one changes the weights at each scale.
3. This does not show that a defect cannot be transferred to a different, growing prime support. It does not establish or refute an equivalence between H2 and the asymptotic conjecture.
4. The constants depend on the actual primes, not only on their number. This theorem provides no uniform bound when the supporting primes escape to infinity.

## A separate obstruction to affine prime cloning

Suppose two original positions `i` and `i+p` are divisible by a prime `p`, and some third position is not. Attempt to embed all positions by an affine map `j -> a+D j` and replace the original prime by a new prime `q`, preserving divisibility versus nondivisibility on these positions.

From `q | a+D i` and `q | a+D(i+p)` one gets `q | Dp`. If `q!=p`, then `q|D`; the first congruence then implies that `q` divides every embedded position, contradicting the required nonmultiple. Hence such an affine copy must retain `q=p`.

CRT does not remove this obstruction: it can choose residues, but cannot change the divisibility of differences between positions. A more elaborate amplification would need a substantially different placement or a different source construction.

## Extension: every fixed threshold c>1 works on a fixed finite support

The eventual fixed-support theorem holds with `2` replaced by any fixed `c>1`. In the small-weight argument choose `1<a<c` and `a/c<beta<1`. Set `t=beta/rho` and

`C_{P,c}=product_p (1-1/p)/(1-p^(beta-1))`.

The prefix hinge is at most `M C_{P,c} rho/(e beta) exp(-beta c/rho)`. A power `p^ceil(a/w_p)` of a prime attaining `rho` supplies an interval hinge at least `(a-1) M/(2Q) exp(-a/rho)`, once `Q exp(-(c-a)/rho)<=1/2` and the prefix hinge can be nonzero. Their ratio tends to zero because `beta c>a`. For the remaining weights use `T0=ceil(c/(rho0 log 2))` and the positive periodic mean gap `delta0=(c-1)Q^(-T0)`. The rest of the proof is unchanged.

In particular, when all source integers use a fixed finite prime set `P`, the corresponding restricted covering function has upper bound `(1+o(1))n`: apply the fixed-support `H_(1+epsilon)` for `M>=M0(P,epsilon)` and round at most `|P|` fractional coordinates. Since `M>=n+1`, the length restriction holds eventually. This conclusion concerns fixed actual primes, not a bound only on the number of primes.

## Uniform obstruction to logarithmic prime cloning

Here the primes themselves are allowed to grow, unlike in the first theorem. Fix an integer `M>=2` and a finite set `P` of primes at most `M`. For an integer `r`, choose distinct primes

`p^r <= q_p <= 2p^r` for every `p in P`,

and use the new interval length `N=M^r`. Such choices exist for all sufficiently large `r` by Bertrand's postulate; the prescribed intervals become disjoint. The theorem below is conditional on any such choices, so no asymptotic prime-distribution estimate is needed in its proof.

**Theorem.** For all sufficiently large `r`, H2 holds at length `N` for every interval and every weight vector in `[0,1]` supported on the cloned primes `q_p`. The threshold for `r` is uniform in the weight vector and in the choices of the cloned primes.

**Proof.** Relabel the weights by their original primes. The valuation profile of any integer `u<=N` determines a `P`-smooth integer

`d=product_p p^(v_{q_p}(u)) <= M`,

because the corresponding cloned divisor is at least `d^r`. Thus only finitely many profiles occur, independently of `r`.

If no such profile has weight greater than two, the prefix hinge vanishes. Otherwise set `rho=max_p w_p/log p`, choose a maximizing prime `p` with `w=w_p>0`, and let

`j=floor(2/w)`, `D=p^j`.

Since `j>=2` and `w>2/(j+1)`,

`j w-1 > (j-1)/(j+1) >= 1/3`,

while `j w<=2`. Every heavy profile `d` satisfies

`log d >= X_w(d)/rho > 2/rho >= log D`.

Consequently `D<d<=M`. Let `d0` be the least heavy profile. All these are ordinary integers, so

`D/d0 <= (M-1)/M`.

For any fixed profile `d`, the number of prefix integers with that profile is at most `(M/d)^r`. There are at most `M` profiles, each with hinge at most `log_2 M`, giving

`sum_{u<=N}(X_w(u)-2)_+ <= M log_2(M) (M/d0)^r`.

The chosen carrier divisor satisfies

`q_p^j <= 2^j D^r <= M D^r`,

and every multiple of it has interval hinge greater than `1/3`. If `(M/D)^r>=2M`, every interval of length `N` therefore has hinge sum at least

`(1/(6M)) (M/D)^r`.

The ratio of the prefix upper bound to this interval lower bound is at most

`6 M^2 log_2(M) ((M-1)/M)^r`.

It is at most one for all

`r >= log(6 M^2 log_2(M))/log(M/(M-1))`.

This condition also implies `(M/D)^r>=2M`, since `D<=M-1`. Together with the distinctness requirement for the cloned primes, it gives an explicit sufficient threshold. This proves the theorem uniformly in all weights. **QED**

This theorem does not rule out amplification by increasing the number of prime coordinates, or by a different relationship among the new prime sizes and the interval length. It does rule out the direct monomial dilation `p -> approximately p^r`, `M -> M^r`, even if weights and CRT phases are reoptimized after each dilation.
