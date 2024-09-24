immutable_var = (12345, 456.25, "Python", True, [3, 2.5, "str", False])
print("Кортеж -",immutable_var)
#immutable_var[0] = 54321    #- изменить нельзя, не изменяемый элемент кортежа
#immutable_var[1] = 54321    #- изменить нельзя, не изменяемый элемент кортежа
immutable_var[4][3] = True   #- изменить можно изменяемый элемент кортежа

mutable_list = [12345, 456.25, "Python", True, [3, 2.5, "str", False]]
print("Список до -", mutable_list)
mutable_list[0] = str(mutable_list[0])
mutable_list[4] = True
print("Список после -",mutable_list)
