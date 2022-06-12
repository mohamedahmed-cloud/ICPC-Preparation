# Problem Name :Infinity Gauntlet
# problem Link : https://codeforces.com/problemset/problem/987/A
# Input Operation
n=int(input())
arr=[]
for i in range(n):
    arr.append(input())
# output Operation
check=["purple", "green", "blue", "orange", "red", "yellow"]
check2=["Power","Time","Space","Soul","Reality","Mind"]
print(6-n)
for i in range(6):
    if check[i] in arr:
        continue
    else:
        print(check2[i])
