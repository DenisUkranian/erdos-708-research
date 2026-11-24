#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <unordered_set>
#include <vector>
struct BigNat {
  std::array<uint32_t,16> digits{};int len=1;
  explicit BigNat(uint32_t x){digits[0]=x;}
  void multiply(uint32_t x) {
    uint64_t carry=0;
    for(int i=0;i<len;++i){uint64_t z=uint64_t(digits[i])*x+carry;digits[i]=z%1000000000;carry=z/1000000000;}
    while(carry){assert(len<16);digits[len++]=carry%1000000000;carry/=1000000000;}
  }
  bool operator<(const BigNat &other)const {
    if(len!=other.len)return len<other.len;
    for(int i=len-1;i>=0;--i)if(digits[i]!=other.digits[i])return digits[i]<other.digits[i];
    return false;
  }
};
using Vec=std::array<int,5>;
const Vec primes{2,3,5,7,11};
int n,B,top,dim;
struct Source { int a,omega,largest; Vec e; uint64_t key; };
std::map<int,std::vector<Vec>> certs;
uint64_t subset_count=0,demand_count=0,by_union=0,by_bins=0,by_cert=0;
uint64_t pruned_subsets=0,pruned_branches=0;
uint64_t rough_pruned_subsets=0,rough_pruned_branches=0;

