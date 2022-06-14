# Problem Name: Ehab and another construction problem
# problem Link : https://codeforces.com/problemset/problem/1088/A
# Input Operation :
import sys
n=int(sys.stdin.readline())
out=0
for i in range(1,n+1):
    for j in range(1,i+1):
        if i%j==0 and j*i>n:
            print(i , j)
            out=1
            break
    if out==1:
        break
if out==0:
    print(-1)