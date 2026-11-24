# A linear counterexample to the proposed one-prime Selberg bridge

## Status

The auxiliary comparison proposed for the standard Selberg denominator is false by a positive multiple of the interval length, even when the sieving primes have bounded reciprocal sum. The counterexample uses classical semismooth-number asymptotics, with the relevant primary statements checked below.

This does **not** refute the original two-level question

    #{a<=N:Omega_Q(a)>=2}
        <= #{b in J:Omega_Q(b)>=1}+o(N),                 (T)

uniformly in Q and the N-term interval J. No interval with a linear violation of (T) is constructed here. The original question, and the general Erdős 708 estimate, remain unresolved in this work.

## 1. The proposed sufficient comparison

For a finite prime set Q, put

    G_Q(R)=sum_{d<=R, d squarefree, p|d => p in Q}1/phi(d),
    F_Q(N)=#{a<=N:Omega_Q(a)<=1}.

The suggested bridge was

    F_Q(N)>=N/G_Q(R)-o(N)                               (B)

uniformly in Q, for R=sqrt(N)/L(N), where log L(N)=o(log N). Combined with an appropriate Selberg upper bound for Q-rough target positions, (B) would have implied (T).

We disprove (B). In particular, a sieve upper bound is not treated as an attained count for an actual interval.

## 2. A fixed-power tail of the primes

Fix a real u>2, let y=N^{1/u}, and take

    Q_N={p prime:y<p<=N}.

Its reciprocal sum tends to log u, a fixed finite constant. An integer counted by F_{Q_N}(N) is y-smooth, or it has exactly one prime occurrence greater than y and all remaining factors are y-smooth. Consequently the exact identity is

    F_{Q_N}(N)=Psi(N,y)+sum_{y<p<=N}Psi(N/p,y).           (1)

A repeated prime p>y is excluded, as it should be: the cofactor in the sum is y-smooth. No ambiguity about distinct versus repeated prime factors occurs.

Let rho be the Dickman function. For each fixed u, classical smooth and semismooth asymptotics give

    F_{Q_N}(N)/N -> f(u),
    f(u)=rho(u)+integral_0^{u-1} rho(v)/(u-v) dv.         (2)

Here is a precise way to handle the endpoint in (1). Apply the fixed-power semismooth asymptotic to primes at most N^{1-1/u}; its upper exponent is strictly below one. For larger primes, N/p<y, so Psi(N/p,y)=floor(N/p) exactly. The sum of the floor errors is at most pi(N)=o(N), and the reciprocal-prime sum has the usual logarithmic limit. This supplies the remaining integral up to exponent one. Thus no theorem requiring an upper exponent less than one is applied directly at an excluded endpoint.

In exponent coordinates, the integral before changing variables is

    integral_{1/u}^1 rho(u(1-t)) dt/t;

substituting v=u(1-t) yields (2).

## 3. The Selberg denominator has the wrong size for this comparison

Every divisor counted in G_{Q_N}(R) uses only primes between y and R. Dropping the restriction d<=R gives the exact upper bound

    G_{Q_N}(R)
      <= product_{y<p<=R}(1+1/(p-1))
       = product_{y<p<=R}(1-1/p)^{-1}.

Mertens' product estimate and log R/log N ->1/2 imply

    limsup G_{Q_N}(R)<=u/2,
    liminf 1/G_{Q_N}(R)>=2/u.                           (3)

An asymptotic evaluation of the restricted divisor sum is unnecessary. The elementary Euler-product upper bound already suffices to refute (B).

## 4. A rigorous strict gap; u=100 suffices

The standard Dickman identities are

    integral_0^infinity rho(v) dv=e^gamma,
    integral_0^infinity v rho(v) dv=e^gamma,
    rho(v)<=1/floor(v)!.

The second identity also follows directly from

    v rho(v)=integral_{max(0,v-1)}^v rho(t)dt

by integration and Tonelli's theorem. The factorial bound follows by iterating rho(v)<=rho(v-1)/v.

Split the integral in u f(u) at u/2. For 0<=v<=u/2,

    u/(u-v)<=1+2v/u.

For u/2<=v<=u-1 the ratio is at most u. Therefore

    u f(u)
      <=(1+2/u)e^gamma
         +u integral_{u/2}^infinity rho(v)dv+u rho(u).   (4)

At u=100 this gives

    100 f(100)
      <=(51/50)e^gamma+200/50!+100/100!
       <1.84.                                          (5)

For example, e^gamma<1.8 already suffices for the displayed strict numerical bound; it follows from the elementary upper estimate gamma<H_100-log 100. No numerical quadrature of rho is used.

Combining (2), (3), and (5), we obtain

    limsup F_{Q_N}(N)/N <0.0184,
    liminf 1/G_{Q_N}(R)>=0.02.

Hence the difference N/G_{Q_N}(R)-F_{Q_N}(N) is bounded below by a fixed positive multiple of N for all sufficiently large N. The o(N) error in (B) cannot absorb it.

More conceptually, letting u tend to infinity only after the fixed-u asymptotic in N, equation (4) and dominated convergence give

    u f(u)->e^gamma<2,

whereas the simple denominator bound still gives the coefficient at least two. This is a genuine gap in this sufficient comparison, not a finite rounding issue.

## 5. What remains open after rejecting this bridge

For this family, the average over CRT shifts of the Q_N-rough count is

    N product_{p in Q_N}(1-1/p)=(1/u+o(1))N.

This is below the one-large-prime allowance f(u)N. The Selberg upper bound being larger than that allowance does not establish any shift attaining the upper bound.

Thus the failure of (B) leaves (T) undecided. It shows that the proposed standard-denominator argument cannot prove (T) through that comparison. A stronger interval-sieve argument could still work, but none is established here.

Even a proof of (T) with an unspecified uniform o(N) error would require a further weighted summation argument before being used in the actual p-demand rows of the original problem. This note makes no such summability claim.

## Primary sources checked

1. Eric Bach and Rene Peralta, *Asymptotic Semismoothness Probabilities*, Mathematics of Computation 65 (1996), 1701--1715, especially Theorem 3.1 and the defining identity for the Dickman function. [Primary paper](https://cr.yp.to/bib/1996/bach-semismooth.pdf).
2. Eric Bach and Jonathan Sorenson, *Approximately Counting Semismooth Integers*, arXiv:1301.5293v2, equation (2) for the exact identity (1). [Primary manuscript](https://arxiv.org/pdf/1301.5293).
3. Ofir Gorodetsky, author-hosted lecture notes, Section 2, for the Dickman delay equation, rapid decay, and Laplace transform. The latter at zero gives the integral e^gamma. [Author's notes](https://people.maths.ox.ac.uk/gorodetsky/vibrant.pdf).

The proof above derives the new counterexample from those standard inputs; it does not reproduce external source text.
