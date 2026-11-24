# The full-tail constraint on cold divisor multiplicities

24 November 2026. This is a proved constraint, not a closing estimate.

Let c>2, A={a<=M:X(a)>c}, n=|A|, and let every counted carrier copy be
assigned to a distinct source a in A, with h|a and h<=sqrt(M). Write

    N_d=sum_{h:d|h}m_h,
    K_tau=#{b in I:X(b)>tau},
    H_tau(y)=#{u<=y:X(u)>tau}.

For every integer d>=2 with X(d)<=c-1, the exact source-factor map gives

    N_d <= H_(c-X(d))(M/d).                            (1)

Indeed a/d is an integer at most M/d, different sources give different
quotients, and complete additivity gives

    X(a/d)=X(a)-X(d)>c-X(d)>=1.

Apply the already proved short-window hot-divisor counting lemma at the
actual threshold tau=c-X(d). Its proof applies to every positive
threshold because the strict superlevel set is closed under taking
multiples. Since M/d<=M/2,

    N_d <= 8*K_(c-X(d))^2/d^2.                        (2)

Together with distinctness and the original source length,

    N_d <= min(n, floor(M/d), 8*K_(c-X(d))^2/d^2).     (3)

This applies, in particular, to every cold divisor X(d)<=1. It does not
replace X(d) by a numerical size bound.

## Consequence for the cold part of Euler energy

Define

    G_cold=(1/M)sum_{d:X(d)<=1}phi(d)*N_d^2.

The d=1 contribution is at most n^2/M. Using (2) once and retaining the
other N_d gives the uniform inequality

    G_cold <= n^2/M
       +(8/M)sum_h m_h
          sum_{d|h,d>=2,X(d)<=1}
             [phi(d)/d^2]*K_(c-X(d))^2.               (4)

Thus the full-tail information controls cold-divisor demand through a
higher target superlevel, rather than through K_1 alone. Formula (4)
retains all actual powers and actual carrier multiplicities.

However, replacing K_(c-X(d)) by K=K_1 and using only the pointwise bounds
in (3) yields at best, by splitting d near K/sqrt(n),

    G_cold <= n^2/M + O(K^2*n/M).                      (5)

For K=O(n), the latter term has order n^3/M and need not be o(n) in the
required subquadratic sparse branch M=o(n^2). No improvement of (4) from
the original exact whole-prime rows has been proved here. Those rows
cannot silently be replaced by equalities for every divisor d or for
each separate prime power.
