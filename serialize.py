# сериализация данных


user = {
    'firstname': 'Taras',
    'lastname': 'Shevchenko',
    'age': 208,
    'email': 'kobzar_1814@gmail.ua'
}

user_2 = {
    'name': 'Taras',
    'surname': 'Bulba',
    'age': 208,
    'email': 'taras_childfree@gmail.ua'
}
# JSON - javascript object notation


import json

print(type(user), user)
json_string = json.dumps(user)  # превращаем словарь в json
print(type(json_string), json_string)

result_from_string = json.loads(json_string)  # обратно превращаем json  всловарь
print(type(result_from_string), result_from_string)