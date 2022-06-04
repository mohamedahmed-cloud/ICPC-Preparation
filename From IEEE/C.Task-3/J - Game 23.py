# input Operataion 
min,max=list(map(int, input().split()))
trans=0
for i in [2,3]:
    while max%(min*i)==0 :
        min=min*i
        trans+=1
if min==max:
    print(trans)
else:
    print(-1)
