# Link of problem is
# "https://codeforces.com/problemset/problem/1669/B"
# -------------
# Input Operation
arr=[]

for i in range(int(input())):
    int(input())
    arr=list(map(int,input().split()))
    # outPut operation
    arr=sorted(arr)
    count=-1
    for j in range(len(arr)-2):
        if arr[j]==arr[j+1] and arr[j+1]==arr[j+2]:
            count=arr[j]
            break
    print(count)
    
