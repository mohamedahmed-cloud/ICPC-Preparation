from re import S
import sys
t=int(sys.stdin.readline())
for i in range(t):
    k=int(sys.stdin.readline())
    n=1
    while True:
        out=int(n*(n+1)/2)
        if out==k:
            print(n)
            break
        elif out>k:
            print(n-1)
            break
        n+=1