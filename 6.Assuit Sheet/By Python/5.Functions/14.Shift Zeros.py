def solve(arr):
    zero=0
    for i in arr:
        if i!=0:
            print(i,end=" ")
        else:
            zero+=1
    print(("0 "*zero).strip())
import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
solve(arr)