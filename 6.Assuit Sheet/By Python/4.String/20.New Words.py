frequency=[0]*5
s=input()
arr=["e","g","y","p","t"]
# indexs=[0,1,2,3,4]
for i in s:
    if i.lower() in "egypt":
        add=arr.index(i.lower())
        frequency[add]+=1
# print(frequency)
print(min(frequency))