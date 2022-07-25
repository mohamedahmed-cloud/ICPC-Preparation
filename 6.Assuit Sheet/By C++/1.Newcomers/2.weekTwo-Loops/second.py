import sys
t=int(sys.stdin.readline())
for _ in range(t):
    num=int(sys.stdin.readline())
    count=num
    for i in range(2,num):
        count+=num-i
    print(count+1)