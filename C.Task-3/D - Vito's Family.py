# Input Operation
test = int(input())
n = []
out = []
for i in range(test):
    n = list(map(int, input().split()))
    # output Operation
    del n[0] #To Remove first element of array 
    sum = 0
    newOne = sorted(set(n))
    for i in range(len(newOne)-1):
        j = i+1
        sum += newOne[j]-newOne[i]
    out.append(sum)
for j in out:
    print(abs(j))


# print(out)


# n = [1, 2, 31, 1, 2, 8]
# newOne =
# print(newOne)
