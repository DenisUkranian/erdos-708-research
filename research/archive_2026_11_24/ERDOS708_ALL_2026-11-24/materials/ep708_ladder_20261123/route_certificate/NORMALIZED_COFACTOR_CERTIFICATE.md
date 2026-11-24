# A normalized cofactor certificate: an actual n-scale advance and the remaining collision lemma

Date: 2026-11-23. Status: the finite normalization and congestion inequalities in Sections 1–4 are proved. The closing collision estimate is not proved. This is not a claim to solve Erdős Problem 708, exactly or asymptotically.

The purpose of the normalization is to keep every actual source, including every inactive cofactor, while preventing the analytic error from being multiplied by an uncontrolled total bank length. It gives a common target payment; it does not establish that this payment fits the target capacity.

## 1. Finite setup, with no optimality assumption

Let `I` be any positive interval of `M` consecutive integers. Let `0 <= w_p <= 1` and

\[
X(a)=\sum_p w_pv_p(a),\qquad H_X(b)=(X(b)-1)_+.
\]

Fix `delta > 0`. Let `A` be any set of distinct integers at most `M` satisfying `X(a)>2+delta`, and put `n=|A|`. The construction below does not require that `A` is the full tail or that the weights are optimal.

For each `a`, let `a^+` be its full part supported on positive-price primes. Choose one positive-price prime occurrence `p(a)` in `a`; taking the numerically largest such prime makes the rule canonical. Set

\[
d(a)=a^+/p(a).
\]

The inactive factor `a/a^+` is *not* discarded from the set of sources or from any multiplicity. It merely does not enter the carrier label. For a distinct carrier `d`, define

\[
\begin{aligned}
A_d&=\{a\in A:d(a)=d\},&m_d&=|A_d|,\\
s_d&=\sum_{a\in A_d}(X(a)-2),&N_d&=\lfloor M/d\rfloor,\\
\beta_d&=s_d/N_d,&h_d&=X(d)-1.
\end{aligned}                                                    \tag{1}
\]

All source copies in `A_d` are counted in `m_d` and `s_d`, including copies with the same active part and different inactive cofactors. Put

\[
S_2=\sum_{a\in A}(X(a)-2)=\sum_d s_d,
\qquad
G_0(b)=\sum_d\beta_d\mathbf1_{d\mid b}.                         \tag{2}
\]

## 2. Normalization theorem

For every carrier,

\[
\boxed{\quad 0<\beta_d\le h_d,\qquad h_d>\delta,\qquad N_d\ge2.\quad} \tag{3}
\]

Moreover, uniformly in the shift of `I`,

\[
\boxed{\quad
S_2\le\sum_{b\in I}G_0(b)\le\frac32S_2,
\qquad
\sum_d\beta_d\frac Md\le\frac32S_2.
\quad}                                                         \tag{4}
\]

Thus, on the genuine full-tail optimum, where the previously proved conditional first-moment theorem gives `S_2=O_delta(n)`, the weighted sum of the *entire* bank lengths is `O_delta(n)`. There is no assumption on the number or size of inactive prime factors, the number of carriers, or the size of an active prime set.

### Proof

Complete additivity and `w_{p(a)}<=1` give

\[
X(d)=X(a)-w_{p(a)}>1+\delta,
\qquad X(a)-2\le X(d)-1=h_d.
\]

Every source in `A_d` is an actual multiple of `d` at most `M`, so distinctness gives `m_d<=N_d`. Consequently `s_d<=m_dh_d<=N_dh_d`, proving the first two assertions of (3). Also `d<=a/p(a)<=M/2`, so `N_d>=2`.

Every interval of `M` consecutive integers contains either `N_d` or `N_d+1` multiples of `d`. Summing the constant payments `beta_d` over the banks proves

\[
S_2\le\sum_I G_0\le S_2+\sum_d\beta_d
\le S_2+\tfrac12\sum_d s_d=\tfrac32S_2.
\]

Finally, `M/d<N_d+1`, and the same calculation proves the last inequality in (4). This proves the theorem.

The bound does not use the invalid assertion `m_d<=pi(M/d)`. Its replacement is the exact, always valid bound `m_d<=floor(M/d)` together with the demand normalization in (1).

