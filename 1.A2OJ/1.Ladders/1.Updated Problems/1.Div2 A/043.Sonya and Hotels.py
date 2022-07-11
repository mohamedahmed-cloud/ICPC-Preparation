# problem Name : Sonya and Hotels 
# problem Link : https://codeforces.com/problemset/problem/1004/A
# Input Operation
import sys
n,d=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
# Input Operation End
# Solution Start
hotels=2
for i in range(1,n):
    if abs(arr[i]-arr[i-1])==2*d:
        hotels+=1
    if abs(arr[i]-arr[i-1])>2*d:
        hotels+=2
print(hotels)