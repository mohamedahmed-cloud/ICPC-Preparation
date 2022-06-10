# Problem Name : Lists
# Problem Link : https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
###########################################
# Input Operation
n = int(input())
arr_out=[]
# Input Operation
for i in range(n):
    arr= list(input().split())
    # print(arr)
    if arr[0]=="insert":
        arr_out.insert(int(arr[1]),int(arr[2]))
    elif arr[0]=="print":
        print(arr_out)
    elif arr[0]=="remove":
        arr_out.remove(int(arr[1]))
    elif arr[0]=="append":
        arr_out.append(int(arr[1]))
    elif arr[0]=="sort":
        arr_out.sort()
    elif arr[0]=="pop":
        arr_out.pop()
    elif arr[0]=="reverse":
        arr_out.reverse()
# print(arr_out)