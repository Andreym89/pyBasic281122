import random

# task_1
my_list1 = [random.randint(1, 200) for i in range(20)]
for index in range(len(my_list1)):
    if my_list1[index] > 100:
        print(my_list1[index], end=' ')
print()


# task_2
my_result = []
for index in range(len(my_list1)):
    if my_list1[index] > 100:
        my_result.insert(1, my_list1[index])
print(my_result)


# task_3
my_list3 = [random.randint(1, 200) for i in range(20)]
if len(my_list3) < 2:
    my_list3.append(0)
elif len(my_list3) >= 2:
    my_list3.append(my_list3[-1] + my_list3[-2])
else:
    pass


# task_4
my_list4 = [random.randint(-100, 100) for i in range(20)]
k = 3
for index in range(k - 1, len(my_list4)):
    if index < len(my_list4):
        my_list4[index - 1] = my_list4[index]
    else:
        break
my_list4.pop()


# task_5
my_list5 = [random.randint(-100, 100) for i in range(20)]
k = 5
C = 7
for index in range(len(my_list5) + 1):
    if index == k:
        my_list5.append(0)
        for j in range(len(my_list5) - 1, k, -1):
            my_list5[j] = my_list5[j - 1]
        my_list5[k] = C
    else:
        pass


# task_6
my_list6 = [random.randint(-100, 100) for i in range(20)]
my_list7 = [random.randint(-100, 100) for i in range(20)]
print('Uniq valuse count in my_list6 and my_list7: ', len(set(my_list6)) + len(set(my_list7)))
