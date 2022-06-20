go=0
arr1=list(map(str, input().split()))
arr2=list(map(str, input().split()))
arr3=list(map(str, input().split()))
arr4=list(map(str, input().split()))
for i in range(1,4):
        # print(i,i-1)
        if arr1[0][i-1]==arr2[0][i-1] and (arr1[0][i]==arr1[0][i-1] or arr2[0][i]==arr2[0][i-1] ) :
            print("YES")
            go=0
            break
        elif arr2[0][i-1]==arr3[0][i-1] and (arr3[0][i]==arr3[0][i-1] or arr2[0][i]==arr2[0][i-1] ):
            print("YES")
            go=0
            break
        elif arr3[0][i-1]==arr4[0][i-1] and (arr3[0][i]==arr3[0][i-1] or arr4[0][i]==arr4[0][i-1] ):
            print("YES")
            go=0
            break
        if i==3:
            if arr1[0][i]==arr2[0][i] and (arr1[0][i]==arr1[0][i-1] or arr2[0][i]==arr2[0][i-1] ) :
                print("YES")
                go=0
                break
            elif arr2[0][i]==arr3[0][i] and (arr3[0][i]==arr3[0][i-1] or arr2[0][i]==arr2[0][i-1] ):
                print("YES")
                go=0
                break
            elif arr3[0][i]==arr4[0][i] and (arr3[0][i]==arr3[0][i-1] or arr4[0][i]==arr4[0][i-1] ):
                print("YES")
                go=0
                break


        else:
            go=1
if go==1:
    print("NO")