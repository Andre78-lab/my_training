import inspect
from inspect import signature
from pprint import pprint

import requests
from traitlets import ObjectName

class MyClassTest:
    a = 5
    b = 6
    def __init__(self, str_1, int_2):
        self.str_1 = str_1
        self.int_2 = int_2
        self.intr = 5
    def test_f(self):
        return print("Тест")



def  introspection_info(obj):
    info_obj = {} #спр. об объекте
    metod_obj = [] # список методов
    print(f'\nОбъект: {obj} ---   тип: {type(obj)}', "-"*20)
    #Получаем тип объекта
    info_obj['type'] = type(obj)
    #Получаем список атрибутов
    info_obj['attributes'] = dir(obj)

    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        if callable(attr):
            metod_obj.append(attr_name)
    #Добовляем методы
    info_obj['methods'] = metod_obj
    #Узнаем из какого модуля
    info_obj['module'] = inspect.getmodule(obj)
    # Вытаскиваем параметры у функций или классов
    if inspect.isfunction(obj) or inspect.isclass(obj):
        signature_obj = inspect.signature(obj)
        param_list = []
        for p_name, param in signature_obj.parameters.items():
            param_list.append([param.name, param.default])
        info_obj['signature'] = param_list

    return info_obj

info = introspection_info(MyClassTest)
print()
pprint(info)

info = introspection_info(123)
print()
pprint(info)

info = introspection_info('String')
print()
pprint(info)

info = introspection_info(ObjectName)
print()
pprint(info)

obj_class = MyClassTest
info = introspection_info(obj_class.test_f)
print()
pprint(info)

