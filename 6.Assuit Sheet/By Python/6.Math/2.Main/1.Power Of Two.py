import sys,math
def solve(a):
    if a==1:
        return "YES"
    for i in range(0,80):
        if int(math.pow(2,i))==a:
            return "YES"
    return "NO"
n=int(sys.stdin.readline())
print(solve(n))