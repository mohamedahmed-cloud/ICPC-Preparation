def solve(A,B,res):
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                res[i][j]+=A[i][k]*B[k][j]
    return res
import sys
Ra,Ca= map(int,sys.stdin.readline().split())
A=[]
for i in range(Ra):
    A.append(list(map(int, sys.stdin.readline().split())))
B=[]
Rb,Cb=map(int,sys.stdin.readline().split())
for j in range(Rb):
    B.append(list(map(int,sys.stdin.readline().split())))

res = [[0 for x in range(Cb)] for y in range(Ra)]


# print(res)
ans=solve(A,B,res)
for i in ans:
    out=""
    for j in i:
        out=out+str(j)+" "
    print(out.strip())

# # Another one
# def solve(A,B,res):
#     import numpy as np
#     res=np.dot(A,B)
#     return res