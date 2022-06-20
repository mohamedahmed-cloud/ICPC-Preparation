# Remember in 2022-2-29 this problem make me mad man 
n,a,b,c=map(int,input().split())
out=[0]*(n+1)
out[0]=0
for i in range(n+1):
    for j in [a,b,c]:
        if i+j<=n and (out[i]>0 or i in [a,b,c,0]):
            out[i+j]=max(out[i+j],out[i]+1)
            # print(i,j)
            # print(out)
print(out[-1])
# print(out)
