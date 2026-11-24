# Audit and scope correction for disjoint prime-support blocks

Date: 2026-11-23.

## Verdict

The proposed fractional/rounding proof is mathematically valid, including
the union of covers and all fixed-ambient quantifiers. However, its claimed
integer class with block size k(M)=o(log M) already has a stronger eventual
EXACT 2n bound from the inherited quadratic theorem plus an elementary
smooth-number count. It should not be presented as a newly uncovered
asymptotic source class.

This correction does not affect the new aggregate-cap hinge theorem or the
shared-core source class. In the shared-core class, different source pieces
demand the same core primes, so independent covers cannot be combined by
the disjoint-demand argument below.

## 1. The proposed union and rounding argument does pass

Partition the source-prime support into disjoint blocks Q_i of size at most
k, and require every source to lie ENTIRELY in one block. Let A_i be the
corresponding source subset, with n_i=|A_i|. Retain the original ambient M.

If n_i<=sqrt(M)/4, Wang's ambient quadratic theorem gives an exact cover of
size <=2n_i. For each other block, the sharp aggregate-core theorem with
R empty gives a raw LP cover of size <=(2+delta)n_i+B_{delta,k}, and vertex
rounding adds at most k. There are fewer than 4n/sqrt(M) such large blocks,
so the proposed total bound

    tau(A,I)<=(2+delta)n+4(B_{delta,k}+k)n/sqrt(M)

is correct.

The union of the block covers is valid even when their target positions
overlap. Each source prime belongs to just one block. At that prime, the
union contains the entire cover of its block, already supplying ALL source
demand at that prime. No demand at the same prime is separately charged by
another block. Its cardinality is at most the sum of the block cover sizes.

Since B_{delta,k}<=D_delta^k, k=o(log M) makes the displayed error o(n).
This is a valid proof, but the following stronger inherited argument
renders the large-block case unnecessary in that regime.

## 2. Uniform elementary count for any k-prime support

Let Q consist of at most k distinct primes, and let Psi_Q(M) count the
positive Q-smooth integers <=M. Rankin's bound with exponent 1/4 gives

    Psi_Q(M)<=M^(1/4) product_{p in Q}(1-p^(-1/4))^(-1).

Order the primes as p_i. The elementary estimate p_i>=i+1 yields

    sum_{p in Q}p^(-1/4)
      <=sum_{i=1}^k(i+1)^(-1/4)
      <=(4/3)k^(3/4).

Also, for 0<=z<=2^(-1/4),

    -log(1-z)<=z/(1-2^(-1/4)).

Consequently, with the explicit absolute constant

    C=4/[3(1-2^(-1/4))],

one has

    Psi_Q(M)<=M^(1/4) exp(C k^(3/4)).                       (1)

This is uniform in the actual primes and requires no prime-distribution
theorem. If Q is empty, the count is one and causes no difficulty.

## 3. Every block is already in Wang's exact regime

If k(M)=o(log M), (1) is M^(1/4+o(1)), uniformly for every block. Hence,
for all sufficiently large M,

    n_i<=Psi_{Q_i}(M)<sqrt(M)/4

for EVERY block i. Apply the ambient quadratic theorem separately to all
blocks and take the safe union just explained. The result is

    tau(A,I)<=2 sum_i n_i=2n

for every shift, not merely an asymptotic coefficient-two bound.

More quantitatively, the elementary sufficient condition

    C k^(3/4)<=(log M)/4-log 4

already ensures this exact conclusion. In particular, k=o((log M)^(4/3))
also suffices asymptotically for the same inherited exact argument. No
priority claim is attached to this elementary consequence.

## Reporting consequence

The aggregate-cap fractional inequality remains an independently useful
new proof step, especially when a substantial core is shared among source
pieces. For disjoint prime blocks, the integer consequence should be stated
as an inherited exact corollary of the quadratic gate, with (1) explaining
why that gate applies to every block. The valid but weaker fractional proof
does not establish a new uncovered range in this particular source class.
