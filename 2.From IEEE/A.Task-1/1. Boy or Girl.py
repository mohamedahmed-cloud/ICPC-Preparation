# Input Operation
his_name = input().split()
# Ouptut Operation
my_list = []
for i in his_name[0]:
    my_list.append(i)

set = set(my_list)
new_list = list(set)
length = len(new_list)
if length % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
