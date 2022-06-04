# Input Operation
num=int(input())
ticket=input()
first=sorted(ticket[:num])
second=sorted(ticket[num:])

# print(first, second)
# Output operation
if all(x>y for x,y in zip(first,second) ) or all(x<y for x,y in zip(first,second) ) :
    print("YES")
else :print("NO")
