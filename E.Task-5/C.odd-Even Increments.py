# Link of problem is
# " https://codeforces.com/problemset/problem/1669/C "
# -------------
# input Operation
test=int(input())
arr=[]
for i in range(test):
    n=int(input())
    arr=list(map(int,input().split()))
    # variables
    odd1=0
    even1=0
    odd2=0
    even2=0
    for j in range(n):
        if j%2==0:
            if arr[j]%2==0:
                even1=1
            else:
                odd1=1
        else:
            if arr[j]%2==0:
                even2=1
            else:
                odd2=1
    if (odd1==1 and even1==1) or (even2==1 and odd2==1):
        print("NO")
    else:print("YES")