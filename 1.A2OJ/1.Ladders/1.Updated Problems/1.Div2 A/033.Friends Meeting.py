# Problem Name : Friends Meeting
# problem Link : https://codeforces.com/problemset/problem/931/A
# Input Operation
from re import A, X
import sys
x=int(sys.stdin.readline())
y=int(sys.stdin.readline())
# input Operation End
# Solution Start
out=0
if abs(x-y)%2==0 and abs(x-y)!=1:
    for i in range(1,int((abs(x-y))/2)+1):
        out+=i*2
elif abs(x-y)%2!=0 and abs(x-y)!=1:
    for i in range(1,int((abs(x-y))/2)+1):
        out+=i*2
        if i==int(abs(x-y)/2) and abs(x-y)!=1:
            out+=i+1
elif abs(x-y)==1:
    out=1
elif abs(x-y)==0:
    out=0
print(out)

