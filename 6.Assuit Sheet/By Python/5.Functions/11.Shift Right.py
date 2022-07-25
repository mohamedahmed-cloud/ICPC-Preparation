import sys
def solve(n,arr,x):
    times=x%n
    for i in range(times):
        l=arr[-1]
        arr=[l]+arr[:-1]
    return arr
n,x=map(int, sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
print(*solve(n,arr,x))
