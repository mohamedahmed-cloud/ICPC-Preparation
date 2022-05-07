# Link of problem is
# "https://codeforces.com/problemset/problem/1660/A"
# -------------
# Input Operation
test=int(input())
for i in range(test):
    a,b=map(int,input().split())
    # Ouput Operation
    if a==0:
        print(1)
    else:print(a+b*2+1)
