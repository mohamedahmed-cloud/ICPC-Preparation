# Problem Name : Alex and a Rhombus
# problem Link : https://codeforces.com/problemset/problem/1180/A
# Input Operation :
import sys
n=int(sys.stdin.readline())
# Output Operation :
out=n*2-1
for i in range(out-2,0,-2):
    out+=i*2
print(out)