### Fractional root choice and arbitrary cold blocks

The choice of the largest active prime is not required. More generally, for each source take any nonempty family of eligible divisors

\[
\mathcal D(a)\subseteq
\{d:d\mid a,\ d\le M/2,\ X(a/d)\le1\}.
\]

The family is always nonempty: deleting one prime occurrence gives an eligible full cofactor. It may include all such cold-complement divisors, with their actual inactive factors retained. It may also include the active-part carriers above, since their omitted inactive factor has zero load.

Choose fractional assignments `theta_{a,d}>=0` with `sum_{d in D(a)} theta_{a,d}=1`, and replace (1) by

\[
m_d=\sum_{a:d\in\mathcal D(a)}\theta_{a,d},\qquad
s_d=\sum_{a:d\in\mathcal D(a)}\theta_{a,d}(X(a)-2),
\qquad \beta_d=s_d/N_d.                                      \tag{4a}
\]

For a fixed `d`, each actual multiple `a` contributes at most one to `m_d`, so `m_d<=N_d`. Also `X(a)-2<=X(d)-1` for every eligible pair. Consequently (3)–(4), the congestion inequality below, and the diffuse comparison all hold **uniformly over these fractional choices**. This permits an adaptive stopping tree to choose the carrier, rather than freezing one arbitrary prime deletion.

## 3. One common capacity and the exact congestion inequality

Define

\[
E_X=\sum_{b\in I}(G_0(b)-H_X(b))_+,
\qquad P_X=\sum_{b\in I}\min\{G_0(b),H_X(b)\}.
\]

Every individual atom fits at every target where it is present, because `beta_d<=h_d<=H_X(b)`. Several atoms can nevertheless overfill the same target. The clipping is applied only after all atoms have been added.

Since `P_X=sum_I G_0-E_X`, (4) gives

\[
\boxed{\quad
\sum_{a\in A}(X(a)-2-\delta)-\sum_{b\in I}H_X(b)
\le E_X-\delta n.
\quad}                                                         \tag{5}
\]

In particular, a uniform bound `E_X <= (delta-epsilon)n+o(n)` on genuine positive full-tail optimizers would give a contradiction. This is a sufficient collision estimate, not a proved property of the normalized certificate.

For bookkeeping, let

\[
D_I=\sum_I G_0-S_2\ge0,\qquad
R_I=\sum_I(H_X-G_0)_+\ge0.
\]

Then the exact identity is

\[
J_{2+\delta}(w)=E_X-R_I-D_I-\delta n                         \tag{6}
\]

when `A` is the full strict tail. Any attempt using the stronger estimate `E_X<=delta n` must be labeled as such; dropping `R_I` and `D_I` can lose genuine usable target capacity. Merely rewriting (6) is not progress on the collision estimate.

### Exact finite optimization over the carrier choices

The minimum *actual* congestion is a linear program. Write `s_a=X(a)-2`, use variables `y_{a,d}>=0` satisfying `sum_{d in D(a)} y_{a,d}=s_a`, and let `e_b>=0`. Minimize `sum_b e_b` subject to

\[
\sum_{a,d:\,d\mid b}\frac{y_{a,d}}{N_d}-e_b\le H_X(b)
\qquad(b\in I).                                            \tag{6a}
\]

Its exact dual, by finite LP duality, is

\[
\boxed{\quad
\mathcal E_X=
\max_{0\le t_b\le1}
\left[
\sum_{a\in A}s_a
 \min_{d\in\mathcal D(a)}
       \frac{\sum_{b\in I,\,d\mid b}t_b}{N_d}
-\sum_{b\in I}H_X(b)t_b
\right].\quad}                                             \tag{6b}
\]

Thus an explicit alternative closing lemma is the uniform arithmetic cut inequality obtained by bounding the bracket in (6b) by `(delta-epsilon)n` on the genuine positive-optimum class. The test functions `t_b` are fractional. Restricting them to indicator functions is an additional assertion: the minimum over source carrier choices does not commute with layer integration in the needed direction. Formula (6b) is an exact optimization target, not its solution.

## 4. An entirely arithmetic, but generally too weak, pair-energy bound

Since each individual atom is at most `H_X(b)`,

