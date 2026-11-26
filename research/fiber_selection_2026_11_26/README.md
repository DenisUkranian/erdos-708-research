# Progression selection and the inverse problem for Erdős 708

This round pursues routes 7 and 11. Let A contain n distinct integers in [2,M] with maximum M. On an arbitrary interval I of M positive integers, τ is the minimum cardinality for product divisibility and H the stronger prime-power level minimum. The unrestricted asymptotic coefficient two remains open. The [earlier uniform bound](../uniform_three_2026_11_26/README.md) remains (3+o(1))n.

### Where the earlier selection criterion fails

The exact optimum of |V|+Σ_{a∈A outside V}ω(a) can exceed every constant times n even when V ranges over **all** unions of progressions of multiples. For a source consisting of an entire residue class 1 mod q, coprime to q, with q asymptotic to log n, the same sources have H≤n+O(n log log n/log n) at every shift. Failure already occurs at density 1/5. A finite example has n=46, M=3001, exact union budget 137, and an actual level-cover witness using 68 positions on the specified nonzero shift. [Proof, finite optimization and arithmetic family](OBSTRUCTION.md).

### What can be transferred to every shift

A source may use an arbitrary collection of valuation-profile classes on a chosen prime set S. Suppose A occupies at least half its canonical container V, n≥M/(log M)^K, and |S|≤exp((log M)^a) for fixed K>0, 0<a<1. Then H≤2n+o(n). If A fills V the bound improves to n+o(n). With fewer governing primes, |S|=o(log M/log log M), a container of size v=M^(β+o(1)) gives H≤[1+log(1/β)+o(1)]v for every fixed β>1/2 through β=1. [Transfer proof and treatment of large primes](TRANSFER.md).

### What any fixed-gap violation would force

If H>(2+δ)n and t=n/M is between 1/(log M)^K and 1/2, prime intersections have source density >33t/32. One endpoint already has an elevated marginal density. A single union V of these intersections, with actual overlaps counted once, has density >65t/64 and contains ≫_δ n[log(2+D)/D]² distinct source rows, D=1+log(M/n). All generators can avoid any preassigned set of exp((log M)^a) primes for fixed 0<a<1. At fixed positive density, the omitted set can have polynomial size, the union contains a positive fraction of the source, and each selected quotient fiber contains polynomially many rows. Even after the exclusions, one lifted prime supports a union with that same density multiplier and ≫_δ t floor(M/p) log(2+D)/D source rows. A matching of disjoint prime pairs alone covers o(n) rows, so the shared prime bases matter. A version at n=M^(0.8+o(1)) allows prime-power intersections and has the same density factors. A weaker fixed factor covers every fixed exponent above exp(−1/2). [Inverse theorem, second moment and union selection](PAIR_INCREMENT.md).

A density increase on a union need not put half its canonical positions into the source. A density increase on an individual fiber does not establish that the quotient retains the covering gap. The transfer result controls predicates on a prescribed number of bases. The inverse theorem does not bound the total number of bases needed by its selected union from above. These are the missing implications for a global argument.

### Finite verification

Run `python verify.py` with NumPy and SciPy. The script cross-checks minimum cut against exhaustive search on 255 small source sets, certifies the 46-row obstruction, constructs and checks its actual target positions, checks a fitted profile against arithmetic counts, and constructs a union of pair progressions by conditional expectations. The finite density test uses a deliberately structured source to check the selection step and makes no assumption that it violates the conjecture. [Recorded output](REPLAY.txt).
