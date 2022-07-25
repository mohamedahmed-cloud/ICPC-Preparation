s=input()
nl,nr=0,0
count=0
lastn,lastl=0,0
arr=[0]
for i in s:
    if i=="L":
        nl+=1
    elif i=="R":
        nr+=1
    
    if nl>0:
        lastl=nl
    if nr>0:
        lastn=nr
    
    if lastl==lastn:
        arr.append(lastl+lastn)
        count+=1
print(count)
iter=0
for i in range(len(arr)-1):
    print(s[arr[iter]:arr[iter+1]])
    iter+=1
