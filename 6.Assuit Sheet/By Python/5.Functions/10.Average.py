import sys
def average(arr):
    l=len(arr)
    sum=0
    for i in arr:
        sum+=i
    ans=sum/l
    return "{:.6f}".format(ans)
n=int(input())
arr=list(map(float, sys.stdin.readline().split()))
print(average(arr))