# What the difference-product bound supplies, and what it does not

Let B be a set of K distinct selected target positions in an interval of length M. For every prime p and exponent j put k_(p,j)=#{b in B:p^j|b}. Exactly,

    sum_(p,j) binom(k_(p,j),2) log p
       = sum_(b<b' in B) log gcd(b,b')
       <= sum_(b<b') log|b-b'|
       <= binom(K,2) log(M-1).

This remains valid when only active primes are retained on the left.

At an original paired optimum, integer selected positions satisfy only the whole-row identities

    D_p(B)=sum_j k_(p,j)=D_p(A)-e_p,

where e_p is the nonnegative integer residual from fractional coordinates. Source counts at individual prime-power levels cannot replace k_(p,j).

After the actual finite-phase normalization, let L_p bound target exponents. Cauchy gives

    sum_j binom(k_(p,j),2)
       >= D_p(B)^2/(2L_p)-D_p(B)/2.

This is a lower-capacity constraint. Increasing K enlarges the allowable difference-product budget; the resulting inequality does not furnish the desired upper bound K<=2n.

More concretely, D_p(B)<=D_p(A)<=nL_p and

    sum_p D_p(A)log p <= n log M.

Therefore the positive quadratic part of this row-total lower bound is at most

    (n/2) sum_p D_p(A)log p <= (n²/2)log M.

For K>=2n, the available right-hand side is already approximately 2n² log M. Thus this particular lower bound has a factor-four scale gap before the negative linear term is subtracted. It cannot contradict K>2n.

This does not rule out a stronger argument exploiting forced banks, actual residue restrictions, or cross-row structure. It identifies precisely why inserting exact whole-row demands into a standard Vandermonde inequality is insufficient.

Ordinary prime-modulus larger sieve also needs additional information: a hot composite root excludes a joint zero pattern from the cold complement, not necessarily a nontrivial proportion of residue classes modulo any one prime. Replacing that joint restriction by independent prime residue exclusions is invalid.

No square-root bound for the global surplus is obtained from this argument.
