def min(arr):
    out=arr[0]
    for i in arr:
        if out>i:
            out=i
    return out
def max(arr):
    out=arr[0]
    for i in arr:
        if out<i:
            out=i
    return out

import sys
n=int(input())
arr=list(map(int,sys.stdin.readline().split()))
print(min(arr),max(arr))