class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message =  message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message =  message 

class Car:
    def __init__(self, model, vin_number, numbers):
        self.model = model
        if self.__is_valid_vin(vin_number):
            self.__vin = vin_number
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self,vin_num):
        if not isinstance(vin_num, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif not (1000000 <= vin_num <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True
    def __is_valid_numbers(self,num):
        if not isinstance(num, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(num) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')