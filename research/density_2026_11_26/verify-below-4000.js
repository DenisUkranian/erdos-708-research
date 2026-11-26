const d=32000n
const cap=[660n,647n,634n,622n,610n,599n,588n,577n,567n,557n,548n,538n,529n,521n,513n,504n,497n,489n,482n,475n,468n,461n,454n,448n]
const h=[9206n,8871n,8533n,8190n,7844n,7495n,7141n,6784n,6422n,6056n,5686n,5312n,4933n,4550n,4162n,3770n,3372n,2970n,2562n,2149n,1731n,1307n,877n,442n]
const cs=[336n,674n,1016n,1362n,1712n,2066n,2423n,2785n,3151n,3521n,3895n,4274n,4657n,5045n,5437n,5835n,6237n,6645n,7058n,7476n,7900n,8330n,8765n,9206n]

const mn=(a,b)=>a<b?a:b,mx=(a,b)=>a>b?a:b,p=a=>mx(0n,a)
const taus=[70n,65n,60n,55n,50n,45n,40n,35n,30n,27n,25n,23n,20n,17n,15n,12n,10n,8n,5n]
const gcd=(a,b)=>b?gcd(b,a%b):a
const mult=taus.reduce((a,b)=>a*b/gcd(a,b),1n)
const rawCap=12976n

function run(goal, lowerOdds, upperDensity, lowMean=false){
  const stack=[[0n,19200n,0n,rawCap,0n,12800n,0n,12800n,0n,12800n]]
  let count=0
  while(stack.length){
    const box=stack.pop()
    count++
    const [a,A,j,J,k,K,b,B,e,E0]=box
    const l=mn(3n*d/2n,p(d+(lowMean?-K:k)-A-J))
    const L=mn(3n*d/2n,p(d+(lowMean?-k:K)-a-j))
    const cut=cs[15]
    const E=mn(E0,mn(B,mn(d,p(L-cut))))
    if(e>E)continue;
    const hb=h.map(H=>p(a-H))
    let demand=j,half=0n
    for(let i=0;i<24;i++){
      const take=mn(demand,cap[i])
      half+=take*hb[i]
      demand-=take
    }
    const qbound=mx(j,mn(J,rawCap/2n))
    const raw=(2n*d*(a+j-upperDensity)-J*J-2n*J*A+2n*half)*rawCap
    const u=200n*d*qbound*(rawCap-qbound)
    const ar=2n*d*rawCap*(rawCap-j)
    const levelScale=d*d*mult
    const pd=200n*d*d*rawCap*levelScale
    const events=[]
    let prevC=0n,penalty=0n,slope=levelScale
    for(const tau of taus){
      const c=p(lowerOdds-d*tau/100n-(lowMean?0n:K))**2n
      const br=p(tau*raw-mn(u,(100n-tau)*ar))
      const weight=100n*(c-prevC)*(mult/tau)
      if(br&&weight){
        events.push([br,weight])
        penalty+=br*weight
        slope-=weight
      }
      prevC=c
    }
    if(slope<0n){
      events.sort((a,b)=>a[0]<b[0]?-1:a[0]>b[0]?1:0)
      let prev=0n
      for(const [at,weight] of events){
        penalty+=(at-prev)*slope
        slope+=weight
        if(slope>=0n)break
        prev=at
      }
    }
    const pass=(num,den)=>10000n*(num*pd+penalty*den)>=goal*den*pd
    const base=a*a+d*(k+b)
    if(pass(base+2n*half,d*d))continue
    const xs=cs.map((C,i)=>{
      const r=mn(d,p(l-C))
      return [2n*d*hb[i]+(2n*d-r)*p(r-B),cap[i]]
    }).sort((x,y)=>x[0]<y[0]?-1:x[0]>y[0]?1:0)
    let left=j,mixed=0n
    for(const [cost,limit] of xs){
      const take=mn(left,limit)
      mixed+=take*cost
      left-=take
    }
    const g=l*(3n*d-l)*p(l-2n*B)-6n*d*d*(lowMean?0n:K)+3n*mixed
    if(pass(3n*d*base+g,3n*d**3n))continue
    const r=mn(d,p(l-cut)),t=l-r
    const et=r>=t?e:E
    const pc=r*p(r-2n*E)+t*p(t-2n*(B-e))+2n*p(r*t-t*et-r*(B-et))
    const pure=mx((3n*d-L)*pc,l*(3n*d-l)*p(l-2n*B))
    const mix2=cs.map((C,i)=>{
      const ri=mn(d,p(l-C)),charge=mn(B,E+p(cut-C))
      return [2n*d*hb[i]+(2n*d-ri)*p(ri-charge),cap[i]]
    }).sort((x,y)=>x[0]<y[0]?-1:x[0]>y[0]?1:0)
    let rem=j,sum2=0n
    for(const [cost,limit] of mix2){
      const take=mn(rem,limit)
      sum2+=take*cost
      rem-=take
    }
    const g2=pure-6n*d*d*(lowMean?0n:K)+3n*sum2
    if(pass(3n*d*base+g2,3n*d**3n))continue
    box[9]=E
    let s=0
    for(const i of [2,4,6,8])if(box[i+1]-box[i]>box[s+1]-box[s])s=i
    if(box[s+1]-box[s]<=1n)return {count,fail:box.map(String)}
    const x=[...box],y=[...box],mid=(box[s]+box[s+1])/2n
    x[s+1]=mid;y[s]=mid;stack.push(y,x)
  }
  return {count,fail:null}
}

const checks = [
  [3376n, 21200n, 12800n, [3732245, 241113]],
  [3403n, 21112n, 12752n, [7098589, 324561]],
];
for (const [goal, lowerOdds, upperDensity, expected] of checks) {
  for (const [index, lowMean] of [false, true].entries()) {
    const result = run(goal, lowerOdds, upperDensity, lowMean);
    if (result.fail || result.count !== expected[index]) {
      throw Error(JSON.stringify(result));
    }
    console.log({ threshold: String(goal), lowMean, ...result });
  }
}
