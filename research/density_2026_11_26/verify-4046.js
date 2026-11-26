const d=128000n
const cap=[660n,647n,634n,622n,610n,599n,588n,577n,567n,557n,548n,538n,529n,521n,513n,504n,497n,489n,482n,475n,468n,461n,454n,448n].map(x=>4n*x)
const h=[9206n,8871n,8533n,8190n,7844n,7495n,7141n,6784n,6422n,6056n,5686n,5312n,4933n,4550n,4162n,3770n,3372n,2970n,2562n,2149n,1731n,1307n,877n,442n].map(x=>4n*x)
const cs=[336n,674n,1016n,1362n,1712n,2066n,2423n,2785n,3151n,3521n,3895n,4274n,4657n,5045n,5437n,5835n,6237n,6645n,7058n,7476n,7900n,8330n,8765n,9206n].map(x=>4n*x)

const mn=(a,b)=>a<b?a:b,mx=(a,b)=>a>b?a:b,p=a=>mx(0n,a)
function run(goal,lowMean=false){
  const capSum=cap.reduce((a,b)=>a+b,0n)
  const stack=[[0n,76800n,0n,capSum,0n,lowMean?0n:76800n]]
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
    const qbound=mx(j,mn(J,capSum/2n))
    const raw=(2n*d*(a+j-51968n)-J*J-2n*J*A+2n*half)*capSum
    const sub=200n*d*qbound*(capSum-qbound)
    let penalty=0n, pd=1n
    for(const tau of [15n,20n,23n,25n,27n,30n,35n,40n]){
      const prob=p(raw*tau-sub)
      const cprior=mn(d*d*tau/100n,p(86758n-d*tau/100n-K)**2n)
      const n=prob*cprior, den=2n*d**4n*capSum*tau
      if(n*pd>penalty*den){penalty=n;pd=den;}
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
const a=run(3205n), b=run(3205n,true)
if(a.fail||b.fail||a.count!==2454563||b.count!==945)throw Error(JSON.stringify({a,b}))
console.log(JSON.stringify({highMean:a,lowMean:b}));
