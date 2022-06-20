'''
Problem Name : 
    Fafa and his Company
problem link :
    https://codeforces.com/problemset/problem/935/A
'''
# Input Operation
number=int(input())
# Output Operation
out=0
for i in range(1,number):
    if((number-i)%i)==0:
        out+=1
print(out)