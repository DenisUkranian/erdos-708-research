# An actual E-free source family without a globally acyclic hot-root cover

24 November 2026. This is a local arithmetic obstruction to a universal root-selection lemma. It is **not** asserted to arise at a positive global optimum, and it does not refute Erdős 708 or a selection theorem restricted to genuine positive global extrema.

## 1. Actual integers and prices

Choose ten distinct primes p_1,...,p_10 and a further prime r. Give the ten heavy primes price 2/5, give r price 1/5, and give every other prime price zero. Set c=21/10. For every five-element subset S of {1,...,10}, take

    a_S=r*product_{i in S}p_i.

There are binom(10,5)=252 distinct source integers, and each has load 11/5>c. One may take M=r*product_{i=1}^{10}p_i, so every source is at most M. For a completely explicit instance, use heavy primes 2,3,5,7,11,13,17,19,23,29 and r=31. Then M=200,560,490,130 and even every three-heavy-prime root is below sqrt(M).

Every hot divisor of a_S contains at least three heavy primes: two heavy primes plus r have load exactly one. Thus a_S cannot be split into two hot factors, since such a split would require at least six heavy occurrences. These are E-free sources. The inclusion-minimal hot divisors are exactly the three-heavy-prime products, each of load 6/5; their complementary cofactors in a_S have load exactly one.

## 2. The proposed global acyclicity condition

Suppose a family of hot roots h_1,...,h_l covers every source in the sense that each a_S is divisible by at least one h_j. Suppose the roots can be ordered so that

    X(gcd(h_j,lcm(h_1,...,h_{j-1}))) <= 1    for every j>=2.    (1)

Only roots which divide some source matter; discard the others. Each remaining root contains a three-heavy-prime subroot. Replace each root by one such subroot. Coverage is retained. Condition (1) is retained too, since each new root and each accumulated least common multiple can only shrink under divisibility.

We have therefore obtained a covering family of triples of the ten heavy coordinates satisfying (1). For such triples, condition (1) says that every triple after the first introduces a coordinate absent from all preceding triples. A completely repeated triple, in particular, is impossible. The family has at most

    1+(10-3)=8

triples.

## 3. Eight triples cannot cover all five-element subsets

Let F be any family of at most eight triples on ten vertices. Include every vertex in a random set R independently with probability 2/3. Remove one vertex from each triple of F that is contained in R. The remaining set is independent in F, and its expected size is at least

    E|R| - E[number of contained triples]
       >= 20/3 - 8*(2/3)^3
        = 116/27 > 4.

Some independent set therefore has at least five vertices. Any five-element subset S of that set contains no triple of F, contradicting the claimed coverage of a_S.

Consequently no family of hot roots satisfying the global successive-cold-gcd condition can cover all 252 sources.

## 4. What this does and does not exclude

The exact multiple-overlap payment identity involves gcd(h_j,lcm of preceding roots), so (1) would have been a convenient sufficient rule for avoiding overlap payments. This example excludes deducing a universal global rule of that form solely from the E-free property, cold cofactors, or bounded heavy occurrence count.

It does not exclude a target-dependent acyclic assignment, a weighted allocation which pays some cycles from other reserve, or a global selection theorem using additional consequences of genuine extremal optimality. The chosen weights have not been shown to be a positive global optimum for any interval. No new asymptotic bound is claimed.
