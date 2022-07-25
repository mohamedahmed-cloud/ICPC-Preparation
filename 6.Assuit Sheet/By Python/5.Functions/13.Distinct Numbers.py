import sys
from collections import Counter
def solve(arr):
    l=Counter(arr).most_common()
    return len(l)

n=int(input())
arr=list(map(int, sys.stdin.readline().split()))
print(solve(arr))