# Input Operation 

row,coloum=list(map(int, input().split()))
for i in range(row):
    arr=[]
    arr=list(map(str, input().split()))
    for j in range(coloum):
        if arr[0][j]==".":
            if (i+j)%2==0:
                print("B",end='')
            else:print("W",end='')
        else:print("-",end='')
    print("")
    