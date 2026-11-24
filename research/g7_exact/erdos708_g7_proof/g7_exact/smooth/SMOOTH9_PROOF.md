# Seven 7-smooth sources admit a nine-point product cover

## Theorem and dependencies

Assume the previously established bounds g(5)<=6 and g(6)<=8. Let A be
seven distinct integers at least 2, all of whose prime factors belong to
{2,3,5,7}. Put M=max(A). For every interval I of M consecutive positive
integers, a subset B of I with |B|<=9 satisfies product(A)|product(B).

This statement covers every M and every interval shift. It does not by
itself prove g(7)=9 for source sets containing other primes. The bound
g(5)<=6 is the external small-n theorem used in the accompanying work;
g(6)<=8 has a separate verified proof in that work.

The proof below consists of elementary reductions, an analytic infinite
tail, and a completely reproducible finite certificate. No common-factor
induction, divisor-closure assumption, or a/p filter is used.

## Elementary source reductions

Distinctness gives product(A)|M!, and the integer binomial coefficient
implies M! divides the product of every interval of M consecutive positive
integers. Thus the complete interval always covers the source product.

If M<=9, take the complete interval. If some source a satisfies 9a<=M,
cover the other six sources with at most eight points. There are at least
nine multiples of a in I, so a fresh one completes a nine-point cover.

If a source is a prime p, cover the other six in eight points. If the
full product is not already covered, the only deficit is one p-unit.
Since the complete interval has sufficient p-valuation, an unused point
divisible by p exists and repairs the deficit. Therefore it suffices to
consider composite sources a with 9a>M.

## The two-source packing reduction

For any distinct a,b in A, cover A minus {a,b} in at most six points using
g(5)<=6. If ab can be factored into three positive integers h7,h8,h9 with

    hj <= floor(M/j), j=7,8,9,

then choose unused multiples of h7,h8,h9 successively. At step j, at most
j-1 interval points have been used and at least j multiples are available.
The resulting cover has at most nine points. Factors equal to 1 can be
omitted.

Any explicit factorization satisfying these three capacities is sufficient;
the search need not solve the corresponding bin-packing problem exactly.

## Analytic closure for every M>=12555

Place the prime factors of ab, with multiplicity, in nonincreasing order
into three bins of capacities floor(M/7), floor(M/8), floor(M/9), accepting
any placement that respects its capacity. Suppose the first failed prime
is p. For M>=63, p<=7<=floor(M/9), so every bin is nonempty when failure
occurs. Its current product C_j satisfies

    C_j >= max(floor(M/(jp))+1,p), j=7,8,9.

Including the failed occurrence of p, the part of ab supported on primes
at least p must then be at least

    T_p(M) = p * product_{j=7,8,9} max(floor(M/(jp))+1,p).

For p=2,3,5 that source part is at most M^2. For p=7 it is at most M^2/2:
the smaller 7-power part divides both distinct source integers, so it is
at most M/2, while the larger is at most M.

The finite exact integer computation in verify_smooth9.py finds the last
failure of these sufficient inequalities, for 63<=M<=12600:

| p | Required inequality | Last failure |
|---|---|---|
| 2 | T_p(M)>M^2 | 1997 |
| 3 | T_p(M)>M^2 | 4508 |
| 5 | T_p(M)>M^2 | 12554 |
| 7 | 2T_p(M)>M^2 | 12284 |

For every M>=12601, no further computation is required:

    T_p(M) > M^3/(7*8*9*p^2) = M^3/(504*p^2).

This exceeds M^2 for p=2,3,5, and exceeds M^2/2 for p=7. Therefore every
pair ab packs successfully for every M>=12555, proving the theorem there.

## Finite reduction to a graph of pairs

For each 7-smooth M<12555, the independent verifier generates all composite
7-smooth a with M/9<a<M by trial division of the actual integers. It first
tests the pair a,M for a three-bin witness. A successful pair closes every
source set containing it and is discarded from consideration.

