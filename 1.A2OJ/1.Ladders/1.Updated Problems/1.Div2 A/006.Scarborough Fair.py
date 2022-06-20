'''
problem Name :
Scarborough Fair
Problem Link :
https://codeforces.com/problemset/problem/897/A
'''
# Input Operation
n,m=map(int,input().split())
str=input()
str2=""
arr=[]
out=""
for i in range(m):
    l,r,c1,c2=input().split()
    l=int(l)
    r=int(r)
# Output Operation
    for j in range(l-1,r):
        if(str[j]==c1):
            str2+=c2
        else:
            str2+=str[j]
    str2=str[:l-1]+str2+str[r:]
    str=str2
    out=str2
    str2=""
print(out)