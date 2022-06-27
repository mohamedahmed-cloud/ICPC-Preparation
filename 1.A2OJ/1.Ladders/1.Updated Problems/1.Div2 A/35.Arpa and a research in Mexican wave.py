# Problem Name : Arpa and a research in Mexican wave
# Problem Link : https://codeforces.com/problemset/problem/851/A
# Input  Operation 
import sys
n,k,t=map(int,sys.stdin.readline().split())
# Input Operation End
# Solution Start
if k>t:
    print(t)
elif t>=k and t<=n:
    print(k)
elif t>n:
    out=t-n
    out2=k-out
    if k<=0:
        print(0)
    else:print(out2)