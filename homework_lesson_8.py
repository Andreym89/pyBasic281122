
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
print('\nAverage age is: ', ave_age//len(dictionary_1))
