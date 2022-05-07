# Link of problem is
# "https://codeforces.com/problemset/problem/1661/A"
# -------------
# Input Operation
test=int(input())
# variable
arra=[]
arrb=[]
for i in range(test):
        n=int(input())
        arra=list(map(int,input().split()))
        arrb=list(map(int,input().split()))
        # Ouput Operation
        out=[]
        for i in range(1,n):
                a=abs(arra[i-1]-arra[i])+abs(arrb[i-1]-arrb[i])
                b=abs(arra[i-1]-arrb[i])+abs(arrb[i-1]-arra[i])
                out.append(min(a,b))
        print(sum(out))