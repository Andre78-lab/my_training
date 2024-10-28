

class Animal:
    """
    Класс млекопитающих
    """
    def __init__(self, name, alive = True, fed = False):
        self.name = name                                # название животного
        self.alive = alive                              # живое / не живое
        self.fed = fed                                  # накормленное / голодное

    def eat(self, food):
        if food.edible == False:
            print(f"'{self.name}' съел '{food.name}'")
            self.fed = True
        else:
            print(f"'{self.name}' не стал есть '{food.name}'")
            self.alive = False
        return self


class Plant:
    """
    Класс растений
    """
    def __init__(self, name, edible = False):
        self.name = name                               # название растения
        self.edible = edible                           # съедобное / ядовитое

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    def __init__(self, name):
        self.name = name
        self.edible = True              # Ядовитое

class Fruit(Plant):
    pass

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)


