from copy import deepcopy

#Task 1
dictionary_1 = [{"name": "John", "age": 15}, {"name": "Jack", "age": 45}, {"name": "James", "age": 35},
                {"name": "Jonathan", "age": 25}, {"name": "Jonathan", "age": 15}]
print(dictionary_1)

youngest_name = ['']
longest_name = ['']
youngest_man = 1000
longest_name_size = 0
ave_age = 0

for i in range(0, len(dictionary_1)):
    if dictionary_1[i]['age'] < youngest_man:
        youngest_name.clear()
        youngest_name.append(dictionary_1[i]['name'])
        youngest_man = dictionary_1[i]['age']
    elif dictionary_1[i]['age'] == youngest_man:
        youngest_name.append(dictionary_1[i]['name'])
        youngest_man = dictionary_1[i]['age']

    if len(dictionary_1[i]['name']) > longest_name_size:
        longest_name.clear()
        longest_name.append(dictionary_1[i]['name'])
        longest_name_size = len(dictionary_1[i]['name'])
    elif len(dictionary_1[i]['name']) == longest_name_size:
        longest_name.append(dictionary_1[i]['name'])
        longest_name_size = len(dictionary_1[i]['name'])
    ave_age += dictionary_1[i]['age']
print(f'Youngest person: {youngest_name}')
print(f'Longest name is: {longest_name}')
print('Average age is: ', ave_age//len(dictionary_1))

#Task 2

my_dict_1 = {1: 1, 2: 2, 3: 4, 4: 5, 69: 78}
my_dict_2 = {1: 11, 26: 22, 23: 3, 4: 4}
print(my_dict_1, my_dict_2)


# a
same_key_in_both_dict = []
for key_1 in my_dict_1.keys():
    for key_2 in my_dict_2.keys():
        if key_1 == key_2:
            same_key_in_both_dict.append(key_2)
print(f"a) {same_key_in_both_dict}")


# b
uniq_key_in_first_dict = []
uniq_key_in_first_dict_counter = 0
for key_1 in my_dict_1.keys():
    uniq_key_in_first_dict_counter = 0
    for key_2 in my_dict_2.keys():
        if key_1 == key_2:
            uniq_key_in_first_dict_counter += 1
    if uniq_key_in_first_dict_counter == 0:
        uniq_key_in_first_dict.append(key_1)

print(f"b) {uniq_key_in_first_dict}")

# c
uniq_key_value_in_first_dict = {}
uniq_key_value_in_first_dict_counter = 0
for key_1 in my_dict_1.keys():
    uniq_key_value_in_first_dict_counter = 0
    for key_2 in my_dict_2.keys():
        if key_1 == key_2:
            uniq_key_value_in_first_dict_counter += 1
    if uniq_key_value_in_first_dict_counter == 0:
        uniq_key_value_in_first_dict[key_1] = my_dict_1[key_1]

print(f"c) {uniq_key_value_in_first_dict}")

# d
new_union_dict = deepcopy(my_dict_1)
for key in my_dict_2.keys():
    if key in new_union_dict.keys():
        new_union_dict[key] = list((new_union_dict[key], my_dict_2[key]))
    else:
        new_union_dict.update({key: my_dict_2[key]})
print(f"d) {new_union_dict}")
