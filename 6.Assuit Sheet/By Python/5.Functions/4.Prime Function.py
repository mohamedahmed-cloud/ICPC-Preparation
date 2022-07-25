import math
def prime(n):
    if n in [0,1]:
        return "NO"
   
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return "NO"
    return "YES"
t=int(input())
for i in range(t):
    print(prime(int(input())))