#include <bits/stdc++.h>
using namespace std;
using E=array<int,4>;
constexpr int pr[4]={2,3,5,7};
struct Src{int a,om; E e;}; vector<Src> src;
E add(E a,E b){for(int i=0;i<4;i++)a[i]+=b[i];return a;}
bool pack(const E &e,int M,int first,int last){
 int c[11]={},B[11]={},s=last-first+1;for(int j=0;j<s;j++)c[j]=M/(first+j);
 vector<int> factors; for(int i=3;i>=0;i--)for(int k=0;k<e[i];k++)factors.push_back(pr[i]);
 for(int mode=0;mode<5;mode++){
  fill(B,B+s,1);bool ok=true;
  for(int p:factors){int best=-1;
   for(int j=0;j<s;j++){if(B[j]>c[j]/p)continue;
    if(best<0 ||(mode==0&&B[j]<B[best])||(mode==1&&B[j]>B[best])||
      (mode==2&&1ll*B[j]*c[best]<1ll*B[best]*c[j])||
      (mode==3&&1ll*B[j]*c[best]>1ll*B[best]*c[j])||
      (mode==4&&1ll*B[j]*c[best]<1ll*B[best]*c[j]))best=j;
   }
   if(best<0){ok=false;break;}B[best]*=p;
  }
  if(ok)return true;
 }
 return false;
}
void gen(){for(int i=2;i<=11537;i++){int x=i;E e{};int om=0;for(int j=0;j<4;j++)while(x%pr[j]==0){x/=pr[j];e[j]++;om++;}if(x==1)src.push_back({i,om,e});}}
int main(int argc,char**argv){assert(argc==2);gen();ofstream outfile(argv[1]);assert(outfile.good());int count=0,clique_max=0;unsigned long long total=0,distinct=0;auto start=chrono::steady_clock::now();
 for(auto m:src){int M=m.a;if(M<=11||m.om<3)continue;
 vector<Src> C;for(auto s:src){if(s.a>=M)break;if(11*s.a>M&&s.om>=3&&!pack(add(m.e,s.e),M,9,11))C.push_back(s);}
 int N=C.size();if(N<7)continue;assert(N<=64);
 vector<uint64_t> adj(N);for(int i=0;i<N;i++)for(int j=i+1;j<N;j++)if(!pack(add(C[i].e,C[j].e),M,9,11)){adj[i]|=1ull<<j;adj[j]|=1ull<<i;}
 vector<vector<uint64_t>> bad3(N,vector<uint64_t>(N));
 for(int i=0;i<N;i++)for(int j=i+1;j<N;j++)if(adj[i]&(1ull<<j)){
   E ab=add(C[i].e,C[j].e);
   for(int k=j+1;k<N;k++)if((adj[i]&(1ull<<k))&&(adj[j]&(1ull<<k))){
    if(!pack(add(ab,C[k].e),M,7,11))bad3[i][j]|=1ull<<k;
   }
 }
 uint64_t leaves=0;unordered_set<uint32_t> ds;vector<int> chosen;E all=m.e;
 auto dfs=[&](auto&&rec,uint64_t avail,int left,E e)->void{
  if(left==0){leaves++;uint32_t key=e[0]+(e[1]<<7)+(e[2]<<14)+(e[3]<<21);ds.insert(key);return;}
  while(__builtin_popcountll(avail)>=left){int i=__builtin_ctzll(avail);avail&=avail-1;uint64_t nxt=avail&adj[i];
    for(int j=0;j<(int)chosen.size();j++)nxt&=bad3[chosen[j]][i];
    if(__builtin_popcountll(nxt)<left-1)continue;
    chosen.push_back(i);rec(rec,nxt,left-1,add(e,C[i].e));chosen.pop_back();
  }
 };
 dfs(dfs,(N==64?~0ull:(1ull<<N)-1),7,all);
 if(leaves){for(auto key:ds)outfile<<M<<" "<<(key&127)<<" "<<((key>>7)&127)<<" "<<((key>>14)&127)<<" "<<((key>>21)&127)<<"\n";count++;clique_max=M;total+=leaves;distinct+=ds.size();cout<<M<<" C="<<N<<" source_sets="<<leaves<<" demand_vectors="<<ds.size()<<"\n";}
 }
 cerr<<"M_with_uncleared="<<count<<" last="<<clique_max<<" total_sets="<<total<<" total_demand_vectors="<<distinct<<" seconds="<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n";
}
