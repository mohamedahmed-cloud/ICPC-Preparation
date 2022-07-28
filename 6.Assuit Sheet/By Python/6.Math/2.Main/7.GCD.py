def solve(a,b):
    return math.gcd(a,b) ,math.lcm(a,b)
import sys,math
a,b= map(int,sys.stdin.readline().split())
ans=solve(a,b)
print(ans[0],end=' ')
print(ans[1])