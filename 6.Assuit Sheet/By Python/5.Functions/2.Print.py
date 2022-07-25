n=int(input())
def Print(n):
    arr=[]
    for i in range(1,n+1):
        arr.append(i)
    return arr
print(*Print(n))