\[
(G_0(b)-H_X(b))_+
\le\sum_{d<e}\min(\beta_d,\beta_e)\mathbf1_{\operatorname{lcm}(d,e)\mid b}.
\]

For proof, sort the nonzero atom values at the target decreasingly. The excess above a capacity at least their maximum is at most the sum of all remaining values; these values already occur among the pairwise minima with the largest atom. Therefore

\[
\boxed{\quad
E_X\le\sum_{d<e}\min(\beta_d,\beta_e)
\left(\left\lfloor\frac{M}{\operatorname{lcm}(d,e)}\right\rfloor+1\right).
\quad}                                                         \tag{7}
\]

All prime powers and all actual least common multiples occur in this formula. The `+1` terms cannot be summed away using a prime-row balance alone. Even the main pair energy need not be `o(n)` under a full-tail assumption without genuine optimality.

If `X(gcd(d,e))<=1`, the two atoms *jointly* fit at a common target: indeed

\[
H_X(b)\ge h_d+h_e\ge\beta_d+\beta_e.
\]

This does not extend to arbitrarily many roots by summing pair statements. For example, with unit prices on three primes, the roots `pq,pr,qr` have cold pairwise gcds and each has hinge one, while the target `pqr` has hinge two. A higher-order collision estimate is still necessary.

## 5. Executed analytic link: joint diffuse transfer after normalization

The analytic route in the adjacent `route_core` work supplies a one-sided diffuse concentration function `psi_B(eta)->0`. For a load `V` with all its prices at most `eta`, reciprocal mean at most `B`, and any quotient interval `J` of length `N`, it bounds the relevant lower-deviation average by `psi_B(eta) N`, uniformly in the shift. Refer to that route for its exact truncation, finite-error conditions, and proof; the following deduction is conditional only on that explicitly stated analytic input.

Write `X=W+V`. For each normalized carrier set

\[
\mu_d=\sum_{p\le M/d}\frac{v_p^{\rm price}}{p-1},
\qquad \nu_d=V(d)+\mu_d.
\]

Here `v_p^{price}` denotes the coefficient of `v_p` in `V`, not the valuation of a number. At a target with `G_0(b)>0`, put

\[
\bar\nu(b)=\frac{\sum_{d\mid b}\beta_d\nu_d}{G_0(b)}.
\]

The original source payments `s_d` and `beta_d` are retained. In particular, the construction does not assume that the diffuse demand on the source is small and does not collapse source multiplicities. Define

\[
E_{\rm model}=\sum_{b\in I}
\left(G_0(b)-(W(b)+\bar\nu(b)-1)_+\right)_+,
\]

with the summand set to zero where `G_0=0`.

The pointwise clipping comparison gives

\[
E_X\le E_{\rm model}
+\delta^{-1}\sum_d\beta_d
 \sum_{\substack{b\in I\\d\mid b}}(\nu_d-V(b))_+.
\]

Indeed, `H_X>delta` on the support of every atom. A positive change of the target hinge by `Delta` changes `min(G_0,H)` by at most `(G_0/delta)Delta`. Jensen's inequality for the positive part then separates the weighted mean `bar nu` into the displayed sum over the *same* banks. Complete additivity gives `V(b)=V(d)+V(b/d)`, including when `d` and `b/d` share prime factors. Applying the one-sided quotient estimate and (4) yields

\[
\boxed{\quad E_X\le E_{\rm model}
+\frac{3\,\psi_B(\eta)}{2\delta}S_2
=E_{\rm model}+O_\delta(\psi_B(\eta)n).\quad}                 \tag{8}
\]

This is a joint target reduction. It does not pay each carrier from an independent target budget. The resulting offset is the root-dependent `V(d)+mu_d`, not a common constant. Replacing those offsets by one mean would require another proof and is not justified by (8).

### The weaker terminal functional: amplify the cap, not the target capacity

The final theorem need not force every uniformly spread source payment to be covered at the same target. It may retain additional unused target capacity. Fix a constant `Lambda>=1` and define, with `G=G_0`,

\[
\mathcal C_{\Lambda}(H)=
\sum_{b:G(b)>0}\min\{\Lambda G(b),H(b)\}
+\sum_{b:G(b)=0}H_X(b).                                   \tag{8a}
\]

