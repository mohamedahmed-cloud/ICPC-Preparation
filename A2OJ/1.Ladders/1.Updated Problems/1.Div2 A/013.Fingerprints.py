# problem Name :Fingerprints
# problem Link : https://codeforces.com/problemset/problem/994/A
# Input Operation :
import sys
n,m=map(int,sys.stdin.readline().split())
arr1=list(map(int,sys.stdin.readline().split()))
arr2=list(map(int,sys.stdin.readline().split()))
# Output Operation :
for i in range(n):
    if arr1[i] in arr2:
        print(arr1[i],end=" ")
