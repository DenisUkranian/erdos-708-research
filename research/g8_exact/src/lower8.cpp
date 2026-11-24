#include <bits/stdc++.h>
using namespace std;
int main(){
 const long long X=246043396342067361LL;
 const int M=2491;
 const int primes[5]={37,41,43,47,53};
 const int needs[5]={6,2,2,2,4};
 int stride[5], total=1;
 for(int i=0;i<5;i++){stride[i]=total;total*=needs[i]+1;}
 vector<array<int,5>> state(total);
 for(int z=0;z<total;z++)for(int i=0;i<5;i++)state[z][i]=(z/stride[i])%(needs[i]+1);
 const int INF=10000;
 vector<int> dp(total,INF);
 dp[0]=0;
 vector<vector<short>> parent(M,vector<short>(total,-1));
 map<array<int,5>,int> types;
 for(int t=1;t<=M;t++){
  long long v=X+t;
  array<int,5> e{};
  for(int i=0;i<5;i++){while(e[i]<needs[i]&&v%primes[i]==0){v/=primes[i];e[i]++;}}
  types[e]++;
  for(int z=total-1;z>=0;z--){
   if(dp[z]>=INF)continue;
   int dest=0;
   for(int i=0;i<5;i++)dest+=stride[i]*min(needs[i],state[z][i]+e[i]);
   if(dp[z]+1<dp[dest]){dp[dest]=dp[z]+1;parent[t-1][dest]=z;}
  }
 }
 int wanted=total-1;
 cout<<"M="<<M<<" states="<<total<<" optimal="<<dp[wanted]<<" distinct_patterns="<<types.size()<<"\n";
 int cur=wanted;vector<int> b;
 for(int t=M;t>=1;t--){int z=parent[t-1][cur];if(z>=0){b.push_back(t);cur=z;}}
 assert(cur==0);reverse(b.begin(),b.end());
 cout<<"Selected offsets:";for(int v:b)cout<<" "<<v;cout<<"\n";
 array<int,5> cover{};for(int t:b){long long v=X+t;for(int i=0;i<5;i++)while(v%primes[i]==0){v/=primes[i];cover[i]++;}}
 cout<<"Demand:";for(int v:needs)cout<<" "<<v;cout<<"\n";
 cout<<"Cover:";for(int v:cover)cout<<" "<<v;cout<<"\n";
 for(auto &kv:types)if(accumulate(kv.first.begin(),kv.first.end(),0)>=2){cout<<"cross ";for(int v:kv.first)cout<<v<<",";cout<<" count="<<kv.second<<"\n";}
}