The actual hinge is kept on targets outside the carrier banks. The multiplier increases the *accounting cap* only; the pointwise payment is always at most the one target hinge. Put `H_model=(W+bar nu-1)_+` on the bank union. The exact same clipping proof, now using `G>delta/Lambda` whenever a positive change is possible, proves

\[
\mathcal C_{\Lambda}(H_X)
\ge\mathcal C_{\Lambda}(H_{\rm model})
-\frac{\Lambda\psi_B(\eta)}\delta\sum_d\beta_dM/d.           \tag{8b}
\]

In particular, on the positive-optimum class,

\[
\boxed{\quad
J_{2+\delta}(X)
\le S_2-\delta n-\mathcal C_{\Lambda}(H_{\rm model})
+\frac{3\Lambda\psi_B(\eta)}{2\delta}S_2.
\quad}                                                       \tag{8c}
\]

This supplies the preferred, weaker terminal target:

> For each fixed `delta>0`, find a fixed `Lambda_delta` and admissible fractional cold-complement assignments for which
> \[
> \mathcal C_{\Lambda_\delta}(H_{\rm model})
> \ge S_2-\tfrac12\delta n                                  \tag{8d}
> \]
> uniformly over the remaining positive global optimizers, for all sufficiently small diffuse cutoffs `eta`.

`Lambda_delta` must be selected before making `eta` small; an uncontrolled dependence on `1/eta` would reintroduce a parameter circularity. Once (8d) is proved, take `eta` so small that the last term in (8c) is at most `delta n/4`. Then `J<0`, a contradiction. The core route's `JOINT_CLIPPED_DIFFUSE_TRANSFER.md` contains the independently written proof of (8a)–(8c).

## 6. A checked arithmetic counterexample to the full-tail-only collision shortcut

The assertion `E_X<=delta n` for every full tail, without genuine optimum conditions, is false even with no diffuse weights.

Take

\[
M=100,\quad I=[1,100],\quad \delta=1/10,\quad
w_p=1\ (p\in\{2,3,5,7,11,13\}),
\]

and all other prices zero. Use the largest active prime in the normalization. The full tail consists of the 37 integers with `X>=3`. Its source surplus above two is `S_2=63`, while the target hinge sum is `121`. The nonzero coefficients are

| d | beta_d | d | beta_d |
|---:|---:|---:|---:|
| 4 | 6/25 | 6 | 5/16 |
| 8 | 5/6 | 9 | 4/11 |
| 10 | 1/5 | 12 | 3/4 |
| 14 | 1/7 | 15 | 1/6 |
| 16 | 3/2 | 18 | 4/5 |
| 20 | 2/5 | 24 | 3/4 |
| 27 | 2/3 | 32 | 8/3 |

The only congested targets and their excesses are

\[
32:\frac{31}{25},\quad
48:\frac{463}{1200},\quad
64:\frac6{25},\quad
72:\frac{653}{13200},\quad
96:\frac{821}{400}.
\]

Consequently

\[
E_X=\frac{2095}{528}>\frac{37}{10}=\delta n.
\]

Here `J_{2.1}=-617/10<0`; the weights are not a global maximizer, since zero weights give surplus zero. Thus the example refutes only a full-tail-only proof of the stronger collision estimate. It does not refute the desired estimate on a positive global maximizer, nor the asymptotic conjecture. The exact unused reserve in (6) is substantial in this example.

### A linear asymptotic obstruction, even when active-prime choice has no freedom

The core route supplied the following sharper example. Set `w_2=1`, all other prices zero, `I=[1,M]`, and `0<delta<1`. The full tail is `A={a<=M:v_2(a)>=3}`, with `n~M/8`. With active-part prime deletion there is only one allowed prime at each source. The carrier `d=2^j`, `j>=2`, has

\[
\beta_{2^j}\longrightarrow (j-1)/4.
\]

At a target of valuation `t`, the limiting payment and capacity are

\[
G_0=\frac{t(t-1)}8,\qquad H_X=(t-1)_+.
\]

Consequently

