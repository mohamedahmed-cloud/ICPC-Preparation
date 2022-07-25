import sys
t=int(sys.stdin.readline())
for _ in range(t):
    num=int(sys.stdin.readline())
    count=num
    if num>2:
        count=abs((num)-(num*(num+1)/2))
        print(int(count+1))
        break
    print(count)
