# Files
'''
with open('files/testFile.txt', 'wt') as file: # 'at' - добавить к концу файла еще данные если будут
    for i in range(0, 4):
        file.write('Hello world\n')

li = ['123', 'qwe', '456']

with open('files/testFile.txt', 'at') as file:
    file.writelines([i+'\n' for i in li])


with open('files/testFile.txt', 'rt') as file:
    result = file.read()
    print(result)


with open('files/testFile.txt', 'rt') as file:
    result = file.read(14)
    print(result)


with open('files/testFile.txt', 'rt') as file:
    result = file.readline()
    print(result)


with open('files/testFile.txt', 'rt') as file:
    result = file.readlines()
    print(result)


def read_txt_file(filename: str):
    with open(filename, 'rt') as file:
        data = file.read()
        return data
    return 0


def write_txt_file(filename: str, data) -> None:
    with open(filename, 'wt') as file:
        data = file.write(str(data))


text = read_txt_file('files/testFile.txt')
if text != 0:
    print(text)
'''


# Task_1

def read_txt_file(filename: str):
    with open(filename, 'rt') as file:
        data = file.read()
        return data
    return 0


def write_txt_file(filename: str, data) -> None:
    with open(filename, 'wt') as file:
        data = file.write(str(data))


def censor_function(forbidden_word: str) -> str:
    """
    функция возвращает строку с подмененными центральными символами на *
    :param forbidden_word: само слово
    :return: обработанное слово
    """

    if len(forbidden_word) > 2:
        star_count = len(forbidden_word) - 2
        forbidden_word = forbidden_word[0] + '*' * star_count + forbidden_word[len(forbidden_word) - 1]
    return forbidden_word


def censored_text(text: str, forbidden_words: list) -> None:
    """
    Функция цензор, на вход функция получает имя файла и список слов для замены. В результате ее работы создается
    файл, в котором слова из списка заменены шаблоном(звездочками)
    :param text: ссылка на файл TXT где нужно найти заменить слова
    :param forbidden_words: Слова для замены в виде списка
    :return:
    """
    source_text = read_txt_file(text)
    source_text_copy = source_text.split(sep=' ')

    for word in range(0, len(source_text_copy)):
        for f_word in range(0, len(forbidden_words)):
            if source_text_copy[word].lower() == str(forbidden_words[f_word]):
                source_text_copy[word] = censor_function(source_text_copy[word])

    source_text_copy = ' '.join(source_text_copy)
    print(source_text_copy)
    write_txt_file('files/testFileCensored.txt', source_text_copy)


list_of_forbidden_words = ['hello', 'world']
censored_text('files/testFile.txt', list_of_forbidden_words)

# Task_2
