# A joint clipped-flow transfer for arbitrary diffuse prices

## Status

This is a new proved reduction for every positive global optimizer of `J_c`, with `c=2+delta`. It combines the normalized bank coefficients from the certificate route with the arithmetic-bank concentration proved in `DIFFUSE_BANK_TRANSFER.md`.

It transfers the **single jointly clipped target flow**, retaining all inactive cofactors and all overlaps. It does not prove the remaining congestion bound. In particular, the transformed target load is not a raw price vector and the exact row balances must not be transferred to it.

## 1. Original optimum and normalized banks

Let

\[
X(t)=\sum_p w_pv_p(t),\qquad 0\le w_p\le1,
\]

be a true positive global maximum of `J_c`, `c=2+delta`. Let `A={a<=M:X(a)>c}`, `n=|A|`, and

\[
H_X(b)=(X(b)-1)_+,
\qquad
S_2=\sum_{a\in A}(X(a)-2).
\]

The following broad root family is allowed. For each source choose any proper divisor `d` with

\[
d\mid a,\qquad a/d\ge2,\qquad X(a/d)\le1.
\tag{R}
\]

One always-available choice is to remove an active prime occurrence and every inactive factor: let

\[
a^+=\prod_{p:w_p>0}p^{v_p(a)},
\qquad d(a)=a^+/p(a).
\]

The largest active prime may be used in this example. More generally, every source may distribute its entire payment fractionally among all the divisors allowed by (R): choose `theta_{a,d}>=0` with `sum_d theta_{a,d}=1`, and assign the fraction `theta_{a,d}(X(a)-2)` to `d`. In that case, interpret every root sum below with these fractions. All inequalities and all error constants are uniform over this choice. Raw additivity and the cold-complement condition give

\[
X(d)=X(a)-X(a/d)>1+\delta.
\tag{1}
\]

For each distinct root `d`, put

\[
s_d=\sum_{a\in A:d(a)=d}(X(a)-2),
\quad N_d=\lfloor M/d\rfloor,
\quad \beta_d=s_d/N_d.
\]

Because `a/d>=2` and `a<=M`, one has `N_d>=2`. Define

\[
G(b)=\sum_{d\mid b}\beta_d,
\qquad
\mathcal N=\sum_d\beta_d M/d.
\]

Every target interval contains at least `N_d` multiples of `d`, and

\[
\sum_{b\in I}G(b)\ge S_2,
\qquad
\mathcal N\le\tfrac32 S_2.
\tag{2}
\]

The second estimate follows from `(M/d)/floor(M/d)<=3/2` when the floor is at least two. At a true global optimizer, the proved full-tail moment estimate gives `S_2=O_delta(n)`.

The actual target congestion is

\[
\mathcal E_X=\sum_{b\in I}(G(b)-H_X(b))_+.
\]

Since the total bank mass is at least `S_2`,

\[
J_c(X)\le\mathcal E_X-\delta n.
\tag{3}
\]

This is the exact target of the certificate route.

## 2. Freeze the diffuse cofactor means, retaining the diffuse root masses

Take any subset of the original coordinates whose prices are at most `eta`, and write

\[
V(t)=\sum_{p\in P_\eta}w_pv_p(t),\qquad W=X-V.
\]

For each root, let

\[
\mu_d=\sum_{p\le M/d,\ p\in P_\eta}\frac{w_p}{p-1},
\qquad \nu_d=V(d)+\mu_d.
\]

All `mu_d` are bounded by the global optimum mean bound `B_delta`. At a target where `G(b)>0`, define the bank-weighted baseline

\[
\bar\nu(b)=\frac{\sum_{d\mid b}\beta_d\nu_d}{G(b)}.
\tag{4}
\]

Set `bar nu(b)=V(b)` when `G(b)=0`, since such positions have no effect on the clipped flow. Define the model target hinge and its congestion by

\[
\widetilde H(b)=(W(b)+\bar\nu(b)-1)_+,
\qquad
\widetilde{\mathcal E}=\sum_{b\in I}(G(b)-\widetilde H(b))_+.
\]

There is no claim that `W+bar nu` is additive, or that it is optimal. These are explicitly defined auxiliary target values.

## 3. The proved joint transfer inequality

Let `psi_B(eta)` be the uniform lower-deficit function from the bank concentration lemma. Then

