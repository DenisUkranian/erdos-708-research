# Exact gcd accounting and a local cold-overlap obstruction

24 November 2026. These are proved identities and a local arithmetic
obstruction. They do not give the needed global bound at a genuine
positive optimum.

## 1. The extra constraint from distinct actual sources

Suppose each of n distinct sources a<=M is assigned at most one carrier
h(a)|a, with h(a)<=sqrt(M). Let m_h count the assigned copies. Define

    N_d=sum_{h:d|h}m_h.

Because these copies come from distinct sources divisible by d,

    N_d<=min(n,floor(M/d)).

The standard divisor identity gcd(h,k)=sum_{d|h,d|k}phi(d) gives exactly

    G=(1/M)sum_{h,k}m_h*m_k*gcd(h,k)
     =(1/M)sum_d phi(d)*N_d^2.

Consequently

    G<=sum_h m_h sum_{d|h}phi(d)/d
      =sum_h m_h product_{p^e||h}[1+e(1-1/p)].

This last upper bound is not the required o(n) estimate or a bound with
the required leading coefficient. Whole-prime row balances do not by
themselves turn the numerical divisor weight phi(d) into the load X(d).
The assumption of at most one assigned carrier per distinct source is
essential for the displayed N_d constraint as stated.

## 2. Pairwise cold gcds do not justify simultaneous payment

Give the six primes 2,3,5,7,11,13 weight 3/5, and all other primes weight
zero. Let H be the 15 products of two distinct listed primes, and let

    b=2*3*5*7*11*13=30030, M=30030.

Every h in H is hot, with X(h)-1=1/5. Every gcd of two distinct members
of H is either 1 or a single listed prime, and hence has load <=3/5<1.
All the carriers obey h<=143<sqrt(M).

Nevertheless, at the actual integer b,

    sum_{h in H}(X(h)-1)=15/5=3,
    X(b)-1=18/5-1=13/5<3.

These carriers can be attached to 15 distinct actual tail sources:
take a_h=h^2<=143^2<M. Every a_h has X(a_h)=12/5>2+1/10.
Thus the example does not use formal unattainable incidence profiles.
It is a pointwise obstruction to the proposed joint payment rule; it is
not an extremal full-tail example, does not assert optimal row balances,
and is not a counterexample to the Erdős 708 asymptotic.

## 3. The exact multiway replacement

For any ordered family h_1,...,h_r dividing b, let

    L_j=lcm(h_1,...,h_j).

Additivity over prime powers gives the exact telescoping identity

    sum_{j=1}^r[X(h_j)-1]
      =X(L_r)-1
       +sum_{j=2}^r[X(gcd(h_j,L_{j-1}))-1].

In particular, if every successive gcd with the accumulated lcm is
cold, the total payment is at most X(b)-1. Coldness of all pairwise
gcds is weaker and, by Section 2, does not suffice. This identity retains
every prime power and identifies the precise additional overlap term
that a cluster argument would have to pay.

No general bound on that additional term, or on G sufficient for the
sparse subquadratic branch at genuine positive global extrema, was
obtained.
