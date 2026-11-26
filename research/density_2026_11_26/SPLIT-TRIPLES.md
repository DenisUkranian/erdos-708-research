# Lower-prime pair and triple estimates in the #708 density proof

The [40% proof](PROOF.md) splits its chosen lower pool \(L\) into the nested prefix \(R=R_{16}\) and \(T=L\setminus R\). Write \(r,t\) for their weighted reciprocal masses and \(e,b-e\) for their variance charges. The 40% proof applies the same \(1-(r+t)/3\) loss to all pure pair contributions. A finer bound is available using the same divisibility moments.

## Pure contribution

Let \(P_{RR},P_{TT},P_{RT}\) be the transferred sums of pure pair hinges, with reciprocal-probability coefficients. For triples entirely within one part, charge each triangle minimum to the average of its three pair hinges. The two costs are at most \(r P_{RR}/3\) and \(t P_{TT}/3\). For a triple with two labels in \(R\) and one in \(T\), the minimum is at most its \(RR\) hinge and at most the average of its two \(RT\) hinges. Summation gives the two upper bounds \(tP_{RR}\) and \(rP_{RT}/2\). The other mixed triple type gives \(rP_{TT}\) and \(tP_{RT}/2\). Diagonal restrictions only reduce these upper bounds. The resulting pure lower estimate, before uniform \(o(1)\) transfer errors, is
\[
(1-r/3)P_{RR}+(1-t/3)P_{TT}+P_{RT}
-\min(tP_{RR},rP_{RT}/2)-\min(rP_{TT},tP_{RT}/2).
\]
Use any of the four linear choices whose pair coefficients are all nonnegative. This permits substituting the old lower bounds
\[
P_{RR}\ge r(r/2-e)_+,\qquad
P_{TT}\ge t(t/2-b+e)_+,\qquad
P_{RT}\ge(rt-te-r(b-e))_+.
\]
In the chosen domain \(r\le1,\ t\le1/2\), so the option that charges the first minimum to \(tP_{RR}\) always has a nonnegative coefficient. Use the option charging the second minimum to \(rP_{TT}\) only if \(1-t/3-r\ge0\). When both costs are charged to the cross hinge, its coefficient is \(1-(r+t)/2\ge1/4\). On boxes, use upper \(r,t\) when charging the losses and lower estimates of the pair hinges in the resulting nonnegative linear forms. Keep the older pure bound as an additional option.

## A mixed contribution for each upper band

When \(i<16\), split the lower prefix \(R_i\) into \(R_{16}\) and \(R_i\setminus R_{16}\) of masses \(u=r\) and \(v=r_i-r\). For fixed upper band \(i\), write \(H_U,H_V\) for its two sums of pair hinges with these lower parts. Mixed triples with two lower labels in the same part cost at most \(u H_U/2\) or \(v H_V/2\). A mixed triple with one lower label in each part costs at most the smaller of its two pair hinges, giving total charge at most \(\min(vH_U,uH_V)\). Thus retain the maximum of the two linear forms
\[
(1-u/2-v)H_U+(1-v/2)H_V,\qquad
(1-u/2)H_U+(1-v/2-u)H_V .
\]
All coefficients are nonnegative since \(r_i=u+v\le1\). For the first lower part, use \(H_U\ge q_i(u-e)_+-u B_{Q_i}\), which follows by taking the positive part of the old pair lower bound before subtracting the upper price charge. For the second, use \(H_V\ge q_i(v-b+e)_+-v B_{Q_i}\), since the second part has charge at most \(b-e\). Under either linear choice the total coefficient of \(B_{Q_i}\) equals \(r_i-r_i^2/2\le1/2\), so the same upper price cancellation applies. Keep the original mixed estimate as another option. On boxes \(v(\ell)=\min(1,(\ell-c_i)_+)-\min(1,(\ell-c_{16})_+)\) increases, then is flat, then decreases. Its minimum over a box occurs at an endpoint. Its maximum is at most \(c_{16}-c_i\) and at most \(r_{i,\mathrm{upper}}-r_{\mathrm{lower}}\).

The moduli in these estimates are the same lower-prime pairs and triples and upper-lower pairs and triples as in the 40% proof. This refinement needs no higher-moment transfer.

## A further source improvement available for a later certificate

The 40% verifier evaluates the multilevel source bonus at the separately minimized forbidden-pair charge \(D_0\), while its target greedy allocation may use a larger \(D\). The source bonus is
\[
S(D)=\min_{B\ge0}\left[B+\sum_j w_j(\tau_j P_0(D)-U_j-B)_+\right],
\]
with \(P_0(D)=P_0(D_0)+(D-D_0)/2\). This has the dual representation
\[
S(D)=\max_{0\le y_j\le w_j,\;\sum y_j\le1}
  \sum_j y_j(\tau_j P_0(D)-U_j).
\]
It follows directly by filling the largest positive breakpoints up to total weight one, or by the piecewise-linear minimization used in the old verifier. Choose an optimizer at \(D_0\) after taking safe box endpoints in the breakpoint and weight bounds. This gives an affine lower estimate with slope \(\frac12\sum y_j\tau_j\). Include this slope in the coefficient of \(D\) in the combined target greedy check and subtract the affine correction at \(D_0\) from its fixed term. The old bound is recovered whenever the chosen allocation already attains \(D_0\). This joint charge is an algebraic refinement. PROOF-3960.md and verify-3960.js use the joint charge.
