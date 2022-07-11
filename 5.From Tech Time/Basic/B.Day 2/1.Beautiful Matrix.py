# my varibles

counter=0
number_of_moves=0
my_count=0
# my input and output operations

for i in range(5):
    counter+=1 #count the number of rows 
    my_str=list(map(int, input().split()))

    # output operations
    if 1 in my_str:
        Need_list=my_str #store my needed list "that contain a "one"  "
        my_count=counter # to give stop counter to give a correct value
        My_index=Need_list.index(1) #give me index of element "one"
        number_of_moves=abs(3-my_count)+abs(2-My_index)   #This relation I conclude by trying solve one example on a paper
print(number_of_moves)


# my_str=[]
# print(my_count)
# print(My_index)
