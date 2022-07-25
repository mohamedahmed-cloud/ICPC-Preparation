string="hello"
s1=input()
ans=""
x=0
for i in s1:
    if i == string[x]:
        ans+=i
        x+=1
        if ans=="hello":
            break
# print(ans)
if ans=="hello":
    print("YES")
else:print("NO")
    