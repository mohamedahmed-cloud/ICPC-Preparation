# Problem Name : Changing Volume
# Problem Link : https://codeforces.com/problemset/problem/1255/A
# Input Operation
import sys
n=int(sys.stdin.readline())
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    press=0
    if a>b:
        while a-b>=5*1000:
            a-=5*1000
            press+=1000
        while a-b>=5*200:
            a-=5*200
            press+=200
        while a-b>=5*20:
            a-=5*20
            press+=20
        while a-b>=5:
            press+=1
            a-=5
        while a-b>=2:
            press+=1
            a-=2
        while a-b>=1:
            press+=1
            a-=1
    elif a==b:
        press=0
    else:
        while b-a>5*1000:
            a+=5*1000
            press+=1000
        while b-a>=5*200:
            a+=5*200
            press+=200
        while b-a>=5*20:
            a+=5*20
            press+=20
        while b-a>=5:
            press+=1
            a+=5
        while b-a>=2:
            press+=1
            a+=2
        while b-a>=1:
            press+=1
            a+=1    
    print(press)


    