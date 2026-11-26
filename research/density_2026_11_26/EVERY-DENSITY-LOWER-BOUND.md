# A linear gap above \(n\) at every fixed density in #708

For every fixed \(0<r<1\), there is a constant \(\epsilon_r>0\) such that for every sufficiently large integer \(M\) there is a source set with \(\max A=M\) and \(|A|=\lfloor rM\rfloor\), and a positive interval \(I\) of length \(M\) such that \(\tau(A,I)\ge (r+\epsilon_r)M\). Here \(\tau\) is the minimum number of distinct target positions whose product is divisible by the source product.

## CRT construction and the lower densities

Use every source with a prime in the band \((M^\alpha,M^\beta]\) and include \(M\). For each band prime \(p\), pick a residue class of target offsets containing the most still-untouched positions. This touches at least a \(1/p\) fraction of the remaining positions, since the \(p\) residue classes partition them. Thus the final untouched count is at most \(M\prod_p(1-1/p)\). Mertens gives the lower bound \((1-\alpha/\beta-o(1))M\) for touched positions. Choose a fixed integer \(K\) with \(\alpha K>1\). The phase modulo \(p\) has \(p^{K-1}\) lifts modulo \(p^K\), of which at most \(M/p+1\) are forbidden by the requirement of avoiding every \(p^K\) multiple in \(I\). Lift independently and apply CRT. Target valuations beyond the first contribute \(o(M)\) since they are bounded and \(\sum_{p>M^\alpha}p^{-2}=o(1)\). The first-power counts differ between intervals by \(o(M)\). Every omitted position touched by the band consumes a unit of the \(o(M)\) excess valuation capacity across band primes. Consequently \(\tau\ge (1-\alpha/\beta-o(1))M\). Additional sources can pad to a higher density while preserving this bound. At any chosen limiting density \(r\), add or remove \(o(M)\) of the sources to enforce \(|A|=\lfloor rM\rfloor\) and retain \(M\). Each removed source contributes at most \(1/\alpha\) total band valuations, so the lower bound changes by only \(o(M)\).

Here and below, for a given band let (I_j) denote the (j)-fold reciprocal-density integral over the points in that band with sum of exponents at most one. For the low densities set \(\alpha=1/3\) and take \(1/3<\beta\le11/20\). No source integer has three distinct band primes, so with \(L=\ln(3\beta)\) the limiting source density is \(s=L-I_2/2\), using the feasible-pair integral as defined below. For \(\beta\le1/2\) we have \(s=L-L^2/2<1-e^{-L}=u\). For \(1/2\le\beta\le11/20\),
\[
u'-s'=\big(1/(3\beta)-1+\ln(3(1-\beta))\big)/\beta.
\]
Its numerator strictly decreases, so the gap takes its minimum at an endpoint. At \(\beta=11/20\) the forbidden-pair triangle has area \((2\beta-1)^2/2\) and \(t_1t_2\ge\beta(1-\beta)\) on it. Thus \(s\le L-L^2/2+1/99<0.386\), while \(u=13/33>0.39\). By continuity and padding this covers every fixed \(0<r\le0.39\).

## Joining the density ranges

Fix \(\alpha=1/4\) and vary \(0.41\le\beta\le2/3\). No source integer has four distinct band primes, so the limiting density is \(s=L-I_2/2+I_3/6\), where \(L=\ln(4\beta)\) and
\[
I_j=\int_{[1/4,\beta]^j}\boldsymbol1_{\sum t_i\le1}\prod_i(dt_i/t_i).
\]
For the floor errors in \(j\)-fold inclusion-exclusion, count the last prime via \(\pi(M/(p_1\cdots p_{j-1}))\ll M/(p_1\cdots p_{j-1}\log M)\) wherever it can exceed \(M^{1/4}\), and sum using the bounded reciprocal band mass. This gives \(O(M/\log M)\) tuples for each \(j\le3\). Repeated-label reciprocal terms are \(o(1)\), and Mertens gives weak convergence of the prime exponent measures to \(dt/t\). The boundary of the integrating region has zero measure.

