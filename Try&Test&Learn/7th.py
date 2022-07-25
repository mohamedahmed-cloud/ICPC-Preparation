import sys,math
n,x,a=map(int,sys.stdin.readline().split())
l=int(a/x)
print(math.ceil(n/l))