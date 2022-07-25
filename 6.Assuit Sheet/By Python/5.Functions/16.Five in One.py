import math,sys

def Max(arr):
    return  "The maximum number : "+str(arr[-1])
def Min(arr):
    return  "The minimum number : "+str(arr[0])

def  prime(arr):
    count=0
    for i in arr:
        out=0
        if i==0 or i ==1:
            out=1
            pass
        else:
            for j in range(2,int(math.sqrt(i))+1):
                if i%j==0:
                    # print(i)
                    out=1
                    break
        if out==0:
            count+=1
    return "The number of prime numbers : "+str(count)

def palindrome(arr):
    count=0
    for i in arr:
        l=list(str(i))
        l.reverse()
        ans=""
        for j in l:
            ans+=j
        if i==int(ans):
            count+=1
    return "The number of palindrome numbers : "+str(count)
def maximum_number_of_divisors(arr,n):
    ans=[0]*n
    for i in range(n):
        for j in range(1,arr[i]):
            if arr[i]%j==0:
                ans[i]+=1
    # Max=max(ans)
    # l=ans.index(Max)
    max=0
    index=0
    for i in range(n):
        if max<=ans[i]:
            max=ans[i]
            index=i
    return "The number that has the maximum number of divisors : "+str(arr[index])
n=int(input())
arr=list(map(int, sys.stdin.readline().split()))
arr.sort()
print(Max(arr))
print(Min(arr))
print(prime(arr))
print(palindrome(arr))
print(maximum_number_of_divisors(arr,n))