Rescale the full triple simplex by \(t_i=(1+v_i)/4\), so \(\sum v_i\le1\). The denominator \(\prod(1+v_i)\ge1+\sum v_i\). Thus \(I_3\le\frac12\int_0^1v^2/(1+v)\,dv=(\ln2-1/2)/2\). For \(\beta\le1/2\) all pairs fit, so \(s\le L-L^2/2+(\ln2-1/2)/12\). At \(\beta=0.41\) this is below \(0.388430\), while \(u=1-1/(4\beta)=16/41>0.39024\). The difference \(1-e^{-L}-L+L^2/2\) increases with \(L>0\), so the strict comparison holds through \(\beta=1/2\). Above \(1/2\) the triple region is constant. Differentiating the pair integral gives
\[
u'-s'=\frac{1/(4\beta)-1+\ln(4(1-\beta))}{\beta}.
\]
The numerator decreases strictly, so the gap is minimized at an endpoint of \([1/2,2/3]\). The first is positive by the preceding argument and the second by the smooth-number argument below. Continuity of \(s\) joins the lower densities to \(s(1/4,2/3)\).

## High densities

Fix \(\beta=2/3\). The complement of the band source set consists of \(M^\alpha\)-smooth integers and integers with a unique prime \(p>M^{2/3}\) times a smooth cofactor \(q\). With \(D\) the Dickman function, its limiting density is
\[
1-s(\alpha,2/3)=D(1/\alpha)+\int_0^{1/3}\frac{D(t/\alpha)}{1-t}\,dt .
\]
To see the integral, sum \(\pi(M/q)-\pi(M^{2/3})\) over smooth \(q\le M^{1/3}\). The total subtracted term is \(O(M/\log M)\). Apply the prime number theorem uniformly for \(M/q\ge M^{2/3}\) and partially sum \(1/[q\log(M/q)]\). The endpoint is \(O(1/\log M)\). The main integral is the limit under bounded convergence after \(q=M^t\), since \(\Psi(M^t,M^\alpha)/M^t\to D(t/\alpha)\). [Fixed-ratio Dickman asymptotic](https://www.cambridge.org/core/journals/proceedings-of-the-royal-society-of-edinburgh-section-a-mathematics/article/smooth-integers-and-de-bruijns-approximation/68FF9370894E1142B975BAC783DFF162)

For \(\alpha\le1/6\), the integral divided by \(\alpha\) is at least \(\int_0^2D(v)\,dv=3-2\ln2>3/2\). For \(\alpha\in[1/6,1/4]\) put \(x=1/(3\alpha)\in[4/3,2]\). The normalized integral equals \(F(x)=x\int_0^1 D(xs)/(1-s/3)\,ds\). Its derivative numerator is 1 for \(xs<1\) and \(-\ln(xs)\) for \(xs>1\). Hence
\[
F'(x)\ge 1/x-\tfrac32\int_{1/x}^1\ln(xs)\,ds
=\tfrac32(1-\ln x)-1/(2x)>0.
\]
At \(x=4/3\), the bound \(D(v)\ge2-v\) for \(1\le v\le4/3\) yields
\[
F(4/3)\ge4\ln(4/3)+4/3-8\ln(9/8)>1.54179>3/2.
\]
Thus \(1-s(\alpha,2/3)>3\alpha/2\) for every \(0<\alpha\le1/4\), while \(u=1-3\alpha/2\). As \(\alpha\downarrow0\), the complement tends to zero by bounded convergence and \(D(v)\to0\). The formula is continuous for \(\alpha>0\). It therefore covers every fixed density from \(s(1/4,2/3)\) up to 1, excluding 1 itself.

Take \(\epsilon_r\) to be half the strict gap between the target lower bound and the desired density. At limiting density 1 the whole interval has \(n+o(n)\) positions. The unrestricted \(2n\) question remains open. Public priority for the fixed-density lower bound was not established. [Original #708 problem](https://hrj.episciences.org/125/pdf)

## Size of the obstruction as density approaches one

The smooth-complement formula works for any fixed \(\beta>1/2\), with upper integration limit \(1-\beta\). Choose \(\beta=1-\sqrt{\alpha}\), for small \(\alpha>0\), fixed while \(M\to\infty\). Changing variables \(t=\alpha v\) gives
\[
\frac{1-s(\alpha,\beta)}{\alpha}
=\frac{D(1/\alpha)}{\alpha}+\int_0^{1/\sqrt{\alpha}}\frac{D(v)}{1-\alpha v}\,dv
\longrightarrow e^\gamma.
\]
The first term tends to zero by the standard rapid decay of \(D\). The integral converges by domination and \(\int_0^\infty D(v)\,dv=e^\gamma\). Meanwhile \((1-u)/\alpha=1/\beta\to1\). By continuity this curve realizes every source density \(r\) sufficiently close to one, and \(\alpha\) tends to zero as \(r\) tends to one along the curve. Therefore the construction gives
\[
\liminf_{M\to\infty}
\frac{\max_{\substack{|A|=\lfloor rM\rfloor\\\max A=M},\, I}\tau(A,I)-\lfloor rM\rfloor}{(1-r)M}
\ \ge\ 1-e^{-\gamma}+o_{r\to1}(1).
\]
The constant is approximately 0.4385. This quantifies the gap relative to the \(M-n\) positions available above the source size. [Dickman Laplace transform, Lemma 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC10952566/)

## Finite example with 80% density

Let \(M=50\), and take \(A\) to be the 40 integers in \([1,50]\) divisible by at least one of \(2,3,5,7,11,13\). Take \(I=[170185,170234]\). The band-touched positions are all offsets from 170184 except \(5,13,17,23,29,37,43,47\), so there are 42. The source valuations at \(2,3,5,7,11,13,17,19,23\) are \((47,22,12,8,4,3,1,1,1)\). The 42 band-touched positions supply \((47,22,12,8,4,3,2,1,2)\). Equality on all six band primes forces every one of the 42 touched positions into every cover. Those positions also satisfy all the source requirements for primes outside the band, so \(\tau(A,I)=42\).

## Exact comparison of endpoint constants

```javascript
const gcd=(a,b)=>b===0n?(a<0n?-a:a):gcd(b,a%b);
const Q=(a,b=1n)=>{const g=gcd(a,b);return [a/g,b/g];};
const plus=([a,b],[c,d])=>Q(a*d+b*c,b*d);
const minus=(a,[c,d])=>plus(a,[-c,d]);
const mul=([a,b],[c,d])=>Q(a*c,b*d);
const div=(a,[c,d])=>mul(a,[d,c]);
const pow=([a,b],k)=>Q(a**BigInt(k),b**BigInt(k));
const less=([a,b],[c,d])=>a*d<c*b;
const one=Q(1n),two=Q(2n),zero=Q(0n);
function logBounds(x){
  const z=div(minus(x,one),plus(x,one));
  let low=zero;
  for(let k=1;k<=15;k+=2)low=plus(low,div(mul(two,pow(z,k)),Q(BigInt(k))));
  return [low,plus(low,div(mul(two,pow(z,17)),mul(Q(17n),minus(one,pow(z,2)))))];
}
const fmt=([a,b])=>Number(a)/Number(b);
const [smallLog,bigLog]=logBounds(Q(41n,25n));
const [lowTwoBand,highTwoBand]=logBounds(Q(33n,20n));
const [logTwoLow,logTwoHigh]=logBounds(Q(2n));
const [log43Low,log43High]=logBounds(Q(4n,3n));
const [log98Low,log98High]=logBounds(Q(9n,8n));
const sUpper=plus(minus(bigLog,div(pow(bigLog,2),two)),div(minus(logTwoHigh,Q(1n,2n)),Q(12n)));
const fLower=minus(plus(mul(Q(4n),log43Low),Q(4n,3n)),mul(Q(8n),log98High));
const gapLower=minus(Q(16n,41n),sUpper);
const lowBandUpper=plus(minus(highTwoBand,div(pow(highTwoBand,2),two)),Q(1n,99n));
if(!less(lowBandUpper,Q(386n,1000n))||!less(sUpper,Q(388430n,1000000n)))throw Error('Overlap');
if(!less(Q(0n),gapLower)||!less(Q(154179n,100000n),fLower)||!less(logTwoHigh,Q(3n,4n)))throw Error("Failed endpoint checks");
console.log({lowBandUpper:fmt(lowBandUpper),sourceUpperAt41:fmt(sUpper),targetMinusSourceAt41:fmt(gapLower),FEndpointLower:fmt(fLower),smallAlphaLower:fmt(minus(Q(3n),mul(two,logTwoHigh)))});
```
