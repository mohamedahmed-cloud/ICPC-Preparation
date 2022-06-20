# Link of problem is
# "https://codeforces.com/problemset/problem/1660/B"
# -------------
# Input Operation
test=int(input())
number=[]
for i in range(test):
    type=int(input())
    number=list(map(int,input().split()))
    # outPut operation
    if type==1 :
        if number[0]==1:
            print("YES")
        else:print("NO")
    else:
        number.sort(reverse=True) 
        if number[0]-number[1]==1 or number[0]-number[1]==0:
            print("YES")   
        else:print("NO")    
    