Among the remaining candidates, connect a,b precisely when the verifier
has not found a valid three-bin witness for ab. A possible counterexample
must select six vertices that form a clique: together with the mandatory
source M, all seven of its pairs must remain unclosed.

The verifier recursively enumerates all such six-vertex cliques without
any Pareto pruning. The actual enumeration contains 3,413,772 source sets,
at 94 different maxima. The largest maximum admitting any such clique is
567; consequently all larger smooth M below 12555 have already been closed
by successful pairs. There are 135,961 distinct resulting source-demand
vectors across these maxima.

## Universal certificates for each remaining demand vector

Write D_p=sum_{a in A}v_p(a). The finite verifier accepts one of the
following independently checked sufficient certificates.

### Separate prime covers

For a prime p, the sum of the k largest p-valuations in I is at least

    sum_{e>=1} min(k,floor(M/p^e)).

Indeed, there are at least floor(M/p^e) interval points with valuation
at least e. If counts k_p meet the four demands and sum k_p<=9, the union
of these separate prime covers gives a nine-point cover. Intersections
are harmless because the demands concern disjoint primes.

### Ordinary nine-bin packing

An explicit factorization into hj<=floor(M/j), j=1,...,9, gives a cover by
successive unused multiples. The verifier checks all capacities and the
resulting complete exponent vector using exact integers.

### Cumulative-GCD slots

A list h1,...,hl, l<=9, is sufficient if its product covers the demand,
each hj<=M, and

    gcd(h1*...*h_{j-1},hj) <= floor(M/j).

To prove this, suppose earlier selected points cover H=h1*...*h_{j-1}.
If there is a fresh multiple of hj, use it. Otherwise hj divides the
product of the selected points, so lcm(H,hj) does also. A fresh multiple
of gcd(H,hj) exists by the displayed size bound, and multiplying by it
supplies H*hj. This proves the assertion by induction.

The file slots9.txt supplies 36,247 explicit lists. The independent C++
verifier factors every entry, checks each cumulative GCD, and checks the
covered demand. A certificate may dominate a smaller source demand;
componentwise domination is checked directly.

### Exhaustive prime-power residue certificates

Only 318 demand vectors, all at M<=48 or M=60, require this final method.
For each active p, put h=min(D_p,floor(log_p M)) and q=p^h. Every residue
r modulo q determines the pointwise lower valuation row

    (min(v_p(r+1),h),...,min(v_p(r+M),h)).

Every actual interval has one of these rows as a lower bound at p. The
CRT checker branches over all combinations of these rows. It may stop
early when a cover of the already fixed prime demands, together with a
universal cover for the remaining disjoint prime demands, costs at most
nine points. Otherwise it uses exact bounded integer multicover on the
fully or partially assigned profiles. The exact solver groups identical
point profiles and enumerates how many points of each group are selected;
its success condition is that all demand coordinates have reached zero.

The complete replay verifies all 318 targets, visiting 99,864 branch nodes
and making 6,049 exact multicover calls. These are checks over all residue
classes, not a bounded sample of numerical shifts.

## Independent replay and result

Run:

    python verify_smooth9.py

The script requires Python 3 and a C++17 compiler. It compiles the two
standalone C++ verifiers with assertions enabled, verifies the analytic
tail, independently reconstructs the entire finite pair-graph reduction,
checks all slot witnesses, and replays every CRT target. It imports none
of the original Pareto or search code.

The recorded run returned PASS in 3.87 seconds including compilation:

| Finite verification method | Distinct demand vectors covered |
|---|---:|
| Separate prime covers | 57018 |
| Ordinary bins | 283 |
| Cumulative-GCD witnesses | 78041 |
| Domination by universally checked CRT targets | 619 |
| Total | 135961 |

The machine-readable result is verification_result.json. The CRT code and
its finite-state/memoization bounds were independently audited by a second
agent, which also replayed all 318 cases successfully.

Thus the entire seven-source 7-smooth case is proved, subject only to the
stated previously established bounds g(5)<=6 and g(6)<=8.
