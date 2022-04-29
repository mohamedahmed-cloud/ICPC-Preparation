n=int(input())
for i in range(n):
    yeah=0
    side=1
    angle=int(input())
    while side<10000:
        if angle*side==(side-2)*180:
            # print(side)
            print("YES")
            yeah=1
            break
        side+=1
    if yeah==0:
        print("NO")

# for _ in range(int(input())):
#     print('YES' if 360%(180-(int(input())))==0 else 'NO')