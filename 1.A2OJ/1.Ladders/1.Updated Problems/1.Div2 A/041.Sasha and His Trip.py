# Problem Name : Sasha and His Trip
# Problem Link : https://codeforces.com/problemset/problem/1113/A
# Input Operation
import sys
n,v=map(int,sys.stdin.readline().split())
# Input Operation End
# Solution Start
dollar=v
i=1
while n!=0:
    i+=1
    if n-1==v:
        n=0
        break
    elif n>v:
        v+=1
        dollar+=i
    else:
        dollar=n-1
        break
print(dollar)