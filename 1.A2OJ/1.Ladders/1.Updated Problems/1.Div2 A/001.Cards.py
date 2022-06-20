'''
Problem Name :
Cards
problem Link :
https://codeforces.com/problemset/problem/1220/A
'''
# Input Operation
n=int(input())
str=input()
# Output operation
arr=str.split(" ")
z=str.count("z")
n=str.count("n")
# print(n, z)
for i in  range(n):
    print(1,end=' ')
for i in range(z):
    print(0,end=' ')