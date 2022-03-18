# input Operation
import string


n, k = list(map(int, input().split()))

# output Operation
counter = 0
for i in range(n):
    sign, value = list(map(str, input().split()))
    if sign == "+":
        k += int(value)
    else:
        if k >= int(value):
            k -= int(value)
        else:
            counter += 1

print(k, end=' ')
print(counter)
