def solve(a,b):
    l=min(a,b)
    h=max(a,b)
    x=(l-1)*l/2
    y=h*(h+1)/2
    all=int(y-x)
    # find even number 
    even=int(h/2)
    alleven=even*(even+1)
    evenbefore=int(math.ceil(l/2))-1
    sumevenbefore=evenbefore*(evenbefore+1)
    w=alleven-sumevenbefore
    m=all-w
    return (all,w,m)
import sys,math
a,b=map(int,sys.stdin.readline().split())
ans=solve(a,b)
print(ans[0])
print(ans[1])
print(ans[2])
