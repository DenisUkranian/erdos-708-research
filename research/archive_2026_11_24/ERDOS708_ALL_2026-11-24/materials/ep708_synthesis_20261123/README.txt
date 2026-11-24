ERDOS PROBLEM 708: SYNTHESIS AND FURTHER PARTIAL RESULTS
Research package prepared for Denis Paliy, 23 November 2026

STATUS
The unrestricted exact bound g(n)<=2n and the unrestricted asymptotic
bound g(n)<=(2+o(1))n are NOT established in this package. This is a
research working note with AI-assisted derivations and separate internal
mathematical audits. No external referee approval, formal verification,
or priority claim is made.

START HERE
erdos708_synthesis.pdf is the 27-page consolidated document. Its LaTeX
source is erdos708_synthesis.tex with included sections/ files. It contains
complete proofs of the principal new claims and a precise remaining target.
The earlier 14-page note and supporting proof notes are in prior_results/.
STATUS.json records individual scopes and external dependencies.
MANIFEST.json contains SHA-256 hashes for the distributed files.

PRINCIPAL COVERING RESULTS
1. Retained exact cofactor Hall criterion, valid for every interval shift.
   In particular, all source primes >= M^alpha, alpha>1/(2e), give exact
   2n for sufficiently large M (fixed alpha).
2. Dense smooth-source theorem: if every source prime is <=Y(M) and
   log Y(M)=o(sqrt(log M)), then tau(A,I)<=(2+o(1))n uniformly in the
   interval shift. One example is Y(M)=exp((log M)^a), fixed 0<a<1/2.
   The proof uses an approximate raw hinge inequality and explicit
   rounding of at most pi(Y) fractional coordinates.
3. Separated prime bands: for an absolute constant kappa0, if all sources
   have the form d*r, all primes of d are <=Y, and r is one prime >=Z
   with Z>=Y^kappa0, exact 2n holds. The small-prime support can grow.
   The constant kappa0 is not evaluated. For additional pure small-prime
   sources A_Q, the bound is 2|A_R|+sum_{a in A_Q}Omega(a).

OTHER RIGOROUS RESULTS
- The user-supplied 32 n^(5/2) argument is reconstructed fully. Its
  three-large-occurrence classification requires c^2 K>=1 and cannot
  simply be continued into the quadratic range.
- In a minimal counterexample, forced prime-deletion banks and two-prime
  removals impose total-demand constraints. In the remaining quadratic
  range the demand core has O(sqrt(n/log n)) primes, and each source has
  at most one prime occurrence outside it, necessarily its unique largest.
- H_(2+epsilon) holds on arbitrary growing supports if all individual raw
  weights are sufficiently small; one arbitrary exceptional weight is
  permitted with zero defect.
- With at most k exceptional weights above c_epsilon/(k+1), the raw hinge
  defect is at most 2^(k+1)(1+log_2 M)^(k+1). The resulting growing-core
  exclusion is about dual vectors, not generic per-instance integer
  rounding.

EXTERNAL INPUTS
Ziming Wang's public manuscript already proves M>=16n^2 => tau<=2n.
Its full written argument was checked in this session, including the
ambient-length extension. Quadratic order is not claimed as a new result.
The generic asymptotic-closure equivalence also uses Wang's uniform raw
fractional transfer theorem. Main source:
https://github.com/science-prince/erdos-708-interval-divisor-covers

Haoyu Chen's earlier explicit-bound work is a baseline and a source of
the raw hinge formulation:
https://github.com/chy4pro/erdos-708-explicit-upper-bounds

The sole external analytic tool for the new sieve arguments is the
fundamental lemma of the combinatorial sieve, with standard Mertens and
prime-counting estimates where specified. Primary references are in
the PDF bibliography. Third-party papers are linked, not redistributed.

REPRODUCIBLE CERTIFICATES (Python 3.10+, standard library only)
Run from the package root:

  python -I computation/exact2n_recognition.py --verify computation/recognition_examples.json
  python -I computation/necessary_core.py --verify computation/core_n100_M146969.json
  python -I computation/dense_core_family.py --verify computation/dense_core_family_certificate.json

The recognizer combines fixed-ambient deletion rules and base cases. Its
output CERTIFIED is an all-shift existence bound; it does not construct
the actual interval cover. UNKNOWN makes no impossibility claim.
Generator and verifier share exact arithmetic helpers, but verification
recomputes every witness from the source list and does not rerun the
recognizer's deletion heuristic. Wang's theorem is explicitly marked
when it is the external base case.

The necessary-core certificate excludes particular hypothetical
minimal-counterexample parameters only. The 16,384-source dense family
shows that specified source-only filters are insufficient; it is not a
counterexample to 708. The 171-versus-170 cofactor example refutes one
unrestricted matching strategy, not the product-cover conjecture.

BUILD
On a standard LaTeX installation, run twice from the package root:

  pdflatex -interaction=nonstopmode -halt-on-error erdos708_synthesis.tex

The report uses standard AMS, Latin Modern, geometry, hyperref, microtype,
fancyhdr, and booktabs packages. The distributed PDF was compiled twice,
checked for unresolved references and overflow, and all pages rendered
for visual inspection.

WHAT REMAINS
The exact general range is 2n<M<16n^2. A growing demand core can be much
larger than the exceptional dual block controlled by the present estimate.
On the reduced minimal-obstruction sequences, however, every source prime
is <10n, so row-count rounding costs only O(n/log n). The sharper remaining
target is a uniform coefficient-two fractional valuation bound on this
explicit structural class; that fractional bound is not established.
The dense-support sieve argument stops before polynomial prime scales,
and the separated-band theorem does not handle arbitrary adjacent scales
or multiple large occurrences. A uniform bounded additive defect for
H_(2+epsilon), for every epsilon>0 and every support/weight vector, would
settle the asymptotic question through the cited transfer theorem.

This package is a completed research checkpoint.
