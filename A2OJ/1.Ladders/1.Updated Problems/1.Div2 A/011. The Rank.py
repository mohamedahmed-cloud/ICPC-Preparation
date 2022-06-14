# Problem Name : The Rank 
# Problem Link : https://codeforces.com/problemset/problem/1017/A
# Input Operation :
import sys
n=int(sys.stdin.readline())
# Output Operation :
out=1
first=0 
for i in range(n):
    arr=list(map(int,sys.stdin.readline().split()))
    # Output Operation :
    if i==0:
        first=sum(arr)
    sum_arr=sum(arr)
    if sum_arr>first :
        out+=1
print(out)

# out=1
# for i in sum_arr:
#     if sum_arr[0]<i :
#         out+=1
# print(out)