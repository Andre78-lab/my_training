def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(40203)
result2 = get_multiplied_digits(4)
result3 = get_multiplied_digits(10000100001011111110011)
result4 = get_multiplied_digits(123456789)

print(result)
print(result2)
print(result3)
print(result4)
