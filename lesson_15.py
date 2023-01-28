'''
OOP
'''


class Light:
    '''
    Documentation
    '''

    # variables - define atributes/fields/properties
    on = bool()
    power = int()
    temperature = int()
    lamp_socket = str()

    # functtion - define methods
    # self - pointer with address of object

    def __init__(self, power: int, temperature: int, lamp_socket: str, on: bool = False):
        self.on = on
        self.power = 100
        self.temperature = 5600
        self.lamp_socket = 'jd27'
        print('Lamp constructor')

    def set_parameters(self, power: int, temperature: int, lamp_socket: str, on: bool = False):
        self.on = on
        self.power = power
        self.temperature = temperature
        self.lamp_socket = lamp_socket
        print('Lamp constructor')

    def show_parameters(self):
        print(f''
              f'On: {self.on}\n'
              f'Power: {self.power}\n'
              f'Temperature: {self.temperature}\n'
              f'Socket: {self.lamp_socket}'
              f'')

    def __str__(self):
        return 'On: {self.on}\nPower: {self.power}\nTemperature: {self.temperature}\nSocket: {self.lamp_socket}'

    def __int__(self):
        return self.power


obj = Light(100, 5600, 'jd27', True)

# добавление динамического свойства объекту
obj.my_new_data = "Tigidum"
# print(obj.my_new_data)
# obj.show_parameters()
print(obj)
