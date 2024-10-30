class Horse:
    """    Класс описание лошади    """

    def __init__(self, *args):
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__(*args)

    def run(self, dx):  # Изменение дистанции
        self.x_distance += dx


class Eagle:
    """    Класс описание орла    """

    def __init__(self, *args):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):  # Изменение высоты
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    """    Класс пегаса наследует от Horse и Eagle (в таком порядке)   """

    def __init__(self, *args):
        super().__init__(*args)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


#print(Horse.mro())
#print(Eagle.mro())
#print(Pegasus.mro())

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
