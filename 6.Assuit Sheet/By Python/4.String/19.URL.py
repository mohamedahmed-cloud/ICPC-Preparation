s= input().split('?')
s1=s[1]
s2=s1.split('&')
for i in s2:
    s3=i.split('=')
    print(s3[0]+ ": " + s3[1])