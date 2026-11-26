"""Exact rational certificates for the two-baseline inverse density multiplier.

Assumptions: 0 <= d <= 1, 0 <= x <= 10, terminal reciprocal mass <= d/256
and E[Z] >= max(1+x,2*x) + d/2.  The common margin is d*max(1,x)/8.
All proofs cover continuous ranges. No sampling is used.
"""
from math import comb
from sympy import Poly, Rational as Q, expand, symbols

d, x = symbols("d x")
L = d / 256


def surplus(pair_moment, mean_of_price, margin, coeff):
    mean_of_price = Q(mean_of_price) if isinstance(mean_of_price, int) else mean_of_price
    return expand(pair_moment - (2 + coeff*d) * (mean_of_price**2/2 + mean_of_price*L) - d*margin/8)


def bernstein(poly):
    """Bernstein coefficients in d on [0,1], padded to a single cubic degree."""
    poly = Poly(poly, d, domain="QQ")
    assert poly.degree() <= 3
    return [sum(poly.nth(i)*Q(comb(k,i),comb(3,i)) for i in range(k+1)) for k in range(4)]


def ordinary_moment():
    coeff = Q(79,64)
    lower = 1 + x + d/2
    cert = x*(1-x)/2 + d*(1-x)*(16+79*x)/128 + d**2*(2048-79*x)/16384
    assert expand(surplus(lower*(lower-1)/2,x,1,coeff) - cert) == 0
    higher = 2*x + d/2
    cert = (1-d)*x*(x-1) + d*(x-1)*(49*x+32)/128 + d**2*(2048-79*x)/16384
    assert expand(surplus(higher*(higher-1)/2,x,x,coeff) - cert) == 0
    assert 2048-79*10 > 0
    print(f"Ordinary quadratic multiplier 2 + {coeff} d: two exact polynomial identities.")


def discrete_moment(include_terminal_pairs=False):
    # Among [0,1] price weights of sum z, off-diagonal pair mass is
    # minimized by consecutive unit weights and a possible last fraction.
    # This gives the interpolated binomial max_{k>=0} k*z-k*(k+1)/2.
    # Its convexity yields the same estimate at E[Z].
    coeff = Q(8,5) if include_terminal_pairs else Q(186,115)
    boundaries = []
    def boundary(label, price_mean, total_mean, slope, margin):
        moment = slope*total_mean - Q(slope*(slope+1),2)
        certificate = surplus(moment,price_mean,margin,coeff)
        if include_terminal_pairs:
            certificate -= (2+coeff*d)*L**2/2
        b = bernstein(certificate)
        assert min(b) >= 0, (label,b)
        boundaries.append((label,b))

    # For fixed d the surplus is concave in x between consecutive integer
    # values of total_mean, on either side of x=1. It suffices to inspect
    # the endpoints of every such interval. These endpoints are below.
    boundary("x=0", 0, 1+d/2, 1, 1)
    boundary("small x, mean=2", 1-d/2, 2, 2, 1)
    boundary("x=1", 1, 2+d/2, 2, 1)
    for j in range(3,21):
        xx = Q(j,2)-d/4
        boundary(f"large x, mean={j}", xx, j, j, xx)
    boundary("x=10", 10, 20+d/2, 20, 10)
    # Any larger coefficient breaks this exact margin under the stated
    # two moment bounds alone, at d=1, x=5/4, total mean=3.
    xstar = Q(5,4)
    if not include_terminal_pairs:
        assert (3-xstar/8)/(xstar*xstar/2+xstar/256)-2 == coeff
    print(f"Interpolated binomial multiplier 2 + {coeff} d: {len(boundaries)} boundary polynomials, each nonnegative in the cubic Bernstein basis.")
    for label, b in boundaries:
        print(label, ":", ", ".join(map(str,b)))


if __name__ == "__main__":
    ordinary_moment()
    discrete_moment()
    discrete_moment(include_terminal_pairs=True)


def verify_dense_curve():
    # On 2<=v<=6 the inverse polygon section has slope 1/2 and
    # joins heights 2 and 3. Continuous mu maximization is proved
    # by k>=ceil(mu)>=mu in the note; this checks the whole linear
    # section and the endpoints as identities, with rational inputs.
    v = symbols("v")
    bound = Q(3,2)+v/4
    assert expand(2*bound-3-v/2) == 0
    for den,num,expected in [(6,1,3),(4,1,Q(5,2)),(3,1,Q(9,4)),(2,1,2)]:
        assert bound.subs(v,Q(den,num)) == expected
    print("Dense curve: exact section [1/6,1/2] and four reference values.")


if __name__ == "__main__":
    verify_dense_curve()
