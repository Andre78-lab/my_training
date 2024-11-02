from math import pi, sqrt


class Figure:
    """Класс фигура"""
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = sides
        self.__color = color
        self.filled = True

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return r, g, b  # Цвет заведен корректно
        else:
            return self.__color  # Цвет заведен НЕ корректно

    def set_color(self, r, g, b):
        self.__color = self.__is_valid_color(r, g, b)
        return self.__color

    def __is_valid_sides(self, *new_sides):
        i_bool = False
        if len(new_sides) == self.sides_count:
            for i in new_sides:
                if isinstance(i, int) and i > 0:
                    i_bool = True  # изменение сторон
                else:
                    i_bool = False
        else:
            i_bool = False
        return i_bool

    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        return self.__sides


class Circle(Figure):
    """Класс окружность, наследует атрибуты класса Figure """
    sides_count = 1

    def __init__(self, color, *sides):
        if len(sides) == self.sides_count:
            super().__init__(color, *sides)
        else:
            super().__init__(color, 1)
        self.__radius = Figure.__len__(self) / (2 * pi)

    def get_square(self):
        return (self.__radius ** 2) * pi


class Triangle(Figure):
    """Класс треугольник произвольный, наследует атрибуты класса Figure """
    sides_count = 3

    def __init__(self, color, *sides):
        if len(sides) == self.sides_count:
            super().__init__(color, *sides)
        else:
            list_ = []
            for i in range(self.sides_count):
                list_.append(1)
            super().__init__(color, *list_)

    def get_square(self):
        p = Figure.__len__(self) / 2
        self.__sides = Figure.get_sides(self)
        if len(self.__sides) == 3:
            if self.prov_st():
                s = sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))
            else:
                return print(f"{self.__sides} не являются длинами сторон треугольника")
        else:
            s = f"Ошибка! Укажите длины трех стороны"
        return s

    def prov_st(self): #признак существования треугольника
        tt = True
        if self.__sides[0] + self.__sides[1] <= self.__sides[2]:
            tt = False
        if self.__sides[1] + self.__sides[2] <= self.__sides[0]:
            tt = False
        if self.__sides[2] + self.__sides[0] <= self.__sides[1]:
            tt = False
        return tt


class Cube(Figure):
    """Класс куб, наследует атрибуты класса Figure """
    sides_count = 12

    def __init__(self, color, *sides):
        list_ = []
        if len(sides) == 1:
            for i in range(self.sides_count):
                list_.append(*sides)
        else:
            for i in range(self.sides_count):
                list_.append(1)
        super().__init__(color, *list_)
        self.__sides = list_

    def get_volume(self):
        if len(self.__sides) == 12:
            return self.__sides[0] ** 3


tr = Triangle((12, 34, 23), 2, 3, 4)
print(tr.set_sides(4, 5, 8))
print(tr.get_square())

circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
