# Problem Name : Ropewalkers
# problem Link : https://codeforces.com/problemset/problem/1185/A
# Input Operation
from array import array
import sys
arr=list(map(int,sys.stdin.readline().split()))
# Input Operation End
# Solution Start
d=arr[-1]
arr=arr[:-1]
arr.sort()
a=arr[0]
b=arr[1]
c=arr[2]
seconds=0
if abs(c-b)<d:
    seconds+=d-abs(c-b)
if abs(b-a)<d:
    seconds+=d-abs(b-a) 
print(seconds)
