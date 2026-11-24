# A row-level warning for the actual-size kernel

This is an obstruction to a coordinatewise transfer lemma. It does not refute the aggregate kernel inequality, or an estimate restricted to genuine positive optimizers.

Let alpha=1/1000, y=z^alpha, N=2z^2, M=2N. Give price one to 2 and to every prime in (y,z], and zero to all other primes. At every level 0<t<1/2, the p=2 row of the proposed actual-size kernel has source event

    a=2k, with an active prime q|k satisfying q^2<=k.

The target event at ambient size M is simply that k has an active prime divisor, because all active primes are <=sqrt(N). Multiplicity in the row is v_2(a)=1+v_2(k).

Choose the quotient shift x divisible by 2^E>N. This preserves all 2-adic valuations at positions 1,...,N. By CRT, the residues of x modulo the band primes can still vary independently. The mean number of odd target quotients avoiding the whole band equals

    (N/2) product_{y<q<=z}(1-1/q) = (alpha/2+o(1))N.

The prefix has fewer than 0.00049N such odd quotients, for all sufficiently large z. Here is an elementary bound, using only the prime number theorem and Mertens' product theorem. A band-avoiding prefix integer is either y-smooth, a large prime >z times a y-smooth cofactor, or a product of two primes >z (the last class is o(N)). The y-smooth class is O(alpha^2 N): for W(k)=sum_{p<=y}log(p)v_p(k), the first two moment expansions give E W^2 <= (3/2+o(1))log^2 y, and every y-smooth k>sqrt(N) has W(k)>(log N)/2.

For the large-prime class, sum over odd y-smooth cofactors u. The harmonic and logarithmic-harmonic sums are

    sum_u 1/u = (e^gamma/2+o(1))log y,
    sum_u log(u)/u = (e^gamma/2+o(1))log^2 y.

Split at u=z^(1/10). The first piece contributes at most

    (e^gamma alpha/(2*1.9)+o(1))N,

and the second at most

    (5e^gamma alpha^2+o(1))N.

Even adding 4alpha^2 N for the smooth class, their sum is below 0.00049N. Thus some actual CRT shift has at least 0.00001N more odd band-avoiding target quotients than the prefix.

Replacing the unrestricted prefix union by the actual-size source event loses at most

    sum_{q active, q<=z} (q-1) = O(z^2/log z)=o(N),

because a discarded multiple qt must satisfy t<q. The p=2 multiplicity is exactly one on odd quotients, while the even-quotient row contributions are preserved by x=0 mod 2^E except for finitely many initial source positions. Therefore the source-minus-target discrepancy in this single row and level is Omega(M).

The reciprocal weighted mean stays bounded: sum_p w_p/(p-1)=1+log(1/alpha)+o(1). All active prices occur in the full tail at any fixed source threshold between 2 and 3: use 8 and 2q^2<=M.

Again, different rows and different levels are not independent. This example only rules out a separate O(sqrt(M)) transfer bound for each row/level, even after enforcing the actual-size cutoff and a bounded reciprocal mean. The aggregate coherent kernel remains the relevant open step.
