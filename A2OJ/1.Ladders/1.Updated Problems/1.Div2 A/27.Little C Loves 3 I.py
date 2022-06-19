# Problem Name:Little C Loves 3 I
# Problem Link : https://codeforces.com/problemset/problem/1047/A
# Input Operation
import sys
n=int(sys.stdin.readline())
a=1
b=1
c=n-2
while c%3==0 or b%3 ==0 or b+c!=n-1:
    c-=1
    b+=1
print(a,b,c)
      