# Problem Name :Maximum Square
# Problem Link : https://codeforces.com/problemset/problem/1243/A
# Input Operation
import sys
test=int(sys.stdin.readline())
for i in range(test):
    n=int(sys.stdin.readline())
    arr=list(map(int,sys.stdin.readline().split()))
    arr.sort()
    if len(set(arr))==1:
        print(arr[0])
    else:
        for i in range(1,n):
            if len(arr[i:])>arr[i]:
                continue
            elif len(arr[i:])==arr[i]:
                print(arr[i])
                break
            else:
                print(len(arr[i:]))
                break 