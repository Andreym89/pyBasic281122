'''
ооп - инкапсуляция и наследование
'''


class User:

    # __ перед свойством - дедлаем его скрытым(private)
    # для доступа к ним нужны отдельные методы

    __name = str()
    __age: int = int()

    def __init__(self, name: str, age: int):
        self.__name = name
        self.set_age(age)

    def __str__(self):
        return f'Name: {self.__name}, age: {self.__age}'

    def set_age(self, age: int):
        if 0 <= age < 200:
            self.__age = age

    # методы которые работают с приватными свойствами - аксцессоры
    # методы меняющие приватные свойства - сеттеры(мутаторы)
    # методы возвращающие приватные свойства - геттеры
    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    # аннотации атрибутов - позволяет получать доступ к приватным свойствам через псевдоним
    # технически это происходит через метод
    # для создания аннотации исподльзуется декоратор @property


    # аннотации

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        if 0 <= age < 200:
            self.__age = age

    @age.getter
    def age(self):
        return self.__age

obj1 = User('Vasya', 92)
    # print(obj1)
    # obj1.set_age(230)
    # print(obj1)
    # print(obj1.get_age())

print(obj1.age)
obj1.age = 101
print(obj1.age)
print(obj1.age)

