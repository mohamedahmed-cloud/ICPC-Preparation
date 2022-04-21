# Input Operation 
a,b= list(map(int, input().split()))
c,d=list(map(int, input().split()))
# Output Operation 

Rick=[]
morty=[]
num=1
# For more accurate answer you can increase the iteration to 10000 instead 1000
for i in range(0,1000):
    Rick.append(b + i*a)
    morty.append(d + i*c )
gen=0
for i in Rick:
    for j in morty:
        if i==j:
            print(i)
            i=gen
            break
    if i==gen:
         break
    num+=1
if num==1001:
    print(-1)
