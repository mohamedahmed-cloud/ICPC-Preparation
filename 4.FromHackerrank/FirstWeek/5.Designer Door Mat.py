# Problem Name : Designer Door Mat
# Problem link : https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
# input Operation 
n,m= map(int, input().split())
# input operation End
# Solution Start
iter=(m-3)//2
out=0
for i in range(n//2+1):
    if i==n//2:
            print("-"*((m-7)//2)+"Mohamed"+"-"*((m-7)//2))
    else:
        j=0
        while j<m:
            if j==iter:
                iter-=3
                print(".|."*(i*2+1),end='')
                out=i*2+1
                j+=(i*2+1)*3
            else:
                j+=1
                print("-",end='')
        print()
iter+=3
for i in range(n//2):
    j=0
    while j<m:
        if j==iter:
            iter+=3
            print(".|."*((m-6)//3-i*2),end='')
            j+=(m-6)-i*6
            if i==n//2-1:
                print("-"*((m-3)//2),end='')
                break
        else:
            print("-",end='')
            j+=1
    print()
