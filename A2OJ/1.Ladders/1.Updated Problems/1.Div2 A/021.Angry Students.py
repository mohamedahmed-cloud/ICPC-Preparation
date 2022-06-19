# Problem Name : Angry Students
# problem Link : https://codeforces.com/problemset/problem/1287/A
# Input Operation
import sys
test=int(sys.stdin.readline())
for i in range(test):
    n=int(sys.stdin.readline())
    str=sys.stdin.readline()
    for i in range(n):
        if str[0]=="P":
            str=str.replace("P","",1)
        else:
            break
    count=0
    out=0
    for i in range(len(str)):
        if str[i]=="P":
            count+=1
            if count>out:
                out=count
        else:
            count=0
    print(out)


