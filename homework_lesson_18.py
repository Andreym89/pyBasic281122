# Task 1
def print_green(skk): print("\033[92m{}\033[00m".format(skk))
def print_yellow(skk): print("\033[93m{}\033[00m".format(skk))


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
        return f'Vehicle class:\nId number: {self.id_number}\nWheels count: {self.wheels_count}\n' \
               f'Engine: {self.engine_power} hp\nMax speed: {self.max_speed} km/h'


class MotorCar(Vehicle):
    car_name = str()
    car_model = str()
    car_year_model = int()
    car_color = str()
    car_vin_code = str()
    car_number_of_seats = int()

    def __init__(self, car_name: str, car_model: str, car_year_model: int, car_color: str, car_vin_code: str,
                 car_number_of_seats: int, id_num: str, wheel_count: int, power: str, max_speed: int):
        self.car_name = car_name
        self.car_model = car_model
        self.car_year_model = car_year_model
        self.car_color = car_color
        self.car_vin_code = car_vin_code
        self.car_number_of_seats = car_number_of_seats
        self.id_number = id_num
        self.wheels_count = wheel_count
        self.engine_power = power
        self.max_speed = max_speed

    def __str__(self):
        return f'MotorCar class:\nCar name: {self.car_name}\nModel: {self.car_model}\nYear: {self.car_year_model}\n' \
               f'Color: {self.car_color}\nVin code: {self.car_vin_code}\n' \
               f'Number of seats: {self.car_number_of_seats}\nWheels count: {self.wheels_count}\n' \
               f'Engine: {self.engine_power} hp\nMax speed: {self.max_speed} km/h'


class Bus(Vehicle):
    bus_count_of_standing_places = int()

    def __init__(self, bus_name: str, bus_model: str, bus_year_model: int, bus_color: str,
                 vin_code: str, bus_number_of_seats: int, id_num: str, wheel_count: int,
                 power: str, max_speed: int, standing_places: int):
        self.car_name = bus_name
        self.car_model = bus_model
        self.car_year_model = bus_year_model
        self.car_color = bus_color
        self.car_vin_code = vin_code
        self.car_number_of_seats = bus_number_of_seats
        self.id_number = id_num
        self.wheels_count = wheel_count
        self.engine_power = power
        self.max_speed = max_speed
        self.bus_count_of_standing_places = standing_places

    def __str__(self):
        return f'Bus class:\nCar name: {self.car_name}\nModel: {self.car_model}\nYear: {self.car_year_model}\n' \
               f'Color: {self.car_color}\nVin code: {self.car_vin_code}\n' \
               f'Number of seats: {self.car_number_of_seats}\nWheels count: {self.wheels_count}\n' \
               f'Engine: {self.engine_power} hp\nMax speed: {self.max_speed} km/h\n' \
               f'Standing places: {self.bus_count_of_standing_places }'


class Bicycle(Vehicle):
    color = str()
    stype = str()

    def __init__(self, wheels_count: int, max_speed: int, color: str, bicycle_type: str):
        self.wheels_count = wheels_count
        self.max_speed = max_speed
        self.color = color
        self.stype = bicycle_type

    def __str__(self):
        return f'Bicycle class:\nWheels count: {self.wheels_count}\nMax speed: {self.max_speed} km/h\n' \
               f'Bicycle type: {self.stype}\nColor: {self.color}'


class MotorBike(Bicycle):
    def __init__(self, wheels_count: int, max_speed: int, color: str, bicycle_type: str, id_num: str, power: int):
        self.wheels_count = wheels_count
        self.max_speed = max_speed
        self.color = color
        self.stype = bicycle_type
        self.id_number = id_num
        self.engine_power = power

    def __str__(self):
        return f'Id num: {self.id_number}\nPower: {self.engine_power}\nWheels count: {self.wheels_count}\n' \
               f'Max speed: {self.max_speed} km/h\nBicycle type: {self.stype}\nColor: {self.color}'


class Truck(MotorCar):
    trailer_type = str()
    load_capacity = int()

    def __init__(self, car_name: str, car_model: str, car_year_model: int, car_color: str,
                 car_vin_code: str, car_number_of_seats: int, id_num: str, wheel_count: int,
                 power: str, max_speed: int, trailer_type:str, load_cap: int):
        self.car_name = car_name
        self.car_model = car_model
        self.car_year_model = car_year_model
        self.car_color = car_color
        self.car_vin_code = car_vin_code
        self.car_number_of_seats = car_number_of_seats
        self.id_number = id_num
        self.wheels_count = wheel_count
        self.engine_power = power
        self.max_speed = max_speed
        self.trailer_type = trailer_type
        self.load_capacity = load_cap

    def __str__(self):
        return f'MotorCar class:\nCar name: {self.car_name}\nModel: {self.car_model}\nYear: {self.car_year_model}\n' \
               f'Color: {self.car_color}\nVin code: {self.car_vin_code}\n' \
               f'Number of seats: {self.car_number_of_seats}\nWheels count: {self.wheels_count}\n' \
               f'Engine: {self.engine_power} hp\nMax speed: {self.max_speed} km/h\n' \
               f'Trailer type: {self.trailer_type}\nLoad capacity: {self.load_capacity} kg'


print_green('Object of parent class')
new_car = Vehicle('AE0000TO', 4, 107, 180)
print(new_car)

my_auto = MotorCar('ZAZ', 'Lanos', 2011, 'Blue', 'VDBWDEVEW', 5, 'AE0000TO', 4, 105, 180)
print_yellow('\nMotorCar is child of class Vehicle')
print(my_auto)

my_bus = Bus('Mercedes', 'Sprinter', 2008, 'White', 'VDBWDEVEWASDFA', 18, 'AE0000TO', 4, 105, 180, 12)
print_yellow('\nBus is child of class Vehicle')
print(my_bus)

my_bicycle = Bicycle(2, 35, 'Red', 'Mountain')
print_yellow('\nBicycle is child of class Vehicle')
print(my_bicycle)

my_truck = Truck('MAN', 'TGS NN', 2011, 'Grey', 'VDBWDEVEW', 2, 'AE0000TO', 4, 350, 150, "Trailer", 20000)
print_yellow('\nTruck is child of class Vehicle')
print(my_truck)


# Task 2
