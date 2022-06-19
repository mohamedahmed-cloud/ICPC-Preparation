# problem Name : Neko Finds Grapes
# Problem Link : https://codeforces.com/problemset/problem/1152/A
# Input Operation
import sys
n,m=map(int,sys.stdin.readline().split())
arr1=list(map(int,sys.stdin.readline().split()))
arr2=list(map(int,sys.stdin.readline().split()))
# Output Operation
even1=0
even2=0
for i in arr1:
    if i%2==0:
        even1+=1
for i in arr2:
    if i%2==0:
        even2+=1
print(min(even1,m-even2)+min(even2,n-even1))