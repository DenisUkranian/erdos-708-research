# Explicit lower-bound certificates for Erdős Problem 708

Date: 2026-11-24.

The following are certificates for individual instances, hence lower bounds for the universal function. They do **not** establish matching universal upper bounds.

For an input set `A` and `M=max(A)`, the target interval is `I={x+1,...,x+M}`. The certified minimum cover sizes are:

| n | Input A | M | x | Exact tau(A,I) |
|---|---|---:|---:|---:|
| 6 | 221,289,299,323,391,437 | 437 | 581200167 | 8 |
| 7 | 289,323,361,391,437,493,551 | 551 | 14478502565190 | 9 |
| 8 | 1369,1517,1591,1739,1961,2173,2279,2491 | 2491 | 246043396342067361 | 11 |
| 9 | 841,899,961,1073,1147,1189,1247,1271,1333 | 1333 | 155833862424257354 | 12 |

The n=6 instance is Proposition 3 of C. Bergström, *Exact Small-n Values ...*, DOI [10.5281/zenodo.24366897](https://doi.org/10.5281/zenodo.24366897). The n=7,8,9 instances here were derived independently during this investigation. Their lower-bound values were already known in this project's prior work; no claim of a new bound or external priority is made.

## A common exact lower-bound lemma

Let the relevant primes be `p_1,...,p_k`, with demand vector `D_i=sum_{a in A}v_{p_i}(a)`. Suppose a distinguished interval point `y=x+c` has valuation vector `h_i`. Suppose every other interval point is divisible by at most one relevant prime and its contribution to prime i, truncated at `D_i`, is at most `u_i`.

A cover omitting y needs at least

`L_without = sum_i ceil(D_i/u_i)`

points, because their supports are disjoint. A cover containing y needs at least

`L_with = 1 + sum_i ceil(max(D_i-h_i,0)/u_i)`.

Thus `tau(A,I) >= min(L_without,L_with)`. Exhibiting a cover of this cardinality proves equality. Truncating valuations at the demand is legitimate because oversupplying a prime cannot satisfy another prime's demand.

## Seven inputs require nine picks

Use primes `(17,19,23,29)` and

`A = {17^2,17*19,19^2,17*23,19*23,17*29,19*29}`.

Set `M=551`, `c=276`, `x=14478502565190`, and `y=x+c=14478502565466`. The Chinese remainder construction is

- `y ≡ 17^2 (mod 17^3)`;
- `y ≡ 19^2 (mod 19^3)`;
- `y ≡ 23 (mod 23^2)`;
- `y ≡ 29 (mod 29^2)`.

Every point has distance at most 275 from y. Since the smallest product of distinct relevant primes is `17*19=323>275`, no noncentral point contains two relevant primes. Since `17^2=289>275` and `19^2=361>275`, and these squares divide y, every noncentral point has 17-adic and 19-adic valuation at most one.

The demand is `(5,5,2,2)`, the central supply is `(2,2,1,1)`, and valid truncated off-center caps are `(1,1,2,2)`. Consequently

- without y: at least `5+5+1+1=12` picks;
- with y: at least `1+3+3+1+1=9` picks.

A nine-point cover is given by offsets

`276,259,293,242,257,295,238,253,247`.

Therefore `tau(A,I)=9`, proving `g(7)>=9`.

## Eight inputs require eleven picks

Use primes `(37,41,43,47,53)` and

`A = {37^2,37*41,37*43,37*47,37*53,41*53,43*53,47*53}`.

Set `M=2491`, `c=1246`, `x=246043396342067361`, and `y=x+c=246043396342068607`. The congruences are

- `y ≡ 37^2 (mod 37^3)`;
- `y ≡ r (mod r^2)` for `r=41,43,47`;
- `y ≡ 26*53=1378 (mod 53^2)`.

All offsets from y have magnitude at most 1245. The least distinct-prime product is `37*41=1517>1245`, so noncentral prime supports are disjoint. Since `37^2=1369>1245` divides y, all noncentral 37-adic valuations are at most one. The distances from y to neighboring multiples of `53^2=2809` are 1378 and 1431, both exceeding 1245. Thus every interval point has 53-adic valuation at most one.

The demand vector is `(6,2,2,2,4)`, the central supply is `(2,1,1,1,1)`, and truncated off-center caps are `(1,2,2,2,1)`.

- without y: at least `6+1+1+1+4=13` picks;
- with y: at least `1+4+1+1+1+3=11` picks.

An eleven-point cover has offsets

`1246,1209,1283,1172,1320,1205,1203,1199,1193,1299,1140`.

Therefore `tau(A,I)=11`, proving `g(8)>=11`.

## Nine inputs require twelve picks

Use primes `(29,31,37,41,43)` and

`A = {29^2,29*31,31^2} ∪ {29*r,31*r : r in {37,41,43}}`.

Set `M=1333`, `c=667`, `x=155833862424257354`, and `y=x+c=155833862424258021`. Choose

- `y ≡ 29^2 (mod 29^3)`;
- `y ≡ 31^2 (mod 31^3)`;
- `y ≡ r (mod r^2)` for `r=37,41,43`.

Every interval point is within 666 of y. Since `29*31=899>666`, noncentral active prime supports are disjoint. Since `29^2=841>666` and `31^2=961>666` divide y, both noncentral valuations are at most one.

The demand is `(6,6,2,2,2)`, the central supply is `(2,2,1,1,1)`, and truncated off-center caps are `(1,1,2,2,2)`.

- without y: at least `6+6+1+1+1=15` picks;
- with y: at least `1+4+4+1+1+1=12` picks.

A twelve-point cover has offsets

`667,638,696,609,725,636,698,605,729,630,626,624`.

Therefore `tau(A,I)=12`, proving `g(9)>=12`.

## Independent integer verification

Run `python verify_clean_witnesses.py`. The program independently factors every relevant interval integer, checks the unique mixed center and every valuation cap, checks input products, verifies all three CRT constructions, and directly checks that the product of each displayed cover is divisible by the product of its input set. It also rechecks the published n=6 certificate. It uses no floating-point arithmetic, no optimization solver, and no nonstandard Python packages.

The generated `clean_witnesses.json` contains all inputs, prime demands, caps, shifts, and achieving covers.
