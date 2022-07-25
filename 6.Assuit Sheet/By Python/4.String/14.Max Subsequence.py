l=int(input())
str=input()
count=1
for i in range(1,l):
    if str[i-1]!=str[i]:
        count+=1
print(count)