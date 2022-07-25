import sys,re
s=input()
r=re.split(r"[L]*L",s)
l=re.split(r"[R]*R",s)
# print(l)
# print(r)
nl,nr=0,0
count=0
lastn,lastl=0,0
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
        count+=1
print(count)

for i in range(len(l)):
    for j in range(len(r)):
        if len(l[i])==len(r[j]) and l[i]!="" and r[j]!="":
            if i<j:
                print(l[i]+r[j])
            else:
                print(r[i]+l[j])