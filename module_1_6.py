from cgi import print_environ_usage

my_dist = {'Вова': 2002, 'Саня': 2005, 'Лена': 1977, 'Коля': 1982}
print(my_dist)
print(my_dist.get('Вова', "Такого ключа нет"))
print(my_dist.get('Наташа', "Такого ключа нет"))
my_dist.update( {'Саша':2006, 'Наташа':1975})
a = my_dist.pop('Коля')
print(a)
print(my_dist)

my_set = {1, 2, 1, 2, 1, 2, 3, 4, 5, True, False, True, (1,2), (2,3), (1,2), "str" , False, "str"}
print(my_set)
my_set.add(78)
my_set.add("str2")
my_set.remove(False)
print(my_set)