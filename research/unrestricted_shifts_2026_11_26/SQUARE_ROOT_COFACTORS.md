# Two outside prime-power atoms at every source density and interval shift

Let A⊆[2,M] have n distinct elements and let I be any positive interval of M consecutive integers. Put y=floor(sqrt(log M)). An outside atom of a means the **full** power of a prime greater than y dividing a. If every a in A has at most two outside atoms then the stronger prime-power-level cover satisfies

    H(A,I) ≤ 2n + o(n),

as n→∞ uniformly in A,M and the shift. The core of a row can contain arbitrarily many small primes with arbitrarily high valuations. More precisely all but M^(1/10+o(1)) rows have distinct one-omission representatives. The exponent 1/10 can be replaced by any fixed positive constant.

Fix an exact y-smooth part k in the source and write X=M/k. A row with two outside atoms has the form k q r, in which q≤r are prime powers on distinct bases; label it q. A row with at most one outside atom has label 1. All actual labels q≤sqrt(X). At each label the number of rows is at most 1 plus the number of prime powers at most X/q, hence O(X/(q log X)) for large X. This follows from the elementary prime counting bound and the O(sqrt(t) log t) bound for nonprime powers through t.

For X≥M^(1/10), join this row to every target divisible by kq with exact smooth part k. Different k have disjoint target sets. Dividing the k-multiples by k gives a consecutive quotient interval of length X+O(1), and the remaining exact-core requirement is coprimality to P=product of the primes through y. We have P=M^o(1), and its coprime density is ≫1/log(2y) by Mertens' product theorem. Each label bank therefore has size ≫X/(q log(2y)): quotient multiples of q have cofactor in an interval of length X/q+O(1), with periodic counting error O(P), negligible since X/q≥sqrt(X).

Given any nonempty set of labels S, put λ=Σ_{q∈S}1/q and let D(b) be the number of these banks containing quotient position b. Then ΣD ≫ Xλ/log(2y). Also ΣD²≪X(λ+λ²). To see the latter, two distinct coprime labels have lcm at most X, and overlap at most X/(qq')+1 ≤ 2X/(qq'). This includes label 1. For distinct powers q<q' of one base p, the corresponding bound is 2X/q'. The total of 1/q' over all ordered increasing pairs on one base is at most Σ_{q∈S} Σ_{j≥1}1/(q p^j) ≤ λ. The diagonal costs O(Xλ).

Cauchy–Schwarz now gives a union of size ≫Xλ/[(1+λ)(log(2y))²]. Every permitted label is 1 or a prime power, so λ≪1+log log X. Since X≥M^(1/10), this union exceeds C Xλ/log X, where C is the absolute row-count constant above, once M is large enough. Hall gives distinct representatives for every row at this k. Repeating for all such k gives simultaneous distinct representatives. Each representative covers every source atom except at most one.

The number of possible cores k≤M is M^o(1): for each fixed σ>0, Rankin's bound is M^σ times ∏_{p≤y}(1−p^(−σ))^(−1)=M^{σ+o(1)}. For the remaining cores X<M^(1/10) there are at most M^(1/10+o(1)) rows in total. Every such row has O(log M) atoms. One extra target per unmatched atom suffices for simultaneous repair across all rows, by the nested prime-power counts. For details, after assigning the representatives, each prime p's maximum positive deficit over its levels is at most the number of p-atoms not covered by their assigned representatives. Adding this many highest remaining p-valuations supplies every level because I itself has sufficient capacity. Take the union of these repair positions.

Finally if M≥(2n)^3 the universal two-block argument in the previous cofactor paper gives H≤2n directly. Otherwise n>M^(1/3)/2 and M^(1/10+o(1))log M=o(n). This proves the result.

## More than two outside atoms

The same conclusion holds under the following alternative condition, for any fixed integer r. In each row with outside atoms designate one outside prime-power atom to omit; with no outside atoms omit nothing. Require the product d of the remaining outside atoms to be squarefree, to have at most r distinct primes, and to satisfy d≤sqrt(M/k), where k is its exact smooth core. The omitted atom may have any exponent. For a fixed label d the number of possible rows is still O(X/(d log X)). The lower count for a bank is unchanged. For λ=Σ_{d∈S}1/d the second moment is now bounded by

    2X Σ_{d∈S} (1/d) Σ_{e∈S} gcd(d,e)/e
      ≤ 2X λ 2^r Σ_{j=0}^r (Σ_{p≤X}1/p)^j/j!.

Indeed e≤sqrt(X) ensures lcm(d,e)≤X. For fixed squarefree d write e=g f with g=gcd(d,e) dividing d, so gcd(d,e)/e=1/f. There are at most 2^r choices for g and the displayed sum bounds all squarefree f with at most r prime factors. This replaces the earlier factor 1+λ by O_r((1+log log X)^r), still o(log X/(log(2y))²) for X≥M^(1/10). The rest of the proof applies verbatim. In particular the result applies when the product of the small remaining outside primes lies below the square-root threshold even if a source has three or more outside atoms. The two kinds of rows described above can coexist: if a label bank list mixes pure prime powers and squarefree products of at most r primes, use (D_1+D_2)^2≤2D_1²+2D_2² to combine the two second-moment estimates.

In fact the squarefreeness condition can be dropped. Here is a version of the second-moment bound for arbitrary labels with at most r distinct primes. The elementary identity Σ_{g|h} φ(g)=h gives

    Σ_{d,e∈S} 1/lcm(d,e) = Σ_g [φ(g)/g²] ( Σ_{d∈S : g|d} g/d )².

For g|d set ν(g,d)=∏_{p|g} p^{−(v_p(d)−v_p(g))/2}. Apply Cauchy–Schwarz to the inner square, splitting it into the product of the sum of (g/d)/ν(g,d) and the sum of (g/d)ν(g,d). The first sum is O_r((1+log log X)^r), uniformly in g with a nonempty inner sum. Indeed each of the at most r primes of g contributes a geometric series of ratio p^(−1/2), and the remaining factors of d form a number with at most r distinct primes. Their reciprocal sum is at most Σ_{j≤r}(Σ_{p≤X}1/(p−1))^j/j!. Inserting this bound into the outer sum leaves

    Σ_{d∈S} (1/d) Σ_{g|d} [φ(g)/g] ν(g,d) ≪_r λ.

For each p dividing d its factor in the inner sum is at most 1+Σ_{i≥0}p^(−i/2), uniformly in v_p(d). This proves Σ_{d,e∈S}1/lcm(d,e)≪_r λ(1+log log X)^r. Hence the enlarged theorem allows arbitrary full prime powers in the leftover d. It contains the original two-atom theorem as r=1.

The explicit products in the estimate even allow a growing rank. Set r=floor(c log log M) for fixed 0<c<1 with c log(2e/c)<1 (for example c=1/3). For X≥M^(1/10), the elementary reciprocal-prime estimate gives Σ_{y<p≤X}1/(p−1)≤(1+o(1))log log M. Since every label prime exceeds y, the products in the two Cauchy factors together cost at most (2+o(1))^r. Using Stirling in the truncated exponential sum, the second-moment penalty is at most

    exp[(c log(2e/c)+o(1)) log log M] = (log M)^{c log(2e/c)+o(1)}.

Multiplication by (log(2y))² still leaves this o(log X). The Hall comparison and final unmatched-row estimate therefore hold for this growing number of distinct atoms as well.
