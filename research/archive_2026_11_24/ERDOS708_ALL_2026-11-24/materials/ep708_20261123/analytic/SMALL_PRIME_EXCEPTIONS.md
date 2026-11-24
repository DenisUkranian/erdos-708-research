# A uniform asymptotic cover when the quotient-prime mass stays below one

## Statement and scope

Let `A subset {2,...,M}` consist of `n` distinct integers, and let `I` be any positive interval of `M` consecutive integers. For `a in A`, write

`p(a)=Pmax(a)`, `d(a)=a/p(a)`.

Let `Q` be the union of the prime divisors of the nonunit quotients `d(a)`. Fix `delta in (0,1]`, and assume

`sum_{q in Q}1/q <= 1-delta`.                                    (Q)

The small primes in `Q` need not tend to infinity.

Choose an integer `T0>=3`, depending only on `delta`, such that

`(2pi(T)+1)/T <= delta` for every real `T>=T0`.                    (T)

Such a choice exists by the elementary prime-counting estimate `pi(T)=O(T/log T)`. Put `k=#{p prime:p<T0}`.

**Finite theorem.** Under (Q), a cover of the source product exists with cardinality at most

`2n + (1+log_2 M)^(k+1)`.                                        (1)

The harmless polylogarithmic term can be replaced by the more precise

`log_2(M) product_{p<T0}(1+floor(log M/log p))`.

Together with any established polynomial long-interval theorem giving the exact bound `2n`, this proves `(2+o(1))n` uniformly over the class (Q), with `delta` fixed.

This is a restricted source-class theorem. It is not the unrestricted Erdős 708 conjecture, and it is not a statement uniform as `delta` tends to zero.

## 1. Good and bad sources

Call a source good if `T(a)=M/d(a)>=T0`; otherwise call it bad. For a bad source,

`p(a)=a/d(a)<=M/d(a)<T0`.

Thus every prime factor of a bad source is less than `T0`. Since sources are distinct, their number `b` satisfies

`b <= product_{p<T0}(1+floor(log M/log p)) <= (1+log_2 M)^k`.        (2)

This is the only place where distinctness is used to bound the exceptional class. The matching argument below also uses distinct source values to bound the sizes of quotient fibers.

## 2. Matching all good quotients

Join each good source `a` to the interval positions divisible by `d(a)`. A prime source has `d(a)=1`, so its neighborhood is all of `I`. Any Hall subset containing a prime source automatically satisfies Hall because `|A|<=M-1`.

Consider a Hall subset `S` consisting only of good composite sources, and let `D={d(a):a in S}`. Each `d in D` is `Q`-smooth. Moreover, if `a=d p(a)`, every prime factor of `d` is at most `p(a)<=M/d`; therefore

`Pmax(d)<=T=M/d`.

Let `N` be the union in `I` of multiples of members of `D`. Define

`K_D(t)=sum_{d in D}[1_{d|t}-sum_{q in Q,q<=M/d}1_{dq|t}]`.

Pointwise, `K_D(t)<=1_N(t)`. A positive summand would require

`d=smooth_{Q intersect [2,M/d]}(t)`.

As `d` increases, the right side is nonincreasing; hence at most one positive summand exists. All other summands are nonpositive. Outside `N`, every summand vanishes.

The usual interval counts of multiples give, for every `d in D`,

`sum_{t in I}[1_{d|t}-sum_{q<=T}1_{dq|t}]`

`>= T[1-sum_{q in Q,q<=T}1/q]-pi_Q(T)-1`

`>= delta T-pi(T)-1 >= pi(T)`,

where the last inequality is (T), and `T>=T0` because the sources are good. Consequently

`|N|>=sum_{d in D}pi(M/d)>=|S|`.

For the last inequality, a source with quotient `d` has the form `d p`, where `p` is a prime at most `M/d`; distinct sources give distinct such pairs. Hall's theorem therefore produces distinct interval positions covering all good quotients.

## 3. Completing the good sources

Let `g=n-b` be the number of good sources. Their matched positions form a set `B0` of size `g` whose product is divisible by the product of their quotients.

For each prime `p`, let `m_p` be the number of good sources whose largest prime is `p`. The target good-source product differs from the quotient product by exactly `m_p` additional copies of `p`. Therefore the current `p`-valuation deficit is at most `m_p`.

Whenever that valuation is still deficient, there is an unused interval multiple of `p`: the entire interval supplies at least the target valuation, because the product of distinct sources in `[1,M]` divides `M!`, and `M!` divides the product of any `M` consecutive integers. Each newly selected multiple increases the valuation by at least one. At most `m_p` additions are needed for prime `p`, and additions may help other primes too.

Since `sum_p m_p=g`, all good sources can be covered using at most `2g` interval positions.

## 4. Repairing the exceptional sources

Starting from the good-source cover, process any remaining deficient prime valuations for the full source product. The initial additional demand for prime `p` is at most `sum_{a bad}v_p(a)`. Again, an unused multiple exists whenever the full target valuation is deficient. Thus at most

`sum_{a bad}Omega(a) <= b log_2 M`

further positions are needed. Combining this with (2) gives

`tau(A,I)<=2g+b log_2 M<=2n+(1+log_2 M)^(k+1)`,

proving (1). The argument also works if one of the good or bad classes is empty. A zero-containing interval is covered by its zero element; wholly negative intervals reduce by absolute values and reversal.

## 5. The asymptotic deduction

For definiteness, use the known exact long-interval result `M>=16n^2 => tau<=2n`. In the remaining range,

`log M<=log(16)+2log n`,

so the error in (1) is `O_delta((1+log n)^(k+1))=o(n)`. This yields the asserted class-uniform asymptotic result.

The quadratic threshold is not essential: the previously established `M>=8n^3` exact theorem gives the same conclusion, because its complementary range also has `log M=O(log n)`.

The gap `delta` must remain fixed. Merely knowing `sum_{q in Q}1/q<1` separately for each member of a varying sequence does not make the error uniform if that sum approaches one.
