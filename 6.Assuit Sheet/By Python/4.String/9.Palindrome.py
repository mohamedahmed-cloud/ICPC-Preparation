str=input()
check=""
for i in range(len(str)-1,-1,-1):
    check+=str[i]
# print(check)
if str==check:
    print("YES")
else:print("NO")