import re,string
s=input()
space=" "
count=0
ans = re.split(r"[!,\\?.\s]\s*", s)
for i in ans:
    x=list(i)
    for j in x:
        if j.lower() in string.ascii_lowercase:
            count+=1
            break
print(count)
# Second solution 

