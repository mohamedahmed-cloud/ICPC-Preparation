def solve(x,n,m):
    if n<100:
        ans=1
        while(n>0):
            if n%2==1:
                ans*=x 
            x*=x 
            n//=2
        return m%ans
    else:
        return m

n=int(input())
m=int(input())
ans=solve(2,n,m)
print(ans)
