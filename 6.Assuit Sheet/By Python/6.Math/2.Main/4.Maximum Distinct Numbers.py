import math
def solve(n):
    return (-1 + math.sqrt(1 + 8 * n)) // 2
n=int(input())
print(int(solve(n)))