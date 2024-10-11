from fake_math import divide as f_divide
from true_math import divide as t_divide

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

rez1 = f_divide(a, b)
rez2 = t_divide(a, b)
print(f' Результат деления {a} на {b} через fake_math = {rez1}')
print(f' Результат деления {a} на {b} через true_math = {rez2}')


result1 = f_divide(69, 3)
result2 = f_divide(3, 0)
result3 = t_divide(49, 7)
result4 = t_divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)