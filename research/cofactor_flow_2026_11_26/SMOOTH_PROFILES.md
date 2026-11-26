# Sharp discrepancy of polylogarithmic smooth-part profiles in shifted intervals

Let X and x be nonnegative integers, with X tending to infinity. Write s_y(t) for the full divisor of t supported on primes at most y, with multiplicity. For an interval J of positive integers let h_J(d) count t in J with s_y(t)=d. Take I=[x+1,x+X], J=[1,X], fix C>1 and set y=(log X)^C and σ=1−1/C. Then

    sup_x sum_d (h_J(d) − h_I(d))_+ = X^(σ+o(1)).

The one-sided sum equals half the L1 distance since both histograms have mass X. The supremum is over actual intervals of integers. The upper error is uniform in x.

## Upper bound

For y-smooth d≤X set Y=X/d. If Y≥y let r be the largest positive odd integer no larger than log Y/log y. Exactness of the y-part d requires d|t and no p≤y dividing t/d. Use the odd Bonferroni truncation through r for the lower count on I. Its signed divisor sum transferred to J changes by at most the number of squarefree e of primes ≤y with ω(e)≤r, because every divisor count changes by at most one. All such de≤X. On J the difference between the even upper bound of degree r−1 and this odd lower bound is at most

    Y (sum_{p≤y} 1/p)^r / r!.

If Y<y bound the deficit by Y directly. The displayed remainder throughout is at most Y^σ X^{o(1)}. Indeed put L=log X, t=log Y, so r=t/(C log L)+O(1). For t≥L/log L, one has log r=log L+O(log log L), and the logarithm of the factorial saving is at least t/C−o(L) by Stirling and sum_{p≤y}1/p=O(log log y). For t<L/log L the desired bound follows from the trivial bound Y times exp(sum 1/p) and Y^{1/C}=X^{o(1)}. This also covers Y<y.

The total divisor-count errors over d are at most sum over y-smooth m≤X of 2^{ω(m)}. By Rankin this is ≤ X^σ times the product over p≤y of (1+p^{−σ})/(1−p^{−σ}). Its logarithm is O_C(1+sum_{p≤y}p^{−σ})=O_C(y^{1−σ}/log y)=o(log X) by partial summation and the prime-counting upper bound. The total remainders are at most X^{σ+o(1)} times the sum of d^{−σ} over all y-smooth d, which the same Euler product bounds by X^{o(1)}. A source profile cannot have d>X. This proves the upper bound.

## Matching lower bound

Choose an integer N divisible by p^k for every p≤y, with k>log_2 X. Center a length-X interval around N. At each noncentral point its full y-part is that of the absolute offset, at most ceil(X/2). The central y-part exceeds X. Hence every y-smooth d in (ceil(X/2),X] contributes a unit deficit.

Put r=floor(log(X/2)/log y). Pick r distinct odd primes in [y/2,y], form their product and multiply by the unique nonnegative power of 2 placing it in (X/2,X]. This has distinct odd parts across choices. There are X^{σ+o(1)} such choices by the prime number theorem and Stirling, since the prime pool has order (log X)^C/log log X. At most one resulting d fails the strict cutoff at ceil(X/2). This proves sharpness. A profile mismatch alone does not imply a covering obstruction.

## Joint moments with external divisors

Keep the original y=(log M)^C. For fixed α<1 and e≤T≤M^α coprime to the product of the core primes, split off e. The e-multiples of an arbitrary shifted length-M interval give a quotient interval of length floor(M/e) or one more. Removing one point handles the longer length. The histogram proof is uniform for X=floor(M/e) here even though y was defined with M: log X is comparable to log M and log y=C log log X+O_{α,C}(1). The Euler bounds and the factorial estimates carry the same exponent and uniform subpower factors. Consequently the sum over e≤T of the L1 errors in the joint counts 'e|t and s_y(t)=d', summed over every d, is at most

    M^{1−1/C+o(1)} T^{1/C}.

In particular when n≥M^{2/3+o(1)}, C<3(1−α) suffices for o(n) total error, uniformly over all bounded coefficient functions of (e,d).

## Application to one-anchor covers

For a given A, match rows to distinct target positions with the same exact core profile. There are at most M^{σ+o(1)} unmatched rows. Cover the small-prime deficits of each such row at cost at most π(y) by the nested prime-power repair lemma, and cover outside-prime deficits at cost at most the total number of distinct outside primes per row, counted across A. Thus H(A,I) ≤ n+sum_{a∈A} ω_{>y}(a)+M^{σ+o(1)}. In the remaining range M≤n^{3/2+o(1)}, any fixed 1<C<3 yields coefficient two whenever that outside-prime sum is at most n+o(n). A uniform bound on this sum is false for general A. The proved small-prime transfer cannot alone close the original conjecture.
