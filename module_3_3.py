def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(2, 5, "str")
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [True, 4, [1,2,3]]
values_dict = {'a': True, 'b': 5, 'c': (1,2,3)}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [{7, 8, 9, 10}, "Str"]
print_params(*values_list_2, 42)

