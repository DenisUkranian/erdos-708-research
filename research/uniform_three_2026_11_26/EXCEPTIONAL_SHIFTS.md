# A superpolynomial exceptional-set estimate for the simultaneous harmonic cut

Let P=lcm(1,...,M), choose x uniformly mod P and write e(x) for the maximum harmonic cut excess on I=x+[1,M] defined in the [harmonic reduction](../cofactor_flow_2026_11_26/HARMONIC_REDUCTION.md). For every fixed δ>0 and integer k≥0 there is c_{δ,k}>0 such that, for all sufficiently large M,

    Pr(e(x)>δ) ≤ exp(−c_{δ,k} log M (log log M)^k).

Consequently the same estimate, with a different constant, holds for the event that there exists A⊆[2,M], |A|≥ρM, with ordinary product-cover number τ(A,I)>(2+ε)|A|, for any fixed ρ,ε>0. A remains shift-adaptive. An individual shift has mass 1/P and need not be excluded by these estimates.

## Initial polynomial tail

Use the [full-period divisor kernel and variance lemma](../unrestricted_shifts_2026_11_26/README.md). With h=sum_{d≤M}1/d, its full-period mean at d is μ_d=1/(dh), its empirical value w_d=M^(-1)sum_{b∈I}K_d(b), and e(x)≤sum_d(μ_d−w_d)_+. In fact

    ||w_d−μ_d||_2 ≤ 1/(Mh) + C/sqrt(Md).

Condition on x mod d. The quotient start is uniform modulo P/d, the sample length J is within one of M/d, the conditional mean differs from μ_d by at most 1/(Mh), and the conditional variance is at most (J/M²)(P/φ(P))/h≪1/(Md). These are the same conductor-shell estimates as in the full-period mean proof.

The harmonic mass of d>Y is log(M/Y)/log M+O(1/log M). Minkowski gives L² norm O(sqrt(Y/M)) for sum_{d≤Y}|w_d−μ_d|. With Y=M^(1−δ/2), Chebyshev proves Pr(e>δ)≪_δ M^(−δ/2) for 0<δ<1, the case δ≥1 being immediate. This gives k=0.

## Resampling one prime

In the finite bipartite transport from μ_d to target slots of capacity 1/M join d to the slots where d divides x+i. The weighted Hall/max-flow min-cut formula says its unmatched mass is exactly e. Explicitly the deficiency is max_S of μ(S)−|N(S)|/M, equivalently max_T of μ({d:B_d⊆T})−|T|/M. Deleting r slots can reduce maximum flow by at most r/M. By CRT the variables X_p=x mod p^e_p, for e_p=floor(log_p M), are independent and uniform. Resampling X_p affects only the slots where x+i was or becomes divisible by p. Hence the change of e is at most 2(1/p+1/M). If that phase is held fixed modulo p^j, the two banks can differ only on slots divisible by p^j, giving the stronger bound 2(1/p^j+1/M).

## Bootstrap

Suppose the asserted bound holds at k. Fix 0<δ<1 and choose

    y=a log M (log log M)^k

with a>0 sufficiently small in terms of δ and k. At all p≤y fix arbitrary residues of the phases modulo the *smallest* power p^j≥y². These powers are at most y³ and divide P for M large. Each resulting cylinder has probability 1/B where log B≤3π(y)log y≤C y. By the induction hypothesis at δ/3, even conditional on the least favourable cylinder, Pr(e>δ/3)≤exp(Cy−c_{δ/3,k} log M(loglog M)^k)=o(1), taking a<c_{δ/3,k}/(2C). Since e≤1, every conditional mean is at most δ/2 for M sufficiently large.

The prime phases remain independent conditional on any such cylinder. In the bounded-differences inequality their sum of squared oscillations is

    ≪ π(y)(y^(−2)+1/M)^2 + sum_{y<p≤M}(1/p+1/M)^2
    ≪ 1/(y log y).

Here sum_{p>y}1/p²≪1/(y log y) follows by dyadic summation from the prime counting bound. McDiarmid's inequality gives Pr(e>δ | cylinder)≤exp(−c δ² y log y). The bound holds over all cylinders and log y≥(1+o(1))loglog M. This proves the step k→k+1. All constants are for fixed k and δ.

## Covering consequence

For any A and shift, the previous harmonic Hall bound gives a one-omission matching of all but m≤Me(x)+O(M/log M) rows. Let A' be the matched rows. Their stronger level cover costs at most 2|A'|. When |A|≤M/2 the [source-removal stability bound of redlydi, Section 2](https://github.com/redlydi/Erdos708-Research/blob/32f397f8fdc00d0e9c73242d8510c541267a30db/reports/erdos708-residue-certificates.md) and rounding give

    τ(A,I) ≤ 2|A'| + C m log(eM/m) + π(M).

Use zero for the m=0 term. For |A|≥M/2 the entire interval suffices. For fixed ρ,ε>0 choose δ sufficiently small that C(2δ)log(e/(2δ))<ρε/2. Then any failure with |A|≥ρM forces e(x)>δ for all large M. Apply the first theorem.

This also works conditional on any prescribed shift family with proportion at least exp(−O(log M(log log M)^j)) for fixed j: apply the bound at k=j+1 and divide by the family's probability. In particular one can prescribe the residues modulo every prime through C log M(log log M)^j, to all levels up to any fixed power of log M, before choosing the shift at random; use k large enough to dominate the logarithm of the reciprocal cylinder probability.

Background for the concentration step: [C. McDiarmid, On the method of bounded differences (1989)](https://doi.org/10.1017/CBO9781107359949.008).

## An explicit growing number of bootstrap steps

For fixed 0<δ<1 one can make the iterated gain explicit:

    Pr(e>δ) ≤ exp(−c_δ log M exp(c δ sqrt(log log M)))

with an absolute c>0 and M sufficiently large in terms of δ. Start with t₀=δ/2 and S₀=c₀δ log M, where c₀>0 is small enough for the polynomial tail to give Pr(e>t₀)≤exp(−S₀). Set J=floor(a δ sqrt(loglog M)), with a>0 an absolute sufficiently small constant; for each i through J put t_i=t₀+iδ/(2J) and S_i=2^i S₀. Inductively, in the same conditional-cylinder argument take y=S_i/(2C), where log B≤Cy. The conditional mean is at most t_i+exp(−S_i/2). Uniformly this last term is smaller than δ/(6J). The next tail has exponent at least c₁(δ/J)² y log y, with c₁ absolute by the squared-oscillation estimate. Since log y≥(1/2)loglog M uniformly for large M, choose a small enough so this exponent is at least 2S_i. The argument is valid through the final step since every y is at most O(log M exp(O(sqrt(loglog M)))) and each fixed prime power used for the cylinders divides P for such y. Finally S_J gives the stated bound. The estimates remain far from the scale exp(−log P) required to rule out a single exceptional residue.
