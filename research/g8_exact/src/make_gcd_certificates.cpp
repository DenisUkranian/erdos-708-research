#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using E=std::array<int,4>;
const int P[4]={2,3,5,7};
struct Factor{int number,shift;E exponent;};

int main(int argc, char**argv){
 if(argc!=4){std::cerr<<"usage: make_gcd_certificates DEMANDS CERTS RESIDUAL\n";return 1;}
 std::ifstream file(argv[1]); assert(file);
 std::ofstream certificates(argv[2]),remaining(argv[3]);
 std::map<int,std::vector<E>> demands;int M;E e{};
 while(file>>M>>e[0]>>e[1]>>e[2]>>e[3])demands[M].push_back(e);
 size_t solved=0,unsolved=0;
 for(const auto& [M, D]:demands){
  E cap{};for(const E& d:D)for(int k=0;k<4;k++)cap[k]=std::max(cap[k],d[k]);
  int stride[4],N=1;
  for(int k=0;k<4;k++){stride[k]=N;N*=cap[k]+1;}
  std::vector<E> power(N);
  for(int z=0;z<N;z++)for(int k=0;k<4;k++)power[z][k]=(z/stride[k])%(cap[k]+1);
  std::vector<Factor> factors;
  for(int h=2;h<=M;h++){
   int v=h;E exp{};
   for(int k=0;k<4;k++)while(v%P[k]==0){v/=P[k];exp[k]++;}
   if(v!=1)continue;
   bool fits=true;int off=0;
   for(int k=0;k<4;k++){if(exp[k]>cap[k])fits=false;off+=exp[k]*stride[k];}
   if(fits)factors.push_back({h,off,exp});
  }
  std::vector<std::vector<int32_t>> predecessor(12,std::vector<int32_t>(N,-1));
  std::vector<std::vector<uint16_t>> choice(12,std::vector<uint16_t>(N,0));
  std::vector<int> reachable={0};
  std::vector<uint8_t> seen(N,0);
  for(int j=1;j<=11;j++){
   std::fill(seen.begin(),seen.end(),0);
   std::vector<int> next;next.reserve(N);
   for(int z:reachable){seen[z]=1;next.push_back(z);predecessor[j][z]=z;choice[j][z]=1;}
   for(int z:reachable){
    const E& old=power[z];
    for(const Factor& h:factors){
     int gcd=1;bool legal=true;
     for(int k=0;k<4;k++){
      if(old[k]+h.exponent[k]>cap[k]){legal=false;break;}
      for(int x=0;x<std::min(old[k],h.exponent[k]);x++)gcd*=P[k];
      if(gcd>M/j){legal=false;break;}
     }
     if(!legal)continue;
     int w=z+h.shift;
     if(!seen[w]){
      seen[w]=1;next.push_back(w);predecessor[j][w]=z;choice[j][w]=h.number;
     }
    }
   }
   reachable.swap(next);
  }
  std::vector<int32_t> dominated_by(N,-1);
  for(int z:reachable)dominated_by[z]=z;
  for(int k=0;k<4;k++){
   int st=stride[k];
   for(int z=N-1;z>=0;z--)if(power[z][k]<cap[k] && dominated_by[z]<0)
    dominated_by[z]=dominated_by[z+st];
  }
  for(const E& d:D){
   int z=0;for(int k=0;k<4;k++)z+=d[k]*stride[k];
   if(dominated_by[z]<0){
    ++unsolved;remaining<<M;for(int x:d)remaining<<' '<<x;remaining<<'\n';
    continue;
   }
   ++solved;int state=dominated_by[z];
   uint16_t order[11];
   for(int j=11;j>=1;j--){
    assert(state>=0);
    order[j-1]=choice[j][state];
    assert(order[j-1]>0);
    state=predecessor[j][state];
   }
   assert(state==0);
   certificates<<M;for(int x:d)certificates<<' '<<x;
   certificates<<" 11";for(int j=0;j<11;j++)certificates<<' '<<order[j];
   certificates<<'\n';
  }
 }
 std::cout<<"CERTIFICATES="<<solved<<" CRT_RESIDUAL="<<unsolved<<"\n";
 assert(solved+unsolved==57515 && unsolved==28);
}
