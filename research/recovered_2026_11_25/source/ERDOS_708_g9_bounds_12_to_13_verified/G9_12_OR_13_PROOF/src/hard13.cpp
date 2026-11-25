#include <bits/stdc++.h>
using namespace std;using E=array<int,5>;const int PS[5]={2,3,5,7,11};
struct Source{int a;E e;};vector<Source> sources;
uint64_t encode(E e){uint64_t z=0;for(int k=0;k<5;k++)z+=uint64_t(e[k])<<(7*k);return z;}
E decode(uint64_t z){E e{};for(int k=0;k<5;k++)e[k]=(z>>(7*k))&127;return e;}
bool easy(int a,int M){for(int d=1;d*d<=a;d++)if(a%d==0){int c=a/d;
 if((d<=M/12&&c<=M/13)||(c<=M/12&&d<=M/13))return true;
 }return false;}
int main(int argc,char**argv){assert(argc==2);ofstream file(argv[1]);
 for(int a=2;a<1573;a++){int x=a;E e{};for(int k=0;k<5;k++)while(x%PS[k]==0){x/=PS[k];e[k]++;}if(x==1)sources.push_back({a,e});}
 int rows=0,zeros=0,maxm=0;long long sum=0;
 for(auto m:sources){int M=m.a;if(M<=13||easy(M,M))continue;
  vector<Source>C;for(auto a:sources){if(a.a>=M)break;if(!easy(a.a,M))C.push_back(a);}
  if(C.size()<8)continue;
  vector<unordered_set<uint64_t>> dp(9);dp[0].insert(encode(m.e));
  for(int i=0;i<C.size();i++){
   uint64_t add=encode(C[i].e);
   for(int k=min(8,i+1);k>=1;k--)for(auto z:dp[k-1])dp[k].insert(z+add);
  }
  if(dp[8].empty())continue;
  rows++;sum+=dp[8].size();maxm=M;
  for(auto z:dp[8]){auto d=decode(z);file<<M;for(int k=0;k<5;k++)file<<" "<<d[k];file<<"\n";}
  cout<<"M="<<M<<" hard_sources="<<C.size()+1<<" vectors="<<dp[8].size()<<"\n";
 }
 cerr<<"ROWS="<<rows<<" LAST="<<maxm<<" DEMANDS="<<sum<<"\n";
}
