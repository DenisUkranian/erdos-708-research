# Erdős 708: exact 2n from density 39.60%

The latest extension is in PROOF-3960.md; verify-3960.js replays its exact arithmetic. The 39.75% proof and earlier checks are dependencies. EVERY-DENSITY-LOWER-BOUND.md disproves a uniform n+o(n) bound at every fixed density below 100%, not 2n. Run verify-lower-bound.js for its endpoint and finite-example checks. The two BOOLEAN notes are independent of the arithmetic bounds.
The main theorem is eventual in M and uniform in the set and the shift. The appendix to PROOF.md extends the earlier 40% theorem down to 39.75%; verify-below-4000.js checks both bridging intervals. SPLIT-TRIPLES.md contains a separate refinement not needed for this theorem. The remainder of this README describes the 40% base proof.

# Erdős 708: density 2/5 research checkpoint

This packet contains a proof for sufficiently large M and density n/M at least 2/5, with a distinct-position cover of size at most 2n in every shift. It is not a resolution of unrestricted Erdős 708 and does not give an explicit effective cutoff for M.

Read PROOF.md first. Each JavaScript certificate uses only BigInt and has no dependencies. Run them separately with Node.js; runtime may be a few minutes. The ranges below overlap:

| Certificate | Density range used | Lower bound on Gamma |
|---|---|---|
| verify-4000.js | 0.4000–0.4035 | 0.3334 |
| verify-4035.js | 0.4035–0.4043 | 0.3236 |
| verify-4043.js | 0.4043–0.4060 | 0.3214 |
| verify-4046.js | alternative bridge, 0.4046–0.4060 | 0.3205 |
| verify-variance.js | 0.4060–0.5000 (density-independent check) | 0.3168 |

The main check was reproduced with 1,781,545 high-mean boxes and 160,589 low-mean boxes. The other checks are included for the overlap argument. All intermediate density thresholds are eventual in M.
