ERDOS PROBLEM 708 — RESEARCH ATTEMPT, 22 NOVEMBER 2026

STATUS: THE GENERAL PROBLEM IS NOT SOLVED.
Neither g(n)<=2n nor g(n)<=(2+o(1))n is proved in this archive.
H2 is explicitly an unproved hypothesis. Matching samples do not prove it.

Read erdos708_research_note.pdf for definitions, complete proofs, assumptions,
attribution, exact auxiliary obstructions, and the remaining gap. The .tex
file is its editable source. Compile twice with pdflatex in a normal LaTeX
installation with the packages named in the preamble.

EXACT CHECKS — Python 3.10+ standard library only:
  python checks/verify_exact_certificates.py
  python checks/verify_hub_obstruction.py
  python checks/verify_hub_family.py
  python checks/verify_omega2_certificate.py

These check, respectively:
  * the largest-prime-only Hall obstruction, 171 sources / 170 neighbors;
    and the false sparse numerical comparison, using exact fractions;
  * the forced hub budget 13, actual product-cover optimum 4, and stronger
    prime-power-count optimum 6, using exhaustive integer dynamic programming;
  * explicit instances in the unbounded hub-charging-gap family, each with
    a valid cover of size 2n-2;
  * the CRT obstruction to the full matching rule with Omega>=2, with
    10,353 sources / 10,352 neighbors. This does NOT refute Omega>=3 or 708.
The associated JSON certificates are stored beside their verifiers.
The optional CRT builder is build_omega2_certificate.py; final-certificate
verification does not rely on the search procedure.

CONSTRUCTION STRESS CHECK:
  python checks/test_peeling.py
This seeded test passed 11,438 rough-only and 6,000 mixed instances in the
research run. The general extension theorem rests on its proof, not these
samples. Some mixed tests have no rough sources and only test the base cover.

MATCHING EXPERIMENTS — requires numpy and scipy (versions in requirements.txt):
  python checks/proper_divisor_matching.py --start 8 --stop 250 --trials 100 --output results/matching_k3.json
  python checks/proper_divisor_matching.py --start 10 --stop 2000 --step 10 --trials 100 --output results/matching_large_k3.json
The two batches contain 44,300 executed checks, with possible overlap.
There is no exhaustive assertion over shifts, lengths, or source sets.
Every returned matching is independently checked for divisibility and
injectivity. Any reported failure exports an exact Hall obstruction.
The additional Omega>=2 sample in results/matching_full_k2.json found no
failure; the separate CRT certificate shows that stronger rule is false.

PROVENANCE AND SCOPE:
This is an AI-assisted exploratory record prepared for Denis Paliy. It does
not assert publication, formal verification, human peer review, or literature
priority. Source papers are cited in the report and are not bundled. No email,
external repository publication, or communication to source authors occurred.
No private correspondence is included. SHA256SUMS.json records file hashes.
