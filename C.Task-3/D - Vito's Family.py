# Time Limit
# Input Operation
list1 = []
for i in range(int(input())):
    list1 = list(map(int, input().split()))
    del list1[0]
    # output Operatioin
    sum1 = 100000000000
    for j in list1:
        sum = 0
        for k in list1:
            sum += abs(j-k)
        if sum < sum1:
            sum1 = sum
    print(sum1)

# Another Two Solution 
# from numpy import repeat

# from numpy import sort

# It Give Time limit

out=0
arr=[]
for i in range(int(input())) :
    arr=list(map(int,input().split()))
    if arr[0]%2==0:
        repeated=arr[0]
        del arr[0]
        # Sort to get medium
        mysort=sorted(arr)
        # Check the first medium number
        med=mysort[int(repeated/2)]
        # sumation
        sum1=0
        out1=0
        for k in mysort:
            sum1+=abs(med-k)
        # check the second meduim number
        med2=mysort[int(repeated/2)-1]
        # sumation
        sum2=0
        for k in mysort:
            sum2+=abs(med-k)
        # compare two meduim numbers
        if sum1<sum2:
            out1=sum1
        else:
            out1=sum2

        # if there is repeated number
        counted=[]
        for k in mysort:
            if mysort.count(k)<=2 and k!=med and k!=med2:
                counted.append(k)
        sum4=0
        sum5=1000000000000000
        for k in mysort:
            for m in counted:
                sum4+=abs(m-k)
            if sum4<sum5 :
                sum5=sum4
        # compare counted out with medium out
        if sum5<out1:
            out=sum5
        else:
            out=out1
        
    else:
        repeated=arr[0]
        del arr[0]
        # Sort to get medium
        mysort=sorted(arr)
        # Check the medium number
        med=mysort[int(repeated/2)]
        # sumation
        sum1=0
        for k in mysort:
            sum1+=abs(med-k)
        # if there is repeated number
        counted=[]
        for k in mysort:
            if mysort.count(k)<=2 and k !=med:
                counted.append(k)
        sum2=0
        sum3=1000000000000000
        for k in mysort:
            for m in counted:
                sum2+=abs(m-k)
            if sum2<sum3 :
                sum3=sum2
        # compare counted out with medium out
        if sum3<sum1:
            out=sum3
        else:
            out=sum1
        
    print(out)
            


# # Another Good one

# Input Operation
test = int(input())
for i in range(test):
    arr = list(map(int,input().split()))
    # Output Operation
    count = arr[0]
    locations = sorted(arr[1:])
    med = int(count/2)
    distance = 0
    for i in range(0, count):
        distance += abs((locations[med] - locations[i]))
    print(distance)
