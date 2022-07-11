string=input().split()
my_list=[]
for i in string[0]:
    my_list.append(i)
# print(my_list)
my_set=set(my_list)
length=len(my_set)
if length%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")