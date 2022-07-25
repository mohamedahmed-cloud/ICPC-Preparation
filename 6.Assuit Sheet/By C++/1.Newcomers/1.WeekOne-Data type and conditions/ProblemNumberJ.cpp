#include <iostream>
using namespace std;

int main(){
    long long a,b;
    cin>>a>>b;
    if (max(a,b)%min(a,b)==0)
     cout<<"Multiples";
    else
        cout<<"No Multiples";
}