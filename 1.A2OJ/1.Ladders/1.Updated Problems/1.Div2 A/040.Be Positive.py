# Problem Name  : Be Positive
# Problem Link  : https://codeforces.com/problemset/problem/1130/A
# Input Operation
import sys
import math
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
lenght=math.ceil(len(arr)/2)
positive=0
negative=0
for i in arr:
    if i>0:
        positive+=1
    elif i<0:
        negative+=1
if positive>= lenght:
    print(1)
elif negative>= lenght:
    print(-1)
else:print(0)
