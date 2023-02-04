import os


class FileWorker:
    """
    Класс который позволяет вывести содержимое папки где находится исполняемый файл (папки 1го уровеня + файлы)
    Так же класс содержит метод который позволяет
    """
    __file_dir_tree_dict = dict()
    __path = str()
    __directories = list()
    __files = list()

    def __init__(self):
        self.__path = os.path.abspath(os.getcwd())
        self.__attributes_creator()
        self.__sorted_tree_dict(True)
        self.__sorted_tree_dict(False)

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

    def __sorted_tree_dict(self, sort_type: bool):
        file_dir_tree_dict_sorted = dict()
        file_dir_tree_dict_sorted['filenames'] = sorted(self.__files, key=lambda v: v.upper(), reverse=sort_type)
        file_dir_tree_dict_sorted['dirnames'] = sorted(self.__directories, key=lambda v: v.upper(), reverse=sort_type)
        if sort_type:
            print(f'Sorted by alphabetically:\n{file_dir_tree_dict_sorted}')
        else:
            print(f'Sorted by reverse\n{file_dir_tree_dict_sorted}')


object1 = FileWorker()
