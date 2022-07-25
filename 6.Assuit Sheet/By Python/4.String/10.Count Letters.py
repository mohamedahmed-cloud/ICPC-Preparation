from collections import Counter 
str1=input()
count=Counter(str1)
main=count.most_common()
# print(main)
main.sort()
# print(main)
for i in range(len(main)):
    print(main[i][0] + " : " + str(main[i][1]))
