def solve(a,b):
    if b-a>=10:
        return 0
    else:
        out=1
        for i in range(a+1,b+1):
            out*=(i%10)
        return out
import sys
a,b=map(int,sys.stdin.readline().split())
print((solve(a,b))%10)
