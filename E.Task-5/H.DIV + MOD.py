# Link of problem is
# "https://codeforces.com/problemset/problem/1650/B"
# -------------
# input Operation
test=int(input())
for i in range(test):
    l,r,a=map(int,input().split())

    # output Operation
    out=[]
    maxPoint=[]
    # max point
    # Important note the max point is
    #  the end or
    #  the  "value this value when divide on "a" give me two number 
    # first is second largest integer can given by integer division
    # second the largest modulus " This might be the max value 
    #  Example if i have "2,100,30" the max point is 100 and 89 
    # because when divide on 30 give 2 and when modulus on 30 give 29.
    maxPoint=[max(l,int(r/a)*a-1),r]
    for j in maxPoint:
        # print(j)
        out.append(int(j/a)+int(j%a))
                
    print(max(out))