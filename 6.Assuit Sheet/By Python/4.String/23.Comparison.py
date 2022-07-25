import string
s=list(input())
s.sort()
for i in s:
    if i in string.ascii_lowercase:
        print(i,end="")

