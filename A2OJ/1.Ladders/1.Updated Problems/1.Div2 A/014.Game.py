# Problem Name : Game
# problem Link : https://codeforces.com/problemset/problem/984/A
# Input Operation :
import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
# Output Operation :
arr.sort()
if n%2==0:
    print(arr[int(n/2-1)])
else :
    print(arr[int(n/2)])