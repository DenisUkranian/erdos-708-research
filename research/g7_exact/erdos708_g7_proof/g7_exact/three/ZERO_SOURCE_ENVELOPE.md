# One smooth source and six pair-core sources

This is a universally valid sufficient criterion, followed by finite integer checks. It applies to the three-large-prime residue of g(7)<=9 after support-three elimination.

Suppose one source a0 has no prime >=11, and each of three large primes has source support at least four. The six other sources must then all be products of two different large primes times a 7-smooth cofactor: twelve incidences are required, so no loop or singleton core is possible. Each pair core pq,pr,qr occurs exactly twice.

Put L1=floor(M/(pq)), L2=floor(M/(pr)), L3=floor(M/(qr)). Each pair's two cofactors are distinct integers between 1 and its L_i, and L_i<=8. Let c_* be the largest of the six actual cofactors, and prescribe in the core-bank cover a point z divisible by its full source. The remaining nontrivial-source cofactor product Q satisfies

    Q <= Q_max := product_i L_i*(L_i-1) / max_i L_i.

To justify the bound, the product of all but the largest of six positive numbers is nondecreasing in every coordinate. Each ordered cofactor pair is bounded coordinatewise by (L_i-1,L_i).

## Coprime merging

A cover of the large-prime product and an independently constructed cover of the entire small-prime product may be united even if the point sets intersect, because the two required products are coprime. If c_* is credited from a prescribed point z, a cover of the remaining small product need avoid only z, rather than every core-cover point.

Choose any interval multiple b0 of a0. If b0 differs from z, these two distinct points credit a0 and c_*. If b0=z, credit a0 at z and select a different point divisible by c_*; one exists because c_*<=8 and the interval contains at least pq>=143 of its multiples. In both cases, after at most one addition to the core cover there are two distinct points crediting a0 and c_*. All subsequent small-product points must avoid these two credited points and one another; they may overlap any other core-cover points.

## Criterion 1: one remaining small factor

The ordinary three-prime bank theorem gives a core cover of at most seven points for the six nontrivial sources, including z. If

    3*Q_max <= M,

one fresh multiple of Q avoids the two credited points. At most 7+1+1=9 points cover all source demands.

## Criterion 2: two spare pair banks

If at least two of the L_i are at least three, there are at least two pair banks with spare capacity beyond their multiplicity two. Prescribe z in its bank. Choose a different spare pair bank to avoid the unique possible triangle point, a multiple of pqr. That removes every positive cycle contribution, so the core cover needs at most six points while retaining z.

After crediting a0 and c_* at two distinct points, as above, the set has at most seven points. Pack the 7-smooth factor Q into two factors of capacities floor(M/3) and floor(M/4). Greedy insertion of its prime factors cannot fail when

    84*Q_max <= M^2.

Indeed, failure at a prime t<=7 would give Q >= t*b1*b2 > M^2/(12*t) >= M^2/84. The two factors have respectively at least three and four interval multiples, so their representatives can avoid the two credited points and each other. The total is at most 6+1+2=9.

## Finite checks

The first finite three-prime envelope run left 2386 classes of this type. Criterion 1 closed 1994. The other 392 are recorded in `zero_unclosed_envelope.json`; all have at least two spare pair banks and satisfy Criterion 2. The largest ratio 84*Q_max/M^2 among those 392 is less than 0.121.

Later strengthened envelope runs leave a subset of those classes. The generic checker `verify_zero_source_envelope.py` reads the current final unresolved-class file and verifies that each row with a0 present satisfies Criterion 1 or 2. The completeness of the upstream finite class enumeration is a separate dependency; these predicates use exact integer arithmetic and are valid for all actual choices of the cofactors in the class.
