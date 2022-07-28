#include <iostream>
using namespace std;
int main()
{
    long long a, b, c, x, y, mul, ans;
    ans=0;
    cin >> a >> b >> c;
    x = min(a, b);
    y = max(a, b);
    if (x < c)
    {
        x = c;
    }
    else if (x > c && x % c != 0)
    {
        mul = x / c;
        x = (mul + 1) * c;
    }
    for (int i = x; i <= y; i += c)
    {
        ans += i;
    }
    cout << ans;
}