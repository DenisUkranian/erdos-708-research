#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <random>
#include <vector>
#include <iomanip>
using namespace std;
using ll=long long;
ll egcd(ll a,ll b,ll&x,ll&y){if(!b){x=1;y=0;return a;}ll xx,yy;ll g=egcd(b,a%b,xx,yy);x=yy;y=xx-(a/b)*yy;return g;}
ll inv(ll a,ll m){if(m==1)return 0;ll x,y;egcd(a,m,x,y);x%=m;return (x+m)%m;}
struct Root{int d;double r;};
struct Case{
 int M;vector<int> spf,pe,rest,ii,primes;vector<double>w,X,Kh,Ka;vector<ll>h,cap,phase;vector<vector<Root>> roots;
 double srcH=0,srcA=0,tailH=0,tailA=0,surplus=0;int n=0;
 Case(int M0):M(M0),spf(M+1),pe(M+1),rest(M+1),ii(M+1),w(M+1),X(M+1),Kh(M+1),Ka(M+1),h(M+1,1),cap(M+1),phase(M+1),roots(M+1){
 for(int i=2;i<=M;i++)if(!spf[i])for(int j=i;j<=M;j+=i)if(!spf[j])spf[j]=i;
 for(int d=2;d<=M;d++){int p=spf[d],e=1,rr=d/p;while(rr%p==0){e*=p;rr/=p;}pe[d]=e*p;rest[d]=rr;ii[d]=inv(pe[d],rr);}
 }
 void prepare(){
 for(int p=2;p<=M;p++)if(w[p]>0){primes.push_back(p);ll q=p;while(q<=M)q*=p;cap[p]=q;}
 for(int a=2;a<=M;a++){int p=spf[a];X[a]=X[a/p]+w[p];h[a]=h[a/p]*(w[p]>0?p:1);}
 for(int d=2;d<=M;d++){
  int a=d,om=0;double mn=1;vector<int>ps;bool good=true;
  while(a>1){int p=spf[a];ps.push_back(p);if(w[p]==0){good=false;break;}mn=min(mn,w[p]);while(a%p==0){a/=p;om++;}}
  if(!good||X[d]<=1+1e-12)continue;
  double r=min(mn,(X[d]-1)/om);
  for(int p:ps)if((ll)d*d<=(ll)M*p)roots[p].push_back({d,r});
 }
 for(int p:primes){vector<double>mh(M+1),ma(M+1);for(auto rt:roots[p]){ll lim=(ll)rt.d*rt.d/p;for(int a=rt.d;a<=M;a+=rt.d){if(h[a]>=lim)mh[a]=max(mh[a],rt.r);if(a>=lim)ma[a]=max(ma[a],rt.r);}}
 for(ll q=p;q<=M;q*=p)for(int a=q;a<=M;a+=q){Kh[a]+=mh[a];Ka[a]+=ma[a];}}
 for(int a=1;a<=M;a++){srcH+=Kh[a];srcA+=Ka[a];if(X[a]>2.1+1e-10){n++;tailH+=Kh[a];tailA+=Ka[a];surplus+=X[a]-2.1;}}
 }
 double eval(){
 vector<ll>res(M+1);
 for(int d=2;d<=M;d++){ll xx=phase[spf[d]]%pe[d];if(rest[d]==1)res[d]=xx;else {ll delta=(res[rest[d]]-xx)%rest[d];if(delta<0)delta+=rest[d];res[d]=(xx+(ll)pe[d]*(delta*ii[d]%rest[d]))%d;}}
 double cost=0;vector<double>mx(M+1);vector<int>vp(M+1);
 for(int p:primes){fill(mx.begin(),mx.end(),0);fill(vp.begin(),vp.end(),0);for(auto rt:roots[p]){int st=rt.d-res[rt.d];for(int a=st;a<=M;a+=rt.d)mx[a]=max(mx[a],rt.r);}
 for(ll q=p;q<=cap[p];q*=p){ll st=q-phase[p]%q;for(ll a=st;a<=M;a+=q)vp[a]++;if(q>cap[p]/p)break;}
 for(int a=1;a<=M;a++)cost+=vp[a]*mx[a];}
 return cost;
 }
 void print(double best){cout<<setprecision(15)<<"M="<<M<<" n="<<n<<" Khprefix="<<srcH<<" Kaprefix="<<srcA<<" Khtail="<<tailH<<" Katail="<<tailA<<" target="<<best<<"\nweights:";for(int p:primes)cout<<" "<<p<<":"<<w[p];cout<<"\nphases:";for(int p:primes)cout<<" "<<p<<":"<<phase[p];cout<<"\n"<<flush;}
};
int main(){mt19937_64 rng(708711);int runs=0;
for(int M:{60,90,120,180})for(int run=0;run<24;run++){
 Case shape(M);vector<int>ps;vector<ll>caps(M+1),phase(M+1);vector<double>w(M+1);
 for(int p=2;p<=M;p++)if(shape.spf[p]==p && p<=pow(M,.65)){ps.push_back(p);ll cap=p;while(cap<=M)cap*=p;caps[p]=cap;phase[p]=rng()%cap;w[p]=(1+rng()%12)/12.;}
 auto objective=[&](vector<double>const& ww,vector<ll>const& ph,bool print=false){Case a(M);a.w=ww;a.phase=ph;a.prepare();if(a.srcH<.5)return -1e99;double target=a.eval();double obj=a.srcH-target;if(print)a.print(target);return obj;};
 double best=objective(w,phase);
 for(int round=0;round<8;round++){
  bool changed=false;
  for(int p:ps){double old=w[p],bw=old;for(int k=0;k<=12;k++){w[p]=k/12.;double v=objective(w,phase);if(v>best+1e-9){best=v;bw=w[p];changed=true;}}w[p]=bw;}
  for(int p:ps){if(w[p]==0)continue;ll old=phase[p],bp=old;for(ll ph=0;ph<caps[p];ph++){phase[p]=ph;double v=objective(w,phase);if(v>best+1e-9){best=v;bp=ph;changed=true;}}phase[p]=bp;}
  // Small continuous rational perturbations address narrow grid vertices.
  for(int step=0;step<80;step++){int p=ps[rng()%ps.size()];double old=w[p];int denominator=(step%2)?60:120;w[p]=max(0.,min(1.,w[p]+(rng()%2?1.:-1.)/denominator));double v=objective(w,phase);if(v>best+1e-9){best=v;changed=true;}else w[p]=old;}
  if(best>1e-8){cout<<"FAIL_JOINT objective="<<best<<" ";objective(w,phase,true);return 0;}
  if(!changed)break;
 }
 runs++;cout<<"RUN "<<runs<<" M="<<M<<" best="<<setprecision(12)<<best<<"\n"<<flush;
}
cout<<"FINAL_PASS "<<runs<<" jointly optimized instances\n";
}
