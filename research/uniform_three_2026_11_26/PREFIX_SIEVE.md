# An exact eventual four-per-source bound from three deleted atoms

Let A⊆[2,M] have n distinct elements, M=max A. For every positive interval I of M consecutive integers the stronger level-cover number H(A,I) is at most 4n−3 for every sufficiently large M, uniformly in source size, density and shift. In particular g(n)≤4n−3 for all sufficiently large n. The argument uses a classical lower sieve at a level strictly above its parity threshold. It does not give coefficient two.

## Strict rough-number comparison

There exists H₀ such that for every real H≥H₀ and prime r with H≥r³, the number in any positive half-open interval of real length H having no prime divisor <r exceeds the number of composite integers ≤H having no prime divisor <r by at least cH/log H, for an absolute c>0.

Put v=log H/log r; first let 3≤v≤V, for fixed sufficiently large V. The Buchstab estimate and the PNT give the canonical composite count as (ω_B(v)−1/v+o_V(1))H/log r. The lower dimension-one linear sieve at D=H/(log H)^C gives at least (exp(−γ) f(v)−o_V(1))H/log r in every shifted interval. Each divisor-count remainder is ≤1; the accumulated remainder is negligible for fixed sufficiently large C. Mertens' product is asymptotic to exp(−γ)/log r. Write h(v)=v(ω_B(v)−exp(−γ)f(v)). One has h(2)=1, and h'(v)=ω_B(v−1)−exp(−γ)F(v−1)≤0 by the delay equations and F+f=2exp(γ)ω_B. On 2<v<3 this derivative is −1/(v−1), since f=0 and exp(−γ) F(s)=2/s for 1<s<2. Thus h(v)≤1−log 2 for v≥3. The resulting positive margin at least (log 2)/v absorbs both errors for fixed V and leaves a difference ≫H/log H.

For v≥V use the fundamental lemma of the dimension-one sieve at level D=sqrt(H). For both the canonical and translated intervals the rough count equals

    H V(r)[1+O(exp(−c v))]+O(sqrt(H)),

where V(r)=∏_{p<r}(1−1/p)≍1/log(2r), with absolute constants. This estimate follows from the fundamental-lemma sieve weights of modulus ≤D and absolute value at most one, with local density 1/p and individual remainders ≤1. Thus the difference of the two rough counts is bounded by O(H exp(−c v)/log(2r)+sqrt(H)). The number of canonical primes ≥r through H is (1+o(1))H/log H, uniformly as r≤H^(1/3). Choose a fixed V large enough that the comparison error is less than half that prime count for all sufficiently large H, using log H=v log r. Subtract the primes and one from the canonical count to obtain a difference ≫H/log H.

