import sys
n=int(sys.stdin.readline())
s=list(sys.stdin.readline())
s=s[:-1]
ans=0
i=0
l=len(s)
while i < len(s):
    if s[i] == "V":
        ans+=5
    elif s[i]=="W":
        ans+=2
    elif s[i]=="X":
        i+=1
    elif s[i]=="Y":
        if i<l-1:
            s.append(s[i+1])
            s.remove(s[i+1])
    elif s[i]=="Z":
        if i<l-1 :
            # print("jl")
            if  s[i+1]=="V":
                ans=ans//5
            if s[i+1]=="W":
                ans=ans//2
                if i<l-2:
                    if s[i+2]=="W" or s[i+2]=="V" :
                        i+=1
                        
    i+=1
print(ans)