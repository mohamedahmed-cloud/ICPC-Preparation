# problem Name : Love Triangle
# problem Link : https://codeforces.com/problemset/problem/939/A
# Input Operation
import sys
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
# input Operation End
# Solution Start
b=set(a)
if n==len(b):
    print("YES")
else:
    print("NO")

