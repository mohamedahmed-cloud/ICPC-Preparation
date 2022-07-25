s1=input().split()
iter=0
for i in s1:
    iter+=1
    list1=list(i)
    list1.reverse()
    if iter==len(s1):
        print("".join(list1),end="")
    else:
        print("".join(list1),end=" ")

