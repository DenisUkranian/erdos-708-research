ERDOS PROBLEM 708: CONTROLLED CORES AND JOINT DIVISOR CERTIFICATES
23 November 2026

STATUS
This is an AI-assisted research continuation prepared for Denis Paliy.
The unrestricted exact 2n bound and unrestricted asymptotic coefficient-two
bound remain unproved in this investigation. The new results are restricted
theorems and precise reductions, with separate internal mathematical audits.
No external peer review, formal verification, or priority is claimed.

START HERE
erdos708_continuation.pdf: the 34-page integrated report with all new proofs.
erdos708_continuation.tex and sections/: its editable LaTeX source.
STATUS.json: machine-readable scope and validation summary.
MANIFEST.json: sizes and SHA-256 hashes of archive deliverables.

PRINCIPAL NEW CONCLUSIONS
1. A diffuse core and arbitrarily many possible one-prime remainders can
   be charged to one shared target hinge. Arbitrary powers are retained.
2. One arbitrary substantial core weight causes no additive defect.
3. With k substantial core weights, the joint hinge defect is at most
   B(epsilon,k)(1+|R|), independently of ambient length M, with
   B<=D_epsilon^k. Capping the whole core improves the earlier
   A(epsilon,k)+B(epsilon,k)|R| estimate.
4. A direct matching construction gives integer cost (2+o(1))n for a
   designated core of at most c0*(log M)^2/log log M arbitrary primes,
   for some sufficiently small absolute c0>0, and at most one DISTINCT
   outside prime per source. No prime-size gap is required; powers are
   arbitrary. This includes every fixed bound (log M)^a with 0<a<2 and
   strengthens the earlier o(log log M) fractional-method consequence.
   An explicit elementary variant permits 10^(-6)*(log M/log log M)^2.
5. If all source primes are <=Y or >=M^alpha, with
   log Y=o(sqrt(log M)), the same integer bound holds for every fixed
   alpha>0, without any extra bound on large-prime multiplicity.
6. An explicit growing-parameter theorem permits
   Y=exp((log M)^(1/3)) and
   Z=exp(log M / exp((1/4)sqrt(log log M))).
7. Clipped raw means >=241/136+o(1) satisfy exact H2 at every shift.
8. The remaining general asymptotic goal is the uniform source-specific
   hinge defect o(n) on the minimal-obstruction core class. Integer
   rounding there already costs only o(n).

SCOPE CHECK, NOT AN ADDITIONAL INDEPENDENT COVERING ADVANCE
If source prime supports split into disjoint components, each using
at most k(M)=o(log M) primes, an eventual EXACT 2n bound already follows
from the external quadratic gate and an elementary Rankin count.
We retain this derivation to distinguish a dependent consequence from
the shared-core improvement. It is not counted as a new integer frontier.

MATHEMATICAL PROOF NOTES
analytic/DIFFUSE_CORE_SINGLE_REMAINDER.md
analytic/CONTROLLED_CORE_SINGLE_REMAINDER.md
analytic/GLUING_ARBITRARY_PURE_CORE.md
analytic/SHARED_CORE_POLYLOGARITHMIC.md
combinatorial/DISCOUNTED_ADAPTIVE_CERTIFICATE.md
combinatorial/UNIFORM_RAW_MOMENTS.md
computation/HEREDITARY_RAW_INTEGER_TRANSFER.md

AUDITS
The remaining Markdown notes in combinatorial/ and computation/ record
separate internal checks, including signed balances, interval shifts,
prime-power tails, growing parameters, and the integer transfer.
These are mathematical checks, not formal proof-assistant certificates.
No finite computational search is used to prove a universal claim here.

INHERITED PROOF DEPENDENCIES
inherited/erdos708_synthesis.pdf contains the preceding 27-page report.
inherited/analytic/ contains the full diffuse, conditional, and smooth
support derivations reused in the current proofs.
inherited/combinatorial/ contains the earlier prime-bank/core derivation
and relevant internal audits. External primary texts are cited by links;
third-party papers and repository source trees are not redistributed.
References inside older notes to ep708_synthesis_20261123/ map to the
inherited/ directory in this archive.

EXTERNAL INPUTS
The exact quadratic ambient gate M>=16n^2 is credited to Ziming Wang's
written working manuscript, Appendix A, not to this continuation.
The analytic inputs include the classical fundamental lemma of the
combinatorial sieve, Chebyshev's estimate, and Mertens' estimates.
See the bibliography in the report for primary links.

REPRODUCING THE PDF
On a standard TeX installation with amsmath, amsthm, lmodern, geometry,
mathtools, xcolor, hyperref, microtype and fancyhdr, run from this directory:

  pdflatex -interaction=nonstopmode -halt-on-error erdos708_continuation.tex
  pdflatex -interaction=nonstopmode -halt-on-error erdos708_continuation.tex

No numerical solver is needed for any proof in this continuation.

PRECISE LIMITATION
The possible demand core in an unrestricted minimal obstruction has size
O(sqrt(n/log n)), which is far larger than the new polylogarithmic source
class. The finite-difference estimate separately permits O(log log n)
substantial weights inside a larger diffuse core, but does not control
arbitrary weights on the full core. The separated-support
theorem still excludes a band of intermediate prime sizes. These conditions
must not be dropped when quoting the results.
