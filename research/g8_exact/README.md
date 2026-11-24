# Computer-assisted proof package: g(8) = 11

**24 November 2026 · exact integer certificates · dependencies declared**

This package addresses the Erdős–Surányi function g(8) from Erdős Problem 708. The new argument proves the **lower bound g(8) >= 11 unconditionally** and provides a computer-assisted proof of **g(8) <= 11, conditional on g(7) <= 9, g(6) <= 8 and g(5) <= 6**. Those earlier inputs are separate results, and the g(5) result relies on an external manuscript.

**Independent replay in this repository preparation:** On 24 November 2026, the supplied `verify_all.py` was executed from scratch with Python 3 and a C++17 compiler. All checks passed: 1,691,461 reduced source sets (50 maxima, all <= 252); 57,515 demand vectors; 57,487 checked cumulative-GCD certificates; 28 exact CRT residual cases; and a lower witness with exact minimum 11. The replay itself is not independent peer review or a Lean formalization.

## Outline of the upper bound

1. Any 8-source instance with a source divisible by a prime >= 11, with Omega(a) <= 2, or with 11a <= M admits a cover of size <= 11 by repairing at most two valuation deficits after applying the 7-source upper bound.
2. For all M >= 11538, three 7-smooth sources can be packed into five multiplicative bins of capacities floor(M/j), j=7,...,11; the remaining five sources require at most six points by g(5) <= 6.
3. For M <= 11537, sound one-sided packing reductions leave 50 possible maxima M <= 252, 1,691,461 source sets and 57,515 prime-valuation demands. The reduction algorithm only discards an instance when it finds an explicit legal packing.
4. A cumulative-GCD extension lemma gives universal 11-position certificates for 57,487 demands, for every interval shift.
5. The remaining 28 demands with M <= 54 are handled by exhaustive CRT residue classes, combined with exact integer multicover. The archived checker reports `ALL_PASS rows=28`.

## Unconditional lower witness

Set
```
A = {1369,1517,1591,1739,1961,2173,2279,2491}
M = 2491
x = 246043396342067361
```
At active primes (37,41,43,47,53), the required exponents are (6,2,2,2,4). For b* = x+1246, the active valuation vector is (2,1,1,1,1). Every other interval position has at most one active prime and cannot provide a 37^2 or 53^2 factor. Consequently any cover uses at least 11 distinct positions. Offsets 25,27,62,80,99,133,136,1199,1203,1205,1246 give a cover of size 11.

## Reproduce

After the full proof package is uploaded, run:
```bash
cd research/g8_exact
python3 verify_all.py
```
Expected terminal line:
```text
ALL CHECKS PASS: upper g(8)<=11 conditional on g(7)<=9,g(6)<=8,g(5)<=6; lower g(8)>=11 unconditional
```

**Import status:** This README is uploaded first. The large source, certificate, and PDF files are being imported as a separate operation. Until they appear on GitHub, use the locally prepared archive.

See also: https://www.erdosproblems.com/708
