# Task 1
def func_additional_explore_error_in_divider():
    """
    Функция, которая последовательно делит элементы двух разных списков и выводит в консоль подробное описание ошибки
    :return:
    """
    divide_values = [2, 0, None, "1", True, False, [], {}]
    values_to_devide = [10, "1", None, True, False, [], 0, {}]
    print('Task 1:')
    if len(divide_values) == len(values_to_devide):
        for i in range(0, len(divide_values)):
            try:
                print(divide_values[i] / values_to_devide[i])
            except TypeError:
                print('Не можна комбінувати ці типи даних')
            except ZeroDivisionError:
                print("Ділити на нуль не можна!")


# Task 2
def func_divider():
    """
        Функция, которая последовательно делит элементы двух разных списков и выводит в консоль одно из 2
        состояние выполнения деления:
            - Щось пішло не так
            - Ділення пройшло успішно!
        :return:
        """
    divide_values = [2, 0, None, "1", True, False, [], {}]
    values_to_devide = [10, "1", None, True, False, [], 0, {}]
    print('Task 2:')
    if len(divide_values) == len(values_to_devide):
        for i in range(0, len(divide_values)):
            try:
                divide_values[i] / values_to_devide[i]
            except Exception:
                print('Щось пішло не так')
            else:
                print('Ділення пройшло успішно!')


# Task 3
def index_printer():
    """
    Функция которая позволяет ввести индекс и получить вывод его значения в консоль
    в случае некорректного индекса пишет в консоль - Потрібно ввести ціле число!
    в случае несуществующего индекса пишет в консоль - Такого індексу не існує
    :return:
    """
    list_of_integers = [0, 1, 2, 3, 4, 5]
    print('Task 3:')
    user_index = input('Enter element: ')
    try:
        print(list_of_integers[int(user_index)])
    except ValueError:
        print('Потрібно ввести ціле число!')
    except IndexError:
        print('Такого індексу не існує')


# Task 4
def taxi_driver_info():
    """
    Функция которая позволяет вывести значение ключа по данным словаря, где ключ вводится с клавиатуры
    в случа ошибки выводится в консоль - Такого ключа не існує
    в случае успеха - ввод нового ключа
    :return:
    """
    person_data = {"name": "Bolt", "age": 23, "gender": "male", "born_date": "06.07.1990"}
    user_key: str
    print('Task 4:')
    continue_programm = True
    while continue_programm:
        user_key = input('Enter key: ')
        try:
            print(person_data[user_key])
        except KeyError as e:
            print('Такого ключа не існує')
            continue_programm = True
        else:
            continue_programm = True
        print('Чекаю наступного ключа!')


func_additional_explore_error_in_divider()
func_divider()
index_printer()
taxi_driver_info()