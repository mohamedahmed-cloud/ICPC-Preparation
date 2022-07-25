import sys
import math
test=int(sys.stdin.readline())
for i in range(test):
    num=int(sys.stdin.readline())
    num1=1
    num2=1
    for i in range(1,num+1):
        num1*=i
        num2*=(i+1)
    fin=num2//num1
    # print(fin)
    # print(math.sqrt(fin))
    # print(float(math.ceil(math.sqrt(fin))))
    if math.sqrt(fin)==float(math.ceil(math.sqrt(fin))):
        print(int(math.sqrt(fin)))
    else:
        print(-1)
    # else:
    #     print(-1)