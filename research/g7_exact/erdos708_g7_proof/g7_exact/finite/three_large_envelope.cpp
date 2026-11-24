#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <set>
#include <vector>
using namespace std;
using U=unsigned __int128;
using V=array<int,3>;
const array<int,4> SP{2,3,5,7};
const array<V,10> E{{V{0,0,0},V{1,0,0},V{0,1,0},V{0,0,1},V{2,0,0},V{0,2,0},V{0,0,2},V{1,1,0},V{1,0,1},V{0,1,1}}};
struct Pattern{array<int,10> c;V demand;int m;};
vector<Pattern> pats;
vector<int> smooth;
int rough(int a,int i){for(int j=0;j<i;j++)while(a%SP[j]==0)a/=SP[j];return a;}
bool isprime(int p){for(int d=2;d*d<=p;d++)if(p%d==0)return false;return p>=2;}
int corecost(const V&ps,const V&D,int M,const V&e,int m){
 int c=1;
 for(int i=0;i<3;i++){
  int worst=0;
  for(int v=e[i];v<=2;v++){
   int n1=max(0,M/ps[i]-(v>=1)),n2=max(0,M/(ps[i]*ps[i])-(v>=2));
   int rem=max(0,D[i]-v),k=0;
   while(k<=9 && min(k,n1)+min(k,n2)<rem)k++;
   worst=max(worst,k);
  }
  c+=worst;
 }
 return min(m+1,c);
}
void gen(int at,int left,array<int,10>&c){
 if(at==10){
  if(left)return;V supp{},d{};
  for(int t=0;t<10;t++)for(int i=0;i<3;i++){supp[i]+=c[t]*(E[t][i]>0);d[i]+=c[t]*E[t][i];}
  if(*min_element(supp.begin(),supp.end())<4)return;
  assert(c[0]<=1);assert(c[7]&&c[8]&&c[9]);
  pats.push_back({c,d,7-c[0]});return;
 }
 for(int n=0;n<=left;n++){c[at]=n;gen(at+1,left-n,c);}
}
int main(int argc,char**argv){
 int top=argc>1?atoi(argv[1]):24696;
 int maxfail=argc>2?atoi(argv[2]):1000000;
 auto start=chrono::steady_clock::now();
 array<int,10> cc{};gen(0,7,cc);assert(pats.size()==46);
 for(int a=1;a<=top;a++){int b=a;for(int p:SP)while(b%p==0)b/=p;if(b==1)smooth.push_back(a);}
 vector<int> primes;for(int p=11;p<=top/13;p++)if(isprime(p))primes.push_back(p);
 uint64_t triples=0,maxima=0,classes=0,passed=0,failed=0;
 ofstream failures("g7_exact/finite/three_large_unresolved.tsv");
 for(int ii=0;ii<(int)primes.size();ii++){
  int p=primes[ii];if(p*p>top)break;
  for(int jj=ii+1;jj<(int)primes.size();jj++){
   int q=primes[jj];if(q*q>top)break;
   for(int kk=jj+1;kk<(int)primes.size();kk++){
    int r=primes[kk],lo=q*r,hi=min(top,9*p*p-1);if(lo>hi)break;
    ++triples;V ps{p,q,r};array<int,10> core{1,p,q,r,p*p,q*q,r*r,p*q,p*r,q*r};
    set<int> ms;
    for(int d:core)for(int s:smooth){int a=d*s;if(a>hi)break;if(a>=lo)ms.insert(a);}
    for(int M:ms){
     ++maxima;
     array<vector<int>,10> cs;
     array<array<array<U,8>,4>,10> up{},minus{};
     array<bool,10> hasM{};
     for(int t=0;t<10;t++){
      int d=core[t];hasM[t]=(M%d==0&&binary_search(smooth.begin(),smooth.end(),M/d));
      for(int s:smooth){if(d*s>M)break;if(7*d*s>M)cs[t].push_back(s);}
      for(int j=0;j<4;j++){
       vector<int> all,nonmax;
       for(int s:cs[t])all.push_back(rough(s,j));
       for(int k=0;k+1<(int)cs[t].size();k++)nonmax.push_back(rough(cs[t][k],j));
       sort(all.rbegin(),all.rend());sort(nonmax.rbegin(),nonmax.rend());
       up[t][j][0]=1;minus[t][j][0]=1;
       for(int k=1;k<=7;k++){
        up[t][j][k]=k<=(int)all.size()?up[t][j][k-1]*all[k-1]:0;
        minus[t][j][k]=k<=(int)nonmax.size()?minus[t][j][k-1]*nonmax[k-1]:0;
       }
      }
     }
     for(auto pat:pats){
      bool possible=true,containsM=false;
      for(int t=0;t<10;t++){if(pat.c[t]>(int)cs[t].size())possible=false;if(pat.c[t]&&hasM[t])containsM=true;}
      if(!possible||!containsM)continue;
      ++classes;array<U,4> full{};full.fill(1);
      for(int j=0;j<4;j++)for(int t=0;t<10;t++)full[j]*=up[t][j][pat.c[t]];
      bool done=false;
      int spare=0;for(int e=7;e<10;e++)if(M/core[e]>pat.c[e])spare++;
      if(pat.c[0]==1){
       U allcoef=1;int largestcoef=1;
       for(int e=7;e<10;e++){int L=M/core[e];assert(L>=2&&pat.c[e]==2);allcoef*=L*(L-1);largestcoef=max(largestcoef,L);}
       U remaining=allcoef/largestcoef;
       if(3*remaining<=U(M)||(spare>=2&&84*remaining<=U(M)*M))done=true;
      }
      int unioncost=0;
      for(int i=0;i<3;i++){int k=0;while(k<=9 && min(k,M/ps[i])+min(k,M/(ps[i]*ps[i]))<pat.demand[i])k++;unioncost+=k;}
      unioncost=min(unioncost,pat.m+(spare==0));
      int freeslots=9-unioncost;
      if(freeslots>0){
       if(freeslots==1&&full[0]<=U(M))done=true;
       bool ok=true;
       for(int j=0;j<4;j++){int sp=SP[j];U threshold=sp;for(int k=1;k<=freeslots;k++)threshold*=max(M/(k*sp)+1,sp);if(full[j]>=threshold){ok=false;break;}}
       if(ok)done=true;
      }
      for(int t=1;t<10&&!done;t++)if(pat.c[t]){
       int c=corecost(ps,pat.demand,M,E[t],pat.m);
       int other_spares=spare-((t>=7&&M/core[t]>pat.c[t])?1:0);
       if(other_spares>0)c=min(c,pat.m);
       int slots=9-c;
       if(slots<=0)continue;
       array<U,4> rem{};for(int j=0;j<4;j++){assert(up[t][j][pat.c[t]]);rem[j]=full[j]/up[t][j][pat.c[t]]*minus[t][j][pat.c[t]-1];}
       if(slots==1&&rem[0]<=U(M/2)){done=true;break;}
       bool ok=true;
       for(int j=0;j<4;j++){
        int sp=SP[j];U threshold=sp;
        for(int k=2;k<=slots+1;k++)threshold*=max(M/(k*sp)+1,sp);
        if(rem[j]>=threshold){ok=false;break;}
       }
       if(ok)done=true;
      }
      if(done)++passed;
      else{
       ++failed;failures<<p<<'\t'<<q<<'\t'<<r<<'\t'<<M;
       for(int x:pat.c)failures<<'\t'<<x;failures<<'\n';
       if(failed>=uint64_t(maxfail))goto finish;
      }
     }
    }
   }
  }
 }
 finish:
 cout<<"{\"triples\":"<<triples<<",\"maxima\":"<<maxima<<",\"classes\":"<<classes<<",\"passed\":"<<passed<<",\"unresolved\":"<<failed<<",\"seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"}\n";
}
