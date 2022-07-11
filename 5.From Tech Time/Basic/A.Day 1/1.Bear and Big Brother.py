# input operation 
limak,bob=list(map(int,input().split()))

# output operation

years=1
while (2**years)*bob>=(3**years)*limak:
    years+=1
    
if limak > bob: 
    print(0)
else:
    print(years)