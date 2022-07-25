import sys
l=int(sys.stdin.readline())
frequency=[0]*26
for i in input():
    add=ord(i)-ord('a')
    frequency[add]+=1
for i in range(len(frequency)):
    print(chr(97+i)*frequency[i],end="")

