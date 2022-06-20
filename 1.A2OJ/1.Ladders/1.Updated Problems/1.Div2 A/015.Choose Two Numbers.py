# Problem Name : Choose Two Numbers
# problem Link : https://codeforces.com/problemset/problem/1206/A
# Input Operation :
import sys
n=int(sys.stdin.readline())
arr1=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
arr2=list(map(int,sys.stdin.readline().split()))
# Output Operation :
print(max(arr1),max(arr2))