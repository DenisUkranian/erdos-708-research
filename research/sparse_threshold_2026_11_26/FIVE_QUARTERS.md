# Two positions per source for intervals of length at least n to the power 5/4 plus epsilon

**Theorem.** Let ε>0 be fixed. There exists c=c(ε)>0 such that the following holds for all sufficiently large n. Let A be n distinct positive integers at most M, and I any interval of M consecutive positive integers. If M≥n^(5/4+ε), there exists F⊆I with

$$
 |F|\le 2n+O_\varepsilon(n^{1-c}),\qquad
 \#\{b\in F:p^j\mid b\}\ge\#\{a\in A:p^j\mid a\}
$$

for every prime p and j≥1. In particular the product of A divides the product of F.

We use the heavy-unitary-divisor extraction from [redlydi, prime-power level-cover report, §§2–5](https://github.com/redlydi/Erdos708-Research/blob/32f397f8fdc00d0e9c73242d8510c541267a30db/reports/erdos708-power-level-cover%20(1).md), which gave this conclusion with exponent 3/2+ε. The additional quotient labels in that extraction will have separate lists indexed by intervals of prime divisors. A further set of private lists pays for repeated copies of their common factor.

## 1. Extraction and the main labels

Use one full prime power p^{v_p(a)} as an atom for each p dividing a. Greedily split each a into two coprime blocks by multiplying the smaller current block by the next atom, in decreasing order of atom size. A unitary divisor d of a means d|a and gcd(d,a/d)=1. For each resulting block h and each of its atoms q we have h²≤Mq. Indeed, immediately before the last atom q_0 of h was placed, the other block was at least h/q_0, and q_0 is the smallest atom of h. If h has at least two atoms then q_0≤sqrt(h) and h≤M^(2/3). Both the inequality h²≤Mq for a shared atom q and the size bound remain valid for a unitary divisor of a mixed block. Labels with at least two distinct prime bases are called mixed.

If M≥(2n)^3, each mixed block has at least floor(M^(1/3))≥2n available multiples, so all mixed blocks can be placed at distinct positions. Deferred single-atom blocks can be repaired at one position each by the level repair argument in §5. This gives |F|≤2n. We therefore assume M<(2n)^3 and put β=1/(5/4+ε) and G=1−β, so n≤M^β and M≪n³. If needed enlarge β to any fixed number strictly between 1/3 and 4/5. All constants below may depend on β.

Choose a sufficiently small fixed λ>0 as specified in §3. Set W=M^(1−λ) and X=Mn/W=nM^λ. Fix the initial greedy blocks. Let D be the set of all nontrivial unitary divisors of mixed initial blocks. In the remaining rows, let r(d) count those containing d unitarily. Choose the least d∈D with d r(d)≥W, and remove all rows with d as a unitary divisor as one group. Repeat until all d fail this test. Within the group for d use labels d and h=a/d. The remaining rows use their two original blocks. Discard labels equal to one, and defer all single-atom labels. The mixed labels d and the mixed terminal blocks form class B. The mixed quotients h from extracted groups form class C.

Each group for d has at least W/d rows, so Σ_d 1/d≤n/W. Every h in class C is at most M/d≤X, and within one group the h are distinct. More generally, for any integer t≥1 the number of class C occurrences divisible by t is at most

$$
 \sum_d\left\lfloor{M\over dt}\right\rfloor\le X/t. \tag{1}
$$

This counts occurrences across all groups, including equal quotient values.

Two integers are compatible when their exponents agree at each common prime. Among class B occurrences with different values and nontrivial gcd, the sum of gcds over compatible pairs is at most nW M^o(1). To see this, order main group labels by extraction time, followed by terminal blocks. If a main d shares a compatible gcd t with a later main or terminal label, then t is a proper unitary divisor of d, since otherwise the later row was already removed at d. The value t belongs to D and was below the threshold t r(t)<W when d was extracted. For two terminal labels the same inequality holds at termination. Each row contributes at most two labels and each earlier label has M^o(1) divisors, so summing gives the stated bound. Distinct labels from the same main group do not arise. Furthermore, compatible noncoprime B values h,k share a full atom q and satisfy h²,k²≤Mq, implying lcm(h,k)≤M.

## 2. The bands associated to a quotient

Let ρ be a sufficiently small fixed positive number, choose λ much smaller than ρ, and put

$$
 Y=M^{G-\rho},\qquad B_0=\lfloor M^{G-2\rho}\rfloor ,\qquad u=M^\theta
$$

where θ>0 is sufficiently small compared with ρ. Real endpoints and the last shortened band cause no difficulty. Every list built below has quotient interval length H=M/t with 1≤t≤X, so H≥M^(G−λ).

Primes through u will all be screened. Between u and Y partition the exponent interval [θ,G−ρ] into finitely many fixed subintervals (the **low bands**) so fine on the logarithmic scale that the sum of 1/p in each band is ≤ν for all large M. Here ν>0 will be chosen after θ. This is possible by the prime reciprocal Mertens formula; the number of bands is independent of M. Divide the integers above Y through M into consecutive bands of length B_0, with left endpoints P_j (the **high bands**). Write r_j=B_0/P_j. Uniformly r_j≪M^(−ρ), and Σ_j r_j=O(log M).

For a class C value h start by recording every low or high band containing a prime divisor of h. If there is a high band and the largest occupied high band contains just one distinct prime divisor p of h, remove this band from the record. In that case put g=h/p^{v_p(h)}. In all other cases retain the entire record and put g=h. Denote the resulting record by S. It contains all bands occupied by g, and all primes ≤u occurring in h occur in g with full exponent. Thus S depends only on which bands g occupies. The residual h/g is either one or one full prime power in a high band outside S. Every h and every g has at most K=ceil(2/θ) occupied bands for all large M. The prescription permits several prime divisors of h in a single retained band.

## 3. Size, separation and probability for the lists

For t=h of record S, or t=g using its record S, first form an uncolored list of multiples b of t in I. Require b/t to have no prime factor ≤u or in a band in S. For t=h additionally require gcd(t,b/t)=1; the only possible additional exclusion beyond the screened factors is the single residual prime. We also use this definition for g=1 when convenient. Each such list has size at least

$$
 c_0 {M/t\over\log M} . \tag{2}
$$


Here are details uniform in t,S,I. The quotients run through H+O(1) consecutive integers, H=M/t≥M^(G−λ). By the standard one-dimensional lower linear sieve, their count free of primes ≤u is at least c H/log u. The upper linear sieve bounds the count of u-rough integers in any quotient interval of length H/p+O(1), for p≤Y, by C H/(p log u). For both estimates take level the quotient length divided by a sufficiently large fixed power of log M. Each residue count has error at most one per modulus, and choose θ sufficiently small compared with ρ−λ so the sieve parameter log(level)/log u is uniformly large even for H/p≥M^(ρ−λ). The constants c,C may be taken absolute after this choice. These estimates follow from the dimension-one fundamental lemma on intervals. See [Ford, Sieve Methods](https://ford126.web.illinois.edu/sieve2023.pdf) and [Tao, the linear sieve](https://terrytao.wordpress.com/2015/01/29/254a-supplement-5-the-linear-sieve-and-chens-theorem-optional/). For an occupied low band, each forbidden prime p costs at most C H/(p log u) by writing a u-rough multiple of p as p times a u-rough quotient. The combined cost for ≤K occupied low bands is ≤C K ν H/log u. Choose ν<c/(4CK). For one high band starting at P≥Y, even the unsieved cost is at most O(H B_0/P+B_0), by summing H/p+O(1) over that band's primes. Its ratio to H is O(M^(−ρ)+M^(−2ρ+λ)), still a power saving after all K bands. The one possible additional residual prime p>Y costs ≤H/p+1. This proves (2).

If an occupied target position belongs to two lists of the same record S, its exact prime valuations through u and at all primes of the bands in S determine the same g for both labels. Indeed these primes divide each candidate t or fail to divide b/t, and in the case t=h they do not divide h/g. This applies to both kinds of lists. In particular lists for two different restoration values g of the same record are disjoint.

We allocate two separate colors per record S, one for placement and one for restoration. To control how often each color occurs set

$$
 t_S=\prod_{j\in S\text{ high}}r_j.
$$

The sum of t_S over all possible records is O((log M)^K), since there are only a fixed number of low bands and Σ_j r_j=O(log M). Choose a normalization Z comparable from above to (log M)^K and large enough that Σ_S t_S/Z≤1. For every occurring record

$$
 t_S\ge M^{-G+\xi} \tag{3}
$$

for some ξ>0 depending only on β. To verify this, let k be the number of its high bands and let a_i=log(P_i)/log M be their lower-end exponents. When k>0 select one distinct prime divisor of h from each such band. There is another distinct prime divisor of h of size at least max_i P_i. It is either the omitted largest high prime, or a second prime in the largest retained high band if that band was retained owing to the tie. Thus Σ_i a_i+max_i a_i≤log_M h≤β+λ. Consequently

$$
 -\log_M t_S\le k\left({\beta+\lambda\over k+1}-G+2\rho\right)+o(1).
$$

For each k≥1, k(β/(k+1)−G)<G, since β/G<4≤(k+1)^2/k. First restrict to k≤K_0=ceil(2/G), valid for small ρ because h≤M and all high primes exceed M^(G−ρ). Choose ρ,λ small in terms of the fixed positive margin over these finitely many k. This proves (3), with k=0 immediate. Now choose a positive κ much smaller than ξ, and λ small enough that κ+λ<ξ. This specifies the constant choices consistently: the size margin uses only β,G,K_0, independent of θ or the number of low bands.

Color the positions independently with the following distribution. each of the two colors of record S gets probability M^(−κ)t_S/(2Z); all remaining probability goes to the main color. The nonmain fraction is at most M^(−κ). By (2), (3), the expected size of any needed colored class C list or restoration list at t≤X is ≫(M/t) M^(−G+ξ−κ−o(1)), which exceeds both M^c and M^c X/t for some c>0. The union bound and the Chernoff lower tail over at most polynomially many needed lists ensure that all have at least X/t candidates simultaneously. In particular no occurring record is left without a color. The restoration records are constructed from the original h labels before coloring even when a particular restoration might ultimately be unnecessary.

## 4. Placement of all quotient labels

Assign occurrences of each numerical class C value h injectively to its placement list; (1) and §3 guarantee enough candidates. No intersections across different records are possible because their colors are disjoint. At any occupied position with s≥1 quotient labels, the s labeled occurrences all have the same screened part g. Distinct h sharing an unscreened prime and this common g must be unequal powers of that prime times g. Their exact exponent conditions exclude a common position. Equal h never coincide by injectivity. All residual prime powers at this position therefore have disjoint bases, each coprime to g.

Credit one copy of g and all residual powers at their shared position. Each of the other s−1 copies of g, if g>1, is assigned to a fresh point of the restoration list for g. Across all placements this requires at most X/g points for each g by (1). Lists for distinct g in one record are disjoint by exactness, and different records have disjoint colors. Thus all restorations can be made simultaneously with distinct positions, disjoint also from all original placements and the main color. The s original labels cost at most s positions and all of their prime-power levels have been covered without any duplicate credit. This part incurs no exceptional tasks.

## 5. Placement of the main labels and the level repair

The uncolored main list for h∈B is V_h={b∈I:h|b, gcd(h,b/h)=1}. Inclusion-exclusion yields

$$
 |V_h|=(M/h)\prod_{p\mid h}(1-1/p)+O(2^{\omega(h)}),\qquad
 \mu_B(h)\le |V_h|+2^{\omega(h)},
$$

where μ_B(h) counts occurrences: each row using h is a distinct source divisible unitarily by h, and a row gives h at most once. The last inequality compares the counts on the canonical prefix and I, each individual floor count differing by at most one. All uncolored lists have size ≥M^(1/3−o(1)) since h≤M^(2/3), each factor product is ≥2^(−ω(h)), and the divisor function for all h≤M is M^o(1). With probability 1−o(1), simultaneously for all such lists, at most 2M^(−κ)|V_h| positions lack the main color, upon making κ smaller than 1/4. This follows by Chernoff again and can be imposed together with §3.

Trim occurrences whose multiplicity exceeds the available main list. Each overflowing value has multiplicity ≥M^(1/3−o(1)) and loses O(M^(−κ)μ_B(h)+2^ω(h)) tasks. In total the trimming costs O(n M^(−κ)+nM^(−1/3+o(1))) tasks. On the remaining tasks use an independent uniform injection into its main list for each numerical h. Different compatible noncoprime values h,k have lcm≤M. Their collision probability per pair of occurrences is at most M^o(1) gcd(h,k)/M, by the list lower bounds and the upper bound 2M/lcm(h,k) for their common candidates. Incompatible values have disjoint lists, and equal values were placed injectively. The gcd estimate in §1 bounds the expected number of noncoprime collisions by nM^(−λ+o(1)). Fix an assignment meeting this bound and omit both ends of every such collision. The number of omitted and trimmed mixed tasks is O(nM^(−c')) for some c'>0. All surviving placed labels at a common main position have disjoint prime supports, so all their level credits can be used.

Take all placement and restoration points already credited. For each prime p the maximum deficit in its level counts over powers p^j is at most the number of still unplaced labels that contain p. Select that many additional unused positions of greatest p-adic valuation, or all remaining ones if fewer. On each level the supply of all of I dominates A since I has at least floor(M/p^j) multiples, and the selected positions of highest valuation repair all deficits for this prime. Taking the union across primes only helps. The total additional budget is at most one per deferred single-atom label and ω(h)≤log_2 M per exceptional mixed label. Each source had at most two labels, and all class C placements and restorations together cost at most the number of their original occurrences. Hence |F|≤2n+O(n M^(−c')log M). In the noncubic range n≤M≪n³ this implies the claimed estimate with a possibly smaller exponent c(ε). Every level inequality now holds.

**Boundary.** The argument uses β/G<4 strictly. It gives neither an endpoint rate for M=n^(5/4) nor a uniform coefficient-two bound throughout the remaining range. No priority claim beyond the comparison to the stated prior report is intended.
