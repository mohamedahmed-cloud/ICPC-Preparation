# Link of problem is
# "https://codeforces.com/contest/1671/problem/B"
# -------------
# Input Operation
test=int(input())
for i in range(test):
    n=int(input())
    arr=[]
    arr=list(map(int,input().split()))
    # Output Operation
    if n==1:print("YES")
    else:
        count=0
        for j in range(1,n):
            if abs(arr[j]-arr[j-1]) in [1]:
                continue
            if abs(arr[j]-arr[j-1]) in [2,3]:
                count+=arr[j]-arr[j-1]
            else:
                count=100
                break
        if count in [0,2,3,4]:
            print("YES")
        else:print("NO")