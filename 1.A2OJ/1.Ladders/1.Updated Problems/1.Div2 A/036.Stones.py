# Problem Name : Stones
# Problem Link : https://codeforces.com/problemset/problem/1236/A
# Input Operation
import sys
n=int(sys.stdin.readline())
for i in range(n):
    stone=0
    A,B,C=map(int,sys.stdin.readline().split())
    while (B>=1 and C>=2):
        stone+=3
        B-=1
        C-=2
    while (A>=1 and B>=2 ):
        stone+=3
        A-=1
        B-=2
    print(stone)
