#include <bits/stdc++.h>
using namespace std;
constexpr int L=24009, V=155;
int sp[L+1],om[L+1];vector<int> dv[L+1], S;int C[V+1][V+1];
using B=bitset<V+1>;
using E=array<int,5>;using U=uint64_t;int ps[5]={2,3,5,7,11};U ex[V+1];
struct Group{B a,allow;int d;U rest;};
U encode(int u){U z=0;for(int i=0;i<5;i++)while(u%ps[i]==0){u/=ps[i];z+=1ULL<<(8*i);}assert(u==1);return z;}
bool pack(U z,int M,int r){vector<int>P;for(int i=4;i>=0;i--)for(int j=0;j<int(z>>(8*i)&255);j++)P.push_back(ps[i]);int cap[3]={M/(r+1),M/(r+2),M/(r+3)};for(int mode=0;mode<3;mode++){int b[3]={cap[0],cap[1],cap[2]};bool ok=true;for(int p:P){int q=-1;for(int i=0;i<3;i++)if(b[i]>=p&&(q<0||(mode==1&&b[i]<b[q])||(mode==2&&b[i]>b[q])))q=i;if(q<0){ok=false;break;}b[q]/=p;}if(ok)return true;}return false;}

int first(int a,int j,int M){for(int d:dv[a])if(a/d<=M/j||om[a/d]<=1)return d;abort();}
bool peel(int a,int b,int M){for(int i=10;i<=12;i++)for(int j=10;j<=12;j++)if(i!=j){int k=33-i-j,d=first(a,i,M),e=first(b,j,M);if(1LL*d*e<=M/k||om[d]+om[e]<=1)return true;}return false;}
int main(){for(int i=2;i<=L;i++)if(!sp[i])for(int j=i;j<=L;j+=i)if(!sp[j])sp[j]=i;for(int i=2;i<=L;i++)om[i]=om[i/sp[i]]+1;for(int i=1;i<=L;i++)for(int j=i;j<=L;j+=i)dv[j].push_back(i);for(int u=2;u<=V;u++){int z=u;while(z>1&&sp[z]<=11)z/=sp[z];if(z==1)S.push_back(u);}
for(int u:S)for(int v:S){int c=INT_MAX;for(int i=10;i<=12;i++)for(int j=10;j<=12;j++)if(i!=j){int k=33-i-j;for(int d:dv[u])if(d==u||d>=i)for(int e:dv[v])if(e==v||e>=j)c=min(c,k*d*e);}C[u][v]=c;}
// Independently generate the minimal smooth divisors and exact tail threshold.
vector<int> minimal;for(int u:S)if(u>=11&&u<=110){bool ok=true;for(int d:dv[u])if(d!=u&&d>=11)ok=false;if(ok)minimal.push_back(u);}
assert((minimal==vector<int>{11,12,14,15,16,18,20,21,25,27,35,49}));
int tail=0;for(int u:minimal)for(int v:minimal){int best=INT_MAX;for(int i=10;i<=12;i++)for(int j=10;j<=12;j++)if(i!=j)for(int d:dv[u])if(d>=i)for(int e:dv[v])if(e>=j)best=min(best,(33-i-j)*d*e);assert(best<INT_MAX);tail=max(tail,best);}assert(tail==24010);
for(int u:S)ex[u]=encode(u); int pass=0,remain=0,maxM=0;long long total=0, allpairs=0,passed=0,triples=0;
for(int M=13;M<=L;M++){
 if(om[M]<2){pass++;continue;}int x=M,large=0;while(x>1){int p=sp[x];x/=p;if(p>11){if(large||1LL*p*p<=M){large=-1;break;}large=p;}}
 if(large<0){pass++;continue;}
 B adj[V+1];for(int u:S)if(u*u<M)for(int v:S)if(v*v<M&&C[u][v]>M)adj[u].set(v);
 vector<pair<int,vector<Group>>> groups;
 int p0=13;while(p0*p0<=M)++p0;
 for(int p=p0;p<=M/4;p++)if(sp[p]==p){
   int T=M/p;vector<int> pool;for(int u:S)if(u<=T&&12*p*u>M&&(large||!peel(p*u,M,M)))pool.push_back(u);
   if(pool.size()<4)continue;
   // all multiples of each source must already be in A; if a multiple missing from pool, discard a.
   B available;for(int u:pool)available.set(u);
   vector<int> keep;for(int u:pool){bool ok=true;int cnt=0;for(int z=u;z<=T;z+=u){if(!available[z]){ok=false;break;}cnt++;}if(ok&&cnt<=5)keep.push_back(u);}pool.swap(keep);
   if(pool.size()<4)continue; if(p==large&&find(pool.begin(),pool.end(),T)==pool.end())continue;
   vector<Group> g;auto dfs=[&](auto&&self,const vector<int>&P,B a,B al,int d)->void{
      if(d>=4){bool ok=true;for(int u:pool)if(a[u])for(int z=u;z<=T;z+=u)if(!a[z])ok=false;
        if(ok&&(p!=large||a[T])){U z=0,last=0;for(int u:pool)if(a[u]){z+=ex[u];last=ex[u];}g.push_back({a,al,d,z-last});}}
      if(d==5||(!large&&d==4)||d+int(P.size())<4)return;
      for(int i=0;i<(int)P.size();i++){int u=P[i];B aa=a;aa.set(u);B n=al&adj[u];vector<int>Q;for(int j=i+1;j<(int)P.size();j++)if(adj[u][P[j]])Q.push_back(P[j]);self(self,Q,aa,n,d+1);}
   };B all;all.set();dfs(dfs,pool,B{},all,0);if(!g.empty())groups.push_back({p,move(g)});
 }
 bool possible=false;long long n=0,np=0;unordered_map<U,bool> cache[2];
 for(int i=0;i<(int)groups.size();i++)for(int j=i+1;j<(int)groups.size();j++){
   if(large&&groups[i].first!=large&&groups[j].first!=large)continue;
   for(auto&a:groups[i].second)for(auto&b:groups[j].second)if(a.d+b.d<=9&&(b.a&~a.allow).none()){
      np++;
      int m=a.d+b.d; vector<int> us;for(int u:S){if(a.a[u])us.push_back(u);if(b.a[u])us.push_back(u);} // sorted
      // two distinct triple products <=M rule, or one for m=9 or known smooth M
      int h=0;bool close=false;
      for(int i=0;i<m&&!close;i++)for(int j=i+1;j<m&&!close;j++)for(int k=j+1;k<m;k++){
        int v=us[i]*us[j]*us[k];if(v>M)break;
        if(m==9||(!large&&v!=M)||(h&&h!=v)){close=true;break;}h=v;
      }
      if(close){triples++;continue;}
      int r=11-a.d-b.d; // m=8 -> r=3 (2 anchors + smooth), m=9 -> r=2
      U z=a.rest+b.rest;auto it=cache[r-2].find(z);bool ok;
      if(it!=cache[r-2].end())ok=it->second;else {ok=pack(z,M,r);cache[r-2][z]=ok;}
      if(ok)passed++;else{possible=true;n++;}
   }
 }
 allpairs+=np;if(possible){remain++;maxM=M;total+=n;cout<<M<<" "<<large<<" "<<np<<" "<<n<<" "<<cache[0].size()+cache[1].size()<<"\n";}
 else pass++;
}
cerr<<"ROWS EXCLUDED="<<pass<<" REMAIN="<<remain<<" MAX="<<maxM<<" PAIRS FAILED="<<total<<" ALL PAIRS="<<allpairs<<" PASSED="<<passed<<" TRIPLE="<<triples<<"\n";
}
