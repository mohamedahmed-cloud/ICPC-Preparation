# Problem Name : Keanu Reeves
# Problem Link : https://codeforces.com/problemset/problem/1189/A
# Input Operation
import sys
n=int(sys.stdin.readline())
str=sys.stdin.readline()
# Output Operation
if str.count("0")==str.count("1"):
    print(2)
    print(str[0],str[1:])
else:
    print(1)
    print(str)