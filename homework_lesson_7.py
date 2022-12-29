from random import randint

# task 3
my_list_1 = [randint(0, 100) for i in range(5)]
my_list_2 = [randint(0, 100) for i in range(5)]
print(my_list_1)
print(my_list_2)
my_result = []
for index in range(0, len(my_list_1) + 1, 2):
    my_result.insert(index, my_list_1[index])
for index in range(1, len(my_list_2), 2):
    my_result.insert(index, my_list_2[index])
print(my_result)

# task 11
my_string = 'aassddccvbb09'
print(my_string)
my_list_3 = []
for index in range(0, len(my_string)):
    if my_string.count(my_string[index]) == 1:
        my_list_3.append(my_string[index])
print(my_list_3)

# task 4
my_list = [1, 2, 3, 4, 5]
print(my_list)
new_list = my_list
new_list.append(my_list[0])
new_list.pop(0)
print(new_list)

# task 5
my_list = [1, 2, 3, 4, 5]
print(my_list)
my_list[0], my_list[-1] = my_list[-1], my_list[0]
print(my_list)
