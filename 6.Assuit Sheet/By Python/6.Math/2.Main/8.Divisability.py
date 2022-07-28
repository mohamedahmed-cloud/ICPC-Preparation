import sys,math
def solve(a,b,w):
    x=min(a,b)
    y=max(a,b)
    if x<w:
        x=w
    elif x>w and x%w!=0:
        mul=x//w
        x=(mul+1)*w
    ans=0
    for i in range(x,y+1,w):
        ans+=i
    return ans
a,b,w=map(int,sys.stdin.readline().split())
print(solve(a,b,w))