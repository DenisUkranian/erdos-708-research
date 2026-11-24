# Uniform raw moments and an improved large-mean exclusion

Date: 2026-11-23.

Status: the original threshold 2+4 epsilon_M is valid. The same first
and second moments also give the improved threshold
241/136+4 epsilon_M. The scalar improvement was independently checked
by the analytic research agent. These estimates exclude a range of
dual weights; they do not settle the remaining low-mean range.

## 1. Setup and a uniform first-moment error

Let M>=4 be an integer. Let 0<=w_p<=1 be supported on primes p<=M.
For a uniformly chosen integer a in {1,...,M}, put

    X(a)=sum_{p<=M}w_p v_p(a),
    mu=sum_{p<=M}w_p/(p-1),
    m=E X,
    J=floor(log_2 M).

Define the explicit nonnegative error

    epsilon_M =
      [pi(M)+(J+1)pi(sqrt M)]/M + 1/floor(sqrt M).          (1)

Then, uniformly in the weight vector,

    mu-epsilon_M <=m<=mu.                                (2)

In particular,

    epsilon_M <=pi(M)/M +(J+3)/sqrt M
       =O(1/log M + log M/sqrt M)=o(1).                   (3)

The asymptotic estimate uses only Chebyshev's standard upper bound
pi(x)=O(x/log x). It is the same uniform error scale requested in
the original candidate.

### Proof of (2)

For each prime p, let j_p=floor(log M/log p). Prime-power counting
gives

    m=(1/M)sum_{p<=M}w_p sum_{j=1}^{j_p}floor(M/p^j).

Compare this with mu=sum_p w_p sum_{j>=1}p^(-j).
All differences are nonnegative. The j=1 floor errors total at most
pi(M)/M. For j>=2 with p^j<=M, only p<=sqrt M occur, and each such
prime has at most J-1 further floor errors. Their total is at most
(J-1)pi(sqrt M)/M.

For p<=sqrt M, the omitted geometric tail is

    sum_{j>j_p}p^(-j)
      =1/[p^(j_p)(p-1)] <p/[M(p-1)]<=2/M.

For p>sqrt M one has j_p=1. Enlarging these primes to all integers
and telescoping gives

    sum_{p>sqrt M}1/[p(p-1)]<=1/floor(sqrt M).

The sum of these four bounds is (1). This proves (2). The elementary
bound in (3) follows from pi(sqrt M)<=sqrt M and
floor(sqrt M)>=sqrt M/2 for M>=4.

## 2. The exact useful second-moment upper bound

Put

    nu=sum_{p<=M}w_p^2 p/(p-1)^2.

Then

    E X^2<=mu^2+nu<=mu^2+2mu.                             (4)

For distinct primes p,q, every pair of valuation levels requires
divisibility by p^j q^k, so

    E[v_p(a)v_q(a)]
      <=sum_{j,k>=1}1/(p^j q^k)
      =1/[(p-1)(q-1)].

For a single prime,

    E[v_p(a)^2]
      <=sum_{j>=1}(2j-1)/p^j
      =(p+1)/(p-1)^2.

Expanding X^2 yields the first inequality in (4); subtracting the
diagonal part already present in mu^2 leaves precisely nu.
Finally, w_p^2<=w_p and p/(p-1)<=2 prove nu<=2mu.
All inequalities are valid at every finite M; no independence of
the valuations is asserted.

## 3. From capped prefix mass to the interval hinge

For any positive M-term interval I, prime-power counting gives

    sum_{b in I}X(b)>=sum_{a<=M}X(a).

Therefore

    Delta_2(M,I,w)
      =sum_{a<=M}(X(a)-2)_+
         -sum_{b in I}(X(b)-1)_+
      <=M-sum_{a<=M}min(X(a),2).                          (5)

In particular, E min(X,2)>=1 implies H_2 simultaneously for every
interval shift. If the original support also contains primes greater
than M, first delete those primes when computing mu. They contribute
nothing to the prefix, and restoring them on the target side can
only help. The hypothesis p<=M in the definition of mu is essential.

## 4. Verification of the original quadratic argument

For 0<=a<=1 and x>=0,

    min(x,2)>=a x-a^2 x^2/8.                              (6)

For x<=2 the right side is at most a x<=x. For x>=2, the quadratic
has global maximum 2, attained at x=4/a when a>0; the case a=0 is
immediate.

