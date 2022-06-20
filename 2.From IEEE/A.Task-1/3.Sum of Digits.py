# input Operation
number = input()

# Output Operation
counter = 0
new_number = 0
if len(number) == 1:
    print(0)
else:

    while(len(number)) > 1:
        for i in list(number):
            new_number += int(i)
        counter += 1
        number = str(new_number)
        new_number = 0

    print(counter)
