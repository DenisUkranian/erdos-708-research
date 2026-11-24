# A sparse family of minimal hot roots can have linear union-transfer error

## What this disproves

The following proposed intermediate inference is false:

> In the full-tail setting, `K=O(n)` and `o(n)` small minimal hot roots of
> bounded multiplicative degree force an `o(n)` error when their union of
> multiples is transferred from the prefix to an arbitrary interval.

The example below also has bounded reciprocal weighted mean, a source-prime
bound `p=O(n)`, `r=O(n/log n)`, and uniform source exponential tails. Thus those
normalizations do not repair the inference. It remains essential to use the
adaptive carrier options and/or true optimizer balances.

This is **not** a counterexample to Erdős 708, to the unrestricted hinge
asymptotic, to the adaptive Hall conjecture, or to a lemma explicitly requiring
genuine global optimality. The last section proves that the active 2-row cannot
be tight: true optimizer balances genuinely exclude this construction.

## Construction

Let `N` tend to infinity, set `M=2N`, and choose

    c=21/10,
    w_2=3/5,
    w_p=1    for primes sqrt(N)<p<=N/2,
    w_p=0    for all other primes.

Let `X` be the raw additive load and take the actual full strict tail

    A={a<=M:X(a)>c},       n=|A|.

Every multiple of 16 lies in `A`, since its 2-adic contribution is at least
`12/5>21/10`. Therefore

    M/16-O(1) <= n <= M.                                 (1)

Every indicated external prime is genuinely used by this tail: `4p<=2N=M`
and

    X(4p)=6/5+1=11/5>21/10.                              (2)

For every such prime put `d_p=2p`. These are minimal hot roots:

    X(d_p)=8/5>1,

while their proper divisors 1, 2, and `p` have load at most 1. In particular
their overshoot is the fixed number `3/5`, and `Omega(d_p)=2`.

Their number `H` satisfies

    H=O(N/log N)=o(n),

and their maximum is at most `N<=8n+O(1)`. Hence for any fixed `B>8` they all
belong to the family of hot roots below `Bn`, for sufficiently large `N`.

## Prefix union

Let

    U_0=#{a<=2N : 2p|a for some sqrt(N)<p<=N/2}.

Dividing even integers by 2 converts this to the union of the corresponding
prime banks on `[1,N]`. No integer at most `N` is divisible by two distinct
such primes, so these banks are disjoint. Thus

    U_0=sum_{sqrt(N)<p<=N/2} floor(N/p)
       =N sum_{sqrt(N)<p<=N/2} 1/p + O(pi(N/2))
       =(log 2+o(1))N.                                  (3)

Here the last line uses the standard reciprocal-prime asymptotic and
`pi(N)=O(N/log N)`.

## An actual shifted interval with a smaller union

Put `Q=product_{sqrt(N)<p<=N/2}p`. For a nonnegative integer `C`, consider

    I_C={2C+1,...,2C+2N}.

Its even members, divided by 2, are exactly `C+1,...,C+N`. For uniform `C`
modulo `Q`, each one of these quotient positions avoids all the indicated
primes with probability

    V_N=product_{sqrt(N)<p<=N/2}(1-1/p)=1/2+o(1).          (4)

The error in replacing the logarithm of the product by minus the reciprocal
sum tends to zero because the smallest prime tends to infinity. Consequently

    E_C #{b in I_C: d_p|b for some p}
         =N(1-V_N)=(1/2+o(1))N.                          (5)

There is an actual residue `C` at which the target union is no greater than
this mean; adding a multiple of `Q` makes `C` positive if desired. By (3)--(5)
the union discrepancy is at least

    (log 2-1/2+o(1))N,                                   (6)

which is `Omega(n)` by (1). This is a discrepancy for actual integer
divisibility in an actual interval, not an arbitrary incidence construction.

## The usual weaker normalizations all hold

For every shift, the number of hot target positions satisfies the automatic
bound

    K<=M<=16n+O(1).                                      (7)

All source primes are either 2 or at most `N/2`, and so are `O(n)`. Their number
is `O(n/log n)`. The reciprocal weighted mean tends to

    3/5+log 2.

The source exponential-tail bound also holds with absolute constants. On the
prefix `[1,2N]`, at most two external prime occurrences are possible once `N`
is large, since three of them have product greater than `N^(3/2)>2N`.
Thus

    X(a) <= (3/5)v_2(a)+2.

For any fixed `0<alpha<(5/3)log 2`, the prefix average of `exp(alpha X)` is
uniformly bounded by a geometric series. Since `n` is a fixed positive
fraction of `M`, its full-tail sum is `O(n)` as well.

The construction therefore survives adding `K=O(n)`, an active support bound,
bounded source moments, and bounded multiplicative degree to a fixed-union
transfer claim.

## Why this does not refute the desired result

The adaptive graph retains additional carriers. In particular, the small hot
root `4` is present: `X(4)=6/5`, and it can handle the sources `4p` through a
cold complement of load 1. The full family has these and further alternatives;
it is not legitimate to force every source through `2p`.

In fact one can prove that this construction is not a genuine global optimizer,
independently of the chosen shift. The calculation was identified independently
by the parent audit and checked against the exact source classification.

For large `N`, the full tail consists exactly of:

* all sources with `v_2(a)>=4`;
* sources with `v_2(a)=2` or `3` containing one external prime occurrence.

There cannot be a further source with two external prime occurrences and a
factor 2, since its value would exceed `2N`; without the factor 2 its load is
only 2. Three external occurrences also have product greater than `2N`.

The first class contributes `(5/8+o(1))N` to the raw source demand `D_2(A)`.
The exact-2-adic-valuation classes contribute, respectively,
`(1/2 log 2+o(1))N` and `(3/8 log 2+o(1))N`. Thus

    D_2(A) = [5/8+(7/8)log 2+o(1)]N
           = [1.2315...+o(1)]N.                          (8)

On the target, **every** multiple of 4 is hot because its 2-adic load is at
least `6/5`. Any paired primal cover satisfying hot saturation must therefore
have 2-row supply at least

    sum_{b in I,4|b} v_2(b)
      >= 2 floor(M/4)+sum_{j>=3} floor(M/2^j)
      = (3/2+o(1))N.                                    (9)

The target supply exceeds (8) by a fixed positive multiple of `N`. Since
`w_2=3/5>0`, this contradicts the required tight active 2-row at a genuine
optimizer. Equivalently, the derivative of `J_c` in the 2-coordinate is
strictly negative, so lowering that coordinate improves the objective.

Any successful proof must therefore exploit the adaptive alternatives and/or
the genuinely stronger exact row equations. The correct next step is the
adaptive Hall/capacity cut in `ADAPTIVE_HALL_LADDER.md`, not a uniform relative
union comparison for every sparse subfamily of minimal hot roots.
