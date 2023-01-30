# Task 1
import csv
import json
class Employee:
    """
    Documentation: класс с данными о конкретном человеке
    """
    firstname: str()
    lastname: str()
    age: int()
    email: str()
    skills: list()
    people_lang: list()
    coding_lang: list()

    export_json_file = 'files/hw15/employee.json'
    export_csv_file = 'files/hw15/employee.csv'
    import_json_file = 'files/hw15/import_employee.json'
    import_csv_file = 'files/hw15/import_employee.csv'

    def __init__(self,
                       firstname: str,
                       lastname: str,
                       age: int,
                       email: str,
                       skills: list,
                       people_lang: list,
                       coding_lang: list):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email
        self.skills = skills
        self.people_lang = people_lang
        self.coding_lang = coding_lang

    def write_to_csv(self):
        data = []
        with open(self.export_json_file, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for row in data:
                writer.writerow(row)

    def write_to_json(self):
        data = {'firstname': self.firstname,
                'lastname': self.lastname,
                'age': self.age,
                'email': self.email,
                'skills': self.skills,
                'people_lang': self.people_lang,
                'coding_lang': self.coding_lang}
        print(type(data))
        data = json.dumps(data, ensure_ascii = False) #второй аргумент - фикс записи кирилицы в читаемом виде
        print(type(data))
        with open(self.export_json_file, "w") as outfile:
            outfile.write(data)

    def create_employee_from_json(self):
        pass

    def create_employee_from_csv(self):
        pass

    def print_parameters(self):
        print(self.firstname)
        print(self.lastname)
        print(self.age)
        print(self.email)
        print(self.skills)
        print(self.people_lang)
        print(self.coding_lang)


empl1 = Employee('Ivasik', 'Telesik', 13, 'ivasik-telesik1732@izkurnanog.ua',
                 ['ходить', 'говорить', 'кодить'], ['Україньська', 'Англійська'], ['Python', 'C++', 'lisp'])

empl1.print_parameters()
empl1.write_to_json()