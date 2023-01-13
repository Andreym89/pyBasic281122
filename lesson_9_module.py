import random


def function_1(my_list_arg: list) -> list:
    """
    Функция возвращает новый список в котором содержаться элементы из my_list по следующему правилу:
    Если строка стоит на нечетном месте в my_list, то ее меняет на перевернутую строку. "qwe" на "ewq".
    Если на четном - без изменения.
    :param my_list_arg:
    :return: new list
    """
    for i in range(0, len(my_list_arg)):
        if i == 0:
            my_list_arg[i] = my_list_arg[i][::-1]
        elif i % 2 == 0:
            my_list_arg[i] = my_list_arg[i][::-1]
    return my_list_arg


def function_2(my_list_arg: list) -> list:
    """
    Функция возвращает новый список в котором содержаться элементы из my_list у которых первый символ - буква "a"
    :param my_list_arg:
    :return: new list
    """
    temp_indexed_value: str
    for i in range(0, len(my_list_arg)):
        my_list_arg[i] = my_list_arg[i][:0] + 'a' + my_list_arg[i][1:]
    return my_list_arg


def function_3(my_list_arg: list) -> list:
    """
    Функция возвращает новый список в котором содержаться элементы из my_list в которых есть символ - буква "a" на
    любом месте.
    :param my_list_arg:
    :return: new list
    """
    new_list_with_a_char = []
    for i in range(0, len(my_list_arg)):
        if 'a' in my_list_arg[i]:
            new_list_with_a_char.append(my_list_arg[i])
    return new_list_with_a_char


def function_4(my_list_arg: list) -> list:
    """
    Функция возвращает новый список в котором содержаться только строки из my_list. В my_list могут быть строки и числа.
    :param my_list_arg:
    :return: new list
    """
    returned_string_list = []
    for i in range(0, len(my_list_arg)):
        if isinstance(my_list_arg[i], str):
            returned_string_list.append(my_list_arg[i])

    return returned_string_list


def function_5(my_str: str) -> list:
    return_list = []
    uniq_counter = 0
    for i in range(0, len(my_str)):
        uniq_counter = 0
        for j in range(0, len(my_str)):
            if my_str[i] == my_str[j]:
                uniq_counter += 1
        if uniq_counter == 1:
            return_list.append(my_str[i])
    return return_list


def function_6(my_str_1: str, my_str_2: str) -> list:
    """
    Функция возвращает список в который поместить те символы, которые есть в обеих строках хотя бы раз.
    :param my_str_1:
    :param my_str_2:
    :return:
    """

    new_list = []
    for i_str1 in range(0, len(my_str_1)):
        for j_str2 in range(0, len(my_str_2)):
            if my_str_1[i_str1] == my_str_2[j_str2]:
                new_list.append(my_str_1[i_str1])
    new_list.sort()
    new_list_copy = new_list.copy()
    index_compensation = 0
    for i in range(1, len(new_list)):
        if new_list[i] == new_list[i - 1]:
            new_list_copy.pop(i - index_compensation)
            index_compensation += 1
    return new_list_copy


def function_7(my_str_1: str, my_str_2: str) -> list:
    """
    Функция возвращает список в который поместить те символы, которые есть в обеих строках,
    но в каждой только по одному разу.
    :param my_str_1:
    :param my_str_2:
    :return:
    """
    new_list = []
    for i_str1 in range(0, len(my_str_1)):
        for j_str2 in range(0, len(my_str_2)):
            if my_str_1[i_str1] == my_str_2[j_str2]:
                new_list.append(my_str_1[i_str1])
    new_list.sort()
    new_list_uniq = []
    for i in range(1, len(new_list)):
        if new_list[i] != new_list[i - 1]:
            new_list_uniq.append(new_list[i - 1])
    return new_list_uniq


def function_8(names: list, domains: list) -> str:
    """
    Функция для генерирования e-mail в формате:
    фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
    :param list of names:
    :param list of domains:
    :return: string
    """
    temp_email = names[random.randint(0, len(names) - 1)] + str(random.randint(100, 999)) + random_chars() + '@' + \
                 domains[random.randint(0, len(domains) - 1)]
    return temp_email


def random_chars() -> str:
    """
    Функция возвращающая строку из случайных букв [a-z] с длиной 5-7 символов
    :return: string of chars
    """
    result_string = ''
    chars = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(0, random.randint(5, 7)):
        result_string += chars[random.randint(0, len(chars) - 1)]
    return result_string