# Problem Name : A pile of stones
# problem Link : https://codeforces.com/problemset/problem/1159/A
# Output Operation
import sys
n=int(sys.stdin.readline())
arr=list(sys.stdin.readline().split())
# Output Operation
count=0
for i in range(n):
    if arr[0][i]=="-":
        count-=1
    elif arr[0][i]=="+":
        count+=1
    if count<0:
        count=0
print(count)