'''
OOP inhert
'''

class Person:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f'Name: {self.__name}.'


# obj = Person('Taras')
# print(obj)


class Employee(Person):
    def __init__(self, name: str, position: str):
        self.__position = position
        super().__init__(name)

    @property
    def position(self):
        return self.__position

    def work(self):
        print(f'{self.name} {self.name} make work')

    def __str__(self):
        return f'Name: {self.name}. Position: {self.position}.'


class Employee_with_salary(Employee):
    def __init__(self, name: str, position: str, salary: int):
        self.salary = salary
        super().__init__(name, position)

    def __str__(self):
        return super().__str__() + f' Salary: {self.salary}'


obj = Employee_with_salary('Taras', 'CEO', 100000)
# obj = Person('Taras')
# print(obj.position)
print(obj)
# obj.work()
print(Employee_with_salary.mro())


'''
Множественное наследование
'''

class Roga:
    def __init__(self, size: str):
        self.__size = size

    @property
    def size(self):
        return self.__size


class Kopyta:
    def __init__(self, color: str):
        self.__color = color

    @property
    def color(self):
        return self.__color


class Los(Roga, Kopyta):
    def __init__(self, roga_size: str, kopyta_color: str):
        super().__init__(roga_size)
        super().__init__(kopyta_color)

    def __str__(self):
        pass


obj2 = Los('Big', 'Brown')
print(obj2)