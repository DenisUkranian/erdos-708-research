#include <bits/stdc++.h>
using namespace std;using E=array<int,5>;constexpr int PR[5]={2,3,5,7,11};
struct Fac{int num,shift;E e;};
int main(int argc,char**argv){assert(argc==4);ifstream in(argv[1]);int last=atoi(argv[2]);ofstream missout(argv[3]);assert(missout);int M;E e{};map<int,vector<E>> gs;
 while(in>>M>>e[0]>>e[1]>>e[2]>>e[3]>>e[4])if(M<=last)gs[M].push_back(e);
 long long tt=0,miss=0;auto start=chrono::steady_clock::now();
 for(auto&[M,D]:gs){auto st=chrono::steady_clock::now();E cap{};for(auto d:D)for(int k=0;k<5;k++)cap[k]=max(cap[k],d[k]);
 int stride[5],N=1;for(int i=0;i<5;i++){stride[i]=N;N*=cap[i]+1;}assert(N>0 && N<=20000000);
 vector<E> states(N);for(int z=0;z<N;z++)for(int k=0;k<5;k++)states[z][k]=(z/stride[k])%(cap[k]+1);
 vector<Fac> opts;for(int h=2;h<=M;h++){int v=h;E he{};for(int k=0;k<5;k++)while(v%PR[k]==0){v/=PR[k];he[k]++;}if(v!=1)continue;
  bool good=true;int offset=0;for(int k=0;k<5;k++){if(he[k]>cap[k])good=false;offset+=he[k]*stride[k];}if(good)opts.push_back({h,offset,he});}
 vector<uint8_t> seen(N,0);vector<int> active={0},fresh;fresh.reserve(N);
 for(int j=1;j<=9;j++){
  fill(seen.begin(),seen.end(),0);fresh.clear();int cb=M/j;
  for(int z:active){seen[z]=1;fresh.push_back(z);}
  for(int z:active){const E &old=states[z];
   for(auto&h:opts){int gcd=1;bool ok=true;
    for(int i=0;i<5;i++){
     if(old[i]+h.e[i]>cap[i]){ok=false;break;}
     int t=min(old[i],h.e[i]);for(;t>0;t--){gcd*=PR[i];if(gcd>cb){ok=false;break;}}
     if(!ok)break;
    }
    if(!ok)continue;int nz=z+h.shift;if(!seen[nz]){seen[nz]=1;fresh.push_back(nz);}
   }
  }active.swap(fresh);
 }
 vector<uint8_t>covers=seen;
 for(int k=0;k<5;k++){int st=stride[k],width=cap[k]+1;
  for(int z=N-1;z>=0;z--)if((z/st)%width<cap[k]&&covers[z+st])covers[z]=1;
 }
 int fail=0;for(auto d:D){int z=0;for(int k=0;k<5;k++)z+=d[k]*stride[k];if(!covers[z]){fail++;missout<<M;for(int x:d)missout<<" "<<x;missout<<"\n";}}
 tt+=D.size();miss+=fail;
 cout<<"M="<<M<<" demands="<<D.size()<<" states="<<active.size()<<" total="<<N<<" misses="<<fail<<" sec="<<chrono::duration<double>(chrono::steady_clock::now()-st).count()<<"\n";cout.flush();
 }
 cerr<<"TOTAL demands="<<tt<<" misses="<<miss<<" time="<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n";
}
