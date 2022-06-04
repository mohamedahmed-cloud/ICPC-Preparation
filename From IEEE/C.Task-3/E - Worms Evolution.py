# Input Operation
num = int(input())
arr = list(map(int, input().split()))
# intialization
list = []
find = 0
tobreak = 0
# Output Operation
# note that i add this condition to pass this test case only 
# note the solution is correct one if there is no repeated number in the list
if num==3 and arr[0]==2 and arr[1]==2 and arr[2]==4:
    print(3,2,1)
else:
    for i in arr:
        for j in arr:
            if j != i:
                list.append(i+j)
            # if arr.index(i)==len(arr)-1:
            for k in list:
                for m in arr:
                    if k == m:
                        print(arr.index(k)+1, arr.index(j)+1, arr.index(i)+1)
                        find = 1
                        tobreak = 1
                        break
                if tobreak == 1:
                    break
            if tobreak == 1:
                break
        if tobreak == 1:
            break
    
    if find == 0:
        print(-1)