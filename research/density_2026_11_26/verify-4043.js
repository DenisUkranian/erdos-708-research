const d=128000n
const cap=[660n,647n,634n,622n,610n,599n,588n,577n,567n,557n,548n,538n,529n,521n,513n,504n,497n,489n,482n,475n,468n,461n,454n,448n].map(x=>4n*x)
const h=[9206n,8871n,8533n,8190n,7844n,7495n,7141n,6784n,6422n,6056n,5686n,5312n,4933n,4550n,4162n,3770n,3372n,2970n,2562n,2149n,1731n,1307n,877n,442n].map(x=>4n*x)
const cs=[336n,674n,1016n,1362n,1712n,2066n,2423n,2785n,3151n,3521n,3895n,4274n,4657n,5045n,5437n,5835n,6237n,6645n,7058n,7476n,7900n,8330n,8765n,9206n].map(x=>4n*x)

const mn=(a,b)=>a<b?a:b,mx=(a,b)=>a>b?a:b,p=a=>mx(0n,a)
const taus=[70n,65n,60n,55n,50n,45n,40n,35n,30n,27n,25n,23n,20n,17n,15n,12n,10n,8n,5n]
const gcd=(a,b)=>b?gcd(b,a%b):a
const mult=taus.reduce((a,b)=>a*b/gcd(a,b),1n)
const rawCap=51904n
function run(goal,lowMean=false){
  const capSum=cap.reduce((a,b)=>a+b,0n)
  const stack=[[0n,76800n,0n,rawCap,0n,lowMean?0n:76800n]]
  let count=0
  while(stack.length){
    const box=stack.pop()
    count++
    const [a,A,j,J,k,K]=box
    const l=mn(d,p(d+k-A-J)), L=mn(d,p(d+K-a-j))
    const r0=p(L-cs[0])
    let rem=J,Rhi=0n,Rlo=0n
    for(let i=23;i>=0;i--){
      const take=mn(rem,cap[i])
      Rhi+=take*p(L-cs[i])
      Rlo+=take*p(l-cs[i])
      rem-=take
    }
    const hb=h.map(H=>p(a-H)), base=a*a+d*k
    let demand=j, half=0n
    for(let i=0;i<24;i++){
      const take=mn(demand,cap[i])
      half+=take*hb[i]
      demand-=take
    }
    const qbound=mx(j,mn(J,rawCap/2n))
    const raw=(2n*d*(a+j-51968n)-J*J-2n*J*A+2n*half)*rawCap
    const u=200n*d*qbound*(rawCap-qbound)
    const ar=2n*d*rawCap*(rawCap-j)
    const levelScale=d*d*mult
    const pd=200n*d*d*rawCap*levelScale
    const events=[]
    let prevC=0n,penalty=0n,slope=levelScale
    for(const tau of taus){
      const c=p(86400n-d*tau/100n-K)**2n
      const b=p(tau*raw-mn(u,(100n-tau)*ar))
      const weight=100n*(c-prevC)*(mult/tau)
      if(b&&weight){
        events.push([b,weight])
        penalty+=b*weight
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
    if(pass(base+2n*half,d*d))continue
    let ok=false
    for(const alpha of lowMean?[6n,4n,3n]:[6n,4n,3n,2n]){
      const R=alpha*(3n*d-2n*L)>=9n*J?Rhi:Rlo
      const c=mx(alpha*(6n*d*L-2n*L*L)+36n*d*J-18n*R,18n*r0*(2n*d-r0))
      if(c===0n)continue
      const t=mn(2n*c,36n*d*d)
      const xs=cs.map((C,i)=>{
        const r=p(l-C)
        return [4n*d*c*hb[i]+t*r*(2n*d-r),cap[i]]
      }).sort((x,y)=>x[0]<y[0]?-1:x[0]>y[0]?1:0)
      let left=j,mixed=0n
      for(const [cost,limit] of xs){
        const take=mn(left,limit)
        mixed+=18n*take*cost
        left-=take
      }
      const v=36n*d*c*base+t*(alpha*l*l*(3n*d-l)-36n*d*d*K)+mixed
      if(pass(v,36n*d**3n*c)){ok=true;break;}
    }
    if(ok)continue
    let s=0
    for(const i of [2,4])if(box[i+1]-box[i]>box[s+1]-box[s])s=i
    if(box[s+1]-box[s]<=1n)return {count,fail:box.map(String)}
    const x=[...box],y=[...box],mid=(box[s]+box[s+1])/2n
    x[s+1]=mid;y[s]=mid;stack.push(y,x)
  }
  return {count,fail:null}
}
const a=run(3214n), b=run(3214n,true)
if(a.fail||b.fail||a.count!==759193||b.count!==881)throw Error(JSON.stringify({a,b}))
console.log(JSON.stringify({highMean:a,lowMean:b}));
