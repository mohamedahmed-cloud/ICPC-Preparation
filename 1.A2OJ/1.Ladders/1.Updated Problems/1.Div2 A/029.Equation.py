# Problem Name : Equation
# Problem Link : https://codeforces.com/problemset/problem/1269/A
# Input Operation
import sys
n=int(sys.stdin.readline())
# Output Operation
a=n
b=0
while True:  
    a+=1
    b+=1
    if a-b==n and (a!=2 and a!=3) and (b!=2 and b!=3) and (a%2==0 or a%3==0) and (b%2==0 or b%3==0):
        break
print(a,b)