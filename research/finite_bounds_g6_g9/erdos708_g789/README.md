# Erdős 708: verified finite bounds, 24 November 2026

## Result and scope

In the **at-most-cardinality** convention, the arguments and finite certificates in this package give

| n | Verified lower bound | Verified upper bound | Exact value established here? |
|---|---:|---:|---|
| 6 | 8 | 8 | Yes, using the external theorem below |
| 7 | 9 | 10 | No |
| 8 | 11 | 12 | No |
| 9 | 12 | 14 | No |

The proof uses John Tripodo's published theorem `g(5) <= 6`, Theorem 1.6 in
*Sharp finite cases of the Erdős–Surányi interval-product problem: g(4)=5 and g(5)=6*,
19 November 2026, manuscript version 1.8:
https://hexagonmath.org/pdf/2611.00694v1 .
That paper reports Lean verification. This session did not rebuild its Lean development.
The assertions here should be read with that explicit external mathematical dependency.

The requested exact values of g(7), g(8), g(9) are **not** established by this package.
No claim of peer review, Lean formalization of these new bounds, or priority is made.
The lower bounds 9, 11, 12 were already present in the prior discussion; the supplied
smaller witnesses are alternative exact certificates, not improved numerical bounds.

## Definition

For n distinct integers A >= 2, put M=max(A). For any integer x >= 0, let
I={x+1,...,x+M}. The number tau(A,I) is the least size of a subset B of I for which
product(A) divides product(B). Then g(n) is the supremum of tau over all such A and x.
Each interval position may be selected only once.

## Why a finite check proves a universal bound

1. If g(n-1)<=r and a source a has a prime divisor p with at least r+1 interval
   multiples of a/p, cover the other n-1 sources in r positions, add a fresh multiple
   of a/p, and repair at most one remaining p-unit in one further position.
   The repair exists because product(A) divides M!, and M! divides the product of I.
2. A counterexample to g(n)<=r+2 therefore uses only primes <=r, has no source
   with at most two prime factors counted with multiplicity, and satisfies
   (r+1)*a > M*Pplus(a) for every a in A.
3. Descending prime-factor packing proves all sufficiently large M, with the
   exact thresholds 9360, 19170, 12320, 24206 for n=6,7,8,9 respectively.
4. The remaining smooth source sets are finite. Every accepted finite case has
   an exact inequality or an explicit factor-slot certificate valid for **every** x.
   No upper-bound proof enumerates a bounded list of interval shifts.

The proof note explains the independent-prime union bound, ordinary factor bins,
the cumulative-GCD slot criterion, and the rough-part product envelope used by
the verifier. There is no floating-point optimization in the independent verifier.

## Additional proved reduction

Using also the g(4)<=5 theorem from the same Tripodo paper, the independently
audited four-large-prime argument proves that a counterexample to g(7)<=9 has
at most three distinct active primes >=11, for every M. A corresponding reduction
for g(8)<=11 also leaves at most three active primes >=11. See
`proofs/CORE_REDUCTIONS.md` and `proofs/FOUR_LARGE_PRIMES_AUDIT.md` for complete proofs.
These do not settle the remaining cases with at most three large primes.

## Reproduce

Requires Python 3.8+ and a C++17 compiler, g++ or clang++. Run from any directory:

```sh
python3 verify_all.py
```

To run a subset of cases:

```sh
python3 verify_all.py --cases 6 7 8
```

The n=9 verification represents many source subsets and can take longer. The
checker closes complete branches with exact sufficient inequalities. The JSON
outputs distinguish represented subsets, directly checked demands, and pruned
families; a represented subset count is not a claim that each was visited separately.

Do not compile the C++ verifier with `-DNDEBUG`: its certificate validations use
assertions. `verify_all.py` compiles with assertions enabled.

The executable is created in a temporary directory. No network access is required.
The external g(5) theorem is a mathematical input, not downloaded by the checker.

## Contents

- `verify/`: independent proof-checking code and exact lower witnesses.
- `certificates/`: explicit cumulative-GCD factor sequences, in JSON and plain text.
- `results/`: captured verification outputs and search summaries.
- `proofs/`: mathematical details and partial reductions for the remaining gaps.
- `search/`: optional certificate-generation code. This is separate from the
  independent checker and is not required to verify the claimed bounds.

To regenerate the optional Pareto search, work inside `search/`, compile
`skyline.cpp` as `skyline.so` using `g++ -O3 -shared -fPIC`, and run
`python3 frontier.py N` and `python3 slot_solver.py N` for the desired N.
The search finds sufficient universal certificates; it does not estimate g(n)
from random intervals. Random lower-bound searches are not used in the proof.

## Attribution

The prime-unit deletion idea is recorded in the earlier research notes for Denis
Paliy; this package applies it to finite n. The cumulative-GCD slot criterion
appears as Theorem 6 in C. Bergström's November 2026 preprint,
https://doi.org/10.5281/zenodo.24366897 . The n=6 lower witness is Proposition 3
of that preprint. Its asserted analytic proof of g(6)<=8 is not used here.
The n=7,8,9 lower witnesses in this package were derived independently in this session.

Prepared with AI-assisted mathematical derivation and separate independent
code checks. A failed search for a larger lower bound is not an upper-bound proof.
