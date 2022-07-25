import sys
n=int(sys.stdin.readline())
count=0
for i in range(1,n):
    if n%i==0:
        count+=i
if count==n:
    print("PERFECT NUMBER")
    print(count)
else:
    print("NOT A PERFECT NUMBER")
    print(count)

    