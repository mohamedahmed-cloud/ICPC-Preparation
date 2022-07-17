# include <iostream>
using namespace std;
int main(){
    int a;
    cin>>a;
    if(a%2==0)
        cout<<"even";
    else
        cout<<"odd";
//    using /2
    // 
    cout<<endl;
    double b=a/2.0;
    b=b-int(b);
    if(b==0)
        cout<<"even";
    else
        cout<<"odd";
    // using "%10"
    cout<<endl;
    int c=a%10;
    if( c==0 || c==2 || c==4 || c==6 ||c==8){
        cout<<"even";
    }else
        cout<<"odd";

    
    return 0;
}