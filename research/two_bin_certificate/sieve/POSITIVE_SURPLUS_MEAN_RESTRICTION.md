# A sharper necessary mean restriction for positive raw surplus

24 November 2026. This is a proved general restriction, not the missing arithmetic transfer theorem.

Let 0<=w_p<=1 for p<=M, set X(a)=sum_p w_p v_p(a), and let I be any positive interval of length M. For c>=2 write

    J_c=sum_{a<=M}(X(a)-c)_+ - sum_{b in I}(X(b)-1)_+.

Put

    mu=sum_p w_p/(p-1),
    e=mu-(1/M)sum_{a<=M}X(a),
    nu=sum_p w_p^2*p/(p-1)^2.

The usual exact prime-power expansion gives e>=0 and

    E_prefix X^2 <= mu^2+nu <= mu^2+2mu.

Furthermore e=O(1/log M) uniformly, by counting the distinct prime powers <=M and bounding the omitted geometric tails.

## 1. Universal positive-surplus gate

For every real x>=0 and 0<=a<=1,

    min(x,2) >= a*x-a^2*x^2/8.                         (1)

Indeed, for x<=2 the right side is at most ax<=x; for x>=2 its maximum over all real x is 2.

Suppose mu>=2 and choose a=4/(mu+2)<=1. Averaging (1) yields

    E min(X,2)
      >= 4(mu-e)/(mu+2)
           -2(mu^2+2mu)/(mu+2)^2
       = (2mu-4e)/(mu+2).                             (2)

Every prime-power occurs at least as often in I as in [1,M]. Hence

    J_c <= J_2
        <= M - sum_{a<=M}min(X(a),2).                (3)

If mu>=2+4e, the right side of (2) is at least one, and (3) gives J_c<=0. Consequently

    J_c>0  ==>  mu<2+4e = 2+O(1/log M).              (4)

This does not need global optimality, a bound on support size, or restrictions on powers, density, or shift. It improves the previously used coarse necessary bound mu=O_c(1).

## 2. A variance-sensitive form

Keeping nu rather than replacing it by 2mu gives, for every 0<=a<=1,

    J_c/M <= 1-a(mu-e)+a^2(mu^2+nu)/8.               (5)

Thus a positive surplus forces the right side of (5) to be positive for every such a. The best admissible choice is

    a=min(1,4(mu-e)/(mu^2+nu)).

In particular the simple choice a=1 implies the necessary inequality

    nu > 8(mu-e-1)-mu^2.                             (6)

If all active primes tend to infinity in a sequence, then nu<=(1+o(1))mu. Equations (5)--(6), together with the optimized a for mu>=3, imply

    J_c>0 ==> mu <= (7-sqrt(17))/2+o(1)
                    = 1.438447187...+o(1).          (7)

For completeness, on bounded mu<3 the quadratic 1-mu+(mu^2+mu)/8 is negative precisely between the two roots (7+-sqrt(17))/2. On mu>=3 choose a=4/(mu+1)<=1; (5) then bounds E min(X,2) below by 2mu/(mu+1)+o(1)>1. Very large mu is already excluded by (4).

## Scope

The estimate controls the first two prefix moments. It does not compare the actual-size hyperbolic kernel between intervals, does not turn rowwise union discrepancy into a common target budget, and does not prove g(n)<=(2+o(1))n.
