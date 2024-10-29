

class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    s_owner = 0
    def __init__(self, owner: str, __model: str, __color: str, __engine_power: int):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(f"\033[34m{self.get_model()} \n{self.get_horsepower()} \n{self.get_color()}")
        if self.s_owner < 2:
            print(f"\033[34mВладелец: {self.owner}")
        else:
            print(f"\033[34mВладелец: \033[32m{self.owner}")

    def set_color(self, new_color):
        global s_owner
        self.s_owner += 1
        color_ = False

        for i_color in self.__COLOR_VARIANTS:
            if new_color.lower() == i_color.lower():
                self.__color = f'\033[32m{new_color}'
                color_ = True
                break
        if color_ == False:
            print(f"\033[31mНельзя сменить цвет на {new_color}.")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()












