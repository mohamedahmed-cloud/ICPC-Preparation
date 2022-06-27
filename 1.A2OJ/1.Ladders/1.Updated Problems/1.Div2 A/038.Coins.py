# Problem Name : Coins
# Probelm Link : https://codeforces.com/problemset/problem/1061/A
# INput Opeation 
import sys
n,s=map(int,sys.stdin.readline().split())
coins=0
while s!=0:
    while n<=s:
        s-=n
        coins+=1
    else:
        n=s
print(coins)