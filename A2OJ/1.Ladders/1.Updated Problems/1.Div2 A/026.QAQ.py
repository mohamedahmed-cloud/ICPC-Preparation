# Problem Name : QAQ
# Problem Link : https://codeforces.com/problemset/problem/894/A
# Input Operation
import sys
str=sys.stdin.readline()
# Output Operation
a,b,c=0,0,0
for i in str:
    if i=="Q":
        c+=b
        a+=1
    if i=="A":
        b+=a
print(c)
