# input operation
number_of_columns=int(input())
column = list(map(int,input().split())) #input multi integer number in the same line
# output Operation
my_list=sorted(column)                  #sorted list   
#To print list in the same formate that "problem" need: 
for i in range(number_of_columns):
    print(my_list[i],end=' ') 

