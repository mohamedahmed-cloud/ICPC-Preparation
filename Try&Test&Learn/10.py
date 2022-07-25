import sys
w,y = map(int, sys.stdin.readline().split())
arr=[]
for i in range(y):
    x,y=map(int,sys.stdin.readline().split())
    arr.append(x)
    arr.append(y)
a,b=arr[0],arr[1]
for i in range(0,len(arr),2):
    if arr[i]>a:
        a=arr[i]
for i in range(1,len(arr),2):
    if arr[i]<b:
        b=arr[i]
out=0 

if a>b:
    print(0)
    quit()
# print(arr[0:2])   
for i in range(0,len(arr),2):
    if (a>=arr[i] and a<=arr[i+1]) and (b>=arr[i] and b<=arr[i+1]):
        out=1
    else:
        print(0)
        out=0
        break
if out==1:
    print(max(a,b))