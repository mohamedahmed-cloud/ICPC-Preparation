t=int(input())
for i in range(t):
    str1=input()
    a=len(str1)
    if a>10:
        print(str1[0]+str(a-2)+str1[-1])
    else:
        print(str1)