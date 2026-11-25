# Hot roots below the square-root scale do not have square-root union discrepancy

24 November 2026. This is a counterexample to a proposed intermediate transfer estimate, not to Erdős 708 or the genuine-optimizer descent (D).

## 1. Exact arithmetic construction

Fix c=9/4. For an integer z>=3 set M=4z² and N=M/2=2z². Use raw prices

    w_2=3/4,
    w_p=1 for odd primes p<=z,
    w_p=0 for all other primes.

Let H={2p:p prime<=z}. Every root h in H is at most 2z=sqrt(M) and is strictly hot:

    X(4)=3/2>1,
    X(2p)=7/4>1 for odd p.

The full source tail A={a<=M:X(a)>c} is nonempty, and every active prime occurs in it. For odd p<=z, the integer 2p² belongs to A, since X(2p²)=11/4>9/4; prime 2 occurs in these sources as well.

For any nonnegative x, take the actual M-term interval

    I_x={2x+1,...,2x+4z²}.

Its multiples of 2, after division by 2, are exactly {x+1,...,x+N}. Hence

    |union_(h in H)(I_x intersect hZ)|
       = N-R_z(x,N),

where R_z(x,N) counts integers in that quotient interval coprime to P(z)=product_(p<=z)p. The prefix union has size N-R_z(0,N).

Average x over one full residue system modulo P(z). By CRT,

    average_x R_z(x,N)=N product_(p<=z)(1-1/p).

Therefore some actual nonnegative shift x satisfies

    prefix_union_size-target_union_size
      >= ceil(N product_(p<=z)(1-1/p))-R_z(0,N).        (1)

No independent or unrealizable residue pattern has been substituted.

## 2. The discrepancy exceeds every fixed multiple of sqrt(M)

The classical Mertens product theorem gives

    N product_(p<=z)(1-1/p) ~ e^(-EulerGamma) N/log z.

Every z-rough integer <=N=2z² is 1, a prime exceeding z, or a product of two primes exceeding z. In the last case both factors are at most 2z, so the number of such products is O(z²/log²z), by the prime number theorem (an upper bound for pi suffices for this error).

Consequently

    R_z(0,N)=1+pi(N)-pi(z)+O(z²/log²z)
            ~ N/(2log z).

Since e^(-EulerGamma)>1/2, (1) is at least

    (e^(-EulerGamma)-1/2+o(1)) N/log z.

Dividing by sqrt(M)=2z gives a quantity tending to infinity. Thus a generic O(sqrt M) transfer error for unions of hot roots h<=sqrt M is false, even with an actual raw load, a nonempty full tail, and no unused active prime.

## 3. Exact finite certificate for scale checking

For z=1000, M=4,000,000, N=2,000,000:

    number of primes <=z                  168
    exact prefix rough count              152,528
    exact CRT mean, decimal rendering     161,930.52701368477...
    ceiling of exact rational mean        161,931
    certified actual union deficit        at least 9,403
    sqrt(M)                               2,000

The rough count was obtained by an exact sieve; the mean and its ceiling were computed with rational arithmetic. The existence of the actual target shift follows from averaging, without a search through the enormous primorial period. This computation is not a computation of g(n).

## 4. Why this does not refute the required descent

The displayed weight vector has not been proved to maximize J_c. In fact, its large collection of low-load source integers provides substantial unused source-side reserve. Generic prefix-union transfer discards that reserve.

For example, a source that is assigned a root h=2p in H with a cold complement must have one of the forms

    a=2pqv or a=4pv,

with odd primes p,q<=z and v containing no active prime. (Terms at the exact source threshold are omitted.) Their total number is o(M): v=1 contributes O(z²/log²z), while v>1 is prime >z for sufficiently large z, and the elementary prime-counting upper bound gives at most

    O(M (log log z)²/log z).

By contrast, the bank union already contains all multiples of 4 and has at least M/4 positions. Thus the discrepancy of the whole prefix union does not imply a corresponding Hall deficiency for the actual eligible sources.

The common factor 2 is cold: X(2)=3/4<1. Its quotient is exactly the smaller actual interval used above. Therefore any successful route must retain the true full-tail source restriction, the new quotient-tail terms, and the clipping gain. Bounding the error of the entire unweighted prefix union independently cannot establish (D).

## 5. An exact moment fact, and its limitation

For every t>=0, exp(tX(m)) has a nonnegative divisor expansion. At a prime power,

    g_t(p^j)=exp(t w_p(j-1)) (exp(tw_p)-1)>=0.

Thus every actual M-term interval satisfies

    sum_(b in I) exp(tX(b)) >= sum_(a<=M) exp(tX(a)).

Likewise all nonnegative integer moments of X dominate exactly on the target, by their nonnegative prime-power divisor expansions. This does not by itself compare the two hinges: a distribution may preserve its mean and dominate all higher moments by putting a small amount of mass at a very large load. The genuine original row balances and global phase optimality would have to exclude or pay for that mechanism. No such exclusion sufficient for (D) is established here.

## Status

The generic square-root root-union estimate is disproved. The exact original descent (D), and the direct square-root bound for Delta_c, remain unproved by this hyperbola approach. No restricted profile theorem is being substituted for the full goal.
