number_of_problems=int(input())
counter=0
for i in range(number_of_problems):
    a,b,c=list(map(int,input().split()))
    if (a+b+c)>=2:
        counter+=1

print(counter)
