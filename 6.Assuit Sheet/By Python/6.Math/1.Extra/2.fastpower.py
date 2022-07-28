def solve(x,n):
    ans=1 
    while n>0:
        if n%2==1:
            # print(1)
            ans*=x 
        x*=x   
        n//=2 
    return ans
print(solve(int(input()),int(input())))