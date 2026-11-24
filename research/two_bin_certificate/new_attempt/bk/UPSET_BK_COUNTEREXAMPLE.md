# A genuine arithmetic obstruction to BK for arbitrary divisibility upsets

24 November 2026. This disproves the proposed enlargement to arbitrary
divisibility-upward sets. It does NOT disprove the conjecture restricted
to one additive threshold D={t:X_w(t)>1}, and it is NOT a counterexample
to Erdős 708 or to a genuine full-tail optimum.

## Statement

There is no absolute C such that every divisibility-upward set D of
positive integers and every actual M-term positive interval I satisfy

    #{a<=M:a=hk with h,k in D} <= C |D intersect I|^2/M + O(1).

In fact there are examples with K=|D intersect I|=o(M), K^2/M tending
to infinity, and the ratio of the left side to K^2/M tending to infinity.

## Parameters and the actual set

Let rho denote the Dickman function. Let the integer u tend to infinity,
and put

    y=ceil(1/rho(u+1)), x=y^u, M=2yx.

Let S be the set of all y-smooth integers in (x,2x]. Define D to be the
upward closure under divisibility of {y} union S. Thus

    t in D iff y divides t or some s in S divides t.

Let L be a positive common multiple of all these finitely many
generators, chosen larger than yx. Take the actual interval

    I={L-yx+1,...,L+yx}.

Every source y*s with s in S is at most M and is the product of two
members of D. These sources are distinct, including when y and s have
common primes. Hence

    E(M) >= |S| = Psi(2x,y)-Psi(x,y).                  (1)

For a nonzero offset t, membership of L+t in D is equivalent to
membership of |t| in D. If 1<=t<=yx and s in S divides t, then
t/s<y. Both s and t/s have all prime factors at most y, so t is
y-smooth. It follows that

    K <= 2x + 2 Psi(yx,y) + 1.                        (2)

The first term counts multiples of y; the last term covers offset zero.
The interval contains exactly M/y=2x multiples of y, so also K>=2x.

## Verified standard smooth-number input

The uniform Hildebrand estimate gives

    Psi(z,y)=z rho(log z/log y)
              [1+O(log(1+log z/log y)/log y)]

for 1<=log z/log y<=exp((log y)^(3/5-epsilon)).
See Hildebrand--Tenenbaum, *Integers without large prime factors*,
Theorem 1.1 and equation (1.8):
https://jtnb.centre-mersenne.org/article/JTNB_1993__5_2_411_0.pdf

The same source's Corollary 1.7 gives
Psi(2x,y)/Psi(x,y)=2^(alpha(x,y))(1+o(1)); its equation (1.26)
implies alpha(x,y)->1 in the present range.

For completeness, the elementary Dickman identity

    (u+1)rho(u+1)=integral_u^(u+1) rho(t) dt <= rho(u) (3)

implies rho(u+1)<=1/(u+1)! at integer arguments. Hence
log y >= log((u+1)!), so the stated uniform range applies, and
log u/log y ->0. Also y rho(u+1)->1. Therefore

    Psi(yx,y)=(1+o(1))yx rho(u+1)=(1+o(1))x,
    Psi(2x,y)-Psi(x,y)=(1+o(1))x rho(u).              (4)

The assertion alpha->1 used above follows directly from the cited
estimate: log x=u log y, while
(log u+log log y)/log y ->0.

## Diverging violation

Combining (1)--(4),

    K <= (4+o(1))x,
    E(M) >= (1+o(1))x rho(u),

and consequently

    E(M) M/K^2 >= (1+o(1)) y rho(u)/8
                >= (1+o(1))(u+1)/8 -> infinity.      (5)

Moreover K/M=O(1/y)->0, and K^2/M>=2x/y=2y^(u-1)->infinity,
so an absolute additive O(1) cannot repair the bound.

## Scope: why this does not yet refute the weighted-threshold claim

This D is an OR of two different hot mechanisms: the small generator y
and large smooth generators. It has not been represented as a single
additive halfspace X_w>1 with all 0<=w_p<=1.

Assigning logarithmic weights log p/log x to p<=y makes the large smooth
generators hot but leaves X(y)=1/u. Raising prices on factors of y to
make y hot also creates mixed hot divisors. Those mixed divisors produce
additional target banks and invalidate the small K calculation for the
new threshold set. They cannot be omitted.

Thus any proof of the proposed bound for X_w must use the additive
threshold structure, rather than only divisibility closure, saturation
of all hot banks, and actual numerical interval laws. The latter
properties all hold in the counterexample above.

## Further warning: even linear one-level prefix comparison fails

One cannot first prove # {a<=M:X(a)>1} <= C K and then apply a prefix BK
bound. Take all active primes in (sqrt(M/2),sqrt(M)], each of weight
3/5, and center I at a sufficiently highly divisible common multiple.
Every nonzero offset of magnitude at most M/2 contains at most one
active occurrence, so K=1 (only the center is hot). The source prefix
contains an unbounded number of hot products of two such primes.
There are no two-hot-factor source products here, since four active
occurrences already have product greater than M. This is a real
additive-threshold counterexample to the one-level comparison only.
