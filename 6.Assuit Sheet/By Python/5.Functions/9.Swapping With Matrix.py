import sys
n,x,y=map(int, sys.stdin.readline().split())
arr=[]
for i in range(n):
    a=list(map(int, sys.stdin.readline().split()))
    arr.append(a)
# swap row
arr[x-1],arr[y-1]=arr[y-1],arr[x-1]
# Swap column
for i in range(n):
    arr[i][x-1],arr[i][y-1]=arr[i][y-1],arr[i][x-1]
# printing
for i in arr:
    for j in i:
        if j==i[-1]:
            print(j,end="")
        else:
            print(j,end=" ")
    print()