#define main oldmain
#include "smooth_frontier.cpp"
#undef main
// No p-free source contains a large prime in the one-large-prime case.
int main(){for(int i=2;i<=L;i++)if(!sp[i])for(int j=i;j<=L;j+=i)if(!sp[j])sp[j]=i;for(int i=2;i<=L;i++)om[i]=1+om[i/sp[i]];for(int i=1;i<=L;i++)for(int j=i;j<=L;j+=i)dv[j].push_back(i);for(int a=2;a<=L;a++){int x=a;for(int k=0;k<5;k++)while(x%ps[k]==0){ex[a][k]++;x/=ps[k];}if(x==1)smooth.push_back(a);}
long long groups=0,sets=0;int maxM=0;set<tuple<int,int,U,U,U,U>> demands;
for(int p=13;p*p<10*24010;p++)if(sp[p]==p){int T=min(p-1,24009/p);vector<int> us;for(int a:smooth)if(a<=T)us.push_back(a);for(int i=0;i<(int)us.size();i++)for(int j=i+1;j<(int)us.size();j++)for(int k=j+1;k<(int)us.size();k++){
 int u=us[i],v=us[j],w=us[k];int upper=min({24009,p*p-1,10*u*v-1});if(p*w>upper)continue;
 for(int r=0;r<3;r++)for(int s=r+1;s<3;s++){
 int Uc[3]={u,v,w};vector<int>A={p*u,p*v,p*w,u*v,u*w,v*w,Uc[r]*Uc[r],Uc[s]*Uc[s]};sort(A.begin(),A.end());A.erase(unique(A.begin(),A.end()),A.end());assert(A.size()==7||A.size()==8);int lo=A.back();if(lo>upper)continue;
 bool ok=true;for(int a:A){if(12*a<=lo){ok=false;break;}for(int b:A)if(b>a&&peel(a,b,lo)){ok=false;break;}if(!ok)break;}if(!ok)continue;groups++;
 auto dfs=[&](auto&&self,int start)->void{if(A.size()==9){int M=*max_element(A.begin(),A.end());if(M>upper)return;int g=0;for(int a:A)g=gcd(g,a);if(g!=1)return;for(int a:A){if(12*a<=M)return;for(int b=2*a;b<=M;b+=a)if(find(A.begin(),A.end(),b)==A.end())return;for(int b:A)if(b>a&&peel(a,b,M))return;}U d=0;for(int a:A)d+=enc(ex[a]);sets++;maxM=max(maxM,M);demands.emplace(M,p,d,enc(ex[u]),enc(ex[v]),enc(ex[w]));return;}
 for(int z=start;z<(int)smooth.size()&&smooth[z]<=upper;z++){int a=smooth[z];if(find(A.begin(),A.end(),a)!=A.end()||12*a<=lo)continue;int mm=max(lo,a);bool good=true;for(int b:A)if(peel(a,b,mm)){good=false;break;}if(!good)continue;A.push_back(a);self(self,z+1);A.pop_back();}};dfs(dfs,0);
 }
} }
for(auto [M,p,d,u,v,w]:demands){cout<<M<<" "<<p;for(int a:dec(d))cout<<" "<<a;for(U q:{u,v,w})for(int a:dec(q))cout<<" "<<a;cout<<"\n";}
cerr<<"GROUPS="<<groups<<" SETS="<<sets<<" DEMANDS="<<demands.size()<<" MAX_M="<<maxM<<"\n";
}
