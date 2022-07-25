# include <iostream>
using namespace std;

int main(){
    int a;
    cin>>a;
    if (isdigit(a))
     cout<<"IS DIGIT";
    else if (isalpha(a)){
        cout<<"ALPHA";
        if(isupper(a))
            cout<<"IS CAPITAL";
        else
            cout<<"IS SMALL";
    }
}