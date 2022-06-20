# input Operation
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
out=[]
for i in range(int(n/3)):
    a=arr[i]
    b=arr[i+int(n/3)]
    c=arr[i+2*int(n/3)]
    if a<b and b<c and b%a==0 and c%b==0:
        # print([a,b,c])
        out.append([a,b,c])
    else:
        break
if len(out)==int(n/3):
    for i in out:
        for j in i :
            print(j,end=' ')
        print()
else:print(-1)
