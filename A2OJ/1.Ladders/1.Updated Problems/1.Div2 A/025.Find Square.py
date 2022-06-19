# Problem Name : Find Square
# Problem Link : https://codeforces.com/problemset/problem/1028/A
# Input Operation
import sys
import math
n,m=map(int,sys.stdin.readline().split())
coloum=0
row=0
multiple=0
for i in range(n):
    arr=[]
    arr=sys.stdin.readline().split()
# Output Operation
    for j in range(m):
        if arr[0][j]=="B":
            multiple+=1
            row+=i+1
            coloum+=j+1
out=int(math.pow(multiple,.5))
print(int(row/(out*out)),int(coloum/(out*out)))