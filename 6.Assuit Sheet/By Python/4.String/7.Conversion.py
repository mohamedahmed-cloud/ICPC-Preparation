string=input()
concat=""
for i in string:
    if i.isupper():
        concat +=i.lower()
    elif i.islower():
        concat +=i.upper()
    if i==",":
        concat += " "
    if i ==" ":
        concat +=" "
print(concat)