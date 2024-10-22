class House:
    def __init__(self, name , number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        str_floors = f"{self.name} \n      Этажи: "
        for i in range(self.number_of_floors):
            str_floors = str_floors + " " + str(i+1)
        print(str_floors)
        if new_floor < 0 or new_floor > self.number_of_floors:
            print(f"Такого {new_floor} этажа не существует")
        else:
            print(f"Вы едите на {new_floor} этаж")
        print(" ")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))