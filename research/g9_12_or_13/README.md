# Nine-source bounds: \(12\le g(9)\le13\) (conditional upper bound)

Recovered from the 24 November 2026 archive ERDOS_708_g9_bounds_12_to_13_verified.zip. Its original verifier was independently replayed in the current audit on 25 November 2026 and completed successfully. The upper bound depends on \(g(8)\le11\) and its upstream dependencies in the separate repository packages. The exact value of \(g(9)\) remains open in this project. No peer review or formal Lean proof is asserted.

## Lower witness (unconditional)

Take
\[
 A=\{841,899,961,1073,1147,1189,1247,1271,1333\},\quad
 M=1333,\quad N=155833862424258021,\quad I=[N-666,N+666].
\]
Demand at \(29,31,37,41,43\) is \((6,6,2,2,2)\); the center supplies \((2,2,1,1,1)\). Each noncentral position contains at most one active prime species since any product of two distinct active primes is >666 and divides \(N\); moreover the 29- and 31-valuations there are at most one since their squares divide \(N\) and exceed 666. A cover using the center needs at least \(1+4+4+1+1+1=12\) positions; without it at least 15. The offsets \(0,29,58,87,116,31,62,93,124,37,41,43\) give an attaining twelve-point cover. Thus \(g(9)\ge12\).

## Upper proof and finite verification

1. If any source has a prime factor \(p\ge13\), cover the other eight in at most 11 positions by the upstream theorem, take a fresh multiple of \(a/p\) (at least \(p\) such positions exist), and repair at most one p-unit from a remaining unused position. The full interval supplies the required product because \(\prod A\mid M!\mid\prod I\). So any obstruction to 13 positions is 11-smooth.
2. If a source has a factorization \(a=uv\), \(u\le\lfloor M/12\rfloor\), \(v\le\lfloor M/13\rfloor\) (in either order), cover the other eight, then append fresh multiples of u and v. Every source of an obstruction is therefore "hard", lacking such a factorization.
3. For 11-smooth \(M\ge1573=121\cdot13\), multiplying prime factors until first reaching 12 produces \(12\le d\le121\), with \(d\le M/13\) and \(M/d\le M/12\). The maximum source itself is easy. For \(M\le13\), take the entire interval. Thus the finite domain is \(14\le M\le1572\).
4. Exhaustively generate distinct hard-source selections of size nine including \(M\), represented by summed five-coordinate exponent vectors. Only 65 maxima survive and all are at most 250. The original generation returned 658,192 distinct vectors.
5. Keep coordinatewise maximal vectors at each \(M\); there are 89,666. Covering a dominating vector covers every dominated vector.
6. Exact cumulative-GCD sufficient certificate: factors \(h_j\le M\) with \(\gcd(h_j,\prod_{i<j}h_i)\le\lfloor M/j\rfloor\) can be supplied in at most j positions. If no fresh multiple of \(h_j\) exists, the old product already supplies it; a fresh multiple of the gcd completes the cumulative required product. Enumerate reachable exponent states for \(j=1,\ldots,13\). This covered 84,496 maximal demands; 5,170 remain, all with \(M\le56\).
7. Exact CRT verification: for each active prime \(p\), enumerate every residue \(x\bmod p^h\) with \(h=\min(D_p,\lfloor\log_p M\rfloor)\), using valuations capped at \(h\). If the cap is the latter, the full interval still supplies the prefix's total demand at those levels; if the cap is \(D_p\), a single higher exponent need not supply more. Independent prime phases combine by CRT. For each phase combination verify an at-most-13-position cover of the capped valuations. Greedy cover success is sufficient; if needed the finite exact branching check uses bounded counts of equal valuation vectors. Independent suffix prime demands may be covered and their selected positions unioned because their coordinates are disjoint. All 5,170 residual demands passed.

Therefore the original verified computation proves the conditional upper bound 13. The new replay checked the exact original archive's regenerated demand/frontier/miss files against its saved data, rather than merely relying on its old logs. See REPLAY_2026-11-25.md for counts and archive hashes.

The complete original archive, including large intermediate tables, logs, and the bundled prior g(8) proof, is preserved byte-for-byte in [the recovered archives](../recovered_2026_11_25/README.md). Restore and independently rerun it from the repository root with:

~~~sh
python3 research/recovered_2026_11_25/restore_archives.py --output recovered_2026_11_25 --verify-g9
~~~

The separate g(8) dependency is also available at [research/g8_exact](../g8_exact/). See [follow-up inventory](../g9_followup/README.md) for later reductions toward 12. No proof of exact equality is claimed.

[Original verification source files](../recovered_2026_11_25/source/ERDOS_708_g9_bounds_12_to_13_verified/G9_12_OR_13_PROOF/src/) are browseable here. The full replay requires the restored original data tables, as documented above.
