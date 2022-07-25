#include <iostream>
#include <string>
using namespace std;
int main(){
    string a,b;
    cin>>a>>b;
    cout<<stoi(a.substr(a.length()-1)) + stoi(b.substr(b.length()-1));
    return 0;
}