Analytic inputs: [Tao, linear sieve and the defining delay equations](https://terrytao.wordpress.com/2015/01/29/254a-supplement-5-the-linear-sieve-and-chens-theorem-optional/), [Vaughan, Chapter 7, Buchstab estimate (42)](https://personal.science.psu.edu/rcv4/568s20/568chapter7.pdf), and [Ford, Sieve Methods, the fundamental lemma](https://ford126.web.illinois.edu/sieve2023.pdf).

## Hall matching of the fixed cofactors

Defer all rows with at most three distinct prime divisors. Also defer rows whose largest prime base is ≤H₀. For each remaining row let d₀(a) be its cofactor after deleting the full powers of its three largest distinct prime bases. Join it to every target multiple of d₀(a).

Fix a nonempty family S of these rows and let T be the union of its neighborhoods. If T=I then |T|≥|S|. Otherwise call an integer d trapped when every one of its multiples in I belongs to T. The integer one is not trapped, and d₀(a) is trapped for each a∈S. Factor each a as a list of primes in increasing order with multiplicities. Along its prefix products let d be the first trapped prefix, so that d is reached no later than d₀(a). Write r for the last (largest) prime in d. The remaining quotient a/d is free of primes strictly below r and contains the three deleted prime bases, all strictly above r. It is composite, M/d≥r³, and M/d≥P⁺(a)>H₀.

Group S by d. Different rows of a group give different composite r-rough quotients ≤M/d. In I every multiple b=dm whose quotient is r-rough has the same initial prime list through d, with the same first trapped prefix; allowing m to contain additional factors equal to r does not change that prefix. All such b belong to T. Different terminal prefixes give disjoint target classes. The strict rough comparison at H=M/d shows that the target class is at least as large as the source class for each d. Summing gives |S|≤|T|. Hall's theorem produces distinct representatives for all these rows, each paying its full cofactor before three deletions.

## Absorbing the bounded-prime rows and reserving one anchor

Allow a high-rank row to use any cofactor obtained by deleting up to three full atoms. For a nonempty subset S of all rows with at least four distinct prime factors, take T to be its neighborhood in this enlarged graph. If T=I then |T|≥|S|+1 since 1 is excluded from A. Otherwise apply the terminal-prefix comparison above to the good rows (largest prime base >H₀) with this common, enlarged T. Their fixed cofactors are still trapped. The strict surplus in every occupied class is at least cH/log H, H=M/d. As the source count in that class is at most H, this proves |T|≥(1+c/log M)|S_good|. In particular, if every row is good, the integer neighborhood has the desired one spare point.

Let K=max(1,π(H₀)) and E_M=(1+log₂ M)^K. There are at most E_M bounded-prime rows. When S contains such a row, one of its alternatives has at least floor(M^(1/K)) multiples in I: delete its numerically largest full prime power, which is at least a^(1/K), leaving cofactor at most M^(1−1/K). Deleting two more atoms only enlarges the bank. If |S_good|≥(E_M+1)log M/c then its surplus already pays for every other row and one extra. Otherwise |S|≤E_M+(E_M+1)log M/c=o(M^(1/K)), and this single alternative bank pays the whole count with slack. Thus every nonempty S has |T|≥|S|+1 for all sufficiently large M.

Anchor any one row at a multiple of its entire value in I, and remove the anchor row and position. Hall now allows distinct representatives for every remaining high-rank row by the one-point slack. Each representative pays all its row's atoms except at most three. Each unanchored low-rank row owes at most three atoms in total. At any prime p, the maximum positive deficit over all power levels is at most the number of its unpaid atoms; taking that many greatest remaining valuations suffices because the whole interval has at least the canonical count at every level. Union these repairs across the primes. The cost is at most 1+4(n−1)=4n−3, also when there are no high-rank rows. All thresholds are absolute.

## A three-per-row bound with a term for clustered large primes

Fix 0<ε<1. For a row a with at least four distinct prime factors let r<p<q be its three largest prime bases. Let d₂(a) be the cofactor left after deleting the entire p- and q-atoms. Let B_ε(A) count these rows for which M/d₂(a)<r^(2+ε). For all sufficiently large M (depending on ε), the same argument gives

    H(A,I) ≤ 3n+B_ε(A)−2.

Allow up to two deletions on high-rank rows outside this exceptional set and up to three on its members. The strict rough comparison holds with H≥r^(2+ε): on compact v≥2+ε use h(v)≤1−log(1+ε); the large-v argument is unchanged. The good rows in the proof have a first trapped prefix at or before their respective cofactors after the specified number of deletions. Its quotient contains at least two larger prime bases and its H is at least the terminal prime to power 2+ε. The large-neighborhood alternative of a bounded-prime row still uses only a single deletion. Each matched ordinary high-rank row thus costs at most three, each exceptional row at most four, and each low-rank row at most three; anchor one row as before.

This gives H≤3n+o(M) uniformly over all source families and shifts, a relative o(n) error at every fixed positive density. Indeed each exceptional row has q<r^(1+ε) and both p and q occur to the first power. Fix small δ>0. Rows with q≤M^δ have upper density tending to zero as δ→0 by the classical smooth-number estimate (or by a fixed initial segment of prime-reciprocal sieve bands). For the others one has r>M^(δ/(1+ε)). Counting multiples of r p q on the canonical prefix and using Mertens' prime reciprocal estimate, their proportion is at most

    Σ_{M^(δ/(1+ε))<r≤M} (1/r) (Σ_{r<p<r^(1+ε)} 1/p)^2
       ≪ (1+log(1/δ)) (log(1+ε)+o_δ(1))².

First take M large with δ,ε fixed, then ε small and finally δ small. This argument allows the source family itself to vary arbitrarily.
