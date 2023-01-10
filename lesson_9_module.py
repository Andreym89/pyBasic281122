def function_1(my_list_arg: list) -> list:
    """
    Функция возвращает новый список в котором содержаться элементы из my_list по следующему правилу:
    Если строка стоит на нечетном месте в my_list, то ее меняет на перевернутую строку. "qwe" на "ewq".
    Если на четном - без изменения.
    :param my_list:
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
    :param my_list:
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
    return my_list_arg


def function_4(my_list_arg: list) -> list:
    """
    Функция возвращает новый список в котором содержаться только строки из my_list. В my_list могут быть строки и числа.
    :param my_list_arg:
    :return: new list
    """
    return my_list_arg


def function_5(my_str: str) -> str:
    return my_str


def function_6(my_str_1: str, my_str_2: str) -> list:
    new_list = []
    return new_list


def function_7(my_str_1: str, my_str_2: str) -> list:
    new_list = []
    return new_list


def function_8(names: list, domains: list) -> str:
    temp_email = ''
    return temp_email