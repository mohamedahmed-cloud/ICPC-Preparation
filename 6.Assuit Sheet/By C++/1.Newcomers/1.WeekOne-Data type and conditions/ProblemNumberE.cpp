#include <iostream>
#include<iomanip>
using namespace std;
int main(){
    cout <<fixed<<setprecision(9);
    double x= 3.141592653;
    double r;
    cin>>r;
    cout<<x*r*r;
}