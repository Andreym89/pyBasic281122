import random
# task_1
'''
my_list1 = [random.randint(1, 200) for i in range(20)]
for index in range(len(my_list1)):
    if my_list1[index] > 100:
        print(my_list1[index], end=' ')
print()
#print(my_list)

# task_2
my_result = []
for index in range(len(my_list1)):
    if my_list1[index] > 100:
        my_result.insert(1, my_list1[index])
print(my_result)

# task_3
if len(my_list1) < 2:
    my_list1.append(0)
elif len(my_list1) >= 2:
    my_list1.append(my_list1[-1]+my_list1[-2])
else:
    pass
#print(my_list)
'''
# task_4
# task_5
my_list5 = [random.randint(-100, 100) for i in range(20)]
print(my_list5)
k = 5
C = 7
for index in range(len(my_list5)+1):
    if index == k:
        my_list5.append(0)
        for j in range(len(my_list5)-1, k, -1):
            my_list5[j] = my_list5[j-1]
        my_list5[k] = C
    else:
        pass
print(my_list5)

'''
# task_6
my_list6 = [random.randint(-100, 100) for i in range(20)]
my_list7 = [random.randint(-100, 100) for i in range(20)]
print('Uniq valuse count in my_list6 and my_list7: ', len(set(my_list1)) + len(set(my_list2)))
'''