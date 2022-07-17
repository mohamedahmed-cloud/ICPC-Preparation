#include <iostream>
#include <cmath>
using namespace std;

int main(){
    double a,b;
    cin>>a>>b;
    double c=a/b;
    // cout 
    // cout<<ceil(a/b);
    cout<<"floor "<<a<<" / "<<b<<" = "<< floor(c)<<endl;
    cout<<"ceil "<<a<<" / "<<b<<" = "<<(ceil(c))<<endl ;
    cout<<"round "<<a<<" / "<<b<<" = "<<(round(c))<<endl ;
}