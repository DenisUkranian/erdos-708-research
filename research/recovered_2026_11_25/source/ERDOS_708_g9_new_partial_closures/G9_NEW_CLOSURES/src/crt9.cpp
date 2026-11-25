#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <set>
#include <unordered_set>
#include <vector>
using V=std::array<int,5>;
const V PS{2,3,5,7,11};
struct PInfo{int p,d,wp;std::vector<std::vector<int>>rows;};
uint64_t nodes=0,exactcalls=0,full=0;

int greedy(const std::vector<V>&v,const V&D,int k) {
  int best=1000;
  for(int mode=0;mode<3;++mode) {
    V rem=D;std::vector<bool>used(v.size(),false);int picked=0;
    while(true) {
      bool done=true;for(int i=0;i<k;++i)if(rem[i])done=false;
      if(done){best=std::min(best,picked);break;}
      if(picked>=best||picked>9)break;
      int pos=-1,score=0;
      for(int j=0;j<int(v.size());++j)if(!used[j]) {
        int gain=0;
        for(int i=0;i<k;++i)gain+=std::min(rem[i],v[j][i])*(mode==1?1000/(D[i]+1):mode==2?1000/(rem[i]+1):1);
        if(gain>score){score=gain;pos=j;}
      }
      if(pos<0)break;
      used[pos]=true;++picked;
      for(int i=0;i<k;++i)rem[i]=std::max(0,rem[i]-v[pos][i]);
    }
  }
  return best;
}

bool exact(const std::vector<V>&v,const V&D,int dim,int budget) {
  ++exactcalls;
  std::map<V,int>mp;
  for(auto a:v){for(int i=dim;i<5;++i)a[i]=0;bool any=false;for(int i=0;i<dim;++i)if(a[i])any=true;if(any)++mp[a];}
  std::vector<std::pair<V,int>>pr(mp.begin(),mp.end());
  std::sort(pr.begin(),pr.end(),[&](auto&a,auto&b){
    int x=0,y=0;for(int i=0;i<dim;++i){x+=a.first[i]+5*(a.first[i]>0);y+=b.first[i]+5*(b.first[i]>0);}return x>y;
  });
  int N=pr.size();std::vector<V>mx(N+1),sum(N+1);
  for(int j=N-1;j>=0;--j)for(int i=0;i<dim;++i){mx[j][i]=std::max(mx[j+1][i],pr[j].first[i]);sum[j][i]=sum[j+1][i]+pr[j].first[i]*pr[j].second;}
  std::unordered_set<uint64_t>bad;
  std::function<bool(int,int,V)>dfs=[&](int j,int left,V rem){
    bool done=true;for(int i=0;i<dim;++i)if(rem[i])done=false;
    if(done)return true;if(!left||j==N)return false;
    for(int i=0;i<dim;++i)if(rem[i]>left*mx[j][i]||rem[i]>sum[j][i])return false;
    uint64_t key=uint64_t(j)<<40|uint64_t(left)<<48;
    for(int i=0;i<dim;++i)key|=uint64_t(rem[i])<<(7*i);
    if(bad.count(key))return false;
    for(int take=std::min(left,pr[j].second);take>=0;--take){
      V next=rem;for(int i=0;i<dim;++i)next[i]=std::max(0,next[i]-take*pr[j].first[i]);
      if(dfs(j+1,left-take,next))return true;
    }
    bad.insert(key);return false;
  };
  return dfs(0,budget,D);
}

int suffix_bound(const std::vector<PInfo>&pi,int start,int M){
  int cost=0;std::vector<int>small;
  for(int i=start;i<int(pi.size());++i){
    int power=1;bool fits=true;
    for(int e=0;e<pi[i].d;++e){if(power>M/pi[i].p){fits=false;break;}power*=pi[i].p;}
    if(fits)small.push_back(power);else cost+=pi[i].wp;
  }
  std::sort(small.rbegin(),small.rend());std::vector<int>bins;
  for(int a:small){bool placed=false;for(int&b:bins)if(b<=M/a){b*=a;placed=true;break;}if(!placed)bins.push_back(a);}
  return cost+bins.size();
}

bool check(int M,const V&original) {
  assert(M>0&&M<=2401);
  for(int d:original)assert(d>=0&&d<128);
  std::vector<PInfo>pi;
  for(int i=0;i<5;++i)if(original[i]) {
    int p=PS[i],q=1,h=0;
    while(q<=M/p&&h<original[i]){q*=p;++h;}
    assert(h>0);PInfo info{p,original[i],0,{}};
    std::set<std::vector<int>>unique;
    for(int r=0;r<q;++r) {
      std::vector<int>row(M),vs;
      for(int j=1;j<=M;++j){int x=r+j,z=0;while(z<h&&x%p==0){++z;x/=p;}row[j-1]=z;vs.push_back(z);}
      std::sort(vs.rbegin(),vs.rend());int supply=0,picks=0;
      for(int a:vs){supply+=a;++picks;if(supply>=info.d)break;}
      assert(supply>=info.d);info.wp=std::max(info.wp,picks);unique.insert(row);
    }
    info.rows.assign(unique.begin(),unique.end());pi.push_back(info);
  }
  std::sort(pi.begin(),pi.end(),[](auto&a,auto&b){if(a.wp!=b.wp)return a.wp>b.wp;return a.rows.size()<b.rows.size();});
  int K=pi.size();V D{};for(int i=0;i<K;++i)D[i]=pi[i].d;
  std::vector<int>suffix(K+1);for(int i=0;i<=K;++i)suffix[i]=suffix_bound(pi,i,M);
  std::vector<V>vals(M);std::vector<int>choices(K);
  std::function<bool(int)>dfs=[&](int k){
    ++nodes;
    if(suffix[k]<=9){
      int allowance=9-suffix[k];
      if(k==0)return true;
      int g=greedy(vals,D,k);
      if(g<=allowance)return true;
      if(allowance>0&&(k==K||g<=allowance+2)&&exact(vals,D,k,allowance))return true;
    }
    if(k==K){++full;std::cerr<<"UNPROVED M="<<M<<" demand=";for(int x:original)std::cerr<<x<<",";std::cerr<<" choices=";for(int x:choices)std::cerr<<x<<",";std::cerr<<"\n";return false;}
    for(int r=0;r<int(pi[k].rows.size());++r){choices[k]=r;for(int j=0;j<M;++j)vals[j][k]=pi[k].rows[r][j];if(!dfs(k+1))return false;}
    return true;
  };
  return dfs(0);
}

int main(int argc,char**argv){
  assert(argc==2);std::ifstream in(argv[1]);assert(in.good());int M,rows=0;V e{};auto start=std::chrono::steady_clock::now();
  while(in>>M>>e[0]>>e[1]>>e[2]>>e[3]>>e[4]) {
    if(!check(M,e))return 2;
    ++rows;
    std::cout<<"PASS "<<rows<<" M="<<M<<" nodes="<<nodes<<" exact="<<exactcalls<<" sec="<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<std::endl;
  }
  std::cout<<"ALL_PASS rows="<<rows<<" nodes="<<nodes<<" exact="<<exactcalls<<" sec="<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<std::endl;
}
