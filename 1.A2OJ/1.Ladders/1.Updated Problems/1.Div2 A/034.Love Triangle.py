# problem Name : Love Triangle
# problem Link : https://codeforces.com/problemset/problem/939/A
# Input Operation
import sys
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
# input Operation End
# Solution Start
out=0
for i in range(n):
    if a[a[a[i-1]-1]-1]==i:
        print(i)
        out=1
        break
print("YES") if out==1 else print("NO")