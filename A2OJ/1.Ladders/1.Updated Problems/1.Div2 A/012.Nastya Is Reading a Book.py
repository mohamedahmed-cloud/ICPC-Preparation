# Problem Name : Nastya Is Reading a Book
# Problem Link : https://codeforces.com/problemset/problem/1136/A
# Input Operation :
import sys
n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
k=int(sys.stdin.readline())
# Output Operation : 
out=n
for i in range(n):
    if arr[i][1]>=k:
        print(out)
        break
    else:
        out-=1
    