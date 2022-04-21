
# Give right Answer but time exceed 


# input Operation 
test=int(input())
for i in range(test):
    A,B,C=list(map(int, input().split()))
    # Output Operation 
    done=0
    for i in range(-58,58):
        for J in range(-22,22):
            for k in range(-100,100):
                if i+J+k== A and i*J *k == B and  i**2 + J**2 +k**2 == C :
                    print(i,J,k)
                    done=1
                    break
            if done==1:break
        if done==1:break            
    if done==0:
        print("No solution.")



