# input Operation
arr=[]
sum1=0
for i in range(5):
    arr.extend([list(map(int,input().split()))])
for i in range(5):
    for j in range(5):
        if arr[i][j]==1:
            sum1=abs(i-2)+abs(j-2)
            break
    if sum1>0:
        break
            
print(sum1)
