# task_1
import random

my_list = [random.randint(1, 200) for i in range(20)]
for index in range(len(my_list)):
    if my_list[index] > 100:
        print(my_list[index], end=' ')
print()
#print(my_list)

# task_2
my_result = []
for index in range(len(my_list)):
    if my_list[index] > 100:
        my_result.insert(1, my_list[index])
print(my_result)

# task_3
if len(my_list) < 2:
    my_list.append(0)
elif len(my_list) >= 2:
    my_list.append(my_list[-1]+my_list[-2])
else:
    pass
#print(my_list)

# task_4
# task_5
# task_6