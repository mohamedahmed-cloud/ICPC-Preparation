'''
Problem Name :
 Tokitsukaze and Enhancement
Problem Link :
 https://codeforces.com/problemset/problem/1191/A
'''
# Input Operation
n=int(input())
# Output Operation
if(n%4==1):
    print(0,"A")
elif(n%4==2):
    print(1,"B")
elif(n%4==3):
    print(2,"A")
elif(n%4==0):
    print(1,"A")

