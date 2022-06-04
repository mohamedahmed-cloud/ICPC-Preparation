# Input operation

out=[]
for i in range(int(input())):
        int(input()) 
        n=list(map(int,input().split()))
        # outPut operation
        number=1
        while(number<=1024):
            mylist=[]
            for i in n:
                mylist.append(number^i)
            if sorted(mylist)==sorted(n):
                # print(sorted(mylist))
                # print(sorted(n))
                out.append(number)
                break
            number+=1
            if number==1025:
                out.append(-1)
for i in out:
    print(i)
