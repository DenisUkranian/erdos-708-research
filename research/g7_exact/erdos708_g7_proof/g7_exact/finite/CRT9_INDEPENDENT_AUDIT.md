# Independent audit of the 7-smooth CRT cover checker

`g7_exact/smooth/crt9.cpp` is sound on its actual input range. A fresh execution of all 318 input demands returned ALL_PASS, with 99,864 recursion nodes and 6,049 exact multicover calls. The largest interval length is 60 and the largest demanded exponent is 18.

For each prime p, h=min(D_p,floor(log_p M)) and the rows enumerate every residue modulo p^h with valuations capped at h. Every actual interval has one of these rows coordinatewise below its true valuations. Capping can make coverage harder, never easier. Enumerating the Cartesian product of the prime-power residue rows therefore includes every actual shift; Chinese remaindering is not used to omit any combination.

The prefix cover and suffix cover concern disjoint prime-coordinate sets. Their target points may overlap without double-counting a prime demand. The suffix bound either uses the worst independently verified single-prime cardinality or combines whole prime demands whose product is at most M into a single required modulus. Both are universal for the suffix residue choices.

The greedy prefix routine reports a successful cardinality only after actually satisfying every processed prime demand with distinct positions. The exact routine groups identical position vectors with their true multiplicities and enumerates every allowable number selected from each group. Its coordinatewise maximum and total-supply pruning are necessary conditions, so cannot reject a feasible branch. Memoized remaining demands have at most 18 units and occupy disjoint seven-bit fields; the pattern index is at most 60, so its field does not overlap the cardinality field. Thus the packed memo key is injective on this input range.

This audit checks the CRT fallback computation. Completeness of the reduction to these 318 demands is supplied by the separate smooth-source finite checker.
