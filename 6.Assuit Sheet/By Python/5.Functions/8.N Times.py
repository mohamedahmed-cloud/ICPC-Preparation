import sys
t=int(input())
for i in range(t):
    n,c=map(str,sys.stdin.readline().split())
    print((int(n)-1)*(c+" "),end="")
    print(c)