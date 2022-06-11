# Problem Name : Pens and Pencils
# Problem URL : https://codeforces.com/problemset/problem/1244/A

# Input Operation
import math


test=int(input())
for i in range(test):
    a,b,c,d,k=map(int,input().split())
    # Output Operation
    if math.ceil(a/c)+math.ceil(b/d)<=k:
        print(k-(math.ceil(b/d)),math.ceil(b/d))
    else:
        print(-1)