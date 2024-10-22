
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


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)





