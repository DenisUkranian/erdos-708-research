# Interval divisor covers — Erdős Problem 708

**Author: Ziming Wang.** Public research artifact, version **1.0.0**, 21 October 2026.

[Repository](https://github.com/science-prince/erdos-708-interval-divisor-covers) · [Release and downloads](https://github.com/science-prince/erdos-708-interval-divisor-covers/releases/tag/v1.0.0) · [中文说明](README.zh-CN.md)

For a set $A$ of $n$ distinct integers at least two, put $M=\max A$. For every interval $I$ of exactly $M$ consecutive integers, let $\tau(A,I)$ be the smallest number of distinct elements whose product is divisible by $\prod_{a\in A}a$, and let $g(n)=\sup_{A,I}\tau(A,I)$. Cardinality bounds use the **at-most** convention.

The strongest unrestricted result in this artifact is

$$
g(n)\le\min\{10n,\lceil cn\rceil+\pi(\lceil cn\rceil)-1\},
\qquad c=\frac{56501}{6400}=8.82828125.
$$

Thus $g(n)\le8.82828125n+O(n/\log n)$. The numerical constant uses Haoyu Chen's **written** H883 atom-hinge theorem, credited in the paper. The artifact also proves equality of the raw fractional, capped fractional, and integer worst-case limsup coefficients, and fractional cost at most $2n$ when the **total source prime support** has size at most five. The latter gives integer cost at most $2n+4$.

The unrestricted exact $2n$ and uniform asymptotic coefficient-two questions remain open in this project. No original-problem counterexample, new Lean endpoint, external peer review, or worldwide priority is claimed.

## Papers

- [Main paper, English (PDF)](papers/main-paper/main.pdf): complete transference proofs, five-coordinate kernel and rational coefficients, quadratic range appendix, attribution and references. [LaTeX project](papers/main-paper/main.tex).
- [Companion paper, Chinese with English abstract (PDF)](papers/companion-paper/副论文-中文修复版.pdf): all four checkpoints, sixteen auxiliary result groups, twelve supplementary tools, all forty B00–B39 route records, explicit counterexamples and remaining gaps. [LaTeX source](papers/companion-paper/main.tex).
- [Result scope](docs/RESULTS.md), [all 333 research-document entries](docs/research-file-index.md), [publication and validation record](docs/PUBLICATION.md).

## Reproduction

The fast integrity and constant check uses only Python's standard library. The exhaustive certificate replay additionally uses NumPy. On the preparation computer, Python is the existing Anaconda environment:

~~~powershell
& 'D:\Anaconda3\envs\selfcontrol\python.exe' -X utf8 -B scripts/verify_release.py
& 'D:\Anaconda3\envs\selfcontrol\python.exe' -X utf8 -B scripts/verify_release.py --full
~~~

On other machines, use Python 3.10+ and the supplied requirements. The full replay checks **1,221,759 sorted grid corners**, covering **115,856,201 labelled corners**, with exact integer arithmetic and no optimizer. The continuous theorem additionally requires the analytic argument in the paper. See [reproduction details](docs/REPRODUCIBILITY.md) and [the recorded replay](verification/EXACT_REPLAY.json).

Both PDFs embed their font programs and explicit Unicode maps. The Chinese paper's 23 pages were checked by four independent text engines; all 36 paper pages were rendered and compared. [PDF checks](verification/PDF_QUALITY.json), [Unicode repair](verification/UNICODE_REPAIR.json), [regression check](verification/UNICODE_REGRESSION.json).

## Evidence and provenance

The evidence directory contains public transcriptions of mathematical notes and audits, with historical and candidate labels retained. Local workspace paths and internal session identifiers were normalized. [SOURCE_MAP.json](verification/SOURCE_MAP.json) records original-source and public-copy SHA-256 hashes. These are public transcriptions, not byte-identical frozen checkpoint archives. [MANIFEST.json](MANIFEST.json) binds the artifact files.

Checkpoints 1–3 remain valid historical derivations but have divergent growth rates below the subsequently verified pre-existing public linear bounds. Later supplements and restricted results do not manufacture a fifth checkpoint.

Downloaded third-party PDFs, complete third-party transcript mirrors, orchestration/recovery metadata and large search caches are excluded. Primary inputs are linked in [references](references/PRIMARY_SOURCES.md). The local preflight reports describe validation before publication; repository visibility and released assets are checked separately at publication.

This repository is publicly readable. Public availability does not add a blanket redistribution license; see [rights and attribution](NOTICE.md). AI assistance is disclosed in both manuscripts.

