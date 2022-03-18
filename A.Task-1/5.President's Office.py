# # Input Operation
n, m, p = input().split()
n, m = int(n), int(m)
a = [""]*n
# print(a)
for i in range(n):
    a[i] = input()
# print(a)
# Ouput Operation
office = set()
for i in range(n):
    for j in range(m):
        if a[i][j] == p:
            for x, y in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
                if x in range(n) and y in range(m) and a[x][y] != ".":
                    office.add(a[x][y])
# print(office)
print(len(office-{p}))