Vec decode(uint64_t key) {
  Vec out{};for(int i=0;i<dim;++i) out[i]=(key>>(7*i))&127;return out;
}
bool factor(int a,Vec &out) {
  out={};for(int i=0;i<dim;++i)while(a%primes[i]==0){a/=primes[i];++out[i];}
  return a==1;
}
int rough(int a,int first) {
  for(int i=0;i<first;++i)while(a%primes[i]==0)a/=primes[i];return a;
}
bool rough_envelope(const std::vector<Source>&c,const Source&m) {
  if(primes[dim-1]>m.a/B)return false;
  for(int i=0;i<dim;++i) {
    std::vector<int> vals;for(const auto&s:c)vals.push_back(rough(s.a,i));
    std::sort(vals.begin(),vals.end(),std::greater<int>());
    BigNat upper(rough(m.a,i)),lower(primes[i]);
    for(int j=0;j<n-1;++j)upper.multiply(vals[j]);
    for(int j=1;j<=B;++j)lower.multiply(std::max(m.a/(j*primes[i])+1,primes[i]));
    if(!(upper<lower))return false;
  }
  return true;
}
bool union_bound(const Vec&e,int M) {
  int used=0;
  for(int i=0;i<dim;++i) {
    bool found=false;
    for(int k=0;k<=B-used;++k) {
      int supplied=0;
      for(int p=primes[i];p<=M;p*=primes[i])supplied+=std::min(k,M/p);
      if(supplied>=e[i]){used+=k;found=true;break;}
    }
    if(!found)return false;
  }
  return true;
}
bool bin_bound(const Vec&e,int M) {
  for(int mode=0;mode<3;++mode) {
    std::vector<int> bins(B,1);bool ok=true;
    for(int i=dim-1;i>=0&&ok;--i) for(int j=0;j<e[i]&&ok;++j) {
      int best=-1;
      for(int k=0;k<B;++k)if(bins[k]*primes[i]<=M/(k+1)) {
        if(best<0)best=k;
        else if(mode==1 && int64_t(M/(k+1))*bins[best]<int64_t(M/(best+1))*bins[k])best=k;
        else if(mode==2 && int64_t(M/(k+1))*bins[best]>int64_t(M/(best+1))*bins[k])best=k;
      }
      if(best<0)ok=false;else bins[best]*=primes[i];
    }
    if(ok) {
      Vec got{};
      for(int j=0;j<B;++j) {
        assert(bins[j]<=M/(j+1));Vec v{};assert(factor(bins[j],v));
        for(int i=0;i<dim;++i)got[i]+=v[i];
      }
      assert(got==e);return true;
    }
  }
  return false;
}
bool certificate_bound(const Vec&e,int M) {
  for(const auto&v:certs[M]) {
    bool dominates=true;for(int i=0;i<dim;++i)if(e[i]>v[i])dominates=false;
    if(dominates)return true;
  }
  return false;
}
void load_certificates(const std::string &path) {
  std::ifstream in(path);assert(in.good());int M;
  while(in>>M) {
    Vec demand{};for(int i=0;i<dim;++i)in>>demand[i];
    int len;in>>len;assert(len<=B);Vec used{};
    for(int j=1;j<=len;++j) {
      int h;in>>h;assert(1<=h&&h<=M);Vec v{};assert(factor(h,v));
      int overlap=1;
      for(int i=0;i<dim;++i)for(int k=0;k<std::min(used[i],v[i]);++k)overlap*=primes[i];
      assert(overlap<=M/j);
      for(int i=0;i<dim;++i)used[i]+=v[i];
    }
    for(int i=0;i<dim;++i)assert(used[i]>=demand[i]);
    certs[M].push_back(demand);
  }
}
int main(int argc,char**argv) {
  assert(argc==6);n=std::stoi(argv[1]);B=std::stoi(argv[2]);
  top=std::stoi(argv[3]);dim=std::stoi(argv[4]);
  auto start=std::chrono::steady_clock::now();load_certificates(argv[5]);
  std::vector<Source> all;
  for(int a=2;a<top;++a) {
    Vec e{};if(!factor(a,e))continue;
    Source s{a,0,0,e,0};
    for(int i=0;i<dim;++i){s.omega+=e[i];if(e[i])s.largest=primes[i];s.key+=uint64_t(e[i])<<(7*i);}
    all.push_back(s);
  }
  int smooth_maxima=0,envelope_maxima=0,enumerated_maxima=0;
  for(const auto&m:all) {
    if(m.a<=B||m.omega<3)continue;
    std::vector<Source> c;
    for(const auto&s:all) {
      if(s.a>=m.a)break;
      if(s.omega>=3&&(B-1)*s.a>m.a*s.largest)c.push_back(s);
    }
    if(int(c.size())<n-1)continue;++smooth_maxima;
    if(rough_envelope(c,m)){++envelope_maxima;continue;}
    ++enumerated_maxima;
    std::unordered_set<uint64_t> seen;seen.reserve(200000);
    std::vector<std::vector<Vec>> upper(c.size()+1,std::vector<Vec>(n));
    std::vector<std::vector<uint64_t>> choose(c.size()+1,std::vector<uint64_t>(n));
    for(int a=0;a<=int(c.size());++a){choose[a][0]=1;for(int b=1;b<n&&b<=a;++b)choose[a][b]=choose[a-1][b-1]+choose[a-1][b];}
    for(int from=int(c.size())-1;from>=0;--from)for(int left=1;left<n&&left<=int(c.size())-from;++left) {
      for(int i=0;i<dim;++i) {
        upper[from][left][i]=c[from].e[i]+upper[from+1][left-1][i];
        if(left<int(c.size())-from)upper[from][left][i]=std::max(upper[from][left][i],upper[from+1][left][i]);
      }
    }
    using U128=unsigned __int128;
    using RVec=std::array<U128,5>;
    std::vector<std::vector<RVec>> rough_upper(c.size()+1,std::vector<RVec>(n));
    std::array<std::array<U128,128>,5> powers{};
    RVec failed_at_threshold{};
    if(n>=9) {
      assert(m.a<=4000); // all larger maxima must have passed the global envelope
      U128 global_cap=1;for(int i=0;i<n;++i)global_cap*=m.a;
      for(int i=0;i<dim;++i) {
        powers[i][0]=1;
        for(int e=1;e<128;++e) {
          if(powers[i][e-1]>global_cap/primes[i])powers[i][e]=global_cap+1;
          else powers[i][e]=powers[i][e-1]*primes[i];
        }
        U128 value=primes[i];
        for(int j=1;j<=B;++j) {
          int factor=std::max(m.a/(j*primes[i])+1,primes[i]);
          if(value>global_cap/factor){value=global_cap+1;break;}
          value*=factor;
        }
        failed_at_threshold[i]=value;
      }
      for(int from=0;from<=int(c.size());++from)for(int i=0;i<dim;++i)rough_upper[from][0][i]=1;
      for(int from=int(c.size())-1;from>=0;--from)for(int left=1;left<n&&left<=int(c.size())-from;++left) {
        for(int i=0;i<dim;++i) {
          rough_upper[from][left][i]=rough(c[from].a,i)*rough_upper[from+1][left-1][i];
          if(left<int(c.size())-from)rough_upper[from][left][i]=std::max(rough_upper[from][left][i],rough_upper[from+1][left][i]);
        }
      }
    }
    std::vector<int> chosen;
    std::function<void(int,int,uint64_t)> visit=[&](int from,int left,uint64_t key) {
      if(left==0) {
        ++subset_count;if(!seen.insert(key).second)return;++demand_count;
        Vec e=decode(key);
        if(union_bound(e,m.a)){++by_union;return;}
        if(bin_bound(e,m.a)){++by_bins;return;}
        if(certificate_bound(e,m.a)){++by_cert;return;}
        std::cerr<<"UNVERIFIED M="<<m.a<<" source=";
        for(int a:chosen)std::cerr<<a<<",";std::cerr<<m.a<<" demand=";
        for(int i=0;i<dim;++i)std::cerr<<e[i]<<",";std::cerr<<"\n";std::exit(2);
      }
      if(n>=9&&left>=2) {
        Vec ceiling=decode(key);
        if(primes[dim-1]<=m.a/B) {
          U128 partial=1;bool all_above=true;
          for(int i=dim-1;i>=0;--i) {
            partial*=powers[i][ceiling[i]];
            if(partial*rough_upper[from][left][i]>=failed_at_threshold[i])all_above=false;
          }
          if(all_above) {
            uint64_t count=choose[c.size()-from][left];
            subset_count+=count;rough_pruned_subsets+=count;++rough_pruned_branches;return;
          }
        }
        for(int i=0;i<dim;++i)ceiling[i]+=upper[from][left][i];
        if(union_bound(ceiling,m.a)) {
          uint64_t count=choose[c.size()-from][left];
          subset_count+=count;pruned_subsets+=count;++pruned_branches;return;
        }
      }
      for(int j=from;j<=int(c.size())-left;++j) {
        chosen.push_back(c[j].a);visit(j+1,left-1,key+c[j].key);chosen.pop_back();
      }
    };
    visit(0,n-1,m.key);
  }
  double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
  std::cout<<"{\"status\":\"PASS\",\"n\":"<<n<<",\"B\":"<<B
           <<",\"cutoff_exclusive\":"<<top<<",\"smooth_maxima\":"<<smooth_maxima
           <<",\"rough_envelope_maxima\":"<<envelope_maxima
           <<",\"enumerated_maxima\":"<<enumerated_maxima
           <<",\"actual_subsets\":"<<subset_count<<",\"unique_demands\":"<<demand_count
           <<",\"prime_union_demands\":"<<by_union<<",\"bin_demands\":"<<by_bins
           <<",\"certificate_demands\":"<<by_cert
           <<",\"prime_union_pruned_branches\":"<<pruned_branches
           <<",\"prime_union_pruned_subsets\":"<<pruned_subsets
           <<",\"rough_pruned_branches\":"<<rough_pruned_branches
           <<",\"rough_pruned_subsets\":"<<rough_pruned_subsets
           <<",\"seconds\":"<<elapsed<<"}\n";
}
