# input Operation
n, m = list(map(int, input().split()))
x, y = list(map(int, input().split()))
repeat = int(input())
# output Operation
steps = 0
for i in range(repeat):
    x1, y1 = list(map(int, input().split()))
    while x <= n and y <= m:

        x += x1
        y += y1
        if x <= 0 or y <= 0 or x > n or y > m:
            # print(x, y)
            x -= x1
            y -= y1
            break

        steps += 1


print(steps)
