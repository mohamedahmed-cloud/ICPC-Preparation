from re import L


def solve(n):
    if n==1:
        return "NO"
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return "NO"
    return "YES"
import math,sys
n=int(sys.stdin.readline())
print(solve(n))