\[
\boxed{
\mathcal E_X
\le\widetilde{\mathcal E}
+\frac{\psi_{B_\delta}(\eta)}{\delta}\mathcal N
\le\widetilde{\mathcal E}
+\frac{3\psi_{B_\delta}(\eta)}{2\delta}S_2.
}
\tag{5}
\]

Consequently,

\[
\boxed{
J_{2+\delta}(X)
\le\widetilde{\mathcal E}-\delta n
+O_\delta(\psi_{B_\delta}(\eta)n).
}
\tag{6}
\]

The final error tends to zero relative to `n` as `eta -> 0`, uniformly in every other parameter, including the density `n/M`, the shift, the number of primes, and the repeated/inactive cofactor structure.

### Proof

Whenever `G(b)>0`, at least one root divides `b`. Nonnegative raw prices and (1) imply

\[
H_X(b)\ge X(d)-1>\delta.
\tag{7}
\]

At a position with `G<=H_X`, the actual clipped flow already equals `G`, so replacing the hinge cannot increase its value. At a position with `G>H_X`, (7) gives `G>delta`; by the 1-Lipschitz property of the hinge,

\[
\begin{aligned}
\bigl[\min\{G,\widetilde H\}-\min\{G,H_X\}\bigr]_+
&\le(\bar\nu-V(b))_+\\
&\le\frac{G(b)}{\delta}(\bar\nu-V(b))_+\\
&\le\frac1\delta\sum_{d\mid b}\beta_d(\nu_d-V(b))_+.
\end{aligned}
\tag{8}
\]

The last step is convexity of the positive part, applied to the weighted average in (4). It is precisely the step that keeps overlaps in a single clipped target budget. No individual coefficient `beta_d` is assumed bounded below.

Raw complete additivity gives

\[
\nu_d-V(b)
=\mu_d-V(b/d)
\quad\text{when }d\mid b.
\]

The quotient positions form a real interval of length `M/d`. The bank lemma therefore gives

\[
\sum_{b\in I:d\mid b}(\nu_d-V(b))_+
\le\psi_{B_\delta}(\eta)M/d.
\tag{9}
\]

Sum (8), apply (9), and use

\[
(G-H)_+=G-\min\{G,H\}.
\]

This proves the first inequality in (5). The second follows from (2), and (6) follows from (3).

## 4. Amplified clipping retains unused target capacity

The terminal goal should not insist that every source's uniformly spread bank mass be paid at the same target. The original dual inequality needs a lower bound on the one total target hinge. Unused capacity must therefore remain available.

Fix any constant `Lambda>=1`. Define the accounting functional

\[
\mathcal C_\Lambda(H)
=\sum_{b:G(b)>0}\min\{\Lambda G(b),H(b)\}
+\sum_{b:G(b)=0}H_X(b).
\tag{10}
\]

In (10), `H` is either the actual hinge `H_X` or the model hinge `tilde H`; the actual hinge is retained unchanged outside the union of the banks. In particular,

\[
\mathcal C_\Lambda(H_X)\le\sum_{b\in I}H_X(b).
\]

The factor `Lambda` increases the accounting cap at a target, **not its actual capacity**. Every target hinge still enters at most once.

The joint transfer proof gives the uniform extension

\[
\boxed{
\mathcal C_\Lambda(H_X)
\ge\mathcal C_\Lambda(\widetilde H)
-\frac{\Lambda\psi_{B_\delta}(\eta)}{\delta}\mathcal N.
}
\tag{11}
\]

Indeed, a positive increase of the clipped functional after replacing the actual hinge by the model hinge is possible only when

\[
\Lambda G>H_X>\delta.
\]

Thus `G>delta/Lambda`, and the same proof as (8) bounds that increase by

\[
\frac\Lambda\delta\sum_{d\mid b}\beta_d(\nu_d-V(b))_+.
\]

Apply (9) and sum. The positions with `G=0` have identical contributions on both sides of (11).

Consequently the direct completion inequality is

\[
\boxed{
J_{2+\delta}(X)
\le S_2-\delta n-\mathcal C_\Lambda(\widetilde H)
+\frac{\Lambda\psi_{B_\delta}(\eta)}\delta\mathcal N.
}
\tag{12}
\]

For example, if one proves for some fixed `Lambda=Lambda(delta)` that

