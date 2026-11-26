
## Extension to density 39.60%

The proof extends to \(n/M\ge0.3960\), with the previous qualifications and uniformity. Apply the pure and mixed split-triples bounds and the affine source/target coupling in SPLIT-TRIPLES.md. For each box, fill the positive source breakpoints at the separately minimized \(D_0\), obtaining a dual solution and a support \(S(D_0)+s(D-D_0)\) with \(s=\sum_j y_j\tau_j/2\). The same \(D\) is used in the target allocation by replacing its coefficient one with \(1+s\) and subtracting \(sD_0\) from the fixed term. This keeps every bound rational, and the greedy allocation still applies.

On \([0.3960,0.3975]\) the odds lower bound is \(20980/32000\) and upper density is \(12720/32000\). The verifier certifies \(\Gamma\ge0.3444>0.208/0.604\) in 12,443,623 high-mean and 470,027 low-mean boxes with no exceptions. Section 2 then proves the exact \(2n\) bound after absorbing the uniform analytic and rounding errors. The 39.75% result covers the upper overlap. The separate CRT example does not challenge \(2n\); it only disproves a uniform \(n+o(n)\) strengthening in positive density.
