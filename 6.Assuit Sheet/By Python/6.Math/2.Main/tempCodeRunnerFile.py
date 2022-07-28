def solve(n):
    ans=0
    end=math.ceil(math.sqrt(n))
    for i in range(1,int(end)):
        if n%i==0:
            ans+=i
            ans+=n//i
    return ans
import sys,math
n=int(sys.stdin.readline())
print(solve(n))