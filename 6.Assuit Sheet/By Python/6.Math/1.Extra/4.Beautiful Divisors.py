import sys,math
def solve(n):
    for i in range(10,0,-1):
        if ((math.pow(2,i)-1)*math.pow(2,(i-1)))<=n and n%((math.pow(2,i)-1)*math.pow(2,(i-1)))==0:
            return int((math.pow(2,i)-1)*math.pow(2,(i-1)))
n=int(sys.stdin.readline()) 
print(solve(n))