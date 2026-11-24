# Erdős 708: g(7)=9

This bundle contains the computer-assisted proof, exact certificates and
portable verifiers for the seven-source Erdős–Surányi covering problem.
The cardinality convention is "at most". The new theorem is **g(7)=9**.

## Read the argument

Start with `erdos708_g7_exact.pdf` or `g7_exact/PROOF.md`. The branch
appendices give the complete reductions, classification arguments and
finite verification records. `g7_exact/LOWER9_SIMPLE.md` supplies a short
explicit witness with maximum 551 and a matching nine-point cover.

## Reproduce every computational component

From this extracted directory, run:

```sh
python3 g7_exact/verify_all.py
```

The only software requirements are Python 3 and a C++17 compiler available
as `g++`. No external Python package, numerical solver, network access or
prebuilt binary is required. Keep assertions enabled: do not use Python
`-O` or compile with `-DNDEBUG`.

The master verifier checks the six-source prior bound, the lower witness,
the complete smooth-source case, and all one-, two- and three-large-prime
branches. It compiles the finite verifiers in temporary directories,
regenerates their complete source universes, and checks explicit integer
certificates. The reference full replay returned PASS in approximately
85 seconds. Where residue checks are needed, all residue classes are covered;
no bounded sample of interval shifts substitutes for a universal proof.

The three-large-prime envelope is the slowest component. Logs may be quiet
for about 45 seconds while that finite calculation runs.

## Mathematical dependencies and scope

The proof uses the classical bounds for one, two and three sources, and
Theorem 1.6 of John Tripodo, *Sharp finite cases of the Erdős–Surányi
interval-product problem: g(4)=5 and g(5)=6*, 19 November 2026, manuscript
version 1.8: https://hexagonmath.org/pdf/2611.00694v1 .

The included proof of `g(6)<=8` depends only on the stated `g(5)<=6`
input and is verified separately. The external paper reports a Lean
formalization; it was not rebuilt here. The new seven-source result is
a computer-assisted proof, not a new Lean formalization.

This bundle establishes the seven-source value. It does not assert exact
values for eight or nine sources or the general asymptotic conjecture.

## Integrity and provenance

`SHA256SUMS` records the distributed static sources, proof documents and
certificate data. Runtime logs and result records may be refreshed by
the verifiers and are omitted from that integrity list. Independent
audit notes are included beside the relevant components. Source-search
heuristics and exploratory failed attempts are not required to replay
the proof and have been omitted.
