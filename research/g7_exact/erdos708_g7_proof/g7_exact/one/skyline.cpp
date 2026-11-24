#include <vector>
#include <array>
#include <algorithm>
#include <cstring>
extern "C" int skyline(const int *input,int n,int d,int *output) {
  std::vector<std::array<int,5>> a(n);
  for(int i=0;i<n;i++) { a[i].fill(0);for(int j=0;j<d;j++)a[i][j]=input[i*d+j]; }
  std::sort(a.begin(),a.end(),std::greater<std::array<int,5>>());
  a.erase(std::unique(a.begin(),a.end()),a.end());
  int h1=2,h2=2,h3=2;
  for(auto x:a){h1=std::max(h1,x[1]+2);h2=std::max(h2,x[2]+2);h3=std::max(h3,x[3]+2);}
  if(d==3){h2=1;h3=1;} else if(d==4)h3=1;
  const int s2=h2+1,s3=h3+1;
  std::vector<int> tree((h1+1)*s2*s3,-1);
  auto at=[&](int i,int j,int k)->int&{return tree[(i*s2+j)*s3+k];};
  int count=0;
  for(auto x:a){
    int u=h1-x[1],v=d>=4?h2-x[2]:1,w=d>=5?h3-x[3]:1;
    int best=-1;
    for(int i=u;i;i-=i&-i)for(int j=v;j;j-=j&-j)for(int k=w;k;k-=k&-k)best=std::max(best,at(i,j,k));
    if(best>=x[d-1])continue;
    for(int j=0;j<d;j++)output[count*d+j]=x[j];count++;
    for(int i=u;i<=h1;i+=i&-i)for(int j=v;j<=h2;j+=j&-j)for(int k=w;k<=h3;k+=k&-k)at(i,j,k)=std::max(at(i,j,k),x[d-1]);
  }
  return count;
}
