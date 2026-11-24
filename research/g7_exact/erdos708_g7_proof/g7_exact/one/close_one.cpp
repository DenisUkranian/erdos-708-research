#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <functional>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <unordered_map>
#include <vector>
using E=std::array<int,5>;
using Mask=std::vector<uint64_t>;
E PS{2,3,5,7,11};
extern "C" int skyline(const int*,int,int,int*);
struct S{int a,om,cf;E e;uint64_t key;};
uint64_t enc(E e){uint64_t k=0;for(int i=0;i<5;++i)k+=uint64_t(e[i])<<(7*i);return k;}
E dec(uint64_t k){E e{};for(int i=0;i<5;++i)e[i]=(k>>(7*i))&127;return e;}
bool pack(E e,const std::vector<int>&caps){
 for(int mode=0;mode<3;++mode){std::vector<int>b(caps.size(),1);bool ok=true;
  for(int i=4;i>=0&&ok;--i)for(int t=0;t<e[i]&&ok;++t){int best=-1;
   for(int j=0;j<int(b.size());++j)if(int64_t(b[j])*PS[i]<=caps[j]){
    if(best<0)best=j;
    else if(mode==1&&int64_t(caps[j])*b[best]<int64_t(caps[best])*b[j])best=j;
    else if(mode==2&&int64_t(caps[j])*b[best]>int64_t(caps[best])*b[j])best=j;
   }
   if(best<0)ok=false;else b[best]*=PS[i];
  }
  if(ok)return true;
 }
 return false;
}
int rough(int a,int i){for(int j=0;j<i;++j)while(a%PS[j]==0)a/=PS[j];return a;}
int allowance_mask(std::vector<S>c,const S&m,int M){
 c.push_back(m);std::vector<int>cf;int zeros=0;
 for(auto&s:c)if(s.e[4])cf.push_back(s.cf);else++zeros;
 std::sort(cf.rbegin(),cf.rend());std::array<std::vector<int>,4>rs;
 for(int i=0;i<4;++i){for(int j=1;j<int(cf.size());++j)rs[i].push_back(rough(cf[j],i));std::sort(rs[i].rbegin(),rs[i].rend());}
 int mask=0;
 for(int d=3;d<=6;++d){int z=7-d;if(d>int(cf.size())||z>zeros)continue;int r=z==1?1:z==2?2:z==3?4:5;int k=9-r-d;bool good=true;
  if(k==1){uint64_t u=1;for(int j=0;j<d-1;++j)u*=rs[0][j];good=u<=uint64_t(M/(r+2));}
  else for(int i=0;i<4;++i){uint64_t u=1,t=PS[i];for(int j=0;j<d-1;++j)u*=rs[i][j];for(int j=r+2;j<=r+k+1;++j)t*=std::max(M/(j*PS[i])+1,PS[i]);if(u>=t)good=false;}
  if(!good)mask|=1<<d;
 }
 return mask;
}
int count(const Mask&m){int k=0;for(auto x:m)k+=__builtin_popcountll(x);return k;}
bool empty(const Mask&m){for(auto x:m)if(x)return false;return true;}
void setbit(Mask&m,int i){m[i/64]|=uint64_t(1)<<(i%64);}
void clearbit(Mask&m,int i){m[i/64]&=~(uint64_t(1)<<(i%64));}
bool has(const Mask&m,int i){return m[i/64]>>(i%64)&1;}
int first(const Mask&m){for(int i=0;i<int(m.size());++i)if(m[i])return i*64+__builtin_ctzll(m[i]);return -1;}
bool union_cover(const E&e,int M){int used=0;for(int i=0;i<5;++i){bool done=false;for(int k=0;k<=9-used;++k){int s=0;for(int64_t p=PS[i];p<=M;p*=PS[i])s+=std::min(k,int(M/p));if(s>=e[i]){used+=k;done=true;break;}}if(!done)return false;}return true;}
bool core_cover(const std::vector<S>&A,int M){
 int d=0,z=0;E pe{},ze{},largest{};int maxcf=0;
 for(auto&s:A)if(s.e[4]){++d;for(int i=0;i<4;++i)pe[i]+=s.e[i];pe[4]+=s.e[4];if(s.cf>maxcf){maxcf=s.cf;largest=s.e;}}else{++z;for(int i=0;i<4;++i)ze[i]+=s.e[i];}
 assert(d>=3&&d<=6&&z==7-d);int r=z==1?1:z==2?2:z==3?4:5;
 E remaining=pe;remaining[4]=0;for(int i=0;i<4;++i)remaining[i]-=largest[i];
 int k=9-r-d;std::vector<int>caps;for(int j=r+2;j<=r+k+1;++j)caps.push_back(M/j);
 if(pack(remaining,caps))return true;
 int kp=0;
 for(;kp<=9;++kp){int supply=0;for(int64_t p=PS[4];p<=M;p*=PS[4])supply+=std::min(kp,int(M/p));if(supply>=pe[4])break;}
 E small=pe;small[4]=0;k=9-r-kp;caps.clear();for(int j=r+1;j<=r+k;++j)caps.push_back(M/j);
 if(k>=0&&pack(small,caps))return true;
 int gm=d==3?4:d==4?5:d==5?6:8;k=9-gm;caps.clear();for(int j=gm+1;j<=9;++j)caps.push_back(M/j);
 if(pack(ze,caps))return true;
 return false;
}
int main(int argc,char**argv){
 auto start=std::chrono::steady_clock::now();std::vector<S>small;
 for(int a=1;a<=24696;++a){int v=a;E e{};int om=0;for(int i=0;i<4;++i)while(v%PS[i]==0){v/=PS[i];++e[i];++om;}if(v==1)small.push_back({a,om,a,e,enc(e)});}
 uint64_t configs=0,rawpass=0,pairpass=0,closurepass=0,graphpass=0,residual=0,leaves=0,unique=0,corepass=0,unionpass=0,fullpackpass=0,unknowns=0;
 const std::string output_dir=argc>1?argv[1]:".";
 std::ofstream unknown_file(output_dir+"/unknown9.txt");
 std::ofstream passed_file(output_dir+"/frontier_pass9.txt");
 if(!unknown_file||!passed_file){std::cerr<<"Cannot open output files\n";return 2;}
 for(int p=11;p<=2744;++p){bool prime=true;for(int q=2;q*q<=p;++q)if(p%q==0)prime=false;if(!prime)continue;PS[4]=p;
  int top=std::min(24696,9*p*p-1);std::vector<S>all;
  for(auto s:small)if(s.a<=top)all.push_back(s);
  for(int ex=1;ex<=2;++ex){int64_t pow=ex==1?p:int64_t(p)*p;for(auto s:small)if(int64_t(s.a)*pow<=top){s.a*=pow;s.om+=ex;s.e[4]=ex;s.key=enc(s.e);all.push_back(s);}}
  std::sort(all.begin(),all.end(),[](const S&a,const S&b){return a.a<b.a;});
  for(const auto&m:all){int M=m.a;if(M<3*p||(M>=1890&&M<9*p))continue;++configs;
   std::vector<S>cs;for(auto s:all){if(s.a>=M)break;if(7*s.a>M&&s.om>1)cs.push_back(s);}
   if(!allowance_mask(cs,m,M)){++rawpass;continue;}
   std::unordered_map<uint64_t,bool>memo;std::vector<int>caps{M/7,M/8,M/9};
   auto good=[&](uint64_t k){auto it=memo.find(k);if(it!=memo.end())return it->second;bool yes=pack(dec(k),caps);memo[k]=yes;return yes;};
   cs.erase(std::remove_if(cs.begin(),cs.end(),[&](const S&s){return good(s.key+m.key);}),cs.end());
   if(cs.size()<6||!allowance_mask(cs,m,M)){++pairpass;continue;}
   std::map<int,int>index;for(int i=0;i<int(cs.size());++i)index[cs[i].a]=i;std::vector<bool>alive(cs.size(),true);
   for(int i=int(cs.size())-1;i>=0;--i){std::vector<uint64_t>forced{cs[i].key};
    for(int a=2*cs[i].a;a<=M;a+=cs[i].a){if(a==M)forced.push_back(m.key);else{auto it=index.find(a);if(it==index.end()||!alive[it->second]){alive[i]=false;break;}forced.push_back(cs[it->second].key);}}
    if(!alive[i])continue;
    for(int x=0;x<int(forced.size());++x)for(int y=x+1;y<int(forced.size());++y)if(good(forced[x]+forced[y]))alive[i]=false;
   }
   std::vector<S>nc;for(int i=0;i<int(cs.size());++i)if(alive[i])nc.push_back(cs[i]);cs.swap(nc);
   int allowed=allowance_mask(cs,m,M);
   if(cs.size()<6||!allowed){++closurepass;continue;}
   int N=cs.size(),W=(N+63)/64;std::vector<Mask>adj(N,Mask(W)),force(N,Mask(W));index.clear();for(int i=0;i<N;++i)index[cs[i].a]=i;
   for(int i=0;i<N;++i){setbit(force[i],i);for(int a=2*cs[i].a;a<M;a+=cs[i].a){assert(index.count(a));setbit(force[i],index[a]);}for(int j=i+1;j<N;++j)if(!good(cs[i].key+cs[j].key)){setbit(adj[i],j);setbit(adj[j],i);}}
   Mask initial(W);for(int i=0;i<N;++i)setbit(initial,i);
   std::unordered_map<uint64_t,int>status;std::map<uint64_t,std::vector<S>>unknown,passed;uint64_t local_leaves=0;
   std::function<void(Mask,Mask,int,int,int)>dfs=[&](Mask avail,Mask sel,int num,int supp,int g){
    if(num==7){
     if(!(allowed>>supp&1)||g!=1)return;++leaves;++local_leaves;
     std::vector<S>A{m};uint64_t key=m.key;for(int i=0;i<N;++i)if(has(sel,i)){A.push_back(cs[i]);key+=cs[i].key;}
     if(status[key]==1)return;
     if(core_cover(A,M)){if(status[key]==0){++unique;++corepass;}else unknown.erase(key);status[key]=1;passed[key]=A;return;}
     if(status[key]==2)return;++unique;E demand=dec(key);
     if(union_cover(demand,M)){++unionpass;status[key]=1;passed[key]=A;return;}
     std::vector<int>fullcaps;for(int j=1;j<=9;++j)fullcaps.push_back(M/j);
     if(pack(demand,fullcaps)){++fullpackpass;status[key]=1;passed[key]=A;return;}
     status[key]=2;unknown[key]=A;return;
    }
    if(num+count(avail)<7)return;
    int possible=supp;for(int i=0;i<N;++i)if(has(avail,i)&&cs[i].e[4])++possible;bool supportok=false;for(int d=supp;d<=possible&&d<=6;++d)if(allowed>>d&1)supportok=true;if(!supportok)return;
    while(!empty(avail)){
      int j=first(avail);Mask f=force[j];clearbit(avail,j);bool valid=true;int added=0,ns=supp,ng=g;
      for(int i=0;i<N;++i)if(has(f,i)&&!has(sel,i)){if(i!=j&&!has(avail,i)){valid=false;break;}++added;ns+=cs[i].e[4]>0;ng=std::gcd(ng,cs[i].a);}
      if(!valid||num+added>7)continue;Mask next=avail,nsel=sel;
      for(int i=0;i<N;++i)if(has(f,i)){setbit(nsel,i);for(int w=0;w<W;++w)next[w]&=adj[i][w];}
      dfs(next,nsel,num+added,ns,ng);
    }
    return;
   };
   dfs(initial,Mask(W),1,m.e[4]>0,M);
   if(local_leaves)++residual;else++graphpass;
   std::vector<int>inputs,outputs;for(auto&[key,st]:status)for(int e:dec(key))inputs.push_back(e);outputs.resize(inputs.size());
   int K=status.empty()?0:skyline(inputs.data(),status.size(),5,outputs.data());int local_unknown=0;
   for(int j=0;j<K;++j){E e{};for(int i=0;i<5;++i)e[i]=outputs[5*j+i];uint64_t key=enc(e);
    if(status[key]==2){++unknowns;++local_unknown;unknown_file<<M<<" "<<p;for(int z:e)unknown_file<<" "<<z;for(auto&s:unknown[key])unknown_file<<" "<<s.a;unknown_file<<"\n";}
    else {passed_file<<M<<" "<<p;for(int z:e)passed_file<<" "<<z;for(auto&s:passed[key])passed_file<<" "<<s.a;passed_file<<"\n";}
   }
   if(local_unknown){unknown_file.flush();passed_file.flush();std::cout<<"UNKNOWN M="<<M<<" P="<<p<<" leaves="<<local_leaves<<" demands="<<status.size()<<" skyline="<<K<<" unknown="<<local_unknown<<std::endl;}
  }
 }
 std::cerr<<"DONE configs="<<configs<<" raw="<<rawpass<<" pair="<<pairpass<<" closure="<<closurepass<<" graph="<<graphpass<<" residual="<<residual<<" leaves="<<leaves<<" unique="<<unique<<" core="<<corepass<<" union="<<unionpass<<" fullpack="<<fullpackpass<<" unknown="<<unknowns<<" seconds="<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"\n";
}
