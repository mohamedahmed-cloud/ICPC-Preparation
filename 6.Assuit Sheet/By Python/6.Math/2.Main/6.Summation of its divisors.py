def solve(n):
    ans=0
    end=int((math.sqrt(n)))+1
    for i in range(1,end):
        if n%i==0:
            ans+=i
            if i!=n//i:
                ans+=n//i
    return ans
import sys,math
n=int(sys.stdin.readline())
print(solve(n))