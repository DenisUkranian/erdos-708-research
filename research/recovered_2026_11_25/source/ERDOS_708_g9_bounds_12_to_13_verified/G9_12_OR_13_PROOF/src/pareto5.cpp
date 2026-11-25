#include <bits/stdc++.h>
using namespace std;using E=array<int,5>;
int main(int argc,char**argv){assert(argc==3);ifstream in(argv[1]);ofstream out(argv[2]);map<int,vector<E>> gs;int M;E e{};
 while(in>>M>>e[0]>>e[1]>>e[2]>>e[3]>>e[4])gs[M].push_back(e);
 long long counted=0,good=0;
 for(auto&[M,D]:gs){E cap{};for(auto d:D)for(int k=0;k<5;k++)cap[k]=max(cap[k],d[k]);int st[4],N=1;
  for(int k=0;k<4;k++){st[k]=N;N*=cap[k+1]+1;}
  vector<int16_t>dp(N,-1);
  for(auto d:D){int z=0;for(int k=0;k<4;k++)z+=d[k+1]*st[k];dp[z]=max(dp[z],(int16_t)d[0]);}
  for(int k=0;k<4;k++)for(int z=N-1;z>=0;z--)if((z/st[k])%(cap[k+1]+1)<cap[k+1])dp[z]=max(dp[z],dp[z+st[k]]);
  int Ngood=0;
  for(auto d:D){int z=0;for(int k=0;k<4;k++)z+=d[k+1]*st[k];if(dp[z]>d[0])continue;
   bool dominated=0;for(int k=0;k<4;k++)if(d[k+1]<cap[k+1]&&dp[z+st[k]]>=d[0])dominated=1;
   if(dominated)continue;
   out<<M;for(int x:d)out<<" "<<x;out<<"\n";Ngood++;
  }
  counted+=D.size();good+=Ngood;cerr<<M<<" original="<<D.size()<<" frontier="<<Ngood<<"\n";
 }
 cerr<<"TOTAL="<<counted<<" FRONTIER="<<good<<"\n";
}
