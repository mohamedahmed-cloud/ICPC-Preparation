# import math
def pow(n,k):
    out=0
    muliply=n
    for i in range(1,k):
        out=n*muliply
        muliply=out
    return out
def solve(x,n):
    iter=2
    ans=0
    while n>=iter:
        ans+=pow(x,iter)
        iter+=2
    return int(ans)

import sys
x,y=map(int, sys.stdin.readline().split())
print(solve(x,y))