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
const band=[2,3,5,7,11,13], primes=[...band,17,19,23];
const isTouched=x=>band.some(p=>x%p===0);
const sources=Array.from({length:50},(_,i)=>i+1).filter(isTouched);
const cover=Array.from({length:50},(_,i)=>170185+i).filter(isTouched);
function v(n,p){let e=0;for(;n%p===0;e++,n/=p);return e;}
const vector=A=>primes.map(p=>A.reduce((s,x)=>s+v(x,p),0));
const src=vector(sources),dst=vector(cover);
if(sources.length!==40||sources.at(-1)!==50||cover.length!==42
   ||src.some((v,i)=>i<band.length?v!==dst[i]:v>dst[i]))throw Error("Finite certificate failed");
console.log({n:sources.length,cover:cover.length,src,dst});
