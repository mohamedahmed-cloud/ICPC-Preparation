# Problem Name : Petya and Origami
# Problem Link :https://codeforces.com/problemset/problem/1080/A

# Input Operation
import math


n,k=map(int,input().split())
# Output Operation
print(math.ceil(n*(2/k))+math.ceil(n*(5/k))+math.ceil(n*(8/k)))