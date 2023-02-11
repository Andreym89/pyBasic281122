class Vehicle:
    """
    Родительский класс описывающий транспортное средство
    """
    id_number = str()
    wheels_count = int()
    engine_power = int()
    max_speed = int()

    def __init__(self, id_number: str, wheels_count: int, engine_power: int, max_speed: int):
        self.id_number = id_number
        self.wheels_count = wheels_count
        self.engine_power = engine_power
        self.max_speed = max_speed

    def __str__(self):
        print(f'Id number: {self.id_number}\nWheels count: {self.wheels_count}\nEngine: {self.engine_power} hp\n'
              f'Max speed: {self.max_speed} km/h')


    new_car = Vehicle('32012rfd332', 4, 320, 280)