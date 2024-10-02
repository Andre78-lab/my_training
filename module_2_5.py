def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


n_ = int(input('Введите число столбцов в матрице - '))
m_ = int(input('Введите число строк в матрице - '))
value_ = int(input('Введите значение элементов в матрице - '))
result = get_matrix(n_, m_, value_)
print(result)

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
