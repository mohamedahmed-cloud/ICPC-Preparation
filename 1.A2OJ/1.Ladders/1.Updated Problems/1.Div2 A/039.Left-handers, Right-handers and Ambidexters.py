# Problem Name : Left-handers, Right-handers and Ambidexters
# problem Link : https://codeforces.com/problemset/problem/950/A
# Input Operation
import sys
l,r,a=map(int,sys.stdin.readline().split())
# Input Operation End
# Solution Start
while (a>0):
    if l>=r and a>0:
        r+=1
        a-=1
    if l<=r and a>0:
        l+=1
        a-=1
    if l==r and a==1:
        break
print(min(r,l)*2)