If mu>=2, take a=4/(mu+2)<=1. Equations (2), (4), and (6) give

    E min(X,2)
      >=[2mu-4 epsilon_M]/(mu+2)
      =1+[mu-2-4 epsilon_M]/(mu+2).                       (7)

Thus

    mu>=2+4 epsilon_M  =>  H_2.                          (8)

There is no missing floor or prime-power correction in this
argument: they are exactly the error in (1).

## 5. A sharper universal variance envelope

The clipped-weight assumption gives

    nu<=(7/6)mu+49/48.                                   (9)

Indeed, using w_p^2<=w_p, every prime p>=7 contributes at most
(7/6)w_p/(p-1) to nu. For p=2,3,5 the largest possible excess over
this expression is, respectively,

    5/6,     1/6,     1/48.

Their sum is 49/48. This is an elementary bound uniform over all
supports and all clipped vectors; it does not require a numerical
prime-sum constant.

## 6. Cauchy--Schwarz and the threshold 241/136

The pointwise identity

    min(x,2)=(x+2-|x-2|)/2

and Cauchy--Schwarz imply, with q=E X^2,

    E min(X,2)>=[m+2-sqrt(q-4m+4)]/2.                    (10)

For nonnegative m, the sufficient condition

    q<=m^2+4m-4                                          (11)

therefore gives capped mean at least one. Since m>=mu-epsilon_M,
the function m^2+4m is increasing on the nonnegative half-line.
For any error epsilon>=mu-m with mu-epsilon>=0, equations (4) and
(11) show that it is enough to have the vector-dependent condition

    nu<=4mu-4-(2mu+4)epsilon+epsilon^2.                   (12)

Using (9), a sufficient scalar condition is

    (17/6-2epsilon)mu
       >=241/48+4epsilon-epsilon^2.                     (13)

For every 0<=epsilon<=1/2, the simpler condition

    mu>=241/136+4epsilon                                (14)

implies (13). At equality in (14), the left side of (13) minus
the right side is exactly

    epsilon(773/204-7epsilon)>=0.

The coefficient 17/6-2epsilon is positive on this range, so every
larger mu also works. The condition mu-epsilon>=0 is automatic
under (14).

Consequently, for every sufficiently large M so that epsilon_M<=1/2,

    mu>=241/136+4epsilon_M  =>  H_2 for every shift.       (15)

The limiting numerical threshold is

    241/136 = 1.7720588235294117...

An exact, slightly smaller finite-error threshold can be read
directly from (13):

    mu >= [241/48+4epsilon_M-epsilon_M^2]
                /(17/6-2epsilon_M).

These are sufficient bounds, not asserted optimal thresholds.

## 7. What the mean restriction does and does not imply

For a distinct source subset A, H_2 implies

    sum_{a in A}X(a)-sum_{b in I}(X(b)-1)_+<=2|A|.

Thus any clipped raw dual witness exceeding 2|A| must have mu below
the threshold in (15), for large M. This is a uniform exclusion,
independent of the source's prime-support structure.

It does NOT bound the number of substantial coordinates by a
constant. For each integer N, choose N distinct primes greater
than N^2, give each weight one, and take M at least their maximum.
Then

    mu<=N/(N^2-1)->0,

although the number of weights equal to one is N. By enlarging
the structural parameter K, such primes can also lie below sqrt K;
small reciprocal mass alone does not exclude them from the
small-prime portion of the demand-defined core.

This example is about weight vectors, not a claim that these
vectors are dual witnesses or that a corresponding counterexample
exists. It demonstrates precisely why the large-mean exclusion
does not control the remaining core cardinality.

For any fixed eta>0, the actual consequence for the substantial
weight set H_eta={p:w_p>=eta} is only

    sum_{p in H_eta}1/(p-1)<=mu/eta.

This bounds a reciprocal-prime sum, not the number or joint
arithmetic arrangement of those primes. The growing dense core
and its interaction with the remaining support still need a
separate argument.

## Analytic input

The only asymptotic input in this note is the classical bound
pi(x)=O(x/log x), recorded, for example, in Granville and
Soundararajan's primary text:
https://dms.umontreal.ca/~andrew/PDF/Book.To1.4.pdf
All moment identities, envelope constants, and cap inequalities
are proved above.
