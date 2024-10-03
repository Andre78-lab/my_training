import random

stone_1 = random.randint(3,20)
print(f'Первое поле, камень {stone_1}')
str_i = "Пары чисел для второго поля: "
for i in range(1, int(stone_1/2)+1):
    for j in range(i+1, stone_1):
        if stone_1 % (i+j) == 0:
            str_i += f' {i} и {j}, '

print(str_i[:-2])