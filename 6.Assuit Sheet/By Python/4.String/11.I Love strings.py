t=int(input())
for i in range(t):
    ans=""
    s1,s2=map(str,input().split())
    i=0
    for i in range(min(len(s1),len(s2))):
        ans+=s1[i]+s2[i]
        # s1=s1[i:]
        # s2=s2[i:]
    if i<len(s1)-1:
        ans+=s1[i+1:]
    if i<len(s2)-1:
        ans+=s2[i+1:]
    print(ans)

