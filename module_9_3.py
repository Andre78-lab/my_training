
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']


first_result = (abs(len(x[0])-len(x[1])) for x in list(zip(first, second)) if (len(x[0]) - len(x[1])) != 0)

second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))