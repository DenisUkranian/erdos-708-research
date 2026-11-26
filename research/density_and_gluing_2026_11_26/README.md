# Covering costs after deleting sources and at intersections of prime progressions

Let $A$ consist of $n$ distinct positive integers in $[1,M]$. For any interval $I$ of $M$ consecutive positive integers write $\tau(A,I)$ for the least number of distinct positions whose product is a multiple of the source product. The stronger minimum $H(A,I)$ requires the level counts at every prime power to dominate those of $A$. All bounds below hold for each shift. The unrestricted estimate $g(n)\le(2+o(1))n$ remains open.

## Exact coefficient two above 39.30 percent

For $n/M\ge0.3930$ and all sufficiently large $M$, every interval admits a product cover with at most $2n$ positions. The earlier bound in the project started at $0.3960$. The proof rounds the prices on primes above $\sqrt M$ into zero-one variables on the source side, derives a signed mean constraint on a putative counterexample, and uses a pair count when the variance estimate is insufficient. The final verifier checks both sides of the mean threshold using outward-rounded integer arithmetic. [Proof and coverage](DENSITY_THRESHOLD.md) · [C++17 verifier](verify_density.cpp)

## A residual set retaining an ordinary covering lower bound

For **every source density**, every fixed integer $R$ and every fixed $0<\delta<1$, choose a sufficiently small fixed $\gamma=\gamma(R,\delta)>0$. Keep just the source integers all of whose primes are at most $4n$ and which have at least $R+1$ distinct prime factors exceeding $(\log M)^\gamma$. If the original interval needs more than $(2+\delta)n$ positions for the product, the retained source $E$ still needs more than $2|E|+\delta n/2$ positions in that same interval. In particular the hard residual still has a positive fraction of the original rows. [Proof for all scales](GLOBAL_RANK.md) · [Congestion and price estimates](PRUNED_RESERVE.md)

Fix $0<\delta\le1$, a positive lower bound $t_0$ on $n/M$, and an arbitrary fixed integer $R$. For some $c=c(t_0,\delta,R)>0$, let $E$ consist of the source integers with **at least $R+1$ distinct prime factors exceeding $M^c$**. For all sufficiently large $M$,

$$
\tau(A,I)>(2+\delta)n\quad\Longrightarrow\quad
\tau(E,I)>2|E|+\delta n/2 .
$$

The same implication holds with $H$ on both sides. In particular, $|E|\gg_\delta n$ by the earlier uniform three-position theorem. The cutoff depends on $R$. No inference about a prescribed fixed cutoff for all $R$ is needed. A version at $n\ge M/(\log M)^K$ first deletes prime factors above $4n$ by removing their source rows, then uses $c=(\log\log M)^{-4}$. The proof reserves a small part of the cost of a single dual witness for simultaneous representations of all discarded rows. [Two representations per bounded-rank row](BOUNDED_RANK.md) · [Proof of the residual inequality](RESIDUAL_GAP.md)

An independent deletion rule removes every row $hpq$ with $h\le H_0<p<q$ and $H_0=\exp(\log M/[(\log\log M)(\log\log\log M)^2])$. These rows can be restored around an arbitrary optimal residual cover at two positions each plus $o(n)$ in total, uniformly for $n\ge M/(\log M)^K$. Every surviving enriched pair of primes above $H_0$ then has at least $\lfloor H_0\rfloor$ canonical quotient positions. A semiprime family at $n\asymp M/\log M$ shows exactly why a pair-density estimate alone did not guarantee this conclusion. [Proof and example](TERMINAL_ROWS.md)

## More than twice the ambient density

At **every** remaining scale of $n,M$, a violation of $H\le(2+\delta)n$ forces two powers $d,e$ of different prime bases such that

$$
\frac{|A\cap de\mathbb Z|}{\lfloor M/(de)\rfloor}>
(2+\delta/64)\frac nM .
$$

Each constituent level also has density greater than $(1+\delta/64)n/M$. The intersection gain survives in an actual union and in a union with one common level. A common slack variable for all powers of a prime bounds its total dual price by one. Only the large prime bases that actually occur in sources need to be counted. These two observations allow repeated prime factors and polynomially sparse sets. [All-scale proof](ALL_SCALES.md) · [First-power version for larger excluded supports](TWO_BASELINES.md) · [Conditional gain on the same pair](CONDITIONAL_GAIN.md)

At positive density one can take actual primes in complete rectangular arrays. A positive fraction of the source is distributed among the cells of a collection of arrays, and each cell is more than twice as dense even when credited only with rows assigned exclusively to it. At logarithmic sparsity the assigned fraction has the explicit lower bound in the proof. Deleting near-terminal rows first guarantees many actual source rows per cell there. The density used after a deletion is always that of the surviving set in the original ambient interval. [Private source assignments and growing rectangles](GRIDS.md)

At fixed source density $t\ge0.1965$, every collection of at most $M^\eta$ of these private cells has an **exact simultaneous level cover of size at most twice its actual number of sources**, for some fixed $\eta>0$. This covers arbitrary shared prime endpoints and all original sources lying on the chosen cells. For $t\ge1/4$, the strict half-occupancy margin pays for duplicate target credits. Down to $t=0.1965$, the proof uses the level-cover form of the 39.30% density estimate inside each quotient. A concentration on a single heavily divisible target is handled by capping the loss separately at each prime. The cost of adjoining a separate cover of the complement is still open. [Physical gluing theorem](PHYSICAL_GRIDS.md)

## Source classes with an actual two-position cover

For any set of primes $P$ and any individual endpoints $p k_p\le M$, let

$$
V=\bigcup_{p\in P}\{p,2p,\ldots,k_pp\},\qquad N=|V|.
$$

Then $H(V,I)\le 2N+O(N/\log\log(10N))$ uniformly over all choices. The estimate also yields $2n+o(n)$ for sources occupying a $1-o(1)$ fraction of $V$. Unrestricted lengths, unrestricted numbers of prime bases and overlaps are all permitted. The proof integrates the active reciprocal-prime mass over the cutoffs before rounding a single target selection. [Prefix union theorem](PREFIX_UNIONS.md) · [Cofactor-demand test for incomplete progressions](PRIME_UNIONS.md)

A separate finite bound for general level covers is $H(A,I)\le3n/2+M/4+O(M/\log M)$ for $M/6\le n\le M/2$. It follows by counting weighted pairs of distinct prime bases. When comparing ordinary product bounds one should also use the existing density certificates, which can already give stronger estimates. [Finite bound](DENSITY_BOUND.md) · [Ordinary product estimates from the earlier certificates](DENSITY_CERTIFICATE.md)

## Verification and dependencies

The executable checks use Python 3. The continuous polynomial certificates in `verify_double.py` also use SymPy. Run the files separately from this directory. [Replay output](REPLAY.txt)

The analytic arguments use the earlier [uniform upper bound](../uniform_three_2026_11_26/README.md), [prime valuation profile estimates](../unrestricted_shifts_2026_11_26/SUBPOWER_PROFILES.md), [density certificates](../density_2026_11_26/README.md), and the one-dimensional sieve in [Ford, Theorem 3.6](https://ford126.web.illinois.edu/sieve2023.pdf). The finite checks exercise inequalities and constructions. The asymptotic assertions rest on the written proofs.
