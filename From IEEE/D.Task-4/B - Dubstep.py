string=input()
repeat=True
# tring something
# for "WUB" in string:
#     print("help")
# string="Helloman"
# if "man" in string:
#     string=string.replace("man", "")
# print(string)
while True:
    if "WUB" in string:
        string=string.replace("WUB"," ")
    else:
        repeat=False
        break
print(string.strip())