# problem Name : Compote
# probelm Link : https://codeforces.com/problemset/problem/746/A
# Input Operation 
import sys
lem=int(sys.stdin.readline())
app=int(sys.stdin.readline())
pears=int(sys.stdin.readline())
out=0
while (lem>=1 and app>=2 and pears>=4):
    out+=7
    lem-=1
    app-=2
    pears-=4
print(out)
