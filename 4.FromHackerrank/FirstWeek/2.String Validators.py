# Problem Name : String Validators
# Problem Link : https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
# ###########################################
# Input Operation
str=input()

out1=0
out2=0
out3=0
out4=0
out5=0
# Output Operation
for i in range(len(str)):
    if str[i].isalnum():
        print(True)
        out1=0
        break
        
    else:
        out1=1
if out1==1:
    print(False)
for i in range(len(str)):       
    if str[i].isalpha():
        print(True)
        out2=0
        break
        
    else:
        out2=1
if out2==1:
    print(False)
for i in range(len(str)):
    if str[i].isdigit():
        print(True)
        out3=0
        break
        
    else:
        out3=1
if out3==1:
    print(False)
for i in range(len(str)):
    if str[i].islower():
        print(True)
        out4=0
        break
        
    else:
        out4=1
if out4==1:
    print(False)
for i in range(len(str)):
    if str[i].isupper():
        print(True)
        out5=0
        break
        
    else:
        out5=1
if out5==1:
    print(False)
# ###########################################