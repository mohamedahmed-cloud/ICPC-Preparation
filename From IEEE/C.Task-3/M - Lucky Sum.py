l, r = list(map(int, input().split()))
output = 0
j = 0
list = [4, 7]
min = l-1

while list[j] < l:
    list.append(list[j]*10+4)
    list.append(list[j]*10+7)
    j += 1

while list[j] <= r:
    output = output+(list[j]-min)*list[j]
    list.append(list[j]*10+4)
    list.append(list[j]*10+7)
    min = list[j]
    j += 1

output = output + (r-min)*list[j]
print(output)
