#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using E=std::array<int,4>;
const E P{2,3,5,7};
struct Source{int a,omega;E e;uint64_t key;};
std::map<int,std::vector<E>>slots,crt;
bool factor(int a,E&e){e={};for(int i=0;i<4;++i)while(a%P[i]==0){a/=P[i];++e[i];}return a==1;}
uint64_t encode(E e){uint64_t k=0;for(int i=0;i<4;++i){assert(e[i]<128);k+=uint64_t(e[i])<<(7*i);}return k;}
E decode(uint64_t k){E e{};for(int i=0;i<4;++i)e[i]=(k>>(7*i))&127;return e;}
bool dominates(const E&a,const E&b){for(int i=0;i<4;++i)if(a[i]<b[i])return false;return true;}

bool pack(const E&e,int M,int first,int last){
  int N=last-first+1;std::vector<int>caps(N);for(int j=0;j<N;++j)caps[j]=M/(j+first);
  for(int mode=0;mode<3;++mode){
    std::vector<int>bins(N,1);bool ok=true;
    for(int i=3;i>=0&&ok;--i)for(int z=0;z<e[i]&&ok;++z){
      int best=-1;
      for(int j=0;j<N;++j)if(bins[j]*P[i]<=caps[j]){
        if(best<0)best=j;
        else if(mode==1&&int64_t(caps[j])*bins[best]<int64_t(caps[best])*bins[j])best=j;
        else if(mode==2&&int64_t(caps[j])*bins[best]>int64_t(caps[best])*bins[j])best=j;
      }
      if(best<0)ok=false;else bins[best]*=P[i];
    }
    if(ok){E total{};for(int j=0;j<N;++j){assert(bins[j]<=caps[j]);E v{};assert(factor(bins[j],v));for(int i=0;i<4;++i)total[i]+=v[i];}assert(total==e);return true;}
  }
  return false;
}

bool prime_union(const E&e,int M){
  int count=0;
  for(int i=0;i<4;++i){
    bool success=false;
    for(int k=0;k<=9-count;++k){
      int got=0;for(int p=P[i];p<=M;p*=P[i])got+=std::min(k,M/p);
      if(got>=e[i]){count+=k;success=true;break;}
    }
    if(!success)return false;
  }
  return true;
}

void load_slots(const char*path){
  std::ifstream f(path);assert(f.good());int M;
  while(f>>M){
    E demand{};for(int&i:demand)f>>i;int length;f>>length;assert(length<=9);E total{};
    for(int j=1;j<=length;++j){
      int h;f>>h;assert(h>=1&&h<=M);E e{};assert(factor(h,e));int overlap=1;
      for(int i=0;i<4;++i)for(int t=0;t<std::min(e[i],total[i]);++t)overlap*=P[i];
      assert(overlap<=M/j);for(int i=0;i<4;++i)total[i]+=e[i];
    }
    assert(dominates(total,demand));slots[M].push_back(demand);
  }
}
void load_crt(const char*path){
  std::ifstream f(path);assert(f.good());int M;E e{};
  while(f>>M>>e[0]>>e[1]>>e[2]>>e[3])crt[M].push_back(e);
}

int main(int argc,char**argv){
  assert(argc==3);load_slots(argv[1]);load_crt(argv[2]);
  auto start=std::chrono::steady_clock::now();std::vector<Source>all;
  for(int a=2;a<12555;++a){E e{};if(!factor(a,e))continue;int om=0;for(int z:e)om+=z;all.push_back({a,om,e,encode(e)});}
  uint64_t total_cliques=0,total_demands=0,by_union=0,by_pack=0,by_slots=0,by_crt=0;
  int maxima=0,clique_maxima=0,last_clique_M=0;
  for(const auto&m:all){
    if(m.a<=9)continue;++maxima;
    std::unordered_map<uint64_t,bool>paircache;
    auto good_pair=[&](uint64_t e){auto it=paircache.find(e);if(it!=paircache.end())return it->second;bool yes=pack(decode(e),m.a,7,9);paircache[e]=yes;return yes;};
    std::vector<Source>c;
    for(const auto&s:all){if(s.a>=m.a)break;if(9*s.a>m.a&&s.omega>1&&!good_pair(s.key+m.key))c.push_back(s);}
    if(c.size()<6)continue;
    assert(c.size()<64);std::vector<uint64_t>adj(c.size(),0);
    for(int i=0;i<int(c.size());++i)for(int j=i+1;j<int(c.size());++j)if(!good_pair(c[i].key+c[j].key)){adj[i]|=uint64_t(1)<<j;adj[j]|=uint64_t(1)<<i;}
    uint64_t local_cliques=0;std::unordered_set<uint64_t>seen;std::vector<int>chosen;
    std::function<void(uint64_t,int,uint64_t)>visit=[&](uint64_t mask,int left,uint64_t key){
      if(left==0){
        ++local_cliques;++total_cliques;if(!seen.insert(key).second)return;++total_demands;E e=decode(key);
        if(prime_union(e,m.a)){++by_union;return;}
        if(pack(e,m.a,1,9)){++by_pack;return;}
        for(const E&v:slots[m.a])if(dominates(v,e)){++by_slots;return;}
        for(const E&v:crt[m.a])if(dominates(v,e)){++by_crt;return;}
        std::cerr<<"UNCOVERED M="<<m.a<<" A=";for(int a:chosen)std::cerr<<a<<",";std::cerr<<m.a<<" demand=";for(int z:e)std::cerr<<z<<",";std::cerr<<"\n";std::exit(2);
      }
      while(__builtin_popcountll(mask)>=left){
        uint64_t bit=mask&-mask;mask-=bit;int j=__builtin_ctzll(bit);
        chosen.push_back(c[j].a);visit(mask&adj[j],left-1,key+c[j].key);chosen.pop_back();
      }
    };
    visit((uint64_t(1)<<c.size())-1,6,m.key);
    if(local_cliques){++clique_maxima;last_clique_M=m.a;}
  }
  std::cout<<"{\"status\":\"PASS_PENDING_CRT_VERIFICATION\",\"smooth_maxima\":"<<maxima
    <<",\"clique_maxima\":"<<clique_maxima<<",\"largest_clique_maximum\":"<<last_clique_M
    <<",\"actual_seven_cliques\":"<<total_cliques<<",\"unique_demands\":"<<total_demands
    <<",\"prime_union\":"<<by_union<<",\"ordinary_bins\":"<<by_pack<<",\"cumulative_gcd\":"<<by_slots
    <<",\"crt_dominated\":"<<by_crt<<",\"seconds\":"<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"}\n";
}
