# Link of problem is
# "Don't Know yet the link"
# -------------
import math
# Input Operation
test=int(input())
for i in range(test):
    n=int(input())
    for i in range(2,n):
        if math.gcd(i-1,n-i-1)==1:
            print(i-1,n-i-1,1,1)
            break