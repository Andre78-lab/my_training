def type_str(n):
    if type(n) == int or type(n) == float:
        return str(n)
    else:
        return n

def add_everything_up(a, b):
    try:
        result = a + b
    except TypeError:
        a = type_str(a)
        b = type_str(b)
        result = a + b
    return result

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))