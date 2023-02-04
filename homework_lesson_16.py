import os


class FileWorker:
    """
    Класс который позволяет вывести содержимое папки где находится исполняемый файл (папки 1го уровеня + файлы)
    Так же класс содержит публичный метод который позволяет вывести отсортированный список файлов и папок

    sorted_tree_dict(bool) - метод позволяющий вывести отсортированное содержимое папки:
        True - алфавитный порядок
        False - обратный порядок
    update_tree_dict(str) - метод позволяющий добавить новый элемент в список содержимого папки, если в str присутствует
    '.'(точка) - то метод считает это файлом, иначе папкой
    """
    __file_dir_tree_dict = dict()
    __path = str()
    __directories = list()
    __files = list()

    def __init__(self):
        self.__path = os.path.abspath(os.getcwd())
        self.__attributes_creator()

    def print_file_dir_tree_dict(self):
        print(self.__file_dir_tree_dict)

    def __attributes_creator(self):
        elements = os.listdir(self.__path)

        for item in elements:
            path_to_element = os.path.join(self.__path, item)
            if os.path.isdir(path_to_element):
                self.__directories.append(item)
            elif os.path.isfile(path_to_element):
                self.__files.append(item)

        self.__file_dir_tree_dict['filenames'] = self.__files
        self.__file_dir_tree_dict['dirnames'] = self.__directories

        print(f'Content of original dictionary:\n{self.__file_dir_tree_dict}')

    def sorted_tree_dict(self, sort_type: bool):
        """
        Метод позволяющий отсортировать сгруппированное содержимое папки по типу

        :param sort_type: тип сортировки True - алфавитный порядок, False - обратный порядок
        :return:
        """
        sort_type = not sort_type
        file_dir_tree_dict_sorted = dict()
        file_dir_tree_dict_sorted['filenames'] = sorted(self.__files, key=lambda v: v.upper(), reverse=sort_type)
        file_dir_tree_dict_sorted['dirnames'] = sorted(self.__directories, key=lambda v: v.upper(), reverse=sort_type)
        if not sort_type:
            return f'Sorted by alphabetically:\n{file_dir_tree_dict_sorted}'
        else:
            return f'Sorted by reverse\n{file_dir_tree_dict_sorted}'

    def update_tree_dict(self, new_elem: str):
        """
        метод принимающий название нового элемента, если в нем есть '.' значит это файл, иначе - папка
        :param new_elem:
        :return:
        """
        if new_elem.rfind('.') == -1:
            print(f'{new_elem} - this elem is dictionary')
            self.__file_dir_tree_dict['dirnames'].append(new_elem)
        else:
            print(f'{new_elem} - this elem is file')
            self.__file_dir_tree_dict['filenames'].append(new_elem)
        return f'Updated dictionary\n{self.__file_dir_tree_dict}'


# Task 1
object1 = FileWorker()

# Task 2
print(object1.sorted_tree_dict(True))  # сортировка по алфавиту
print(object1.sorted_tree_dict(False))  # сортировка в обратном порядке

# Task 3
object1.update_tree_dict('new_dir_1')  # добавляем папку в список содержимого папки
object1.update_tree_dict('new_file_1.py')  # добавляем файл в список содержимого папки
object1.print_file_dir_tree_dict()
