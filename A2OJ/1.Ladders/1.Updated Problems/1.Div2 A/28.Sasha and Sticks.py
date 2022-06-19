# problem Name : Sasha and Sticks
# problem Link : https://codeforces.com/problemset/problem/832/A
# Input Operation  
import sys
n,k=map(int,sys.stdin.readline().split())
a=n//k
b=a%2
if b==0:
    print("No")
else:
    print("Yes")
