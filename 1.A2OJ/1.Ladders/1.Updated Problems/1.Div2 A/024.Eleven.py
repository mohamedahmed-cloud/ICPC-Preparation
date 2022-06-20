# problem Name : Eleven
# Problem Link : https://codeforces.com/problemset/problem/918/A
# Input Operation
import sys
import math 
n=int(sys.stdin.readline())
n1=0
n2=1
n3=0
str=""
arr=[]
for i in range(int(math.pow(n,.5))+10):
    arr.append(n3)
    n1=n2
    n2=n3
    n3=n1+n2

for i in range(n):
    if (i+1) in arr:
        str+="O"
    else:str+="o"
print(str)