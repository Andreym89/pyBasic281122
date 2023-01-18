# Task_1

def read_txt_file(filename: str):
    with open(filename, 'rt') as file:
        data = file.read()
        return data
    return 0


def write_txt_file(filename: str, data) -> None:
    with open(filename, 'wt') as file:
        data = file.write(str(data))


def delete_some_symbols(text: str) -> str:
    gramar_list = ['.', ',', '!', '?', "'"]
    text = text.replace('\n', ' ')
    for i in range(0, len(gramar_list)):
        text = text.replace(gramar_list[i], '')
    return text


def word_cleaner(word: str) -> list:
    list_word_spec_chair = []
    return list_word_spec_chair


def censor_function(forbidden_word: str) -> str:
    """
    функция возвращает строку с подмененными центральными символами на *
    :param forbidden_word: само слово
    :return: обработанное слово
    """
    list = word_cleaner(forbidden_word)
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

    print(source_text_copy)
    for word in range(0, len(source_text_copy)):
        for f_word in range(0, len(forbidden_words)):
            if str(forbidden_words[f_word]) in source_text_copy[word].lower():
                source_text_copy[word] = censor_function(source_text_copy[word])

    source_text_copy = ' '.join(source_text_copy)
    print(source_text_copy)
    write_txt_file('files/testFileCensored.txt', source_text_copy)


list_of_forbidden_words = ['hello', 'world']
censored_text('files/testFile.txt', list_of_forbidden_words)


# Task_2


def words_count(text: str) -> None:
    source_text = delete_some_symbols(read_txt_file(text))
    source_text = source_text.split(sep=' ')
    words_count_var = len(source_text)

    for element in range(0, len(source_text)):
        source_text[element] = source_text[element].lower()

    source_text.sort()

    while '' in source_text:
        source_text.remove('')

    source_text_uniq_word = []
    source_text_uniq_word = list(set(source_text))
    source_text_uniq_word_dict = {}

    for uniq_elem in range(0, len(source_text_uniq_word)):
        uniq_word_counter = 0
        for i in range(0, len(source_text)):
            if source_text_uniq_word[uniq_elem] == source_text[i]:
                uniq_word_counter += 1
        source_text_uniq_word_dict[source_text_uniq_word[uniq_elem]] = uniq_word_counter

    print(source_text_uniq_word_dict)


words_count('files/someTextForCount.txt')