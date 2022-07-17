# problem Name : Word
# Problem Link : https://codeforces.com/contest/59/problem/A

# Input Operation
import sys
string=sys.stdin.readline()
# Solution Start
up=0
down=0
for i in string:
    if i.isupper():
        up+=1
    elif i.islower():
        down+=1
if up>down:
    print(string.upper())
else:
    print(string.lower())
