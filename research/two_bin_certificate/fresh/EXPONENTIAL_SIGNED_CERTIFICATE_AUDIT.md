# Exponential signed certificate: an exact calculation and its two gaps

24 November 2026. This note does not prove the aggregate hyperbolic-kernel transfer or Erdős 708.

Let `0 <= w_p <= 1`, let `X(n)=sum_p w_p v_p(n)`, and set

    F(n)=2^(-X(n)),
    P(n)=X(n)-2+2 F(n).

## 1. A pointwise target certificate

For every real `x>=0`,

    x-2+2^(1-x) <= (x-1)_+.

For `0<=x<=1`, convexity puts `2^(-x)` below the chord `1-x/2`.
For `x>=1`, use `2^(1-x)<=1`. Hence `P(n)<=(X(n)-1)_+` for every integer, with all prime powers included.

Write `P(n)=sum_{d|n} alpha_d`, so `alpha=mu*P`. For `d=p^e`,

    alpha_(p^e)=w_p-2(1-2^(-w_p))2^(-(e-1)w_p).

For `d` with at least two distinct prime factors,

    alpha_d=2 (-1)^omega(d) F(d)
                product_(p|d)(2^(w_p)-1).

Since `2^(w_p)-1<=1`, the negative mixed coefficients satisfy

    (-alpha_d)_+ <= 2 F(d).

At a prime power with `X(d)>=2`, the same bound follows immediately from the displayed single-prime formula. Consequently,

    P(d)-(-alpha_d)_+ >= X(d)-2   whenever X(d)>=2.

Thus every genuine upper-tail source individually has enough exponential reserve to pay the negative coefficient attached to that same integer.

## 2. Why this is not the missing arithmetic inequality

There are two distinct unresolved losses.

First, low-load prefix integers cannot simply be discarded from a signed divisor certificate. `P(x)<0` for `0<x<1`; even for `1<x<2`, subtracting a negative coefficient can produce a negative corrected source contribution. For three distinct primes of price `17/50`, the total load is `51/50`, and

    P(d)-(-alpha_d)_+
      = 51/50-2+2*2^(-51/50)
        -2*(1-2^(-17/50))^3 < 0.

This strict sign can be checked without floating point: `q=2^(-17/50)` lies between `79004/100000` and `79005/100000`, as follows by taking fiftieth powers and comparing with `2^(-17)`. The expression `51/50-2+2q^3-2(1-q)^3` is increasing in `q`, and its value at the latter rational endpoint is negative.

Second, the full divisor expansion has coefficients at moduli `d>M`. Their prefix counts vanish, while an actual length-M interval may contain one multiple of each. Truncating at `M` is not justified by the pointwise target bound for the infinite expansion. Positive and negative omitted terms must be controlled jointly; an absolute-value bound is not uniform in the growing active support.

For unit prices the first issue disappears, because every load is integral. In that case

    alpha_(p^e)=1-2^(1-e)>=0,
    alpha_d=2*(-1)^omega(d)*2^(-Omega(d))   (omega(d)>=2),

and `P(d)-(-alpha_d)_+ >= (Omega(d)-2)_+` for every `d`. The second, arithmetic truncation issue remains. This is not a proof even of the unrestricted unit-price interval inequality.

## 3. Relation to the new hyperbolic kernel

The kernel in `../optimality/WATERFILLING_HYPERBOLIC_CERTIFICATE.md` proves source coverage and common target-budget feasibility without these low-load pointwise failures. Its aggregate interval transfer has not been derived from the exponential calculation above. Replacing that transfer by an unproved truncation theorem would only move the gap.

No new value of `g(n)` or claimed solution follows from this note.
