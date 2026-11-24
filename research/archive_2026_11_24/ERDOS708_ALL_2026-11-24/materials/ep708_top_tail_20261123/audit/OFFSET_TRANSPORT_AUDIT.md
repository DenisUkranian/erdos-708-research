# Offset transport: the valid local injection and the remaining obstruction

## Status

This note audits the proposed cofactor-bank transport step. It proves the local injection for distinct cofactors and gives an exact counterexample to the half-radius Hall inference for repeated cofactors. The example preserves an actual interval, distinct sources, a common bank target, the canonical top-source set, high source loads, and the proposed prime-fibre bound.

It is **not** a counterexample to the full adaptive cofactor route, a fractional cofactor-product cover, the coefficient-two bound, or J_weak. The displayed weights are explicitly not an optimal dual. No search or computation of g(n) is used.

## 1. The distinct-cofactor transport lemma

Let I=[ell,r] be an integer interval of length M and let b0 belong to I. Let D be a set of distinct positive integers, each dividing b0 and satisfying d<=floor(M/2).

There is an injective assignment

    d -> b0+epsilon*d in I\{b0},

where one common sign epsilon can be used for all d.

Indeed the longer side of b0 has length

    max(b0-ell,r-b0)>=floor(M/2).

Choose its sign. Every indicated target lies on that side, is a multiple of d, and has a distinct distance d from b0. Thus one source per distinct cofactor can be moved away from the common target. The target b0 itself can additionally serve one more source if desired.

This lemma does not assign one target per occurrence of a repeated cofactor. The following example shows that the fibre bounds alone do not supply that missing conclusion after the proposed safe truncation of offsets.

## 2. An exact half-radius counterexample

Take

    M=30,  I={360,361,...,389},  b0=360,
    w_2=w_3=w_5=1,

with every other weight zero. Choose the sources and their deleted prime units as follows.

| Source a | Deleted prime q | Cofactor d=a/q |
|---:|---:|---:|
| 16 | 2 | 8 |
| 24 | 3 | 8 |
| 18 | 2 | 9 |
| 27 | 3 | 9 |
| 20 | 2 | 10 |
| 30 | 3 | 10 |

All six sources are distinct, their maximum is M, and 2n<M<16n^2 for n=6. The three cofactors divide b0.

For each d in {8,9,10}, the fibre contains two distinct sources and satisfies the proposed prime-scarcity constraint exactly:

    r_d=2=pi(M/d).

Here pi(T) counts primes at most the real number T. The only possible deleted primes in each displayed fibre are 2 and 3.

Nevertheless, restricting transports to

    |b-b0|<=M/2=15

leaves only the four available bank targets

    {360,368,369,370}.

There are no negative offsets, because b0 is the left endpoint of I. For d=8,9,10 the only positive multiple of d at most 15 is d itself. Thus the six-source Hall condition fails in the truncated transport graph, even if b0 is retained as an extra shared target.

The still narrower rule using offsets k*d with k<=q/2 fails for the same reason: q is 2 or 3, so its only positive integral choice is k=1.

### The top-source and high-load conditions are retained

For these weights, the largest source loads below M are

    X(16)=X(24)=4,

followed by load three at 8,12,18,20,27,30. Therefore

    A={16,18,20,24,27,30}

is precisely the canonical forced-M top-six set when equal loads are ordered by decreasing integer value. Every selected source has X(a)>=3>2.

Thus neither top-source selection nor high source loads repair this particular half-radius Hall inference.

## 3. Why the example does not refute the full two-stage route

The discarded longer-side positions immediately repair the matching. The following six actual targets are distinct:

| Source a | Cofactor d | Assigned target b |
|---:|---:|---:|
| 16 | 8 | 368 |
| 24 | 8 | 376 |
| 18 | 9 | 369 |
| 27 | 9 | 378 |
| 20 | 10 | 370 |
| 30 | 10 | 380 |

Each target belongs to I and is divisible by its assigned cofactor. Hence the full cofactor stage succeeds in this instance. The failed inference concerns only the restriction to offsets of radius M/2, or the stronger k<=q/2 restriction; it does not show that an augmenting argument using the whole interval must fail.

The displayed weights also fail the active-row optimality equations. Their source demand at 2 is

    D_2(A)=4+1+2+3+0+1=11.

But 360,368,384 are all hot targets and have total 2-adic valuation

    v_2(360)+v_2(368)+v_2(384)=3+4+7=14>11.

Complementary slackness would select all three with mass one, contradicting an active 2-row equality. Thus this is not a balanced optimal/minimal-obstruction instance. That missing hypothesis is stated explicitly, rather than silently attributed to the top-source property.

## 4. What still requires a global argument

With the full interval retained, the fibres can collide at positions

    b0+k*d=b0+l*e.

The local bounds r_d<=pi(M/d) do not by themselves count those shared positions. The distinct-cofactor lemma handles one occurrence per d. It does not show that the remaining fibre occurrences can be augmented simultaneously, nor that a connected overlap cluster has one common bank target.

The full proposed fractional stage is weaker than a one-source/one-target matching. It asks for one shared choice of target masses that covers the aggregate cofactor valuations. A matching obstruction alone therefore would not disprove that fractional stage.

One precise relaxed formulation allows, for each source a, fractional deletion credits alpha_{a,p}>=0 with sum_{p|a}alpha_{a,p}=1. Its seed-cover LP is

    minimize sum_{b in I}z_b
    subject to 0<=z_b<=1,
       sum_b z_b v_p(b)+sum_{a:p|a}alpha_{a,p}>=D_p(A).

Its exact dual objective is

    sum_{a in A}[X_w(a)-max_{p|a}w_p]
       -sum_{b in I}(X_w(b)-1)_+.

The subtraction of the maximum price is the dual effect of choosing which prime unit to remove. Proving that this seed LP is at most n+o(n) would be a sufficient further result; it has not been proved here. The common-target injection and the example above neither establish nor refute it.

## Conclusion

The distinct-cofactor transport is valid. The safe half-radius extension to repeated fibres is false, even for a canonical high-load top set with exact prime-fibre bounds. Restoring the full interval repairs the exhibited example, so the unrestricted adaptive/fractional two-stage route remains open. No asymptotic coefficient-two conclusion is claimed.
