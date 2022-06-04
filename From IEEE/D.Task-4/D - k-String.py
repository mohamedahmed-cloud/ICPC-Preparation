# input Operation 
k=int(input())
string=input()
arr=[]
arr2=[]
set1=()
go=1
# output operation
arr=sorted(string)
set1=set(string)
arr2=sorted(set1)
# print(set1)
for i in arr2:
    if arr.count(i)%k==0:
        go=1
    else:
        go=0
        print(-1)
        break
out=""
if go==1:
    for i in range(k):
        for j in arr2:
            # print((arr.count(j)/k))
            out+=(j*int((arr.count(j)/k)))
if go==1:
    print(out)