\[
\frac{E_X}{M}\longrightarrow
\sum_{t\ge9}\frac{(t-1)(t-8)}{8\,2^{t+1}}
=\frac5{1024},\qquad
\boxed{\ E_X/n\longrightarrow 5/128.\ }                     \tag{9}
\]

The passage to the limit is dominated: `beta_{2^j}<=j-1`, so the target payments are bounded by a constant times `t^2`, whose geometric valuation tail is uniformly summable. The series follows by putting `t=k+8` and using `sum k/2^k=2`, `sum k^2/2^k=6`.

Thus the stronger congestion bound fails by a *linear* amount for every `delta<5/128`, under full-tail structure and all of the elementary length gates. There is no diffuse load in this example. It does not refute a theorem using genuine global optimality: here

\[
J_{2+\delta}/M\longrightarrow-\frac14-\frac\delta8<0.
\]

Nor does it rule out the more flexible choice of all actual cold-complement divisors in (4a). It rules out asserting that the active-prime uniform-bank construction automatically removes congestion once the diffuse term has been controlled.

In the limiting one-prime profile, `H/G=8/t<=4` for every `t>=2`. Thus `Lambda=4` captures the whole positive target hinge in (8a). Amplified clipping removes this particular false obstruction without changing any actual target capacity. This is a check of the weaker formulation, not a proof of its terminal bound in general.

## 7. The corrected finite closing ladder

The parameter order must be fixed before allowing `n`, `M`, the source support, and the shift to vary.

1. Fix `delta>0` and take a genuine positive global maximizer of `J_{2+delta}`. Use its whole strict tail and the already proved row equalities, source-tail moment bound, support restriction, and quadratic gate. An unbounded positive sequence has `M=o(n^2)` by the audited near-quadratic exclusion.
2. Choose a small error allowance `epsilon<delta/10`, then a source-load cutoff `L=L(delta,epsilon)` using the full-tail exponential bound. Deleting the sources above `L` costs at most `epsilon n` in original weighted demand. Every subsequent deletion must retain its contribution to the budget explicitly.
3. Construct the normalized coefficients (4a) from the actual source copies, permitting all cold-complement divisors if useful. Their weighted total bank length is already `O_delta(n)`. This is proved and does not require a gap in the actual prime factors.
4. **First missing arithmetic lemma:** choose a fixed amplification `Lambda_delta` and prove (8d) for some admissible fractional cold-complement assignments, uniformly for all sufficiently small `eta`. The model retains the offsets `V(d)+mu_d`; do not replace them by one constant and do not transfer original row equalities to this nonadditive auxiliary model. The actual-congestion cut formulation (6b) is a stronger alternative route. The proof of (8d) must handle all overlaps jointly, including cycles of arbitrary length, and must use genuine global optimality where full-tail structure is insufficient.
5. After `Lambda_delta` is fixed, choose `eta` so small that the last term in (8c), together with any explicitly charged source deletion, is below the negative margin reserved in (8d). Equations (4), (8b), and (8c) make this choice uniform in `M`, the shift, all source copies, and all prime powers. This analytic transfer is proved; the arithmetic assertion (8d) is not.
6. A prospective stopping-tree proof of Step 5 may classify by actual carrier product size, merge source groups with a hot common divisor using the independently proved hot-root cluster inequality, and use signed corrections for the remaining cold intersections. **What must be certified at each merge or correction** is (i) one pointwise target capacity; (ii) no negative boundary term with uncharged total size; and (iii) preservation of the `O_delta(n)` weighted bank norm. A stopping tree with unbounded signed norm is not a valid reduction.
7. Once Step 5 gives a strict `J_{2+delta}<0` contradiction uniformly on every unbounded positive sequence, bounded-size exceptional tails contribute only a constant `C_delta`. Therefore `L_raw(A,I)<=(2+delta)|A|+C_delta`. The existing Wang fractional-to-integer theorem then gives the requested asymptotic as `delta` tends to zero. No new rounding theorem or exact `2n` claim is needed.

This is a ladder to the full result, not a ladder of increasingly large fixed exterior-prime classes. Its open part is arithmetic collision control after a rigorous n-scale analytic transfer. The counterexample in Section 6 specifies why full-tail structure alone cannot prove the stronger collision statement.

