# Getting GCD 
# Initialize
# n,p=map(int,input().split())
# com=0
# for i in range(1,min(n,p)+1):
#     if n%i==0 and p%i==0 :
#         if i>com :
#            com=i
# print(com)

# import math
# print(math.gcd(11,5))

# Solving 
import math
n=int(input())
for i in range(n):
    num=int(input())
    for i in range(2,num):
        if math.gcd(i,num-i-1)==1:
            print(i,num-i-1,1)
            break
