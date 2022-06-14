# problem Name :Olympiad
# problem Link : https://codeforces.com/problemset/problem/937/A
# Input Operation :
import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
# Output Operation :
arr2=list(set(arr))
while 0 in arr2:
    arr2.remove(0)
print(len(arr2))