# Task 1
import csv
import json
class Employee:
    """
    Documentation: класс с данными о конкретном человеке, в котором 2 метода записи в файлы json и csv
    """
    firstname: str()
    lastname: str()
    age: int()
    email: str()
    skills: list()
    people_lang: list()
    coding_lang: list()

    export_json_file_path = 'files/hw15/employee.json'
    export_csv_file_path = 'files/hw15/employee.csv'

    def __init__(
            self,
            firstname: str,
            lastname: str,
            age: int,
            email: str,
            skills: list,
            people_lang: list,
            coding_lang: list
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email
        self.skills = skills
        self.people_lang = people_lang
        self.coding_lang = coding_lang

    def write_to_csv(self):
        """
        :return: fill data in csv file in files/hw15/employee.csv
        """
        data = {
             'firstname': self.firstname,
             'lastname': self.lastname,
             'age': str(self.age),
             'email': self.email,
             'skills': self.skills,
             'people_lang': self.people_lang,
             'coding_lang': self.coding_lang
        }
        with open(self.export_csv_file_path, 'wt') as file:
            for key in data.keys():
                file.write("%s, %s\n" % (key, data[key]))

    def write_to_json(self):
        """
        :return: fill data in json file in files/hw15/employee.json
        """
        data = {'firstname': self.firstname,
                'lastname': self.lastname,
                'age': self.age,
                'email': self.email,
                'skills': self.skills,
                'people_lang': self.people_lang,
                'coding_lang': self.coding_lang}
        data = json.dumps(data, ensure_ascii = False) #второй аргумент - фикс записи кирилицы в читаемом виде
        with open(self.export_json_file_path, "w") as outfile:
            outfile.write(data)

    def __str__(self):
        print(self.firstname)
        print(self.lastname)
        print(self.age)
        print(self.email)
        print(self.skills)
        print(self.people_lang)
        print(self.coding_lang)


empl1 = Employee('Ivasik', 'Telesik', 13, 'ivasik-telesik1732@izkurnanog.ua',
                 ['ходить', 'говорить', 'кодить'], ['Україньська', 'Англійська'], ['Python', 'C++', 'lisp'])
empl1.write_to_json()
empl1.write_to_csv()