# Link of problem is
# "https://codeforces.com/problemset/problem/1672/A"
# -------------
# INput Operation
test=int(input())
arr=[]
for i in range(test):
    n=int(input())
    arr=list(map(int,input().split()))
    # Output Operation
    arr.sort(reverse=True)
    count=0
    for i in arr:
        while(i>=2):
            i-=1
            count+=1
        # else:break
    if count%2 == 0:
        print("maomao90")
    else:print("errorgorn")