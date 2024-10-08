def calculate_structure_sum(d_structure, *args):
    sum_all = 0
    for i in d_structure:
        if isinstance(i, dict):
            for j, k in i.items():
                sum_all = sum_all + calculate_structure_sum((j, k))
        elif isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            sum_all = sum_all + calculate_structure_sum(i)
        else:
            if isinstance(i, int):
                sum_all += i
            elif isinstance(i, str):
                sum_all += len(i)
    return sum_all


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

data_structure1 = [
    {'d': 1, 's': 1},
    {'a': 1, 'b': 1},
    (1, {'c': 1, 'd': 1}, [1, "a", 1, 1])
]

result = calculate_structure_sum(data_structure)
print(result)
result1 = calculate_structure_sum(data_structure1)
print(result1)