\[
\mathcal C_\Lambda(\widetilde H)\ge S_2-\tfrac12\delta n,
\tag{13}
\]

then choose `eta` **after** `Lambda` so that the final error in (12) is less than `delta n/4`. Equation (12) contradicts positive `J_c`. The required estimate is (13) uniformly over the remaining joint-optimum class, not a bound on each bank separately.

### A verified warning against the stronger uniform-routing requirement

For arbitrary weights, the earlier congestion target `E_X<=delta n` is false even with one active prime. Take `w_2=1`, all other prices zero, `0<delta<1`, and `I=[1,M]`. As `M->infinity`,

\[
A=\{a:v_2(a)\ge3\},\qquad n\sim M/8,
\]

and the root `2^j`, `j>=2`, has `beta_{2^j}->(j-1)/4`. At a target with `v_2(b)=t`,

\[
G(b)\longrightarrow t(t-1)/8,\qquad H_X(b)=t-1
\quad(t\ge2).
\]

Therefore

\[
\frac{\mathcal E_X}M\longrightarrow
\sum_{t\ge9}\frac{(t-1)(t-8)}{8\,2^{t+1}}
=\frac5{1024},
\qquad
\frac{\mathcal E_X}n\longrightarrow\frac5{128}.
\tag{14}
\]

This is not a positive global optimizer: its original `J_c` is negative. It therefore does not refute (13) or the desired theorem. It does show why an unrestricted claim about the unamplified routing congestion would be too strong. In the limiting one-prime model, `Lambda=4` already captures the entire target hinge, because `4G>=H_X` at every positive-hinge state. Amplified accounting removes this artificial chain overload while spending each target's capacity only once.

## 5. What this does and does not remove

The theorem controls all diffuse **cofactor fluctuations** jointly, at the actual source scale `n`, even in the sparse branch. It does not replace the original full diffuse load by a scalar constant.

The root terms `V(d)` remain in (4). They can carry a substantial proportion of the original diffuse source demand. The model baseline is their bank-weighted average plus the corresponding cofactor means. Therefore (5) cannot be combined with a finite-substantial-profile theorem by silently deleting those root terms.

The preferred next sufficient inequality is now the **single amplified model-capacity bound** (13), which retains unused target capacity and is weaker than forcing the uniform bank routing itself to have small congestion. Proving that bound remains an arithmetic problem about simultaneous source-root demands and target overlap. The theorem does not make it follow from balance alone.

## 6. Larger cold-complement allowance: the audited tau version

The entire argument is valid with any fixed `tau<c-1`. Put

\[
\gamma=c-1-\tau>0,\qquad
s_a=X(a)-(1+\tau),\qquad
S_\tau=\sum_{a\in A}s_a.
\]

Allow fractional root choices satisfying `d|a`, `a/d>=2`, and `X(a/d)<=tau`. Then

\[
X(d)>c-\tau=1+\gamma,
\qquad
\mathcal N\le\tfrac32S_\tau.
\]

Use `s_a` in the definitions of `s_d,beta_d,G`; all diffuse baselines and amplified accounting definitions remain the same. The exact original objective is

\[
J_c(X)=S_\tau-\gamma n-H(X).
\]

Thus the generalized joint transfer is

\[
\boxed{
J_c(X)
\le S_\tau-\gamma n-\mathcal C_\Lambda(\widetilde H)
+\frac{\Lambda\psi_{B_c}(\eta)}{\gamma}\mathcal N.
}
\tag{15}
\]

The proof changes only the hot-root lower bound from `delta` to `gamma`.

For the specific useful choice

\[
c=2+\delta,\qquad \tau=1+\delta/2,\qquad\gamma=\delta/2,
\]

this reads

\[
\boxed{
J_{2+\delta}(X)
\le S_\tau-\tfrac12\delta n-\mathcal C_\Lambda(\widetilde H)
+\frac{2\Lambda\psi_{B_\delta}(\eta)}\delta\mathcal N,
\qquad \mathcal N\le\tfrac32S_\tau.
}
\tag{16}
\]

The requirement `a/d>=2` is material for the factor `3/2`. If a proposed deletion leaves the complement equal to one, use a proper admissible complement (a prime of weight at most one always works here). Otherwise replace the normalization constant by the correct one; do not silently retain `3/2` for unit-length banks.
