import sys
def solve(a,b):
    return (b+a)
t=int(input())
a=list(map(int, sys.stdin.readline().split()))
b=list(map(int, sys.stdin.readline().split()))
print(*solve(a,b))